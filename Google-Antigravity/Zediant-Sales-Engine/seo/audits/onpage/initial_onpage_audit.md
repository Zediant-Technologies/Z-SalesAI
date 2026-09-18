# Initial On-Page SEO Audit — Zediant Technologies

Status: Draft / Read-only discovery
Date: 2026-08-19

---

## 1. Homepage — P0

**Finding:** The homepage `<title>` and meta description do not match the homepage's own H1 or Zediant's current, documented positioning.

- Title: "Innovative Digital Solutions for Business Growth - Zediant Technologies"
- Meta description: "Zediant offers cutting-edge digital solutions to drive your business forward. Explore our services in SaaS development, e-commerce, cloud solutions, and more to transform your business."
- H1: "Your Global AI-Enabled Product Engineering Partner"

Evidence: direct fetch of the homepage. Business Impact: the title/meta tag — the text that actually appears in search results — sells a generic "digital solutions" agency, while the page itself and the rest of the current context (company.md, services.md) describe a specific, differentiated AI-enabled product engineering and dedicated-pods partner. This mismatch likely suppresses click-through from the searches most relevant to Zediant's actual current business, and does not target any of the four currently published services. SEO Impact: title/meta are primary on-page ranking and CTR signals; neither currently contains "engineering pods," "product engineering," "AI-enabled," or any current service name. Recommendation: rewrite the title and meta description to reflect the current positioning and lead service names, subject to approval. Priority: **P0**. Approval: **HUMAN APPROVAL REQUIRED** (this is a live page edit).

## 2. Overlapping / duplicate-intent service pages — P1

Four pairs of live pages appear to target overlapping search intent, which risks keyword cannibalization (per `context/seo/seo_rules.md` §3 and §9, and `context/seo/keyword_strategy.md` cannibalization control):

| Legacy page | Current page | Overlap |
|---|---|---|
| `/services/cloud-security/` ("Cloud Solutions") | `/services/platform-engineering/` ("Secure, Scalable, and AI-Powered Platform Engineering") | Both address cloud infrastructure/platform work |
| `/services/saas-development/` ("SaaS Product Integrations") | `/services/ai-enabled-product-engineering/` ("Build Intelligent Platforms with AI-Ready Architectures") | Both address SaaS/product platform development |
| `/services/build-your-team/` ("IT Staff Augmentation") | `/services/dedicated-engineering-pods` (404 — does not exist) | Both address embedded/augmented engineering capacity; unclear which is the intended canonical page for Zediant's primary service |
| `/services/ecommerce-business/`, `/services/digital-presence/` | No current equivalent — these are not part of the four currently published services in `services.md` | Unclear strategic status |

**Finding:** Evidence: direct fetch and comparison against `services.md`'s four currently-published services. Business Impact: prospects and search engines may land on the older, more generic page instead of the page that reflects current capability and differentiation (SOC 2 alignment wording, AI-assisted delivery method, senior-default staffing) — diluting the intended positioning. SEO Impact: two pages competing for the same query intent typically split ranking signal rather than reinforcing it. Recommendation: per `seo_rules.md` §3 ("existing page before new page"), determine for each pair whether to consolidate, differentiate, or redirect — do not simply add more content to either page until a decision is made. Priority: **P1**. Approval: **HUMAN APPROVAL REQUIRED** for any consolidation, redirect, or canonical change.

## 3. Claims-policy conflict on `/services/digital-presence/` — P0

**Finding:** This page's meta description and body content advertise "SEO to social media marketing" and broader digital marketing services.

Evidence: direct fetch. Per `services.md` §"Not offered," Zediant does **not** offer standalone SEO execution, standalone content marketing, or brand/marketing strategy as services — engineering delivery is the business. Per `policies/claims-and-compliance.md` §4, capabilities not documented in `services.md` must not be claimed, and this is treated as a `DATA GAP`.

Business Impact: this page may be generating enquiries for a service Zediant is not positioned or resourced to deliver, and its content is currently in direct conflict with the approved services list. SEO Impact: none directly, but this page should not be used as a template or reference for any new SEO content, and should not be linked into content strategy until resolved. Priority: **P0**. Recommendation: escalate to a human for review of this page's status (retire, rescope, or reconfirm as an approved capability). Approval: **HUMAN APPROVAL REQUIRED**.

## 4. ZCoupler product gap on the Middleware Integration page — P1

**Finding:** `/services/middleware-integration/` does not mention ZCoupler anywhere in its content, despite ZCoupler being the named product referenced in `campaigns.md` (campaign C4 — "Middleware & API Integration (ZCoupler)") and described in `services.md` as Zediant's most strongly evidenced capability (CS-01, the automotive DMS middleware case study).

Evidence: direct fetch. Business Impact: the page underrepresents Zediant's strongest, most differentiated proof point in this category. SEO Impact: a missed opportunity to build topical authority and branded-product search presence around "ZCoupler." Recommendation: add ZCoupler framing and link to the relevant case study (CS-01), subject to content brief and approval. Priority: **P1**. Approval: **HUMAN APPROVAL REQUIRED** (content publication).

## 5. Legacy pages unmapped to current taxonomy — P2

`/services/ecommerce-business/` and `/services/digital-presence/` do not correspond to any of the four currently published services in `services.md`, nor to any of the C1–C5 campaigns in `campaigns.md`. E-commerce and CMS work is documented in `services.md` as capability #9 ("E-commerce & CMS Development," sold standalone) but is not currently represented in the site's primary navigation or the new four-service page set.

**Finding:** Evidence: comparison of live navigation/pages against `services.md`. Business Impact/SEO Impact: unclear without a decision on strategic status — these pages may be intentionally retained for a real, sold-standalone capability, or may be legacy remnants of an earlier "generalist digital agency" positioning. Recommendation: confirm with a human owner whether e-commerce/CMS development remains an actively sold, standalone capability worth an optimized page, or should be folded into a broader service page. Priority: **P2**. Approval: **HUMAN APPROVAL REQUIRED** for any resulting page change.

## 6. Case study pages — spot-check recommendation — P2

The live case-studies hub lists 10 case studies that broadly correspond to the 10 approved case studies (CS-01 through CS-10) documented in `case_studies.md`. This discovery pass did not fetch and line-by-line verify each individual live case-study page's claims against the approved metrics in `case_studies.md` (per `policies/claims-and-compliance.md` §8: use documented metrics exactly, never improve/round/extrapolate).

**Recommendation:** a dedicated content audit pass should verify each live case-study page's stated metrics, customer names, and confidentiality handling (in particular CS-02 and CS-06, which `policies/confidentiality.md` flags as requiring special care) against `case_studies.md` before any of them are used as SEO proof content or linked from new pages. Priority: **P2**. This is a verification task, not itself a website change.

## 7. Summary

| Item | Priority | Approval Required |
|---|---|---|
| Rewrite homepage title/meta to match current positioning | P0 | Yes |
| Resolve digital-presence SEO/marketing claims conflict | P0 | Yes (escalation) |
| Resolve cloud-security vs platform-engineering overlap | P1 | Yes |
| Resolve saas-development vs ai-enabled-product-engineering overlap | P1 | Yes |
| Resolve build-your-team vs dedicated-engineering-pods (404) | P1 (linked to technical P0) | Yes |
| Add ZCoupler framing to middleware-integration page | P1 | Yes |
| Clarify strategic status of ecommerce-business / digital-presence | P2 | Yes |
| Verify live case-study pages against case_studies.md metrics | P2 | No (verification only) |
