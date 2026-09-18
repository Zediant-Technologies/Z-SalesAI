---
name: "crm-update"
description: "Zediant's CRM update SOP — maps output from Lead Qualification, PTB Scoring, Campaign Selection, and Email/LinkedIn Personalization onto Zediant's real Zoho Leads schema and writes it. Covers Case Study and Business Challenges enrichment fields, the merged LinkedIn Message & Follow-up field (now written for every lead regardless of LinkedIn Status), the Apollo Person ID write to Social Lead ID, and ICP/PTB scores on repurposed Skype_ID/Twitter fields. Enforces the BDM approval gate: Lead_Status must already be 'Approved for Outreach' before writing anything campaign-readiness-related — never grants approval itself. Use whenever a scored/routed/personalized lead needs pushing into Zoho, or right after Email Personalization produces variables, or to set LinkedIn Status, or to diagnose a blank Social Lead ID or missing LinkedIn Message. Do NOT use to decide if a company is worth pursuing, calculate PTB, pick a campaign, or write personalization content."
---

---
name: crm-update
metadata:
  version: "5.1"
---

# CRM Update — LinkedIn Outreach Edition

Take everything Lead Qualification, PTB Scoring, Campaign Selection, and Email/LinkedIn Personalization already produced for one company, and get it into Zoho accurately — using the fields that actually exist, not the fields a spec imagined.

## The one thing to understand before anything else

**Zediant's Zoho Leads module has no spare capacity.** As of the last live check (August 8, 2026), it is at 9/10 custom fields. The old `ICP_Score` and `PTB_Score` custom fields have been **deleted** — do not write to those api_names, they no longer exist. `LinkedIn_Follow_up` has also been **deleted**; its content now lives inside `LinkedIn_Message`, which was relabeled **LinkedIn Message & Follow-up** and holds both the connection message and the follow-up in one field. Two new custom fields were added: `Case_Study` and `Business_Challenges`.

Score storage moved to two repurposed standard fields, both **plain text**, not the old integer custom fields: `Skype_ID` is now labeled **ICP Score** and `Twitter` is now labeled **PTB Score**. Write the score as a plain numeric string (e.g. `"88"`), not a JSON number — both fields are `text` type.

**This repurposing has a real cost that this skill must not paper over.** `Skype_ID` previously stored the Saleshandy Campaign ID once a lead's campaign was confirmed activated — that capability has nowhere to go now that the field holds ICP Score instead. This skill no longer writes a Saleshandy Campaign ID anywhere. `saleshandy-distribution` now uses `Lead_Status` alone (`Approved for Outreach` → `Outreach Scheduled`) as its push-eligibility signal instead of checking `Skype_ID` for emptiness — see that skill for the corresponding change. If a BDM wants to know exactly which Saleshandy sequence a lead landed in, that now has to come from `Lead_Campaign_Category` (the C1-C5 category) plus the campaign registry, not a literal sequence ID stored on the record.

This skill does not invent new fields, does not assume capacity that doesn't exist, and does not silently drop data that has nowhere to go — it names the gap in Data Gaps instead. See **Field Mapping** below for the authoritative, schema-verified mapping.

**This skill also owns the mechanics of the BDM approval gate — not the approval decision itself.** `campaigns.md`'s non-negotiable operating rules require `Lead_Status = Approved for Outreach` in Zoho before any lead enters a campaign. This skill enforces that by reading the live value before writing anything that signals campaign-readiness — it never sets `Lead_Status` to `Approved` on its own initiative. That transition belongs to a human BDM working the record in Zoho.

**Campaign routing uses C1-C5 exclusively.** All `Lead_Campaign_Category` writes must use C1-C5 campaign names, never List A-E.

**The production outreach model is two channels, both written for every qualified lead, as of v5.1.** Every qualified lead gets Email personalization (`Email_Personalised_Opening`, `Email_Pain_Points`) **and** the merged `LinkedIn_Message` field. `LinkedIn Status` (`Ready to Connect` / `Not Required`) is a priority/sequencing flag for the manual LinkedIn execution process, not a gate on whether `LinkedIn_Message` gets written — see **LinkedIn Message & Follow-up — merged field format** below. This reverses the v4.0-through-v5.0 behavior where the field was only written when `LinkedIn Status = Ready to Connect`. This skill writes whatever `email-personalization` produced — it does not decide who gets priority; that ranking happens upstream. See `email-personalization`'s LinkedIn Selection Strategy for the actual criteria.

## Scope — and the boundary that matters

