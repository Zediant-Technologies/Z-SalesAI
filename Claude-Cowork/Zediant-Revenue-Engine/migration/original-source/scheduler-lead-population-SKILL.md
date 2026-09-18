---
name: "scheduler-lead-population"
description: "Zediant's Scheduler 1 — the daily lead factory. Orchestrates a wide, actually-paginated Apollo search, Zoho dedup, qualification, PTB scoring, campaign selection, enrichment, email + LinkedIn personalization for every survivor, batched Zoho write (LinkedIn Message written for every lead regardless of LinkedIn Status; Social Lead ID validated against the Apollo handoff), and a Cliq summary of counts/funnel/campaign mix only — no individual lead names or emails. Runs daily at 7:00 AM IST to populate Zoho with qualified, scored, personalized leads awaiting BDM approval. Quality over quota — ~100/day is a ceiling, never a target to pad. Skips Cold leads (PTB below 50) before spending credits. Routes software dev shops/consultancies to Partner/Overflow. Use: 'Run Scheduler 1', 'source leads from Apollo', 'populate today's leads'."
---

---
name: "scheduler-lead-population"
---

# Scheduler 1 — Lead Population Orchestrator (v4.6)

Daily sourcing workflow: pull a wide, actually-paginated candidate pool from Apollo, screen it cheaply, spend credits only on survivors, personalize for Email and LinkedIn for every survivor, and write to Zoho for BDM review.

## The core operating principle

Think like a senior salesperson deciding who's worth a BDM's time today, not like a database scraper filling a quota. **~100 qualified leads/day is an indicative ceiling, never a floor or a target.** If the genuinely qualified pool today is 40, write 40 and report the shortfall honestly in the Cliq summary — that is a successful run. Never loosen a qualification, PTB, or campaign-fit threshold, and never use a weaker lead to round the count up, purely to reach a number. A padded batch that the BDM rejects at review damages trust in every future run more than an honestly small one does.

**A written batch that's small relative to a large available Apollo pool is a different problem from a genuinely thin market, and the two must not be reported the same way.** See Step 0 and `apollo-search-builder`'s Volume Diagnostic — a real run returned only 8-10 leads against a 100 target from a 7,000-record segment, and the root cause was pipeline mechanics (an under-paginated search), not a thin market. Don't default to "the market was thin" without checking.

## The one thing to understand before anything else

**Screening is free; enrichment is not.** `apollo_mixed_people_api_search` returns name, title, company, industry, headcount, location, and technology tags at no credit cost — it just withholds the email address. Qualification, PTB scoring, and campaign selection need none of that withheld data. So every gate runs *before* enrichment, and only leads that survive all three gates ever cost a credit.

The old ordering enriched all leads up front and then discarded the Cold ones. That spent credits on leads the workflow was about to throw away. Never restore that ordering.

## What this skill does and does not do

**Does:** source a wide, properly-paginated candidate pool, screen, score, route, enrich survivors, personalize Email and LinkedIn content for every survivor, write to Zoho, notify Cliq.

**Does not:** approve leads, push to Saleshandy, activate campaigns, send email, or execute the actual LinkedIn outreach (connection request, message send). Approval is a human action in Zoho; distribution is Scheduler 2; LinkedIn execution is manual, using the content this skill stores — for every lead, not just the ones flagged `Ready to Connect`.

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

### Step 0 — Source a wide, actually-paginated candidate pool

Delegate sourcing to `apollo-search-builder` v1.6's Candidate Pool Strategy rather than running a single narrow search sized to land exactly at today's target. Retrieve 300–500 raw candidates across the day's rotated searches (see that skill's Search Rotation table — geography, technology, title, and signal focus each rotate day to day so pools don't exhaust and repeat work doesn't waste a search). This costs zero credits; the funnel from here to a written lead is what determines quality, not the width of the initial pull.

**This pooling must actually paginate, not just call the search endpoint once at its default page size.** A single default-sized `apollo_mixed_people_api_search` call (`per_page=25`, no `page` iteration) returns 25 candidates regardless of how many thousands exist in the underlying segment — everything downstream inherits that false scarcity, and a large Apollo total becomes irrelevant if only page 1 was ever pulled. Confirm the raw pool this step produced is actually in the 300-500 range (or genuinely pool-exhausted, per Known regional pool sizes) before moving to Step 1 — see `apollo-search-builder`'s Mandatory pagination and Volume Diagnostic sections.

