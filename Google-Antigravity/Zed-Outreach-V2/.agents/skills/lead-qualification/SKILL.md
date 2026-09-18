---
name: "lead-qualification"
description: "Zediant's lead qualification SOP — decide whether a company is worth pursuing before any sales effort is spent on it. Use this whenever a specific company or contact needs assessing: \"should we go after X\", \"is this a good lead\", \"qualify these leads\", \"does this company fit our ICP\", \"worth pitching to\", or when reviewing leads imported into Zoho, arriving inbound, mentioned in a referral, or handed over from prospecting. Trigger even when the user doesn't say \"qualify\" — any request to judge fit, filter a lead list, or decide whether to pursue an account belongs here. Returns QUALIFIED / RESEARCH_REQUIRED / REJECTED with reasoning. Its Step 6 Business Challenges finding must be one self-contained, noun/gerund-led sentence, since that exact wording is later merged verbatim into live Apollo email templates in two grammatically different slots. Stops at the verdict; it does not calculate PTB scores, write to CRM, or select campaigns."
---

# Lead Qualification

Decide whether a company is worth Zediant's sales effort, before that effort is spent.

The point of qualifying is not to be selective for its own sake. Zediant has one BDM, one founder closing, and roughly 90% of revenue in a single client. Every hour spent on a poor-fit prospect is an hour not spent reducing that concentration. A qualification call that says "no" quickly is as valuable as one that says "yes".

## Scope — and the boundary that matters

**Owns:** assessing a named company or contact against the ICP, producing a QUALIFIED / RESEARCH_REQUIRED / REJECTED verdict with reasoning, and flagging what's missing.

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Finding or sourcing prospects | `apollo-search-builder` |
| Enriching contact data | `apollo-search-builder` |
| PTB scoring, including post-engagement re-scoring | `ptb-scoring` skill (`ptb_scoring.md`) |
| CRM writes and the `Lead_Status` BDM approval gate | `crm-update` skill |
| Campaign selection and messaging | `campaign-selection` skill, `campaigns.md` |

PTB scoring is outside the scope of lead-qualification. This skill does not calculate Initial Buying Signal Score or Post-Engagement PTB. `ptb-scoring` owns both stages. Post-Engagement PTB is N/A / Not Yet Scored before applicable engagement evidence exists. `ptb-scoring` owns both Initial Buying Signal Score (Path A) and Post-Engagement PTB Score (Path B); this skill never calculates either.

### How this differs from apollo-search-builder

Both apply the ICP. The difference is **where the lead came from**.

`apollo-search-builder` scores leads it sourced itself, inline, to decide whether enrichment credits are worth spending. That scoring is a cost gate on its own workflow.

This skill qualifies a company that arrived from **anywhere else** — a CRM import, an inbound enquiry, a referral, a name someone mentioned in a meeting, a list a partner sent over, a company the founder noticed. There are no Apollo credits at stake and no search to design. The question is only: is this worth pursuing?

If a request involves *finding* companies, that's the other skill. If it involves *judging* companies already named, it's this one.

## Context files — reference, never restate

**For day-to-day qualification, read `context/playbooks/_core-reference.md` instead of the full source docs** — it carries the current ICP Score model (six weighted dimensions, matching this skill exactly), hard/soft disqualifiers, excluded industries, geography/capacity ceiling, escalation triggers, and the unsubstantiated-claims list, pre-extracted from `icp.md`/`company.md`/`services.md`/`case_studies.md`/`competitors.md`. If the lead's likely campaign is already known, `context/playbooks/C{1-5}.md` adds that campaign's own business problems and disqualification signals.

`icp.md` remains the authority of record — read it directly rather than the playbook only for a genuinely novel edge case (a DATA CONFLICT, an excluded industry not listed, a scoring dispute). Duplicating ICP content into this skill itself (as opposed to the playbook, which is an intentional, labeled digest) is how the two drift apart.

Full source docs, for edge cases the playbook doesn't cover: `services.md` capability boundaries → what Zediant can actually deliver · `company.md` capacity ceiling and commercial position · `campaigns.md` segment-to-campaign mapping · `case_studies.md` vertical proof depth · `competitors.md` competitor identification · `pricing-public.md` approved/context-restricted commercial guidance and internal viability references