**Owns:** assembling one company's CRM payload from the upstream skills' output, mapping it onto Zediant's real Zoho Leads fields, performing the create-or-update write via the Zoho CRM connector, and enforcing (never granting) the `Lead_Status = Approved for Outreach` gate before writing anything campaign-readiness-related.

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Deciding whether the company is worth pursuing | `lead-qualification` |
| Calculating the priority score | `ptb-scoring` |
| Choosing which campaign the company enters | `campaign-selection` |
| Writing personalization content, deciding LinkedIn priority, generating LinkedIn messages | `email-personalization` |
| **Deciding** whether a lead is approved for outreach | A human BDM, in Zoho. This skill reads and enforces that decision; it does not make it |
| Activating a campaign or adding a lead to a Saleshandy sequence | Nobody, automatically. `campaigns.md`'s non-negotiable rules require an explicit human action for both |
| Sending, tracking opens/replies, or any post-send engagement data | Not yet built — a separate, future concept |
| Manual LinkedIn execution (sending the connection request, the message, the follow-up) | A human, using the content this skill stores, regardless of `LinkedIn Status`. `LinkedIn Status` values beyond `Ready to Connect`/`Not Required` (e.g. `Connection Sent`, `Connected`, `Message Sent`) are written by that human process, not by this skill |

---

# FIELD MAPPING — verified against live Zoho schema, August 8, 2026 (LinkedIn Message write rule updated August 12, 2026)

Zoho's Leads module has 63 fields total: 54 standard, 9 custom (1 slot free of the 10 cap). This table is the only authoritative mapping this skill uses.

## Custom fields (9/10 allocated)

