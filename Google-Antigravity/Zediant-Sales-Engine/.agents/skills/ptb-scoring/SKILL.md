---
name: ptb-scoring
description: "Zediant's PTB scoring authority — one score only: PTB Score (Initial Buying Signal), 0-100, calculated before outreach for Qualified leads from pre-outreach evidence. Uses active need, current buying signal, urgency/timing, growth/change, relevance of the business challenge to Zediant, and evidence strength/recency. Writes the numeric PTB score to Zoho's Twitter field at the initial CRM write. There is no separate post-engagement PTB score. PTB is not combined with ICP Score and is not a qualification gate. Every point must trace to stated evidence."
---

# PTB Scoring — Initial Buying Signal

Zediant uses **one PTB score** for lead prioritization. **PTB = Initial Buying Signal.** It is calculated once during initial lead processing, before outreach, for every Qualified lead that reaches this skill.

PTB answers: **“How strong is the observable evidence that this qualified prospect has a current or emerging reason to engage Zediant now?”**

PTB is a 0–100 score based only on pre-outreach evidence. There is no separate pre-engagement PTB and post-engagement PTB model. There is no Path A / Path B distinction. Do not recalculate, overwrite, or create a second PTB score after outreach.

## Scope

**Owns:** calculating the single PTB Score (Initial Buying Signal) from evidence already gathered upstream; producing an explainable 0–100 breakdown; handing the numeric score to `campaign-selection` and `crm-update`.

**Does not own:** qualification, ICP scoring, campaign selection, personalization, CRM writes, or outreach approval.

## PTB versus ICP

- **ICP Score:** How good a fit is this prospect for Zediant?
- **PTB Score:** How strong is the current buying signal for this qualified prospect?

Never combine, average, or substitute the two scores. PTB is not a qualification gate. A high PTB does not make a poor ICP fit qualified, and a high ICP does not create a high PTB.

## PTB rules

- Calculate PTB after qualification and signal enrichment, before campaign selection and CRM write.
- Use only evidence available before outreach.
- Never use email opens, replies, LinkedIn responses, meetings, or other engagement evidence.
- Never use ICP Score, company size, geography, industry fit, or persona seniority as a PTB scoring input.
- Every non-zero point must trace to stated evidence.
- Lack of evidence is scored conservatively; never invent evidence.
- PTB is informational and prioritization-oriented. It never independently approves outreach and never blocks a qualified lead from CRM write or campaign selection.

## The six evidence categories

Score each category independently on a 0-100 evidence scale using the bands below, then combine using the weighting formula in **Category Weighting** further down. Every non-zero point in every category must trace to stated, sourced evidence — the same evidence-first discipline required throughout the revenue engine.

### A. Active Business / Technical Need

Is there a specific, verifiable technical or business need this company appears to have right now — not a generic "any software company could use engineering capacity" observation.

| Evidence | Score band | Reasoning |
|---|---|---|
| A specific, verified need directly matching a Zediant capability — e.g. multiple simultaneous open senior engineering roles, a documented integration/migration/modernization initiative, a stated capacity constraint found on a careers page or public statement | 70-100 | Concrete, checkable, and directly relevant |
| A plausible but more generic need inferred from company type/stage, without a specific verified instance | 30-69 | Real but soft — worth noting, not a strong opener |
| A genuine search was performed and turned up nothing specific | 0-29 | Absence of found evidence, not evidence of absence — label as "not found," never as "none exists" |
| No search was actually performed for this factor | 0, and flag explicitly in Data Gaps | Never silently omit a category — an unscored category looks identical to a scored-zero one otherwise |

### B. Current Buying Signal

Reuses the same signal evidence `apollo-search-builder`'s Signal priority table already collects (funding, multiple simultaneous open senior roles, a single open role, acquisition/merger, product launch, a technology modernization initiative, an outage or scaling complaint, headcount growth, a Strong-tier technology match) — this skill does the scoring, not a re-collection of the evidence.