### Steps 1-6 — screen, qualify, PTB score, campaign select, enrich survivors

Execute as documented in the original Scheduler 1 skill and in `apollo-search-builder`/`lead-qualification`/`ptb-scoring`/`campaign-selection`, unchanged in mechanics. Three additions from the current sourcing motion apply within these steps:

- **Zoho exclusion is permanent.** Apply `apollo-search-builder`'s full 5-step dedup cascade (Apollo Person ID → Email → LinkedIn URL → domain+name → company+name) before spending anything on a candidate. A person or company already in Zoho under this workflow is excluded from that point forward, regardless of a new score, a new trigger, or a different campaign fit on a later day. An Apollo-side processed-list label is secondary protection only — Zoho is the source of truth, and if the two ever disagree, Zoho wins. Check tier 4/5 matches (domain+name, company+name) for false positives if the exclusion count on a fresh rotation segment looks disproportionately high — over-matching is a real cause of a written batch coming back smaller than it should.
- **Signal Enrichment Pass.** Before finalizing PTB-relevant scores, run `apollo-search-builder`'s Signal Enrichment Pass on ICP-surviving candidates to fill real Buying Signal and Technology Fit data rather than defaulting to Unknown (which scores 0 in `ptb-scoring`). This recovers real prospects that would otherwise land under the PTB Reject threshold purely from missing data, not from actual poor fit — it does not change any scoring threshold.
- **Partner / Engineering Overflow routing.** If screening or qualification surfaces a candidate whose own business is software development, IT consultancy, or managed technology services, do not route it into C1–C5 by default. Classify it separately as Partner/Overflow per `apollo-search-builder` Step 6a and carry that classification through PTB scoring and into the Zoho write (Step 8) rather than silently dropping it or silently merging it into a standard campaign count. If genuinely ambiguous between partner and end-client, flag it with the specific question rather than guessing.

**Capture `apollo_person_id` for every candidate at Step 0/enrichment time and carry it forward as its own field through every stage** — per `apollo-search-builder`'s Apollo Person ID Capture requirement. This is what Step 8 below writes to `leadchain0__Social_Lead_ID`; don't leave this to be reconstructed at write time, since by then the original search/enrichment response may no longer be in context.

### Step 6a — Business Challenges and Case Study (enrichment, before personalization)

Two more fields now exist on every surviving lead, and they belong at enrichment time, not bolted on during outreach copywriting:

- **Business Challenges** — this is not new work. `lead-qualification`'s Step 6 already produces this finding for every Qualified lead (open roles, roadmap slippage, integration work, outages, stated capacity constraints). Carry that finding forward as-is, preserving whatever hedged/inferred phrasing `lead-qualification` used — don't firm it up into a stated fact on the way through.
- **Case Study** — the single most relevant approved Zediant case study for this lead, selected using Company/Industry/Business Challenges/Selected Campaign/relevant Zediant service, in that order of relevance (Business Challenges should drive which case study fits, not just shared industry). **Only pull from approved case study content that actually exists** — never invent a customer, a metric, a technology, or an outcome. If nothing approved genuinely fits, leave it blank; that is a normal, expected outcome for this run, not a defect.

Both values need to exist before Step 7 generates outreach copy, since Business Challenges is the primary input to Email Personalised Opening and Email Pain Points, and Case Study (when one exists) is available to both channels.

### Step 7 — Personalize: Email and LinkedIn for every survivor

Run `email-personalization` on every lead that survived qualification, PTB scoring, and campaign selection. That skill now produces, per lead:

- `Email_Personalised_Opening` and `Email_Pain_Points` — every survivor gets these, built primarily from Business Challenges
- The merged LinkedIn Message & Follow-up content — **as of `email-personalization` v2.3, generated for every survivor, not just leads marked `Ready to Connect`** — built from Business Challenges, Case Study (if one exists), campaign, and buying intent — never a copy of the email content
- A `LinkedIn Status` decision (`Ready to Connect` or `Not Required`) — ranked across the **whole batch**, not per-lead in isolation, targeting approximately the top 25 out of every ~100 qualified leads on quality, not quota. **This is now a priority/sequencing flag for the manual LinkedIn process, not a gate on whether LinkedIn content exists** — see `email-personalization` Section 4

Case Study is used where it genuinely fits the email sequence or the LinkedIn message — never force it into every touch just because a value exists in the field.