| Zoho api_name | Label | Type | Source skill / value |
|---|---|---|---|
| `Lead_Campaign_Category` | Lead Campaign Category | picklist | `campaign-selection`'s Selected Campaign (C1–C5 only). Valid values: `C1 - AI-Enabled Product Engineering`, `C2 - Engineering Pods & Staff Augmentation`, `C3 - Platform Engineering & Cloud Modernization`, `C4 - Middleware & API Integration`, `C5 - Enterprise Custom Development & Modernization`. **Depends on the picklist in Zoho Setup actually containing all five C1-C5 values** |
| `Email_Personalised_Opening` | Email Personalised Opening | textarea (2000) | `email-personalization`'s opening block, verbatim. Never condensed or reworded — write exactly what that skill produced |
| `Email_Pain_Points` | Email Pain Points | textarea (2000) | `email-personalization`'s pain-point block, verbatim |
| `LinkedIn_Message` | **LinkedIn Message & Follow-up** | textarea (2000) | Holds both the connection/opening message and the follow-up in one field, in the fixed two-part format under **LinkedIn Message & Follow-up — merged field format** below. **As of v5.1, write this for every qualified lead `email-personalization` produced content for, regardless of `LinkedIn Status`.** Only leave it blank when `email-personalization` genuinely didn't supply content (see Exception Handling) — never blank it just because `LinkedIn Status = Not Required` |
| `Case_Study` | Case Study | textarea (2000) | The single most relevant approved Zediant case study for this lead, per `email-personalization`'s case study selection. **Only from approved case study content — never invented.** If no approved case study fits, leave blank with a short reason, don't fabricate one — see Data Gaps |
| `Business_Challenges` | Business Challenges | textarea (2000) | The lead-specific business/product/technology/engineering challenge(s), carried forward from `lead-qualification`'s Business Challenges finding (Step 6) and refined by PTB scoring/campaign selection if anything material changed. Phrase inferred challenges as inferred — see `lead-qualification`'s own phrasing discipline |
| `leadchain0__Social_Lead_ID` | Social Lead ID | text (150) | **Used to store the Apollo Lead ID** (`apollo_person_id` from `apollo-search-builder`'s handoff). **Write it whenever an Apollo ID is available upstream — treat a missing value on an Apollo-sourced lead as a data gap to investigate, not a normal blank.** See **Social Lead ID — write rules** below for the full procedure, added after a live run wrote this field blank despite Apollo-sourced leads. Note: this field was originally created by an installed Zoho Marketplace extension (`leadchain0` / LeadChain) and is wired into that extension's Lead→Contact/Deal conversion mapping — repurposing it for Apollo IDs is a deliberate, explicit decision, not this skill's default behavior for extension-owned fields generally |
| `LinkedIN_Link` | LinkedIN Link | text (255) | Contact's LinkedIn profile URL, if found during qualification or personalization research |
| `Lead_Status_Modified_Time` | Lead Status Modified Time | datetime | System-managed by Zoho on `Lead_Status` change — this skill does not write it directly |

**Deleted — do not reference as writable fields:** `ICP_Score`, `PTB_Score` (deleted today — see repurposed standard fields below), `LinkedIn_Follow_up` (deleted today — merged into `LinkedIn_Message`), `Scoring_Reason`, `Technology_Stack`, `Personalization_Notes`, `Qualifying_Status`. Their content, where it still needs to be captured, now lives in the standard `Description` field — see below.

## Standard fields repurposed for pipeline data (already in production use — do not treat as available for anything else)

| Zoho api_name | Repurposed label | Source |
|---|---|---|
| `Skype_ID` | **ICP Score.** New repurposing as of today, replaces the deleted `ICP_Score` custom field | Write `lead-qualification`'s numeric ICP score as a plain text string (e.g. `"88"`) — this is a `text` field, not `integer`. **No longer available to store a Saleshandy Campaign ID** — see the note above and `saleshandy-distribution`'s updated gate |
| `Twitter` | **PTB Score.** New repurposing as of today, replaces the deleted `PTB_Score` custom field | Write `ptb-scoring`'s Final PTB Score as a plain text string (e.g. `"95"`) — also `text`, not `integer` |
| `Rating` | **LinkedIn Status.** Repurposed and relabeled in live Zoho | Written by this skill (`Ready to Connect` or `Not Required`, from `email-personalization`'s LinkedIn Selection decision) and later updated by a human during manual LinkedIn execution. See **LinkedIn Status — write rules** below. **This field no longer controls whether `LinkedIn_Message` gets written — see that field's row above and the merged-field-format section below** |

### Social Lead ID — write rules (added v5.1)

A real run surfaced `leadchain0__Social_Lead_ID` coming back blank in Zoho for leads that were genuinely Apollo-sourced. Root cause was upstream — `apollo_person_id` wasn't reliably captured and carried through every stage before reaching this skill — and `apollo-search-builder` v1.6 now addresses that at the source (see that skill's Apollo Person ID Capture section). This skill's part of the fix:

1. **Before writing, confirm `apollo_person_id` was actually supplied** by the upstream handoff for any lead marked as Apollo-sourced (`Lead_Source` indicating Apollo, or the lead otherwise coming from an `apollo-search-builder` run this session).
2. **If it's present, write it exactly as supplied** — no reformatting, no truncation, no deriving a substitute ID from name+company.
3. **If it's missing on a lead that should have one**, don't write the field blank and move on silently. Flag it explicitly in Data Gaps: `"Social Lead ID missing — lead is Apollo-sourced but no apollo_person_id was supplied upstream, needs investigation"`. This is different from a lead that never went through Apollo at all (e.g., manually researched or referral-sourced), where a blank `leadchain0__Social_Lead_ID` is correct and expected — say which case applies.
4. **Never fabricate a Social Lead ID** to avoid a blank field — a fabricated ID is worse than a blank one, since it would look like real Apollo provenance on inspection.

### LinkedIn Message & Follow-up — merged field format

Since `LinkedIn_Follow_up` no longer exists as a separate field, write both messages into `LinkedIn_Message` using this fixed two-part format so a human running LinkedIn outreach can tell them apart at a glance:

```
CONNECT:
[the connection/opening message, verbatim from email-personalization]

FOLLOW-UP:
[the follow-up message, verbatim from email-personalization]
```

Plain labels and a blank line only — no em dash, no bullet characters, no decorative separator. Both halves still have to pass the no-AI-special-character check individually before this skill writes them.

**Write rule as of v5.1: this field is written for every qualified lead `email-personalization` produced content for, regardless of `LinkedIn Status`.** Prior versions of this skill (through v5.0) wrote `LinkedIn_Message` only when `LinkedIn Status = Ready to Connect` and left it blank for `Not Required`. That gate is removed — `email-personalization` v2.3 now generates this content for every qualified lead as a matter of course, and this skill writes whatever it receives. `LinkedIn Status` still tells the BDM and the manual LinkedIn process which leads to work first; it no longer determines whether content exists in Zoho. See Exception Handling for the (now rare) case where `email-personalization` genuinely didn't supply content for a lead.

### LinkedIn Status — write rules

Live picklist values on `Rating`: `-None-`, `Not Required`, `Ready to Connect`, `Connection Sent`, `Connected`, `Message Sent`, `Follow-up Due`, `Follow-up Sent`, `Response Received`, `Not Interested`, `No Response`, `Paused`, `Do Not Contact`, `Active`, plus four legacy display labels (`Completed`, `Not Started`, `Replied`, `Shut Down`) that are leftovers from the field's old stock configuration.

**This skill writes exactly two values, and only these two:** `Ready to Connect` or `Not Required` — per `email-personalization`'s LinkedIn Selection Strategy output. Every other value in the list (`Connection Sent` through `Do Not Contact`, and the four legacy labels) belongs to the human-run manual LinkedIn execution process downstream. Never write those, even if asked to "advance" a lead's LinkedIn status — that update happens in Zoho directly by whoever is running the LinkedIn outreach.

**Known landmine:** the four legacy display labels (`Completed`, `Not Started`, `Replied`, `Shut Down`) carry old internal `actual_value` codes left over from this field's original configuration (e.g. the display label `Replied` internally stores as `Project Cancelled`). This skill never writes any of the four, so it never hits this — but if a human asks why a record shows an odd internal value, that's why. Don't try to fix or reconcile this table; it's out of scope for this skill.

## Standard firmographic fields (ordinary use, no repurposing)

`Company`, `First_Name`, `Last_Name`, `Designation`, `Email`, `Phone`, `Mobile`, `Website`, `Lead_Source`, `Industry`, `No_of_Employees`, `Annual_Revenue`, `Country`, `State`, `City`. Populate from whatever qualification/enrichment already gathered.

## `Description` — now the home for retired-field content

`Description` (standard textarea, 32,000 characters) is where the content that used to live in `Scoring_Reason`, `Technology_Stack`, and `Personalization_Notes` now goes, appended in a fixed, readable format rather than lost. It is not a dumping ground — keep it structured so a BDM scanning the list view still gets full context in one place, per Step 3 below.

`Lead_Status` is the standard Zoho picklist that now carries the entire pipeline state. Live values (verified August 2026): `-None-`, `New Lead`, `Rejected`, `Attempted to Contact`, `Contact in Future`, `Contacted`, `Junk Lead`, `Lost Lead`, `Not Contacted`, `Pre-Qualified`, `Not Qualified`, `Meeting Booked`, `Resurfaced Again`.

The pipeline uses this subset:

| Value | Written by | Meaning |
|---|---|---|
| `New Lead` | Scheduler 1 / this skill on first write | Scored, awaiting BDM review |
| `Approved for Outreach` | BDM, manually | Cleared for a campaign — **the Scheduler 2 trigger** |
| `Outreach Scheduled` | Scheduler 2 | Pushed to Saleshandy |
| `Engaged` | BDM, manually after a reply | Prospect responded |
| `Rejected` | BDM, manually | Not pursuing |

**`Approved for Outreach`, `Outreach Scheduled`, and `Engaged` must be added to the picklist in Zoho Setup before any of this works.** Until they are, writes of those values fail with a picklist error — surface it rather than substituting `Pre-Qualified` or anything else that happens to be valid.

## Known constraint: Lead_Campaign_Category picklist must contain C1-C5 only (no List A-E)

**CRITICAL:** Update Zoho Setup → Leads module → Lead_Campaign_Category field → Picklist values to contain ONLY:

```
C1 - AI-Enabled Product Engineering
C2 - Engineering Pods & Staff Augmentation
C3 - Platform Engineering & Cloud Modernization
C4 - Middleware & API Integration
C5 - Enterprise Custom Development & Modernization
```

If the picklist hasn't been corrected yet, writes will fail with a clear Zoho error if the value doesn't match. **This skill does not silently substitute a different value — it surfaces the exact error**, so a real gap doesn't get quietly papered over.

---

# REQUIRED INPUTS

Company Name · Email (used as the duplicate-check key) · everything already produced by `lead-qualification` (verdict, ICP score, firmographics, Business Challenges finding), `ptb-scoring` (Final PTB Score, tier, Positive/Negative Factors), `campaign-selection` (Selected Campaign as C1-C5, Reason for Selection), `apollo-search-builder` (Apollo Lead ID, if this lead was Apollo-sourced), and `email-personalization` (Email Personalised Opening, Email Pain Points, Case Study selection, LinkedIn Status decision, and the merged LinkedIn Message & Follow-up content for every qualified lead) · whether a human has already approved this lead in Zoho (checked live, not assumed).

Re-read the upstream outputs rather than re-deriving any of this — this skill's only genuinely new work is mapping and writing.

---

# WORKFLOW

## Step 1 — Confirm all upstream passes are present

If any of Lead Qualification, PTB Scoring, Campaign Selection, or Email Personalization is missing, stop and name which one — don't write a partial record and don't backfill a missing stage with a guess. **As of v5.1, the merged LinkedIn Message & Follow-up content is expected for every qualified lead** — its absence is now a genuine missing-input error to flag (per Exception Handling), not an expected outcome tied to `LinkedIn Status`. Business Challenges should already exist from `lead-qualification`; Case Study is only required if `email-personalization` found an approved one to match — an empty Case Study is a legitimate outcome, not a missing input, when no approved case study fits.

## Step 2 — Check for an existing record

Use the Zoho CRM connector to look up the lead by `Email` (or `Company` + contact name if email is unavailable). This determines whether Step 6 creates a new record or updates an existing one.

## Step 3 — Build `Description`

`Description` absorbs what `Scoring_Reason`, `Technology_Stack`, and `Personalization_Notes` used to hold separately, in one readable block. Business Challenges and Case Study now have their own real fields (see Field Mapping) so they don't need to be repeated here in full — a one-line pointer is enough:

```
[PTB tier] PTB NN/100 - [one-line reason from Positive Factors]. Campaign: C[1-5] - [one-line Reason for Selection]. [Any Negative Factors worth flagging]
Tech stack: [named technologies if captured upstream, else omit this line entirely - don't write "Tech stack: unknown"]
Personalization angle: [the core Trigger to Pain Point to Zediant Relevance angle from email-personalization, condensed to one line]
```

Use a plain hyphen, not an em dash, in this template now that the same no-AI-special-character discipline applies to every field this skill writes, not just the four outreach content fields.

Omit a line entirely if there's nothing real to put in it — don't pad the field with placeholder text. This is a condensation step, same discipline the old `Scoring_Reason`/`Personalization_Notes` fields required: specific and scannable, not raw skill output pasted in wholesale.

## Step 4 — Write the content fields verbatim

Unlike `Description`, `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message` (the merged Message & Follow-up), and `Business_Challenges` are **not condensed**. Write exactly what the upstream skill produced, character for character. These fields feed directly into the Saleshandy email template and a human's LinkedIn message — rewriting or summarizing them here would silently change what actually gets sent.

`Case_Study` is also written verbatim when one was selected — never summarized, never invented if none was selected upstream.

Before writing, confirm none of these fields contains an em dash, en dash, or other AI-typical special character per `email-personalization`'s "write like a human" rule — see Validation. This skill doesn't regenerate content to fix a violation; if one is found, flag it back rather than silently stripping characters and changing the copy.

## Step 5 — Write `LinkedIn Status` (`Rating`), `LinkedIn_Message`, Apollo Lead ID, and scores

Write `Rating` = `Ready to Connect` or `Not Required` exactly as `email-personalization` decided — see **LinkedIn Status — write rules** above. This value is a priority flag; it does not gate `LinkedIn_Message`.

Write `LinkedIn_Message` (the merged Message & Follow-up field) whenever `email-personalization` supplied content — which, as of v2.3 of that skill, is every qualified lead — regardless of the `Rating` value written alongside it. Only leave it blank when the upstream output genuinely didn't include LinkedIn content for this lead (see Exception Handling); don't withhold it because `Rating = Not Required`.

Write `leadchain0__Social_Lead_ID` = the Apollo person ID if this lead came through `apollo-search-builder`; leave blank if it didn't (don't fabricate one) — and follow the full procedure in **Social Lead ID — write rules** above, including flagging a missing ID on an Apollo-sourced lead as a data gap rather than a normal blank.