| Evidence strength (per `apollo-search-builder`'s Signal priority table) | Score band |
|---|---|
| Highest (recent funding; multiple simultaneous open senior eng roles) | 80-100 |
| High (a single open senior role; acquisition/merger; product launch; technology modernization initiative; outage/scaling complaint) | 55-79 |
| Moderate (headcount growth alone; Strong-tier technology match alone, with nothing else corroborating) | 25-54 |
| No signal found after a genuine check | 0-24 |

### C. Business Urgency / Timing Signal

Explicit, stated, or publicly documented evidence of timing — a deadline, a compliance requirement, an end-of-life notice on core technology, a publicly stated timeline. **Never inferred or assumed** — this is the single easiest category to fabricate, and the rule is absolute: no explicit timing evidence found means this category scores low, full stop.

| Evidence | Score band |
|---|---|
| An explicit, dated, verifiable deadline, compliance requirement, or end-of-life notice | 70-100 |
| A stated timeline or initiative with a general but real time horizon (e.g. a publicly announced modernization program without a hard date) | 30-69 |
| No explicit timing evidence found | 0-29 |

Do not infer urgency from company growth, hiring, funding, or generic business problems alone — those belong to Factors A/B/D. Manufacturing urgency from adjacent evidence here is exactly the failure mode this category exists to prevent.

### D. Growth / Expansion / Change Signal

Uses the same headcount growth tiers and change signals already defined in `apollo-search-builder`.

| 24-month signal | Read | Score band |
|---|---|---|
| > +15% headcount growth, or verified recent funding/expansion | Genuine growth, capacity pressure likely | 70-100 |
| +5% to +15% | Steady, neutral positive | 40-69 |
| -5% to +5% | Flat — verify other signals before scoring high | 15-39 |
| < -15% (contracting) | Genuinely ambiguous — could be a bench cut (strong prospect) or a real decline (weak prospect); both look identical in the data | Score 20-40 and **state the ambiguity explicitly** in the evidence note — do not resolve it silently in either direction, matching the discipline already used elsewhere in this pipeline for contracting companies |
| No growth or change data available | 0-14, flagged as a data gap | |

### E. Relevance of the identified Business Challenge to Zediant

Reads `lead-qualification`'s Step 6 Business Challenges finding — does not re-derive it — and scores how directly that specific, already-identified challenge maps to a Zediant capability. `context/playbooks/C{1-5}.md` (that lead's campaign) or `context/playbooks/_core-reference.md`'s "Not offered" list is usually enough to judge this; open `services.md` directly only when the playbook genuinely doesn't resolve it. This is deliberately **not** the same thing as ICP Fit (which measures segment/size/geography match): a company can be an excellent ICP fit with a Business Challenge that's only loosely something Zediant addresses, or a weaker ICP fit with a challenge that's a direct, obvious match.

| Evidence | Score band |
|---|---|
| The identified Business Challenge maps directly and specifically to a documented Zediant capability | 70-100 |
| The Business Challenge is plausibly addressable by Zediant but the match requires some interpretation | 30-69 |
| The Business Challenge is vague, generic, or only tangentially something Zediant does | 0-29 |

If `lead-qualification` hedged the Business Challenges finding ("a hiring pattern that suggests possible capacity pressure"), score against the hedge as stated — do not firm up an uncertain finding into a confident one just to justify a higher score here.

### F. Evidence Strength / Recency

A cross-cutting category scoring how strong and how current the evidence actually is across Factors A-D and E combined — not a restatement of any one factor, but an honest check on how much weight the whole score deserves.

| Evidence quality | Score band |
|---|---|
| Multiple factors have verified, dated evidence from primary or company-owned sources (careers page, official announcement, filed documentation) within roughly the last 6 months | 70-100 |
| Evidence exists but is either single-source, from a secondary source (aggregator, third-party news), or somewhat older (roughly 6-12 months) | 35-69 |
| Evidence is thin, stale (12+ months), or leans heavily on inference rather than anything directly observed | 0-34 |

Factor F feeds both the numeric score (via its weight, see below) and the **Confidence Level** field in the output — a low Factor F score should always be reflected in a Low or Medium Confidence Level, never contradicted by it.

## Category weighting — APPROVED, AUTHORITATIVE

**Zediant leadership has confirmed this weighting. It is authoritative for every PTB scoring score, effective immediately — this is no longer a proposal or a working default.**

The combination formula is fixed and not in question:

```
PTB Score =
  (A × wA) + (B × wB) + (C × wC) + (D × wD) + (E × wE) + (F × wF)

where wA + wB + wC + wD + wE + wF = 100%
```

**Authoritative weighting:**

| Factor | Weight | Rationale |
|---|---:|---|
| A. Active Business / Technical Need | 25% | The most direct "is there a real reason to reach out" evidence, mirroring why Business Problem/Technical Need carries the heaviest weight (35-41%) in `campaign-selection`'s own Campaign Fit Score |
| B. Current Buying Signal | 20% | Second-heaviest, mirroring Business Signal's weighting in the same Campaign Fit Score model |
| C. Business Urgency / Timing Signal | 15% | Real but the hardest category to find genuine evidence for pre-engagement; weighted below A/B accordingly |
| D. Growth / Expansion / Change Signal | 15% | Corroborating evidence, similar weight to Urgency |
| E. Relevance of Business Challenge to Zediant | 15% | Distinct from ICP Fit; weighted to matter but not dominate |
| F. Evidence Strength / Recency | 10% | A confidence modifier on the other five, weighted lightest since it is about evidence quality rather than a sixth independent signal |

