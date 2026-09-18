# 08 — Page-by-Page Content Blueprints

Status: Read-only recommendations. Nothing below has been implemented. Every H1/H2 suggestion is a **proposal for future human-approved implementation**, not a live change.

Covers every page classified OPTIMIZE or REWRITE in `01-page-audit.md`.

---

## Homepage (`/`) — OPTIMIZE

**Current Situation:** Strong breadth (4 services, verticals, tech stack, testimonials, security standards) undercut by one leftover section ("Ready to ditch ecommerce headaches?") from an earlier positioning era, and an H1 that doesn't use the approved primary keyword's core phrase.

**SEO Problem:** H1 "AI-Enabled Dedicated Engineering Partner" doesn't reinforce "product engineering," the approved primary keyword — search engines and skimming visitors get a Pods/AI signal but not a product-engineering signal.

**Content Problem:** The ecommerce-headaches section is inconsistent with the current 4-service B2B enterprise positioning and likely a holdover from the same era as the legacy `/services/ecommerce-business/` and `/services/digital-presence/` pages.

**Positioning Problem:** Otherwise consistent; this is a leftover-content issue more than a systemic positioning conflict.

**Recommended H1 (proposal only):** "AI-Enabled Product Engineering & Dedicated Engineering Pods" or similar — keep the strong AI/Pods signal, add the "product engineering" phrase explicitly.

**Recommended H2 structure (proposal only, sections only — not full copy):**
- Why Choose Us (keep)
- What We're Offering (keep — 4 services)
- The "AI-Edge" (keep)
- Solutions for High-Stakes Industries (keep — good ICP signal)
- Case Studies spotlight (keep, but expand beyond the current 4 linked)
- Technologies (keep)
- Testimonials (keep, pending verification per `01-page-audit.md`)
- Security Standards (keep, pending SOC2 wording fix)
- Remove or replace: "Ready to ditch ecommerce headaches?"

**Content Additions:** None required beyond the wording above — this page's breadth is already good.

