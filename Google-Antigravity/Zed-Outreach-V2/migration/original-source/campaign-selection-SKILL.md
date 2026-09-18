---
name: "campaign-selection"
description: "Zediant's campaign selection SOP — decides which single Saleshandy campaign (C1-C5) a PTB-scored lead enters, and why. Use whenever the user wants to route, assign, or select a campaign for a lead: 'which campaign for X', 'route this lead', 'what campaign should this go in', 'assign a campaign to these leads', or right after PTB Scoring has produced a score and the lead needs to move toward outreach. Also use when comparing how well a company fits multiple campaigns, or diagnosing why a lead was routed somewhere unexpected. Do NOT use this to decide whether a lead is worth pursuing (lead-qualification) or to calculate the priority score itself (ptb-scoring) — this skill assumes both are already done. Does not write emails, does not touch CRM, and never activates a campaign — it only produces a recommendation with reasoning."
---

---
name: "campaign-selection"
metadata:
  version: "2.2"
---

# Campaign Selection — C1-C5 Edition

Decide which single campaign a PTB-scored, Qualified lead enters — and produce a reason a BDM can check, not just a name.

## The one thing to understand before anything else

**Campaigns are now C1-C5 only.** These are the actual Saleshandy sequences with verified senders and limits, live in Saleshandy following the platform migration. The routing decision is driven by segment (agency, SaaS, product company) and signal (funding, hiring, specific technical need), but the **output is always a C1-C5 campaign name** — the ones that actually exist. The live Saleshandy sequence ID is resolved by `saleshandy-distribution` at push time (by title match, never hardcoded) — this skill's job stops at naming the right C1-C5 campaign, not at tracking its current sequence ID.

This skill executes a precedence walk: Source → Segment → Signal → Persona, stopping at the first match. The walk outputs one C1-C5 campaign. The six-dimension match assessment (Steps 8) confirms fit and produces a confidence score and credible alternative — which is where explainability comes from.

## Scope — and the boundary that matters

**Owns:** taking a single PTB-scored company and returning one selected campaign (C1-C5), with reasoning, a confidence rating, and a named alternative.

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Deciding whether the company is worth pursuing | `lead-qualification` |
| Calculating the priority score | `ptb-scoring` |
| Writing the campaign assignment into Zoho | `crm-update` skill |
| Drafting or personalizing the actual email/LinkedIn copy, or deciding LinkedIn eligibility | `email-personalization` skill |
| Activating a campaign, changing its status, or adding a lead to Saleshandy | Nobody, automatically. Human approval required before outreach |

## Context files — reference, never restate

| Document | What it supplies |
|---|---|
| `campaigns.md` | The authority. Per-campaign definitions (Target ICP, Buying Signals, Disqualification Signals), the live C1-C5 campaign registry (Saleshandy sequence names, sender mailboxes, status) |
| `icp.md` | Segment definitions (Agency, SaaS, Product Company) backing the Selection Principle's "Segment" step |
| `services.md` | Recommended Services per campaign, and Business Problems Solved for the Business Challenge Match dimension |
| `case_studies.md` | Proof points to cite in Reason for Selection |
| `pricing.md` | Commercial context if a campaign choice has pricing implications worth flagging |
| `company.md` | General company facts if needed for edge-case reasoning |
| `ptb-scoring` | Owns the score and tier this skill gates on, and most of the firmographic/signal data this skill reuses rather than re-gathering |

---

# REQUIRED INPUTS

Company Name · Industry · Country · Employee Count · Revenue (if available) · Technology Stack (as captured during qualification/PTB — there is no dedicated Zoho field for this; read it from those upstream outputs, not from a Zoho query) · Business Description · PTB Score · Buying Signals · Business Challenges · Decision Makers · Growth Indicators

All of this should already exist from the `lead-qualification` and `ptb-scoring` passes. Re-read those outputs rather than re-researching — the only new work this skill does is match the existing profile against C1-C5 campaign definitions.

---

# WORKFLOW

## Step 1 — Gate on PTB Score

| PTB Score | Action |
|---|---|
| 70 and above (Warm / High Priority) | Proceed |
| 60–69 (Borderline) | Stop. `ptb-scoring` already recommends manual review — campaign selection on an unreviewed Borderline lead front-runs that review |
| Below 60 (Reject) | Stop. Do not select a campaign. Log the reason |

## Step 2 — Pull the company profile forward

Industry, business model, technology maturity, and growth stage should already be established from qualification and PTB scoring. Read those outputs. Only investigate if something material has changed since.

## Step 3 — Confirm the primary business challenge

Reference `services.md`'s Business Problems Solved. This is usually already established — confirm it, don't redo it.

## Step 4 — Confirm buying signals

Reference the signal already identified during qualification and PTB scoring. If the strength or type of signal has shifted, note it — the Selection Principle's "Signal" step depends on getting this right.

## Step 5 — Walk the Selection Principle, in order

