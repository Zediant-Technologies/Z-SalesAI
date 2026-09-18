# 01 — Page Audit

Status: **Read-only audit. No website files were modified.** Method: direct live-page fetch of every URL in scope (no source-code repository is connected to this session — see note in the Introduction). All findings are dated 2026-08-22 unless otherwise noted.

## Introduction — how this audit was conducted

No website source-code repository was available in this session (the connected folder is a sales/content-operations project folder, not a code repo). Per this task's own instruction to inspect "the complete Zediant website source code," this is flagged as a **DATA GAP**: framework, component structure, and routing were instead determined by direct, unauthenticated fetch of every live public page — the same read-only method used in this project's prior technical/on-page audits (`seo/audits/technical/initial_technical_audit.md`, `seo/strategy/gate-1-decision-pack.md`). This is sufficient to audit rendered content, headings, links, and metadata, but cannot inspect component reuse, build configuration, or server-side logic directly. If actual repository access becomes available, re-run Section 3 below.

## Section 3 — Site architecture inspection

- **Framework:** Astro (confirmed via `generator: Astro v4.5.10` meta tag on multiple pages, including the 404 page). Statically generated site.
- **Routing:** Clean path-based routing matching the approved nav structure exactly (`/`, `/services/*`, `/about-us/*`, `/case-studies/*`, `/blogs/*`). No query-string or hash-based routing observed.
- **Canonical tags:** Present and self-referencing on pages checked (e.g. `/services/dedicated-engineering/` canonical = `https://zediant.com/services/dedicated-engineering/`, non-www). Not individually re-verified on all 44 pages in this pass — treat as LIKELY consistent, not CONFIRMED site-wide.
- **Structured data (schema.org/JSON-LD):** No JSON-LD blocks were detected in the fetched/rendered content on the homepage. Only basic Open Graph (`og:type`, `og:image`) and Twitter Card meta tags were found. **CONTENT/EVIDENCE GAP** — no Organization, Service, Article, or BreadcrumbList structured data was observed anywhere in this pass. This cannot be fully confirmed without raw HTML/view-source inspection (WebFetch renders to markdown), so this is LIKELY, not certain.
- **Sitemap implementation:** `sitemap.xml` re-fetched 2026-08-22 — **unchanged since the 2026-08-19/20 discovery passes.** Still 22 URLs, still `lastmod: 2024-08-21` on every entry, still lists dead/legacy URLs, still uses short case-study slugs that 404 live, still omits the blog section entirely. See "Sitemap detail" below.
- **Robots.txt:** Unchanged — `User-agent: *`, empty `Disallow`, sitemap declared. All crawling permitted.
- **Blog architecture:** `/blogs/` hub renders only **7 of the site's ~20 live blog posts**, with no pagination — `/blogs/2/` returns a 404. The other 13 posts are live, fetchable by direct URL, and (per the LinkedIn cross-post link every article carries) externally discoverable, but **are not linked from the blog hub and have no on-site path leading to them.** This is a significant, previously undocumented finding — see `04-internal-linking-audit.md`.
- **Case study architecture:** `/case-studies/` hub correctly lists and links all 10 live case studies. Each case study page links only to 2–3 "Related" case studies — **none link to any `/services/*` page.**
- **Internal linking architecture:** Every page shares an identical global header (4 About links, 4 Service links, Case Studies, Blogs) and footer — this guarantees every page is at minimum reachable from every other page via chrome navigation. The gap is *contextual, in-body* linking (case studies → services, services → case studies, blog → blog), covered in `04-internal-linking-audit.md`.

### Sitemap detail (re-verified 2026-08-22, matches prior audit exactly)

