---
name: scheduler-lead-population
description: "Zediant's Scheduler 1 — the daily lead factory. Orchestrates an Apollo search with verified email enforcement across all five campaigns (C1-C5), qualification, PTB scoring, campaign selection, enrichment, email personalization for every survivor, and direct writing of all 10 custom fields to the Apollo contact record (Approval Status = 'New', Zoho Sync Status = 'Not Synced'). No cold leads are written to Zoho CRM during Scheduler 1 — Zoho CRM receives leads only upon prospect response. BDM reviews and approves leads directly in Apollo ('Approved for Outreach'). Sourcing pulls 7–10 high-intent qualified leads per daily run. Routes software dev shops to Partner/Overflow. Use: 'Run Scheduler 1', 'source leads from Apollo', 'populate today's leads'."
---

# Scheduler 1 — Lead Population Orchestrator (v6.0 - Apollo Native Pipeline)

Daily sourcing workflow: pull a candidate pool from Apollo with verified emails only, screen it cheaply, spend credits only on survivors, personalize email content for every survivor, and write all 10 enriched custom fields directly to the Apollo contact record for BDM review.

**CRITICAL WORKFLOW RULE**: Cold uncontacted leads reside exclusively in Apollo. No leads are written to Zoho CRM during Scheduler 1. Zoho CRM receives leads **only when a response is received** from outreach.

---

## The core operating principle

Think like a senior salesperson deciding who's worth a BDM's time today, not like a database scraper filling a quota.

