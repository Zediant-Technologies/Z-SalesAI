# Overview

This document defines who Zediant Technologies should sell to, who it should not, and how an AI agent should decide between the two.

For Zediant specifically, an ICP is not "any company that needs software built." Zediant is a 25–35 person engineering firm operating at break-even with approximately 90% of revenue concentrated in a single client. It can onboard 5–7 additional developers within three months. Those three facts constrain the ICP more than any market opportunity does.

A good Zediant prospect is therefore one that:

1. Needs sustained engineering capacity rather than a one-off deliverable
2. Can be served within a 5–7 developer ramp
3. Has a founder, CTO, or COO who can commit budget without extended procurement
4. Sits in Australia or the UAE, where Zediant has delivery history and time-zone advantage
5. Reduces rather than increases revenue concentration

## The two-axis ICP model

Zediant's ICP operates on two independent axes. An agent must evaluate both.

| Axis | Question it answers | Drives |
|---|---|---|
| **Segment** | How do we sell to them? | Campaign selection, messaging, sender, cadence |
| **Vertical** | Do we have proof for them? | Case study selection, credibility, discovery depth |

A prospect can be a strong segment fit with no vertical proof (a SaaS company in a sector Zediant has never served) or a strong vertical fit with a weak segment motion (a large automotive enterprise requiring procurement Zediant cannot survive). Both matter. Neither alone is sufficient.

**Segment ICPs** are the go-to-market motion, defined in Zediant's internal sales playbook as Lists A, B, and C.
**Vertical ICPs** are the six industries where Zediant holds documented delivery evidence.

## What this document does not do

It does not rank market attractiveness in the abstract. It ranks fit against Zediant's actual capacity, proof, and commercial position as of August 2026. When Zediant's concentration risk resolves or headcount grows, the priorities here should be revisited.

Cross-reference: `company.md` for capability and limitation detail · `services.md` for service definitions · `campaigns.md` for campaign structure.

---

# ICP Framework

Every prospect is evaluated across five dimensions. An agent should assess all five before recommending action.

## 1. Business Fit

Does the prospect's business situation create a durable need for external engineering capacity?

| Signal | Strong | Weak |
|---|---|---|
| Engineering demand | Ongoing roadmap or recurring project pipeline | Single defined deliverable, then nothing |
| Internal team | Exists but constrained | None at all, or fully sufficient |
| Hiring position | Trying and failing to hire, or frozen | Hiring successfully and quickly |
| Growth trajectory | Scaling, funded, or expanding | Contracting or static |

## 2. Technical Fit

Can Zediant actually build what this prospect needs?

| Signal | Strong | Weak |
|---|---|---|
| Stack overlap | .NET, Java, React, Node, PHP, mobile, cloud | Rust, Go, Elixir, embedded, blockchain protocol, low-code platforms |
| Work type | Product development, integration, modernisation, platform | AI/ML research, computer vision, speech AI, model training |
| Architecture | Web, mobile, API, microservices, middleware | Firmware, real-time control systems, HPC |
| Integration surface | CRM, ERP, DMS, POS, cloud services | Proprietary systems with no access granted |

**Hard technical exclusions.** Zediant does not do deep AI/ML research or model building, computer vision, speech AI, or low-code/no-code platform work. These are documented capability boundaries, not preferences.

## 3. Commercial Fit

Can this prospect pay at Zediant's rate level, and is the deal shape viable?

| Signal | Strong | Weak |
|---|---|---|
| Deal size | USD 10,000–20,000 fixed scope; USD 80,000–150,000+ annualised pod | Below USD 5,000; or above what a 5–7 developer ramp can serve |
| Rate tolerance | Accepts senior-rate positioning | Comparing against lowest-cost freelance or commodity offshore |
| Blended rate viability | Supports a minimum USD 25–30/hour blended rate | Below the documented margin floor |
| Engagement shape | Retainer, pod, or T&M | Demands fixed price on undefined scope |
| Speculative work | Willing to pay for POC or discovery | Expects free POC or unpaid tender documentation |

**Documented commercial rule.** Internal strategy explicitly directs Zediant to stop free POCs and unpaid tender documentation, converting these to fixed-cost discounted rates or retainer/Teaming Agreement arrangements. An agent should treat a demand for free speculative work as a commercial disqualifier, not a relationship investment.

## 4. Strategic Fit

Does winning this account improve Zediant's position beyond the revenue?

| Signal | Strong | Weak |
|---|---|---|
| Concentration impact | New logo, reduces dependence on the dominant client | Further expansion of the already-dominant account |
| Reference potential | Willing to be named or provide a reference | Strict NDA with no reference rights |
| Geographic depth | Australia or UAE, deepening regional case studies | Scattered market with no follow-on |
| Vertical depth | Automotive, fintech, or another proven vertical | One-off sector with no repeatability |
| Partner potential | Agency or consultancy that could refer repeat work | Terminal end-client with no network effect |

**Documented strategic priority.** Internal materials state that reducing dependency on the single largest client is a standing priority ranked *alongside* revenue growth, not below it. A new-logo win worth ₹15 lakh is explicitly valued more highly than the same revenue from the dominant client. The stated target is no single client above 40% of revenue within 12–18 months.

## 5. Growth Potential

Will this relationship expand?

| Signal | Strong | Weak |
|---|---|---|
| Entry shape | Small scope with visible follow-on work | Terminal project with defined end |
| Roadmap visibility | Multi-quarter roadmap discussed | No forward plan articulated |
| Expansion surface | Multiple systems, teams, or products | Single isolated application |
| Relationship depth | Multiple stakeholders engaged | Single champion, no multi-threading |
| Historical pattern match | Resembles Networx or STAGER progression | Resembles a transactional vendor engagement |

**Documented expansion pattern.** Most long-term Zediant relationships began as a single small project and expanded once delivery quality was proven. Networx is the documented example: small projects first, then an ongoing managed services arrangement. An agent should weight a small opening scope with expansion surface *above* a larger one-off project.

## ICP scoring model

Two scores exist and must not be confused.

### ICP Score — set once at sourcing, before any contact

| Criterion | Points | Source |
|---|---|---|
| Company fit (exact segment match on size, stage, category) | 0–25 | Search filters and firmographics |
| Buying signal present | 0–30 | Funding, hiring, expansion, incident, acquisition |
| Right persona reached | 0–25 | CEO, Founder, CTO, or COO |
| Geography match | 0–20 | Australia or UAE = 20; secondary markets score lower |

### PTB Score — Propensity To Buy, re-scored as engagement occurs

| Criterion | Points | Signal |
|---|---|---|
| Engagement | 0–40 | Connection accepted, email opened, replied |
| Urgency signal | 0–30 | Timeline, budget, or pain point stated in a reply or call |
| Multi-threading | 0–15 | More than one stakeholder engaged |
| Decision-maker confirmed reachable | 0–15 | The right persona is actually responsive |

**Assumption flag.** The PTB component weights are a proposed default and have not been confirmed by Zediant leadership. Treat as provisional.

**Known inconsistency.** Zediant's Sales Bible (Appendix C) defines a single blended model with different weights — Company fit 0–20, Buying signal 0–25, Persona 0–20, Geography 0–15, Engagement 0–20. The two-score split above supersedes it for AI agent use, because engagement data does not exist at sourcing time and cannot be scored then. Flag this if a human references the Sales Bible weights.

### Shared tiering

| Score | Tier | Action |
|---|---|---|
| 80–100 | **Hot** | Prioritise immediately; loop in the Founder early |
| 50–79 | **Warm** | Standard sequence, normal priority |
| Below 50 | **Cold** | Low-touch nurture; do not spend enrichment credits |

---

# PRIMARY ICPs — SEGMENT

These three segments define Zediant's go-to-market motion. Every outbound prospect should map to exactly one.

---

# ICP 1 — Digital Agencies

## Industry Overview

Independent digital, creative, and technology agencies that sell strategy, design, and delivery to their own client base. They carry recurring project pipelines but variable engineering demand, which makes permanent development headcount economically awkward. Zediant positions as white-label delivery capacity behind the agency's brand.

Internal strategy refers to this segment as **"Aggregators"** — organisations that already manage portfolios of 50+ clients, allowing Zediant to reach many end-clients through one relationship at near-zero incremental customer acquisition cost. Securing three anchor agency partners is a stated strategic objective.

## Why They Need Zediant

Agencies win work in bursts. A large project lands and the choice is to hire (slow, and creates bench cost when the project ends), subcontract (variable quality, no continuity), or decline the work. Zediant offers a fourth option: a white-labelled pod that scales up for the project and down afterwards, without redundancy exposure.

## Business Problems

- Project won that exceeds current delivery capacity
- Bench cost between projects erodes already-thin margins
- Turning down work because the team cannot absorb it
- Client deadlines fixed but delivery capacity variable
- Reliance on freelancers with no continuity or accountability
- Design and strategy capability strong, engineering capability shallow
- Margin compression from subcontracting at retail rates

## Technology Challenges

- No in-house senior engineering leadership
- Inconsistent code quality across freelance contributors
- No shared delivery standards, CI/CD, or code review process
- Legacy client estates the agency must support but did not build
- CMS and e-commerce platform work exceeding team depth
- Mobile capability absent or outsourced ad hoc
- Security requirements from enterprise end-clients the agency cannot satisfy

## Digital Transformation Challenges

- End-clients asking for platform work beyond the agency's marketing origins
- Pressure to offer AI capability without engineering depth to deliver it
- Moving from project billing to retainer and managed-service models
- Building repeatable delivery rather than bespoke effort every time

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 10–100 |
| Revenue | Approximately AUD 3M–15M (**assumption**, inferred from documented targets at ~AUD 4–5M) |
| Growth stage | Established, project-driven, 5+ years trading |

## Geography

Australia (primary — Sydney, Melbourne, Brisbane, Perth), UAE (primary — Dubai). United Kingdom opportunistic.

## Decision Makers

