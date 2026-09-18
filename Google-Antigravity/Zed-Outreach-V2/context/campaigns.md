# Overview

This document governs outbound campaign selection, messaging, and routing for Zediant Technologies. It is the reference an AI agent consults to answer: *given this lead, which campaign, why, from which mailbox, with what angle?*

**Zediant's campaign taxonomy is service-based.** There are exactly five live campaigns, C1–C5, each named for and organised around one of Zediant's core service lines. A lead enters the single campaign matching the service it most plausibly needs. This document defines the current service-based campaign taxonomy. **Only C1–C5 are valid campaign identifiers.** No legacy campaign taxonomy or retired campaign naming should be used anywhere in the Revenue Engine.


### Current Campaigns

| Campaign | Name | Planned Share |
|---|---|---:|
| **C1** | AI-Enabled Product Engineering | **25%** |
| **C2** | Engineering Pods & Staff Augmentation | **25%** |
| **C3** | Platform Engineering & Cloud Modernization | **15%** |
| **C4** | Middleware & API Integration (ZCoupler) | **25%** |
| **C5** | Enterprise Custom Development & Modernization | **10%** |


## Migration notice — read before using this document

| Item | Before | Now |
|---|---|---|
| Taxonomy | Current service-based campaign structure | **C1–C5**, one per core service line |
| Sending platform | Saleshandy (retired) | **Apollo Sequences** (native email + LinkedIn multichannel execution) |
| Sequence ID handling | Hardcoded sequence IDs | **Resolved dynamically.** `campaign-selection` outputs campaign name (C1–C5); `apollo-distribution` resolves that name to a live Apollo sequence by title match at enrollment time. |
| CRM picklist | `Lead_Campaign_Category` used List-letter values requiring a mismatch-mapping table | `crm-update` v5.1+ writes C1–C5 names directly — the old mismatch table is retired along with it |

## Campaign Portfolio Allocation

The following percentages are the **planned portfolio distribution targets** across qualified leads. They are operational planning targets, not campaign-selection scores and must never override a lead's evidence-based campaign fit.

| Campaign | Campaign Name | Planned Share |
|---|---|---:|
| **C1** | AI-Enabled Product Engineering | **25%** |
| **C2** | Engineering Pods & Staff Augmentation | **25%** |
| **C3** | Platform Engineering & Cloud Modernization | **15%** |
| **C4** | Middleware & API Integration (ZCoupler) | **25%** |
| **C5** | Enterprise Custom Development & Modernization | **10%** |

### Allocation rules

1. Select the campaign based on the prospect's **actual business problem, technical need, business signal, ICP fit, PTB/buying signal, and persona**.
2. The 25/25/15/25/10 percentages are used to monitor portfolio balance **after qualification and campaign-fit scoring**.
3. Never move a lead into a weaker-fit campaign merely to satisfy a percentage target.
4. If the qualified pipeline does not contain enough evidence for a campaign, leave that campaign below target and report the shortfall as a portfolio gap.
5. Campaign distribution targets do not constitute outreach approval. The existing BDM approval gate remains mandatory.
6. For planning purposes, a batch of 100 qualified leads would target approximately C1=25, C2=25, C3=15, C4=25, C5=10, subject to actual evidence-based fit.

### Campaign Fit Scoring (Single PTB Standard)

In accordance with `GEMINI.md` Section 15A and `ptb-scoring/SKILL.md`, Zediant uses **one numeric PTB score only (Initial Buying Signal, 0–100)** calculated pre-outreach for every qualified lead. There is no separate post-engagement PTB model and no Path A / Path B distinction.

`campaign-selection/SKILL.md` uses the standard five-factor campaign-fit model, consuming the single PTB score directly as its Buying Signal input:

| Factor | Weight | Description |
|---|---:|---|
| Business Problem / Technical Need | **35%** | Verifiable technical requirement matching Zediant capabilities |
| Business Signal | **25%** | Observable corporate event (growth, hiring, restructuring, tech adoption) |
| ICP Fit | **15%** | Firmographic, geography, employee size, and domain qualification |
| Buying Signal (PTB Score) | **15%** | Pre-outreach Buying Signal score from `ptb-scoring` |
| Persona Fit | **10%** | Decision-maker relevance and authority |
| **Total** | **100%** | |

**High-Intent Signal Priority Rule:**
During production operations, leads are routed strictly to the campaign where **actual business pain, technology triggers, and PTB scores are highest**. Portfolio allocation targets are secondary balancing guidelines and must **never** be used to force or pad leads into lower-fit campaigns. If a campaign lacks high-intent leads on a given day, it receives zero leads.

---

**Why service-based, not intent-based.** The old taxonomy grouped prospects by buying situation (an agency at capacity, a funded SaaS company, a company hiring) and let one service — usually a pod — get sold five different ways. The new taxonomy is simpler and matches what's live in Apollo: one sequence per service, and campaign selection is a question of *which service does this prospect most plausibly need*, not *which situation are they in*. A single prospect's underlying business situation still shapes messaging and case study choice within a campaign — that reasoning hasn't disappeared, it has moved into each campaign's own Messaging Angle and Personalization sections below.

**Campaign selection principle.** Campaign selection is based only on the current C1–C5 service taxonomy. The prospect's business situation, buying signal, technical need, ICP fit, PTB signal, and persona help determine which service is the best fit, but none of these create a separate campaign taxonomy. Referrals and other lead sources also enter the appropriate C1–C5 campaign based on the service need identified.

## Non-negotiable operating rules

These override every other instruction in this document.

| Rule | Detail |
|---|---|
| **Never activate a campaign without approval** | All Apollo sequences (C1–C5) remain Draft or paused until explicit human verification. Activation is an explicit human (BDM) action in Apollo. No automated task may change sequence status. |
| **BDM approval gate in Apollo** | No lead enters an active Apollo sequence without `Approval Status = "Approved for Outreach"` on the Apollo contact record. Non-negotiable. `apollo-distribution` uses this as its sole eligibility check. |
| **Resolve sequences by name, never hardcode an ID** | `apollo-distribution` resolves a campaign name (C1–C5) to a live Apollo sequence by title match at enrollment time. This document records campaign names, senders, and daily limits — never a static sequence ID. |
| **Apollo is the sending & intelligence platform** | Apollo is the sole platform for lead acquisition, contact intelligence, and sequence delivery. Saleshandy is retired. |
| **Response-triggered Zoho CRM creation** | Leads are added to Zoho CRM **ONLY when a response is received** through outreach. Cold uncontacted prospects remain in Apollo. On reply, `apollo-reply-tracker` + `crm-update` creates the lead in Zoho CRM (`Lead_Status = "Engaged"`), writes back the `Zoho Record ID`, and updates `Zoho Sync Status = "Synced"`. |
| **Mailbox warm-up & health** | Active mailbox (`rajeev@zedianttechnologies.info`, Apollo account `6a70212e10bb20000cb56d8f`) maintains conservative limits (25–35 emails/day total across initial + follow-ups). |
| **Multichannel sequence cadence** | Apollo sequences use a cohesive 5-step multichannel structure (Automated Emails + LinkedIn Connection and Message tasks) for C1–C5. |
| **Apollo custom fields enrichment** | Antigravity enriches all 10 custom fields on Apollo contacts (`ICP Score`, `Lead Source`, `Target Segment`, `Company Trigger`, `Pain Point`, `Outreach Angle`, `Approval Status`, `Zoho Record ID`, `Zoho Sync Status`, `Personalised Email`). |
| **Pacing delay** | Apollo connected email account maintains a minimum 600-second (10 minutes) pacing delay between outbound emails to protect sender domain reputation. |
| **Strict email verification** | Only contacts with Apollo `contact_email_status = ['verified']` are eligible for outreach. Never email guessed or catch-all addresses. |
| **Zero tracking pixels** | Both open tracking and click tracking remain **disabled** (`enable_open_tracking: false`, `enable_click_tracking: false`) to maximize inbox placement. |
| **Threaded sequence cadence** | Email follow-up steps send as threaded replies (`Re: {{Subject}}`) directly in the same conversation thread. Threaded bumps look human and build genuine dialogue. |
| **Low-friction CTAs** | Never ask for a 30-minute meeting on Touch 1. Use low-friction, permission/curiosity-based CTAs (e.g., *"Open to checking a 2-minute teardown of how we set this up for [similar client]?"* or *"Worth a brief chat, or should I leave you in peace?"*). |
| **Drop the sequence on reply** | If a prospect replies at any point, Apollo automatically stops the sequence. Respond as a real human conversation the same business day. |
| **One campaign per lead** | Each lead maps to exactly one of C1–C5. High-Intent Signal Priority dictates routing. |