Don't run LinkedIn selection lead-by-lead as each one finishes qualification — batch it, since the ranking is relative to the rest of today's cohort. Hold personalization output for all survivors, then run the LinkedIn Selection priority ranking once across the full set before Step 8. LinkedIn *content* generation, however, doesn't need to wait on the ranking — every survivor gets it regardless of where they land in the ranking.

Rank the final written batch by PTB Score, not by ICP Score or company size alone — per `ptb-scoring` v1.3, a high-ICP lead with no buying signal should generally sit below a lower-ICP lead with a real, evidenced trigger. This affects the order the BDM sees leads in, and which leads land in the `Ready to Connect` priority slice.

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
    "Twitter": "100",
    "Lead_Campaign_Category": "C1 - AI-Enabled Product Engineering",
    "Business_Challenges": "...",
    "Case_Study": "...",
    "Email_Personalised_Opening": "...",
    "Email_Pain_Points": "...",
    "Rating": "Not Required",
    "LinkedIn_Message": "CONNECT:\n...\n\nFOLLOW-UP:\n...",
    "leadchain0__Social_Lead_ID": "...apollo_person_id...",
    "LinkedIN_Link": "https://linkedin.com/in/...",
    "Description": "[Excellent] PTB 100/100 - Series A SaaS founder, funding 4mo. Campaign: C1 - AI platform scaling matches product-engineering angle.\nTech stack: Cloud Infrastructure, AI/NLP (Strong fit)\nPersonalization angle: Engineering team growth driving capacity pressure on product roadmap."
  }]
}
```

Note the example above deliberately shows `Rating: "Not Required"` **with `LinkedIn_Message` still populated** — this is the corrected v4.6 behavior, not an inconsistency. A `Ready to Connect` lead's payload looks identical except for the `Rating` value; the presence of `LinkedIn_Message` no longer depends on which one is written.

**Score fields changed today:** `ICP_Score` and `PTB_Score` custom fields are deleted. Scores now go to `Skype_ID` (ICP Score) and `Twitter` (PTB Score) as plain text strings, e.g. `"78"` and `"100"` — not JSON numbers, both fields are `text` type. This was verified with a real write/read/delete test against a throwaway record, not assumed from the field label.

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

Post to channel `P1064180000000316007` (#zsales).

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
Dropped — Cold (PTB <50): 45   ← no credits spent
Dropped — no email found on enrichment: 4
Partner/Overflow (classified, not written): 3
Written to Zoho: 68

Average PTB score (written leads): 74
By campaign: C1: 18 | C2: 22 | C3: 11 | C4: 9 | C5: 8
LinkedIn priority (Ready to Connect): 17 of 68
LinkedIn content generated: 68 of 68 (every written lead, regardless of priority)
Social Lead ID populated: 68 of 68

Top rejection reason today: ICP-rejected (industry/size mismatch), 37% of drops
Best signal observed: technology-modernisation initiatives, Victoria SaaS segment
Next search rotation: UAE + product companies, .NET/Java + Product leadership

Apollo credits used: 61 (balance: 1,179)
All records: Lead_Status = "New Lead" — awaiting BDM review

Note: today's batch of 68 is below the ~100 indicative ceiling. This
reflects [genuine pool thinness in today's rotation segment | tighter-
than-usual signal availability], not a lowered bar — no thresholds were
relaxed to reach a higher count. Raw candidate pool was confirmed
actually-paginated (380 pulled across N pages), so this is not a
pagination artifact.
```

Include the "below target" note only when the written count falls meaningfully short of ~100, and always state the reason plainly rather than letting a shortfall pass without comment — and confirm via `apollo-search-builder`'s Volume Diagnostic that it's genuine before writing "market was thin," since that conclusion has been wrong before in this pipeline. Report credits used and remaining every run — it is the number that reveals a filter regression before the monthly bill does. Report the LinkedIn-priority count, LinkedIn content coverage, Social Lead ID coverage, and average PTB score alongside the campaign breakdown — together they reveal whether selection criteria, content generation, or ID capture drifted from expected behavior.

This mirrors the same summary-only discipline `saleshandy-distribution` enforces on its Step 7 Cliq post — both schedulers report to the same channel, and neither ever puts an individual lead's name or email where the whole team can see it. The added funnel and coverage detail is still aggregate-only; it does not reintroduce any per-lead identity into the channel.

---

## Design decisions resolved August 12, 2026 — for anyone reconciling this skill against the "Daily Fresh Lead Generation Agent" draft

The draft proposed several changes that were evaluated against the live schema and pipeline and resolved as follows. These are binding until revisited, not open questions:

