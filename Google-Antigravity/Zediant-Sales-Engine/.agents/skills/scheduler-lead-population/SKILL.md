---
name: scheduler-lead-population
description: "Zediant's Scheduler 1 — the daily lead factory. Orchestrates an Apollo search with verified email enforcement across all five campaigns (C1-C5), Zoho dedup, qualification, campaign selection, enrichment, email personalization for every survivor, batched Zoho write (Social Lead ID validated against the Apollo handoff), and a Cliq summary of counts/funnel/campaign mix only — no individual lead names or emails. Runs daily to populate Zoho with qualified, scored, personalized leads awaiting BDM approval. Quality over quota — 7–10 high-intent qualified leads per daily run during conservative deliverability ramp-up (up to 80 production maximum at full scale). Routes software dev shops/consultancies to Partner/Overflow. Use: 'Run Scheduler 1', 'source leads from Apollo', 'populate today's leads'."
---

# Scheduler 1 — Lead Population Orchestrator (v5.2)

Daily sourcing workflow: pull a candidate pool from Apollo with verified emails only, screen it cheaply, spend credits only on survivors, personalize email content for every survivor, and write to Zoho for BDM review.

## The core operating principle

Think like a senior salesperson deciding who's worth a BDM's time today, not like a database scraper filling a quota.