---

# LIVE CAMPAIGN REGISTRY

| # | Campaign Name | Apollo Sequence ID | Sequence Structure | Cadence & Threading |
|---|---|---|---|---|
| **C1** | C1 - AI-Enabled Product Engineering | `6aa7ec0e7c0f80000cbd7600` | **6-step Multichannel (4 Emails + 2 LinkedIn)** | Step 1 (Day 1 Auto Email) → Step 2 (Day 4 LinkedIn Connect) → Step 3 (Day 6 Email Threaded) → Step 4 (Day 9 LinkedIn Message) → Step 5 (Day 13 Email Framework / Benchmark) → Step 6 (Day 17 Email Breakup) |
| **C2** | C2 - Engineering Pods & Staff Augmentation | `6aa7eca553473f000c678940` | **6-step Multichannel (4 Emails + 2 LinkedIn)** | Step 1 (Day 1 Auto Email) → Step 2 (Day 4 LinkedIn Connect) → Step 3 (Day 6 Email Threaded) → Step 4 (Day 9 LinkedIn Message) → Step 5 (Day 13 Email Framework / Playbook) → Step 6 (Day 17 Email Breakup) |
| **C3** | C3 - Platform Engineering & Cloud Modernization | `6aa7ecb31fd57300143fbfa7` | **6-step Multichannel (4 Emails + 2 LinkedIn)** | Step 1 (Day 1 Auto Email) → Step 2 (Day 4 LinkedIn Connect) → Step 3 (Day 6 Email Threaded) → Step 4 (Day 9 LinkedIn Message) → Step 5 (Day 13 Email Cloud Audit Benchmark) → Step 6 (Day 17 Email Breakup) |
| **C4** | C4 - Middleware & API Integration (ZCoupler) | `6aa7ecbea907dd00140753b2` | **6-step Multichannel (4 Emails + 2 LinkedIn)** | Step 1 (Day 1 Auto Email) → Step 2 (Day 4 LinkedIn Connect) → Step 3 (Day 6 Email Threaded) → Step 4 (Day 9 LinkedIn Message) → Step 5 (Day 13 Email Middleware Architecture) → Step 6 (Day 17 Email Breakup) |
| **C5** | C5 - Enterprise Custom Development & Modernization | `6aa7ecc953473f000c678b8e` | **6-step Multichannel (4 Emails + 2 LinkedIn)** | Step 1 (Day 1 Auto Email) → Step 2 (Day 4 LinkedIn Connect) → Step 3 (Day 6 Email Threaded) → Step 4 (Day 9 LinkedIn Message) → Step 5 (Day 13 Email Decoupling Teardown) → Step 6 (Day 17 Email Breakup) |

*Volume Allocation:* All campaigns share the single active mailbox capacity during ramp-up (**25–35 emails/day total**). Sourcing pulls ~7–10 leads/day allocated based on **High-Intent Signal Priority** (where technical need and PTB score are strongest). Sequences are managed natively in Apollo and resolved dynamically by `apollo-distribution` via title match or ID.

## ⚠️ Open items — operational status

### 1. Mailbox warm-up status
Active mailbox (`rajeev@zedianttechnologies.info`, Apollo account `6a70212e10bb20000cb56d8f`) Warmbox warmup concludes on **September 17, 2026** (currently >89% complete). Live sequences may be activated on September 17.

### 2. Send schedule timezone
Confirm sequence schedule directly in Apollo before activation:
| Target market | Schedule |
|---|---|
| United States (US/Eastern & Pacific) | 09:00–16:00 local, Mon–Fri |
| Australia (AEST) | Australia/Sydney, 08:30–16:30, Mon–Fri |
| UAE | Asia/Dubai, 08:30–16:30, **Sunday–Thursday** |

### 3. "ZCoupler" naming rule
C4 is officially named **"Middleware & API Integration (ZCoupler)"** in the campaign registry. However, in all prospect-facing emails, refer to the capability as **"Zediant Middleware"** or **"integration and middleware engineering"**. Never use "ZCoupler" externally.

---

# CAMPAIGN FRAMEWORK

## Why service-based

Each campaign now corresponds to exactly one thing Zediant sells: C1 is the AI-Enabled Product Engineering service, C2 is the Dedicated Engineering Pods and Staff Augmentation services together, C3 is Platform Engineering, Cloud & DevOps, C4 is Integration & Middleware Engineering, and C5 is Enterprise Custom Development (including Legacy Modernisation). See `services.md` for full service definitions — this document assumes that layer and builds the outbound motion on top of it.

**Services without their own campaign.** Not every service in `services.md` has a dedicated C1–C5 campaign. Mobile Application Development, Web Application Development, E-commerce & CMS Development, and QA & Test Automation are documented as "usually delivered within a pod" — leads whose stated need is one of these route to **C2**. Data Engineering & Analytics has "limited standalone evidence" and is documented as a cross-sell into Integration work — leads route to **C4** as the primary fit, with **C1** as a secondary fit where the driver is AI-ready data architecture rather than integration. Maintenance & Managed Services, UI/UX Design, and Advisory & Engineering Consulting are not primary outbound motions at all — Maintenance is the natural conversation at the close of a build engagement, Advisory is the low-commitment entry offer available *within* any of C1–C5 rather than a campaign of its own, and UI/UX is a supporting function never sold standalone. Do not create outbound sequences around these three; if a prospect's stated need is genuinely just one of them, use the closest campaign above and route the actual service conversation through discovery.

## Selection principle

Campaign selection follows this order of precedence:

1. **Discovered technical need** — what does the prospect actually need built or extended? This determines the campaign directly, because campaign now equals service.
2. **Referral override** — if the lead is a referral or partner introduction, `campaigns.md`'s prior source-overrides-everything rule still applies to *messaging tone and cadence* (see Referral-sourced leads below), but the lead still enters whichever of C1–C5 matches the discovered need. There is no separate referral campaign anymore.
3. **Persona** — shapes messaging tone (technical, consultative, or executive) once the campaign is already selected. Mailbox/sender assignment is an Apollo configuration detail this document does not track (see the Open Items note above).

Vertical industry does **not** drive campaign selection. It drives case study selection and personalisation within the campaign, exactly as before.

## Referral-sourced leads

A referral or partner introduction is still handled differently in tone and cadence than a cold lead, even though it now enters one of C1–C5 rather than a dedicated campaign:

- **Lead with the referrer's name in the first line**, not the campaign's standard messaging angle.
- Use a **two-touch warm sequence** rather than the standard four-touch cold cadence for that lead specifically — a four-touch pursuit of a warm referral reads as pushy and can damage the referrer relationship.
- No pitch in the opening message; propose a short introductory conversation instead.
- Update the referrer on the outcome regardless of result.

---

# C1 — AI-Enabled Product Engineering

**Daily limit:** 30 · **Status:** Draft

## Campaign Objective

Win funded SaaS and product companies whose roadmap has outgrown their engineering capacity, positioning Zediant's AI-assisted delivery methodology as the way to close that gap. This is the outbound expression of the AI-Enabled Product Engineering service — internal materials name the underlying SaaS segment the highest strategic priority.

## Business Situation

Select this campaign when a company needs a platform built, rebuilt, or extended at a pace its internal team cannot match — particularly where funding, a public roadmap commitment, or competitive pressure is the driver. The dominant signal is **funding, launch, or scaling pressure**, not primarily an open-role hiring gap (that need routes to C2 instead).

## Target ICP

| Dimension | Profile |
|---|---|
| Industries | B2B SaaS, vertical SaaS, fintech, proptech, other software product categories |
| Company size | 10–200 employees |
| Growth stage | Seed, Series A, Series B — post product-market-fit |
| Countries | Australia (primary), UAE (primary), UK/US/South Africa (opportunistic) |
| Decision makers | CTO, Founder/CEO, VP Engineering, Head of Engineering |

Cross-reference: `icp.md` → ICP 2 (SaaS Companies, Seed–Series B).

## Business Problems

- Roadmap commitments to investors or customers that engineering cannot meet
- Runway pressure making a wrong hire expensive and slow to correct
- Founders still writing code instead of selling or raising
- Feature velocity slower than better-funded competitors
- MVP architecture not built to scale past current tenant count
- Technical debt from a fast build now blocking growth
- Enterprise customers imposing security requirements the startup cannot meet

## Buying Signals

- **Funding round announced** — the strongest single signal
- Public roadmap or product launch commitment
- Acquisition completed, creating integration workload
- Competitor shipped a feature they lack
- Scaling complaints visible in reviews or status pages
- New enterprise logo announced
- Founder posting publicly about growth or hiring difficulty
- Investor-committed milestone approaching

## Disqualification Signals

- Pre-seed or idea stage with no funding and no product
- No technical co-founder or engineering leadership
- Already operates a large offshore team
- Core need is AI/ML research rather than product engineering
- Recently completed layoffs with contracting roadmap
- Fewer than 10 employees with no funding
- **Dominant signal is active engineering hiring, not a build/scale need** → route to C2 instead

## Recommended Services

AI-Enabled Product Engineering (primary). Cross-sells: Platform Engineering & Cloud DevOps, Data Engineering & Analytics, Dedicated Engineering Pods (for ongoing capacity once the build lands). See `services.md`.

## Value Proposition

Senior engineering capacity in 5–10 days instead of a multi-month local hiring cycle, working inside the client's stack, sprints, and review standards, with an AI-assisted delivery methodology mapped to every SDLC stage.

## Messaging Angle

Lead with **roadmap versus headcount**. The CTO's problem is that the roadmap grows faster than the local senior talent market allows. Emphasise senior-only staffing, speed to team, and client control over who joins.

**Do not lead with an AI product pitch.** Zediant's defensible AI claim is delivery method, not shipped AI product portfolio — internal policy is explicit on this. See `services.md` → AI Capabilities and `competitors.md` → Category 9 (AI-Native Engineering Firms) before ever discussing "what AI have you shipped."

Effective frame: *"The roadmap grows faster than you can hire senior engineers locally."*

## Recommended Email Tone

**Technical.** Architecture, AI-assisted development, scalability, security. Concrete and specific — this audience detects and discounts marketing language quickly.

## Personalization Opportunities

- Funding round: amount, date, lead investor
- Named investors and what they typically push portfolio companies toward
- Product launches or roadmap statements
- Recently announced enterprise customers
- Technology stack visible in job posts or engineering blog
- CTO's LinkedIn posts or conference talks
- Acquisition activity
- Public status page incidents or user complaints about performance

## Discovery Questions

Campaign-specific probes. The 20 segment questions in `icp.md` → ICP 2 apply as the qualification base.

1. What did the last raise change about the roadmap?
2. What are you committed to shipping, and by when?
3. Who committed to that timeline — you, the board, or a customer?
4. What is the gap between the plan and current capacity, in engineer-months?
5. What happens if the milestone slips a quarter?
6. What is your architecture today, and what will break first at 5x scale?
7. Is the platform multi-tenant? Does it need to be?
8. Do you have CI/CD, code review, and automated coverage?
9. When you say AI, do you mean features in your product, or faster delivery of your software?
10. Has anyone on the team built LLM features into production before?
11. What is your funding position and runway?
12. Have you validated this architecture with anyone external?
13. What does your security review for a new vendor involve?
14. Would you start with a defined scope before a longer commitment?
15. Who else needs to agree before this moves forward?

## Recommended CTA

Primary: **15-minute call to compare against hiring.** Secondary: **Technical overview document** — a lower-friction alternative for CTOs who dislike calendar commitments. Tertiary: **Architecture review** as a paid or discounted entry engagement.

## Sequence Strategy (Apollo Multichannel)

Six-step Apollo multichannel sequence combining 4 automated threaded emails and 2 non-blocking LinkedIn tasks:

| Step | Type | Timing | Purpose & Custom Field Integration |
|---|---|---|---|
| Step 1 | `auto_email` | Day 1 | Personalized body using `{{Personalised Email}}` (3-beat micro-structure) + Teardown CTA. |
| Step 2 | `linkedin_step_connect` | Day 4 (+3d) | LinkedIn connection request task referencing `{{Company Trigger}}` (no pitch, no Zediant mention). |
| Step 3 | `auto_email` | Day 6 (+2d, Threaded) | Threaded follow-up on AI-accelerated velocity (30–40% faster) & senior architecture ownership, referencing `{{Pain Point}}`. |
| Step 4 | `linkedin_step_message` | Day 9 (+3d) | Conversational LinkedIn check-in task (send only if connected; non-blocking). |
| Step 5 | `auto_email` | Day 13 (+4d, Threaded) | Technical delivery framework / benchmark (14-day production readiness). |
| Step 6 | `auto_email` | Day 17 (+4d, Threaded) | Graceful permission-to-close breakup referencing `{{Pain Point}}`. |

## Common Objections

| Objection | Response direction |
|---|---|
| "We're not ready to outsource." | Reframe as extension; client owns the roadmap and interviews every engineer |
| "What AI products have you built?" | Answer honestly — capability is AI-assisted delivery; AI product work is being built out. Internal policy mandates this |
| "You're more expensive than other offshore shops." | Senior-default staffing, no junior bench; compare total cost including rework |
| "We haven't heard of Zediant." | Small scoped start; offer an existing client reference |
| "We don't want a long contract." | Most long relationships began as one project |
| "Security is a concern." | DevSecOps, SAST/DAST, encryption, RBAC. **Use "SOC 2 Type II aligned"; escalate any request for the attestation report** |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Recipient's morning, local time |
| Cadence | 4 emails over 12–14 days |
| Channels | LinkedIn connection Day 3, LinkedIn message Day 8 (manual) |
| On reply | Same-day, routed internally by topic (technical vs. commercial) |
| Escalation | Loop in the Founder early on Hot-tier leads (ICP score 80+) |
| No reply | Follow-Up Later in Zoho; re-engage on the next funding or launch signal |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline; no historical data on Apollo sequences yet |
| Meeting rate | Contributes to 15–30 discovery meetings/month across all campaigns |
| Qualified opportunities | Funded SaaS with confirmed roadmap gap and named budget |
| Pipeline generated | Larger deals — annualised pod value USD 80,000–150,000+ |
| Strategic contribution | New logos reducing client concentration |

