# Initial Content Audit — Zediant Technologies

Status: Draft / Read-only discovery
Date: 2026-08-19

---

## 1. Page classification

| Type | Pages observed | Notes |
|---|---|---|
| Homepage | 1 | Positioning mismatch — see on-page audit |
| Service (current, matches services.md's 4 published services) | 3 live + 1 broken (404) | ai-enabled-product-engineering, platform-engineering, enterprise-custom-development live; dedicated-engineering-pods missing |
| Service (legacy, unmapped or overlapping) | 5 | ecommerce-business, digital-presence, saas-development, middleware-integration, cloud-security, build-your-team |
| Case study | 10 | Broadly matches CS-01–CS-10 in case_studies.md; not individually verified in this pass |
| Blog / resource | 7 | Most recent June 2025; oldest February 2024 |
| About | at least 2 confirmed live (Our Story, Careers); Team Culture / How We Work / Trust & Compliance referenced in nav but not individually fetched | UNKNOWN status for unfetched pages |
| Legal | 2 (Privacy Policy, Terms of Use, per sitemap) | Not individually re-verified live in this pass |
| Separate/parallel site | 1 (work.zediant.com) | DATA GAP — status undocumented |

## 2. Strong pages

- `/services/ai-enabled-product-engineering/`, `/services/platform-engineering/`, `/services/enterprise-custom-development/` — these three pages correctly reflect Zediant's current published service catalog and are the closest match to the company's documented positioning.
- `/case-studies/` hub — a reasonably complete proof library (10 case studies) that broadly tracks the approved case study index.

## 3. Weak / thin pages

- Homepage — strong H1 but undermined by legacy title/meta (see on-page audit, P0).
- `/services/digital-presence/` — content promotes services outside the documented service catalog (P0 claims conflict).
- Blog section — topics are generic web-development commentary ("Web Development Trends for 2024," "The Future of Web and App Development") rather than content demonstrating the specific expertise areas Zediant now leads with (AI-assisted delivery, dedicated pods, platform engineering, middleware/ZCoupler). This does not build topical authority for the themes in `context/seo/seo_strategy.md`'s primary SEO theme list.

## 4. Missing commercial pages

- **Dedicated Engineering Pods** — Zediant's primary, ~90%-of-billing service has no working dedicated page (see technical audit, P0). This is the single highest-priority content gap identified in this discovery.
- No page found that centers ZCoupler as a named, brandable middleware product, despite it being Zediant's most strongly evidenced capability (CS-01) and the anchor of campaign C4.
- No geography-specific landing content for the two primary target markets (Australia, UAE) was observed. Per `context/seo/seo_strategy.md`, any future location pages must have genuine market-specific value, not be created by swapping a country name — this is a candidate for later keyword/content-brief work, not an immediate gap to fill blindly.

## 5. Overlapping pages (cannibalization risk)

See on-page audit §2 for the four specific page pairs/groups. Summary: `cloud-security` / `platform-engineering`; `saas-development` / `ai-enabled-product-engineering`; `build-your-team` / `dedicated-engineering-pods` (missing); and the unmapped `ecommerce-business` / `digital-presence` pair.

## 6. Orphan / unclear pages

- `work.zediant.com` in its entirety — not linked from or referenced by the main site's navigation in anything observed during this pass, discovered only via general web search. Treated as a DATA GAP pending human clarification, not as an orphan page to fix within this site's architecture.
- Sitemap-listed case-study short-slug URLs (e.g. `/case-studies/wholesale`) are effectively orphaned dead ends — they exist only in the stale sitemap and 404 on request.

## 7. Content evidence check

Per `policies/claims-and-compliance.md` and `context/seo/seo_rules.md` §6–7, this discovery pass did not identify any new fabricated claims on the live site beyond the two items already logged: the homepage's generic legacy copy (P0, on-page audit) and the digital-presence SEO/marketing claim (P0, on-page audit). Company statistics found on `work.zediant.com` (48 team members, 97% satisfaction, 100+ projects) are **not corroborated** by `company.md` and must not be treated as approved figures anywhere in the Revenue Engine — see technical audit §4.

## 8. Recommendation

Do not begin content drafting until the P0 items above (sitemap, broken Pods page/link, homepage title/meta, digital-presence claims conflict, work.zediant.com status) are resolved with human input. Once resolved, the highest-value next content step is a proper content brief (per `context/seo/content_strategy.md`) for a canonical Dedicated Engineering Pods page and a ZCoupler-centered middleware page — both pending approval.