Write `Skype_ID` (ICP Score) and `Twitter` (PTB Score) as plain numeric text strings, e.g. `"88"` and `"95"` — not JSON numbers, both are `text` fields.

## Step 6 — Check the live `Lead_Status` before writing anything campaign-readiness-related

Query the actual current value in Zoho — never trust a value passed in from earlier in the conversation. Four cases:

| Live `Lead_Status` | Action |
|---|---|
| `-None-` or record doesn't exist yet | This is a first-time write. Set it to `New Lead` — never `Approved for Outreach` |
| `New Lead` or `On Hold` | Write the scoring/campaign/personalization/LinkedIn data, but leave `Lead_Status` untouched |
| `Approved for Outreach` | Data can be written normally. `Skype_ID` now holds ICP Score and is written at Step 5 like any other field — it is no longer a signal that gets written only after campaign activation. Saleshandy push-eligibility is `saleshandy-distribution`'s concern, driven by `Lead_Status`, not by anything this skill writes here |
| `Rejected` | Stop. Don't overwrite scoring, campaign, or personalization data onto a record a human already rejected |

## Step 7 — Set `Lead_Status` only per the rule above

The only value this skill writes to `Lead_Status` on its own initiative is `New Lead`, and only on a first-time write. Writing `Approved` requires an explicit, distinct instruction from the user in the moment — treat it as a deliberate action, not something inferred from a high PTB Score or a `Ready to Connect` LinkedIn Status.