---

# THE QUALIFICATION MODEL

Two things determine the verdict, and they are not the same kind of test.

## 1. Hard disqualifiers — binary, checked first

A hard disqualifier means Zediant **cannot or will not** serve this company, regardless of how attractive it looks. These override any score.

Check these before doing any other work. They're cheap to check and they end the assessment, so running them first saves the rest of the effort.

| Disqualifier | Why it's absolute |
|---|---|
| Needs 50+ engineers, or a ramp beyond 5–7 developers in three months | Exceeds documented delivery capacity. Winning it would damage delivery |
| Core need is AI/ML research, model training, computer vision, or speech AI | Outside capability. `services.md` marks these Not Supported |
| Needs low-code/no-code platform work | No capability documented |
| Needs embedded, firmware, SCADA, industrial control, robotics control, or telematics software | Outside capability |
| Requires full on-site presence as a non-negotiable | No in-person capability |
| Expects free POC or unpaid tender documentation | Prohibited by commercial policy |
| Competing purely on lowest hourly rate | Zediant has deliberately chosen not to compete there |
| Requires certifications Zediant cannot evidence (ISO 27001, ISO 9001, CMMI) | Cannot be provided |
| Public sector tender without a Teaming Agreement | Actively deprioritised |
| Recruitment or staffing agency | Competitor in the augmentation motion, not a buyer |
| University, college, bootcamp, student, or individual | Not a commercial buyer |
| Direct competitor seeking to resell capacity without a partner agreement | Competitive risk |
| Existing Zediant client | Not a new lead — route to account management |

**A company scoring 90 with a hard disqualifier is REJECTED, not RESEARCH_REQUIRED.** The score measures attractiveness; the disqualifier measures feasibility. Attractive and infeasible is still a no.

## 2. Fit score — graded, uses the existing model

Apply the **ICP Score** model defined in `icp.md`. Do not invent a new one, and don't reach for the `ptb-scoring` skill's model here either — PTB scoring is outside the scope of lead-qualification. This skill does not calculate Initial Buying Signal Score or Post-Engagement PTB. `ptb-scoring` owns both stages. Post-Engagement PTB is N/A / Not Yet Scored before applicable engagement evidence exists. The separate `ptb-scoring` skill owns PTB scoring and post-engagement re-scoring; running it here would duplicate work and produce two different numbers for the same company.

The six ICP dimensions and their weights live in `icp.md`: Business Fit (0–25), Technical Fit (0–20), Commercial Fit (0–15), Strategic & Growth Fit (0–15), Persona Fit (0–15), and Geography Fit (0–10). Read the current `icp.md` rather than duplicating or recreating this model here. **Buying signals are not an ICP Score dimension.** They are collected as evidence and scored separately by `ptb-scoring` Path A as the Initial Buying Signal Score.

### Verdict bands

| ICP Score | Verdict | Meaning |
|---|---|---|
| 80–100 | **QUALIFIED** | Strong fit, act now |
| 50–79 | **QUALIFIED** | Solid fit, standard priority |
| 30–49 | **RESEARCH_REQUIRED** | Specific evidence or human judgement needed |
| Below 30 | **REJECTED** | Not worth pursuing |
| Any score + hard disqualifier | **REJECTED** | Feasibility overrides attractiveness |

Zediant's tiering language (Hot / Warm / Cold) maps onto this: 80+ is Hot, 50–79 Warm, below 50 Cold. Report both the numeric score and the verdict so the BDM can see how close a call it was.

---

# WORKFLOW

## Step 1 — Verify the company is real and identifiable

Confirm the company exists and you're assessing the right one. Company names collide constantly — "Integral" is a Brisbane IT consultancy and also a dozen unrelated firms worldwide.

Anchor on the **domain**, not the name. If no domain is available and the name is ambiguous, that's an identification problem, not a qualification problem — flag for manual review rather than guessing and producing a confident assessment of the wrong company.

| Situation | Action |
|---|---|
| Domain confirmed, business description available | Proceed |
| Name only, unambiguous (distinctive name, known market) | Proceed, note the assumption |
| Name only, ambiguous | **Flag for manual review.** Do not guess |
| Website dead or parked | Flag — may be defunct |
| Cannot find any trace of the company | **RESEARCH_REQUIRED** unless reliable evidence establishes that the company is not real or is defunct; do not guess |

