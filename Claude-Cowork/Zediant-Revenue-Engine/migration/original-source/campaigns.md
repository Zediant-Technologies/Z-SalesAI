# Overview

This document governs outbound campaign selection, messaging, and routing for Zediant Technologies. It is the reference an AI agent consults to answer: *given this lead, which campaign, why, from which mailbox, with what angle?*

**Zediant's campaign taxonomy is service-based.** There are exactly five live campaigns, C1–C5, each named for and organised around one of Zediant's core service lines. A lead enters the single campaign matching the service it most plausibly needs. This document supersedes and fully replaces the earlier intent-based List A–E taxonomy and the sending platform it ran on. **No document, field, or agent should reference "List A" through "List E" or the prior sending platform by name anywhere.** Where those names still appear in other Zediant knowledge files, treat it as a defect to be corrected against this document, not as a valid alternative structure.

## Migration notice — read before using this document

| Item | Before | Now |
|---|---|---|
| Taxonomy | Intent-based: List A (Agency Capacity Extension), List B (SaaS Scaling), List C (SaaS Hiring Signal), List D (Product Feature Outsourcing), List E (Referral / Partner Sourced) | Service-based: **C1–C5**, one per core service line |
| Sending platform | (prior platform, retired) | **Saleshandy** |
| Sequence ID handling | Prior-platform campaign IDs hardcoded in this document | **Not recorded here.** `campaign-selection` outputs a campaign name (C1–C5); `saleshandy-distribution` resolves that name to a live Saleshandy sequence ID by title match at push time. This document intentionally stays ID-agnostic so it never goes stale if a sequence is recreated. |
| CRM picklist | `Lead_Campaign_Category` used List-letter values requiring a mismatch-mapping table | `crm-update` v5.1+ writes C1–C5 names directly — the old mismatch table is retired along with it |

**Why service-based, not intent-based.** The old taxonomy grouped prospects by buying situation (an agency at capacity, a funded SaaS company, a company hiring) and let one service — usually a pod — get sold five different ways. The new taxonomy is simpler and matches what's actually live in Saleshandy: one campaign per service, and campaign selection is a question of *which service does this prospect most plausibly need*, not *which situation are they in*. A single prospect's underlying business situation still shapes messaging and case study choice within a campaign — that reasoning hasn't disappeared, it has moved into each campaign's own Messaging Angle and Personalization sections below.

**Historical mapping — for context only, not a live routing rule.** If older material or a human references the retired List letters, this is what they corresponded to. Do not use this table to route anything; always route by service need per the AI Selection Rules under each campaign below.

| Retired list | Was about | Now maps to |
|---|---|---|
| List A — Agency Capacity Extension | Agencies needing delivery capacity | **C2** (the underlying need was pods/staff augmentation) |
| List B — SaaS Scaling | Funded SaaS with roadmap pressure | **C1** primarily (the underlying service pitched was AI-Enabled Product Engineering); **C2** where the specific need was capacity rather than platform build |
| List C — SaaS Hiring Signal | Companies with open engineering roles | **C2** (staff augmentation / pods covering a hiring gap) |
| List D — Product Feature Outsourcing | CTO-led product companies needing a defined roadmap slice built | Split by the actual technical need: **C3** (platform/cloud work), **C4** (integration/middleware/DMS work), or **C5** (enterprise/legacy work) |
| List E — Referral / Partner Sourced | Warm introductions | Not a campaign anymore. See **Referral-sourced leads** under Non-negotiable operating rules — a referral still lands in whichever of C1–C5 matches the need surfaced at discovery. |

## Non-negotiable operating rules

These override every other instruction in this document.