## Step 8 — Perform the write

Use `upsertRecords` on the Leads module with `Email` as the duplicate-check field where possible. Map every field per **Field Mapping** above — nothing outside that table. Ensure `Lead_Campaign_Category` contains a C1-C5 value exactly matching a picklist option in Zoho, `Rating` contains exactly `Ready to Connect` or `Not Required`, `LinkedIn_Message` is populated whenever upstream supplied content (independent of `Rating`), `leadchain0__Social_Lead_ID` is populated whenever an Apollo ID was supplied upstream, and `Skype_ID`/`Twitter` are sent as text strings, not numbers.

## Step 9 — Report what actually happened

State plainly: created or updated, which fields were written, what `Lead_Status` and `LinkedIn Status` are now, whether `LinkedIn_Message` and `leadchain0__Social_Lead_ID` were populated, and anything that couldn't be written (missing picklist value, missing data, a Zoho API error).

---

# DECISION RULES

Never write `Lead_Status = Approved for Outreach` without an explicit, in-the-moment human instruction to do so. This is the single most important rule.

Never write `ICP_Score` or `PTB_Score` — those custom fields are deleted. The scores go to `Skype_ID` and `Twitter` respectively, as text.

Never write a Saleshandy Campaign ID anywhere — that capability no longer exists in this schema. Don't invent a substitute field for it.