Apply the precedence walk exactly, one step at a time, and stop as soon as one step resolves the decision:

### 5a. Source
Referral or warm partner introduction?
- **YES** → Determine campaign by segment/signal in conversation (continue to 5b below)
- **NO** → Continue to Segment

### 5b. Segment
What does the company sell?

| Segment | → Campaign Family | Action |
|---|---|---|
| **Agency** (sells services, has delivery function) | → **C2** | Agency → C2 (Engineering Pods & Staff Augmentation). Decision complete. |
| **SaaS** (sells product, VC-funded, scaling) | → **Continue to Signal** | |
| **Product Company** (bootstrapped or acquired, owns product) | → **Continue to Signal** | |

### 5c. Signal (for SaaS/Product only)
What's the dominant buying signal?

| Signal | → Campaign | Reasoning |
|---|---|---|
| Funding announced within 6 months | **C1** | Product roadmap scaling → product engineering focus |
| Active senior engineering roles open 60+ days | **C2** | Hiring signal → pods/augmentation for immediate gap-fill |
| Platform/cloud/DevOps modernization need | **C3** | Infrastructure & platform engineering focus |
| Integration, middleware, or data-flow work | **C4** | Middleware & API integration focus |
| Feature outsourcing or legacy modernization | **C5** | Enterprise custom development, long-term modernization |
| No clear signal (default) | **C2** | Safe default; pods/augmentation for flexible capacity |

### 5d. Persona
This determines sender/tone within the selected campaign, not the campaign itself.

| Persona | → Sender | Tone |
|---|---|---|
| Founder, CEO | rajeev@ | Founder-to-founder, business outcomes |
| CTO, VP Engineering, Head of Delivery | manish@ | Technical, architecture, scalability |
| COO, Operations, MD | pritamjit@ | Consultative, operations, efficiency |

## Step 6 — Confirm against the campaign's own rules

Once the precedence walk points at a campaign, read that specific campaign's definition in `campaigns.md` and confirm:
- The company's segment/profile matches the campaign's Target ICP
- The company does NOT trip that campaign's Disqualification Signals
- The business challenge and signal genuinely align with what the campaign targets

If the company trips a Disqualification Signal, work back through Step 5 for the next-best fit.

## Step 7 — Score the selected campaign (and strongest runner-up) on six dimensions

This is where confidence comes from. Precedence already made the pick in Steps 5–6; this step explains it.

For the selected campaign and the next-most-plausible alternative, rate each dimension:

| Dimension | What it checks |
|---|---|
| **Industry Match** | Does the company's segment match this campaign's Target ICP? |
| **Business Challenge Match** | Does the confirmed problem match this campaign's documented Business Problems? |
| **Buying Signal Match** | Does the signal match this campaign's documented Buying Signals, and at what strength? |
| **Technology Match** | Does the stack fit what this campaign's Recommended Services deliver? |
| **Decision Maker Match** | Does the contact match this campaign's documented decision-maker profile? |
| **Service Match** | Do this campaign's Recommended Services plausibly solve the confirmed challenge? |

Rate each: **Excellent / Strong / Possible / Weak**

Roll up into one overall confidence:

| Pattern | Campaign Confidence |
|---|---|
| Most dimensions Excellent, none Weak | **High** |
| Mostly Strong, one or two Possible | **Medium** |
| Multiple Possible or any Weak on a critical dimension | **Low** — flag this; worth a human glance before outreach |

If the runner-up's profile is close (within one tier on most dimensions), name it as **Alternative Campaign**. Otherwise, say "None credible."

---

# DECISION RULES

- **Never select more than one primary campaign.** Exactly one C1-C5 campaign should fit once precedence is applied correctly.
- **Never select a campaign whose Disqualification Signals the company trips.** Feasibility overrides fit.
- **Always use C1-C5.** Never output List A-E, Campaign 1–5, or any other taxonomy.

---

# EXCEPTION HANDLING

| Situation | Action |
|---|---|
| No C1-C5 campaign fits after working through Steps 5–6 | Recommend Manual Review. Name which segment the company fits, even if imperfectly |
| Business challenge is unclear even after re-reading qualification and PTB outputs | Recommend further discovery before committing to a campaign |
| The precedence walk and the six-dimension scoring point at different campaigns | Flag the discrepancy specifically rather than silently picking whichever looks more confident |

---

# VALIDATION

Before returning a selection, confirm:

- [ ] The chosen campaign is one of **C1, C2, C3, C4, or C5** — never List A-E, never other taxonomy
- [ ] Campaign's Target ICP from `campaigns.md` is satisfied
- [ ] The company doesn't trip that campaign's Disqualification Signals
- [ ] Business challenge and buying signal genuinely align with what the campaign targets
- [ ] Technology fit has been checked against the campaign's Recommended Services
- [ ] Campaign Confidence reflects the six-dimension scoring
- [ ] Alternative Campaign named, if any, is genuinely close
- [ ] The selected campaign name matches one of the five rows in the Campaign Registry below (the live Saleshandy sequence ID is resolved by `saleshandy-distribution` at push time, not tracked here)