| Rule | Detail |
|---|---|
| **Never activate a campaign** | All five Saleshandy sequences (C1–C5) are Draft. Activation is an explicit human (BDM) action in Saleshandy. No automated task may change sequence status. |
| **BDM approval gate** | No lead enters a campaign without `Lead_Status = "Approved for Outreach"` in Zoho CRM. Non-negotiable. `saleshandy-distribution` uses this as its sole eligibility check. |
| **Resolve sequences by name, never hardcode an ID** | `saleshandy-distribution` resolves a campaign name (C1–C5) to a live Saleshandy sequence by title match at push time. This document records campaign names, senders, and daily limits — never a sequence ID. |
| **Saleshandy sends, Apollo sources** | Apollo is sourcing and enrichment only. Apollo sequences must never be used for outreach. **Saleshandy is the sole sending platform.** The prior sending platform is fully retired — Zediant no longer holds an active outbound relationship with it. |
| **Mailbox warm-up** | Confirm current warm-up status directly in Saleshandy before assuming any mailbox is ready to send. This has historically been the primary blocker before the pipeline could go live — do not assume it is resolved without checking. |
| **Four-touch email limit** | Documented deliverability rule: keep email sequences to four touches. Beyond that produces diminishing returns and higher spam-report rates. |
| **Personalise the first line** | Never send a fully generic template. Documented rule across both the LinkedIn and cold email playbooks. |
| **Drop the sequence on reply** | If a prospect replies at any point, stop the sequence and respond as a real conversation the same business day. |
| **One campaign per lead** | Each lead maps to exactly one of C1–C5. If a lead's need genuinely spans two services, pick the dominant one using the AI Selection Rules under that campaign and let cross-sell happen after the relationship starts — do not enrol a lead in two campaigns. |

---

# LIVE CAMPAIGN REGISTRY

| # | Campaign Name | Sender mailbox | Daily limit | Status |
|---|---|---|---|---|
| **C1** | AI-Enabled Product Engineering | rajeev@ | 30 | Draft |
| **C2** | Engineering Pods & Staff Augmentation | manish@ | 30 | Draft |
| **C3** | Platform Engineering & Cloud Modernization | manish@ | 30 | Draft |
| **C4** | Middleware & API Integration (ZCoupler) | pritamjit@ | 30 | Draft |
| **C5** | Enterprise Custom Development & Modernization | rajeev@ | 30 | Draft |

All five sequences confirmed live in Saleshandy, all currently in Draft — queued as an import target but not sending. Draft only blocks sending; approved leads can still be pushed into the prospect list per `saleshandy-distribution`.

## ⚠️ Open items — do not resolve independently

### 1. Sender domain discrepancy — unresolved, flag rather than fix

Every written reference to sender mailboxes across Zediant's knowledge base (this document, `company.md`, `icp.md`) uses the **@zediant.com / @zediant.tech** convention. However, a live Cliq activity log from a completed Scheduler 2 run shows the actual sending mailbox as **rajeev@zedianttechnologies.info**, with a 15/day quota noted at the mailbox level (distinct from the 30/day campaign-level limit shown above).

This is a real, live discrepancy between documented and observed sender domains. **No agent should silently standardise on one or the other.** If a task depends on the exact sender address or the mailbox-level send quota, confirm the current value directly in Saleshandy rather than trusting either source, and escalate the conflict to a human for resolution.

### 2. Sender-to-persona mapping — carry forward from prior audit, unverified against current C1–C5 setup

The table above assigns rajeev@ to C1 and C5, manish@ to C2 and C3, and pritamjit@ to C4. This is inherited directly from the prior service-based sender assignment and has **not been independently re-verified** against Zediant's documented persona-matching guidance:

- **rajeev@** → Founders, CEOs, Managing Directors (founder tone)
- **pritamjit@** → Heads of Delivery, Operations, business leaders (consultative tone)
- **manish@** → CTOs, VP Engineering, Engineering Managers (technical tone)

C4 (Middleware & API Integration) is a technical subject typically owned by a CIO, IT Manager, or Enterprise Architect — assigning it to pritamjit@ (a consultative/business mailbox) rather than manish@ (technical) may be the same mismatch the prior audit flagged for the old middleware campaign. **Flag to a human before activation; do not silently reassign.**

### 3. Send schedule timezone — carry forward, unconfirmed for the current Saleshandy setup

Prior audit found the campaign send schedule defaulted to America/Detroit hours against Australian and UAE prospects. Confirm the actual configured schedule for each of C1–C5 directly in Saleshandy before activation. Target schedule if not yet corrected:

| Target market | Schedule |
|---|---|
| Australia (AEST) | Australia/Sydney, 08:30–16:30, Mon–Fri |
| Australia (AWST/Perth) | Australia/Perth, 08:30–16:30, Mon–Fri |
| UAE | Asia/Dubai, 08:30–16:30, **Sunday–Thursday** |