Never write a `Lead_Campaign_Category` value outside C1-C5. If `campaign-selection` outputs anything other than C1-C5, that's a bug upstream — surface it rather than working around it.

Never write `Rating`/LinkedIn Status to anything other than `Ready to Connect` or `Not Required`. Every execution-stage value belongs to a human running LinkedIn outreach manually.

**As of v5.1: never withhold `LinkedIn_Message` solely because `LinkedIn Status = Not Required`.** Write it whenever `email-personalization` supplied content, regardless of the `Rating` value. This reverses the pre-v5.1 rule.

Never invent a Case Study. If `email-personalization` didn't find an approved one that genuinely fits, leave `Case_Study` blank and say so in Data Gaps — a blank field is correct behavior here, not a failure.

Never present an inferred Business Challenge as a confirmed fact. Write it the way `lead-qualification` phrased it — if that skill hedged it, this skill writes the hedge too, it doesn't firm up the language on the way into Zoho.

Never invent a field, picklist value, or workaround not in the Field Mapping table above. If something doesn't fit, say so in Data Gaps rather than forcing it somewhere close-enough.

Never silently substitute a value when a Zoho write fails (e.g., writing a different campaign instead of the selected one) — surface the actual error.

Never condense or reword `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message`, `Business_Challenges`, or `Case_Study` — write them verbatim from the upstream skill that produced them. Condensation belongs only in `Description`.

**Never write `leadchain0__Social_Lead_ID` blank on a lead that's genuinely Apollo-sourced without flagging it as a data gap.** A blank Social Lead ID is only unremarkable when the lead never went through Apollo at all — see Social Lead ID — write rules above.

Never fabricate a Social Lead ID to avoid a blank field.

---

# EXCEPTION HANDLING

| Situation | Action |
|---|---|
| `Lead_Campaign_Category` write fails because a C1-C5 value isn't a valid picklist value yet | Surface the exact Zoho error. Check whether the picklist edit in Zoho Setup has actually landed. Don't substitute a different category or silently drop the field |
| The Leads module reports the 10-custom-field cap on a write | Stop and flag — the schema changed since the last `getFields` check and Field Mapping needs re-verification |
| No existing record found and required firmographic fields (Company, Email) are missing | Don't create a record with critical fields blank — flag what's missing |
| A contact name wasn't supplied upstream, only an email address | Leave `First_Name`/`Last_Name` blank. Note it in Data Gaps |
| Two records plausibly match the same company | Don't guess which one to update — flag the ambiguity rather than risk overwriting the wrong record |
| `Lead_Status` is already `Rejected` | Stop, per Step 6. Report back rather than writing over a human decision |
| `email-personalization` genuinely didn't supply `LinkedIn_Message` content for a qualified lead (e.g., the batch was too large to complete in one pass per that skill's own exception handling) | Leave `LinkedIn_Message` blank for now and flag it in Data Gaps as outstanding, not as "Not Required, so no content expected" — as of v5.1 this is a real gap to close, not a normal state |
| A content field (Email Opening, Email Pain Points, LinkedIn Message & Follow-up, Business Challenges, or Case Study) contains an em dash or other AI-typical special character | Flag it back to the skill that produced it rather than silently editing the copy yourself |
| No approved case study fits this lead | Leave `Case_Study` blank. This is a normal, expected outcome, not an error — note it in Data Gaps |
| A Zoho write to `Skype_ID` or `Twitter` is rejected or silently ignored | Surface it immediately — these are repurposed standard fields, not custom fields, and their write behavior should be re-verified against live Zoho if this happens, since it previously took a real test write to confirm they actually persist |
| `leadchain0__Social_Lead_ID` is blank but the lead is genuinely Apollo-sourced (e.g. `Lead_Source` or session context indicates Apollo) | Flag explicitly in Data Gaps as a data gap needing investigation, per Social Lead ID — write rules. Don't write it silently blank as if it were a normal case |

---

# ESCALATION

Escalate to a human rather than proceeding:

- Anyone asks you to set `Lead_Status = Approved for Outreach` as a matter of routine rather than a specific, deliberate decision about this lead
- Anyone asks you to advance `LinkedIn Status` past `Ready to Connect` (e.g., to `Connection Sent` or `Connected`) — that belongs to the human running LinkedIn outreach
- A Zoho write fails for a reason not covered in Exception Handling
- The upstream outputs conflict with what's already in Zoho for this record
- A duplicate or near-duplicate record situation that isn't a clean single match
- A C1-C5 value is returned from `campaign-selection` that doesn't match any of the five valid values
- `leadchain0__Social_Lead_ID` is missing across a whole batch of otherwise-Apollo-sourced leads — this suggests an upstream capture problem in `apollo-search-builder`, not a per-lead data gap, and is worth surfacing as a pattern rather than flagging each lead individually