---

# OUTPUT FORMAT

```
## Selected Campaign
C[1-5] — [Campaign Name]

## Reason for Selection
[The precedence path taken (Source → Segment → Signal → Persona)
and why this company fits the selected campaign's profile]

## Campaign Confidence
High | Medium | Low
[From the six-dimension rollup. Name any dimension that scored
Possible or Weak]

## Business Challenges
[The confirmed challenge this campaign addresses]

## Buying Signals Used
[The specific signal(s) that drove the Signal step, with strength]

## Alternative Campaign
[Named runner-up with its own confidence, or "None credible"]

## Recommended Service Focus
[From this campaign's Recommended Services, narrowed to fit
this specific company]

## Recommended Sender
[rajeev@ | manish@ | pritamjit@]
[Why this persona/sender fits the decision maker]

## Data Gaps
[Anything that would change the selection if resolved]
```

When selecting for a batch, lead with a compact table — company, selected campaign, confidence, one-line reason — then expand only Low-confidence selections.

---

# CAMPAIGN REGISTRY (C1-C5)

| Campaign | Name | Saleshandy Sequence ID (reference only) | Sender | Daily Limit | Primary Use Case |
|---|---|---|---|---|---|
| **C1** | AI-Enabled Product Engineering | `68Pvv34nP7` | rajeev@ | 30 | SaaS CTOs; product roadmap scaling |
| **C2** | Engineering Pods & Staff Augmentation | `1qPBL69vzD` | manish@ | 30 | Agencies; SaaS scaling; hiring gaps |
| **C3** | Platform Engineering & Cloud Modernization | `Mgw473olzA` | manish@ | 30 | Platform/cloud/DevOps modernization |
| **C4** | Middleware & API Integration | `glwGOA9Rw6` | pritamjit@ | 30 | Integration, middleware, data flows |
| **C5** | Enterprise Custom Development & Modernization | `6vaKGDl4aW` | rajeev@ | 30 | Enterprise features, legacy modernization |

**These IDs are Saleshandy sequence IDs, verified live on August 8, 2026 — not the prior-platform campaign UUIDs this table listed before the platform migration.** They are shown for human reference only. `saleshandy-distribution` never reads this table or hardcodes an ID from it — it resolves the current sequence ID at push time by matching the campaign's title prefix (`C1 - `, `C2 - `, ...) via `list_sequences`, specifically because IDs can change if a sequence is ever recreated. If this table and a live Saleshandy lookup ever disagree, the live lookup is correct and this table is stale.

---

# RELATED SKILLS

| Skill | Relationship |
|---|---|
| `lead-qualification` | Upstream. Establishes that the company is worth pursuing at all |
| `ptb-scoring` | Upstream, immediately before this skill. Gates entry and supplies the profile this skill reuses |
| `email-personalization` | Downstream. Takes the selected C1-C5 campaign and finds the verified, company-specific fact that instantiates its messaging angle for both Email and, where selected, LinkedIn |
| `crm-update` | Owns writing the campaign assignment into CRM and enforces the BDM approval gate |

---

# SUCCESS CRITERIA

| Measure | Target |
|---|---|
| Selections that are C1-C5 only (no List A-E) | 100% |
| Selections a human can re-derive from stated reasoning | 100% |
| Selections that trip the chosen campaign's Disqualification Signals | Zero |
| Low-confidence selections sent without being flagged | Zero |

---

# VERSION

Version 2.2 · Owner: Zediant AI Sales Team · August 8, 2026

**Change in 2.2:** Replaced every remaining reference to the prior sending platform (description, scope, context files, validation checklist, Campaign Registry) with Saleshandy, matching the platform migration already reflected in `crm-update`, `scheduler-lead-population`, `email-personalization`, and `saleshandy-distribution`. The Campaign Registry's ID column was also factually wrong, not just mislabeled — it held prior-platform campaign UUIDs that don't correspond to anything live. Replaced with the real Saleshandy sequence IDs (verified live via `list_sequences` on August 8, 2026) and an explicit note that `saleshandy-distribution` resolves these dynamically and never hardcodes from this table, since sequence IDs can change if a sequence is recreated.

**Change in 2.1:** Clarified that Technology Stack is read from upstream qualification/PTB output, not a dedicated Zoho field (that field was deleted August 8, 2026 — see `crm-update` v4.0). Noted `email-personalization` now also handles LinkedIn content, not just email.

**Change in 2.0:** Removed all List A-E references. Campaign routing now uses C1-C5 exclusively — at the time these ran on a different sending platform; see the 2.2 change note below for the later migration to Saleshandy. Updated Selection Principle walkthrough, campaign registry, and output format to reflect C1-C5 taxonomy only.

