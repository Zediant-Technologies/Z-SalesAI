---
name: campaign-selection
description: "Zediant campaign selection SOP — selects exactly one C1-C5 campaign for a Qualified lead using business problem, technical need, business signal, ICP fit, persona fit, and the single PTB Score (Initial Buying Signal). PTB is consumed, never calculated here. No post-engagement PTB model, no PTB gate, no CRM writes, no outreach activation."
---

---
name: "campaign-selection"
metadata:
  version: "3.1"
---

# Campaign Selection — C1-C5 Edition

Decide which single campaign a Qualified lead enters — and produce a reason a BDM can check, not just a name. The Buying Signal factor this skill consumes is the single numeric **PTB Score (Initial Buying Signal)** produced by `ptb-scoring`. This skill never calculates PTB itself.

## The one thing to understand before anything else

**Campaigns are now C1-C5 only.** These are the actual Saleshandy sequences with documented limits, live in Saleshandy as of the migration from Instantly. Sender/mailbox assignment is not tracked by this skill or by `campaigns.md` — per explicit human instruction, which email account sends a given campaign is an operational Saleshandy configuration detail, not a campaign-selection concern. Campaign selection is **service-based**: the question is which C1-C5 service the prospect most plausibly needs, based on their actual business problem/technical need, business signal, ICP fit, PTB/buying signal, and persona — evaluated together as a weighted evidence score, not resolved by any single attribute (industry, company type, lead source, or persona) acting alone. The **output is always a C1-C5 campaign name** — the ones that actually exist. The live Saleshandy sequence is resolved by `saleshandy-distribution` at push time (by campaign name/title, never by an ID tracked in this skill) — this skill's job stops at naming the right C1-C5 campaign, not at tracking its sequence identity.

## Scope — and the boundary that matters

**Owns:** taking a single Qualified company with its numeric PTB Score (Initial Buying Signal) and returning one selected campaign (C1-C5), with reasoning, a fit score, and a named alternative where genuinely relevant. **Never calculates, estimates, or changes PTB.**

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Deciding whether the company is worth pursuing | `lead-qualification` |
| Calculating the priority score | `ptb-scoring` | Sole owner of the single PTB Score (Initial Buying Signal), calculated before outreach and consumed here; this skill never calculates or changes PTB |
| Writing the campaign assignment into Zoho | `crm-update` skill |
| Drafting or personalizing the actual email/LinkedIn copy, or deciding LinkedIn eligibility | `email-personalization` skill |
| Resolving which live Saleshandy sequence a campaign name maps to | `saleshandy-distribution` skill |
| Activating a campaign, changing its status, or adding a lead to Saleshandy | Nobody, automatically. Human approval required before outreach |

## Context files — reference, never restate

**For day-to-day selection, `context/playbooks/C{1-5}.md` carries everything below per campaign already** — Business Problems, Target ICP, Buying/Disqualification Signals, case study with confidentiality notes, portfolio share — pre-extracted from the same sources. Score all plausible candidates' playbooks, pick the strongest Campaign Fit Score. Open the full docs below only for a genuinely novel edge case a playbook doesn't resolve.

| Document | What it supplies |
|---|---|
| `campaigns.md` | The authority. Per-campaign definitions (Business Problems, Target ICP, Buying Signals, Disqualification Signals), the campaign-fit scoring model, portfolio allocation targets, and the live C1-C5 campaign registry (daily limit) |
| `icp.md` | ICP fit signals feeding the ICP Fit factor. ICP does not determine the campaign by itself |
| `services.md` | Recommended Services per campaign, and Business Problems Solved for the Business Problem/Technical Need factor |
| `case_studies.md` | Proof points to cite in Reason for Selection — respect current governance (e.g. C1 has no approved case study; do not cite CS-04 or CS-07 for C1) |
| `pricing.md` | Commercial context if a campaign choice has pricing implications worth flagging |
| `company.md` | General company facts if needed for edge-case reasoning |
| `ptb-scoring` | Sole owner of the single PTB Score (Initial Buying Signal), calculated before outreach and consumed here; this skill never calculates or changes PTB |

