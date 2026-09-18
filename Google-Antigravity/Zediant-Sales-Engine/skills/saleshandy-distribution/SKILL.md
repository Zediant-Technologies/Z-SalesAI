---
name: "saleshandy-distribution"
description: "Zediant Scheduler 2 — distributes all BDM-approved Zoho leads to the correct Saleshandy campaign without activating sequences. Uses Lead_Status = 'Approved for Outreach' as the sole eligibility gate, validates current campaign and Saleshandy configuration at runtime, prevents duplicate enrollment, pushes approved personalization fields and case-study tags, updates successful leads to 'Outreach Scheduled', and reports aggregate results to Cliq. No artificial volume ceiling."
---

---
name: "saleshandy-distribution"
metadata:
  version: "1.9"
---

# Saleshandy Distribution — Scheduler 2 (v1.9)

Push BDM-approved leads from Zoho to Saleshandy campaigns. This is the final step before email sending begins.

---

## Overview

**What it does:**
1. **Fetch approved leads from Zoho** (`Lead_Status = "Approved for Outreach"` ONLY)
2. Validate campaigns exist and resolve them to a Saleshandy sequence (Draft sequences are valid import targets, not skipped)
3. Check for duplicates (skip if already added)
4. Batch by campaign (C1–C5), then split each campaign batch by Case Study availability (see Step 4a)
5. Push to Saleshandy via API with `Email_Personalised_Opening` / `Email_Pain_Points` / `Business_Challenges` / `Case_Study` as merge variables, tagged with the campaign tag and a `CASE_STUDY_AVAILABLE` / `CASE_STUDY_NOT_AVAILABLE` tag
6. Update Zoho: Lead_Status = "Outreach Scheduled"
7. Log results to Cliq for visibility (SUMMARY COUNTS ONLY, no individual lead details)

**The one thing:** This is the final gate before email sending, but it is not the final gate before enrollment. Approved leads get imported into their sequence's prospect list even while that sequence sits in Draft — Draft only blocks the sequence from actually sending, it does not block prospects from being queued into it. Activating a Draft sequence to Active is a separate, explicit BDM decision made directly in Saleshandy; this skill never makes it. This skill only pushes the Email channel — LinkedIn outreach (using the content `email-personalization`/`crm-update` store for every lead regardless of `LinkedIn Status`) is manual and doesn't go through Saleshandy at all.

---

## Scope

**Owns:**
- Fetching approved leads from Zoho (with strict Lead_Status filtering)
- Validating Saleshandy campaigns
- Batching by campaign and by Case Study availability
- Pushing to Saleshandy API with the correct merge variables and tags
- Updating Zoho Lead_Status
- Logging to Cliq (summary format)

**Does not own:**
- Deciding lead approval (BDM does in Zoho)
- Creating campaigns (Saleshandy setup done separately)
- Deciding whether a lead has a case study, or selecting which one — `email-personalization` decides this; this skill only reads the resulting `Case_Study` field and tags accordingly
- Monitoring email sends (Saleshandy-Reply-Tracker skill does)
- Re-enrichment or re-scoring
- Generating or editing the personalization content this skill pushes (`email-personalization` does)
- Anything related to LinkedIn — that content stays in Zoho for manual use, never enters Saleshandy

---

## Required Inputs

**None.** Runs on-demand with no parameters.

Processes all leads with `Lead_Status = "Approved for Outreach"`. This status alone is the eligibility gate — see the note on the retired `Skype_ID` gate below.

### Volume Rule

Scheduler 2 has **no artificial daily lead ceiling**. Process every currently eligible BDM-approved lead that can be safely distributed in the run. There is no requirement to stop at 80; the 80-lead ceiling belongs to Scheduler 1 only. If 61 approved leads are available, process up to 61. If 100 are available, process all 100, subject only to actual tool/runtime capacity. Never pad, truncate for convenience, or invent a quota.

### Exact Campaign Mapping

The current Zoho `Lead_Campaign_Category` values are authoritative:

- `C1 - AI-Enabled Product Engineering`
- `C2 - Engineering Pods & Staff Augmentation`
- `C3 - Platform Engineering & Cloud Modernization`
- `C4 - Middleware & API Integration (ZCoupler)`
- `C5 - Enterprise Custom Development & Modernization`