### 4. "ZCoupler" naming

C4 is officially named **"Middleware & API Integration (ZCoupler)"** — this document uses that name as given. This does **not** authorise using the word "ZCoupler" in outbound messages, proposals, or conversations with a prospect. No source outside the campaign name itself confirms ZCoupler as an approved, publicly usable product name (see `campaigns.md` history and `company.md` → Products, which documents only "Zediant Middleware"). Refer to the capability as **"Zediant Middleware"** or **"integration and middleware engineering"** in any prospect-facing content until a human confirms otherwise.

### 5. Mailbox warm-up status

Not independently re-verified as part of this document's rewrite. Confirm current warm-up status in Saleshandy before assuming any of C1–C5 is ready to activate.

---

# CAMPAIGN FRAMEWORK

## Why service-based

Each campaign now corresponds to exactly one thing Zediant sells: C1 is the AI-Enabled Product Engineering service, C2 is the Dedicated Engineering Pods and Staff Augmentation services together, C3 is Platform Engineering, Cloud & DevOps, C4 is Integration & Middleware Engineering, and C5 is Enterprise Custom Development (including Legacy Modernisation). See `services.md` for full service definitions — this document assumes that layer and builds the outbound motion on top of it.

**Services without their own campaign.** Not every service in `services.md` has a dedicated C1–C5 campaign. Mobile Application Development, Web Application Development, E-commerce & CMS Development, and QA & Test Automation are documented as "usually delivered within a pod" — leads whose stated need is one of these route to **C2**. Data Engineering & Analytics has "limited standalone evidence" and is documented as a cross-sell into Integration work — leads route to **C4** as the primary fit, with **C1** as a secondary fit where the driver is AI-ready data architecture rather than integration. Maintenance & Managed Services, UI/UX Design, and Advisory & Engineering Consulting are not primary outbound motions at all — Maintenance is the natural conversation at the close of a build engagement, Advisory is the low-commitment entry offer available *within* any of C1–C5 rather than a campaign of its own, and UI/UX is a supporting function never sold standalone. Do not create outbound sequences around these three; if a prospect's stated need is genuinely just one of them, use the closest campaign above and route the actual service conversation through discovery.

## Selection principle

Campaign selection follows this order of precedence:

1. **Discovered technical need** — what does the prospect actually need built or extended? This determines the campaign directly, because campaign now equals service.
2. **Referral override** — if the lead is a referral or partner introduction, `campaigns.md`'s prior source-overrides-everything rule still applies to *messaging tone and cadence* (see Referral-sourced leads below), but the lead still enters whichever of C1–C5 matches the discovered need. There is no separate referral campaign anymore.
3. **Persona** — determines which of the three sender mailboxes fits the contact once the campaign is already selected (see the sender-to-persona table under Open Items above).

Vertical industry does **not** drive campaign selection. It drives case study selection and personalisation within the campaign, exactly as before.

## Referral-sourced leads

A referral or partner introduction is still handled differently in tone and cadence than a cold lead, even though it now enters one of C1–C5 rather than a dedicated campaign:

- **Lead with the referrer's name in the first line**, not the campaign's standard messaging angle.
- Use a **two-touch warm sequence** rather than the standard four-touch cold cadence for that lead specifically — a four-touch pursuit of a warm referral reads as pushy and can damage the referrer relationship.
- No pitch in the opening message; propose a short introductory conversation instead.
- **Sender:** override the campaign's default sender with rajeev@ (or the founder-tone mailbox once the domain question above is resolved) regardless of which of C1–C5 the lead is filed under, since a warm introduction expects founder-level warmth, not the campaign's default technical or consultative voice.
- Update the referrer on the outcome regardless of result.

---

# C1 — AI-Enabled Product Engineering

**Sender:** rajeev@ · **Daily limit:** 30 · **Status:** Draft — see the tone-mismatch note below before activating

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

**⚠️ Open tension.** This campaign's sender was changed to rajeev@ (founder tone) while the messaging angle and tone above remain technical (manish@'s documented voice). Per `icp.md`'s sender-persona table, rajeev@ suits Founder/CEO contacts and manish@ suits CTO/VP Engineering contacts — C1 targets both personas. Either write the copy in founder tone to match the sender, or confirm rajeev@ is intended to carry technical messaging for this campaign specifically. Flag to a human before activation rather than resolving silently.

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