## Campaign Priority

**HIGH.** Named the highest strategic priority internally. Publicly observable signals, founder-level decisions without procurement, best alignment with long-term positioning.

## Related Services

`services.md` → AI-Enabled Product Engineering · Platform Engineering & Cloud DevOps · Data Engineering & Analytics

## Related Case Studies

**None currently approved.**

Do not use CS-04 or CS-07 as C1 proof points. Do not imply that Zediant has a client case study proving AI product engineering delivery. Do not create or infer a replacement case study.

## Related ICPs

`icp.md` → ICP 2 (SaaS Companies, Seed–Series B)

## AI Selection Rules

Choose C1 when:

- The company sells its own software product on a subscription or product-led model
- Funding is disclosed at seed, Series A, or Series B, or a specific build/scale need is stated
- Headcount is 10–200
- The dominant observable signal is **funding, launch, or scaling pressure** — not an open-role hiring gap
- Contact is CTO, Founder, or VP Engineering

Choose a different campaign when:

- The dominant signal is **active engineering job posts** or a capacity/staffing gap → **C2**
- The core need is infrastructure, deployment, or cloud reliability rather than the product itself → **C3**
- The core need is connecting systems or data exchange → **C4**
- The company is not VC-funded and the need is a defined roadmap item on an established product → **C5**

---

# C2 — Engineering Pods & Staff Augmentation

**Daily limit:** 30 · **Status:** Draft

## Campaign Objective

Win prospects — digital agencies, funded SaaS companies with a hiring gap, and CTO-led product companies — whose need is engineering capacity itself, either as a full embedded pod or as individual senior engineers augmenting an existing team. This campaign carries two distinct entry angles into the same underlying service: **agency capacity extension** and **hiring-gap coverage**.

## Business Situation

Select this campaign for either of two situations:

1. **Capacity angle** — a digital agency, studio, or consultancy is winning work its delivery team cannot absorb, and hiring, freelancing, or declining the work each carry a cost it feels.
2. **Hiring-gap angle** — a company (most often SaaS or product) has one or more open engineering roles, particularly senior ones open 60+ days, and needs the work covered while the search continues or instead of a permanent hire.

Both angles lead to the same service — Dedicated Engineering Pods or Staff Augmentation — so both are handled inside this one campaign, differentiated by messaging angle and case study, not by a separate sequence.

## Target ICP

| Dimension | Profile |
|---|---|
| Industries | Digital agencies, creative agencies with development, web/product agencies, UX studios, technology consultancies; also SaaS and product companies with an open-role signal |
| Company size | 10–200 employees |
| Growth stage | Established, project-driven (agencies); any stage with allocated hiring budget (hiring-gap) |
| Countries | Australia (primary), UAE (primary), UK (opportunistic) |
| Decision makers | COO, Head of Delivery, Managing Director, Founder/CEO, Technical Director (agencies); CTO, VP Engineering, Head of Engineering, Engineering Manager (hiring-gap) |

Cross-reference: `icp.md` → ICP 1 (Digital Agencies) and ICP 2 (SaaS Companies) where the dominant signal is hiring rather than funding.

## Business Problems

- Project won that exceeds current delivery capacity
- Bench cost between projects eroding thin margins
- Work declined because the team cannot absorb it
- Freelancers with no continuity, accountability, or backfill
- Senior roles open for months with no viable candidates
- Competing for talent against better-funded local employers
- Recruitment fees consuming budget without producing hires
- Hiring freeze imposed while workload continues

## Buying Signals

- Named client win or large contract announced (agency angle)
- **Multiple simultaneous engineering job posts**, especially senior or long-vacant (hiring-gap angle — the single most personalisable signal available)
- A senior or lead role open 60+ days, or reposted
- Headcount reduced while client roster holds
- Agency acquisition or merger
- New service line requiring engineering depth
- Hiring freeze announced alongside continuing project commitments

## Disqualification Signals

- Pure creative, brand, or media-buying agency with no development offering
- Under 10 employees at an agency (insufficient project volume to sustain a pod)
- Already operates a captive offshore development arm
- Recruitment or staffing agency (competitor, not buyer)
- Roles are non-engineering, junior/graduate-only, or in stacks outside documented capability
- Company is hiring successfully and quickly with no backlog problem

## Recommended Services

Dedicated Engineering Pods, Staff Augmentation (both primary). Also the entry point for Mobile Application Development, Web Application Development, E-commerce & CMS Development, and QA & Test Automation, which are typically delivered within a pod rather than sold as standalone campaigns. See `services.md`.

## Value Proposition

Delivery capacity — full pod or individual senior engineers — that flexes with demand, under the client's brand or direction, without permanent headcount, bench cost, or a multi-month local search.

## Messaging Angle

**For the agency angle:** commercial, not technical. Lead with the bench-versus-backlog trade-off. Emphasise white-labelling, scale-down terms, and overlap hours. Do not lead with AI — an agency COO buys predictable delivery capacity, not AI.

Effective frame: *"When you win a project bigger than your current bench, do you hire, subcontract, or stretch the timeline?"*

**For the hiring-gap angle:** name the specific open role and how long it has been posted — the most personalisable opening available in any Zediant campaign. Frame as complementary to hiring, not a replacement; a CTO defending a headcount plan will resist "don't hire" but will engage with "cover the gap while you hire."

Effective frame: *"You've had a senior backend role open since May. What is that costing you in shipped features?"*

## Recommended Email Tone

**Consultative** for the agency angle. **Technical and direct** for the hiring-gap angle — this audience is time-poor and reads on mobile between interviews.

## Personalization Opportunities

- Recently announced client win or project; open developer roles on an agency's careers page
- **Exact job title and posting date** for hiring-gap leads — the highest-value personalisation in the entire campaign set
- Number of concurrently open engineering roles; whether a role has been reposted
- Technology stack visible in job posts or case studies
- Founder, MD, or CTO LinkedIn posts about growth, hiring, or capacity
- Office expansion, award wins, or PR indicating pipeline growth

## Discovery Questions

The 20 segment questions in `icp.md` → ICP 1 apply for agency leads; the 20 in ICP 2 apply for hiring-gap leads. Campaign-specific probes:

1. What triggered you to look at external delivery capacity now?
2. How did you resource the last project that exceeded your team, or the last time a role sat open?
3. What have you declined or delayed in the last twelve months, and what was it worth?
4. How much are you spending on freelancers, subcontractors, or recruitment fees monthly?
5. What has gone wrong with a subcontractor or contractor before?
6. Do your clients (or internal stakeholders) know who builds, or is white-labelling essential?
7. How long has the role been open, and what has it cost you in delivery terms?
8. Would you consider covering the gap while a search continues?
9. What overlap hours would you need to work comfortably?
10. Who signs off on a delivery partner or contract-spend decision?

## Recommended CTA

Primary: **Discovery call, 15 minutes.** Secondary: **Send two relevant case studies or two anonymised engineer profiles** — documented as an effective lower-friction alternative for both audiences.