Use the exact current value from Zoho and resolve it to the corresponding current Saleshandy sequence at runtime. Never reduce it to `C1`, `C2`, etc. for matching unless the live Saleshandy title explicitly requires that prefix. Never use legacy List A-E values. If the Zoho campaign value and Saleshandy sequence taxonomy do not match, flag `DATA GAP` / `CONFIGURATION MISMATCH` and do not guess.

A real production run hit this: leads carrying near-miss values like `"C2 - Agency Engineering Expansion"`, `"C4 - Middleware & API Integration"` (missing the `(ZCoupler)` suffix), `"C4 - Middleware/API Integration"`, a bare `"Middleware & API Integration"` with no campaign prefix, and `"Other / Unscored"` were correctly left untouched at `Approved for Outreach` and reported as a DATA GAP rather than force-matched or silently dropped. That is the intended behavior — do not "fix" a near-miss value by assuming which campaign was meant.

---

## No-Work Path

If the Zoho query returns zero records with `Lead_Status = "Approved for Outreach"`, do not search Apollo, do not call Saleshandy import, and do not modify any Zoho records. Report a successful no-work run to Cliq with zero eligible/added/failed leads.

---

## Workflow

### Step 1: Fetch Approved Leads from Zoho (Batch) — STRICT FILTERING

**🔴 CRITICAL:** This step MUST filter on `Lead_Status = "Approved for Outreach"` ONLY.

**`Skype_ID` is no longer part of this filter.** `Skype_ID` was repurposed on August 8, 2026 to hold the **ICP Score** (per `crm-update` v5.0) — it is a real, populated business field on every qualified lead now, not an empty marker this skill can use to detect "not yet pushed." Checking it for emptiness would now either skip every lead (ICP Score is always populated by the time a lead reaches Approved for Outreach) or push leads incorrectly. `Lead_Status` alone is the gate: this skill flips `Lead_Status` to `"Outreach Scheduled"` in Step 6 on success, which removes the lead from this filter on every subsequent run without needing a second marker field.

Call COQL query or getRecords with explicit filter:
```
Lead_Status = "Approved for Outreach"
```