| Role | Priority | Why |
|---|---|---|
| COO / Head of Delivery | **Primary** | Owns delivery capacity and margin; feels the problem daily |
| Managing Director | **Primary** | Owns P&L; can commit without procurement |
| Founder / CEO | **Primary** | Same, in owner-operated agencies |
| CTO / Technical Director | Secondary | Present in technical agencies; evaluates quality |
| Operations Manager | Secondary | May scope but rarely decides |

**Sender mapping.** pritamjit@ — the BDM mailbox is assigned to agency directors, heads of delivery, and operations leaders.

## Buying Signals

- Recently won a large or named client contract
- Job posts for developers, especially multiple simultaneous roles
- Headcount reduced while client roster holds (bench cut, capacity now external)
- Agency acquisition or merger
- New service line announced requiring engineering depth
- Expansion into a new city or country
- Public case studies showing platform work beyond their core offering
- Award wins or PR indicating pipeline growth

## Negative Signals

- Pure creative, brand, or media-buying agency with no development offering
- Under 10 employees (insufficient project volume to sustain a pod)
- Already owns a captive offshore development arm
- Recruitment or staffing agency rather than a delivery agency
- Headcount declining sharply with no compensating pipeline
- Positions itself as a full-service competitor to Zediant rather than a channel

## Technology Stack

WordPress, Drupal, Joomla, Shopify, Magento, BigCommerce, WooCommerce, Sitecore, Optimizely, HubSpot, ActiveCampaign, React, Angular, jQuery, PHP/Laravel, .NET, Node.js, Figma-class design tooling, AWS, Azure.

## Budget Indicators

- Existing subcontractor or freelance spend (proves budget exists and is already allocated)
- Retainer clients providing predictable revenue
- Enterprise or government end-clients (higher project values)
- Multi-year client relationships
- Physical office and 20+ headcount

## Urgency Indicators

- Named project win with a committed delivery date
- Developer resignation mid-project
- End-client escalation on a late delivery
- Pitch won that requires capability the agency does not have
- Tender response requiring engineering capacity to be evidenced

## Qualification Questions

1. What does your delivery team look like today — in-house, freelance, or a mix?
2. How many developers do you have, and what disciplines?
3. When you win a project larger than the team can absorb, what do you do?
4. How often does that happen?
5. What have you had to turn down in the last twelve months?
6. What does your current subcontractor or freelance spend look like?
7. What has gone wrong with external development partners before?
8. How important is white-labelling — do your clients know who builds?
9. What is the typical size and duration of a project for you?
10. What is your client mix — retainer or project?
11. What technologies do your projects typically require?
12. Do you have internal technical leadership, or does that fall to you?
13. What happens to your team between large projects?
14. What are your margins on subcontracted development versus in-house?
15. What deadlines are you working against right now?
16. Who signs off on a delivery partner decision?
17. Do your end-clients impose security or compliance requirements on you?
18. What time-zone overlap would you need to work comfortably?
19. Would you start with one project before committing to a longer arrangement?
20. If capacity were not a constraint, what work would you be pursuing?

## Recommended Services

| Priority | Service |
|---|---|
| 1 | Dedicated Engineering Pods (white-labelled) |
| 2 | Staff Augmentation |
| 3 | Web Application Development |
| 4 | E-commerce & CMS Development |
| 5 | Mobile Application Development |
| 6 | Maintenance & Managed Services |
| 7 | QA & Test Automation |

## Recommended Campaign

**C2 — Engineering Pods & Staff Augmentation.** Sender: pritamjit@. See `campaigns.md`.

## Recommended Email Angle

Lead with the bench-versus-backlog trade-off, not with technology. The agency leader's problem is commercial, not technical: capacity that must flex without carrying cost. Emphasise white-labelling, scale-down terms, and time-zone overlap. Do not lead with AI — an agency COO does not buy AI, they buy predictable delivery capacity.

Effective opening frame: *"When you win a project bigger than your current bench, do you hire, subcontract, or stretch the timeline?"*

## Common Objections

| Objection | Response direction |
|---|---|
| "We already have freelancers we trust." | Continuity and accountability — a freelancer leaving mid-project has no backfill; a pod does |
| "Our clients wouldn't accept offshore." | White-label model; clients see the agency's brand |
| "We can't afford your rates on our margins." | Compare against fully-loaded cost of a local hire plus bench time, not against a freelance hourly rate |
| "We've been burned by offshore before." | Start with a small defined scope; senior-only staffing; reference an existing agency client |
| "Time zones make it hard." | 2.5 hours to Perth, 4.5 to Sydney; overlap is structured deliberately, not left to chance |

## Success Stories

DIJGTAL (Australia) — Project Manager Kevin Moynihan describes moving from a single internal IT person to needing a full organisation, and states Zediant "blend in perfectly." Networx (Australia) — CEO Mikhael Haider describes starting with small projects and growing into an ongoing managed services arrangement. See `case_studies.md`.

## Priority Score

**HIGH.** This is the segment with the best channel economics (one relationship reaching many end-clients), the clearest pain, the shortest decision path, and a documented strategic objective attached to it (three anchor agency partners).

---

# ICP 2 — SaaS Companies (Seed to Series B)

## Industry Overview

Venture-funded software product companies between seed and Series B, typically 10–200 employees, with a defined product, paying customers, and a roadmap that outpaces engineering capacity. Internal materials name this segment the **highest strategic priority** because it aligns with Zediant's long-term positioning as an AI-enabled product engineering partner.

## Why They Need Zediant

Funded SaaS companies are measured on shipping speed against a finite runway. Senior engineering hiring in Australia and the UAE is slow and competitive, and every month a roadmap item slips is a month of runway spent without progress. A pod adds capacity in 5–10 days without permanent headcount commitment.

## Business Problems

- Roadmap commitments made to investors or customers that engineering cannot meet
- Runway pressure making a wrong hire expensive and slow to correct
- Founders still writing code instead of selling or raising
- Feature velocity slower than better-funded competitors
- Customer churn attributable to missing features
- Technical debt from a fast MVP now blocking growth
- Hiring competing against better-funded local employers

## Technology Challenges

- MVP architecture not built to scale past current tenant count
- No multi-tenant experience on the team
- Single points of failure in a small engineering team
- Manual deployment and no CI/CD discipline
- No automated test coverage, making refactoring unsafe
- Security posture insufficient for enterprise customers or SOC 2 requirements of their own
- Data not structured to support analytics or AI features

## Digital Transformation Challenges

- Moving from a founder-built prototype to a production platform
- Adding AI features under competitive pressure without in-house LLM experience
- Enterprise customers imposing security and compliance requirements the startup cannot meet
- Scaling engineering process, not just headcount

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 10–200 |
| Revenue | ARR approximately USD 1M–20M (**assumption**, inferred from stage) |
| Funding stage | Seed, Series A, Series B |
| Growth stage | Post-product-market-fit, scaling |

## Geography

Australia (primary — Sydney, Melbourne, Brisbane, Perth), UAE (primary). United Kingdom, United States, South Africa opportunistic.

## Decision Makers

| Role | Priority | Why |
|---|---|---|
| CTO / Co-founder & CTO | **Primary** | Owns the build decision and the hiring problem |
| Founder / CEO | **Primary** | Owns runway and roadmap; decides fast at this stage |
| VP Engineering / Head of Engineering | **Primary** | Owns velocity where a CTO layer exists above |
| Engineering Manager | Secondary | Influences; rarely decides at this deal size |
| Head of Product | Secondary | Feels roadmap slippage acutely; strong internal champion |

**Sender mapping.** manish@ for CTO and VP Engineering (technical tone: architecture, AI-assisted development, scalability, security). rajeev@ for Founders and CEOs (founder tone: engineering partnership, business outcomes, long-term collaboration).

## Buying Signals

- Funding round announced (strongest single signal — capital allocated to engineering)
- Multiple open engineering roles, especially senior or long-vacant
- Public roadmap or product launch commitment
- Acquisition completed, creating integration workload
- Competitor shipped a feature they lack
- Scaling complaints visible in reviews, status pages, or support channels
- Hiring for platform, architecture, or DevOps roles
- New enterprise logo announced (triggers security and scale requirements)
- Founder posting publicly about hiring difficulty

## Negative Signals

- Pre-seed or idea stage with no funding and no product
- No technical co-founder or engineering leadership
- Bootstrapped with a strict cost-minimisation posture (still qualifiable — see AutoRFP-type angle — but at lower priority)
- Already has a large offshore team
- Core need is AI/ML research rather than product engineering
- Recently completed layoffs with contracting roadmap
- Fewer than 10 employees with no funding

## Technology Stack

React, Next.js, Angular, Vue-adjacent, Node.js, Python, .NET, Java Spring Boot, PostgreSQL, MongoDB, Redis, AWS, Azure, GCP, Docker, Kubernetes, Terraform, GitHub Actions, Stripe-class payments, Segment-class analytics, OpenAI API, LangChain, vector databases.

## Budget Indicators

- Named funding round with disclosed amount
- Existing engineering payroll (proves budget category exists)
- Paying enterprise customers
- Prior use of contractors or agencies
- Investor pressure for delivery milestones
- Named CTO or VP Engineering role filled

## Urgency Indicators

- Funding closed within the last six months
- Investor-committed roadmap milestone approaching
- Enterprise deal contingent on a feature or security posture
- Key engineer resignation
- Competitor launch
- Runway under 18 months creating shipping pressure
- Security questionnaire blocking a deal

## Qualification Questions

1. What does your engineering team look like today, and how large?
2. What roles are open, and how long have they been open?
3. What is driving the need to extend capacity now?
4. What is the biggest bottleneck in shipping — speed, specific skills, or budget?
5. Which roadmap items have slipped in the last two quarters, and why?
6. What percentage of the team's time goes to maintenance versus new development?
7. What is your current architecture, and what is breaking about it?
8. Is the platform multi-tenant today? Does it need to be?
9. What scale are you designing for over the next 18 months?
10. Do you have CI/CD, code review, and automated test coverage?
11. Has anyone on the team built LLM or AI features into production?
12. When you say AI, do you mean features in your product or faster delivery of your software?
13. What is your funding position and runway?
14. Are there investor-committed milestones driving the timeline?
15. Have you worked with an external engineering partner before? What worked and what didn't?
16. Who would a pod report to, and is there a product owner with time available?
17. What working hours overlap would you need?
18. What does your security review look like for a new vendor?
19. Who else is involved in a decision like this?
20. Would you prefer to start with a defined initial scope before committing longer term?