**Ramp-up production target is 7–10 high-intent qualified leads per daily run** (aligned with Zediant's single-mailbox deliverability limit: 25–35 emails/day total, 600s spacing, 0 tracking pixels, strict email verification). Sourcing targets 25–50 raw verified candidates to find the best 7–10 prospects. Sourcing rotates across all five campaigns (C1–C5). Never loosen a filter, lower a score threshold, or pad a category to reach a round number. Reporting "only 6 genuinely qualified today" is the correct outcome when that's what's true.

---

## Screening is free; enrichment is not

`search_people` (with `contact_email_status: ["verified"]`) returns name, title, company, industry, headcount, location, and technology tags at no credit cost. Qualification, ICP scoring, and campaign selection need none of the withheld email data. Every gate runs *before* enrichment, and only leads that survive all of those gates ever cost a credit. PTB Score (Initial Buying Signal, 0–100) is calculated after qualification and feeds into `Company Trigger` and campaign selection.

---

## What this skill does and does not do

**Does:**
- Source a properly-filtered candidate pool (`contact_email_status: ["verified"]`) across all five campaigns
- Screen, qualify, and score ICP fit (1–100)
- Evaluate Buying Signals & PTB (Initial Buying Signal)
- Select target campaign (`Target Segment`) and messaging angle (`Outreach Angle`)
- Enrich survivor contacts with verified email
- Generate Antigravity personalization (`Personalised Email`, `Pain Point`, LinkedIn copy)
- **Write all 10 custom fields directly to the Apollo Contact**
- Post execution summary (counts/funnel/campaign mix) to Cliq `#Z-Outreach-Auto-Update`

**Does not:**
- Write cold leads to Zoho CRM (Zoho CRM receives leads only post-response)
- Approve leads for outreach (BDM approves in Apollo)
- Enroll leads into sequences (Scheduler 2 / `apollo-distribution` does this after BDM approval)
- Send emails or activate sequences

---

## Active Pipeline Sequence

```
Apollo Sourcing (contact_email_status: ["verified"])
→ Deduplication (Apollo Contact & Domain)
→ Lead Qualification & ICP Scoring (1–100)
→ PTB Scoring (Initial Buying Signal) & Company Trigger
→ Campaign Selection (Target Segment: C1–C5) & Outreach Angle
→ Email & LinkedIn Personalization (Personalised Email, Pain Point)
→ Apollo Contact Enrichment (All 10 Custom Fields Written + Sequences Field Populated)
→ Apollo Contact Status: Approval Status = "New" | Zoho Sync Status = "Not Synced" | Sequences = C1-C5
→ Awaiting BDM Approval in Apollo
```

---

## BDM Approval Gate — In Apollo

BDM reviews freshly populated leads directly in Apollo (e.g. filtered by `Approval Status = "New"`):

| Apollo Field | Value Set | Meaning | Next Step |
|---|---|---|---|
| `Approval Status` | `New` | Set by Scheduler 1 | Awaiting human review in Apollo |
| `Approval Status` | `Approved for Outreach` | Set manually by BDM | Cleared for Scheduler 2 sequence enrollment |
| `Approval Status` | `Responded` | Set by `apollo-reply-tracker` | Prospect replied; synced to Zoho CRM |

Scheduler 1 writes `Approval Status = "New"` and NOTHING ELSE. It never marks a lead "Approved for Outreach" autonomously.

---

## WORKFLOW

### Step 0 — Source candidate pool with verified emails
Delegate sourcing to `apollo-search-builder`. Enforce `contact_email_status: ["verified"]`.
- Ramp-up: retrieve **25–50 raw verified candidates** across C1–C5 rotation.
- Capture `apollo_person_id` and contact ID for every candidate.

### Steps 1–6 — Screen, qualify, PTB score, select campaign, enrich survivors
1. **Qualification & ICP Scoring**: Run `lead-qualification`. Determine verdict (QUALIFIED / RESEARCH_REQUIRED / REJECTED) and `ICP Score` (1–100).
2. **PTB Scoring & Company Trigger**: Run `ptb-scoring`. Evaluate initial buying signals (0–100). Synthesize the 1–2 sentence `Company Trigger` summarizing the observable evidence.
3. **Campaign Selection & Outreach Angle**: Run `campaign-selection`. Assign `Target Segment`:
   - `C1 - AI-Enabled Product Engineering`
   - `C2 - Engineering Pods & Staff Augmentation`
   - `C3 - Platform Engineering & Cloud Modernization`
   - `C4 - Middleware & API Integration (ZCoupler)`
   - `C5 - Enterprise Custom Development & Modernization`
   Assign `Outreach Angle`:
   - `Product Development` (for C1, C5)
   - `Engineering Capacity` (for C2, C3)
   - `Other` (for C4 or unique custom needs)
4. **Credit Enrichment**: Spend credit to unlock verified email on surviving Qualified candidates.

### Step 7 — Antigravity Personalization
Run `email-personalization`:
- `Personalised Email` (id: `6aa79177f203040018e0af9d`): Complete, cohesive 3-beat human narrative (50–90 words), natural tone, no AI clichés, no em-dashes, ready to send as Step 1 body:
  - **Beat 1 (The Hook):** Must be product-grounded (cite the prospect's actual flagship product/platform by name, e.g. `Crunchwork`, `Hutly`, `MachShip`, and the specific workflow problem it solves, avoiding generic filler like "modernizing user workflows").
  - **Beat 2 (Zediant Positioning):** For C1, articulate Zediant's core differentiator as **AI-Accelerated Delivery & Senior Ownership** (shipping feature modules 30-40% faster using modern AI-assisted engineering workflows under senior architectural ownership, embedded in 2-3 weeks).
  - **Beat 3 (The Ask):** Low-friction permission-based ask offering a 2-minute teardown of release acceleration without lengthy hiring lags.
- `Pain Point` (id: `6aa790fa8c717000101fa55c`): The specific technical/business challenge as a noun/gerund phrase, fitting into Step 3 email ("Saw earlier how {{Company}} was navigating {{Pain Point}}").
- LinkedIn copy (CONNECT prompt under 300 chars, non-pitch; and conversational FOLLOW-UP).

### Step 8 — Write All 10 Custom Fields & Populate Native "Sequences" Field on Apollo Contact

1. **Write Custom Fields**: Call `PUT https://api.apollo.io/v1/contacts/{contact_id}`:

```json
{
  "typed_custom_fields": {
    "6aa77b8749beb6001c395715": 85,
    "6aa77f1d3a845200202a56d6": "Apollo",
    "6aa790d821b4e6001cb70994": "C1 - AI-Enabled Product Engineering",
    "6aa790eddc1736001c90b2cf": "Scaling enterprise AI copilot with active senior hiring",
    "6aa790fa8c717000101fa55c": "Core dev team bottlenecked on infrastructure and LLM pipeline integration",
    "6aa79157e03659000e5b1889": "Product Development",
    "6aa79177f203040018e0af9d": "Saw what you are building on the product roadmap...",
    "6aa79220a06e87001c96131b": "New",
    "6aa7924153f031001ce91b15": "",
    "6aa7926fe82ec5000c4f65db": "Not Synced"
  }
}
```

2. **Populate Native "Sequences" Field**: Apollo maintains a native system field and UI column for **"Sequences"** (`emailer_campaign_ids`), which corresponds directly to the selected `Target Segment`. Populate this by adding the contact to the matching C1–C5 sequence via:
   `POST https://api.apollo.io/v1/emailer_campaigns/{sequence_id}/add_contact_ids`
   ```json
   {
     "contact_ids": ["{contact_id}"],
     "emailer_campaign_id": "{sequence_id}",
     "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
     "sequence_active_in_other_campaigns": false
   }
   ```
   **Live Sequence Mapping:**
   - C1: `6aa7ec0e7c0f80000cbd7600` (C1 - AI-Enabled Product Engineering)
   - C2: `6aa7eca553473f000c678940` (C2 - Engineering Pods & Staff Augmentation)
   - C3: `6aa7ecb31fd57300143fbfa7` (C3 - Platform Engineering & Cloud Modernization)
   - C4: `6aa7ecbea907dd00140753b2` (C4 - Middleware & API Integration (ZCoupler))
   - C5: `6aa7ecc953473f000c678b8e` (C5 - Enterprise Custom Development & Modernization)

   This ensures both the `Target Segment` custom field and the native `Sequences` field in Apollo reflect the assigned campaign, while maintaining `Approval Status = "New"` in a safe, staged state awaiting BDM review.

**Field ID Reference:**
- `6aa77b8749beb6001c395715`: `ICP Score` (Number, 1–100)
- `6aa77f1d3a845200202a56d6`: `Lead Source` (Picklist: `Apollo`, `LinkedIn`, `Other`)
- `6aa790d821b4e6001cb70994`: `Target Segment` (String: C1–C5 title)
- `6aa790eddc1736001c90b2cf`: `Company Trigger` (Textarea: evidence of buying signal)
- `6aa790fa8c717000101fa55c`: `Pain Point` (Textarea: specific problem addressed)
- `6aa79157e03659000e5b1889`: `Outreach Angle` (Picklist: `Engineering Capacity`, `Product Development`, `Other`)
- `6aa79177f203040018e0af9d`: `Personalised Email` (Textarea: Step 1 complete email narrative)
- `6aa79220a06e87001c96131b`: `Approval Status` (Picklist: `New`, `Approved for Outreach`, `Responded`)
- `6aa7924153f031001ce91b15`: `Zoho Record ID` (String: empty until response sync)
- `6aa7926fe82ec5000c4f65db`: `Zoho Sync Status` (Picklist: `Not Synced`, `Synced`)
- Native Apollo System Field: `Sequences` (`emailer_campaign_ids`, staged with target sequence)

### Step 9 — Report Summary to Cliq
Post run summary to Cliq `#Z-Outreach-Auto-Update`:
- Total Sourced
- Qualified Count
- Campaign Mix (C1–C5)
- Confirmation: All custom fields written to Apollo, `Approval Status = "New"`, ready for BDM review.