**Use exactly these weights.** Do not invent alternative weights, do not normalize them differently, do not add a seventh factor, and do not remove one of the six. No PTB scoring output needs to disclose a pending-approval status any longer — this table is the final, ratified formula, not a working default.

## Score bands (PTB scoring) — descriptive labels only, never a gate

| PTB Score | Label | Meaning |
|---|---|---|
| 70-100 | **Strong pre-engagement signal** | Multiple categories show real, dated evidence of active need |
| 40-69 | **Moderate pre-engagement signal** | Some real evidence, but thinner or less corroborated |
| 0-39 | **Weak pre-engagement signal** | Little or no verifiable pre-engagement evidence found |

**These labels are informational only.** A low PTB score never blocks Campaign Selection, never blocks the CRM write, and never substitutes for BDM judgment — see Campaign Selection's own handling of this score for confirmation that no hard gate is reintroduced here.

## Output Format (PTB scoring)

```
## PTB Score
NN/100 — [Strong | Moderate | Weak] pre-engagement signal

## Score Breakdown
| Factor | Points Awarded | Weight | Weighted Contribution | Evidence | Source | Date |
|---|---|---|---|---|---|---|
| A. Active Business / Technical Need | | 25%* | | | | |
| B. Current Buying Signal | | 20%* | | | | |
| C. Business Urgency / Timing Signal | | 15%* | | | | |
| D. Growth / Expansion / Change Signal | | 15%* | | | | |
| E. Relevance of Business Challenge to Zediant | | 15%* | | | | |
| F. Evidence Strength / Recency | | 10%* | | | | |
| **PTB Score** | | **100%** | **NN** | | | |

*Authoritative weighting — see Category Weighting above.

## Evidence Summary
[The specific, sourced evidence that drove the strongest categories]

## Ambiguous / Contradictory Evidence
[e.g. a sharply contracting headcount signal — state the ambiguity, don't resolve it silently]

## Confidence Level
High | Medium | Low
[Driven primarily by Factor F — High: most factors have recent, primary-source evidence.
Medium: evidence exists but is thinner/older/secondary-source. Low: little verifiable
evidence found across most factors]

## Data Gaps
[Which factors lack evidence, whether that's a research gap or a genuine absence]
```

## Workflow (PTB scoring)

```
Lead Qualification → ICP Score → PTB Score (PTB scoring) → Campaign Selection → Personalization → CRM → BDM Approval
```

1. Confirm the lead has a Qualified verdict from `lead-qualification`. If it doesn't, stop — this skill does not qualify companies.
2. Pull forward the evidence already gathered upstream (Signal Enrichment Pass, headcount growth, Business Challenges finding, any Apollo Intent data) rather than re-researching from scratch — this skill's new work is scoring that evidence, not re-collecting it.
3. Score each of the six factors using the tables above, citing specific, sourced, dated evidence for every non-zero point. A factor with no evidence found scores at the bottom of its band and is flagged, never silently skipped.
4. Combine into the final PTB Score using the authoritative weighting above.
5. Assess Confidence Level, driven primarily by Factor F.
6. Return the full breakdown — never a bare number.
7. Hand the numeric score to `campaign-selection` as the Buying Signal factor input for its Campaign Fit Score, and to `crm-update` for the `Twitter` write (see CRM Write States below).

## Exception Handling (PTB scoring)

| Situation | Action |
|---|---|
| No search was performed for a given factor | Score 0 for that factor and flag it explicitly in Data Gaps — do not let it look identical to a genuinely-searched, evidence-free factor |
| Evidence is ambiguous (e.g. sharply contracting headcount) | Score conservatively within the band, state the ambiguity plainly, do not resolve it in either direction |
| Evidence for Factor C (urgency) does not exist | Score low — never infer urgency from Factors A/B/D |
| A lead has essentially no verifiable pre-engagement evidence at all across every factor | Score accordingly, low across the board — this is a legitimate, expected PTB Score, not a reason to fall back to `N/A / Not Yet Scored`. Scheduler 1 always produces a numeric value; see CRM Write States |

---


## CRM WRITE CONTRACT

`crm-update` writes the numeric PTB Score to Zoho's `Twitter` field as plain text during the initial Scheduler 1 write. Example: `"76"`. The same PTB number is the Initial Buying Signal used by the BDM to prioritize the lead. There is no later PTB replacement model in this operating design.

If a numeric PTB cannot be produced because the scoring skill itself was not run, treat that as a workflow error and report `DATA GAP`; do not invent a value and do not create a second scoring model.

## Scheduler 1 handoff

`Lead Qualification → ICP Score → Signal Enrichment → PTB Score (Initial Buying Signal) → Campaign Selection → Personalization → QA → CRM`