**Content Removals:** The ecommerce-headaches section (subject to business confirmation it's genuinely obsolete, not a still-sold capability — see the unresolved `/services/ecommerce-business/` status in prior audits).

**Internal Links:** Add links to the remaining 6 case studies not currently featured on the homepage.

**CTA:** Existing CTAs ("Book a Strategy Session," "Get your free consultation") are fine — no change needed.

**Priority:** High

---

## AI-Enabled Product Engineering (`/services/ai-enabled-product-engineering/`) — REWRITE

**Current Situation:** H1 and framing read as generic "AI-first engineering firm" / platform-architecture content rather than product engineering; heavy structural and claim overlap with Platform Engineering.

**SEO Problem:** Primary keyword "AI-enabled product engineering company" isn't reinforced by the H1 or the page's dominant language, weakening topical relevance for its own target term.

**Content Problem:** No case studies linked; the "AI Across the Development Lifecycle" 4-icon grid duplicates the shape (not the specifics) of the equivalent grids on the Dedicated Engineering and Enterprise Custom Development pages.

**Positioning Problem:** This is the page most at odds with `policies/claims-and-compliance.md` §5's caution against overclaiming generic AI/ML depth — phrases like "AI-First engineering firm" read as competing on AI-development positioning rather than "AI-assisted delivery methodology applied to product engineering."

**Recommended H1 (proposal only):** Something that pairs "product engineering" with the AI differentiator, e.g. "AI-Enabled Product Engineering for Scaling SaaS Platforms" — deliberately reintroducing "product engineering" as a literal phrase.

**Recommended H2 structure (proposal only):**
- Building Future-Ready Products (reframe from "Platforms" to "Products" to sharpen the product-engineering distinction from Platform Engineering)
- Roadmap vs. Headcount: the problem this service solves (new section, drawing on `campaigns.md` C1's existing, unused messaging)
- Our Strategic Capabilities (keep)
- AI Across the Product Development Lifecycle (keep, retitled for consistency)
- Engagement Models (new — currently the only one of the 4 service pages besides Dedicated Engineering that could use this; borrow the tiering concept, don't copy Pods' exact tiers)
- Solutions for Industry DNA (keep)
- Case Study spotlight (new — link CS-05 Zakaa/Diamond dashboard, the closest available fit)
- Enterprise-Grade Security (keep, pending sitewide SOC2 wording fix)
- Global Engineering Presence (keep)

**Content Additions:** Roadmap-vs-headcount framing; a linked case study; an engagement-model/tiering section.

**Content Removals:** Language implying broad AI/ML product depth ("AI-First engineering firm," "Unlike standard offshore firms, our entire ecosystem is externally audited" as a generalized claim) — flag for claims review, not a stylistic edit.

**Internal Links:** Add CS-05 case study link; consider linking to Platform Engineering with clearly differentiated framing ("for infrastructure and platform scaling, see Platform Engineering") to make the boundary explicit rather than implicit.

**CTA:** Existing "Build Your AI-Enabled Platform Today" is fine, though "Platform" could become "Product" for consistency with the reframed positioning.

**Priority:** High

---

## Enterprise Custom Development (`/services/enterprise-custom-development/`) — REWRITE (H1/audience framing only — body content is largely good, see `01-page-audit.md`)

**Current Situation:** Strong body content undercut by an H1 that narrows the audience to "Public Limited Companies (PLCs)" specifically.

**SEO Problem:** Primary keyword "enterprise custom software development" is present but the H1's PLC framing may suppress relevance for the broader documented ICP (established product companies and enterprises generally, per `campaigns.md` C5).

**Content Problem:** None significant — Legacy Modernization, Middleware & API Orchestration, and High-Concurrency Engineering are all genuinely covered.

**Positioning Problem:** The PLC-only framing in the hero is not supported anywhere else on the page or in `campaigns.md`'s actual ICP definition — it reads as a stray decision from an earlier, narrower audience assumption.

**Recommended H1 (proposal only):** "Enterprise Custom Software Development & Modernization" (matches the approved SEO title almost exactly) or "Bespoke Engineering for Complex Enterprise Systems" — either drops the PLC-only framing while keeping the "bespoke"/enterprise-grade tone.

**Recommended H2 structure:** Keep the existing structure as-is (Engineering for Complexity at Scale / Specialized Knowledge for Complex Industries / Navigating Your Toughest Engineering Hurdles / AI-Augmented Development / Why Leading Enterprises Trust Zediant / Security / Delivering Measurable Outcomes) — it's sound; only the H1/hero framing needs to change.

**Content Additions:** A linked case study (CS-08 once resolved, or CS-09/BigCommerce in the meantime).

**Content Removals:** None beyond the PLC-specific hero framing.

**Internal Links:** Add 1–2 case study links.

**CTA:** Existing CTAs fine.

**Priority:** High

---

## Platform Engineering (`/services/platform-engineering/`) — OPTIMIZE

**Current Situation:** Strong, technically specific page; main issue is the unsupported "99.99% availability" claim and the missing case-study link.

**SEO Problem:** None significant — good keyword alignment.

**Content Problem:** "99.99% availability" is stated as a capability without support in `context/` and is the exact figure `case_studies.md` prohibits attaching to the one case study (11Wickets) that would otherwise support it.

**Positioning Problem:** None significant.

**Recommended H1:** No change needed.

**Recommended H2 structure:** No structural change needed.

**Content Additions:** Link CS-04 (11Wickets) as a case study.

**Content Removals/Corrections:** Remove or properly qualify the "99.99% availability" claim (flagged for claims review, not a stylistic choice) — also relevant to `campaigns.md` C3's own instruction not to promise this tier without confirmed staffing.

**Internal Links:** Add CS-04.

**CTA:** No change needed.

**Priority:** High (for the claim fix specifically), Medium (for the case-study link)

---

## Dedicated Engineering Pods (`/services/dedicated-engineering/`) — OPTIMIZE

**Current Situation:** The site's strongest service page. Main gaps are the missing case-study link and SOC2 wording.

**SEO/Content/Positioning Problems:** None significant.

**Recommended H1/H2:** No change needed — this page should be the template, not the target, of rewrites.

**Content Additions:** Link CS-06 (Team Augmentation for Automotive Software).

**Content Removals:** None.

**Internal Links:** Add CS-06.

**CTA:** No change needed.

**Priority:** Medium

---

## Trust & Compliance (`/about-us/trust-compliance/`) — OPTIMIZE

**Current Situation:** Good structure, undercut by the single most consequential wording problem on the site — this canonical trust page states "Zediant is a SOC 2 Type II certified organization" as flat fact.

**SEO Problem:** The approved primary keyword is "SOC 2 Type II aligned software partner" — the live page uses the opposite, non-compliant term on its own canonical page for this topic.

**Content Problem:** None beyond the wording.

**Positioning Problem:** This is a compliance-policy issue, not merely an SEO one — see `policies/claims-and-compliance.md` §6.

**Recommended H1:** No change needed.

**Recommended H2 structure:** No structural change needed.

**Content Additions:** None.

**Content Removals/Corrections:** Replace every instance of "certified" with "aligned" (or the fuller "SOC 2 Type II aligned, independently assessed against the framework's controls" if a more precise, still-accurate phrasing is preferred) — sitewide, not just this page. This single correction, applied everywhere it's needed, is arguably the highest-priority content change identified in this entire audit given how many pages it touches.

**Internal Links:** No change needed.

**CTA:** No change needed.

**Priority:** **Highest — P0**

---

## Blog Hub (`/blogs/`) — REWRITE

**Current Situation:** Technical/template bug (13 of 20 posts unreachable) compounded by a stale, generic featured-post selection.

**SEO Problem:** Search engines and users alike cannot discover 65% of the blog's own content via on-site navigation.

**Content Problem:** The 7 posts that *are* shown skew toward the more generic/dated end of the content set (3 of the 7 shown are exactly the posts flagged as "generic/dated" in `06-blog-audit.md`), while several of the strongest on-strategy posts (the ZCoupler comparison cluster) are hidden.

**Recommended fix (not a content rewrite — a template/logic fix):** Once source/CMS access is available, confirm why the hub only renders 7 posts and add pagination or a full listing. This is flagged for developer/CMS investigation, not something to guess at from the rendered page alone.

**Content Additions (post-fix):** A deliberate "Featured" selection that foregrounds the ZCoupler cluster and Dedicated Engineering Pods content over the generic web-development-trends posts, consistent with current positioning.

**Priority:** **High — this is a genuine indexability defect, not a nice-to-have.**

---

## Service-to-Content Map (Section 29)

| Service | Case Studies (best-fit) | Existing Blogs (best-fit) | Missing Topics |
|---|---|---|---|
| AI-Enabled Product Engineering | CS-05 (Zakaa/Diamond dashboards) — imperfect fit | Harnessing PWAs (currently linked here, weak fit); When AI Learns to Survive (currently linked here, poor fit — see `06`) | Roadmap-vs-headcount / MVP-to-scale narrative content; a genuinely strong case-study match is currently missing entirely |
| Dedicated Engineering Pods | CS-06 (Team Augmentation, Automotive) | Driving Success with Staff Augmentation Strategies; Empower Your Team/IT Outsourcing | Staff augmentation vs. dedicated pod comparison (see `03-content-gap-analysis.md`) |
| Platform Engineering | CS-04 (11Wickets) | Connect Everything/ZCoupler Formula; How an In-House Middleware Platform; Why Middleware Integration is the Hidden Hero; ZCoupler vs Traditional Middleware | None significant — best-covered service by blog volume |
| Enterprise Custom Development | CS-02 (Wholesale Parts CRM), CS-08 (Material Handling, pending resolution), CS-09 (BigCommerce), CS-10 (WordPress/Poker) | Leveraging Sitecore; Making the Old New Again | Named-stack legacy-modernization deep dives (.NET Framework, Java EE) |

**Note:** CS-01 (Middleware for DMS), CS-03 (Lubricant Tool), and CS-07 (Ionic Crypto) sit slightly outside this four-row mapping — CS-01 is Integration/Middleware-specific (best paired with the Middleware Integration service page, not one of the 4 top-level services directly), and CS-03/CS-07 are more general Enterprise Custom Development proof points. This reflects a real structural note: **Integration & Middleware Engineering (the ZCoupler cluster) has the site's richest case-study and blog evidence of any topic, but its live commercial page (`/services/middleware-integration/`) sits below the top-level nav's 4 services and currently receives none of that evidence** — reinforcing the B-priority content gap already flagged in `03-content-gap-analysis.md`.