## Step 2 — Industry and segment fit

Classify against `icp.md`. Segment governs, vertical informs.

| Band | Meaning |
|---|---|
| **Excellent** | Exact match to a primary segment ICP, in a vertical with documented delivery proof |
| **Good** | Exact segment match, vertical without direct proof |
| **Acceptable** | Adjacent segment, or right vertical but imperfect segment fit |
| **Poor** | Tenuous connection; would need a stretch to justify |
| **Reject** | On the excluded-industry list |

**The classification rule that catches most mistakes:** classify by what the company *is*, not by who its customers are. A funded SaaS company selling software to hospitals is a SaaS prospect, not a healthcare prospect. A proptech platform is SaaS, not real estate. Getting this backwards routes a good lead into an excluded industry and rejects it wrongly.

Where `icp.md` lists an industry as a focus area but with no supporting case study, say so. "Listed but unproven" is a real category and it affects how confidently the BDM can open a conversation.

## Step 3 — Company size and maturity

Assess against the size bands in `icp.md`. Where company size suggests the opportunity may be commercially too small, use the documented ICP and commercial guidance as context; do not infer a pricing floor from employee count. The ceiling exists for capacity reasons: above a certain size, engagements need a ramp Zediant cannot deliver.

| Signal | Read |
|---|---|
| Employee count | Primary size measure — most reliable |
| Revenue | Secondary. Unreliable for private companies; treat as directional |
| Funding stage | Strong maturity indicator for SaaS. Verify externally — Apollo does not carry it reliably |
| Years trading | Distinguishes established from early. Useful for agencies |
| Headcount trend | See below |

**Headcount direction matters as much as headcount size.** A company that has shrunk sharply is genuinely ambiguous: they may have cut an internal bench and now need external capacity — an excellent prospect for exactly Zediant's offer — or the business may be contracting with no budget behind the need. Both look identical in the data.

Don't resolve that ambiguity silently in either direction. Note it, score conservatively, and flag it for the BDM to qualify on the first conversation. Rejecting a bench-cutting agency loses a real opportunity; promoting a shrinking one wastes a sequence.

## Step 4 — Geographic fit

Check against the geography priority in `icp.md`.

Two things need to be true, and they're separate: the company operates in a target market, **and** the specific contact is reachable in a workable timezone. A Sydney-headquartered company's CTO based in San Francisco is a weaker lead than the firmographics suggest.

| Check | Note |
|---|---|
| Company HQ or primary market | Primary markets score highest |
| Contact's actual location | Affects overlap hours and personalisation credibility |
| Timezone overlap | India→UAE 1.5h, →Perth 2.5h, →Sydney 4.5h |
| Working week | UAE commonly Sunday–Thursday — affects outreach cadence, not qualification |
| Language | English-language business operation assumed; flag if not |

Secondary geographies aren't disqualifying but score lower and generally need a warm introduction to be worth pursuing.

## Step 5 — Decision makers

Zediant's deal size requires someone who can commit budget without extended procurement. That's the real test, not seniority for its own sake.

| Found | Read |
|---|---|
| Founder, CEO, CTO, COO, or MD identified | Strong — can commit |
| VP or Head of Engineering | Good — may need sign-off above |
| CIO or IT Director | Workable, but implies procurement |
| Engineering Manager, Product Manager only | Weak — influences, rarely decides |
| No named contact | Score persona low, flag for enrichment |
| Only non-technical, non-commercial contacts | Weak |

Where no qualifying persona exists at a company that otherwise fits well, that's a **finding, not a rejection** — name the titles worth targeting instead. The company may be worth pursuing once the right person is identified.

## Step 6 — Business challenges

Assess whether this company plausibly has a problem Zediant solves. Match observable evidence to the challenges documented in `services.md`.

The distinction worth holding: a company *could* use engineering capacity (almost any software company could) versus a company showing *evidence* of needing it. The first is not a qualification; the second is.

Evidence looks like: open engineering roles, a public roadmap that has slipped, an acquisition creating integration work, systems that visibly don't talk to each other, a platform outage, an end-of-life notice on core technology, a stated capacity constraint.