## Email Sequence Strategy

Four touches maximum.

| Step | Timing | Purpose |
|---|---|---|
| Email 1 | Day 0 | Name the roadmap-versus-hiring squeeze. Reference the specific funding or scaling signal. Single ask. |
| Email 2 | Day 3–5 | Answer the three questions CTOs always ask: seniority, speed to team, quality ownership. Offer a technical overview instead of a call. |
| Email 3 | Day 7–10 | Direct ask with calendar link, or offer an architecture review as an alternative entry point. |
| Break-up | Day 12–14 | Acknowledge that a healthy hiring pipeline makes this irrelevant. Leave the door open on the specific slipping-roadmap-item frame. |

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
| On reply | Same-day. Route technical questions to manish@; commercial to rajeev@ |
| Escalation | Loop in the Founder early on Hot-tier leads (ICP score 80+) |
| No reply | Follow-Up Later in Zoho; re-engage on the next funding or launch signal |

## Success Metrics

| Metric | Target |
|---|---|
| Reply rate | Establish baseline; no historical data on Saleshandy yet |
| Meeting rate | Contributes to 15–30 discovery meetings/month across all campaigns |
| Qualified opportunities | Funded SaaS with confirmed roadmap gap and named budget |
| Pipeline generated | Larger deals — annualised pod value USD 80,000–150,000+ |
| Strategic contribution | New logos reducing client concentration |

## Campaign Priority

**HIGH.** Named the highest strategic priority internally. Publicly observable signals, founder-level decisions without procurement, best alignment with long-term positioning.

## Related Services

`services.md` → AI-Enabled Product Engineering · Platform Engineering & Cloud DevOps · Data Engineering & Analytics

## Related Case Studies

`case_studies.md` → CS-04 (11Wickets — nameable) · CS-07 (Cryptocurrency Trading Application)

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

**Sender:** manish@ · **Daily limit:** 30 · **Status:** Draft

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

**Consultative** for the agency angle (matches pritamjit@'s documented voice where that mailbox is used for a specific lead). **Technical and direct** for the hiring-gap angle (matches manish@'s documented voice) — this audience is time-poor and reads on mobile between interviews.

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

## Email Sequence Strategy

Four touches maximum.

| Step | Timing | Purpose |
|---|---|---|
| Email 1 | Day 0 | Name the bench-versus-backlog trade-off or the specific open role. Single low-commitment ask. |
| Email 2 | Day 3–5 | Pre-answer the objections this audience always raises (continuity, white-labelling, overlap hours, or hiring-vs-augmenting). Offer case studies or profiles instead of a call. |
| Email 3 | Day 7–10 | Direct ask for 15 minutes, with a calendar link. Reference a specific proof point. |
| Break-up | Day 12–14 | Close the loop without pressure. Invite a "later" reply for re-engagement. |

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

`case_studies.md` → CS-06 (Team Augmentation for Automotive Software) · CS-02 (Wholesale Parts CRM, do not use alongside CS-06 — same client)

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

**Sender:** manish@ · **Daily limit:** 30 · **Status:** Draft

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

Primary: **Scoped infrastructure or reliability assessment** (paid, per `pricing.md` policy — never free). Secondary: **15-minute call** if the prospect prefers to start there.

## Email Sequence Strategy

Four touches maximum.

| Step | Timing | Purpose |
|---|---|---|
| Email 1 | Day 0 | Name the specific reliability, deployment, or cost pain. Single ask. |
| Email 2 | Day 3–5 | Reference a proof point (CS-04 / 11Wickets is the strongest, nameable example). Offer a scoped assessment instead of a call. |
| Email 3 | Day 7–10 | Direct ask with a calendar link. |
| Break-up | Day 12–14 | Acknowledge internal capacity may resolve it. Leave the door open. |

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
| On reply | Same-day, technical questions routed to manish@ |
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

`case_studies.md` → CS-04 (11Wickets Scalability & Performance Optimisation — nameable, strongest fit)

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

**Sender:** pritamjit@ · **Daily limit:** 30 · **Status:** Draft — see sender-persona open item above; verify this mailbox is correct for a technical audience before activation

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