22 URLs, `lastmod: 2024-08-21` on all of them. Contains: `/services/ecommerce-business`, `/services/digital-presence`, `/services/saas-development`, `/services/middleware-integration`, `/services/cloud-security`, `/services/build-your-team` (5 of these 6 are LEGACY/obsolete pages per `gate-1-decision-pack.md`), plus `/about-us/team-culture` and `/about-us/how-we-work` — **two URLs that do not correspond to any page in the current live navigation** (current About nav is Who We Are / Engineering Excellence / Trust & Compliance / Careers). Whether `team-culture`/`how-we-work` still resolve live was not re-tested in this pass — flagged **UNMAPPED / DATA GAP**, not assumed dead. The sitemap omits all 4 current service pages, all 4 current About pages by their real slugs, the blog section entirely, and uses short case-study slugs (`/case-studies/wholesale`, `/case-studies/wickets`, etc.) that do not match the live long-form slugs and 404 (already confirmed in the prior technical audit).

## Section 5 — SEO Excel mapping to live pages

Every one of the 44 URLs in `seo/content/approved/Zseodata_corrected-Keyword Map.csv` was checked against the live site. Result: **44 of 44 map to a real, live, resolvable page. Zero UNMAPPED.** (Two rows — `/about-us/our-story/` and `/privacy-policy/`, `/terms-of-use/` — were spot-checked via the homepage's footer/nav links rather than individually re-fetched in full in this pass; treat their detailed content audit as LIKELY-current rather than independently re-verified line-by-line.)

No page beyond these 44 was discovered as commercially significant during this pass. The 13 orphaned blog posts are already among the 44 (they are documented in the approved keyword file even though they're unreachable via on-site navigation) — this is a linking problem, not a mapping problem.

## Master Audit Table

Legend — H1 Assessment / Content Assessment: **Strong / Good / Partial / Weak / Misaligned**. Search Intent satisfaction: **PASS / PARTIAL / FAIL**.

| URL | Page Type | Primary Keyword (approved) | Search Intent Satisfied | H1 Assessment | Content Assessment | Secondary Topic Coverage | Positioning | Internal Linking | CTA | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|
| `/` | Homepage | product engineering services | PARTIAL | Partial — H1 "AI-Enabled Dedicated Engineering Partner" leads with Pods/AI, not "product engineering" | Good breadth (4 services, verticals, tech stack, testimonials) but includes leftover "Ready to ditch ecommerce headaches?" section inconsistent with current 4-service positioning | Partially covered — AI-enabled and Pods get strong presence; Platform Engineering and Enterprise Custom Development are comparatively thin on the homepage | Partial — strong AI/Pods framing, but ecommerce-era section and generic "Trusted Globally" language dilute the "product engineering partner" positioning | Good — links to all 4 service pages, About pages, 4 case studies (not all 10) | Multiple, consistent (#contact anchor) | **OPTIMIZE** |
| `/services/ai-enabled-product-engineering/` | Service (current) | AI-enabled product engineering company | PARTIAL | Partial/Misaligned — H1 "Build Intelligent Platforms with AI-Ready Architectures" reads as platform engineering, not product engineering | Good technical depth but heavy overlap in structure/claims with Platform Engineering page | Covers SaaS Platform Development, AI Integration, Data-Driven Systems, API-First — all present but generic-AI-agency-flavored in places | Weak — content skews toward "AI-first engineering firm" / generic AI-development claims rather than "AI-assisted delivery methodology applied to product engineering," the distinction `policies/claims-and-compliance.md` §5 explicitly requires | No case studies linked at all | "Build Your AI-Enabled Platform Today" — fine, generic | **REWRITE** (H1 + differentiation from Platform Engineering) |
| `/services/dedicated-engineering/` | Service (current, CANONICAL Pods page) | dedicated engineering pods | PASS | Strong — H1 explicitly uses "Dedicated Engineering Pods" | Strong — pod tiers, team composition, named roles (Strategist/Engine/Gatekeeper/Orchestrator) are genuinely specific and differentiated | Well covered — recruitment lag, backlog debt, quality erosion, 3 pod tiers | Good — "extension of your internal engineering organization," "outcome-focused," explicitly not commodity staffing | No case studies linked (Team Augmentation for Automotive Software, CS-06, would be a strong fit) | "Talk to Our Engineering Experts" | **OPTIMIZE** (add case-study proof; fix SOC2 wording) |
| `/services/platform-engineering/` | Service (current) | platform engineering and cloud DevOps company | PASS | Good — H1 covers "Secure, Scalable, and AI-Powered Platform Engineering" | Good technical specificity (Terraform, CI/CD, IaC, microservices decomposition) | Well covered — availability, DevSecOps, observability, multi-region | Good — closest of the 4 pages to a genuinely distinct positioning | No case studies linked (11Wickets, CS-04, is a strong, directly-relevant fit and currently unused here) | "Modernize Your Platform Now" | **OPTIMIZE** (add CS-04 case study; fix "99.99% availability" claim — see below) |
| `/services/enterprise-custom-development/` | Service (current) | enterprise custom software development | PARTIAL | Weak — H1 "Bespoke Engineering Solutions for **Public Limited Companies (PLCs)**" narrows the audience far below the page's actual documented ICP (established product companies and enterprises broadly, per `campaigns.md` C5 — not PLCs specifically) | Good depth on legacy modernization, middleware orchestration, high-concurrency | Legacy Modernization is present as an H3, consistent with services.md's "usually within Enterprise Custom Development" structure | Weak on this one point — the PLC framing is a real positioning misalignment, not just an SEO nuance | No case studies linked (several — CS-02, CS-08, CS-09 — would fit) | "Discuss Your Enterprise Project" / "Consult with Our Engineering Experts" | **REWRITE** (H1 audience framing) |
| `/about-us/who-we-are/` | Company / Trust | who is Zediant | PASS | Good — H1 "Engineering the Future of Global Platforms" is brand-appropriate | Good — company overview, differentiators, leadership credentials (Rajeev Jaiswal, 20+ years) | Covers AI-enabled engineering, SOC2, product mindset, senior-led staffing, pod model, global footprint | Good, brand-consistent | Good — links to all core pages | "Talk to Our Engineering Experts" | **OPTIMIZE** (SOC2 wording) |
| `/about-us/engineering-excellence/` | Company | Zediant engineering quality and delivery practices | PASS | Good — H1 "The Zediant Operating System: Where Speed Meets Security" is distinctive and on-brand | Good — genuinely detailed delivery framework (Discovery→Blueprinting→AI-Augmented Dev→QA→DevOps→Optimization) | Well covered; this page is arguably the site's best differentiated content | Good | Good | "Discuss Your Engineering Roadmap Today" | **KEEP** (light SOC2 wording fix only) |
| `/about-us/trust-compliance/` | Company / Trust | SOC 2 Type II aligned software partner | FAIL on the wording requirement specifically | Good — H1 "Enterprise Trust, Built on Security and Compliance" is appropriate | Good structure (SOC2, security framework, regional compliance, risk-reduction) | Well covered | **Critical wording problem** — this is the canonical SOC2/trust page and it states outright "Zediant is a SOC 2 Type II **certified** organization" — the exact non-compliant wording the approved keyword file and `policies/claims-and-compliance.md` §6 both require to be "aligned" | Good | "Talk to Our Security & Engineering Experts" | **OPTIMIZE — wording correction is P0, not cosmetic** |
| `/about-us/careers/` | Company / Recruitment | software engineering careers | PASS | Good — H1 "Don't Just Code. Engineer the Future." | Adequate for recruitment intent | Covers culture, tech stack, career paths | Fine for a recruitment page; one unverifiable claim ("Elite 1% of engineers") flagged below | Good | None specific (implicit via WhatsApp/social) | **KEEP** (flag the "Elite 1%" claim only) |
| `/case-studies/` (hub) | Case Study Hub | Zediant case studies | PASS | Good — simple, functional H1 | Good — all 10 case studies listed with one-line summaries | N/A | Fine | Good hub-level, but **zero links from the hub context into relevant service pages per case study** | "Get your free consultation" | **OPTIMIZE** (add service-page tagging per case study) |
| `/blogs/` (hub) | Blog Hub | product engineering blog | FAIL | Fine as a hub H1 | **Only shows 7 of ~20 live posts; no pagination; most recent post is 14 months old relative to this audit date** | N/A | Weak — topics skew informational/generic, several off-strategy | **Critical gap — 13 live posts are orphaned from this hub, see 04** | "More Details" (single link) | **REWRITE** (content roadmap + fix the missing-posts bug) |
| `/privacy-policy/`, `/terms-of-use/` | Legal | (none — correctly no commercial target) | PASS | N/A | Not independently re-audited in this pass (low priority, no commercial keyword target) | N/A | N/A | N/A | N/A | **KEEP** |

Case studies and blog posts are audited individually in `05-case-study-audit.md` and `06-blog-audit.md` — their master-table-style summaries live there to keep this table readable.

## Sections 7–9 — Keyword alignment, secondary-topic coverage, and heading architecture detail

### `/` Homepage
- **H1 vs primary keyword ("product engineering services"):** H1 is "AI-Enabled Dedicated Engineering Partner." Rating: **Partial**. The H1 communicates AI + dedicated engineering strongly but never says "product engineering," the approved primary keyword's core phrase. It's a reasonable brand H1, just not a strong keyword-intent match — and per this brief's own principle (Section 7), the H1 should *first* make sense to a CTO, which it largely does, but it doesn't clearly telegraph "we build/scale your product" the way "product engineering" does.
- **Secondary keyword coverage** ("dedicated engineering pods" — Already covered, strong nav/section presence; "AI-enabled product engineering" — Already covered; "software engineering services" — Partially covered, implicit rather than named).
- **Current heading architecture (as observed):**
```text
H1: AI-Enabled Dedicated Engineering Partner.
H2: why choose us
  H3: Experience excellence with us. Your success, our priority.
H2: what we're offering
  H3: Experts at battle tested frameworks.
H2: The "AI-Edge"
  H3: How We Use AI to Build Your Product Better.
H2: Our Partners
  H3: Technology Sharing Partners.
H2: We win when our clients win
  H3: We Give Every Project Our Full Attention And Care
H2: Ready to ditch ecommerce headaches?          ← positioning mismatch, see below
H2: Get started!
H2: Trusted Globally
H2: Trusted by Global Enterprises for Scalable Engineering
H2: Engineering Solutions for High-Stakes Industries.
H2: Technologies we are working on.
H2: GO BEYOND. BE INFORMED.
  H3: Dive into business, technology & innovation insights.
H2: Claim your free strategy session: Brainstorm to brilliance.
H2: Real clients, real wins: what they say about us.
H2: Security standards @ Zediant
```
- **"Ready to ditch ecommerce headaches?"** is a specific, out-of-place H2 on the homepage of a company now positioned around AI-enabled product engineering and dedicated pods — it reads as leftover copy from an earlier "digital solutions agency" era (the same era `services.md` and the prior technical audit already flag for the homepage title/meta and the legacy `/services/ecommerce-business/` and `/services/digital-presence/` pages). Recommend flagging for removal/replacement once approved — not touched in this audit.

### `/services/ai-enabled-product-engineering/`
- **H1 vs primary keyword ("AI-enabled product engineering company"):** H1 is "Build Intelligent Platforms with AI-Ready Architectures." Rating: **Weak/Misaligned**. This H1 does not contain "product engineering" or even "AI-enabled" — it reads like a platform-engineering headline, which is exactly the cannibalization risk `Zseodata_corrected.xlsx`'s own Mapping/Cannibalization Assessment column flags for this page ("watch AI-capability claims discipline"). Section 12 of this audit brief is explicit that this page "should communicate product engineering rather than generic AI development" — the current H1 does neither cleanly; it communicates platform/architecture.
- **Secondary coverage:** "AI-enabled product engineering services" (Partially — implied, not stated), "AI product engineering" (Partially covered), "product engineering services" (Missing — the phrase "product engineering" does not appear to be used prominently on this page's own content at all, based on the extraction).
- **Current heading architecture:**
```text
H1: Build Intelligent Platforms with AI-Ready Architectures
H2: Building Future-Ready Platforms
H2: Key Differentiators
H2: what we're offering
  H3: Our Strategic Capabilities
    (sub-items, not true H3s: SaaS Platform Development / AI Integration / Data-Driven Systems / API-First Architectures)
H2: AI Across the Development Lifecycle: 40% Faster Delivery
  H3: Code Acceleration / Testing Automation / Smart Debugging / Knowledge Generation
H2: Code the Future of Your Business
H2: Ready to Engineer Your Competitive Advantage?
H2: Solutions for Industry DNA
  H3: Automotive / SaaS / Fintech & Payments / Enterprise Platforms
H2: Enterprise-Grade Security: The Non-Negotiable Standard
  H3: Our Six Pillars of Trust (SOC 2 Type II Certified / Secure SDLC / Advanced Data Protection / RBAC / Global Compliance / AI-Driven Monitoring)
H2: Global Engineering Presence
H2: This enables
H2: Let's get connected
```
- Structural note: this page's section pattern (hero stat → differentiators → capabilities grid → "AI across the lifecycle" 4-icon grid claiming "40% faster" → industry verticals → security pillars → global presence → contact) is **nearly identical in shape** to `/services/dedicated-engineering/` and `/services/platform-engineering/`, which each repeat the same stat range (30–40%) and the same 4-icon "AI workflow" grid pattern (Augmented Coding/Precision Testing/Smart Debugging/Instant Documentation on the Pods page; Code Acceleration/Testing Automation/Smart Debugging/Knowledge Generation here). This is the concrete evidence behind the Section 12 "four pages must not sound like four versions of the same page" finding — detailed in `02-service-positioning-audit.md`.

### `/services/dedicated-engineering/`
- **H1 vs primary keyword ("dedicated engineering pods"):** **Strong** — direct match.
- **Secondary coverage:** "dedicated engineering team" (Already covered — "function as a seamless extension of your internal engineering organization"), "dedicated development team" (Partially — the page prefers "Pods"/"team" language over the literal phrase "dedicated development team," which is fine semantically but means this exact phrase isn't reinforced on its own target page), "hire dedicated development team" (Not appropriate for this page as a literal heading — it's a transactional long-tail better served by the CTA copy, which it already is: "Talk to Our Engineering Experts").
- **Heading architecture:**
```text
H1: Elite Dedicated Engineering Pods for Scalable Product Development
H2: Why Scaling Engineering is a High-Stakes Challenge
  H3: Recruitment Lag / Operational Overload / The Backlog Debt / Quality Erosion
H2: A Better Way to Scale Engineering
H2: What defines a Zediant Engineering Pod?
  H3: The Strategist (Tech Lead/Architect) / The Engine (2–4 devs) / The Gatekeeper (QA) / The Orchestrator (PM)
H2: Engineering Engagement Models
  H3: Foundation Pod / Growth Pod / Enterprise Pod
H2: Ready to Scale Your Engineering Capacity?
H2: Engineering at the Speed of AI?
  H3: Augmented Coding / Precision Testing / Smart Debugging / Instant Documentation
H2: The Result
H2: Global Footprint, Local Collaboration
H2: Enterprise-Grade Trust as Standard
  H3: Secure SDLC / Data Sovereignty / Transparency
H2: Let's get connected
```
This is the site's **best-executed service page** — the named pod-role model (Strategist/Engine/Gatekeeper/Orchestrator) and three named tiers (Foundation/Growth/Enterprise Pod) are genuinely specific, memorable, and defensible IP, not generic agency language. Recommend this structure as the template the other three service pages should be measured against for distinctiveness.

### `/services/platform-engineering/`
- **H1 vs primary keyword:** **Good** match.
- **Secondary coverage:** "cloud-native engineering services" (Already covered — microservices, IaC), "DevOps consulting" (Already covered), "platform engineering company" (implicit, fine).
- **Heading architecture:**
```text
H1: Secure, Scalable, and AI-Powered Platform Engineering
H2: Engineering Resilience for High-Growth Platforms
  (Platform-First Architecture / AI-Enabled DevOps Workflows / Security-First Engineering)
H2: High-Velocity Platform Capabilities
  (Microservices Architecture / API Ecosystems & Integrations / Advanced CI/CD Pipelines / Cloud Infrastructure (IaC))
H2: Is Your Infrastructure Ready for the Next Million Users?
H2: Security-First DevOps (SOC 2 Type II Aligned)
  (Automated Security Scanning / Identity & Access Management / Secure CI/CD Pipelines / Data Protection & Sovereignty)
H2: Reducing Developer Friction with AI-Enabled DevOps
  (Infrastructure as Code / Observability & Monitoring / Automated Scaling & Optimization / AI-Assisted DevOps Workflows)
H2: Built for Performance, Stability, and Growth
  (High Availability / Scalability / Faster Deployments / Resilience & Fault Tolerance)
H2: Supporting Multi-Regional Enterprise Scale
  (Follow-the-Sun Support / Latency Optimization / Global Governance)
H2: Enterprise-Grade Security & Compliance
H2: Let's get connected
```
- **Unsupported/risky claim flagged:** this page states **"99.99% availability"** as a capability claim. This is the exact figure `context/case_studies.md` explicitly warns must never be attached to the 11Wickets engagement (per `gate-1-decision-pack.md` §2, which notes approvingly that the *live case-study page* correctly omits it) — yet the service page itself now makes this claim in general terms. Flagging as a **CONTENT/EVIDENCE GAP / possible unsupported claim** per Section 19–20 of this brief: no source in `context/` substantiates a 99.99% SLA capability, and `campaigns.md` C3's own Disqualification Signals explicitly warn against promising this exact tier without confirmed staffing.

### `/services/enterprise-custom-development/`
- **H1 vs primary keyword:** **Weak** — "Bespoke Engineering Solutions for Public Limited Companies (PLCs)" is a narrow audience claim not supported by `campaigns.md` C5's actual documented ICP (established product companies and enterprises across software, automotive, manufacturing, logistics, fintech, retail tech — company size 20–500+, "bootstrapped or listed," not exclusively publicly listed companies).
- **Secondary coverage:** "enterprise legacy application modernisation" (Covered, as H3 "Legacy Modernization" — good), "legacy system modernization" (Covered), "custom enterprise software development" (Partially — "bespoke" is used more than "custom" in the H1 itself).
- **Heading architecture:**
```text
H1: Bespoke Engineering Solutions for Public Limited Companies (PLCs)
H2: Engineering for Complexity at Scale
  H3: We go beyond development to ensure / Key Differentiators / what we're offering
H2: Specialized Knowledge for Complex Industries
  (Automotive & CRM / Fintech & Transactional Platforms / Logistics & Supply Chain / Enterprise E-commerce)
H2: Navigating Your Toughest Engineering Hurdles
  H3: Legacy Modernization / Middleware & API Orchestration / High-Concurrency Engineering / Performance Optimization
H2: Discuss Your Enterprise Engineering Needs
H2: AI-Augmented Development: 40% Faster, Fully Compliant
H2: Why Leading Enterprises Trust Zediant
  H3: Verified Governance / SOC 2 Type II Compliance / Proven Global Footprint / AI-Enabled Engineering Efficiency
H2: Security is Non-Negotiable: SOC 2 Type II Certified
  H3: Our Security Framework Includes / Why This Matters
H2: Delivering Measurable Outcomes
  H3: Typical Outcomes
H2: Let's get connected
```
Good structural depth (Legacy Modernization gets a proper H3 with real content, consistent with `services.md`'s documented structure); the audience-framing problem is isolated to the H1/hero, not systemic across the page.

## Sections 10–11 — Content depth and positioning summary

All four service pages answer "what is the service" and "what does Zediant deliver" adequately. Where they consistently fall short, per this brief's own buyer-question checklist:
- **"Which case studies demonstrate the capability?"** — FAIL on all four service pages. Zero case studies are linked from any service page.
- **"What engagement model is appropriate?"** — PASS on Dedicated Engineering (3 named tiers); PARTIAL/absent on the other three.
- **Positioning check against** *"Zediant helps product companies build, modernize and scale software products by providing experienced engineering capabilities and flexible engineering teams"*: the AI-Enabled Product Engineering page is the one page that drifts furthest from this statement — its content is closer to generic "AI-first engineering firm" / infrastructure-and-architecture messaging than to product-building messaging, and several phrases ("AI-First engineering firm," "Unlike standard offshore firms, our entire ecosystem is externally audited") read as competing-on-AI-hype rather than the AI-assisted-delivery-methodology framing `policies/claims-and-compliance.md` §5 requires.

## Flagged claims requiring verification (Section 20 — E-E-A-T / evidence)

| Claim | Location | Status |
|---|---|---|
| "SOC 2 Type II **Certified**" (used as a flat, unqualified fact, not "aligned") | Homepage, AI-Enabled Product Engineering (×3), Dedicated Engineering (×2), Enterprise Custom Development (×2, plus a heading/body contradiction), Trust & Compliance ("certified organization"), Engineering Excellence | **CONTENT/EVIDENCE GAP** — no source in `context/` confirms a completed attestation; policy requires "aligned." This is worse and more widespread than the 2026-08-20 audit found — re-verify sitewide before any further SOC2-themed content work. |
| "99.99% availability" | Platform Engineering service page | **CONTENT/EVIDENCE GAP** — explicitly the figure `case_studies.md` prohibits attaching to the one case study that could plausibly support it; no other source substantiates it as a general capability claim. |
| "Elite 1% of engineers" | Careers page | **CONTENT/EVIDENCE GAP** — no source, methodology, or benchmark is cited anywhere in `context/`. |
| "50% increase in page views" / "20% increase in lead conversions" (material handling case study, CS-08) | Case study page | **Already-known DATA CONFLICT** vs. `case_studies.md`'s documented "30% increase in website traffic" — reconfirmed live in this pass, unresolved (see `gate-1-decision-pack.md` §2). |
| Team of 4 / 3-month duration / "Australian entrepreneur" (Ionic crypto case study, CS-07) | Case study page | **Already-known DATA CONFLICT** vs. `case_studies.md`'s documented team of 3 / 5 months / country not published — reconfirmed live, unresolved. |
| "We've passed the toughest security audit, proving our system is like Fort Knox for your data" | Homepage, AI-Enabled Product Engineering, Platform Engineering | Flagged in the 2026-08-20 audit as the phrasing that makes a strong unqualified security claim independent of the SOC2 label — still present, unchanged. |
| Testimonial quotes (DIJGTAL, Zwick Roell, Networx, STAGER) | Homepage | Not cross-referenced against any approved source in `context/` in this pass — **DATA GAP**, not a confirmed problem; recommend verifying these are real, current, and permissioned quotes before any homepage rewrite treats them as fixed content. |

None of the above were corrected, removed, or rewritten in this pass — they are flagged for the human-approved implementation phase only.