## Sequence Strategy (Apollo Multichannel)

Five-step Apollo multichannel sequence combining automated emails and high-touch LinkedIn tasks:

| Step | Type | Timing | Purpose & Custom Field Integration |
|---|---|---|---|
| Step 1 | `auto_email` | Day 1 | Personalized body using `{{Personalised Email}}` (body only; salutation and signature managed in sequence) + low-friction CTA. |
| Step 2 | `linkedin_step_connect` | Day 3 (+2d) | LinkedIn connection request task referencing `{{Company Trigger}}` (no pitch, no Zediant mention). |
| Step 3 | `auto_email` | Day 6 (+3d, Threaded) | Threaded follow-up dynamically referencing `{{Pain Point}}` (senior capacity in 2–3 weeks). |
| Step 4 | `linkedin_step_message` | Day 9 (+3d) | LinkedIn message task upon connection referencing `{{Pain Point}}` with conversational follow-up. |
| Step 5 | `auto_email` | Day 13 (+4d, Threaded) | Technical proof point / low-pressure breakup referencing `{{Pain Point}}`. |

## Common Objections

| Objection | Response direction |
|---|---|
| "We already have freelancers/a recruiter we trust." | Continuity and backfill — a freelancer leaving mid-project has no replacement; a pod does |
| "Our clients wouldn't accept offshore." | White-label model; the client sees the agency's brand |
| "We can't afford your rates on our margins." | Compare against fully-loaded local hire plus bench time or recruitment fees, not a freelance hourly rate |
| "We've been burned by offshore before." | Ask specifically what failed; small defined scope; senior-only staffing; offer a reference |
| "We want a permanent hire, not a contractor." | Not either/or — cover the gap while the search continues |
| "Time zones make it hard." | 2.5 hrs to Perth, 4.5 to Sydney; overlap structured deliberately |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Land in the recipient's morning, local time |
| Cadence | 4 emails over 12–14 days |
| Channels | LinkedIn connection Day 3, LinkedIn message Day 8 (manual) |
| Signal monitoring | Re-trigger hiring-gap leads if the role is reposted — a reposted role is a stronger signal than the original |
| On reply | Same-business-day response. Drop the sequence entirely. |
| No reply after break-up | Move to Follow-Up Later in Zoho. Re-engage in one quarter (agency) or 60 days (hiring-gap, if role still open). |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline; expected among the strongest given signal specificity on the hiring-gap side — assumption, unvalidated |
| Meeting rate | Contributes to 15–30 discovery meetings/month |
| Qualified opportunities | Agencies with named projects and confirmed budget; companies with confirmed open role and allocated budget |
| Conversion to pod | Track augmentation-to-pod expansion — the documented land-and-expand path |
| Anchor partners secured | **3** agency partners — the stated strategic objective |

## Campaign Priority

**HIGH.** Combines the best channel economics available (agency relationships reaching many end-clients) with the most specific, personalisable signal in the portfolio (open roles).

## Related Services

`services.md` → Dedicated Engineering Pods · Staff Augmentation · Web Application Development · E-commerce & CMS Development · Mobile Application Development · QA & Test Automation

## Related Case Studies