1. **The draft's 5-category taxonomy (Product Engineering / Engineering Expansion / Integration-API / Modernisation / Growth-Product-Signals) is internal search-rotation guidance only.** `Lead_Campaign_Category` in Zoho continues to take C1-C5 exclusively, per `crm-update`'s live schema constraint. See `apollo-search-builder`'s mapping table if a label from the draft needs translating to a C1-C5 value.
2. **The draft's blanket 20-200 employee floor is not a global override of `icp.md`'s per-segment bands** (agencies 10-100, SaaS 10-200, CTO-led product companies 20-200). It is the default starting filter specifically for the SaaS/product-focused portion of the daily sourcing motion. A real sub-20-employee, strong-signal lead cleared this pipeline on its merits before this decision was made, and nothing here should have prevented that outcome — see `apollo-search-builder`'s Candidate Pool Strategy note.
3. **There is no separate Trigger Score.** The draft's Trigger Score weight table (funding, hiring, modernisation, etc.) was folded into `ptb-scoring` v1.3's existing Buying Signals category (still capped at 0-20 points), rather than becoming a second, parallel score that could disagree with PTB. If "Trigger Score" comes up in conversation, it refers to that category's reasoning.
4. **None of the draft's proposed new CRM fields** (Apollo Organization ID, Import Date, Search/Batch ID, Trigger Signal, Trigger Date, Technology Fit, Prospecting Priority) get Zoho's one remaining free custom field slot. All fold into `Description` as structured text, consistent with how `Scoring_Reason`/`Technology_Stack`/`Personalization_Notes` were already absorbed there when those fields were deleted.

---

## Version history

| Version | Change |
|---|---|
| 3.2 | Personalization mandatory; Description field added |
| 4.0 | Removed duplicate YAML frontmatter block. Switched approval gate from `Qualifying_Status` to `Lead_Status` (`New Lead`). Moved enrichment from Step 1 to after all three gates — credits now spent only on survivors. Batched Zoho dedup into one COQL query. Context files loaded once per run. Removed `Rating: "Not Started"` and `Twitter` writes (both invalid against live schema at the time). Removed stale references to the prior sending platform. |
| 4.1 | FIX: Added CRITICAL mandate that `Lead_Status` MUST ALWAYS be `"New Lead"` — never `"Pre-Qualified"`, `"Active"`, or other values. |
| 4.2 | LinkedIn outreach: `Scoring_Reason`/`Technology_Stack`/`Personalization_Notes` deleted from Zoho, folded into `Description`. `Qualifying_Status` fully deleted. Added Step 7 — Email personalization for all survivors plus batch-ranked LinkedIn Selection for ~25 of every ~100. `Rating` is now the live LinkedIn Status field — this skill writes it as `Ready to Connect`/`Not Required` only, reversing the old "do not write Rating" guidance. `leadchain0__Social_Lead_ID` now carries the Apollo Lead ID. Step 8 JSON payload and Cliq summary updated accordingly. |
| 4.3 | `ICP_Score`/`PTB_Score` custom fields deleted; scores now written to `Skype_ID`/`Twitter` as text strings (verified with a live test write). `LinkedIn_Follow_up` deleted, merged into `LinkedIn_Message` using a CONNECT/FOLLOW-UP two-part format. Added Step 6a - Business Challenges (carried forward from `lead-qualification`) and Case Study (approved-content-only, never invented) now populated at enrichment time, before Step 7 personalization. `Skype_ID` no longer functions as a Saleshandy-activation gate - `saleshandy-distribution` now gates on `Lead_Status` alone. Step 8 JSON payload updated accordingly. |
| 4.4 | Step 9 Cliq summary hardened to explicit MANDATORY format rules: summary counts and aggregates only, zero individual lead names/emails/companies/titles, no exceptions for small runs. This was implicit before ("No per-lead detail") but not spelled out — made explicit because posting individual lead identities to a team-wide channel doesn't scale past a handful of leads and shouldn't happen even at small volume. Matches the same discipline already enforced in `saleshandy-distribution`'s Step 7. |
| 4.5 | Reviewed against the "Daily Fresh Lead Generation Agent" draft and reconciled with the live pipeline (see Design Decisions section above). Added Step 0 — sourcing now explicitly delegates to `apollo-search-builder` v1.5's wide-pool-then-funnel Candidate Pool Strategy rather than a single narrow search. Added the core operating principle: ~100/day is an indicative ceiling, never a quota to pad toward. Added Partner/Overflow routing within Steps 1-6 and its handling in Step 8 (default: don't write to the daily batch; if tracked, flag explicitly in Description). Step 7 now explicitly ranks the written batch by PTB Score rather than ICP Score alone. Step 9 Cliq summary expanded to include funnel breakdown by drop reason, average PTB score, top rejection reason, best signal observed, and next search rotation segment — still aggregate-only, no per-lead identity, per the unchanged v4.4 format rules. Added an explicit shortfall-reporting note for when the written count lands meaningfully under ~100. |
| **4.6** | **Fixed two live-run defects and one throughput problem, all reported the same day. (1) `LinkedIn_Message` is now written for every survivor regardless of `Rating` — Step 7 and Step 8 updated to match `email-personalization` v2.3 and `crm-update` v5.1, which reversed the old Ready-to-Connect-only content gate. (2) `leadchain0__Social_Lead_ID` capture and write is now explicitly required at Step 0 (capture) and validated at Step 8 (write), per `apollo-search-builder` v1.6's Apollo Person ID Capture and `crm-update` v5.1's Social Lead ID — write rules, after a live run wrote this field blank for genuinely Apollo-sourced leads. (3) Step 0 now explicitly requires real pagination (300-500 raw candidates actually pulled, not a single default-sized page) after a live run returned only 8-10 written leads against a 100 target from a 7,000-record Apollo segment — traced to an under-paginated search, not a thin market. Added a Signal Enrichment Pass reference in Steps 1-6 to recover real PTB-relevant data before scoring finalizes, without lowering any threshold. Step 9 Cliq summary expanded with LinkedIn content coverage and Social Lead ID coverage counts, and the shortfall note now references the Volume Diagnostic explicitly.** |