## Recommended Services

| Priority | Service |
|---|---|
| 1 | Dedicated Engineering Pods |
| 2 | AI-Enabled Product Engineering |
| 3 | Platform Engineering & Cloud DevOps |
| 4 | QA & Test Automation |
| 5 | Advisory & Consulting (architecture review as entry) |
| 6 | Mobile Application Development |
| 7 | Data Engineering & Analytics |

## Recommended Campaign

**C1 — AI-Enabled Product Engineering** (funded, roadmap-driven) or **C2 — Engineering Pods & Staff Augmentation** (active engineering hiring). See `campaigns.md`.

## Recommended Email Angle

Lead with roadmap-versus-headcount. The CTO's problem is that the roadmap grows faster than the local senior talent market allows. Emphasise senior-only staffing, speed to team, and that the client interviews every engineer. Offer a technical overview or architecture review as a lower-friction alternative to booking a call.

Do not lead with an AI product pitch. Zediant's defensible AI claim is delivery method, not shipped AI product portfolio.

Effective opening frame: *"The roadmap grows faster than you can hire senior engineers locally."*

## Common Objections

| Objection | Response direction |
|---|---|
| "We're not ready to outsource." | Reframe as extension, not outsourcing; client owns roadmap and interviews the engineers |
| "You mention AI — what AI products have you built?" | Answer honestly: capability is AI-assisted delivery, AI product work is being built out. Internal policy mandates this honesty |
| "You're more expensive than other offshore shops." | Senior-default staffing; no junior bench; compare total cost including rework |
| "We haven't heard of Zediant." | Start with a small scoped piece; offer an existing client reference |
| "We don't want a long contract." | Start with defined initial scope; most long relationships began that way |
| "Security is a concern." | SOC 2 Type II aligned processes, DevSecOps, encryption — see the wording caution below |

## Success Stories

STAGER (Europe) — CEO Tino Pallivera describes Zediant as "an integral part of our team," having built and supporting multiple applications. Cryptocurrency Trading Application — 4.9 Google Play / 4.4 App Store, delivered by a 3-person team in 5 months. See `case_studies.md`.

## Priority Score

**HIGH.** Named the highest strategic priority in internal materials. Strongest alignment with long-term positioning, fastest decision cycles, and clearest buying signals (funding and hiring are both publicly observable).

---

# ICP 3 — Product Companies (CTO-Led)

## Industry Overview

Non-VC-backed software and technology product companies with established revenue, growing engineering teams, and a defined product roadmap. Distinguished from ICP 2 by funding model rather than by need — these companies may be bootstrapped, profitable, family-owned, or listed. Decisions are typically CTO-led rather than founder-led.

## Why They Need Zediant

These companies have proven products and real revenue but constrained engineering capacity. Without venture funding, every permanent hire is scrutinised, which makes flexible external capacity commercially attractive. They are also more likely to carry legacy estates requiring modernisation.

## Business Problems

- Specific product features consistently deprioritised for lack of capacity
- Roadmap items nobody internal is free to own
- Legacy product requiring maintenance while a new version is built
- Growth outpacing engineering without funding to hire ahead of it
- Platform migration or rebuild that internal capacity cannot absorb
- Every hire scrutinised because there is no runway cushion

## Technology Challenges

- Ageing product architecture requiring incremental modernisation
- Integration with customer systems consuming disproportionate effort
- Technical debt accumulated across years of shipping
- Difficulty hiring for the legacy stack the product runs on
- Scaling issues appearing as the customer base grows
- Security and compliance requirements from enterprise customers

## Digital Transformation Challenges

- Migrating an on-premise or single-tenant product to SaaS
- Adding API and integration capability to a closed product
- Modernising a monolith without disrupting existing customers
- Building data and analytics capability into a product that lacks it

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 20–200 |
| Revenue | Approximately USD 3M–30M (**assumption**, inferred from stage and headcount) |
| Growth stage | Established, profitable or near-profitable, growing |

## Geography

Australia, UAE (primary). United Kingdom, United States opportunistic.

## Decision Makers

| Role | Priority | Why |
|---|---|---|
| CTO | **Primary** | Owns the build decision; the defining persona for this ICP |
| Head of Engineering / VP Engineering | **Primary** | Owns capacity and delivery |
| Founder / CEO | Secondary | Involved on commercial terms |
| Head of Product | Secondary | Feels the deprioritised-feature problem |
| CIO / IT Director | Secondary | Where the product company is also an enterprise |

**Sender mapping.** manish@ for CTO and engineering leadership. pritamjit@ for product companies where the buyer is commercial rather than technical.

## Buying Signals

- Actively outsourcing specific features (the defining signal for this segment)
- Growing engineering team with open roles
- Product v2 or rebuild announced
- New integration or API programme
- Acquisition requiring product consolidation
- Entering a new market requiring localisation or compliance work
- Legacy platform end-of-life notice
- Public performance or scaling complaints

## Negative Signals

- No engineering team at all
- Product is entirely third-party or white-labelled
- Contracting business with declining headcount
- Requires deep AI/ML research
- Hardware or embedded systems as the core product
- Already has a captive offshore development centre

## Technology Stack

.NET, Java, PHP, Node.js, Python, React, Angular, jQuery, MS SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, AWS, Azure, on-premise and hybrid infrastructure, Salesforce, ERP systems.

## Budget Indicators

- Established recurring revenue
- Existing engineering payroll
- Prior contractor or partner spend
- Enterprise customer base with higher contract values
- Listed or PLC status (budget process exists, though slower)

## Urgency Indicators

- Customer-committed feature deadline
- Contract renewal contingent on a capability
- Legacy platform support ending
- Key engineer departure with concentrated knowledge
- Competitive displacement threat
- Compliance deadline

## Qualification Questions

1. What is the product, and who are your customers?
2. How large is your engineering team, and how is it structured?
3. What is on the roadmap that keeps getting deprioritised?
4. What is preventing those items from being built?
5. Are you already outsourcing any development? To whom, and how is it going?
6. What is your current architecture, and how old is it?
7. What proportion of engineering time goes to maintaining the existing product?
8. Are you planning a rebuild, migration, or major version?
9. What integrations do your customers ask for that you cannot deliver?
10. How difficult is it to hire for your stack locally?
11. What is your release cadence, and what constrains it?
12. Do you have automated test coverage?
13. What security or compliance requirements do your customers impose?
14. Who owns the decision on an engineering partner?
15. What is your budget approval process and timeline?
16. Have you worked with an external partner before? What happened?
17. What internal resource would be available to support onboarding?
18. What does success look like in the first three months?
19. Is this a one-off need or an ongoing capacity gap?
20. What happens to the business if this work does not get done this year?

## Recommended Services

| Priority | Service |
|---|---|
| 1 | Dedicated Engineering Pods |
| 2 | Integration & Middleware Engineering |
| 3 | Legacy Modernisation |
| 4 | Platform Engineering & Cloud DevOps |
| 5 | AI-Enabled Product Engineering |
| 6 | Maintenance & Managed Services |
| 7 | Data Engineering & Analytics |

## Recommended Campaign

**C4 — Middleware & API Integration (ZCoupler)** (primary, integration-led) or **C5 — Enterprise Custom Development & Modernization** (where the need is legacy/enterprise work rather than integration). Sender: manish@ or pritamjit@ — see the sender-persona open item in `campaigns.md`. See `campaigns.md`.

## Recommended Email Angle

Lead with the specific deprioritised roadmap item. This buyer knows exactly which feature has been pushed back four quarters. Emphasise that a pod can own a defined slice of the roadmap end-to-end, without disturbing the internal team's priorities. For bootstrapped companies, cost-efficiency framing works better than speed framing — every hire is scrutinised because there is no funding cushion.

Effective opening frame: *"If there's a roadmap item that keeps slipping because nobody's free to own it, that's the conversation worth having."*

## Common Objections

| Objection | Response direction |
|---|---|
| "Our product is too complex for an outside team." | Start with a defined peripheral module to prove capability before core work |
| "Knowledge transfer would take too long." | Pod includes a tech lead; AI-generated documentation accelerates onboarding |
| "We can't afford it without funding." | Compare against fully-loaded permanent cost; flexible scale-down protects downside |
| "We tried outsourcing and it failed." | Ask specifically what failed; differentiate on senior-only staffing and pod structure |
| "Our stack is unusual." | Verify against documented capability honestly; disqualify if outside it |

## Success Stories

Zwick Roell (USA) — Digital Officer Rhonda Viera cites "high quality and smooth delivery" and confirmed intent to engage again. Lubricant Recommendation Application — adopted by 23+ lubricant companies across APAC. See `case_studies.md`.

## Priority Score

**HIGH.** Strong fit for the pod model, CTO-led decisions are technically informed and fast, and this segment carries the most legacy modernisation and integration opportunity — Zediant's most differentiated capabilities.

---

# VERTICAL ICPs

These six industries carry documented Zediant delivery evidence. A vertical ICP does not replace a segment ICP — it supplements it with industry-specific problems, signals, and proof.

**Qualification note.** The 20 segment qualification questions above apply to every vertical. The questions listed under each vertical are *additional* industry-specific probes, not replacements.

---

# ICP 4 — Automotive & Dealer Networks

## Industry Overview

Vehicle OEMs, dealer groups, parts distributors, dealer management system (DMS) vendors, and automotive data and SaaS providers. This is Zediant's deepest and most defensible vertical, with production systems deployed across APAC, UK, and USA dealer networks.

## Why They Need Zediant