---

# VALIDATION

Before confirming a write is complete, confirm:

- [ ] Every field written appears in the Field Mapping table by its real `api_name` — no invented field, and nothing written to `ICP_Score`, `PTB_Score`, `LinkedIn_Follow_up`, `Scoring_Reason`, `Technology_Stack`, `Personalization_Notes`, or `Qualifying_Status` (all deleted)
- [ ] `Lead_Status` was only set to `Approved` following an explicit human instruction in this interaction, never inferred from score or tier
- [ ] `Rating` (LinkedIn Status) contains only `Ready to Connect` or `Not Required` — never an execution-stage value
- [ ] `LinkedIn_Message` (merged Message & Follow-up) is populated whenever `email-personalization` supplied content, **independent of the `Rating` value**, and uses the CONNECT / FOLLOW-UP two-part format
- [ ] `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message`, `Business_Challenges`, `Case_Study` were written verbatim, not condensed, and contain no em dash or other AI-typical special character
- [ ] `Skype_ID` (ICP Score) and `Twitter` (PTB Score) were written as text strings, not numbers
- [ ] `Case_Study` contains only an approved, upstream-sourced case study, or is blank — never a fabricated one
- [ ] `Business_Challenges` phrases inferred challenges as inferred, matching `lead-qualification`'s own hedging, not stated as confirmed fact
- [ ] `Description` is condensed and readable, not raw skill output pasted in wholesale
- [ ] `leadchain0__Social_Lead_ID` contains the Apollo Lead ID where one exists upstream; where it's missing on an Apollo-sourced lead, that's flagged in Data Gaps rather than silently left blank; where the lead genuinely never went through Apollo, blank is correct and unremarked
- [ ] `Lead_Campaign_Category` contains a C1-C5 value (never List A-E) that matches the Zoho picklist exactly
- [ ] The create-vs-update decision was based on an actual lookup by Email, not assumed
- [ ] No Saleshandy Campaign ID was written anywhere — that field no longer exists

---

# OUTPUT FORMAT

```
## CRM Write Result
Created | Updated — [Company Name] ([Email])

## Fields Written
| Field (api_name) | Value |
|---|---|
[Only fields actually written this pass]

## Lead_Status
[Current value after this write, and whether this skill changed it]

## LinkedIn Status
[Ready to Connect | Not Required, and confirm the merged LinkedIn Message
& Follow-up field was written — this is now expected for every
qualified lead, independent of the Status value]

## Social Lead ID
[Written value if Apollo-sourced, or "not applicable - not Apollo-sourced",
or "MISSING - flagged for investigation" if it should have a value and doesn't]

## Campaign Category
Lead_Campaign_Category = [C1 through C5 value written]

## Not Written / Data Gaps
[Anything that couldn't be mapped, was missing, or hit a Zoho error]
```

When processing a batch, lead with a compact table — company, created/updated, `Lead_Status`, LinkedIn Status, `LinkedIn_Message` written (Y/N), Social Lead ID present (Y/N/N-A), campaign, any error — then expand only the records with a Data Gap or error.

---

# RELATED SKILLS

| Skill | Relationship |
|---|---|
| `lead-qualification` | Upstream. Supplies the verdict, ICP score (now written to `Skype_ID`), and the Business Challenges finding this skill writes to `Business_Challenges` |
| `ptb-scoring` | Upstream. Supplies the Final PTB Score (now written to `Twitter`) and the tier folded into `Description` |
| `campaign-selection` | Upstream. Supplies `Lead_Campaign_Category` as C1-C5 and its reasoning |
| `email-personalization` | Upstream, immediately before this skill. Supplies `Email_Personalised_Opening`, `Email_Pain_Points`, the Case Study selection, the LinkedIn Status priority decision, and — as of v2.3, for every qualified lead — the merged LinkedIn Message & Follow-up content |
| `apollo-search-builder` | Often upstream of all of the above — many leads reaching this skill already exist in Zoho from an earlier Apollo-sourced write. Supplies the Apollo Lead ID written to `leadchain0__Social_Lead_ID`; v1.6 added mandatory capture of this ID at search/enrichment time to fix a live gap where it was reaching this skill blank |
| `saleshandy-distribution` | Downstream, separate run. No longer reads `Skype_ID` to decide push-eligibility — uses `Lead_Status` alone now that `Skype_ID` holds ICP Score |

---

# SUCCESS CRITERIA