---

# REQUIRED INPUTS

Company Name · Industry · Country · Employee Count · Revenue (if available) · Technology Stack (as captured during qualification/scoring — there is no dedicated Zoho field for this; read it from those upstream outputs, not from a Zoho query) · Business Description · Buying Signal factor: numeric PTB Score (Initial Buying Signal) · Buying Signals · Business Challenges · Decision Makers · Growth Indicators · Referral/partner-introduction status (if known)

All of this should already exist from the `lead-qualification` pass plus the single PTB Score from `ptb-scoring`. Re-read those outputs rather than re-researching — the only new work this skill does is match the existing profile against C1-C5 campaign definitions. The normal, expected state for every lead reaching this skill pre-engagement (e.g. from Scheduler 1) is a numeric PTB Score (Initial Buying Signal) from `ptb-scoring` PTB scoring — that is not missing information and never triggers re-research or a Human Review escalation on its own. True `N/A / Not Yet Scored` is now a rare fallback, not the default.

---

# WORKFLOW

## Step 1 — Confirm PTB Score

`ptb-scoring` supplies one numeric **PTB Score (Initial Buying Signal)** for Scheduler 1 leads. PTB is the single buying-signal score used by this skill. This skill consumes the score and never recalculates it.

- A numeric PTB score is expected for every Qualified Scheduler 1 survivor.
- Do not apply any post-engagement PTB threshold. There is no separate post-engagement PTB model in the current architecture.
- Do not reject, stop, or hold a Qualified lead because PTB is below an arbitrary campaign-selection threshold. PTB is an evidence input to campaign fit and a prioritization signal, not a qualification gate.
- If PTB is genuinely missing, flag `DATA GAP`, do not invent or estimate a value, and continue campaign selection from the other available evidence if the workflow permits.

**Scheduler 1 compatibility:** the normal flow is `Lead Qualification → ICP Score → PTB Score (Initial Buying Signal) → Campaign Selection`.

## Step 2 — Pull the company profile forward

Industry, business model, technology maturity, and growth stage should already be established from qualification and PTB scoring. Read those outputs. Only investigate if something material has changed since.

## Step 3 — Confirm the primary business problem / technical need

Reference `services.md`'s Business Problems Solved and each C1-C5 campaign's own Business Problems section in `campaigns.md`. This is usually already established — confirm it, don't redo it. This is the single largest factor (35%) in the campaign-fit score below.

## Step 4 — Confirm business signal and Buying Signal factor

Reference the business signal and the PTB Score already identified upstream. PTB contributes directly to the Campaign Fit Score as the Buying Signal factor.

## Step 5 — Score campaign fit and determine the dominant service need

**The primary question is: "What service does this prospect most plausibly need, based on the evidence available?"** Segment (agency, SaaS, product company), lead source, and persona are supporting evidence for that question — none of them independently determines the campaign.

### 5a. Identify plausible candidate campaigns

Using the confirmed business problem/technical need from Step 3, shortlist which of C1-C5 could plausibly fit by comparing against each campaign's own Business Problems in `campaigns.md`. Illustrative, non-exhaustive examples of how a dominant need maps to a campaign:

| Dominant service need observed | Illustrative campaign |
|---|---|
| Product engineering / SaaS roadmap / scalability need | C1 |
| Engineering capacity gap / hiring pressure / need for team extension (including an agency needing delivery capacity) | C2 |
| Infrastructure / cloud / DevOps / deployment reliability need | C3 |
| Connecting systems / APIs / middleware / data exchange need (including an agency needing integration work) | C4 |
| Broader enterprise custom development or legacy modernization not fitting C1-C4 | C5 |

These are starting points for evidence-gathering, not standing rules — a digital agency, a SaaS company, or a product company can each land in any of C1-C5 depending on the actual dominant need. Do not let industry, company type, lead source, or persona alone decide the outcome; they inform the score in 5b.