**Required fields:**
- `id` (Zoho Lead ID)
- `First_Name`, `Last_Name`, `Email`, `Title`, `Company`
- `Lead_Campaign_Category` (C1–C5)
- `Email_Personalised_Opening` (merge variable)
- `Email_Pain_Points` (merge variable)
- `Business_Challenges` (merge variable — see Step 4, added in v1.6)
- `Case_Study` (merge variable **and** the field this skill's tagging decision is based on — see Step 4a, added in v1.7)
- `Lead_Status` (for verification that it equals "Approved for Outreach")

**Known Zoho field API names (added v1.9 — skip schema discovery):** the label shown in the Zoho UI does not always match the field's actual API name used in COQL/getRecords. This mapping is stable and confirmed against the live Leads module schema — use it directly instead of calling `getFields` to rediscover it every run (a full `getFields` call on the Leads module returns the entire module schema, which is enormous and burns a large amount of context for a single lookup):

| Zoho UI label | Zoho API name (use this in COQL/getRecords) |
|---|---|
| Title | `Designation` |
| First Name | `First_Name` |
| Last Name | `Last_Name` |
| Email | `Email` |
| Company | `Company` |
| Lead Campaign Category | `Lead_Campaign_Category` |
| Email Personalised Opening | `Email_Personalised_Opening` |
| Email Pain Points | `Email_Pain_Points` |
| Business Challenges | `Business_Challenges` |
| Case Study | `Case_Study` |
| Lead Status | `Lead_Status` |

**Fallback:** if a COQL/getRecords call errors with `INVALID_QUERY` naming a field not in this table, call `getFields` for the Leads module to re-resolve just that one field's API name, then correct this table in the next skill edit — don't silently keep re-discovering the same mapping every run.

**Single batch fetch, no per-lead queries.**

**Do not process leads that do not have Lead_Status = "Approved for Outreach".**

If only 1 of 2 leads is approved:
- Fetch: Returns 1 lead
- Process: Push only that 1 lead
- Update Zoho: Only update that 1 lead's Lead_Status

Example: If Michelle Aguilar is approved but Srini Vasudevan is not:
- Fetch query returns: [Michelle Aguilar]
- Import: 1 lead to Saleshandy
- Update Zoho: 1 record updated
- Cliq notification: "Added: 1 lead"
- Srini's record remains untouched with Lead_Status = "New Lead"

---

### Step 2: Resolve Campaigns to Real Saleshandy IDs

Campaign names in Zoho (`C1`–`C5`) are labels, not Saleshandy identifiers. Resolve them at runtime — never hardcode IDs from a previous run.

For each unique campaign in the batch, call `list_sequences` once and match on title prefix (`C1 - `, `C2 - `, …):

```
list_sequences(pageSize: 100)
→ payload[].id      = sequenceId  (e.g. "68Pvv34nP7")
→ payload[].title   = match against "C1 - ", "C2 - ", ...
→ payload[].active  = must be true to SEND, but NOT required to IMPORT — record it for the Cliq status line, don't gate on it
→ payload[].steps[] = step list (steps[0] is Step 1)
```

Then get the Step 1 ID for each matched sequence — prospects are enrolled at a *step*, not at the sequence:

```
list_sequence_steps(sequenceId: "68Pvv34nP7")
→ find the entry where number == 1
→ that entry's `id` is the stepId to import into
```

**Also check whether the sequence has a sender attached, for reporting purposes:**

```
list_sequence_email_accounts(sequenceId: "68Pvv34nP7")
→ empty array = no sender attached = sequence cannot send yet
```

An empty result here does not block the import either — it only affects whether the sequence can send once activated. Note it for the Cliq status line so the BDM knows a sender still needs to be attached before this campaign is send-ready, same as a Draft status.

**Do this once per unique campaign, not per lead.** Cache `{campaign → sequenceId, stepId}` for the run.

**Token-efficiency note (added v1.9):** `list_sequence_email_accounts` returns the full email-account object per sender — sending limits, ramp-up settings, HTML signatures, etc. — none of which this skill needs beyond "is the array empty or not." This is a real cost (five sequences × two senders each is a non-trivial chunk of a run's tokens) but there is currently no lighter-weight tool call available for this check, and the sequence/sender configuration can drift between runs (a sequence going Draft, a sender disconnecting), so this skill does not currently cache this check across runs — it re-verifies every run so the Cliq "Saleshandy Status" line stays accurate. If a persistent cross-run cache for this is wanted later, it needs an explicit decision on acceptable staleness (e.g., re-verify at least every 24-48h) and on where that cache lives — do not add one without that decision being made and documented here first.

**Skip-and-flag rules (never auto-fix):**

| Condition | Action |
|---|---|
| No sequence matches the campaign label | Skip those leads, flag in Cliq — there's nothing to import into |
| `active` is false (Draft/paused) | **Import anyway.** Draft blocks sending, not enrollment — a lead sitting in a Draft sequence's prospect list is exactly where it should be while the BDM decides when to switch it on. Note the Draft status in the Cliq summary as a "not yet sending" flag, not a skip reason |
| No email accounts attached | **Import anyway**, same reasoning — no sender attached blocks sending, not enrollment. Note it in the Cliq summary alongside the Draft status if both apply |

**Activating a sequence (Draft → Active) is always an explicit human action. This skill never calls `update_sequence_status`, regardless of how many leads have been imported into a Draft sequence or how long they've been sitting there.** Importing prospects and activating the campaign are two separate decisions — this skill only ever does the first one.

---

### Step 3: Deduplication

**Do not call Apollo here.** Apollo is a sourcing tool and has no knowledge of what is in a Saleshandy sequence — querying it burns credits and returns an answer to the wrong question.

Two layers handle duplicates:

1. **Zoho-side (primary):** the Step 1 filter on `Lead_Status = "Approved for Outreach"` already excludes anything already pushed — Step 6 flips a successfully-pushed lead's `Lead_Status` to `"Outreach Scheduled"`, which removes it from this filter on every subsequent run. `Skype_ID` plays no role in this check (see the note in Step 1).
2. **Saleshandy-side (safety net):** pass `conflictAction: "noUpdate"` on import. Saleshandy matches on email and will not overwrite or re-enroll an existing prospect.

Also de-duplicate *within* the batch by email before building the payload — Zoho can hold two records for the same person.

---

### Step 4: Build the Prospect Payload

`import_prospects_to_sequence_step` keys every prospect by **field label**, exactly as returned by `list_fields` — not by snake_case API names. Wrong casing or underscores silently produce empty merge tags in the sent email.

Call `list_fields(systemFields: true)` once per run and confirm the labels below still exist before building payloads.

| Zoho field | Saleshandy label (exact) |
|---|---|
| `First_Name` | `First Name` |
| `Last_Name` | `Last Name` |
| `Email` | `Email` |
| `Title` (Zoho API name `Designation` — see Step 1) | `Job Title` |
| `Company` | `Company` |
| `Email_Personalised_Opening` | `Email Personalised Opening` |
| `Email_Pain_Points` | `Email Pain Points` |
| `Business_Challenges` | `Business Challenge` — note the naming mismatch, singular in Saleshandy vs. plural in Zoho. Same field, different label |
| `Case_Study` | `Case Study` |

**🔴 Fixed in v1.6 — this table was incomplete.** `Business_Challenges`/`Case_Study` were previously left out of the push entirely, on the assumption that `email-personalization` only produces two content fields now. That assumption was wrong and never re-checked against what the live templates actually do: pulling the real, active template content for all five campaigns on August 11, 2026 showed `{{Business Challenge}}` and `{{Case Study}}` are genuinely merged into a dedicated proof-point email in every campaign (and into a second slot in C1). Because this skill never sent them, every email reaching that step shipped with a blank or literal unresolved merge tag — a real defect, not a cosmetic gap. Both fields are pushed as of this version.

`Personalization Hook` is a different situation and stays unpushed: it isn't a `Personalization_Notes`-derived label at all, and — unlike `Business Challenge` and `Case Study` — **no Saleshandy prospect field by that name exists**, confirmed via `list_fields`. It appears in one template line (C5's final message) that is a known, accepted limitation per explicit direction, not something this skill's push payload can fix by adding a field that isn't there.

If `Case_Study` or `Business_Challenges` is blank for a given lead (a normal, expected outcome per `email-personalization`'s no-fabrication rule), push it as an empty string rather than omitting the key — the live template line still renders, just with nothing where the merge tag sits. That is the correct behavior, not a defect to work around.

`Email Personalised Opening` and `Email Pain Points` are **custom prospect fields** that must exist in Saleshandy (Settings → Prospect Fields) before the first run — they replace the four `Personalization_Notes`-derived labels (`Opening Observation`, `Business Challenge`, `Case Study`, `Personalization Hook`) this skill used before Zoho's `Personalization_Notes` field was deleted. `Business Challenge` and `Case Study` survived that deletion as real, standing Saleshandy fields even though this skill temporarily stopped sending them — they were never actually removed from Saleshandy, only from this skill's payload. If `list_fields` doesn't return all four labels this skill now pushes, stop and flag — the Saleshandy prospect field must be created or renamed first, and the Saleshandy email template's merge tags updated to match. Do not push, or every email ships with blank personalization lines.

### Step 4a — Case Study availability tagging (added v1.7)

**Every lead pushed to Saleshandy must carry one of two tags, based on whether `Case_Study` is populated in Zoho for that lead:**

| `Case_Study` in Zoho | Saleshandy tag |
|---|---|
| Populated (a real, approved case study `email-personalization` selected) | `CASE_STUDY_AVAILABLE` |
| Blank (no approved case study genuinely fit — a normal, expected outcome per `email-personalization`'s no-fabrication rule) | `CASE_STUDY_NOT_AVAILABLE` |

This is a real business need, not a cosmetic label: it lets the BDM (or a Saleshandy view/filter) separate leads whose case-study-proof email will read as strong social proof from leads where that email will render with an empty merge tag, without opening each record in Zoho to check.

**Mechanics — determine this at the same time as the campaign batching, before the push:**

1. After Step 1's fetch, evaluate `Case_Study` for every approved lead: non-empty string → `CASE_STUDY_AVAILABLE`; empty/null → `CASE_STUDY_NOT_AVAILABLE`. Do this per lead, not per campaign or per batch.
2. `import_prospects_to_sequence_step`'s `tags` parameter applies at the call level (one tag list per call, applied to every prospect in that call's `prospectList`) — confirmed against the tool's actual behavior, not assumed. Because the campaign tag and the case-study tag both need to land correctly on every prospect, **split each campaign's batch into two sub-batches: one for `CASE_STUDY_AVAILABLE` leads, one for `CASE_STUDY_NOT_AVAILABLE` leads**, and make one `import_prospects_to_sequence_step` call per sub-batch (so a campaign that previously took 1 call may now take up to 2, depending on whether both groups are non-empty for that campaign).
3. Each sub-batch's `tags` array carries **both** tags: the existing campaign tag (e.g. `"C1-Campaign"`) and the new case-study tag (e.g. `"CASE_STUDY_AVAILABLE"`). Both are created automatically by Saleshandy if they don't already exist (per the existing `tags` behavior — minimum 3 characters, already satisfied by both new tag values).
4. **Before implementing the split, check `list_fields`/the Saleshandy tool documentation for a per-prospect tag field on individual `prospectList` entries.** If Saleshandy's API does support per-prospect tags (rather than only a call-level list), prefer that — it avoids doubling the number of import calls per campaign. Use the call-level split described above only if a genuine per-prospect tag field isn't available. Document whichever mechanism is actually used the first time this runs, so this section can be corrected if the assumption above turns out to be wrong.
5. This does not change any of Step 4's field-mapping logic — `Case_Study` is still pushed as a merge variable (empty string when blank) exactly as before. The tag is an additional, separate signal layered on top of the existing merge-variable push, not a replacement for it.

**This tagging is required for every Saleshandy push, with no exceptions** — a lead should never reach Saleshandy without one of the two tags, since the whole point is a complete, filterable view across every actively-outreached lead.

A parallel version of this same classification is available in Apollo via `apollo_labels_add_entity_ids_to_label_names` if useful for internal Apollo-side tracking, but that is optional and out of scope for this skill — the requirement this skill enforces is the Saleshandy tag on every lead sent for Email outreach. See `apollo-search-builder`'s note on this if Apollo-side tagging is wanted too.

---

### Step 5: Push to Saleshandy (Batched by Campaign and Case Study Availability)

Use `import_prospects_to_sequence_step` or call the Saleshandy REST API directly (`skills/saleshandy-distribution/scripts/push_to_saleshandy.py`). **Do not use `add_leads_to_sequence`** — that tool takes numeric Saleshandy Lead Finder IDs for leads already revealed inside Saleshandy, and cannot accept leads sourced from Apollo and stored in Zoho. It will silently drop every lead in the batch.

**Direct REST API Endpoint:**
`POST https://api.saleshandy.com/v1/sequences/{sequenceId}/steps/{stepId}/prospects`
Headers: `x-api-key: <SALESHANDY_API_KEY>`, `Content-Type: application/json`

Up to two calls per campaign now, using the `stepId` cached in Step 2 and the sub-batches built in Step 4a:

```
import_prospects_to_sequence_step(
  stepId: "gOwE9LAKwb",              // Step 1 of the matched sequence
  prospectList: [
    {
      "First Name": "Patrick",
      "Last Name": "Donelan",
      "Email": "patrick@eql.com",
      "Job Title": "CTO and Co-Founder",
      "Company": "EQL",
      "Email Personalised Opening": "...",
      "Email Pain Points": "...",
      "Business Challenge": "...",   // empty string if Case_Study/Business_Challenges is blank in Zoho — never omit the key
      "Case Study": "..."
    }
    // ... every prospect in this call shares the same Case_Study-availability status
  ],
  conflictAction: "noUpdate",        // never overwrite an existing prospect
  verifyProspects: true,             // catch bad emails before they burn reputation
  tags: ["C1-Campaign", "CASE_STUDY_AVAILABLE"]   // campaign tag + case-study tag together
)
```

A second call for the same campaign's `CASE_STUDY_NOT_AVAILABLE` sub-batch looks identical except for `tags: ["C1-Campaign", "CASE_STUDY_NOT_AVAILABLE"]` and its own `prospectList`. Skip the second call entirely if a campaign has no leads in that sub-batch this run — don't make an empty call just to keep the pattern symmetrical.

**Token-efficiency note (added v1.9):** `import_prospects_to_sequence_step` requires the full `prospectList` inline in the call — there is no way to pass it by file reference, so one full appearance of each batch's content in the call is unavoidable. Do not also write the batch out to a file and separately display/read that file's full content before making the call "to check it" — that doubles the token cost of every batch for no quality benefit. Build the batch, spot-check counts/structure only (e.g. length, a couple of keys), and pass it straight into the tool call.

**Response handling:** the import is asynchronous. The tool returns a `requestId` and an initial status. If `statusResponse.payload.isCompleted` is false, poll `check_prospect_import_status(requestId)` before treating the push as done. If `failedProspectsURL` is populated, those leads did **not** enrol — record them as failures and leave their Zoho `Lead_Status` as `"Approved for Outreach"` (don't touch it) so the next run's Step 1 filter picks them back up and retries them.

Only mark a lead successful once the import has completed without appearing in the failed set.

---

### Step 6: Update Zoho Lead Status

For each successfully completed Saleshandy import, update ONLY:

```json
{
  "zoho_id": "...",
  "lead_status": "Outreach Scheduled"
}
```

Do **not** write to `Description`, `Skype_ID`, `Twitter`, `Rating`, campaign fields, personalization fields, or any other business-process field. `crm_update` remains the authoritative owner of general CRM business-process writes; Scheduler 2 owns only this explicit distribution state transition.

Batch the status updates with `updateRecords` where supported. Update only leads whose Saleshandy import has completed successfully. Failed, skipped, or unverified imports remain `Approved for Outreach` so they can be retried on a later run.

`Lead_Status = "Outreach Scheduled"` is the only CRM marker required to prevent the same lead from being fetched by the next Scheduler 2 run.

### Step 7: Log to Cliq — SUMMARY COUNTS ONLY

Send summary to `P1064180000001095002` (#Z-Outreach-Auto-Update).

**Completion sequencing (MANDATORY):** Required order: Saleshandy distribution (Steps 1-5) → Zoho `Lead_Status` updates (Step 6) → compose this aggregate Cliq summary → post it → verify the Cliq tool response indicates success (see below) → only then declare the Scheduler 2 run complete.

**Format rules (MANDATORY):**
- **NO individual lead names or emails in Cliq notification**
- **SUMMARY COUNTS ONLY** (total Added, Skipped, Failed)
- **Campaign breakdown** (counts only)
- **Case Study tag breakdown** (counts only — added v1.7)
- **No per-lead details like: "john.doe@acme.com → C3"**

```
🚀 Scheduler 2 Complete — Saleshandy Distribution

Added: 12 leads
Skipped: 0 leads
Failed: 0 leads

By Campaign:
• C1 (AI-Enabled Product Engineering): 5 leads
• C2 (Engineering Pods & Staff Augmentation): 4 leads
• C3–C5: 3 leads

Case Study Tags:
• CASE_STUDY_AVAILABLE: 8 leads
• CASE_STUDY_NOT_AVAILABLE: 4 leads

Zoho Updates:
✅ Lead_Status updated to "Outreach Scheduled" (12 leads)

Saleshandy Status:
→ C1 is in Draft (not Active) — leads are queued in the prospect list, will not send until a BDM activates the sequence in Saleshandy.

Duration: 4.1s | Timestamp: 2026-08-12T08:03:00+05:30 | Status: Complete
```

**Format rules (MANDATORY):**
- Only show counts: "Added: N", "Skipped: N", "Failed: N"
- Campaign breakdown as counts only: "C1: 5 leads" NOT "C1: john.doe@..., jane.smith@..."
- Case Study tag breakdown as counts only: "CASE_STUDY_AVAILABLE: N" / "CASE_STUDY_NOT_AVAILABLE: N", never which leads got which tag
- No individual lead names, emails, or error reasons per lead
- No "Failed Leads (Manual Review)" section with email list
- Campaign status and next steps are OK to include

This format scales to 100+ leads without clutter and keeps Cliq channel clean.

**Cliq success verification (MANDATORY):** After calling the Cliq posting tool, inspect its actual response before considering this step done — a tool call alone is not delivery confirmation. Only a response indicating success counts.

**Cliq failure handling:** If the post fails, retry the Cliq post once only — never re-import leads to Saleshandy, never re-run the Zoho `Lead_Status` updates, and never activate a Saleshandy sequence as a workaround. If the retry also fails, report `CLIQ_NOTIFICATION_FAILED` with the exact failure reason, plus confirmation that no duplicate Saleshandy imports or duplicate Zoho updates were attempted. Classify the run as `COMPLETED_WITH_NOTIFICATION_FAILURE` rather than fully complete.

---

## Success Criteria

| Measure | Target |
|---|---|
| Only "Approved for Outreach" leads fetched and processed | 100% |
| No unapproved leads pushed to Saleshandy | 100% |
| Zoho Lead_Status updated to "Outreach Scheduled" | 100% (only for added leads) |
| Duplicate prevention | 100% |
| Merge variables pulled from `Email_Personalised_Opening`/`Email_Pain_Points`, not a deleted field | 100% |
| Every lead pushed to Saleshandy tagged `CASE_STUDY_AVAILABLE` or `CASE_STUDY_NOT_AVAILABLE` | 100% — no lead reaches Saleshandy without one of the two tags |
| Case Study tag matches the actual `Case_Study` field state in Zoho at push time | 100% |
| Cliq notification contains ONLY summary counts | 100% — no individual lead details |
| Run completes in < 15 seconds | 95% |

---

**Version 1.9** · September 10, 2026 · Zediant Technologies · Saleshandy Edition

**Changelog v1.9:**
- **Catch-up fix — this file had drifted from the version actually in production use.** Restored three sections that were missing from this copy: the "Volume Rule" (no artificial daily lead ceiling), the "Exact Campaign Mapping" section (the 5 authoritative C1-C5 values plus the DATA GAP/CONFIGURATION MISMATCH flagging rule for near-miss campaign values — this rule is what correctly held back 24 leads with mismatched campaign labels in a live run rather than mis-routing or silently dropping them), and the "No-Work Path" section
- **Catch-up fix:** Step 6 in this copy still instructed writing an activity note into `Description` and referenced it from Step 1's worked example. The production version does not do this — Scheduler 2 writes `Lead_Status` only and explicitly must not touch `Description`, `Skype_ID`, `Twitter`, `Rating`, campaign fields, or personalization fields (that remains `crm-update`'s job). Both references removed to match
- **New — token efficiency:** added a static Zoho UI-label → API-name reference table to Step 1 (e.g. "Title" → `Designation`) so a full `getFields` call against the Leads module — which returns the entire module schema, a very large payload — is no longer needed just to resolve one field name every run. Kept a documented fallback: re-run `getFields` (and update this table) only if a COQL/getRecords call errors on a field not in the table
- **New — token efficiency:** added a note to Step 5 against writing a batch's full prospect payload to a file and displaying/reading it back before calling `import_prospects_to_sequence_step` — that call already requires the full payload inline, so a preview step roughly doubles the token cost of every batch with no quality benefit
- **Considered and deliberately NOT done:** caching `list_sequence_email_accounts` results across runs (it's the single most verbose per-run call, returning full sender objects — ramp-up settings, signatures, etc. — just to check whether the array is empty). Not implemented because it requires a staleness/storage decision (how stale is acceptable before it risks reporting wrong Draft/sender status to the BDM, and where would the cache persist) that hasn't been made yet. Documented as an open option in Step 2 rather than guessed at

**Changelog v1.8:**
- Updated automated Zoho Cliq notification destination to `#Z-Outreach-Auto-Update` (`P1064180000001095002`).

**Changelog v1.7:**
- Added Step 4a — every lead pushed to Saleshandy is now tagged `CASE_STUDY_AVAILABLE` or `CASE_STUDY_NOT_AVAILABLE` based on whether `Case_Study` is populated in Zoho at push time, per explicit direction that this needs to be visible and filterable in Saleshandy, not just in Zoho
- Because Saleshandy's `import_prospects_to_sequence_step` `tags` parameter applies at the call level, each campaign's batch is now split into up to two sub-batches by Case Study availability, each pushed with its own call carrying both the campaign tag and the case-study tag — documented as the assumed mechanism pending confirmation that a genuine per-prospect tag field isn't available, which would be preferable if it exists
- Step 6's activity note appended to `Description` now includes which case-study tag was applied
- Step 7 Cliq summary gained a Case Study Tags breakdown (counts only, same aggregate-only discipline as the campaign breakdown)
- Noted that the same classification is optionally available in Apollo via labels, but that this skill only enforces the Saleshandy-side requirement

**Changelog v1.6:**
- **Fixed a real defect, not a stylistic gap:** Step 4's merge-variable table only pushed `Email_Personalised_Opening`/`Email_Pain_Points`, on a stale assumption that those were the only two content fields `email-personalization` produces. Pulling the actual live template content for all five campaigns (August 11, 2026) showed `{{Business Challenge}}` and `{{Case Study}}` are genuinely merged into a dedicated proof-point email in every campaign — this skill just never sent the values, so those emails shipped with a blank or literal unresolved merge tag. Added `Business_Challenges` → `Business Challenge` and `Case_Study` → `Case Study` to Step 1's required fields and Step 4's push table
- Documented the `Business_Challenges`/`Business Challenge` naming mismatch (plural in Zoho, singular in Saleshandy) explicitly, so it doesn't get mistaken for two different fields on a future pass
- Clarified that a blank `Case_Study`/`Business_Challenges` (a normal, expected outcome per `email-personalization`'s no-fabrication rule) should be pushed as an empty string, not omitted — the template line still renders correctly with nothing in it
- Left `Personalization Hook` unpushed and undocumented as a fixable gap — confirmed via `list_fields` that no such Saleshandy field exists at all, unlike `Business Challenge`/`Case Study` which were real fields this skill simply stopped sending. It surfaces in one template line (C5's final message) that is a known, accepted limitation per explicit direction, not something a push-payload change can address

**Changelog v1.5:**
- Changed how Draft (inactive) sequences are handled. Previously this skill skipped any lead whose campaign sequence was Draft rather than Active. Per explicit direction: import approved leads into a Draft sequence's prospect list anyway — Draft only blocks the sequence from sending, it does not block enrollment, and getting leads queued into the right list ahead of activation is useful, not premature. The one rule that does not change: **this skill still never calls `update_sequence_status`.** Activating a sequence from Draft to Active remains a BDM decision made directly in Saleshandy, on its own timeline, regardless of how many leads are already queued in it
- Applied the same reasoning to "no email accounts attached" — that blocks sending too, not enrollment, so it's no longer a skip condition either. Both conditions are now reported in the Cliq summary as status flags rather than reasons a lead didn't get pushed
- Step 1's `list_sequences` `active` field and the `list_sequence_email_accounts` check are still read every run, but now feed the Cliq status line instead of a skip decision

**Changelog v1.4:**
- `Skype_ID` retired as this skill's "already pushed to Saleshandy" marker. `Skype_ID` was repurposed on August 8, 2026 to hold the ICP Score (per `crm-update` v5.0) and is now a populated business field, not an empty/non-empty flag this skill can read. The push-eligibility filter (Step 1) and the "already pushed" dedup check (Step 3) now rely on `Lead_Status = "Approved for Outreach"` alone; a successful push flips `Lead_Status` to `"Outreach Scheduled"`, which is sufficient by itself to keep a lead from re-entering the batch on the next run. Step 6 no longer writes a campaign name into `Skype_ID` — see `crm-update` v5.0 for the same decision documented on the write side
- Cliq summary template's "Skype_ID populated with campaign name" line removed to match

**Changelog v1.3:**
- `Personalization_Notes` deleted from Zoho on August 8, 2026. Step 1's required-fields list and Step 4's merge-variable table now read `Email_Personalised_Opening` / `Email_Pain_Points` directly instead of parsing four sub-values out of `Personalization_Notes`
- Noted that LinkedIn content (`LinkedIn_Message` — relabeled LinkedIn Message & Follow-up, holding both the connect and follow-up content — and `Rating`) never enters this skill's scope — Saleshandy carries Email outreach only
- Step 6's `description` update clarified as an append, not an overwrite, of what `crm-update` already stored in `Description`

**Changelog v1.2 (carried forward):**
- Step 1 CRITICAL mandate: Fetch ONLY `Lead_Status = "Approved for Outreach"` leads. If only 1 of 2 leads is approved, fetch 1, push 1, update 1.
- Step 7 Cliq notification is SUMMARY COUNTS ONLY. No individual lead names/emails. Format scales to 100+ leads without clutter.
