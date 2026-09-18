# Overview

This document is the commercial reference for every Zediant AI agent. It covers how Zediant prices, which engagement model to recommend, how to qualify budget, and — critically — when an agent must stop talking and hand the conversation to a human.

Zediant's commercial position as of August 2026 is specific and constrains everything below:

| Fact | Implication |
|---|---|
| Operating at break-even | Margin discipline matters more than volume |
| ~90% of revenue from one client | New logos are worth more than their revenue suggests |
| Capacity: 5–7 additional developers in three months | Deals beyond this cannot be priced, only escalated |
| Typical deal size USD 10,000–20,000 | Below ~USD 10,000 is rarely viable |
| Larger pods USD 80,000–150,000+ annualised | The base-case path to the revenue target |
| Target gross margin 40–50% | Requires a minimum blended rate of USD 25–30/hour |
| Billable utilisation 50–60%, target 75–85% | Idle capacity is the real cost, not the rate |

## ⚠️ CRITICAL — Two rate sources disagree materially

Zediant holds **two internal pricing documents that do not reconcile.** An agent quoting from the wrong one could be 40% or more out.

| Source | Australian-market rate |
|---|---|
| **Rate Card** (Rate_Card.xlsx) | Tech Lead peaks at **AUD 69/hour**; Senior at **AUD 54/hour** |
| **Sales Bible Appendix I** | Australian-market engagements at **AUD 85–95/hour blended** |

AUD 85–95 blended is **above the highest individual rate in the rate card**. A blended rate cannot exceed the rate of the most expensive person in the blend. These two figures cannot both be correct.

**Possible readings** — none confirmed:

1. The Sales Bible figure is a target or aspirational market rate, not the current card
2. The Rate Card is a cost-plus internal calculation and the Sales Bible reflects the client-facing price
3. One document is stale