`case_studies.md` → Primary: CS-02 (Wholesale Parts CRM), CS-03 (Lubricant Recommendation & Equipment Maintenance Application), CS-06 (Team Augmentation for Automotive Software), CS-07 (Cryptocurrency Trading Application), CS-08 (Sitecore CMS Multisite Platform), CS-09 (BigCommerce Integration for Australia's Largest Office Supply Brand), CS-10 (WordPress Migration for an Online Poker Platform). **Never present CS-02 and CS-06 together as separate customers — they are the same underlying account; see the CS-02/CS-06 restriction in `case_studies.md`.**

## Related ICPs

`icp.md` → ICP 1 (Digital Agencies) · ICP 2 (SaaS Companies) where hiring is the dominant signal

## AI Selection Rules

Choose C2 when:

- The company sells services to its own clients and has an internal delivery function, however small, **or**
- The company has one or more open, verified engineering roles at mid-level or senior, in a stack within Zediant's documented capability
- Headcount is 10–200
- The contact is COO, Head of Delivery, MD, agency Founder, CTO, VP Engineering, or Engineering Manager

Choose a different campaign when:

- The company sells its own software product and the dominant signal is funding/scaling rather than hiring → **C1**
- The core need is infrastructure or cloud reliability → **C3**
- The core need is connecting systems → **C4**
- The company is established/non-funded and needs a defined roadmap item built → **C5**

---

# C3 — Platform Engineering & Cloud Modernization

**Daily limit:** 30 · **Status:** Draft

## Campaign Objective

Win prospects whose problem sits in the infrastructure layer beneath their product — cloud architecture, CI/CD, reliability, observability, and modernising cloud infrastructure — rather than in the application layer itself.

## Business Situation

Select this campaign when a company's engineering problem is deployment, reliability, scaling, or cloud cost, not a missing product feature. The signal is usually an incident, a hiring gap in DevOps/SRE, or an announced cloud migration.

## Target ICP

| Dimension | Profile |
|---|---|
| Industries | SaaS, fintech, e-commerce, enterprise platforms, logistics |
| Company size | 20–200 employees |
| Decision makers | CTO, VP Engineering, Head of Infrastructure, DevOps Lead, CIO |

Cross-reference: `icp.md` → ICP 2 (SaaS Companies) and ICP 3 (Product Companies) where the stated problem is infrastructure rather than product.

## Business Problems

- Manual, slow, or unreliable deployment processes
- Infrastructure configured by hand and impossible to reproduce
- Downtime and performance degradation under load
- No observability — problems discovered by users rather than monitoring
- Security scanning absent from the delivery pipeline
- Monolithic architecture blocking independent team delivery
- Cloud spend growing without visibility or control

## Buying Signals

- Recent public outage or degraded-performance incident
- Hiring for DevOps, SRE, or platform engineering roles
- Announced migration to cloud or between clouds
- Rapid user growth
- New compliance requirement (SOC 2, GDPR, sector regulation)
- Post-acquisition infrastructure consolidation

## Disqualification Signals

- Requires a specific cloud certification tier Zediant cannot evidence
- Wants full production ownership with no internal counterpart
- Demands a contractual 99.99% uptime SLA with penalties
- Expects genuine 24/7 on-call coverage at low cost
- Infrastructure is already mature with a dedicated internal platform team

## Recommended Services

Platform Engineering, Cloud & DevOps (primary). Cross-sells: Dedicated Engineering Pods (assessment findings often reveal application-layer work), Enterprise Custom Development, QA & Test Automation, Maintenance & Managed Services. See `services.md`.

## Value Proposition

Deployment, reliability, and cloud cost brought under control — reproducible infrastructure, security embedded in the pipeline, and observability that surfaces problems before customers do.

## Messaging Angle

Lead with the specific reliability or deployment pain, not a generic "we do DevOps" pitch. This is a technical audience that responds to a named problem: an outage, a slow release cadence, or an unexplained cloud bill.

Effective frame: *"Deployments take a day and someone has to babysit them — what does that cost you during a bad week?"*

**Do not promise 24/7 SRE coverage** without confirming staffing at the point of quoting — genuine round-the-clock coverage is unlikely at Zediant's current headcount. See `services.md` → Platform Engineering, Cloud & DevOps → Risks.

## Recommended Email Tone

**Technical.** Deployment frequency, MTTR, infrastructure as code, observability. This audience discounts vague reliability claims quickly.

## Personalization Opportunities

- A specific named outage, status-page incident, or public performance complaint
- Job posts for DevOps, SRE, or platform roles
- Announced cloud migration or multi-cloud strategy
- Public statements about scaling or growth outpacing infrastructure
- Compliance deadlines (SOC 2, GDPR) creating pipeline security pressure

## Discovery Questions

1. What does your deployment process look like today, start to finish?
2. How often do you deploy, and how long does it take?
3. When something breaks in production, how do you find out?
4. What is your current uptime, and do you have an SLA commitment?
5. Is your infrastructure defined in code, or configured manually?
6. What does your monitoring and alerting stack look like?
7. Do you run security scanning in your pipeline?
8. What was your last significant incident, and what caused it?
9. What is your cloud spend, and is it trending in a way that concerns you?
10. Do you have DevOps or SRE people internally, or does this fall to developers?
11. What compliance requirements do you carry?
12. What would need to be true for you to consider this urgent?

## Recommended CTA

Primary: **Scoped infrastructure or reliability assessment** (paid, per `pricing-public.md` policy — never free). Secondary: **15-minute call** if the prospect prefers to start there.

## Sequence Strategy (Apollo Multichannel)

Five-step Apollo multichannel sequence combining automated emails and high-touch LinkedIn tasks:

| Step | Type | Timing | Purpose & Custom Field Integration |
|---|---|---|---|
| Step 1 | `auto_email` | Day 1 | Personalized body using `{{Personalised Email}}` (body only; salutation and signature managed in sequence) + low-friction CTA. |
| Step 2 | `linkedin_step_connect` | Day 3 (+2d) | LinkedIn connection request task referencing `{{Company Trigger}}` (no pitch, no Zediant mention). |
| Step 3 | `auto_email` | Day 6 (+3d, Threaded) | Threaded follow-up dynamically referencing `{{Pain Point}}` (cloud reliability & DevOps spend). |
| Step 4 | `linkedin_step_message` | Day 9 (+3d) | LinkedIn message task upon connection referencing `{{Pain Point}}` with conversational follow-up. |
| Step 5 | `auto_email` | Day 13 (+4d, Threaded) | Technical proof point / low-pressure breakup referencing `{{Pain Point}}`. |

## Common Objections

| Objection | Response direction |
|---|---|
| "Our problem is application code, not infrastructure." | Confirm at discovery; if true, redirect to C1 or C5 rather than force-fitting this campaign |
| "We already have a DevOps engineer." | Ask about the ratio of maintenance vs. new capability work — one person rarely covers both at scale |
| "We need 24/7 coverage." | Do not commit without confirming staffing; escalate |
| "Migration is too risky." | Reference incremental, non-disruptive migration patterns and the specific case study proof point |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Recipient's morning, local time |
| Cadence | 4 emails over 12–14 days |
| Channels | LinkedIn connection Day 3, message Day 8 (manual) |
| On reply | Same-day |
| No reply | Follow-Up Later; re-engage after the next public incident or growth signal |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline |
| Meeting rate | Contributes to 15–30 discovery meetings/month |
| Assessment engagements booked | Leading indicator — assessments convert to delivery |
| Qualified opportunities | Confirmed infrastructure pain with allocated budget |

## Campaign Priority

**MEDIUM-HIGH.** Strong technical differentiation and a nameable reference client, but a narrower buying trigger (incident- or migration-driven) than C1 or C2.

## Related Services

`services.md` → Platform Engineering, Cloud & DevOps · Enterprise Custom Development · QA & Test Automation

## Related Case Studies

`case_studies.md` → Primary: CS-04 (11Wickets Scalability & Performance Optimisation — nameable, strongest fit). Secondary: CS-06 (Team Augmentation for Automotive Software — DevOps/CI-CD/disaster-recovery work).

## Related ICPs

`icp.md` → ICP 2 (SaaS Companies) · ICP 3 (Product Companies), infrastructure-driven segment

## AI Selection Rules

Choose C3 when:

- The stated problem is deployment, reliability, scaling, or cloud cost — not a missing product feature
- The buying signal is an outage, DevOps/SRE hiring, or a cloud migration announcement
- The contact is CTO, VP Engineering, Head of Infrastructure, DevOps Lead, or CIO

Choose a different campaign when:

- The need is building new product capability → **C1**
- The need is pure engineering capacity, not infrastructure expertise → **C2**
- The need is connecting systems or data exchange → **C4**
- The need is legacy application modernisation rather than infrastructure → **C5**

---

# C4 — Middleware & API Integration (ZCoupler)

**Daily limit:** 30 · **Status:** Draft

## Campaign Objective

Win organisations whose systems don't talk to each other — dealer networks, multi-store retailers, logistics operators, and any business where an acquisition or platform sprawl has created disconnected data. This is Zediant's most differentiated technical specialism and its strongest documented proof point.

## Business Situation

Select this campaign when the prospect's problem is explicitly about data exchange between systems — DMS, CRM, ERP, POS — rather than about a single application. Unlike C1/C2/C3/C5, this campaign can open with proof rather than proposition: the DMS middleware work is production evidence across three regions.

## Target ICP

| Dimension | Profile |
|---|---|
| Industries | Automotive and dealer networks (primary), retail and multi-store, logistics, e-commerce, finance, manufacturing, healthcare |
| Company size | 50+ employees; any organisation running multiple systems |
| Decision makers | CIO, IT Manager, CTO, Head of Operations, Digital Transformation Manager, Enterprise Architect |

Cross-reference: `icp.md` → ICP 4 (Automotive & Dealer Networks) · ICP 7 (Logistics & Supply Chain).

## Business Problems

- Multiple systems hold fragmented data with no consolidated view
- Legacy applications cannot exchange data with modern cloud systems
- Manual reconciliation between systems consumes staff time and introduces errors
- No real-time synchronisation across the estate
- Order and inventory data inconsistent across stores or channels
- Reporting impossible across system boundaries

## Buying Signals

- Recent acquisition creating duplicate systems
- New ERP or CRM implementation
- Multi-store or franchise expansion
- Regulatory reporting requirement spanning systems
- Public complaints about data accuracy
- Hiring for integration or data engineering roles

## Disqualification Signals

- Requires integration with a proprietary system the client cannot grant access to
- Expects a fixed price before source-system discovery
- Source data quality so poor that integration cannot deliver value without a separately funded cleansing programme
- Looking for an off-the-shelf iPaaS product (Salesforce-to-mainstream-SaaS) rather than engineered integration — see `competitors.md` → Category 8, qualify on whether a pre-built connector already exists
- No internal system owners available

## Recommended Services

Integration & Middleware Engineering (primary). Data Engineering & Analytics routes here as a secondary fit where the driver is reporting/consolidation rather than AI readiness. See `services.md`.

## Value Proposition

An integration layer — Zediant Middleware — that standardises, enriches, and validates data in transit between systems that were never designed to talk to each other, built as a repeatable pattern rather than a bespoke one-off.

## Messaging Angle

Lead with the **specific systems that don't talk to each other**, named precisely. This is the one campaign where Zediant can open with proof rather than proposition.

Effective frame: *"Every dealer runs a different DMS and none of them talk to each other."*

**Do not use "ZCoupler" in outbound copy** — see the open item above. Refer to the capability as "Zediant Middleware" or "integration and middleware engineering."

## Recommended Email Tone

**Technical** for CTO/Enterprise Architect audiences. **Executive and consultative** for CIO/IT Director audiences. Select tone by persona, not by a fixed campaign default.

## Personalization Opportunities

- Named systems in use (ERP, CRM, DMS) visible in job posts or case studies
- Acquisition or merger activity creating duplicate systems
- Integration or API announcements
- Job posts naming legacy technologies
- Customer complaints or reviews naming a missing feature or data-accuracy problem

## Discovery Questions

1. Which systems need to talk to each other, and which are the sources of truth?
2. How does data move between them today?
3. How much manual effort goes into moving or reconciling that data weekly?
4. How current does the data need to be — real time, hourly, daily?
5. Do those systems expose APIs, and do you have documentation?
6. Do you control those systems, or are they vendor-managed?
7. How many duplicate or conflicting records do you estimate you have?
8. What reporting do you need that you cannot produce today?
9. Have you attempted this integration before? What blocked it?
10. Who internally owns each of these systems?

## Recommended CTA

Primary: **Technical consultation, 20–30 minutes.** Secondary: **Integration assessment** (paid, scoped). **Never offer a free POC** — internal policy explicitly prohibits it.

## Sequence Strategy (Apollo Multichannel)

Five-step Apollo multichannel sequence combining automated emails and high-touch LinkedIn tasks:

| Step | Type | Timing | Purpose & Custom Field Integration |
|---|---|---|---|
| Step 1 | `auto_email` | Day 1 | Personalized body using `{{Personalised Email}}` (body only; salutation and signature managed in sequence) + low-friction CTA. |
| Step 2 | `linkedin_step_connect` | Day 3 (+2d) | LinkedIn connection request task referencing `{{Company Trigger}}` (no pitch, no Zediant mention). |
| Step 3 | `auto_email` | Day 6 (+3d, Threaded) | Threaded follow-up dynamically referencing `{{Pain Point}}` (middleware & real-time sync). |
| Step 4 | `linkedin_step_message` | Day 9 (+3d) | LinkedIn message task upon connection referencing `{{Pain Point}}` with conversational follow-up. |
| Step 5 | `auto_email` | Day 13 (+4d, Threaded) | Technical proof point / low-pressure breakup referencing `{{Pain Point}}`. |

## Common Objections

| Objection | Response direction |
|---|---|
| "We already have a vendor." | This client's own vendor could not solve the DMS problem — Zediant was the specialist layer beneath |
| "You won't understand our systems." | Name the specific platforms (ERA, CDK, Pentana are documented examples) — domain knowledge is demonstrable |
| "Integration projects always fail." | This one became a product other dealers adopted |
| "We're evaluating an iPaaS platform." | Qualify whether a connector exists for their specific systems — if legacy or industry-specific, engineering is genuinely the better answer |
| "The DMS vendor won't give us API access." | Real constraint — qualify early, it can block the entire engagement |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Recipient's morning, local time |
| Cadence | 4 emails over 12–14 days, expect longer overall cycle |
| Channels | LinkedIn connection Day 3, message Day 8 (manual) |
| On reply | Same-day, routed internally by topic (technical vs. commercial) |
| No reply | Follow-Up Later; re-engage on acquisition, migration, or end-of-life signals |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline |
| Assessment engagements booked | Leading indicator for this campaign |
| Qualified opportunities | Named system or feature with confirmed budget |
| Pipeline generated | Among the highest average deal values across the five campaigns |
| Vertical depth | Case studies added in automotive, logistics, and manufacturing |

## Campaign Priority

**HIGH.** Carries Zediant's most differentiated capability and its strongest documented evidence, though with longer cycles than C1/C2.

## Related Services

`services.md` → Integration & Middleware Engineering · Data Engineering & Analytics · Enterprise Custom Development

## Related Case Studies

`case_studies.md` → Primary: CS-01 (Middleware Integration for Multiple Large DMS — highest priority), CS-05 (Real-Time Executive Dashboards — Diamond Professional Consultants / Zakaa Innovation Hub, confirmed identity). Secondary: CS-02 (Wholesale Parts CRM), CS-03 (Lubricant Recommendation & Equipment Maintenance Application), CS-08 (Sitecore CMS Multisite Platform).

## Related ICPs

`icp.md` → ICP 4 (Automotive & Dealer Networks) · ICP 7 (Logistics & Supply Chain)

## AI Selection Rules

Choose C4 when:

- The stated problem is explicitly about systems not exchanging data
- The prospect mentions DMS, ERP, CRM, or POS integration by name
- An acquisition has created duplicate systems
- The contact is CIO, IT Director, CTO, or Enterprise Architect

Choose a different campaign when:

- The need is product development rather than integration → **C1**
- The need is pure engineering capacity → **C2**
- The need is infrastructure/deployment reliability rather than data exchange → **C3**
- The need is broader legacy application modernisation, of which integration is only one part → **C5**

---

# C5 — Enterprise Custom Development & Modernization

**Daily limit:** 30 · **Status:** Draft

## Campaign Objective

Win established, non-VC-funded product companies and enterprises that need a defined slice of the roadmap built externally, or that are carrying legacy systems requiring modernisation. This campaign carries Zediant's highest average deal value and its deepest legacy-stack differentiation.

## Business Situation

Select this campaign when a company has a proven product and real revenue but a specific body of work — a deprioritised feature, a legacy system nobody can safely touch, or a modernisation programme — that nobody internal is free to own. Unlike C1, funding is not the trigger; a concrete unbuilt or unmodernised thing is.

## Target ICP

| Dimension | Profile |
|---|---|
| Industries | Software product companies, automotive and dealer systems, manufacturing, logistics, fintech, retail technology, enterprise platforms |
| Company size | 20–500+ employees |
| Growth stage | Established, profitable or near-profitable, bootstrapped or listed |
| Countries | Australia (primary), UAE (primary) |
| Decision makers | CTO, Head of Engineering, CIO, IT Director, Head of Product, Enterprise Architect, Digital Transformation Manager |

Cross-reference: `icp.md` → ICP 3 (Product Companies, CTO-Led) and the relevant vertical ICPs (4, 6, 7) where the driver is modernisation rather than integration specifically.

## Business Problems

- Specific roadmap items consistently deprioritised for lack of capacity
- Legacy product requiring maintenance while a new version is built
- Systems that cannot be safely modified due to lost institutional knowledge
- Unsupported technology stacks creating security exposure
- Every hire scrutinised because there is no funding cushion
- Escalating maintenance cost consuming the engineering budget

## Buying Signals

- Actively outsourcing specific features — the defining signal
- Product v2 or rebuild announced
- End-of-life or end-of-support notice on a platform
- Failed security audit or auditor finding
- Acquisition requiring product or system consolidation
- Cloud migration mandate from the board
- Inability to hire for the legacy stack

## Disqualification Signals

- No engineering team at all
- Product is entirely third-party or white-labelled
- Requires embedded, firmware, SCADA, or industrial control software
- Requires deep AI/ML research
- Requires 50+ engineers ramped immediately
- Procurement demands a named-brand systems integrator
- Fixed-price demand on an undocumented legacy estate
- **Expects free POC or unpaid tender documentation** — explicitly prohibited by internal policy

## Recommended Services

Enterprise Custom Development and Legacy Modernisation (both primary — Legacy Modernisation is documented as "usually within Enterprise Custom Development"). Cross-sells: Integration & Middleware Engineering, Platform Engineering & Cloud DevOps, Dedicated Engineering Pods. See `services.md`.

## Value Proposition

A team that owns a defined slice of the roadmap end-to-end, or safely modernises a legacy system, without disturbing internal priorities — backed by integration and modernisation depth most firms of Zediant's size do not have.

## Messaging Angle

Lead with the **specific unbuilt or unmodernised thing**. This buyer knows exactly which feature has been pushed back four quarters, or which system nobody dares touch.

For bootstrapped companies, cost-efficiency framing outperforms speed framing — every hire is scrutinised because there is no funding cushion.

Effective frames:
- Product: *"If there's a roadmap item that keeps slipping because nobody's free to own it, that's the conversation worth having."*
- Legacy: *"It works, but nobody dares change it — what happens if the person who understands it leaves?"*

## Recommended Email Tone

**Technical** for CTO and architect audiences. **Executive and consultative** for CIO and IT Director audiences. Select by persona, not campaign default.

## Personalization Opportunities

- Product roadmap statements or public changelog
- Named legacy systems visible in job posts or case studies
- Acquisition or merger activity
- Job posts naming legacy technologies (Java EE, .NET Framework, classic ASP.NET)
- Vendor end-of-life announcements affecting their stack
- Conference talks or engineering blog posts by the CTO

## Discovery Questions

1. What is on the roadmap that keeps getting deprioritised, or which system can't be touched?
2. How long has it been that way?
3. What does not addressing it cost you — revenue, churn, security exposure?
4. Are you already outsourcing any development? To whom, and how is it going?
5. What is the age and stack of the system in question?
6. Is anyone still with you who built it? What documentation exists?
7. Can this be done incrementally, or does it need a cutover?
8. What is your tolerance for downtime?
9. What proportion of engineering time goes to maintaining what exists?
10. Who owns the decision on an external partner, and what is the budget approval process?

## Recommended CTA

Primary: **Technical consultation, 20–30 minutes.** Secondary: **Modernisation or feature-scoping assessment** — paid or discounted, never free. Tertiary: **Architecture review.**

## Sequence Strategy (Apollo Multichannel)

Five-step Apollo multichannel sequence combining automated emails and high-touch LinkedIn tasks:

| Step | Type | Timing | Purpose & Custom Field Integration |
|---|---|---|---|
| Step 1 | `auto_email` | Day 1 | Personalized body using `{{Personalised Email}}` (body only; salutation and signature managed in sequence) + low-friction CTA. |
| Step 2 | `linkedin_step_connect` | Day 3 (+2d) | LinkedIn connection request task referencing `{{Company Trigger}}` (no pitch, no Zediant mention). |
| Step 3 | `auto_email` | Day 6 (+3d, Threaded) | Threaded follow-up dynamically referencing `{{Pain Point}}` (strangler pattern & monolithic rewrite risks). |
| Step 4 | `linkedin_step_message` | Day 9 (+3d) | LinkedIn message task upon connection referencing `{{Pain Point}}` with conversational follow-up. |
| Step 5 | `auto_email` | Day 13 (+4d, Threaded) | Technical proof point / low-pressure breakup referencing `{{Pain Point}}`. |

## Common Objections

| Objection | Response direction |
|---|---|
| "Our product is too complex for an outside team." | Start with a defined peripheral module before core work |
| "Knowledge transfer would take too long." | Pod includes a tech lead; AI-generated documentation accelerates onboarding |
| "We can't afford it without funding." | Compare against fully-loaded permanent cost; flexible scale-down protects downside |
| "We tried outsourcing and it failed." | Ask specifically what failed; differentiate on senior-only staffing and pod structure |
| "We'd need a POC first." | Offer fixed-cost discounted scoped work, never free |
| "Nobody understands that system anymore." | Speak to Zediant's general legacy/acquired-system recovery approach. No case study is currently designated as approved C5 evidence — see Related Case Studies below; do not cite CS-06 as a C5 proof point. |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Recipient's morning, local time |
| Cadence | 4 emails over 12–14 days; expect longer overall cycle |
| Channels | LinkedIn connection Day 3, message Day 8 (manual) |
| On reply | Same-day, routed internally by topic (technical vs. commercial) |
| No reply | Follow-Up Later; re-engage on acquisition, migration, or end-of-life signals |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline |
| Assessment engagements booked | Leading indicator — assessments convert to delivery |
| Qualified opportunities | Named system or feature with confirmed budget |
| Pipeline generated | Highest average deal value across the five campaigns |
| Vertical depth | Case studies added in automotive, logistics, and manufacturing |

## Campaign Priority

**HIGH.** Highest deal values in the portfolio and the deepest legacy-stack differentiation, offset by the longest sales cycles of the five campaigns.

## Related Services

`services.md` → Enterprise Custom Development · Legacy Modernisation · Integration & Middleware Engineering · Platform Engineering & Cloud DevOps

## Related Case Studies

**None.** `case_studies.md`'s Campaign-to-Case-Study Mapping explicitly states C5 has no assigned case study and flags this as an open DATA CONFLICT: none of CS-01, CS-06, or CS-08's own documented business problems independently establish Enterprise Custom Development & Modernization as their campaign fit, even as a secondary or structural reference. Do not cite CS-01, CS-06, or CS-08 — or any other case study — as C5 evidence, structural parallel, or proof point of any kind until this conflict is resolved by a human and reflected in `case_studies.md`.

## Related ICPs

`icp.md` → ICP 3 (Product Companies, CTO-Led) · ICP 4 (Automotive) · ICP 6 (Manufacturing) · ICP 7 (Logistics)

## AI Selection Rules

Choose C5 when:

- The company sells its own product but is not VC-funded at seed–Series B stage
- A specific feature, legacy system, or modernisation need is identifiable
- The signal is a deprioritised roadmap item, an end-of-life notice, an audit finding, or an acquisition — not funding or an open hiring role
- Contact is CTO, CIO, IT Director, or Enterprise Architect
- Headcount is 20–500+

Choose a different campaign when:

- Funded seed–Series B SaaS with roadmap/scaling pressure → **C1**
- The dominant signal is an open engineering role → **C2**
- The core need is infrastructure/deployment reliability rather than the application itself → **C3**
- The core need is specifically connecting systems rather than broader modernisation → **C4**
- Enterprise requiring 12+ engineers or heavy procurement → **do not sequence; escalate to a human**

---

# DOCUMENT CONTROL

| Attribute | Value |
|---|---|
| Document | `campaigns.md` |
| Purpose | Campaign selection, messaging, and routing reference for Zediant AI agents |
| Taxonomy | Service-based, C1–C5 only |
| Current campaigns | C1–C5 only. No sixth campaign and no other campaign identifiers exist. |
| Retired campaign taxonomy | None referenced. Any prior letter-based campaign structure has been fully retired and does not appear anywhere in this document. |
| Sending platform | **Apollo Sequences** (native email + LinkedIn multichannel execution) |
| What changed in this revision | **Apollo Outreach Migration (September 2026):** Saleshandy retired as sending platform. All sequences (C1–C5) migrated to Apollo's native multichannel environment (6 steps: automated emails + LinkedIn connection and message tasks). Integrated Apollo custom field `Personalised Email` (`6aa79177f203040018e0af9d`) for full first-touch email body generated by Google Antigravity. Sequence enrollment resolved dynamically by `apollo-distribution`. BDM approval gate enforced via `Approval Status = "Approved for Outreach"`. |
| Known open items | "ZCoupler" naming still unconfirmed as an approved public product name · mailbox warm-up status concluding Sept 17, 2026. |
| Cross-references updated in this pass | `icp.md`, `services.md`, `case_studies.md`, `competitors.md` — campaign references use only the current C1–C5 taxonomy |