Dealer networks run fragmented technology estates. Each dealership may use a different DMS, none of which exchange data. Zediant has built the middleware layer that solves exactly this problem, repeatedly, and holds domain knowledge of DMS data models that is genuinely rare.

## Business Problems

- No consolidated view of customer and sales data across a dealer network
- Manual, paper-based processes for specifications and recommendations
- Inconsistent data quality across dealers
- Sales and service representative activity untracked
- Parts and inventory data fragmented across locations
- Poor customer experience from disconnected systems

## Technology Challenges

- Multiple incompatible DMS platforms across the network
- Legacy dealer systems with no APIs
- No standardisation, enrichment, or validation of data in transit
- Field staff without mobile access to systems
- Supplier specification databases changing frequently and managed manually

## Digital Transformation Challenges

- Consolidating dealer data without replacing dealer systems
- Extending OEM systems to a franchised network Zediant's client does not control
- Building analytics on data that first requires unification
- Modernising decades-old dealer platforms incrementally

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 50–1,000+ |
| Revenue | Mid-market to enterprise |
| Growth stage | Established; dealer networks and OEM suppliers |

## Geography

Australia, UAE (primary — documented delivery in both). APAC broadly, UK, USA (documented middleware adoption).

## Decision Makers

CIO, IT Director, CTO, Head of Digital, Operations Head, Dealer Network Manager, Head of Aftersales.

## Buying Signals

- Dealer network expansion or acquisition
- DMS migration or vendor change
- OEM mandate for data standardisation
- New model or product line launch requiring system updates
- Aftersales or parts programme launch
- Public complaints about dealer data accuracy

## Negative Signals

- Single independent dealership (too small)
- Pure vehicle retail with no technology function
- Requires embedded or in-vehicle software (outside capability)
- DMS vendor unwilling to grant integration access

## Technology Stack

DMS platforms, .NET, C#, MS SQL Server, Java, Spring, Hibernate, JSP, JMS, ActiveMQ, Objective-C, Swift, AngularJS, jQuery, LINQ, Salesforce, REST/JAX-RS.

## Budget Indicators

Enterprise or OEM parent, multi-site dealer group, existing DMS licence spend, dedicated IT function, prior integration project spend.

## Urgency Indicators

DMS end-of-life notice, OEM compliance deadline, acquisition requiring consolidation, dealer conference or model-year deadline.

## Additional Qualification Questions

1. How many dealers or sites are in the network?
2. Which DMS platforms are in use, and how many different ones?
3. Do you control those systems or do the dealers?
4. How does data move between dealers and head office today?
5. What manual effort goes into consolidating that data?
6. Do you have API access to the DMS platforms?
7. What reporting can you not produce today?
8. Do field staff have mobile access to these systems?
9. Has an integration project been attempted before? What blocked it?
10. What is the OEM relationship, and does it impose requirements?

## Recommended Services

Integration & Middleware Engineering (primary), Enterprise Custom Development, Mobile Application Development, Legacy Modernisation, Data Engineering & Analytics, Maintenance & Managed Services.

## Recommended Campaign

**C4 — Middleware & API Integration (ZCoupler)**, plus industry-specific automotive outreach. See `campaigns.md`.

## Recommended Email Angle

Lead with dealer data fragmentation and reference the DMS middleware experience directly. This is the one vertical where Zediant can open with proof rather than proposition. Naming the problem precisely — "every dealer runs a different DMS and none of them talk to each other" — demonstrates domain knowledge immediately.

## Common Objections

Integration access from third-party DMS vendors; concern about disrupting live dealer operations; preference for the DMS vendor's own integration offering; data ownership questions across the franchise network.

## Success Stories

Wholesale Parts CRM — 50+ dealers across APAC, 5,700 customers, 12-person team over 18 months. Middleware Integration for Multiple Large DMS — became a repeatable solution adopted by leading automotive parts dealers across APAC, UK, and USA. Lubricant Recommendation Application — 23+ lubricant companies in APAC. See `case_studies.md`.

## Priority Score

**HIGH.** Deepest documented evidence, most differentiated capability, proven repeatability across three regions.

---

# ICP 5 — Financial Services & Fintech

## Industry Overview

Payment platforms, trading and investment applications, lending platforms, RegTech and compliance software, and financial data providers.

## Why They Need Zediant

Financial applications carry disproportionate security, transaction-integrity, and audit requirements. Zediant's security posture and documented delivery of an independently security-audited trading application address the exact concerns that make fintech buyers cautious about offshore partners.

## Business Problems

- Transaction integrity and zero-data-loss requirements
- Regulatory and compliance obligations with engineering implications
- Customer trust dependent on visible security
- Multi-provider and multi-exchange integration complexity
- Legacy core systems constraining product velocity
- Compliance reporting spanning disconnected systems

## Technology Challenges

- Low-latency, high-volume transactional architecture
- Multi-factor authentication and end-to-end encryption
- Third-party security audit readiness
- Real-time processing and reconciliation
- Integration across payment providers, exchanges, and market data
- Data residency and sovereignty requirements

## Digital Transformation Challenges

- Migrating core financial systems without transaction loss
- Adding mobile and self-service to legacy platforms
- Meeting evolving regulation with engineering change
- Building compliance evidence into the SDLC

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 20–500 |
| Revenue | USD 2M–50M (**assumption**) |
| Growth stage | Funded startup through established provider |

## Geography

Australia, UAE (primary). United Kingdom opportunistic.

## Decision Makers

CTO, Head of Engineering, CIO, Head of Compliance, Founder/CEO, Head of Product, CISO.

## Buying Signals

- Funding round
- New licence or regulatory approval obtained
- New market entry
- Security incident or audit finding
- Compliance deadline (regulatory change)
- Mobile app launch or rebuild announced
- Hiring for security or platform engineering

## Negative Signals

- Requires cryptocurrency protocol or blockchain core development
- Needs a regulated entity licence Zediant cannot provide
- Requires on-shore-only data residency with no offshore processing permitted
- Requires deep quantitative or algorithmic trading model development

## Technology Stack

.NET, C#, Java Spring Boot, Node.js, Python, Ionic, Angular, React, MS SQL Server, PostgreSQL, Oracle, Redis, AWS, Azure, OAuth2, JWT, AES-256, TLS/SSL, payment gateway APIs, market data APIs.

## Budget Indicators

Funded or revenue-generating, regulated entity status, existing security and compliance spend, enterprise or institutional customers.

## Urgency Indicators

Regulatory deadline, audit finding, security incident, licence condition, competitor launch, investor-committed milestone.

## Additional Qualification Questions

1. What regulatory regime applies to you, and who is your regulator?
2. What data residency requirements apply?
3. Do you require an independent security audit of delivered code?
4. What is your transaction volume and peak load?
5. What payment providers or exchanges do you integrate with?
6. What are your latency requirements?
7. What is your current authentication and encryption approach?
8. Has your platform been penetration tested? What were the findings?
9. What compliance evidence do you need from a development partner?
10. What is your incident response and change control process?

## Recommended Services

AI-Enabled Product Engineering, Platform Engineering & Cloud DevOps, Mobile Application Development, QA & Test Automation (security testing), Enterprise Custom Development, Integration & Middleware Engineering.

## Recommended Campaign

**C1 — AI-Enabled Product Engineering** (primary) or **C5 — Enterprise Custom Development & Modernization** (where the need is enterprise-grade/security-heavy custom development). See `campaigns.md`.

## Recommended Email Angle

Lead with security and transaction integrity, not speed. Reference the independently security-audited trading application. This buyer's first question is "can I trust you with this," and answering it before it is asked shortens the conversation considerably.

**Critical caution.** Fintech buyers will interrogate SOC 2 status directly and are the most likely segment to request the attestation report. Use "SOC 2 Type II aligned" and escalate any request for the report. Never repeat website phrasing such as "externally audited."

## Common Objections

Security and data residency; regulatory acceptance of an offshore partner; requirement for named security certifications; concern about audit trail and change control; preference for a locally-regulated supplier.

## Success Stories

Cryptocurrency Trading Application — multi-factor authentication, end-to-end encryption, independent third-party security audit approval, 4.9 Google Play / 4.4 App Store. See `case_studies.md`.

## Priority Score

**MEDIUM-HIGH.** Strong documented proof and high deal values, but the highest scrutiny on the unresolved SOC 2 wording issue. Proceed with care until that is settled.

---

# ICP 6 — Manufacturing & Industrial

## Industry Overview

Industrial equipment manufacturers, material handling, industrial technology, and multi-region manufacturing businesses with distributed sales and service operations.

## Why They Need Zediant

Manufacturers typically run multi-country digital estates with inconsistent branding and disconnected CRM, alongside ageing internal systems. Zediant has documented delivery of an enterprise multi-site CMS with Salesforce synchronisation for exactly this profile.

## Business Problems

- Country-specific websites inconsistent with global brand
- Leads captured on the web but lost before reaching sales
- Marketing dependent on developers for routine content changes
- No personalisation by geography or customer behaviour
- Product and specification data managed manually
- Disconnected ERP, CRM, and web systems

## Technology Challenges

- Enterprise CMS requiring multi-language and multi-region configuration
- CRM synchronisation without manual intervention
- Legacy internal systems with no integration surface
- Product information management across catalogues
- Ageing on-premise infrastructure

## Digital Transformation Challenges

- Consolidating country-level digital autonomy under global governance
- Adding e-commerce to a traditionally offline sales model
- Modernising internal systems without disrupting production
- Building analytics across manufacturing, sales, and service

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 100–5,000 |
| Revenue | Mid-market to enterprise |
| Growth stage | Established, multi-region |

## Geography

Australia, UAE (primary). Global manufacturers with APAC operations.

## Decision Makers

CIO, IT Director, Head of Digital, Head of Marketing, Digital Transformation Manager, Head of Aftersales.

## Buying Signals

- Rebrand or global website consolidation programme
- Expansion into new markets
- CMS or ERP end-of-life notice
- E-commerce initiative announced
- Marketing technology consolidation
- Acquisition requiring digital estate consolidation