### 5b. Score each plausible candidate on the campaign-fit model

Use `campaigns.md`'s Campaign Fit Scoring model. The current Scheduler 1 state uses the single PTB Score (Initial Buying Signal) as the Buying Signal factor.

| Factor | Weight |
|---|---:|
| Business Problem / Technical Need | **35%** |
| Business Signal | **25%** |
| ICP Fit | **15%** |
| PTB / Buying Signal | **15%** |
| Persona Fit | **10%** |
| **Total** | **100%** |

```
Campaign Fit Score =
  (Business Problem / Technical Need × 35%)
+ (Business Signal × 25%)
+ (ICP Fit × 15%)
+ (PTB / Buying Signal × 15%)
+ (Persona Fit × 10%)
```

The PTB / Buying Signal factor is the numeric PTB Score supplied by `ptb-scoring`. It is consumed here, not recalculated. Use the same five-factor formula for Scheduler 1. Do not renormalize or create another PTB variant.

For every candidate, first score each applicable factor on a 0–100 evidence scale, then calculate the Campaign Fit Score using the fixed weights above.

### 5c. Select the strongest evidence-based fit

The candidate with the strongest Campaign Fit Score is the selection, subject to the disqualification check in Step 6. Do not select a campaign because it is under its portfolio allocation target, and do not pass over the strongest-fit campaign because it is already at or above target — **portfolio allocation percentages are planning targets only and never override evidence-based fit.** If the qualified pipeline genuinely doesn't produce enough evidence for a given campaign, that campaign runs below target and the shortfall is reported as a portfolio gap, not manufactured by re-scoring a weaker fit upward.

### 5d. Referral handling

A referral or partner introduction is **not** a separate campaign. A referred lead is scored and selected into whichever of C1-C5 the evidence supports, exactly as above. Referral status may change tone, opening, or cadence downstream — it does not create a separate taxonomy and does not override the service-need-based selection.

## Step 6 — Confirm the selected campaign against its own rules

Once Step 5 produces a leading candidate, read that specific campaign's definition in `campaigns.md` and confirm:
- The company's profile matches the campaign's Target ICP (this is also reflected in the ICP Fit factor above)
- The company does NOT trip that campaign's Disqualification Signals
- The business problem and signal genuinely align with what the campaign targets

If the leading candidate trips a Disqualification Signal, move to the next-strongest-scored candidate from Step 5b and re-check.

## Step 7 — Finalize confidence and alternative

| Pattern | Campaign Confidence |
|---|---|
| Campaign Fit Score clearly highest, evidence strong across most factors | **High** |
| Campaign Fit Score highest but by a narrow margin, or evidence thin on 1–2 factors | **Medium** |
| Two or more candidates score within a similar range, or evidence is thin/missing on a factor central to the decision | **Low** — see Human Review Conditions below |

If a runner-up candidate's Campaign Fit Score is genuinely close (within a similar range) to the selected campaign, name it as **Alternative Campaign** with a brief reason it was not selected. Otherwise, say "None credible."

---

# DECISION RULES

- **Never select more than one primary campaign.** Exactly one C1-C5 campaign is the output.
- **Never select a campaign whose Disqualification Signals the company trips.** Feasibility overrides fit.
- **Campaign fit — not portfolio allocation — decides the campaign.** The 25/25/15/25/10 portfolio percentages are planning/monitoring targets only. Never move a lead into a weaker-fit campaign merely to satisfy a portfolio percentage, and never withhold a lead from its strongest-fit campaign because that campaign is already at or above target.
- **Referral or partner introduction is not a separate campaign.** It may affect tone, opening, or cadence only.
- **Do not output a Saleshandy sequence ID.** Sequence resolution by campaign name/title is owned entirely by `saleshandy-distribution`; this skill never stores or repeats a sequence ID.
- **Always use C1-C5.** Never output List A-E, Campaign 1–5, or any other taxonomy.

---

# EXCEPTION HANDLING / HUMAN REVIEW CONDITIONS

Escalate to **HUMAN REVIEW REQUIRED** rather than forcing a selection when:

| Situation | Action |
|---|---|
| No C1-C5 campaign fits after working through Steps 5–6 | Recommend Human Review. Name which candidate came closest, even if imperfectly |
| Business problem/technical need is unclear even after re-reading qualification and PTB outputs | Recommend further discovery before committing to a campaign |
| Two or more candidates have materially similar Campaign Fit Scores that the available evidence cannot separate | Flag the discrepancy specifically rather than silently picking whichever looks more confident |
| A DATA CONFLICT exists in the underlying context (`campaigns.md`, `icp.md`, `case_studies.md`) that bears on this selection | Escalate; never resolve a DATA CONFLICT by choosing whichever interpretation produces a better-looking campaign |
| Required information is missing | Recommend further discovery |
| Enterprise opportunity requiring 12+ engineers or heavy procurement (per `campaigns.md`'s existing escalation rule) | Escalate to a human; do not invent a new campaign or category to accommodate it |
| A decision would require inventing or assuming facts not present in the source data | Escalate rather than assume |

---

# VALIDATION

Before returning a selection, confirm:

- [ ] The chosen campaign is one of **C1, C2, C3, C4, or C5** — never List A-E, never other taxonomy
- [ ] Selection was made from the five-factor Campaign Fit Score using the single numeric PTB Score as the 15% Buying Signal factor
- [ ] PTB Score (Initial Buying Signal) state was never gated by the Post-Engagement PTB 70+/60-69/<60 thresholds — that gate applies only to the PTB state
- [ ] no second PTB score or post-engagement PTB model was created
- [ ] If the state was (missing PTB state), no score value was invented, estimated, or treated as 0 or as a rejection — campaign selection proceeded on the renormalized four-factor score
- [ ] Campaign's Target ICP and Business Problems from `campaigns.md` are satisfied
- [ ] The company doesn't trip that campaign's Disqualification Signals
- [ ] Portfolio allocation (25/25/15/25/10) was not used to justify or override the selection
- [ ] Exactly one campaign is returned as the selection
- [ ] Campaign Confidence reflects the Campaign Fit Score pattern from Step 7
- [ ] Alternative Campaign named, if any, is genuinely close in score
- [ ] No Saleshandy sequence ID appears anywhere in the output
- [ ] Referral status (if any) did not create or imply a separate campaign
- [ ] Any DATA CONFLICT or missing-evidence situation was escalated, not guessed

---

# OUTPUT FORMAT

```
Primary Campaign:
C1 / C2 / C3 / C4 / C5

Campaign Name:
[exact current campaign name]

Score Breakdown:
[Show the evidence score (0-100) and weighted contribution actually calculated for this lead, not the weights alone.]

PTB Score — example format, use this lead's real number, not this illustrative one:
- Business Problem / Technical Need: 90/100 × 35% = 31.50
- Business Signal: 70/100 × 25% = 17.50
- ICP Fit: 80/100 × 15% = 12.00
- PTB / Buying Signal (Initial Buying Signal): 75/100 × 15% = 11.25
- Persona Fit: 90/100 × 10% = 9.00
Campaign Fit Score: [sum of the five weighted contributions]/100

PTB Score (Initial Buying Signal) numeric — the same five-factor weights, factor explicitly labeled to avoid confusion with PTB scoring:
- Business Problem / Technical Need: 90/100 × 35% = 31.50
- Business Signal: 70/100 × 25% = 17.50
- ICP Fit: 80/100 × 15% = 12.00
- Buying Signal (PTB Score (Initial Buying Signal)): 64/100 × 15% = 9.60
- Persona Fit: 90/100 × 10% = 9.00
Campaign Fit Score: [sum of the five weighted contributions]/100

If PTB is missing unexpectedly, flag DATA GAP and do not invent a value. Campaign selection may continue only if the workflow explicitly permits it.

# CAMPAIGN REGISTRY (C1-C5)

| Campaign | Name | Daily Limit | Primary Use Case |
|---|---|---|---|
| **C1** | AI-Enabled Product Engineering | 30 | SaaS CTOs; product roadmap scaling |
| **C2** | Engineering Pods & Staff Augmentation | 30 | Agencies; SaaS scaling; hiring gaps |
| **C3** | Platform Engineering & Cloud Modernization | 30 | Platform/cloud/DevOps modernization |
| **C4** | Middleware & API Integration (ZCoupler) | 30 | Integration, middleware, data flows |
| **C5** | Enterprise Custom Development & Modernization | 30 | Enterprise features, legacy modernization |

Sender/mailbox assignment per campaign is intentionally not tracked here — per explicit human instruction (September 2026), which account sends a campaign is a Saleshandy configuration detail this skill and `campaigns.md` no longer encode. `saleshandy-distribution` resolves live sending configuration directly in Saleshandy at push time.

This skill does not store, display, or resolve Saleshandy sequence IDs. `saleshandy-distribution` is solely responsible for resolving the current live Saleshandy sequence by matching the campaign's name/title at push time — no ID is duplicated here.

---

# RELATED SKILLS

| Skill | Relationship |
|---|---|
| `lead-qualification` | Upstream. Establishes that the company is worth pursuing at all |
| `ptb-scoring` | Sole owner of the single PTB Score (Initial Buying Signal), calculated before outreach and consumed here; this skill never calculates or changes PTB |
| `email-personalization` | Downstream. Takes the selected C1-C5 campaign and finds the verified, company-specific fact that instantiates its messaging angle for both Email and, where selected, LinkedIn |
| `crm-update` | Owns writing the campaign assignment into CRM and enforces the BDM approval gate |
| `saleshandy-distribution` | Downstream. Resolves the selected campaign name/title to the current live Saleshandy sequence; owns all sequence-ID resolution |

The normal workflow is: Lead qualification → ICP Score → PTB Score (Initial Buying Signal) → Campaign selection → Personalization → CRM → BDM approval → Saleshandy. Campaign selection never activates outreach and never bypasses BDM approval.

---

# SUCCESS CRITERIA

| Measure | Target |
|---|---|
| Selections that are C1-C5 only (no List A-E) | 100% |
| Selections made from the correct Campaign Fit Score for the lead's Buying Signal state (five-factor for both the applicable numeric buying-propensity state, renormalized four-factor for missing PTB state when), not segment/industry/persona alone | 100% |
| PTB Score (Initial Buying Signal) state selections incorrectly gated by the PTB hard threshold | Zero |
| the two numeric buying-propensity states scores confused, converted, or mislabeled in output | Zero |
| Selections justified by portfolio allocation percentage instead of evidence-based fit | Zero |
| Selections a human can re-derive from stated reasoning | 100% |
| Selections that trip the chosen campaign's Disqualification Signals | Zero |
| Low-confidence or conflicted selections sent without being flagged as HUMAN REVIEW REQUIRED | Zero |
| Saleshandy sequence IDs appearing in this skill's output | Zero |

---


# VERSION

Version 3.1 · September 2026

**Change in 3.1 — sender/mailbox assignment removed (SURGICAL, EDIT-ONLY):** Per explicit human instruction, this skill no longer tracks or surfaces per-campaign sender mailbox assignment — it does not matter to the business which account sends which campaign, and that is a Saleshandy configuration detail, not a campaign-selection concern. Removed the "Sender is the documented campaign-level alias only" decision rule, the sender-identity-resolution Human Review Condition, the sender validation checklist line, and the "Sender (documented alias)" column from the Campaign Registry table (daily limits and use-case notes unchanged). `saleshandy-distribution` owns actual sending configuration. No campaign taxonomy, scoring model, weight, or threshold changed.

Version 3.0 · Single PTB Initial Buying Signal architecture · September 6, 2026

Current operating rule: PTB is one numeric 0–100 score calculated before outreach for Qualified leads. Campaign Selection consumes that score as the Buying Signal factor and never calculates or gates on PTB. No second post-engagement PTB model exists in the current workflow.