| Measure | Target |
|---|---|
| Writes using a field not in the Field Mapping table | Zero |
| `Lead_Status` set to `Approved` without an explicit human instruction in that interaction | Zero |
| `Rating`/LinkedIn Status written to an execution-stage value by this skill | Zero |
| `LinkedIn_Message` withheld solely because `Rating = Not Required` | Zero — reversed from the pre-v5.1 target |
| `LinkedIn_Message` written for a qualified lead where `email-personalization` supplied content | 100% |
| `leadchain0__Social_Lead_ID` blank on a genuinely Apollo-sourced lead without a Data Gap flag | Zero |
| `ICP_Score`/`PTB_Score`/`LinkedIn_Follow_up` referenced as writable fields | Zero |
| A Saleshandy Campaign ID written anywhere | Zero (field no longer exists for this) |
| `Case_Study` containing a fabricated case study | Zero |
| Zoho write failures silently papered over with a substitute value | Zero |
| `Lead_Campaign_Category` writes containing List A-E values (deprecated) | Zero |
| `Lead_Campaign_Category` writes containing invalid C1-C5 values | Zero |

---

# VERSION

Version 5.1 · Owner: Zediant AI Sales Team · August 12, 2026

**Changes in V5.1 — LinkedIn Message unconditional write, Social Lead ID fix:**
- Reversed the `LinkedIn_Message` write gate: this field is now written for every qualified lead `email-personalization` supplied content for, regardless of `Rating`/`LinkedIn Status`. Previously (V4.0 through V5.0) it was only written when `Rating = Ready to Connect` and left blank otherwise — that matched `email-personalization`'s old behavior, which itself changed in that skill's v2.3
- Added **Social Lead ID — write rules**, a dedicated procedure for `leadchain0__Social_Lead_ID`, in direct response to a live run where the field came back blank in Zoho despite Apollo-sourced leads. This skill's part of the fix: confirm `apollo_person_id` was actually supplied before writing, write it exactly as supplied, and flag a missing value on an Apollo-sourced lead as a Data Gap rather than a silent blank — paired with the upstream fix in `apollo-search-builder` v1.6
- Updated Field Mapping, Workflow Steps 1 and 5, Decision Rules, Exception Handling, Escalation, Validation, Output Format, Related Skills, and Success Criteria to match both changes

**Changes in V5.0 — score field repurposing, Case Study/Business Challenges, LinkedIn field merge:**
- `ICP_Score` and `PTB_Score` custom fields deleted from Zoho. Scores now live on repurposed standard fields: `Skype_ID` → ICP Score, `Twitter` → PTB Score. Both are `text` type — write scores as numeric strings, not JSON numbers. Verified live with a real write/read/delete test on a throwaway record, not assumed from the field label alone
- This broke `Skype_ID`'s prior role storing the Saleshandy Campaign ID once a campaign was activated — that capability is gone. This skill no longer writes any Saleshandy Campaign ID. `saleshandy-distribution`'s push-eligibility check moved to `Lead_Status` alone
- `LinkedIn_Follow_up` deleted. `LinkedIn_Message` relabeled **LinkedIn Message & Follow-up** and now holds both messages in a fixed CONNECT / FOLLOW-UP two-part format
- Two new custom fields added: `Case_Study` and `Business_Challenges`. Both written verbatim from upstream, never condensed, never fabricated — `Case_Study` must come from an approved source or stay blank; `Business_Challenges` carries forward `lead-qualification`'s Step 6 finding, preserving whatever hedging language that skill used
- Custom field count now 9/10 (was 10/10 — the ICP/PTB deletion freed one more slot than Case Study + Business Challenges consumed)
- No-AI-special-character validation extended to the two new fields and to the `Description` template itself

**Changes in V4.0 — LinkedIn outreach fields:**
- `Scoring_Reason`, `Technology_Stack`, `Personalization_Notes`, and `Qualifying_Status` deleted from Zoho; removed from Field Mapping. Their content now folds into the standard `Description` field (Step 3)
- Added four new custom fields: `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message`, `LinkedIn_Follow_up` — written verbatim, never condensed
- `Rating` repurposed and relabeled **LinkedIn Status** in live Zoho — this skill writes only `Ready to Connect`/`Not Required`; all execution-stage values belong to manual LinkedIn work
- `leadchain0__Social_Lead_ID` repurposed to store the Apollo Lead ID (was previously pass-through-only)
- Added the no-AI-special-characters check to Validation for all four content fields
- Custom field count confirmed still 10/10 after the swap

**Changes in V3.0:**
- Removed the duplicated YAML frontmatter block (the second block was rendering as body text)
- Approval gate moved from `Qualifying_Status` to `Lead_Status`; `Qualifying_Status` marked retired but still occupying a custom slot (now fully deleted, see V4.0)
- `Rating` and `Twitter` marked do-not-write — both repurposings were documented but never implemented in Zoho, so writes to them failed (Rating's status changed in V4.0 — see above)
- Documented the real, verified `Lead_Status` and `Lead_Campaign_Category` picklist state, including which values are missing
- References to the prior sending platform replaced with Saleshandy
</content>