## Negative Signals

- Requires embedded, PLC, SCADA, or industrial control system software
- Requires IoT device firmware
- Procurement demands a named-brand global systems integrator
- No digital or IT function

## Technology Stack

Sitecore, Optimizely, WordPress, Drupal, .NET, C#, MS SQL Server, Java, Salesforce, SAP-class ERP, AWS, Azure, jQuery, HTML5, CSS.

## Budget Indicators

Multi-region operations, existing enterprise CMS or ERP licence spend, dedicated marketing and IT functions, established brand.

## Urgency Indicators

Rebrand deadline, market entry date, platform end-of-life, licence renewal, trade show or product launch.

## Additional Qualification Questions

1. How many country or brand sites are in scope?
2. What languages and regions must be supported?
3. What CMS and CRM are you on today?
4. How are web leads reaching sales currently?
5. How long does a routine content change take?
6. Who owns content in each region — central or local?
7. Do you need personalisation, and based on what data?
8. What ERP or product data must the site connect to?
9. Are e-commerce plans on the roadmap?
10. Have licence costs been budgeted separately from implementation?

## Recommended Services

E-commerce & CMS Development (primary), Integration & Middleware Engineering, Enterprise Custom Development, Web Application Development, Data Engineering & Analytics, Maintenance & Managed Services.

## Recommended Campaign

**C2 — Engineering Pods & Staff Augmentation** (e-commerce/CMS delivered within a pod, primary) and **C4 — Middleware & API Integration (ZCoupler)** (secondary). Enterprise manufacturing rarely closes from cold outbound. See `campaigns.md`.

## Recommended Email Angle

Lead with multi-site governance and the lead-loss problem between web and CRM. Reference the documented 30% traffic increase and in-house content management outcome. Marketing and digital leaders in this vertical respond to control and measurability, not to engineering capability.

## Common Objections

Preference for a local digital agency; licence cost concerns; internal marketing team resistance; requirement for on-site workshops; brand governance concerns about an offshore partner.

## Success Stories

Sitecore CMS Multisite Platform — material handling equipment manufacturer, Salesforce sync, personalisation, company-stated 30% traffic increase, 5-person team over 6 months. See `case_studies.md`.

## Priority Score

**MEDIUM.** Good documented proof and healthy deal values, but longer sales cycles and a referral-led rather than outbound-led motion.

---

# ICP 7 — Logistics & Supply Chain

## Industry Overview

Freight, transport, warehousing, distribution, and supply chain technology providers operating across multi-party networks.

## Why They Need Zediant

Logistics runs on data exchange between parties who use different systems. This is structurally the same problem as automotive dealer networks, where Zediant's middleware capability is strongest.

## Business Problems

- No visibility across a multi-party logistics chain
- Manual data exchange between carriers, warehouses, and customers
- Order and inventory data inconsistent across systems
- Customers demanding real-time tracking the business cannot provide
- Manual reconciliation between operational and financial systems

## Technology Challenges

- Integration across carrier, WMS, TMS, and ERP systems
- Real-time event processing and tracking
- EDI and legacy message format handling
- Mobile access for drivers and warehouse staff
- Scaling under seasonal peak load

## Digital Transformation Challenges

- Replacing manual and paper processes at point of work
- Building customer-facing visibility portals
- Modernising legacy operational systems incrementally
- Adding analytics across a fragmented data estate

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 50–1,000 |
| Revenue | Mid-market |
| Growth stage | Established or scaling |

## Geography

Australia, UAE (primary — UAE is a significant logistics hub).

## Decision Makers

CIO, IT Manager, COO, Operations Head, Head of Supply Chain, CTO.

## Buying Signals

- Network or route expansion
- New WMS or TMS implementation
- Customer contract requiring visibility or tracking
- Acquisition requiring system consolidation
- Peak-season performance failure
- Regulatory or customs system change

## Negative Signals

- Requires physical automation, robotics, or warehouse hardware control
- Requires telematics device firmware
- Single-vehicle or micro operator
- No IT function

## Technology Stack

Java, Spring, .NET, Node.js, MS SQL Server, Oracle, PostgreSQL, MongoDB, JMS, ActiveMQ, REST APIs, EDI, mobile (Flutter, React Native), AWS, Azure.

## Budget Indicators

Multi-site operations, existing WMS/TMS spend, enterprise customer contracts, dedicated IT function.

## Urgency Indicators

Customer contract requirement, peak season approaching, system end-of-life, acquisition integration, regulatory change.

## Additional Qualification Questions

1. How many parties exchange data in your chain — carriers, warehouses, customers?
2. What systems do each of them use?
3. How is data exchanged today — API, EDI, file, or manual?
4. What visibility do your customers ask for that you cannot provide?
5. What manual reconciliation happens weekly?
6. What is your peak versus average volume?
7. Do drivers or warehouse staff have mobile system access?
8. What happened during your last peak season?
9. What is on the roadmap that will add more systems?
10. Do you control the systems being integrated, or do partners?

## Recommended Services

Integration & Middleware Engineering (primary), Enterprise Custom Development, Web Application Development, Mobile Application Development, Data Engineering & Analytics, Platform Engineering & Cloud DevOps.

## Recommended Campaign

**C4 — Middleware & API Integration (ZCoupler)**. See `campaigns.md`.

## Recommended Email Angle

Lead with multi-party visibility and manual reconciliation effort. Quantify: ask how many hours a week go into moving data between systems. Logistics buyers are operationally minded and respond to eliminated effort more than to technology.

## Common Objections

Partner systems outside their control; peak-season risk tolerance; preference for a logistics-specialist vendor; integration access from carriers.

## Success Stories

Middleware Integration for Multiple Large DMS demonstrates the directly analogous multi-party integration pattern. Note honestly that Zediant's logistics-specific case studies are thinner than its automotive evidence. See `case_studies.md`.

## Priority Score

**MEDIUM.** Strong structural fit for the differentiated middleware capability, but weaker direct vertical proof than automotive.

---

# ICP 8 — Retail & E-commerce

## Industry Overview

Multi-store retailers, B2B and B2C e-commerce operators, and franchise retail networks.

## Why They Need Zediant

Retail estates accumulate systems — POS, e-commerce, inventory, ERP, loyalty — that rarely integrate cleanly. Zediant covers both the e-commerce platform layer and the integration layer beneath it.

## Business Problems

- Inventory inconsistent across stores and channels
- Order data fragmented between online and physical
- Platform failing under peak trading load
- Marketing dependent on developers for content changes
- No single customer view across channels
- Enterprise platform licence cost disproportionate to features used

## Technology Challenges

- POS and e-commerce integration
- Peak traffic and concurrency handling
- Catalogue and product information management at scale
- Platform migration between e-commerce systems
- Multi-region and multi-currency configuration

## Digital Transformation Challenges

- Unifying online and physical retail data
- Replatforming without losing SEO or trading continuity
- Adding B2B ordering to a B2C platform
- Building customer analytics across channels

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 50–1,000 |
| Revenue | Mid-market |
| Growth stage | Established, multi-channel |

## Geography

Australia, UAE (primary).

## Decision Makers

Head of Digital, E-commerce Director, CIO, IT Manager, Head of Marketing, COO.

## Buying Signals

- Replatforming announced or licence renewal approaching
- Peak trading failure (publicly visible)
- Store network expansion
- B2B channel launch
- International market entry
- Loyalty or CRM programme launch

## Negative Signals

- Single-store independent retailer
- Pure marketplace seller with no owned platform
- Requires in-store hardware or POS terminal development
- Commodity brochure-site budget

## Technology Stack

Magento, BigCommerce, Shopify, WooCommerce, Sitecore Commerce, WordPress, .NET, PHP, Laravel, MS SQL Server, MySQL, POS systems, ERP, AWS, Azure, CDN.

## Budget Indicators

Multi-store or multi-channel operations, existing platform licence spend, dedicated digital or e-commerce team, established trading volume.

## Urgency Indicators

Peak trading season approaching, licence renewal, platform end-of-life, competitor launch, post-incident remediation.

## Additional Qualification Questions

1. What platform are you on, and why are you considering change?
2. How many stores, channels, and regions?
3. How many SKUs are in the catalogue?
4. How do POS and e-commerce share inventory data today?
5. What are your peak traffic volumes, and what happened last peak?
6. Who manages content, and how long does a change take?
7. What is your current conversion rate and where does it drop?
8. What ERP or inventory system must this connect to?
9. Have licence costs been budgeted separately?
10. What are your SEO rankings and what is the migration risk tolerance?

## Recommended Services

E-commerce & CMS Development (primary), Integration & Middleware Engineering, Platform Engineering & Cloud DevOps, Web Application Development, Data Engineering & Analytics, Maintenance & Managed Services.

## Recommended Campaign

**C2 — Engineering Pods & Staff Augmentation** (via agencies serving retail, primary) and **C4 — Middleware & API Integration (ZCoupler)** (secondary). See `campaigns.md`.

## Recommended Email Angle

Lead with peak-load risk or channel data fragmentation, depending on the observed signal. Retail buyers are deadline-driven around trading seasons; anchor urgency to their calendar rather than to a generic value proposition.

## Common Objections

Preference for a specialist e-commerce agency; platform vendor's own partner network; peak-season change freeze; SEO risk during migration.

## Success Stories

Sitecore multisite implementation with e-commerce roadmap consideration. Documented expert-level BigCommerce and Sitecore capability in the internal skill matrix. See `case_studies.md`.

## Priority Score

**MEDIUM.** Genuine capability with strong platform coverage, but a competitive market with many specialist e-commerce agencies. Best approached through the agency channel rather than direct.

---

# ICP 9 — Energy, Oil & Gas

## Industry Overview

Energy producers, oil and gas operators, and energy services businesses, particularly in the UAE where Zediant has documented delivery.

## Why They Need Zediant

Large energy organisations run many enterprise systems with fragmented, manual reporting. Zediant has delivered a consolidated executive KPI dashboard in exactly this environment.