---

**Owner:** Zediant AI Sales Team
**Status:** Production Ready (v4.6)
**Last Updated:** August 12, 2026

**Critical facts carried forward, still true:**
- Scheduler 1 MUST write `Lead_Status = "New Lead"` — never "Pre-Qualified" or any other value
- `Lead_Status` is the single field controlling pipeline state
- Scheduler 2 filters on `Lead_Status = "Approved for Outreach"` — incorrect values will cause filtering to fail
- `Rating` (LinkedIn Status) MUST be written as `"Ready to Connect"` or `"Not Required"` only — never an execution-stage value
- LinkedIn Selection is a batch-level priority ranking (Section 4 of `email-personalization`), not a per-lead decision made in isolation, and as of v4.6 it no longer gates content generation
- `Lead_Campaign_Category` takes C1-C5 only, never the daily search-rotation labels and never legacy List A-E

**New in v4.6:**
- `LinkedIn_Message` written for every survivor regardless of `Rating` value — reversed from the old Ready-to-Connect-only gate
- `leadchain0__Social_Lead_ID` capture (Step 0) and write validation (Step 8) made explicit, after a live run surfaced this field blank on Apollo-sourced leads
- Step 0 now requires confirmed real pagination (300-500 raw candidates), after a live run returned 8-10 written leads against a 100 target from a 7,000-record segment due to an under-paginated search
- Signal Enrichment Pass referenced in Steps 1-6 to recover real PTB-relevant data before scoring, without lowering thresholds
- Step 9 Cliq summary gained LinkedIn content coverage and Social Lead ID coverage counts

**New in v4.5:**
- Quality-over-quota made explicit as the core operating principle; ~100/day is a ceiling, not a target
- Step 0 added: sourcing explicitly delegates to `apollo-search-builder`'s wide-pool Candidate Pool Strategy
- Partner/Engineering Overflow classification and routing added
- Batch ranked by PTB Score, not ICP Score, before the Zoho write
- Cliq summary (Step 9) expanded with funnel/rejection-reason/average-score detail, still aggregate-only
- Four schema-reconciliation decisions from the "Daily Fresh Lead Generation Agent" draft review recorded as binding (taxonomy, employee band, trigger score, new fields)

**New in v4.3:**
- Scores go to `Skype_ID`/`Twitter` (text), not `ICP_Score`/`PTB_Score` (deleted)
- `LinkedIn_Message` now carries both the connection message and the follow-up in one field
- `Business_Challenges` and `Case_Study` are populated during enrichment (Step 6a), not deferred to the outreach-copy stage
- `Case_Study` must be blank, never fabricated, when no approved case study genuinely fits
</content>