**Mandatory rule for every agent.** Do **not** quote an hourly rate to a prospect. Do not select between these sources. Route all rate questions to a human. Guidance for handling the question conversationally is in [Pricing Questions](#pricing-questions).

Until this is resolved, every rate in this document is recorded as **internal reference only**.

Cross-reference: `company.md` · `services.md` · `icp.md` · `campaigns.md` · `case_studies.md` · `competitors.md`

---

# PRICING PHILOSOPHY

## Documented principles

These come directly from Zediant's own commercial materials.

### 1. Honest estimation over padding

Zediant's stated preference is **defensible estimates rather than conservative padding or scope inflation**. An estimate should be what the work costs, not what protects the vendor.

### 2. Fixed budget means lean MVP, not fewer features

When a client's budget is fixed, documented policy is to **keep all requested modules in scope and deliver each as a lean, functional MVP**, rather than cutting features from the scope. This preserves the client's sense of a complete solution while staying within budget.

This is a genuine differentiator in proposal conversations. Most vendors respond to a fixed budget by removing scope.

### 3. Capacity, not hours

Internal strategy directs Zediant to move from **selling hours to selling capacity** — productised pod tiers with a published rate card designed to shorten the proposal cycle and enable decisions during a discovery call rather than weeks later.

### 4. No free speculative work

Documented and unambiguous: **stop free POCs and uncompensated tender documentation.** Free POCs convert to fixed-cost discounted rates. Tender support moves to a retainer model or requires a formal Teaming Agreement.

This is a policy, not a preference. An agent must not offer free work under any framing.

### 5. Margin protection over rate cutting

Internal guidance: **protect margins ruthlessly, increase rates gradually, and completely avoid the culture of free, speculative work.** The stated growth path is rate discipline, not volume at lower margin.

### 6. Long-term partnership over transaction

The documented commercial pattern is that most long-term relationships began as a single small project and expanded once delivery quality was proven. Pricing should support that path — a small first engagement priced to be easy to say yes to, with expansion economics behind it.

### 7. Founder holds final authority

**The Founder retains final say on any deal.** A BDM — or an AI agent — must never quote outside documented ranges without checking. This is explicit.

## Value-based pricing — the honest position

Zediant's documented pricing is **cost-plus with a 35% margin**, not value-based. The rate card is built from salary, benefits, fixed cost per hour, and an idle-margin allowance.

**Do not describe Zediant's pricing as value-based.** It is competitively-positioned cost-plus. Where value framing is appropriate is in the *comparison* — total cost of ownership against a local hire, or rate multiplied by rework against a cheaper vendor — not in the pricing model itself.

## Business outcomes as commercial justification

Where a prospect challenges price, the documented comparisons are:

| Against | Comparison |
|---|---|
| Cheaper offshore vendor | Rate × rework, missed deadlines, and security gaps — not rate alone |
| Local permanent hire | Fully-loaded cost: salary + on-costs + recruitment fee + months of work not happening |
| Freelancer | Continuity, backfill, code review, and QA that a rate does not include |
| Doing nothing | The cost of the roadmap item that keeps slipping |

Use only outcomes documented in `case_studies.md`. Never invent an ROI figure.

## When pricing should NOT be discussed

An agent must **not** open, volunteer, or negotiate on price in these situations:

| Situation | Why | Do instead |
|---|---|---|
| First outbound touch | Price before need destroys the discovery conversation | Lead with the problem |
| Before scope is understood | Any number given now becomes an anchor that cannot be revised upward | "It depends on shape — can I ask a few questions?" |
| Prospect asks "what's your hourly rate?" cold | **The two rate sources conflict** | Route to a human; see [Pricing Questions](#pricing-questions) |
| Referral or partner introduction | A warm intro expects a conversation, not a quote | Discovery first |
| Enterprise procurement or RFP | Formal process; requires considered response | Escalate |
| Prospect is comparing on lowest rate | Zediant has chosen not to compete there | Qualify out or reframe |
| Any request for free work | Prohibited by policy | Offer fixed-cost discounted scope |
| Prospect asks for a written rate card | Two sources conflict | Escalate to the Founder |

---

# ENGAGEMENT MODELS

## Model comparison

| Model | Deal size | Duration | Risk holder | Priority |
|---|---|---|---|---|
| Dedicated Teams (Pods) | USD 80k–150k+ annualised | 6–18+ months | Shared | **1 — Primary** |
| Time & Material | Variable | 3–18 months | Client | 2 |
| Staff Augmentation | Small, recurring | 1–12 months | Client | 3 |
| Support & Maintenance | Small, recurring | Rolling | Shared | 4 |
| Fixed Cost Projects | USD 10k–20k typical | 2–6 months | **Zediant** | 5 |
| Managed Services | Small–medium, recurring | Rolling | Zediant | 6 |
| Consulting / Advisory | Small | 1–4 weeks | Zediant | 7 — entry motion |
| Discovery Workshop | Small | 1–2 weeks | Zediant | 8 — entry motion |
| Proof of Concept | Small, **never free** | 4–8 weeks | Negotiated | 9 |
| AI Advisory | Small | 2–4 weeks | Zediant | 10 |

---

## 1. Dedicated Teams (Engineering Pods)

### Overview

A self-contained squad — tech lead, developers, QA, project manager — embedded in the client's roadmap and process. Zediant's primary and preferred commercial model, representing approximately 90% of current billing.

### Business Situation

The client has sustained engineering demand exceeding internal capacity, with a roadmap rather than a single deliverable.

### Ideal Customer

Funded SaaS (seed–Series B), digital agencies with recurring pipeline, CTO-led product companies. 10–200 employees. Australia or UAE.

### Advantages

| For the client | For Zediant |
|---|---|
| Capacity in 5–10 days versus months of hiring | Predictable recurring revenue |
| Scale down without redundancy exposure | Higher utilisation and better margin |
| Predictable monthly cost | Deepest client relationship and expansion surface |
| Tech lead and PM included, not billed extra | Strongest retention of the models |

### Limitations

- Requires client-side product ownership; an absent product owner stalls delivery
- Not suited to a single defined deliverable
- 2–4 week ramp before full productivity
- Constrained by the 5–7 developer, three-month capacity ceiling

### Typical Project Size

Medium to Large. **INTERNAL PLANNING ASSUMPTION — NOT APPROVED FOR EXTERNAL USE (pod tier composition):** documented pod tiers conflict between sources — see the warning in `services.md`. Website tiers are Foundation / Growth / Enterprise; internal strategy defines Maintenance (40 hrs/month), Growth (1 full-stack + 0.5 QA), and Scale (2 devs + 1 lead + 1 QA). Confirm which is commercially active before quoting composition.

### Typical Duration

6–18 months, rolling. Documented longest: 18 months (12 people) and 3+ years (continuing).

### Decision Makers

CTO · VP Engineering · Founder/CEO · COO (agency) · Managing Director.

### Business Outcomes

Company-stated 30–40% acceleration in feature delivery. Documented: 70%→93% test coverage; 3+ year retention; 12-person team sustained 18 months.

### Recommended Services

`services.md` → Dedicated Engineering Pods · Platform Engineering · QA & Test Automation · Integration & Middleware

### Typical Risks

| Risk | Mitigation |
|---|---|
| Client expects fixed deliverables from a capacity model | Define outcomes and cadence in the SOW |
| Scope creep without commercial recognition | Change request process |
| Ramp cost absorbed silently | Price the ramp period explicitly |
| Utilisation below the 75% target | Monitor; the internal cost of idle capacity exceeds rate concessions |
| Over-reliance if the pod becomes the client's only engineering | Flag as a delivery risk, not a commercial win |

### Discovery Questions

1. Is this ongoing capacity, or a defined deliverable?
2. What does your roadmap look like over the next two to three quarters?
3. Who would the pod report to day to day?
4. Do you have a product owner with genuine time available?
5. What is your sprint cadence and review process?
6. How would you want to scale up or down, and on what notice?
7. What budget cycle does this fall into — opex, headcount, or project?
8. Is the budget approved, or does it need building a case for?

### Qualification Signals

Multi-quarter roadmap · Identified product owner · Existing CI/CD and review discipline · Recent funding or committed budget · Willingness to start with a defined trial scope · CTO or Founder engaged directly.

### Disqualification Signals

Single defined deliverable · No internal technical counterpart · Expects fixed price for a capacity model · Needs more than 5–7 developers inside three months · Budget below USD 10,000 total.

### When AI should recommend this model

Recommend when the need is **ongoing**, the client has internal technical management, and the roadmap extends beyond one deliverable. This is the default recommendation for C1 (AI-Enabled Product Engineering) and C2 (Engineering Pods & Staff Augmentation) prospects.

---

## 2. Time & Material

### Overview

Hourly billing against a flexible backlog. Documented as the model used on Zediant's largest and longest engagements.

### Business Situation

Requirements are evolving, scope cannot be fixed responsibly, or discovery continues throughout delivery.

### Ideal Customer

Clients with genuine scope uncertainty who understand that fixing price on unknown scope prices in risk they will pay for.

### Advantages

| For the client | For Zediant |
|---|---|
| Pays for work done, not risk premium | No fixed-price risk exposure |
| Scope can change without renegotiation | Scope changes are billable, not absorbed |
| Faster start — no exhaustive specification | Suits discovery-led work |

### Limitations

- Client bears budget uncertainty
- Requires trust and transparent reporting
- Harder to approve where procurement demands a fixed number
- Can drift without milestone discipline

### Typical Project Size

Variable — small through large. Documented T&M engagements: 12 people/18 months, 8 people/10 months, 6 people/6 months.

### Typical Duration

3–18 months.

### Decision Makers

CTO · VP Engineering · CIO · Founder.

### Business Outcomes

Best documented outcomes across the portfolio were delivered on T&M, including the largest and longest engagements.

### Recommended Services

`services.md` → Integration & Middleware · Legacy Modernisation · Enterprise Custom Development · Dedicated Pods

### Typical Risks

| Risk | Mitigation |
|---|---|
| Budget drift | **Documented policy: strict Agile milestones or T&M retainers with built-in delay clauses** |
| Client loses confidence without visibility | Transparent sprint reporting |
| No natural stopping point | Define review gates at fixed intervals |
| Delivery delays (a documented past issue on a 10-month engagement) | Delay clauses — introduced specifically in response |

### Discovery Questions

9. How well defined is the scope today, honestly?
10. What is likely to change once we start?
11. Would you rather pay a risk premium for certainty, or pay for what's built?
12. What budget visibility do you need, and how often?
13. Does your approval process require a fixed number?
14. What milestone structure would give you confidence?

### Qualification Signals

Acknowledged scope uncertainty · Prior T&M experience · Internal technical counterpart · Budget flexibility · Trust established through a smaller prior engagement.

### Disqualification Signals

Procurement mandates fixed price · No internal capacity to review progress · History of disputes with T&M vendors · Requires absolute cost certainty.

### When AI should recommend this model

Recommend when scope genuinely cannot be fixed — integration, modernisation, and discovery-led product work. **Always pair with milestone or delay clauses**, per documented policy.

---

## 3. Staff Augmentation

### Overview

Individual engineers placed into the client's team under the client's management. Documented commitment tiers at 40, 80, and 120 hours, plus monthly.

### Business Situation

A specific skill gap or temporary capacity need not justifying a permanent hire, or a hiring freeze with continuing workload.

### Ideal Customer

Clients with strong internal engineering management who need capability, not partnership.

### Advantages

| For the client | For Zediant |
|---|---|
| Lower commitment than a pod | Entry motion into pod expansion |
| Faster than local hiring | Low delivery overhead |
| Rate improves with commitment tier | Predictable if the tier is monthly |

### Limitations

- **Commercially the weakest model.** Competes directly with commodity staffing on price
- Client-side management quality determines outcome and Zediant cannot control it
- Single-person dependency
- Weakest relationship stickiness
- Little opportunity to demonstrate Zediant's methodology

### Typical Project Size

Small. Commitment tiers documented at 40, 80, and 120 hours and monthly, with rate improving at higher commitment.

### Typical Duration

1–12 months. Rate card validity periods of 30, 60, and 90 days attach to the commitment tiers.

### Decision Makers

Engineering Manager · CTO · Delivery Manager · COO (agency).

### Business Outcomes

Documented: an engagement that began as team augmentation ran 3+ years and raised test coverage from 70% to 93%.

### Recommended Services

`services.md` → Staff Augmentation · QA & Test Automation

### Typical Risks

| Risk | Mitigation |
|---|---|
| Commoditisation and margin erosion | Position the pod wherever the workload justifies it |
| Client treats the engineer as interchangeable | Emphasise the organisation behind the placement |
| Individual departure | Structured replacement process |
| Blended rate falls below the USD 25–30/hour margin floor | Check the mix before quoting |

### Discovery Questions

15. What specific role or skill are you filling?
16. Is this covering a gap, a peak, or a permanent need you cannot hire for?
17. How long has the role been open, and what has it cost you?
18. Is this budgeted as headcount or contract spend?
19. Who approves contract spend, and how does that differ from headcount approval?
20. What commitment level can you make — 40, 80, 120 hours, or monthly?
21. Is there scope beyond this one role if it goes well?

### Qualification Signals

Clearly defined role · Strong internal engineering management · Documented development process · Realistic senior-rate budget · Expansion potential.

### Disqualification Signals

Competing purely on hourly rate · No internal technical management · Need under one month · Expects the individual to own outcomes without support — that is a pod, priced accordingly.

### When AI should recommend this model

Recommend when the client explicitly wants one or two individuals under their own direction. **Treat as a land-and-expand entry point**, not a destination — the documented pattern is augmentation proving quality, then pod expansion.

---

## 4. Fixed Cost Projects

### Overview

Defined scope, timeline, and price. Zediant holds the delivery risk.

### Business Situation

Scope is genuinely stable and specifiable — a defined feature, module, migration, or platform build.

### Ideal Customer

Clients with a clear specification and a procurement process requiring a fixed number.

### Advantages

| For the client | For Zediant |
|---|---|
| Cost certainty | Faster approval in fixed-budget environments |
| Simpler internal approval | Clean scope boundaries |
| Clear deliverable | Documented successful delivery at this shape |

### Limitations

- **Zediant carries all overrun risk**
- Requires genuinely stable scope — rare
- Change requests become commercial conversations
- Inappropriate for undocumented legacy estates or greenfield platforms

### Typical Project Size

**INTERNAL PLANNING ASSUMPTION — NOT APPROVED FOR EXTERNAL USE.** USD 10,000–20,000 — inferred typical current deal size; not formally approved for external quotation. See [Budget Ranges](#budget-ranges).

### Typical Duration

2–6 months. Documented fixed-price deliveries: 3 people/5 months, 5 people/6 months.

### Decision Makers

CTO · Head of Product · Head of Digital · Procurement.

### Business Outcomes

Documented fixed-price outcomes: 4.9 Google Play / 4.4 App Store ratings; 30% website traffic increase.

### Recommended Services

`services.md` → Mobile Development · E-commerce & CMS · Web Development · defined modules within larger services

### Typical Risks

| Risk | Mitigation |
|---|---|
| Scope ambiguity absorbed as overrun | **Documented policy: state explicitly what is out of scope** |
| Client-side content or data delays | Name client dependencies in the SOW with dates |
| Change requests eroding margin | Formal change request process from day one |
| Underestimation on unfamiliar work | Founder review before commitment |

**Documented out-of-scope items** — state these explicitly in every fixed-price proposal: content creation, data migration, data feeding, ongoing SEO execution.

### Discovery Questions

22. How settled is the specification — could it change after we start?
23. What is explicitly in scope, and what is not?
24. Who owns content, data, and third-party dependencies?
25. What is your change request process and approval path?
26. What happens if requirements change mid-delivery?
27. Is fixed price a procurement requirement or a preference?
28. What is the approved budget figure?

### Qualification Signals

Written specification exists · Client understands change requests carry cost · Clear dependency ownership · Realistic timeline · Budget approved at a specific figure.

### Disqualification Signals

Undocumented legacy estate · Greenfield platform with undefined scope · Expects unlimited revisions within the fixed price · No specification but demands a fixed number · Client cannot name what is out of scope.

### When AI should recommend this model

Recommend **only** when scope is genuinely stable and specifiable. Where a prospect wants fixed price on unclear scope, the correct response is a paid discovery or scoping engagement first — never a guess.

---

## 5. Managed Services

### Overview

Zediant owns ongoing operation and support of defined applications. Publicly described as "Engineering as a Service."

### Business Situation

Internal engineers are consumed by supporting existing applications, or a key person holding system knowledge is leaving.

### Ideal Customer

Organisations with production applications and no dedicated support capacity.

### Advantages

| For the client | For Zediant |
|---|---|
| Internal engineers released for new work | Highly predictable recurring revenue |
| Predictable monthly cost | Strongest retention vehicle |
| Continuity independent of individuals | Natural expansion path into development |

### Limitations

- **Scope ambiguity is the primary commercial risk** — the boundary between support and enhancement must be contractual
- Lower margin than development if scope is not controlled
- Undocumented inherited applications need a discovery period before SLAs can be committed
- **24/7 coverage should not be committed** without confirmed staffing

### Typical Project Size

Small to medium, recurring. Documented tier: 40 hours/month maintenance pod.

### Typical Duration

Rolling, typically annual with monthly billing. Documented client progression from project into multi-year managed services.

### Decision Makers

CTO · IT Manager · Operations Head · CIO.

### Business Outcomes

Documented: a named client progressed from small projects to an ongoing managed services arrangement described as "above expectation."

### Recommended Services

`services.md` → Maintenance, Support & Managed Services · Platform Engineering

### Typical Risks

| Risk | Mitigation |
|---|---|
| Unlimited enhancement expected within a fixed retainer | Define support versus enhancement contractually |
| SLA committed before understanding the application | Fund a discovery period first |
| 24/7 expectation at low retainer cost | Do not commit; escalate |
| Knowledge concentrated in one engineer | Documented handover requirements |

### Discovery Questions

29. What applications need support, and what are they built on?
30. What is your ticket volume, and what is the incident-to-request mix?
31. What coverage hours do you genuinely need?
32. What is the business cost of an hour of downtime?
33. Where does support end and enhancement begin, in your view?
34. What documentation exists?
35. Is there an SLA you are contractually bound to with your own customers?
36. What is currently spent on this internally?

### Qualification Signals

Quantified internal support burden · Documented applications or willingness to fund discovery · Realistic coverage expectations · Departing key person creating urgency.

### Disqualification Signals

Demands 24/7 on-call at low cost · Expects unlimited enhancement in a fixed fee · Requires an SLA with financial penalties · Undocumented application with no discovery funded.

### When AI should recommend this model

Recommend at the natural end of a build engagement, or where a client's internal team is visibly consumed by support. Treat as the **strongest retention and expansion vehicle**, not a downgrade.

---

## 6. Consulting / Advisory

### Overview

Short expert engagements — architecture review, performance assessment, technical due diligence, platform optimisation.

### Business Situation

The client faces a decision they cannot validate internally, or a problem they cannot diagnose.

### Ideal Customer

Any prospect at a decision point. **The highest-value entry motion in the portfolio.**

### Advantages

| For the client | For Zediant |
|---|---|
| Low commitment, high insight | Lowest-friction way into a relationship |
| Independent validation | Findings scope the follow-on delivery |
| Fast — days or weeks | Founder-delivered, high credibility |

### Limitations

- Low direct revenue; value is in conversion
- Client may implement findings elsewhere
- Quality depends entirely on access granted
- Superficial if scope is not tightly bounded

### Typical Project Size

Small. Fixed price is appropriate and common.

### Typical Duration

1–4 weeks.

### Decision Makers

CTO · Founder/CEO · VP Engineering · CIO.

### Business Outcomes

Documented: the largest engagement in Zediant's history opened with a transformational roadmap rather than a build brief.

### Recommended Services

`services.md` → Advisory & Engineering Consulting

### Typical Risks

| Risk | Mitigation |
|---|---|
| Findings implemented by another vendor | Accept as the cost of the entry motion |
| Scope creep in a short engagement | Fixed deliverable and fixed price |
| Access not granted, undermining quality | Make access a stated precondition |
| Prospect seeking free consulting as "scoping" | **Charge for it. Documented policy** |

### Discovery Questions

37. What decision are you trying to make?
38. What happens if you get it wrong?
39. Who has looked at this already?
40. What access can you give us to systems and people?
41. Who consumes the output, and in what form?
42. If we identify work, do you have capacity to execute it internally?

### Qualification Signals

Specific pending decision with a deadline · Willingness to grant access · Executive consuming the output · Budget available for follow-on execution.

### Disqualification Signals

Seeking free consulting framed as a scoping call · Will not grant access · No budget to act on findings · Wants a vendor-neutral audit with no follow-on potential.

### When AI should recommend this model

Recommend as the **opening offer** where a prospect is interested but not ready to commit to delivery. An architecture review converts better than a capacity pitch. **Always paid.**

---

## 7. Discovery Workshop

### Overview

A structured scoping engagement producing a specification, estimate, and delivery plan.

**Assumption.** Discovery Workshop is not named as a distinct commercial product in Zediant's documentation. It is described here as a defensible application of the documented policy that speculative scoping work must be paid. Confirm before offering it as a named product.

### Business Situation

The prospect wants a fixed price but has no specification — the most common commercial impasse.

### Ideal Customer

Prospects with genuine intent, budget, and an undefined problem.

### Advantages

| For the client | For Zediant |
|---|---|
| A costed, buildable plan | Converts free scoping into paid work |
| Can take the plan to market if they wish | Removes fixed-price estimation risk |
| Small commitment to test the relationship | Qualifies seriousness |

### Limitations

- Some prospects refuse to pay for scoping
- Short engagement, limited revenue
- Requires senior time

### Typical Project Size

Small. Fixed price appropriate.

### Typical Duration

1–2 weeks.

### Decision Makers

CTO · Founder · Head of Product.

### Business Outcomes

Not separately documented. The transformational roadmap preceding Zediant's largest engagement is the closest analogue.

### Recommended Services

`services.md` → Advisory & Engineering Consulting

### Typical Risks

Prospect uses the output to tender elsewhere · Scope of the workshop itself expands · Findings reveal the project is not viable.

### Discovery Questions

43. What would you need to see before committing to a build?
44. Has anyone documented the requirement yet?
45. Would a costed plan be valuable even if you built it elsewhere?

### Qualification Signals

Wants fixed price but has no spec · Has budget but no plan · Willing to pay for the plan.

### Disqualification Signals

Expects scoping free as part of the sales process · No budget for delivery afterwards.

### When AI should recommend this model

Recommend whenever a prospect requests a fixed price on undefined scope. This is the correct, policy-compliant answer to that request.

---

## 8. Proof of Concept (POC)

### Overview

A small technical build validating feasibility before larger commitment.

### ⚠️ Documented policy — POCs are never free

Internal strategy is explicit: **immediately transition free POCs to fixed-cost discounted rates.** Free POCs were identified as a drain on billable capacity delivering bandwidth waste without guaranteed returns.

**An agent must never offer a free POC under any framing** — not as a "pilot," "trial," "sample," or "demonstration."

### Business Situation

Technical feasibility is genuinely uncertain, or the client needs to evaluate delivery quality before a larger commitment.

### Ideal Customer

Prospects with real budget who need de-risking, not prospects seeking free work.

### Advantages

| For the client | For Zediant |
|---|---|
| Validates feasibility at low cost | Discounted but paid — capacity is compensated |
| Evaluates delivery quality | Documented conversion path to larger engagements |
| Small commitment | Qualifies seriousness through willingness to pay |

### Limitations

- Discounted rate compresses margin
- May not convert
- Small scope may not represent full delivery complexity

### Typical Project Size

Small, at a discounted fixed cost. **Specific discount levels are not documented** — see [Discount Policy](#discount-policy).

### Typical Duration

4–8 weeks.

### Decision Makers

CTO · Founder · Head of Product.

### Business Outcomes

Documented commercial pattern: most long-term relationships began as a single small project and expanded once quality was proven.

### Recommended Services

Any, scoped small.

### Typical Risks

| Risk | Mitigation |
|---|---|
| Prospect expects free | State the policy clearly and early |
| POC scope creeps into a full build | Fixed scope, fixed price, fixed date |
| Discount becomes the expected ongoing rate | State that POC pricing is one-off |
| No conversion | Qualify budget for the follow-on before starting |

### Discovery Questions

46. What specifically needs proving — feasibility, or our capability?
47. If the POC succeeds, what is the next step and is it budgeted?
48. Who decides based on the outcome?
49. What would a successful POC need to demonstrate?

### Qualification Signals

Budget confirmed for the follow-on · Clear success criteria · Decision-maker engaged · Willing to pay for the POC.

### Disqualification Signals

Expects it free · No budget for what follows · Success criteria undefined · Running the same POC with several vendors on spec.

### When AI should recommend this model

Recommend where genuine technical uncertainty exists, or where a prospect wants to evaluate quality before a larger commitment. **Always paid, always fixed scope.**

---

## 9. AI Advisory

### Overview

Assessment of AI adoption viability, data readiness, and a staged roadmap.

### Business Situation

Board or leadership has mandated an AI initiative with no internal plan, or the team wants to know whether their data supports what is being asked.

### ⚠️ Scoping constraint

Zediant's defensible AI capability is **AI-assisted delivery**, not shipped AI products. Internal guidance is explicit about not overstating this. AI Advisory should focus on **readiness, feasibility, and staged adoption** — questions Zediant can answer well — rather than implying a delivery portfolio that does not exist.

### Ideal Customer

Organisations with an AI mandate and no plan, particularly where data readiness is the real blocker.

### Advantages

| For the client | For Zediant |
|---|---|
| Honest assessment rather than an AI sales pitch | Entry point into data and integration work |
| Realistic staged path | Differentiates through honesty |
| Identifies data gaps before spend | Aligns with documented AI-ready architecture positioning |

### Limitations

- **Competitors with genuine AI product portfolios will outrank Zediant** on pure AI engagements
- No AI product case study exists
- Risk of the engagement raising portfolio questions Zediant cannot answer

### Typical Project Size

Small.

### Typical Duration

2–4 weeks.

### Decision Makers

CTO · Head of Data · Founder · CIO.

### Business Outcomes

Not documented. Do not claim AI delivery outcomes.

### Recommended Services

`services.md` → Advisory & Consulting · Data Engineering & Analytics

### Typical Risks

| Risk | Mitigation |
|---|---|
| Prospect expects AI product delivery credentials | Scope honestly at the outset |
| Data is not ready and the client will not fund fixing it | Surface early |
| Loses to an AI-native specialist | Accept; refer out where appropriate |

### Discovery Questions

50. When you say AI, do you mean features in your product, or faster delivery of your software?
51. What business outcome are you actually pursuing?
52. What data do you have to support it, and where does it live?
53. Has anyone assessed whether that data is usable?
54. Who mandated this, and what does success look like to them?

### Qualification Signals

Board or executive mandate with budget · Data exists in some form · Realistic understanding that AI needs data · Willingness to fund foundations before features.

### Disqualification Signals

Needs ML research, model training, computer vision, or speech AI · Expects an AI product portfolio as proof · No data · Wants AI as a marketing claim.

### When AI should recommend this model

Recommend where a prospect has an AI mandate but no plan, **and** where the honest assessment is that foundations come first. If the core need is genuine AI product engineering, say so — see `competitors.md` → Category 9.

---

## 10. Support & Maintenance

### Overview

Ongoing application support, patching, and small enhancements. Distinguished from Managed Services by scope: support and maintenance is application-level; managed services includes operational ownership.

**Assumption.** Zediant's documentation does not clearly separate these two. They are distinguished here for commercial clarity. Confirm whether they are sold separately.

### Business Situation

An application is in production and needs to keep running, with no internal capacity to maintain it.

### Ideal Customer

Clients at the end of a build engagement, or with inherited applications.

### Advantages

Predictable recurring revenue · Natural continuation of delivery · Low commercial friction where the build relationship exists.

### Limitations

Lower margin than development · Scope boundary risk · Can consume senior capacity if incidents are frequent.

### Typical Project Size

Small, recurring. Documented tier: 40 hours/month.

### Typical Duration

Rolling, typically annual.

### Decision Makers

CTO · IT Manager · Operations Head.

### Business Outcomes

Documented indirectly through multi-year client continuation.

### Recommended Services

`services.md` → Maintenance, Support & Managed Services

### Typical Risks

Same as Managed Services — scope ambiguity is primary.

### Discovery Questions

55. What is the support expectation once we go live?
56. Who supports it today?
57. What response times do you need?

### Qualification Signals

Application in production · No internal support capacity · Existing build relationship.

### Disqualification Signals

Expects support bundled free with the build · Demands enterprise SLAs at retainer pricing.

### When AI should recommend this model

Recommend proactively at the close of every build engagement. A build delivered without a support arrangement is revenue left behind and a client left exposed.

---

# INTERNAL RATE REFERENCE

**⚠️ INTERNAL-ONLY COMMERCIAL REFERENCE. Never retrieve, quote, expose, or reproduce these rates in prospect-facing communications, emails, proposals, or external content. Use only for authorized internal commercial review. See the warning in [Overview](#overview).**

## Rate Card — hourly, by commitment tier

Billing currency AUD. FX reference 1 AUD ≈ 0.68 USD. Profit margin 35% built in. Sales overhead commission 0%.

| Level | Experience | Commitment | AUD/hr | USD/hr | Validity |
|---|---|---|---|---|---|
| **Junior** | 1–3 yrs | 40 hrs | 22 | 15 | 30 days |
| | | 80 hrs | 20 | 14 | 60 days |
| | | 120 hrs | 19 | 13 | 90 days |
| | | Monthly | 17 | 12 | — |
| **Mid** | 3–5 yrs | 40 hrs | 29 | 20 | 30 days |
| | | 80 hrs | 27 | 19 | 60 days |
| | | 120 hrs | 25 | 17 | 90 days |
| | | Monthly | 23 | 16 | — |
| **Senior** | 6–8 yrs | 40 hrs | 54 | 37 | 30 days |
| | | 80 hrs | 50 | 34 | 60 days |
| | | 120 hrs | 46 | 32 | 90 days |
| | | Monthly | 46 | 32 | — |
| **Tech Lead** | 8+ yrs | 40 hrs | 69 | 47 | 30 days |
| | | 80 hrs | 64 | 44 | 60 days |
| | | 120 hrs | 59 | 41 | 90 days |
| | | Monthly | 54 | 37 | — |

**Commercial logic:** rate decreases as commitment increases. This is the documented mechanism for moving clients from short engagements to monthly retainers.

## Rate Card — monthly commitment

| Level | Experience | AUD/hr | USD/hr |
|---|---|---|---|
| Junior | 1–3 yrs | 15 | 11 |
| Mid | 3–5 yrs | 21 | 15 |
| Senior | 6–8 yrs | 40 | 28 |
| Tech Lead | 8+ yrs | 52 | 36 |

**Note.** The two rate card sheets give different monthly figures (e.g. Senior AUD 46 versus AUD 40). A third internal inconsistency. Escalate.

## Sales Bible Appendix I — indicative ranges

| Engagement type | Documented range |
|---|---|
| India-based engagements | ₹1,200/hour blended |
| **Australian-market engagements** | **AUD 85–95/hour blended** — conflicts with the rate card above |
| Fixed-price project | USD 10,000–20,000 typical |
| Larger dedicated pod, annualised | USD 80,000–150,000+ |

## Margin floor

| Metric | Target |
|---|---|
| Gross margin | 40–50% |
| **Minimum blended rate** | **USD 25–30/hour** |
| Billable utilisation | 75–85% (currently 50–60%) |

**Critical implication.** At monthly rates, Junior is USD 11/hour and Mid is USD 15/hour — **both below the stated USD 25–30 blended floor.** A pod weighted toward junior and mid engineers will not meet the margin target. Any pod composition should be checked against the floor before it is quoted. This is a live commercial risk in the documented rate structure.

## Documented unit economics

From internal strategy — treat as a planning model, not a quotable figure:

| Metric | Value |
|---|---|
| Average retainer | USD 3,000/month (≈ ₹2.5 lakh) |
| Delivery cost per retainer | ≈ ₹1 lakh |
| Gross profit per retainer | ≈ ₹1.5 lakh |
| Break-even | One deal every three months covers the entire sales team and software cost |

---

# COMMERCIAL QUALIFICATION

## Budget indicators

| Signal | Strength |
|---|---|
| Named budget figure with approval path | **Strong** |
| Recent funding round with disclosed amount | **Strong** |
| Existing engineering payroll | Strong — proves the category exists |
| Current spend on contractors, freelancers, or another vendor | **Strong** — budget already allocated |
| Open engineering roles with disclosed salary bands | Strong — headcount budget convertible to contract |
| Recruitment fees being paid without a hire | Strong |
| Enterprise customers with higher contract values | Moderate |
| Existing platform licence spend | Moderate |
| "We're exploring options" with no figure | Weak |
| Asking for free work | **Disqualifying** |

## Buying authority

| Persona | Typical authority | Implication |
|---|---|---|
| Founder / CEO (10–200 staff) | Can commit without procurement | Fastest path — the reason Zediant targets this persona |
| CTO | Usually can commit at Zediant's deal size | Primary target |
| VP Engineering | Often needs CTO or CFO sign-off | Qualify the path |
| COO / MD (agency) | Owns P&L, can commit | Fast |
| Engineering Manager | Rarely commits at this size | Route upward |
| CIO (enterprise) | Requires procurement | Long cycle — escalate |
| IT Manager | Recommends, rarely decides | Route upward |

**Documented rationale.** Zediant targets C-suite and founder-level specifically because they can commit engineering budget without lengthy procurement at a USD 10,000–20,000 deal size.

## Business need

| Level | Description | Action |
|---|---|---|
| **Urgent, funded** | Named problem, deadline, allocated budget | Prioritise; loop in Founder |
| **Real, unfunded** | Genuine problem, budget not yet allocated | Help build the internal case |
| **Aspirational** | "We should probably..." | Nurture |
| **None** | Curiosity or benchmarking | Disqualify politely |

## Timeline

| Signal | Read |
|---|---|
| Committed external deadline (customer, investor, regulator) | Strongest — creates real urgency |
| Internal roadmap milestone | Moderate |
| "Sometime this year" | Weak |
| "We're just looking ahead" | Nurture only |

## Urgency

Genuine urgency comes from an external commitment, not internal enthusiasm. Test with: *"What happens if this doesn't get done this quarter?"* A vague answer means there is no deadline.

## Procurement process

| Type | Cycle | Zediant fit |
|---|---|---|
| Founder decides | Days to weeks | **Ideal** |
| CTO decides with budget | Weeks | **Ideal** |
| Finance approval required | Weeks to a month | Workable |
| Formal procurement / vendor onboarding | 1–3 months | Difficult — escalate |
| Public tender | 3–6+ months | **Avoid without a Teaming Agreement** |

## Decision process

Questions to establish it: who else is involved · what is the approval path for this amount · has anything similar been approved before, and how long did it take · what would stop this internally · is this budgeted, or does a case need building.

---

# DISCOVERY QUESTIONS

Fifty commercial discovery questions. Questions 1–56 above are model-specific; these are the general commercial set.

## Budget existence and size

1. Has a budget been allocated to this, or is it still being scoped?
2. Roughly what range are you working within?
3. Is this capital or operating expenditure?
4. What budget line does this come from — engineering, product, IT, or transformation?
5. What are you currently spending to address this problem?
6. What do you spend on contractors or external development today?
7. If you hired for this, what salary band would the role sit in?
8. Have you paid recruitment fees on this role already?
9. What is the cost to the business of this not being done?
10. What would you consider expensive for this, and what would you consider cheap?

## Authority and approval

11. Who else is involved in a decision like this?
12. Who signs off on spend at this level?
13. Have you approved something similar before? How long did it take?
14. What is the approval path — you, finance, board?
15. Is there a threshold above which this needs additional sign-off?
16. Who would object to this internally, and why?
17. Who owns the outcome if this succeeds?
18. Does procurement need to be involved?

## Timeline and urgency

19. What timeline are you working against?
20. What is driving that date?
21. Is that deadline external — customer, investor, regulator — or internal?
22. What happens if this slips a quarter?
23. When would you want a team starting?
24. Is there a budget cycle deadline affecting this?
25. What has stopped this from happening already?

## Commercial model preference

26. Do you have a preference between fixed price and time and material?
27. Is fixed price a procurement requirement or a preference?
28. How settled is the scope, honestly?
29. What is likely to change once we start?
30. Would you rather pay a premium for certainty, or pay for what gets built?
31. What commitment level are you comfortable with initially?
32. Would you want to start smaller before committing further?

## Prior vendor experience

33. Have you worked with an external engineering partner before?
34. What worked, and what didn't?
35. How was that engagement priced?
36. What would you do differently this time?
37. Are you speaking to other providers?
38. What do you like about the alternatives you're considering?
39. What would rule someone out for you?

## Value and comparison

40. What are you comparing this against — hiring, another vendor, or doing nothing?
41. If you hired instead, what would the fully-loaded cost be?
42. How long would hiring take, and what is the cost of that delay?
43. What would make this an obviously good decision for you?
44. What does success look like commercially, not just technically?

## Risk and terms

45. What contractual terms matter most to you?
46. Do you need an SLA, and is it contractual with your own customers?
47. What are your payment terms with other vendors?
48. Is there anything in your standard contract we should see early?
49. What security or compliance review does a new vendor go through?
50. What would need to be true for you to start next month?

---

# PRICING QUESTIONS

Guidance for the questions prospects actually ask.

## "What is your hourly rate?"

**Do not answer with a number.** Two internal sources conflict materially.

> "Rates depend on seniority and commitment level — a monthly commitment prices differently from ad-hoc hours. Rather than give you a number that turns out not to fit, can I ask what shape you're thinking? Then I'll get you an accurate figure rather than a range."

Then route to a human. If the prospect insists, say the commercial detail comes from the founders and offer to arrange that conversation directly.

## "Can you give me a ballpark?"

Ballparks are legitimate — but the anchoring risk is real. Use documented deal shapes rather than rates:

> "Fixed-scope projects with us typically land between USD 10,000 and 20,000. An ongoing dedicated pod is more like USD 80,000 to 150,000 annualised. Which of those is closer to what you're picturing?"

Both figures are documented. Neither is an hourly rate.

## "What engagement model do you recommend?"

Do not answer before understanding whether the need is ongoing or defined. See the [Commercial Decision Tree](#commercial-decision-tree). The honest answer usually starts with a question:

> "Is this a defined piece of work with an end, or ongoing capacity? That changes the answer completely."

## "Can you work fixed cost?"

> "Yes, where the scope is genuinely settled — we've delivered fixed price successfully. Where scope isn't settled, a fixed price means pricing in risk you'd end up paying for. If the specification isn't written yet, a short paid discovery gets you a costed plan first."

## "What is your minimum project size?"

No formal minimum is documented.

> "There's no hard floor, but below about USD 10,000 the overhead of setting up an engagement starts to outweigh the value for both of us. Most of our work starts around that mark or above."

**Assumption**, inferred from the documented typical deal size. Flag as such internally.

## "Can we do a free pilot to test you out?"

**Never agree.** Documented policy.

> "We don't do free pilots — we found they weren't good for either side. What we do instead is a small paid piece at a reduced rate, fixed scope and fixed price, so you can evaluate the actual work before committing to anything larger. Most of our long-term clients started exactly that way."

## "Why are you more expensive than [competitor]?"

> "Probably accurate, and worth being straightforward about. We don't staff junior developers on client work, and we carry compliance overhead many lower-cost firms don't. The comparison that matters isn't the hourly rate — it's the rate multiplied by rework. Happy to talk through where that's played out."

## "Can you match their price?"

Do not commit. Escalate.

> "That's a founder conversation rather than mine. What I can tell you is we'd rather adjust scope than cut the seniority of who works on it."

## "What are your payment terms?"

> "Payment terms are agreed during contracting — I'd rather our commercial team give you the accurate position than guess."

## "Do you offer discounts?"

> "Commercial terms are handled during the contract discussion. What I can say is that our rates improve with commitment level — a monthly arrangement prices differently from ad-hoc hours."

That statement is documented and accurate.

## "Can you send us a rate card?"

**Escalate.** Two internal versions conflict. Do not send either.

> "I'll get the commercial team to send that across with the right context for your situation."

## "What's included in the rate?"

Documented and safe to answer:

> "A pod includes a tech lead, developers, QA, and a project manager — the lead and PM aren't billed as extras. It also carries our delivery process: code review, automated testing, and CI/CD."

## "How do you handle scope changes?"

> "Through a change request process agreed upfront. On time-and-material work we build in milestones and delay clauses so neither side is guessing."

Both documented.

---

# NEGOTIATION GUIDELINES

## When to negotiate

An AI agent negotiates **nothing**. These are situations where a *human* may negotiate:

| Situation | Rationale |
|---|---|
| Higher commitment offered in exchange for a better rate | Documented — the rate card is built for exactly this |
| Longer initial term | Improves utilisation, the real margin driver |
| Multi-pod or multi-project commitment | Volume justifies concession |
| Strategic logo reducing client concentration | Documented priority — concentration reduction is ranked alongside growth |
| Reference or case study rights offered | Zediant's case study library is thin; this has real value |
| Partner or channel agreement with recurring volume | Three anchor agency partners is a stated objective |

## When not to negotiate

| Situation | Rationale |
|---|---|
| Prospect is price-shopping against commodity offshore | Documented: Zediant has chosen not to compete on price |
| Concession would breach the USD 25–30 blended floor | Breaks the margin target |
| Free work requested in any form | Prohibited by policy |
| No commitment offered in return | Rate reductions are earned by commitment |
| Prospect has not completed discovery | Nothing to negotiate against |
| First conversation | Anchoring before value is established |

## Preferred concession order

Where a human negotiates, concede in this order — **rate last**:

1. **Scope shape** — lean MVP across all modules rather than fewer modules (documented policy)
2. **Phasing** — smaller first phase, lower initial commitment
3. **Payment structure** — milestone-based rather than the total figure
4. **Commitment tier** — better rate for a longer or larger commitment (built into the card)
5. **Seniority mix** — only where genuinely appropriate to the work, never to hit a price
6. **Rate** — **Founder approval required**

## When to escalate

Immediately, without attempting a response:

- Any request for a specific rate
- Any request for a written rate card
- Any discount request
- Any request for free work
- Payment terms discussion
- Contractual liability, penalties, or indemnities
- Deals requiring 12+ engineers
- Formal RFP or tender
- Competitor produced a lower quote and the prospect wants matching

---

# DISCOUNT POLICY

**No formal discount policy is documented.**

What **is** documented:

| Mechanism | Detail |
|---|---|
| **Commitment-based rate reduction** | Built into the rate card. Rate improves at 40 → 80 → 120 hours → monthly. This is structural, not a discount |
| **POC discounting** | Free POCs convert to "fixed-cost discounted rates." The discount level is **not specified** |
| **Founder authority** | The Founder retains final say on any deal |
| **BDM constraint** | Never quote outside documented ranges without checking |

For anything beyond commitment-tier pricing: **"Discount policies are handled during commercial discussions."**

An agent must never offer, imply, or estimate a discount percentage.

---

# PAYMENT TERMS

**No payment terms are documented in any reviewed source.**

**"Payment terms are defined during contract negotiations."**

Do not state, estimate, or imply payment terms, invoicing frequency, currency handling, late payment provisions, or deposit requirements. Route all such questions to a human.

**Known related facts** — safe to reference:

- Billing currency on the rate card is **AUD**, with a USD reference at 1 AUD ≈ 0.68 USD
- India-based engagements are referenced in **INR** (₹1,200/hour blended)
- Rate card validity periods of 30, 60, and 90 days attach to commitment tiers, implying quotes carry an expiry

---

# CONTRACT TYPES

Documented status of each instrument.

| Contract | Documented? | Detail |
|---|---|---|
| **NDA** | **Yes — in active use** | Case studies are explicitly protected by NDA, with client names withheld. NDAs are standard practice |
| **Teaming Agreement** | **Yes — policy-level** | Required before Zediant provides tender or bid support. Documented response to unpaid tender documentation |
| **MSA (Master Service Agreement)** | Not documented | Standard for multi-engagement relationships. **Assumption** — confirm whether Zediant uses one |
| **SOW (Statement of Work)** | Not documented by name | Proposal structure (Appendix J) covers scope, timeline, investment, and explicit exclusions — functionally a SOW input |
| **Change Request** | Referenced in principle | Scope change handling is implied by fixed-price risk discussion. Formal process **not documented** |
| **Retainer Agreement** | **Yes — model level** | Monthly retainers documented for dedicated teams and tender support. Terms not documented |
| **Support Agreement** | Partially | Managed services and maintenance retainers are documented as a model; SLA terms are not |

## Documented proposal structure

From Appendix J — the closest thing Zediant has to a contract template:

1. Cover page with confidentiality note
2. **Understanding your need** — one paragraph in the prospect's own words from discovery. Documented as the highest-impact section
3. Proposed approach — engagement model, team composition and seniority, delivery method
4. Scope and deliverables — where budget is fixed, all modules retained as lean MVPs
5. Timeline — phased where possible
6. **Investment** — clear itemised pricing broken down by phase, role, or module. **Never a single unexplained total**
7. Why Zediant — senior talent, AI-assisted delivery, security posture, partnership track record
8. **What is explicitly out of scope** — content creation, data migration, data feeding, ongoing SEO execution
9. Next step — one clear call to action

**Proposal turnaround: within 2 business days** of a qualified discovery call. Documented; delays beyond this measurably reduce close rates.

---

# BUDGET RANGES

## Documented ranges — safe to reference

| Engagement shape | Range |
|---|---|
| Larger dedicated pod, annualised | **USD 80,000–150,000+** |
| Average retainer (internal planning model) | USD 3,000/month |

## INTERNAL PLANNING REFERENCE — NOT APPROVED FOR EXTERNAL QUOTATION

| Engagement shape | Range | Status |
|---|---|---|
| Fixed-price project | USD 10,000–20,000 | Inferred/assumed typical current deal size — not formally approved. Do not quote as a documented commercial figure. |

## Not documented

Everything else. For any engagement shape not listed above: **"Budget is determined after discovery."**

Specifically undocumented: minimum engagement size · POC pricing · workshop pricing · advisory day rates · managed services retainer bands · SLA pricing tiers · onboarding or ramp charges · travel or expenses.

**Never invent a number for any of these.**

---

# COMMERCIAL OBJECTIONS

| Objection | Guidance | Escalate? |
|---|---|---|
| **"Too expensive."** | Acknowledge directly. Reframe from rate to total cost including rework, missed deadlines, and security gaps. Do not defend the rate abstractly. | No, unless a specific number is demanded |
| **"We need lower rates."** | Ask what commitment they can offer in return — the rate card is built for exactly this trade. Do not concede unilaterally. | **Yes**, for any actual rate change |
| **"We need fixed cost."** | Fine where scope is settled. Where it isn't, offer paid discovery to produce a costed plan. Never guess a fixed price on unclear scope. | No |
| **"We need a trial."** | Offer a small paid piece at reduced rate, fixed scope and price. Reference that most long-term clients started this way. | No |
| **"We need a free POC."** | **Refuse, warmly and without apology.** Documented policy. Offer fixed-cost discounted scope instead. | No — the answer is always no |
| **"We need an on-site team."** | Qualify how hard the requirement is. If genuinely fixed, Zediant is not a fit — say so. | No |
| **"We need a local team."** | Qualify which parts genuinely need local presence. Often strategy and client-facing work do; engineering does not. | No |
| **"Your competitor quoted 30% less."** | Acknowledge it is probably accurate. Explain the seniority and compliance difference. Do not match. | **Yes** if matching is requested |
| **"Send us your rate card."** | Do not send. Two internal versions conflict. | **Yes** |
| **"What are your payment terms?"** | "Defined during contract negotiations." | **Yes** |
| **"We need an SLA with penalties."** | Underwriting decision, not a sales one. | **Yes** |
| **"Can you invoice in our currency?"** | Not documented. | **Yes** |
| **"We only work with local entities."** | No AU or UAE entity is documented. Flag honestly. | **Yes** |
| **"Our procurement needs three quotes."** | Signals a formal process and a longer cycle. Qualify whether Zediant is a genuine contender or column filler. | **Yes** |
| **"We'd want to own the IP."** | Standard expectation for custom development. Terms not documented. | **Yes** |

---

# COMMERCIAL DECISION TREE

```
START: Prospect has a real need and some budget signal
│
├─ Q1. Is the need ONGOING or a DEFINED DELIVERABLE?
│   │
│   ├─ ONGOING → Q2. Does the client have internal technical management?
│   │            ├─ STRONG   → Do they want capacity or outcomes?
│   │            │             ├─ Capacity → STAFF AUGMENTATION
│   │            │             └─ Outcomes → DEDICATED POD
│   │            └─ WEAK/NONE → DEDICATED POD (they need the lead and PM)
│   │
│   └─ DEFINED → Q3. Is the scope genuinely specified in writing?
│                ├─ YES → Is the client comfortable with cost variability?
│                │        ├─ NO  → FIXED COST
│                │        └─ YES → TIME & MATERIAL
│                └─ NO  → DISCOVERY WORKSHOP or paid ADVISORY first
│                         Never quote fixed price on unwritten scope
│
├─ Q4. Is the application already in production and needing upkeep?
│   └─ YES → SUPPORT & MAINTENANCE, or MANAGED SERVICES if
│            operational ownership is wanted
│
├─ Q5. Is the client at a DECISION POINT rather than a build point?
│   ├─ Architecture or platform decision → ADVISORY (paid)
│   ├─ AI mandate with no plan           → AI ADVISORY (scope honestly)
│   └─ Feasibility genuinely uncertain   → POC (paid, fixed scope, never free)
│
├─ Q6. COMMERCIAL VIABILITY CHECK — run before recommending anything
│   ├─ Total deal below ~USD 10,000?           → Likely not viable. Qualify hard
│   ├─ Blended rate below USD 25–30/hour?      → Breaks the margin floor. Escalate
│   ├─ Requires 12+ engineers?                 → Exceeds capacity. Escalate
│   ├─ Requires free work?                     → REJECT. Policy
│   ├─ Competing purely on lowest rate?        → DISQUALIFY
│   ├─ Public tender without Teaming Agreement?→ REJECT. Policy
│   └─ Expands the already-concentrated account?→ Deprioritise vs a new logo
│
└─ Q7. Which model maximises EXPANSION potential?
    Where two models both fit, choose the one with the better expansion path.
    Documented pattern: small first engagement → proven quality → expansion.
    Preference order: Pod > T&M > Managed Services > Staff Aug > Fixed Cost
```

**Q6 clarification — internal viability reference:** deal below approximately USD 10,000 may be considered likely not viable and should be qualified carefully. This is an internal planning threshold only. It is **NOT** a minimum project size, minimum contract value, or approved external pricing floor and must never be presented to prospects as such, and must never be quoted, emailed, or included in prospect-facing proposals or commercial communications.

---

# COMMERCIAL AUTHORITY BOUNDARY

The automated agent **MUST NOT independently:**

- negotiate price
- approve discounts
- change payment terms
- change contractual terms
- approve SLA commitments
- approve penalties
- approve guarantees
- approve commercial exceptions
- commit delivery dates
- commit team composition where not already approved
- create binding commercial commitments

**The agent may:**

- explain approved commercial models
- explain approved pricing ranges where explicitly authorized
- identify the appropriate commercial model
- explain what information is needed for a quote
- recommend discovery where scope is unclear
- escalate commercial decisions to the authorized human

When authority is unclear: **ESCALATE — DO NOT GUESS.**

This preserves the existing Founder/commercial approval hierarchy documented throughout this file (see [Negotiation Guidelines](#negotiation-guidelines) and [Escalation Rules](#escalation-rules)). It does not create new approval roles or change who holds final commercial authority.

**Campaign-selection boundary.** `pricing-public.md` may recommend a commercial engagement model after assessing the prospect's need, but it does not select or assign the campaign. `campaign-selection` remains the sole authority for selecting the single primary C1–C5 campaign. The operational rule remains ONE LEAD → ONE PRIMARY CAMPAIGN.

---

# ESCALATION RULES

## Escalate immediately — do not respond

| Trigger | Route to |
|---|---|
| Any specific hourly or daily rate requested | Founder |
| Written rate card requested | Founder |
| Any discount request | Founder |
| Payment terms, invoicing, or currency questions | Founder / Finance |
| Contractual liability, penalties, indemnities | Founder |
| SLA with financial penalties | Founder |
| IP ownership terms | Founder |
| Formal RFP, tender, or procurement process | Founder |
| Public sector tender | Founder — Teaming Agreement required first |
| Deal requiring 12+ engineers | Founder — exceeds capacity |
| Competitor quote matching requested | Founder |
| MSA, SOW, or legal document review | Founder |
| Request for a client reference | Founder — NDA constraints |
| SOC 2 attestation report requested | Founder — position contested |
| Local legal entity required for contracting | Founder |
| Multi-year or multi-pod commitment | Founder |
| Anything the Founder has previously priced differently | Founder |

## Handle without escalation

- Explaining engagement models and their trade-offs
- The approved deal-shape range (USD 80k–150k+ annualised pod) — see [Budget Ranges](#budget-ranges) for the fixed-price range's internal-only, not-approved-for-quotation status
- Explaining what is included in a pod
- Explaining the change request principle
- Explaining why free POCs are not offered
- Commercial discovery questions
- Qualifying budget, authority, timeline, and process
- Explaining scope-versus-price trade-offs in principle

## The governing rule

**The Founder retains final say on any deal.** This is documented and absolute. When uncertain whether to escalate, escalate. A delayed answer costs less than a wrong number that becomes an anchor.

---

# AI RETRIEVAL RULES

## How to use this document

| Trigger | Retrieve |
|---|---|
| Prospect asks about price | [Pricing Questions](#pricing-questions) — never the rate tables |
| Choosing an engagement model | [Commercial Decision Tree](#commercial-decision-tree) |
| Qualifying budget | [Commercial Qualification](#commercial-qualification) |
| Preparing a discovery call | [Discovery Questions](#discovery-questions) |
| Handling a commercial objection | [Commercial Objections](#commercial-objections) |
| Prospect mentions contracts | [Contract Types](#contract-types) |
| Building a proposal | Documented proposal structure in [Contract Types](#contract-types) |
| Unsure whether to answer | [Escalation Rules](#escalation-rules) |

## Hard rules

1. **Never quote an hourly rate.** Two internal sources conflict by 25–75%.
2. **Never send a rate card.** Two versions exist and disagree.
3. **Never offer free work** — not as a POC, pilot, trial, sample, or demonstration.
4. **Never state payment terms.** None are documented.
5. **Never state a discount percentage.** No policy exists.
6. **Never invent a minimum project size.** The USD 10,000 guidance is inferred and marked as an assumption.
7. **Never quote fixed price on unwritten scope.** Offer paid discovery.
8. **Never commit to an SLA, penalty, or guarantee.**
9. **Check the margin floor** before recommending any pod composition — junior and mid monthly rates sit below it.
10. **Check capacity** — 5–7 developers in three months — before discussing any engagement shape.
11. **Prefer the model with better expansion potential** where two fit equally.
12. **Weight new logos above existing-client expansion.** Concentration reduction is a documented standing priority.
13. **When uncertain, escalate.** The Founder holds final authority on every deal.

## Externally Usable Figures — Context Restricted

The only commercial numbers an agent may state to a prospect, each restricted to the stated context:

| Figure | Context | Rule |
|---|---|---|
| USD 80,000–150,000+ | Larger dedicated engineering pod / annualised engagement | Use only when the applicable commercial context is established |
| 5–10 days | Team onboarding | Use only where the applicable onboarding context is established |
| 5–7 developers in 3 months | Capacity/scaling reference — use when qualifying out | Qualification/capacity context only; do not present as a guaranteed delivery commitment |
| 30 days notice | Scale-down terms documented for agency pitches | Agency-pitch context only; do not generalize as a universal Zediant contractual term |
| 2 business days | Proposal turnaround | Use only when the applicable operational context is confirmed; do not present as a universal contractual commitment |

**USD 10,000–20,000 is not in this list.** See [Budget Ranges](#budget-ranges) — it is an internal planning reference, not an approved external figure.

**None of the figures above may be generalized into universal pricing, contractual terms, delivery commitments, capacity guarantees, or commercial promises. Use only where the applicable context and approval are established.**

Everything else is internal reference or requires escalation.

---

# DOCUMENT CONTROL

| Attribute | Value |
|---|---|
| Document | `pricing-public.md` |
| Purpose | Commercial reference for Zediant AI sales, proposal, and meeting-prep agents |
| Engagement models documented | 10 |
| Sources | Zediant Rate Card (Rate_Card.xlsx), Sales Bible v1.0 Appendices I and J, 12-Month Sales & Growth Strategy (March 2026), Strategic Growth Plan, Zediant Company Profile 2026 |
| Last verified | August 2026 |

## Open items requiring human decision — ordered by commercial risk

1. **🔴 Rate card conflict.** Sales Bible says AUD 85–95/hour blended for Australia; the Rate Card peaks at AUD 69/hour for a Tech Lead. A blended rate cannot exceed the highest individual rate. **Nothing can be quoted until this is resolved.**
2. **🔴 Margin floor versus rate card.** Junior (USD 11/hr) and Mid (USD 15/hr) monthly rates sit below the stated USD 25–30/hour blended floor. A junior-weighted pod cannot hit the 40–50% gross margin target. The rate structure and the margin target are not compatible as written.
3. **🟠 Two rate card sheets disagree** on monthly rates — Senior appears as both AUD 46 and AUD 40.
4. **🟠 Pod tier definitions conflict** between the website (Foundation / Growth / Enterprise) and internal strategy (Maintenance / Growth / Scale), on both name and composition.
5. **🟠 No payment terms documented** anywhere.
6. **🟠 No discount policy documented** beyond commitment-tier structure. POC discount level unspecified.
7. **🟡 No documented minimum project size.** The USD 10,000 guidance is inferred.
8. **🟡 MSA, SOW, and change request processes not documented.**
9. **🟡 No AU or UAE legal entity documented** — may constrain contracting.
10. **🟡 Discovery Workshop and AI Advisory** are constructed here from documented policy; neither is a named Zediant product. Confirm before offering.
11. **🟡 Support & Maintenance versus Managed Services** are not clearly separated in source documents.
12. **🟡 Rate card FX reference** of 1 AUD ≈ 0.68 USD is undated and will drift.

## Recommended immediate action

Until items 1 and 2 are resolved, every agent should treat pricing as **escalation-only**. The reputational cost of quoting a rate that the Founder then revises upward is higher than the friction of saying "let me get you an accurate figure."

## Related Context Files

| File | Relationship |
|---|---|
| `company.md` | Business model, capacity constraints, and commercial position |
| `services.md` | Service definitions and engagement models per service |
| `icp.md` | Commercial Fit dimension and budget qualification signals |
| `campaigns.md` | When pricing may and may not enter an outreach sequence |
| `case_studies.md` | Documented engagement models, team sizes, and durations by project |
| `competitors.md` | Price objection handling and competitive rate positioning |