## Business Problems

- KPI reporting fragmented and manual across enterprise systems
- Leadership decisions delayed by slow reporting cycles
- No single source of truth for management reporting
- Data access not controlled by role
- Manual reconciliation between operational and financial systems

## Technology Challenges

- Integrating multiple established enterprise systems
- Role-based access control over sensitive operational data
- Scalable reporting architecture
- Data governance and residency requirements
- Legacy systems with limited integration surface

## Digital Transformation Challenges

- Consolidating reporting across business units
- Building analytics foundations on legacy data
- Modernising internal systems in a change-averse, safety-critical environment
- Meeting regional data sovereignty requirements

## Ideal Company Size

| Attribute | Range |
|---|---|
| Employees | 200–10,000+ |
| Revenue | Enterprise |
| Growth stage | Established |

## Geography

UAE (primary — documented delivery). Australia opportunistic.

## Decision Makers

CIO, IT Director, Head of Digital Transformation, COO, CFO, Head of Data.

## Buying Signals

- Digital transformation programme announced
- New leadership demanding better reporting
- ERP or core system upgrade
- Regulatory reporting requirement
- Business unit consolidation
- Data platform or analytics initiative

## Negative Signals

- Requires SCADA, industrial control, or operational technology systems
- Safety-critical embedded systems
- Procurement demands a named-brand global consultancy
- Requires on-site presence as a hard requirement

## Technology Stack

Python, Oracle, ReactJS, REST APIs, MS SQL Server, SAP-class ERP, analytics and visualisation components, Azure, AWS.

## Budget Indicators

Enterprise scale, dedicated IT and data functions, existing enterprise software spend, documented transformation programme with budget.

## Urgency Indicators

Board reporting requirement, regulatory deadline, leadership change, fiscal year planning cycle, audit finding.

## Additional Qualification Questions

1. What reporting do you produce today, and how many people-hours does it consume?
2. How many source systems feed executive reporting?
3. Do business units agree on metric definitions?
4. What role-based access requirements apply to the data?
5. What data residency or sovereignty rules apply?
6. Who is the executive sponsor for this?
7. What is the procurement process and expected timeline?
8. Is on-site presence a requirement at any stage?
9. What compliance frameworks govern this system?
10. What analytics capability is planned beyond initial reporting?

## Recommended Services

Data Engineering & Analytics (primary), Enterprise Custom Development, Integration & Middleware Engineering, Platform Engineering & Cloud DevOps, Advisory & Consulting.

## Recommended Campaign

**C4 — Middleware & API Integration (ZCoupler)** (primary, given the Data Engineering & Analytics driver) — but see `case_studies.md` CS-05 for the unresolved oil-and-gas/consultancy discrepancy affecting this ICP's sole proof point. This vertical does not respond to cold outbound. See `campaigns.md`.

## Recommended Email Angle

Only appropriate on a warm introduction. Lead with executive reporting latency and manual effort. Reference the documented UAE dashboard engagement. Emphasise role-based access and governance, which matter more here than delivery speed.

## Common Objections

Preference for a global systems integrator; on-site presence requirements; data sovereignty; vendor scale and financial stability questions; extended procurement processes.

## Success Stories

Enterprise Performance Monitoring Dashboard, UAE — role-based dashboards, unified KPI aggregation, 6-person team over 6 months. See `case_studies.md`.

## Priority Score

**MEDIUM-LOW for outbound; MEDIUM-HIGH for referral.** Strong proof and high deal values, but procurement cycles, scale expectations, and on-site preferences make cold acquisition impractical at Zediant's current size.

---

# INDUSTRIES EVALUATED AND EXCLUDED

The following industries appear in generic ICP frameworks but are **not** Zediant ICPs. An agent should not build outreach around them without explicit human direction.

| Industry | Status | Reasoning |
|---|---|---|
| **Healthcare** | Listed, unproven | Named as a middleware focus industry in the company profile, but no case study, reference, or named client exists. Regulatory burden (HIPAA-equivalent, clinical safety) is significant and unaddressed in any Zediant material. **Treat as opportunistic only.** |
| **Education** | Not an ICP | No evidence of delivery, capability, or targeting in any source. Note that a documented case study client, The Alpha School System (TASS), is an education *software vendor* — that is ICP 3 (product company), not education as a vertical. |
| **Construction** | Not an ICP | No evidence in any source. |
| **Professional Services** | Not an ICP as a buyer | Consultancies appear in Zediant materials as *partner* targets (referral channel), not as end clients. Targeting them as buyers conflicts with the partner strategy. |
| **Government** | Actively deprioritised | Internal strategy explicitly identifies uncompensated government tender documentation as a drain on billable capacity, directing a move to retainer or Teaming Agreement models. Long procurement, security clearance requirements, and on-shore mandates compound the problem. **Do not pursue without a Teaming Agreement.** |
| **Media & Entertainment** | Listed, unproven | Named as a focus industry in the company profile with no supporting case study. Opportunistic only. |
| **Real Estate** | Listed, unproven | Named as a focus industry with no supporting case study. Note that documented prospects (Properti, Hutly) are proptech *software companies* — ICP 2, not real estate as a vertical. |

**Rule for agents.** If a prospect falls in an excluded industry but matches a segment ICP strongly (they are a funded SaaS company that happens to sell into healthcare), classify by **segment**, not by their customers' industry. The segment ICP governs.

---

# DECISION MAKER MATRIX

| Role | Goals | Challenges | KPIs | Buying Motivation | Preferred Messaging | Sender |
|---|---|---|---|---|---|---|
| **Founder / CEO (SaaS)** | Ship product, extend runway, raise next round | Hiring too early, burning runway, investor pressure | Revenue growth, burn rate, runway months, roadmap delivery | Speed to market without permanent headcount risk | Extend the team without full-time hiring overhead; flexible scale-down | rajeev@ |
| **CTO** | Ship the roadmap without compromising architecture | Cannot hire senior engineers; technical debt; security demands | Velocity, uptime, defect rate, security posture | Senior talent access and architectural integrity | Senior-only staffing, you interview every engineer, security posture, architecture validation | manish@ |
| **VP Engineering / Head of Engineering** | Predictable delivery, healthy team | Capacity constraints, context switching, attrition | Sprint velocity, cycle time, escaped defects | Capacity that integrates without management overhead | Works inside your sprints, standards, and review process — not around them | manish@ |
| **Engineering Manager** | Team throughput and morale | Backlog pressure, unplanned work | Story points, ticket throughput, on-time delivery | Relief from backlog without onboarding burden | Fast onboarding, fits existing process, no management overhead added | manish@ |
| **COO (Agency)** | Deliver client work profitably | Capacity variability, bench cost, margin compression | Utilisation, project margin, on-time delivery, client satisfaction | Capacity that flexes without carrying cost | White-label, scale down with 30 days notice, predictable monthly cost | pritamjit@ |
| **Managing Director (Agency)** | Grow the agency, protect margin | Turning down work, subcontractor quality | Revenue, margin, client retention, pipeline conversion | Win larger work without permanent hires | Bid for work you'd otherwise decline; margin protection | pritamjit@ |
| **CIO** | Stable, governed, compliant estate | Legacy systems, vendor risk, integration debt | Uptime, incident volume, project delivery, audit findings | Reduced risk and governed delivery | Governance, security documentation, transparent reporting, executive accountability | rajeev@ |
| **IT Director / IT Manager** | Keep systems running, deliver projects | Under-resourced, legacy support burden, vendor sprawl | Ticket volume, SLA attainment, project delivery | Support burden relief and integration capability | Managed services, integration, continuity independent of individuals | pritamjit@ |
| **Head of Product / Product Manager** | Ship roadmap, hit customer commitments | Engineering capacity, competing priorities | Feature throughput, adoption, NPS, churn | Roadmap items that finally get built | A pod that owns a defined slice of the roadmap end-to-end | manish@ |
| **Operations Head** | Process efficiency, cost control | Manual processes, disconnected systems | Cost per transaction, cycle time, error rate | Eliminated manual effort | Quantified hours removed from manual work | pritamjit@ |
| **Digital Transformation Manager** | Modernise the estate | Legacy resistance, integration complexity, stakeholder alignment | Programme milestones, systems retired, adoption | Incremental modernisation without disruption | Phased migration, no big-bang cutover, legacy-and-modern capability in one team | rajeev@ |
| **Head of Digital / Head of Marketing** | Campaign speed, brand consistency | Developer dependency, fragmented sites | Traffic, conversion, lead volume, publishing cycle time | Control without developer dependency | Manage content in-house; consistent global brand; leads sync automatically | pritamjit@ |
| **CFO** | Decision quality, cost control | Slow reporting, disputed numbers | Reporting cycle time, forecast accuracy | Faster, more accurate management reporting | Single source of truth; eliminated manual reporting hours | rajeev@ |
| **CISO / Head of Compliance** | Reduce risk, satisfy auditors | Vendor risk, evidence gathering | Audit findings, incident count, vendor assessments | Verifiable secure delivery practices | DevSecOps, SAST/DAST, encryption, RBAC — **use "SOC 2 aligned"; escalate report requests** | manish@ |
| **QA Lead / SDET** | Release confidence | Manual regression, flaky tests, environments | Coverage, escaped defects, regression cycle time | Automation capacity and expertise | Test generation from user stories; QA engineer included in the pod | manish@ |
| **Enterprise Architect** | Coherent target architecture | Legacy constraints, integration debt | Architecture compliance, technical debt reduction | Independent validation and execution capability | Architecture review with AI-assisted validation; delivery capability behind the advice | manish@ |

---

# COMPANY SIZE MATRIX