**Technical** for CTO/Enterprise Architect audiences. **Executive and consultative** for CIO/IT Director audiences. Select tone by persona, not by a fixed campaign default — and see the open sender-mailbox question above before assuming pritamjit@ is right for a given contact.

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

## Email Sequence Strategy

Four touches maximum, though this campaign typically runs a longer decision cycle than C1/C2 — expect 2–3 touch rounds over a quarter for larger accounts.

| Step | Timing | Purpose |
|---|---|---|
| Email 1 | Day 0 | Name the specific system disconnect. Demonstrate domain knowledge in the first two lines. |
| Email 2 | Day 3–5 | Proof point — reference CS-01 (Middleware Integration for Multiple Large DMS) by vertical. Pre-empt the ownership/knowledge-transfer objection. |
| Email 3 | Day 7–10 | Offer a scoped assessment rather than a sales call. |
| Break-up | Day 12–14 | Acknowledge internal capacity may resolve it. Position the assessment as available whenever priorities shift. |

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
| On reply | Route technical detail to manish@; commercial to rajeev@ or pritamjit@ per the confirmed persona |
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

`case_studies.md` → CS-01 (Middleware Integration for Multiple Large DMS — highest priority) · CS-05 (Zakaa Executive Dashboards, subject to the oil-and-gas/consultancy discrepancy noted in case_studies.md)

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

**Sender:** rajeev@ · **Daily limit:** 30 · **Status:** Draft

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

## Email Sequence Strategy

Four touches, though expect a longer overall cycle than C1/C2 — 2–3 touch rounds over a quarter is typical for larger accounts.

| Step | Timing | Purpose |
|---|---|---|
| Email 1 | Day 0 | Name the specific unbuilt feature or legacy risk. Demonstrate domain knowledge in the first two lines. |
| Email 2 | Day 3–5 | Proof point by vertical. Pre-empt the ownership and knowledge-transfer objection. |
| Email 3 | Day 7–10 | Offer a scoped assessment rather than a sales call. |
| Break-up | Day 12–14 | Acknowledge internal capacity may resolve it. Position the assessment as available whenever priorities shift. |

## Common Objections

| Objection | Response direction |
|---|---|
| "Our product is too complex for an outside team." | Start with a defined peripheral module before core work |
| "Knowledge transfer would take too long." | Pod includes a tech lead; AI-generated documentation accelerates onboarding |
| "We can't afford it without funding." | Compare against fully-loaded permanent cost; flexible scale-down protects downside |
| "We tried outsourcing and it failed." | Ask specifically what failed; differentiate on senior-only staffing and pod structure |
| "We'd need a POC first." | Offer fixed-cost discounted scoped work, never free |
| "Nobody understands that system anymore." | Reference CS-06's reverse-engineering and month-one developer's manual outcome |

## Recommended Follow-up Strategy

| Element | Approach |
|---|---|
| Timing | Recipient's morning, local time |
| Cadence | 4 emails over 12–14 days; expect longer overall cycle |
| Channels | LinkedIn connection Day 3, message Day 8 (manual) |
| On reply | Route technical detail to manish@; commercial to rajeev@ |
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

`case_studies.md` → CS-06 (Team Augmentation for Automotive Software — 70%→93% test coverage, 3+ year relationship) · CS-08 (Sitecore CMS Multisite) · CS-01 (Middleware Integration, where modernisation is the framing rather than pure integration)

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
| Sending platform | Saleshandy |
| What changed in this revision | Full replacement of the List A–E intent-based taxonomy with the service-based C1–C5 taxonomy. All references to the prior sending platform removed — Saleshandy is now the sole documented sending platform. Sequence IDs are no longer recorded in this document (resolved by name at push time, per `campaign-selection` and `saleshandy-distribution`). |
| Known open items | Sender domain discrepancy (@zediant.com/.tech documented vs. @zedianttechnologies.info observed live) — unresolved, flagged for human review · sender-to-persona mapping for C1–C5 not independently re-verified against documented persona rules · send schedule timezone not independently re-verified for the current Saleshandy setup · "ZCoupler" naming still unconfirmed as an approved public product name · mailbox warm-up status not independently re-verified |
| Cross-references updated in this pass | `icp.md`, `services.md`, `case_studies.md`, `competitors.md` — all List A–E references replaced with C1–C5 per the mapping in this document |