**This finding travels further than the qualification report.** `scheduler-lead-population` carries this exact wording forward, unchanged, into the `Business_Challenges` Zoho field — and from there it is merged directly into live Apollo email templates as `{{Business Challenge}}`, in two different grammatical slots across the five campaigns: as a standalone opening sentence on its own line (C2/C3/C4/C5's proof-point email), and as a subordinate clause following the word "Given" (C1's second email: *"Given {{Business Challenge}} I thought this might be worth a look."*). One string has to work in both places, so write the finding as **one self-contained sentence, phrased as a noun or gerund-led capsule rather than a full narrated paragraph** — something that reads naturally both on its own and immediately after "Given".

- Weak (report-style, multi-sentence, doesn't fit either slot cleanly): *"The company has three open senior engineering roles that have been live for over two months, and their public roadmap shows a delayed release, suggesting they may be short on delivery capacity."*
- Better (one gerund-led capsule, works standalone and after "Given"): *"three open senior engineering roles sitting unfilled for two months alongside a roadmap release that's already slipped"*

Keep the underlying evidence and hedging honest — don't strengthen a "may be" into a stated fact just to make the sentence tighter. If the evidence is genuinely uncertain, the capsule can still say so ("a hiring pattern that suggests possible capacity pressure") without losing the single-sentence, dual-fit shape.

## Step 7 — Buying-signal evidence (separate from ICP Score)

Buying signals make a lead timely rather than merely plausible, but they are **not part of the ICP Score**. Collect and preserve the evidence here; do not add buying-signal points to the ICP Score and do not calculate the Initial Buying Signal Score in this skill. `ptb-scoring` owns the separate pre-engagement Initial Buying Signal Score (Path A).

| Strength | Examples |
|---|---|
| **High intent** | Funding within 90 days · senior engineering role open 60+ days · acquisition completed · legacy end-of-life notice · outage or security finding · compliance deadline |
| **Medium intent** | Funding 3–12 months old · one or two open roles · product launch announced · market expansion · cloud migration · new CIO or CTO appointed |
| **Low intent** | Firmographic match with nothing observable · generic growth marketing · aged funding · non-engineering roles only |

**Distinguish "no signal found" from "no signal exists."** If a reasonable search turned up nothing, say *"no signal identified in available sources"* and record the evidence state conservatively; do not convert an unknown research state into an ICP penalty or a buying-signal score. If the company demonstrably shows nothing (static headcount, no news, no hiring, no announcements over a long period), that's genuinely a low score.

The difference matters because the first is a research gap that enrichment or a few minutes of searching might close, and the second is a real judgement about the company. Reporting them the same way makes the score untrustworthy.

**Verify funding claims externally.** Companies that look funded frequently turn out to be bootstrapped. A lead qualified as "recently funded and scaling" that isn't produces outreach the prospect knows is wrong — worse than no outreach, because it signals nobody looked.

## Step 8 — Negative signals

Distinct from hard disqualifiers. These reduce the score and may push a lead to RESEARCH_REQUIRED; they do not end the assessment by themselves.

| Negative signal | Effect |
|---|---|
| Already operates a captive offshore development centre | Strong negative — capacity need likely already met |
| Recent material layoffs with contracting roadmap | Strong negative unless a compensating signal exists |
| Under 10 employees, unfunded | Usually below commercial viability |
| No engineering function at all | Strong negative — nothing to extend |
| Secondary geography with no warm introduction | Moderate negative |
| Excluded industry with no segment override | Usually a rejection — check `icp.md` |
| Pure creative, brand, or media agency with no development offering | Strong negative for the Agency segment (C2 routing) |
| Product is entirely white-labelled or third-party | Strong negative |
| Prior failed engagement with Zediant | Escalate rather than score |

### Concentration check — Zediant-specific and easy to miss

`icp.md` treats reducing single-client concentration as a standing priority ranked alongside growth. Two consequences at qualification time:

- **A new logo is worth more than its revenue suggests.** Where two leads are otherwise equal, the one that diversifies the client base is the better lead.
- **An expansion of the already-dominant account is not a new lead.** It may be good business, but it doesn't reduce concentration. Flag it as expansion and route it to account management rather than qualifying it as new pipeline.

Never name the dominant client in any output that could reach outside the company.

## Step 9 — Verdict

Combine into a single verdict with reasoning that a BDM can act on.

| Verdict | Criteria | Next step |
|---|---|---|
| **QUALIFIED** | Score 50+, no hard disqualifier, identifiable buyer, plausible need | → ICP qualification complete (Initial Buying Signal: handled separately by `ptb-scoring`; Post-Engagement PTB: N/A / Not Yet Scored unless engagement evidence already exists) |
| **RESEARCH_REQUIRED** | Score 30–49, or a material evidence gap/ambiguity that must be resolved before treating the lead as fully qualified | → Research or manual review, with the specific missing evidence or question named |
| **REJECTED** | Score under 30, or any hard disqualifier | → Stop. Log the reason |

**RESEARCH_REQUIRED is a real workflow state, not a hedge.** Use it when there is a specific material question or evidence gap that must be resolved — is the headcount drop a bench cut or a decline, is the on-site requirement genuinely fixed, is this the same company we spoke to last year. Name the question. A RESEARCH_REQUIRED status that just says "unclear" wastes the BDM's time as much as a wrong QUALIFIED. Name the evidence needed, the source to check, or the decision question.

Rejection reasons are worth recording precisely. `icp.md` notes that rejection data refines the ICP over time, which only works if the reasons are specific enough to aggregate.

---

# OUTPUT FORMAT

```
## Qualification Status
QUALIFIED | RESEARCH_REQUIRED | REJECTED — ICP Score: NN/100 (Hot / Warm / Cold)

## Qualification Summary
[2–3 sentences: what this company is, and the single most important
reason for the verdict]

## Industry Fit
Excellent | Good | Acceptable | Poor | Reject
[Segment classification and vertical. Note if the vertical is listed
in icp.md but has no supporting case study]

## Company Size Assessment
[Employees, revenue if known, funding stage, headcount trend with direction]

## Geographic Fit
[Company market and contact location separately. Timezone overlap]

## Decision Makers Identified
[Named contacts with titles, and whether they can commit budget.
If none: which titles to target instead]

## Buying Signals
[Signal, strength, source. If none found, state whether that is a
research gap or a genuine absence]

## Negative Signals
[Including the concentration check where relevant]

## Business Challenges
[Observable evidence of a problem Zediant solves — not speculation
about what they could theoretically need]

## Recommended Next Step
→ ICP Qualification Complete | → Research Required (specific evidence/question) | → Stop (reason)

## Reason for Qualification Decision
[The reasoning, including anything that nearly changed the verdict.
Downstream, this folds into crm-update's Description field via
ptb-scoring and campaign-selection's own reasoning — make it specific
enough to be useful to whoever reads it next]

## Data Gaps
[What is missing and whether it would change the verdict. Only list
gaps that matter]
```

When qualifying several leads at once, lead with a compact table — company, verdict, score, one-line reason — then expand only on the RESEARCH_REQUIRED cases and any REJECTED case where the reason isn't obvious. A reviewer scanning twenty leads needs the shape of the batch before the detail.

---

# EXCEPTION HANDLING

| Situation | Action |
|---|---|
| **Insufficient information** | Assess on what exists, flag specific gaps, note whether they'd change the verdict. Don't refuse to assess — a provisional verdict with named gaps is more useful than none |
| **Missing data that Apollo could fill** | Flag for enrichment, but note that enrichment costs credits and shouldn't be spent on a lead already heading for REJECTED |
| **Conflicting information** | Use the most reliable source, state which and why. Company website and filings beat aggregators; aggregators beat inference. **Record the conflict** — don't silently pick |
| **Company cannot be verified** | Set **RESEARCH_REQUIRED** and escalate for manual review. Never assess a company you can't confirm exists |
| **Ambiguous company name** | Escalate. A confident assessment of the wrong company is worse than no assessment |
| **Industry not covered by `icp.md`** | Escalate. Do not extend the ICP by inference |
| **Looks like an existing client or the dominant account** | Stop and escalate. Do not qualify as new pipeline |
| **Prior engagement history exists** | Escalate — history changes the approach in ways a score can't capture |

---

# ESCALATION

Escalate to a human rather than deciding:

- An industry or segment appears that `icp.md` doesn't cover
- ICP rules are ambiguous for this case
- Information conflicts and no source is clearly more reliable
- The company may be an existing client, the dominant account, or a competitor
- The lead requires a capacity or capability judgement beyond documented limits
- A prospect requests the SOC 2 attestation report, an SLA with penalties, or 24/7 coverage — these are flagged in `company.md` as escalation triggers regardless of qualification outcome
- A public sector or tender opportunity appears
- Business judgement is genuinely required and a score would be false precision

Escalating is not a failure. A wrong QUALIFIED sends the BDM into a conversation they can't win; a wrong REJECTED loses a real opportunity silently, which is worse because nobody finds out.

---

# VALIDATION

Before returning a verdict:

- Company identity confirmed by domain, or the ambiguity flagged
- Industry classified by what the company *is*, not by its customers
- Hard disqualifiers checked **before** scoring
- Score uses the ICP model from `icp.md`, not the `ptb-scoring` skill's model
- Both company market and contact location assessed
- Decision maker either named, or target titles suggested
- Signals distinguish "not found" from "not present"
- Funding claims verified externally, not assumed from firmographics
- Concentration impact considered
- Verdict, score, and tier all stated
- Reasoning specific enough to be useful downstream
- RESEARCH_REQUIRED cases name the exact evidence gap, source to check, or human decision question

---

# RELATED SKILLS

| Skill | Relationship |
|---|---|
| `apollo-search-builder` | Sources and enriches. Qualifies its own output inline; this skill handles leads from everywhere else |
| `ptb-scoring` skill (`ptb_scoring.md`) | Separate PTB authority. Initial PTB may remain N/A / Not Yet Scored; `ptb-scoring` owns PTB evaluation and post-engagement re-scoring using engagement evidence (replies, meetings, buying signals) when applicable |
| `campaign-selection` | Selects the single primary C1-C5 campaign for a QUALIFIED lead; Initial Buying Signal is handled separately by `ptb-scoring`, and Post-Engagement PTB remains N/A / Not Yet Scored until engagement evidence exists |
| `crm-update` | Owns the real Zoho write and enforces (not grants) the `Lead_Status = Approved for Outreach` approval gate. **This skill's verdict is an input to that gate, not a substitute for it** — no lead enters a campaign on an AI verdict alone |

---

# SUCCESS CRITERIA

The skill works when the BDM trusts the verdicts enough to act on them without re-checking, and when REJECTED leads stay rejected on review.

| Measure | Target |
|---|---|
| Verdicts overturned at BDM review | < 20% |
| REJECTED leads later found to be good fits | Near zero — false negatives are the expensive error |
| RESEARCH_REQUIRED cases naming a specific evidence gap or question | 100% |
| Hard disqualifiers caught before scoring | 100% |
| Enrichment credits spent on leads that end REJECTED | Zero |

The most dangerous failure is a plausible-sounding QUALIFIED verdict on a company with a hard disqualifier — it passes review because the reasoning reads well, and the problem only surfaces in the sales conversation.

Version 1.3 · Uses the ICP scoring model defined in `icp.md`. When that model changes, this skill inherits the change automatically — which is the reason it isn't duplicated here. Updated August 8, 2026: replaced references to the retired `Qualifying_Status` field and the deleted `Scoring_Reason` field with the live `Lead_Status` gate and `crm-update`'s `Description` field, per `crm-update` v4.0. Replaced the last stale "List A" reference (Step 8 negative signals) with "Agency segment (C2 routing)" to match `apollo-search-builder` v1.4's retirement of the List A-E taxonomy.

**Changed August 11, 2026 (v1.3):** Step 6's Business Challenges finding now carries an explicit phrasing rule — one self-contained, noun/gerund-led sentence — because the exact wording travels unedited into the live Apollo `{{Business Challenge}}` merge tag, which is embedded in two grammatically incompatible slots across the five campaign templates (standalone sentence in four campaigns, a subordinate clause after "Given" in C1). Writing it as a narrated multi-sentence report finding, as before, broke the C1 slot. See `email-personalization` v2.2 and `apollo-distribution` v1.6 for the matching fixes on the content-generation and merge-push sides.