| Size band | Employees | Characteristics | Recommended Services | Deal Shape | Priority |
|---|---|---|---|---|---|
| **Startup** | 1–10 | Pre-seed to seed, founder-led, minimal process | Advisory, small Fixed Cost, single Staff Augmentation | Under USD 15,000 | **Low** — usually below viable deal size unless funded |
| **SMB** | 10–50 | Seed to Series A SaaS, small agencies, growing product companies | Dedicated Pods (Foundation), Staff Augmentation, Web, Mobile, QA, Advisory | USD 15,000–50,000 | **High** — core ICP band |
| **Mid Market** | 50–200 | Series A/B SaaS, established agencies, product companies | Dedicated Pods (Growth), AI-Enabled Product Engineering, Platform Engineering, Integration, E-commerce & CMS, Managed Services | USD 50,000–150,000 | **Highest** — best fit for capacity, deal size, and decision speed |
| **Enterprise** | 200+ | PLCs, OEMs, manufacturers, energy | Enterprise Custom Development, Integration & Middleware, Legacy Modernisation, Data Engineering, Advisory | USD 150,000+ | **Medium** — high value but capacity-constrained and procurement-heavy |

**Capacity rule applying to all bands.** Zediant can onboard 5–7 additional developers within three months against 25–35 total headcount. Any engagement requiring a larger or faster ramp must be phased or declined, regardless of size band.

---

# COUNTRY MATRIX

| Country | Status | Preferred Services | Buying Behaviour | Communication Style | Practical Notes |
|---|---|---|---|---|---|
| **Australia** | Primary | Dedicated Pods, AI-Enabled Product Engineering, Platform Engineering, Web, Mobile, E-commerce & CMS | Comfortable with monthly retainers and dedicated-pod pricing; fixed-price more common for smaller well-scoped work. Decisions relatively fast at founder and COO level | Direct, low formality. Over-selling and excessive formality read as *less* credible. Be specific and straightforward | India is 4.5 hrs behind AEST (Sydney/Melbourne/Brisbane), 2.5 hrs behind AWST (Perth). Perth offers materially better overlap and is under-exploited. Schedule outreach to land in the recipient's morning |
| **UAE** | Primary | Dedicated Pods, Integration & Middleware, Enterprise Custom Development, Data Engineering, Staff Augmentation | Relationship-building matters before the deal moves. A short introductory call is better received than jumping to a full discovery pitch. Comfortable with dedicated-team and staff-augmentation models | Relationship-first, more formal than Australia. Patience is required; rushing the commercial conversation damages trust | India is 1.5 hrs ahead — near-full working-day overlap, a genuine and quantifiable advantage. **Working week runs Sunday–Thursday** for many organisations; adjust cadence and meeting scheduling accordingly. Enterprise and government-adjacent buyers expect security documentation early |
| **United Kingdom** | Secondary / opportunistic | Dedicated Pods, SaaS platform work, Legacy Modernisation | Not systematically pursued. Zediant's site references SaaS engineering for the UK market and UK GDPR alignment | Direct, moderately formal | 5.5 hrs behind IST (BST) — reduced overlap. Pursue only on a specific opportunity or warm introduction |
| **United States** | Secondary / opportunistic | Dedicated Pods, AI-Enabled Product Engineering | Not systematically pursued. Documented clients exist (Zwick Roell, Iron Software partnership) | Direct, fast-paced, outcome-focused | 9.5–13 hrs behind IST — minimal overlap. Do not build campaigns; pursue warm introductions only |
| **South Africa** | Secondary / opportunistic | Dedicated Pods, Staff Augmentation | Named as opportunistic in internal strategy. No documented delivery | Direct | 3.5 hrs behind IST — good overlap. No case studies to support entry |
| **India** | Delivery base, not a market | — | — | — | All delivery originates here. Rate card references India-based engagements at ₹1,200/hour blended, but India is not a target market |

**Geographic discipline rule.** Internal strategy explicitly recommends picking one geography and building 3–5 deep case studies around it. An agent should resist diluting into secondary markets while Australia and UAE outbound remains unproven at full capacity.

---

# LEAD QUALIFICATION RULES

## Ideal Prospect — score 80–100, act immediately

All of the following:

- Matches a segment ICP exactly on size, stage, and category
- Located in Australia or UAE
- Founder, CEO, CTO, or COO reached directly
- Active buying signal within the last 6 months (funding, hiring, expansion, incident, acquisition)
- Technology stack within Zediant's documented capability
- Deal size viable at USD 10,000+ with pod expansion potential
- New logo (reduces concentration) rather than existing-client expansion

**Action.** Prioritise immediately. Loop in the Founder early. Enrich, route to the mapped campaign, and flag for same-day follow-up on any reply.

## Acceptable Prospect — score 50–79, standard sequence

Most of the following, with no disqualifiers:

- Matches a segment ICP on most dimensions
- Australia or UAE, or a strong secondary-market opportunity
- Correct persona reached or reachable within one step
- Buying signal present but older, weaker, or inferred
- Technology stack largely within capability
- Deal size plausible but unconfirmed

**Action.** Standard sequence, normal priority. Enrich and route to the mapped campaign. No Founder involvement until a reply.

## Borderline Prospect — score 30–49, nurture only

Any of the following:

- Segment fit partial (right size, wrong stage; or right stage, wrong category)
- Secondary geography with no warm introduction
- Persona reached is below decision level with no clear path upward
- No observable buying signal
- Stack partially outside documented capability
- Deal size likely below USD 10,000
- Company contracting (headcount down materially) with unclear compensating pipeline

**Action.** Low-touch nurture. **Do not spend Apollo enrichment credits.** Revisit if a buying signal appears. Bang Digital — an agency with ~29% headcount decline over 12 months — is a documented example of a borderline prospect that entered a campaign with an explicit "qualify hard on first contact" flag.

## Reject Prospect — score below 30, or any hard disqualifier

**Action.** Do not enrich, do not sequence, mark as rejected in Zoho with a reason. Rejection reasons feed messaging and ICP refinement over time.

---

# EXCLUSION RULES

## Hard disqualifiers — never target

| Category | Rule |
|---|---|
| **Capacity** | Requires 50+ engineers ramped immediately |
| **Capability — AI** | Core need is AI/ML research, model training, or foundation model development |
| **Capability — vision/speech** | Requires computer vision or speech AI |
| **Capability — low-code** | Requires low-code or no-code platform development |
| **Capability — hardware** | Requires embedded systems, firmware, SCADA, industrial control, robotics control, or telematics device software |
| **Delivery model** | Requires full on-site presence as a hard, non-negotiable requirement |
| **Commercial** | Expects free POC or unpaid tender documentation — explicitly prohibited by internal strategy |
| **Commercial** | Primary decision criterion is lowest hourly rate; competing against commodity offshore or freelance pricing |
| **Commercial** | Cannot support a minimum USD 25–30/hour blended rate |
| **Certification** | Requires certifications Zediant cannot evidence (ISO 27001, ISO 9001, CMMI) |
| **Government** | Public sector tender requiring unpaid documentation, security clearance, or on-shore-only delivery, absent a Teaming Agreement |
| **Competitive** | Direct competitor — another offshore engineering services firm seeking to resell Zediant capacity without a partner agreement |
| **Recruitment** | Recruitment and staffing agencies (they are competitors in the augmentation motion, not buyers) |
| **Academic** | Universities, students, individual learners, bootcamps |
| **Non-commercial** | Individuals with an app idea and no funding or business entity |

## Soft disqualifiers — deprioritise, do not enrich