**Ramp-up production target is 7–10 high-intent qualified leads per daily run** (aligned with Zediant's single-mailbox deliverability limit: 25–35 emails/day total, 300–480s randomized spacing, 0 tracking pixels, strict email verification). Sourcing targets 25–50 raw verified candidates to find the best 7–10 prospects. The long-term production ceiling remains up to 80 qualified prospects per run once multiple warmed sending mailboxes/domains are activated. Never loosen a filter, lower a score threshold, or pad a category to reach a round number — a shortfall reported honestly is a successful run; a padded batch that gets rejected at BDM review is not. Reporting "only 6 genuinely qualified today" is the correct outcome when that's what's true, not a failure to explain away.

**A shortfall is only acceptable when it's genuine.** A written batch that's small relative to a large available Apollo pool is a different problem from a genuinely thin market, and the two must not be reported the same way. See Step 0 and `apollo-search-builder`'s Volume Diagnostic — check pipeline mechanics and pagination before concluding a market segment is simply thin.

## The one thing to understand before anything else

**Screening is free; enrichment is not.** `search_people` (with `contact_email_status: ["verified"]`) returns name, title, company, industry, headcount, location, and technology tags at no credit cost — it just withholds the email address. Qualification, ICP scoring, and campaign selection need none of that withheld data. So every gate runs *before* enrichment, and only leads that survive all of those gates ever cost a credit. PTB Score (Initial Buying Signal, 0–100) is calculated after qualification and before CRM write; it is a prioritization signal, not a qualification gate. No second PTB score exists in Scheduler 1.

The old ordering enriched all leads up front and then discarded the rejected ones. That spent credits on leads the workflow was about to throw away. Never restore that ordering.

## What this skill does and does not do

**Does:** source a properly-filtered candidate pool (enforcing `contact_email_status: ["verified"]`) across all five campaigns, screen, score, route, enrich survivors, personalize email content for every survivor, write to Zoho, notify Cliq.

**Does not:** approve leads, push to Saleshandy, activate campaigns, send email, or execute LinkedIn outreach (current execution scope is 100% focused on email deliverability; LinkedIn outreach tasks are postponed). Approval is a human action in Zoho; distribution is Scheduler 2. Scheduler 1 calculates the single numeric 0–100 PTB Score (Initial Buying Signal) through `ptb-scoring`. There is no separate post-engagement PTB model.

---

**Active pipeline:** Discovery (`contact_email_status: ["verified"]`) → Deduplication → Qualification → ICP Score → PTB Score (Initial Buying Signal) → Campaign Selection → Personalization → CRM (Zoho write) → BDM Approval. PTB is calculated once before outreach. Scheduler 1 never creates a second PTB score.

---

## The approval gate — `Lead_Status`

`Lead_Status` (standard Zoho picklist) is the single field controlling pipeline state. `Qualifying_Status` is **not** used by this workflow, and as of August 8, 2026 the field has been deleted from Zoho entirely — if you see it referenced anywhere, that reference is stale.

| Value | Written by | Meaning |
|---|---|---|
| `New Lead` | **Scheduler 1** | Sourced, scored, awaiting BDM review |
| `Approved for Outreach` | BDM, manually in Zoho | Cleared to enter a campaign |
| `Outreach Scheduled` | Scheduler 2 | Pushed to Saleshandy |
| `Engaged` | BDM, manually after a reply | Prospect responded |
| `Rejected` | BDM, manually | Not pursuing |

**Scheduler 1 writes `New Lead` and NOTHING ELSE.** It never writes `"Pre-Qualified"`, `"Active"`, or any other value — that transition is the entire point of the review gate.

---

## WORKFLOW

### Step 0 — Source a candidate pool with verified emails across campaigns

Delegate sourcing to `apollo-search-builder`'s Candidate Pool Strategy. Enforce `contact_email_status: ["verified"]` on all searches.
- During ramp-up: retrieve **25–50 raw verified candidates** across the day's rotated searches.
- At full scale: retrieve 300–500 raw candidates across rotated searches.
This costs zero credits; the funnel from here to a written lead is what determines quality.

**Source across C1–C5, not just C1/C2, unless the user names a specific campaign.** Follow `apollo-search-builder`'s Campaign Coverage Rotation section for the default 25/25/15/25/10 target-share split across all five campaigns, scaled proportionally down for a 7–10 ramp-up run rather than collapsed to two campaigns. If the user does name a specific campaign, source only that one.

**This pooling must use `search_people` with `contact_email_status: ["verified"]` and paginate if needed.** Confirm the raw pool produced meets the target before moving to Step 1.

### Steps 1-6 — screen, qualify, campaign select, enrich survivors

Execute the specialist skills in sequence. `lead-qualification` owns the qualification verdict and ICP scoring. `ptb-scoring` then calculates the numeric 0–100 PTB Score (Initial Buying Signal) from pre-engagement evidence. `campaign-selection` consumes that score as its Buying Signal factor. `email-personalization` creates the outreach copy. `crm-update` performs the Zoho write. Three additions from the current sourcing motion apply within these steps:

- **Zoho exclusion is permanent.** Apply `apollo-search-builder`'s full 5-step dedup cascade (Apollo Person ID → Email → LinkedIn URL → domain+name → company+name) before spending anything on a candidate. A person or company already in Zoho under this workflow is excluded from that point forward.
- **Signal Enrichment Pass.** Run `apollo-search-builder`'s Signal Enrichment Pass on ICP-surviving candidates to fill real Buying Signal and Technology Fit data — as raw evidence carried on the lead record — rather than defaulting to Unknown. This raw evidence feeds ICP Score, campaign fit, and the pre-outreach PTB score calculated by `ptb-scoring`.
- **Partner / Engineering Overflow routing.** If screening or qualification surfaces a candidate whose own business is software development, IT consultancy, or managed technology services, do not route it into C1–C5 by default. Classify it separately as Partner/Overflow per `apollo-search-builder` Step 6a and carry that classification through into the Zoho write (Step 8) rather than silently dropping it or silently merging it into a standard campaign count.

**Capture `apollo_person_id` for every candidate at Step 0/enrichment time and carry it forward as its own field through every stage** — per `apollo-search-builder`'s Apollo Person ID Capture requirement. This is what Step 8 below writes to `leadchain0__Social_Lead_ID`; don't leave this to be reconstructed at write time, since by then the original search/enrichment response may no longer be in context.

### Step 6a — Business Challenges and Case Study (enrichment, before personalization)

Both fields below are governed by `zediant_outreach_natural_language_blacklist.md` — `lead-qualification`'s Step 6 reads it before authoring the Business Challenges finding, and `email-personalization`'s Step 0 reads it before drafting Case Study (and Email Personalised Opening / Email Pain Points in Step 7 next). This step doesn't re-run the blacklist check itself; it's carrying forward output that was already produced under that rule.

Two more fields now exist on every surviving lead, and they belong at enrichment time, not bolted on during outreach copywriting:

- **Business Challenges** — this is not new work. `lead-qualification`'s Step 6 already produces this finding for every Qualified lead (open roles, roadmap slippage, integration work, outages, stated capacity constraints). Carry that finding forward as-is, preserving whatever hedged/inferred phrasing `lead-qualification` used — don't firm it up into a stated fact on the way through.
- **Case Study** — the single most relevant approved Zediant case study for this lead, selected using Company/Industry/Business Challenges/Selected Campaign/relevant Zediant service, in that order of relevance (Business Challenges should drive which case study fits, not just shared industry). **Only pull from approved case study content that actually exists** — never invent a customer, a metric, a technology, or an outcome. If nothing approved genuinely fits, leave it blank; that is a normal, expected outcome for this run, not a defect.

Both values need to exist before Step 7 generates outreach copy, since Business Challenges is the primary input to Email Personalised Opening and Email Pain Points, and Case Study (when one exists) is available to both channels.

### Step 7 — Personalize: Email and LinkedIn for every qualified survivor

Run `email-personalization` on every lead that survived qualification and campaign selection. PTB Score (Initial Buying Signal) is not a gate here; it is a prioritization input. PTB is already available from the scoring step and must not block personalization. That skill now produces, per lead:

- `Email_Personalised_Opening` and `Email_Pain_Points` — every survivor gets these, built primarily from Business Challenges
- The merged LinkedIn Message & Follow-up content — **as of `email-personalization` v2.3, generated for every survivor, not just leads marked `Ready to Connect`** — built from Business Challenges, Case Study (if one exists), campaign, and buying intent — never a copy of the email content
- A `LinkedIn Status` decision (`Ready to Connect` or `Not Required`) — ranked across the **whole batch**, not per-lead in isolation, targeting approximately the top quarter of the written batch on quality, not quota. **This is now a priority/sequencing flag for the manual LinkedIn process, not a gate on whether LinkedIn content exists** — see `email-personalization` Section 4

Case Study is used where it genuinely fits the email sequence or the LinkedIn message — never force it into every touch just because a value exists in the field.

Don't run LinkedIn selection lead-by-lead as each one finishes qualification — batch it, since the ranking is relative to the rest of today's cohort. Hold personalization output for all survivors, then run the LinkedIn Selection priority ranking once across the full set before Step 8. LinkedIn *content* generation, however, doesn't need to wait on the ranking — every survivor gets it regardless of where they land in the ranking.

Order the final written batch using the existing qualification result, ICP Score, PTB Score (Initial Buying Signal), campaign fit, and evidence quality. Do not invent a new score or threshold. Use the single PTB Score (Initial Buying Signal) because it is the only PTB score in the current workflow. If a prioritization order is needed, use the existing PTB Score (Initial Buying Signal) alongside ICP/qualification evidence, never a combined score.

### Step 8 — Write to Zoho in one batch

Single `upsertRecords` call, `duplicate_check_fields: ["Email"]`, max 100 records per call.

**🔴 CRITICAL — MANDATORY:**
- `Lead_Status` field MUST ALWAYS be written as exactly `"New Lead"`
- NEVER write `"Pre-Qualified"`, `"Active"`, `"Pending Review"`, or any other value
- The only valid value at this step is `"New Lead"`
- `Rating` (LinkedIn Status) MUST be exactly `"Ready to Connect"` or `"Not Required"` — never an execution-stage value like `"Connection Sent"`
- **`LinkedIn_Message` must be written whenever `email-personalization` produced content for the lead — as of v4.6, this is every survivor, independent of the `Rating` value written alongside it.** Do not omit it for `Rating: "Not Required"` leads; that was the pre-v4.6 behavior and it is now reversed
- **`leadchain0__Social_Lead_ID` must be written whenever an `apollo_person_id` was captured for the lead upstream.** If a lead is Apollo-sourced but this value is missing, don't write it blank silently — flag it in the run report per `crm-update`'s Social Lead ID — write rules, since a live run previously surfaced this field coming back blank across a batch of genuinely Apollo-sourced leads
- `Lead_Campaign_Category` takes C1–C5 only — never the daily sourcing-rotation labels ("Product Engineering," "Engineering Expansion," etc.) and never the legacy List A-E values
- Any other value on these fields will break the BDM approval gate, Scheduler 2 filtering, or the manual LinkedIn process

```json
{
  "module": "Leads",
  "duplicate_check_fields": ["Email"],
  "data": [{
    "First_Name": "...",
    "Last_Name": "...",
    "Email": "...",
    "Company": "...",
    "Designation": "...",
    "Industry": "...",
    "No_of_Employees": 16,
    "Country": "...", "State": "...", "City": "...",
    "Lead_Source": "Web Research",
    "Lead_Status": "New Lead",
    "Skype_ID": "78",
    "Twitter": "74",
    "Lead_Campaign_Category": "C1 - AI-Enabled Product Engineering",
    "Business_Challenges": "...",
    "Case_Study": "...",
    "Email_Personalised_Opening": "...",
    "Email_Pain_Points": "...",
    "Rating": "Not Required",
    "LinkedIn_Message": "CONNECT:\n...\n\nFOLLOW-UP:\n...",
    "leadchain0__Social_Lead_ID": "...apollo_person_id...",
    "LinkedIN_Link": "https://linkedin.com/in/...",
    "Description": "[Excellent] Series A SaaS founder, funding 4mo. Campaign: C1 - AI platform scaling matches product-engineering angle.\nTech stack: Cloud Infrastructure, AI/NLP (Strong fit)\nPersonalization angle: Engineering team growth driving capacity pressure on product roadmap."
  }]
}
```

Note the example above deliberately shows `Rating: "Not Required"` **with `LinkedIn_Message` still populated** — this is the corrected v4.6 behavior, not an inconsistency. A `Ready to Connect` lead's payload looks identical except for the `Rating` value; the presence of `LinkedIn_Message` no longer depends on which one is written.

**Score fields:** `ICP_Score` and `PTB_Score` custom fields are deleted. ICP Score goes to `Skype_ID` as a plain text string, e.g. `"78"` — not a JSON number, the field is `text` type. `Twitter` holds the active buying-propensity score. During Scheduler 1, `ptb-scoring` calculates the numeric PTB Score (Initial Buying Signal, 0–100) and `crm-update` writes that score to `Twitter`. **The value written to `Twitter` must be the numeric score as text, such as `"74"`** (single token, no space, no `/`). `ptb-scoring` is the only skill authorized to calculate the number; `crm-update` writes it. Per `GEMINI.md` Section 15A, this is the single authoritative PTB score; there is no second post-engagement score and no overwriting of this score. This field mapping was verified with a real write/read/delete test against a throwaway record, not assumed from the field label.

`LinkedIn_Follow_up` no longer exists as a separate field. Write both the connection message and the follow-up into `LinkedIn_Message` using the CONNECT / FOLLOW-UP two-part format shown above.

For a Partner/Overflow-classified candidate that clears the bar for tracking (rare — most should simply not be written if they aren't a fit for anything), note the classification explicitly in `Description` (e.g., `"[Partner/Overflow] Software dev shop, potential subcontracting fit, not routed to C1-C5"`) rather than leaving it looking like a standard end-client lead. Default to not writing Partner/Overflow candidates into the daily batch at all unless there's a specific reason to track them — this workflow's job is end-client prospecting, and a parallel Partner list is a separate, not-yet-built concern.

**Fields this skill must NOT write:**

| Field | Why |
|---|---|
| `Qualifying_Status` | Deleted from Zoho as of August 8, 2026. `Lead_Status` is the gate |
| `Scoring_Reason`, `Technology_Stack`, `Personalization_Notes` | Deleted from Zoho the same day, to make room for the four LinkedIn-outreach fields. Their content now lives in `Description` (see the payload example above) |
| `ICP_Score`, `PTB_Score` | Deleted today. Use `Skype_ID`/`Twitter` instead - see above |
| `LinkedIn_Follow_up` | Deleted today. Merged into `LinkedIn_Message` - see above |
| `Lead_Status_Modified_Time` | System-managed by Zoho |
| `Rating` set to anything other than `Ready to Connect` / `Not Required` | Execution-stage LinkedIn values belong to the human running LinkedIn outreach manually, never to this skill |
| Any new field for Apollo Organization ID, import date/batch ID, Trigger Signal, Technology Fit, or Prospecting Priority | No Zoho custom-field slot exists for these (the one remaining slot stays reserved per the resolved design decision below). Fold all of this into `Description` as structured text instead of inventing a field |

`Skype_ID` no longer functions as a Saleshandy-campaign-activation gate - that role is gone now that the field holds ICP Score. `saleshandy-distribution` uses `Lead_Status` alone for its push-eligibility check, so this skill doesn't need to leave `Skype_ID` empty on purpose anymore.

`Description` gives the BDM full context in the list view without opening each record - keep it populated, it is what makes a 50-lead review tractable. Business Challenges and Case Study now live in their own fields, so `Description` only needs a one-line pointer to them, not the full text, but should still carry the tech-stack and Partner/Overflow notes shown above since those have no dedicated field.

**Error handling:** a picklist-value rejection means Zoho Setup is out of sync with this skill. Surface the exact Zoho error naming the field and value. Never silently substitute a different value to make the write succeed. If `leadchain0__Social_Lead_ID` writes come back empty across a noticeable share of a batch despite Apollo sourcing, treat that as a pattern worth investigating in Step 0's capture, not a per-lead curiosity — see `apollo-search-builder`'s Apollo Person ID Capture and `crm-update`'s Escalation entry for this exact symptom.

### Step 9 — Cliq summary — SUMMARY COUNTS, FUNNEL, AND AGGREGATES ONLY, NO PER-LEAD DETAIL

Post to channel `P1064180000001095002` (#Z-Outreach-Auto-Update).

**🔴 Completion sequencing (MANDATORY):** This step is the final mandatory action of the run, not an optional wrap-up — the run is not complete until it has actually executed. Required order: Zoho CRM write (Step 8) → compose the aggregate summary below → post it to #Z-Outreach-Auto-Update → verify the Cliq tool response indicates success (see below) → only then declare the Scheduler 1 run complete. A chat-only summary back to the requester, however detailed, is a supplement to this step and never a substitute for it — do not stop at the Zoho write and report the run as finished without this post having actually gone out.

**🔴 Format rules (MANDATORY, unchanged from v4.4):**
- **NO individual lead names, emails, companies, or titles in the Cliq notification.** Not even a "here are today's highlights" callout listing a few by name — zero exceptions.
- **Counts, funnel breakdown, and aggregates only.** This has to scale to a 100+ lead run without turning into a wall of text. A per-lead line multiplied by 100 leads is exactly the failure mode this format exists to prevent — never build toward that, regardless of how few leads a given run produced.
- Full per-lead detail lives in Zoho itself (that's what the BDM review queue is for) and, if the run was triggered interactively, in the chat response back to the requester — never in Cliq.

The funnel and rejection-reason detail below (v4.5) plus the pagination/volume note (v4.6) is what turns this into something a BDM or the Founder can actually use to judge whether a shortfall was a genuinely thin market day, a filter regression, or a pipeline mechanics issue:

```
📥 Scheduler 1 — Lead Population

Candidate pool (Apollo, pre-screen, actually paginated): 380
Dropped — duplicate/Zoho-excluded: 62
Dropped — ICP-rejected (industry/size/geography): 140
Dropped — weak technology fit + no signal (after Signal Enrichment Pass): 58
Dropped — no email found on enrichment: 4
Partner/Overflow (classified, not written): 3
Written to Zoho: 68

By campaign: C1: 18 | C2: 22 | C3: 11 | C4: 9 | C5: 8
LinkedIn priority (Ready to Connect): 17 of 68
LinkedIn content generated: 68 of 68 (every written lead, regardless of priority)
Social Lead ID populated: 68 of 68

Top rejection reason today: ICP-rejected (industry/size mismatch), 37% of drops
Best signal observed: technology-modernisation initiatives, Victoria SaaS segment
Next search rotation: UAE + product companies, .NET/Java + Product leadership

Apollo credits used: 61 (balance: 1,179)
All records: Lead_Status = "New Lead" — awaiting BDM review

Note: today's batch of 68 is below the 80 maximum production output. This
reflects [genuine pool thinness in today's rotation segment | tighter-
than-usual signal availability], not a lowered bar — no thresholds were
relaxed to reach a higher count. Raw candidate pool was confirmed
actually-paginated (380 pulled across N pages), so this is not a
pagination artifact.
```

Include the "below maximum" note when the written count is materially below 80, and always state the reason plainly rather than letting a shortfall pass without comment — and confirm via `apollo-search-builder`'s Volume Diagnostic that it's genuine before writing "market was thin," since that conclusion has been wrong before in this pipeline. Report credits used and remaining every run — it is the number that reveals a filter regression before the monthly bill does. Report the LinkedIn-priority count, LinkedIn content coverage, and Social Lead ID coverage alongside the campaign breakdown — together they reveal whether selection criteria, content generation, or ID capture drifted from expected behavior. **If the batch skews heavily toward only one or two campaigns (e.g. C1/C2 at 90%+ of the batch with C3-C5 near zero) without the user having requested a single specific campaign, name that skew explicitly in the note rather than only reporting the raw campaign-count split** — a lopsided split is itself a signal worth surfacing, the same way a pagination shortfall or a thin-market claim gets called out rather than left implied.

This mirrors the same summary-only discipline `saleshandy-distribution` enforces on its Step 7 Cliq post — both schedulers report to the same channel, and neither ever puts an individual lead's name or email where the whole team can see it. The added funnel and coverage detail is still aggregate-only; it does not reintroduce any per-lead identity into the channel.

**Cliq success verification (MANDATORY):** After calling the Cliq posting tool, inspect its actual response — a `tool_use` call by itself does not mean the notification was delivered. Only a response that indicates success (e.g. a `status: success` result) counts as delivered. If the response is missing, ambiguous, or indicates failure, treat Step 9 as not yet done and proceed to the failure handling below rather than assuming success.

**Cliq failure handling:** If the Cliq post fails, attempt at most one retry of the Cliq post itself — never rerun Apollo sourcing or enrichment, never repeat the Zoho write, never create duplicate CRM records, and never start Scheduler 2 or any Saleshandy action as a workaround. If the retry also fails, report this clearly as `CLIQ_NOTIFICATION_FAILED` together with the exact failure reason returned by the tool, plus explicit confirmation that (a) CRM processing was not rerun, (b) no duplicate lead writes were attempted, and (c) no Saleshandy action was started. Classify the overall run as `COMPLETED_WITH_NOTIFICATION_FAILURE` in that case, not as a fully complete run — a successful Zoho CRM write is necessary but not sufficient on its own to declare the run complete.

---


# CURRENT BINDING RULES — SEPTEMBER 2026

1. Production ramp-up target is **7–10 high-intent qualified leads per run** (scaling up to an 80 ceiling once multiple warmed mailboxes/domains are active).
2. Scheduler 1 must enforce `contact_email_status: ["verified"]` on all candidate searches to protect domain deliverability (< 1% bounce target).
3. The lead flow is: Apollo (`search_people`, verified) → Dedup → Qualification → ICP Score → Signal Enrichment → **PTB Score (Initial Buying Signal)** → Campaign Selection → Email Personalization → QA → Zoho → Cliq.
4. **PTB = Initial Buying Signal. There is one PTB score only (0–100).**
5. Calculate PTB once before outreach for every Qualified survivor.
6. Write the numeric PTB score as text to Zoho `Twitter`.
7. Do not calculate, wait for, or create a second post-engagement PTB score.
8. PTB is not a qualification gate and is never combined with ICP Score.
9. Campaign Selection consumes the same PTB score as its Buying Signal factor and does not apply a separate PTB threshold.
10. Outreach execution scope is Email-Only; LinkedIn outreach execution tasks are postponed.
11. If fewer leads are written than the target, report the exact funnel shortfall reason rather than lowering standards or padding the batch.

## CHANGE LOG — v5.2, September 2026 (Deliverability & Single PTB Alignment)

- Aligned production target to 7–10 high-intent qualified leads/day ramp-up ceiling (matching single-mailbox 25–35 emails/day limit, 300–480s randomized spacing, 0 tracking pixels).
- Enforced `contact_email_status: ["verified"]` across all search operations.
- Updated Apollo tool names to native Antigravity MCP (`search_people`).
- Clarified email-only outreach scope and removed all remaining references to a second post-engagement PTB score overwriting `Twitter`.