- Under 10 employees with no funding
- No engineering team and no technical counterpart
- Already operates a captive offshore development centre
- Recently completed material layoffs with contracting roadmap
- Existing dominant-client expansion that worsens concentration risk
- Excluded industries (see [Industries Evaluated and Excluded](#industries-evaluated-and-excluded)) without a segment override

## Escalation triggers — do not answer, escalate to a human

| Trigger | Reason |
|---|---|
| Request for the SOC 2 Type II attestation report | Zediant's materials say "aligned," "compliant," and "certified" in different places. Unresolved. |
| Security questionnaire or RFP requiring certification evidence | Same |
| Request for a client reference | Several case studies are NDA-protected with placeholder names |
| Request for an SLA with financial penalties | Underwriting decision, not a sales decision |
| Request for 24/7 on-call coverage | Staffing feasibility unconfirmed at 25–35 headcount |
| Enterprise deal requiring 12+ engineers | Exceeds documented ramp capacity |
| Any request for free speculative work | Contradicts documented commercial policy |

---

# SERVICE TO ICP MAPPING

● = primary recommendation · ○ = secondary · — = not applicable

| Service | Agencies | SaaS | Product Cos | Automotive | Fintech | Manufacturing | Logistics | Retail | Energy |
|---|---|---|---|---|---|---|---|---|---|
| Dedicated Engineering Pods | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | — |
| AI-Enabled Product Engineering | ○ | ● | ● | ○ | ● | — | — | ○ | — |
| Platform Engineering & DevOps | ○ | ● | ● | ○ | ● | ○ | ○ | ● | ○ |
| Enterprise Custom Development | — | — | ○ | ● | ● | ● | ● | ● | ● |
| Integration & Middleware | — | ○ | ● | ● | ○ | ● | ● | ● | ● |
| Legacy Modernisation | — | — | ● | ● | ○ | ● | ○ | ○ | ○ |
| Mobile Development | ● | ○ | ○ | ● | ● | — | ○ | ○ | — |
| Web Development | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ |
| E-commerce & CMS | ● | — | — | ○ | — | ● | — | ● | — |
| QA & Test Automation | ○ | ● | ○ | ○ | ● | — | ○ | ○ | — |
| Data Engineering & Analytics | — | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● |
| Maintenance & Managed Services | ● | ○ | ● | ● | ○ | ○ | ○ | ○ | ○ |
| Staff Augmentation | ● | ○ | ○ | — | — | — | — | — | — |
| Advisory & Consulting | ○ | ● | ● | ○ | ○ | ○ | ○ | ○ | ● |
| UI/UX Design | ○ | ○ | ○ | ○ | — | ○ | — | ○ | — |

---

# INDUSTRY PRIORITY

## Tier 1 — Lead with these

| Industry / Segment | Why |
|---|---|
| **Digital Agencies (AU)** | Best channel economics — one relationship reaches many end-clients. Shortest decision path. Documented strategic objective of three anchor agency partners. Documented client evidence (DIJGTAL, Networx). |
| **SaaS Companies, Seed–Series B (AU/UAE)** | Named highest strategic priority internally. Publicly observable buying signals (funding, hiring). Founder-level decisions without procurement. Aligns with long-term positioning. |
| **Automotive & Dealer Networks** | Deepest documented proof — production systems across APAC, UK, USA. Most differentiated capability (DMS middleware). Domain knowledge genuinely hard to replicate. |
| **Product Companies, CTO-led (AU/UAE)** | Strong pod fit, technically informed and fast decisions, richest source of integration and modernisation work. |

## Tier 2 — Pursue with proof and patience

| Industry | Why it is not Tier 1 |
|---|---|
| **Financial Services & Fintech** | Strong proof and high deal value, but the heaviest scrutiny on the unresolved SOC 2 wording issue. Elevate to Tier 1 once that is settled. |
| **Manufacturing & Industrial** | Good documented proof (Sitecore multisite) and healthy deal values, but longer cycles and referral-led rather than outbound-led. |
| **Logistics & Supply Chain** | Structurally excellent fit for the middleware differentiator, but vertical-specific proof is thinner than automotive. |
| **Retail & E-commerce** | Real capability and broad platform coverage, but a crowded market of specialist e-commerce agencies. Best reached through the agency channel. |

## Tier 3 — Opportunistic only, do not build campaigns

| Industry | Why |
|---|---|
| **Energy, Oil & Gas** | Strong single proof point and high value, but procurement cycles, scale expectations, and on-site preferences make cold acquisition impractical at current size. Referral-only. |
| **Healthcare** | Listed as a focus industry with no supporting evidence. Significant unaddressed regulatory burden. |
| **Media & Entertainment** | Listed with no supporting evidence. |
| **Real Estate** | Listed with no supporting evidence. Proptech *software* companies belong in ICP 2. |
| **Government / Public Sector** | Actively deprioritised. Unpaid tender documentation is a documented drain on capacity. Requires a Teaming Agreement before any pursuit. |

**Rationale for the ranking.** Tiering is driven by four factors in order: documented proof of delivery, decision-cycle length against Zediant's cash position, alignment with the 5–7 developer ramp constraint, and contribution to reducing single-client concentration. Market size is deliberately *not* a ranking factor — a large addressable market Zediant cannot serve or prove itself in is worth less than a small one where it can win.

---

# AI RETRIEVAL KEYWORDS

## Industry keywords (100)

digital agency, creative agency, web design agency, digital marketing agency, UX studio, UI design studio, product agency, software agency, development agency, technology consultancy, boutique consultancy, white-label development, agency partner, SaaS company, software as a service, B2B SaaS, vertical SaaS, enterprise SaaS, seed stage startup, Series A startup, Series B startup, funded startup, venture backed, bootstrapped software company, product company, software product company, ISV, independent software vendor, platform company, scale-up, technology company, automotive, automotive technology, automotive CRM, dealer management system, DMS, dealership, dealer network, OEM, automotive parts, aftermarket parts, vehicle data, lubricants, fintech, financial technology, payments, payment platform, trading platform, cryptocurrency exchange, investment platform, lending platform, regtech, compliance software, insurtech, banking technology, manufacturing, industrial manufacturing, material handling, industrial equipment, heavy equipment, industrial technology, logistics, freight, transport, supply chain, warehousing, distribution, third party logistics, 3PL, fleet management, retail, multi-store retail, e-commerce, online retail, B2B e-commerce, B2C e-commerce, franchise retail, omnichannel retail, marketplace, energy, oil and gas, upstream oil, energy services, utilities, renewable energy, mining technology, proptech, real estate technology, media technology, healthcare technology, edtech, hospitality technology, professional services firm, systems integrator, IT services, managed service provider, cloud consultancy, data consultancy, product consultancy, fractional CTO, technology partner, engineering partner, offshore development

## Buying intent keywords (100)

hiring engineers, hiring developers, hiring senior developers, hiring CTO, hiring VP engineering, hiring DevOps, hiring SRE, hiring QA, hiring platform engineer, engineering roles open, recruitment lag, cannot hire, hiring freeze, talent shortage, developer shortage, extending engineering team, extend capacity, scale engineering, engineering capacity, additional developers, dedicated team, dedicated developers, development partner, technology partner, outsourcing development, offshore team, nearshore team, staff augmentation, team augmentation, white label development, subcontract development, overflow capacity, bench capacity, seed funding, Series A funding, Series B funding, raised funding, funding round, investment round, venture funding, new funding, runway, product launch, new product, product roadmap, roadmap slippage, feature backlog, backlog growing, technical debt, rebuild platform, platform rebuild, version two, v2 launch, replatforming, cloud migration, cloud native, migrate to AWS, migrate to Azure, legacy modernisation, legacy migration, end of life, unsupported framework, monolith to microservices, digital transformation, transformation programme, system consolidation, post merger integration, acquisition integration, ERP upgrade, ERP implementation, CRM upgrade, CRM migration, CMS migration, e-commerce replatform, API integration, system integration, middleware project, data platform, data warehouse, analytics initiative, business intelligence project, AI initiative, AI strategy, LLM integration, generative AI project, machine learning project, automation initiative, workflow automation, security audit, SOC 2 preparation, compliance deadline, penetration test, security incident, outage, downtime, performance issues, scaling issues, peak load failure, market expansion, international expansion, new market entry, office opening, contract won, tender won, RFP issued

## Technology keywords (100)

.NET, .NET 8, .NET 9, ASP.NET, C#, LINQ, Entity Framework, Java, Spring, Spring Boot, Hibernate, JSP, EJB, Servlets, JMS, ActiveMQ, JAX-RS, Node.js, Express, TypeScript, JavaScript, Python, FastAPI, Django-adjacent, PyTorch, PHP, Laravel, CakePHP, LAMP, React, React 18, Angular, Angular 17, AngularJS, Next.js, jQuery, HTML5, CSS3, Tailwind CSS, Bootstrap, Sass, Less, Flutter, React Native, Ionic, Cordova, Swift, Objective-C, Kotlin, Android, iOS, MS SQL Server, MySQL, PostgreSQL, MongoDB, Oracle, Redis, NoSQL, Snowflake, SSIS, AWS, AWS Lambda, serverless, Azure, Azure AI, Google Cloud, Docker, Kubernetes, Terraform, CloudFormation, infrastructure as code, GitHub Actions, CircleCI, Jenkins, CI/CD, DevOps, DevSecOps, New Relic, observability, microservices, API first, event driven, REST API, GraphQL, OAuth2, JWT, OIDC, RBAC, SAST, DAST, SBOM, AES-256, TLS, Selenium, Appium, JMeter, BrowserStack, GitHub Copilot, Cursor IDE, OpenAI API, LangChain, vector database, RAG, Sitecore, Optimizely, WordPress, Drupal, Joomla, Magento, BigCommerce, Shopify, WooCommerce, Salesforce, HubSpot, ActiveCampaign

---

# DOCUMENT CONTROL

| Attribute | Value |
|---|---|
| Document | `icp.md` |
| Purpose | ICP knowledge base governing prospect qualification for all Zediant AI sales agents |
| Segment ICPs | 3 |
| Vertical ICPs | 6 |
| Industries excluded with reasoning | 7 |
| Sources | Zediant Sales Bible v1.0 (July 2026), Zediant 12-Month Sales & Growth Strategy (March 2026), Strategic Growth Plan, Outbound Email Strategies, Zediant Company Profile 2026, Zediant Rate Card, zediant.com |
| Last verified | August 2026 |

## Open items requiring human confirmation

1. **SOC 2 Type II wording** — "aligned," "compliant," and "certified" all appear across Zediant's published materials. Unresolved. Affects fintech and enterprise ICPs most acutely.
2. **PTB Score component weights** — proposed default, not confirmed by leadership.
3. **Scoring model conflict** — the Sales Bible's single blended model conflicts with the two-score (ICP + PTB) split used here. This document supersedes for agent use; confirm with leadership.
4. **Headcount inconsistency** — the March 2026 growth strategy states a 20-person team; the July 2026 Sales Bible states 25–35. Both are internal. Use 25–35 as the more recent figure.
5. **Revenue bands** for all ICPs are inferred from headcount, stage, and documented deal sizes, not published.
6. **Client concentration target** — internal documents state both "no single client above 40% within 12–18 months" (March 2026) and describe current concentration at ~90% (July 2026). Confirm current actual position before using either figure externally.
7. **Named dominant client** — internal strategy names InfoMedia and Netlube. Treat as confidential; never reference in outbound.

## Handling rules for AI agents

1. Items marked **Assumption** are inferences. Never present them as fact.
2. Classify by **segment** first, vertical second. Where they conflict, segment governs campaign selection.
3. Never target an industry from the excluded list without explicit human direction.
4. Never enrich a prospect scoring below 50 — this wastes Apollo credits on leads that will not be sequenced.
5. No lead enters an outreach campaign without human approval in Zoho (`Qualifying_Status = Approved`). This gate is non-negotiable.
6. Default to "SOC 2 Type II aligned." Escalate any request for the attestation report.
7. Never name a client in outbound material without confirming permission.
8. Never reference the dominant client relationship in any external communication.
9. Respect the 5–7 developer, three-month ramp constraint in every engagement discussion.
10. Weight new logos above existing-client expansion — concentration reduction is a standing priority ranked alongside growth.

## Related Context Files

| File | Relationship |
|---|---|
| `company.md` | Capability, limitation, and certification detail underpinning every fit assessment here |
| `services.md` | Service definitions, discovery questions, and disqualification signals per service |
| `campaigns.md` | Campaign structures, sequences, and sender mapping referenced throughout |
| `case_studies.md` | Full proof points referenced under each ICP's Success Stories |
| `competitors.md` | Alternatives each ICP evaluates Zediant against |
| `pricing.md` | Rate card and commercial thresholds underpinning Commercial Fit |
