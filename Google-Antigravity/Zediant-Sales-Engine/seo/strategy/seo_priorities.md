# SEO Priorities — Initial Baseline

Status: Draft / Read-only discovery output
Date: 2026-08-19
Source discovery: `seo/prompts/initial_discovery.md`

This document synthesizes the technical, on-page, content, competitor, and keyword findings from the initial discovery pass into a prioritized backlog. No website changes have been made. Every P0/P1 item below requires human approval before implementation, per `Claude.md`, `MASTER_SEO_PROMPT.md`, and `context/seo/seo_rules.md`.

---

## P0 — Critical technical/indexation or high-value commercial issues

| # | Finding | Evidence | Business Impact | SEO Impact | Recommendation | Effort | Approval |
|---|---|---|---|---|---|---|---|
| P0-1 | Primary nav link to "Dedicated Engineering Pods" 404s | Direct fetch of `/services/dedicated-engineering-pods` | Zediant's flagship service (~90% of billing per company.md) has no working page | Broken primary conversion path; wasted link equity | Identify canonical URL (candidate: consolidate with `/services/build-your-team/`) and fix, or publish new page | Low–Medium | Yes |
| P0-2 | Sitemap is ~2 years stale and lists 404ing/incorrect URLs | Direct fetch of sitemap.xml, dated 2024-08-21 | Search engines likely crawling dead URLs and missing current pages | Wasted crawl budget; under-representation of current site | Regenerate sitemap from live site architecture | Low | Yes |
| P0-3 | Homepage title/meta tag contradicts current positioning and H1 | Direct fetch | Search snippets sell a generic "digital solutions" agency, not the actual current business | Suppresses relevance/CTR for the terms that matter now | Rewrite title/meta to reflect AI-Enabled Product Engineering / Pods positioning | Low | Yes |
| P0-4 | `/services/digital-presence/` advertises SEO/social-media-marketing services not in `services.md`'s offered capability list | Direct fetch vs. `services.md` "Not offered" list | Possible mismatch between marketed and deliverable capability | Page should not be used as an SEO content reference until resolved | Escalate for review of this page's status | Low (review only) | Yes (escalation) |
| P0-5 | `work.zediant.com` is a live, undocumented parallel site with unsupported company statistics (48 staff vs. documented 25–35; 97% satisfaction; 100+ projects) | WebSearch + direct fetch | Unknown — could be legacy, staging, or active; contradicts approved company facts | Potential duplicate content and brand/authority split | Escalate to determine ownership and intended fate before any SEO action | Low (escalation) | Yes |

## P1 — High-value service/search opportunities

| # | Finding | Recommendation | Approval |
|---|---|---|---|
| P1-1 | `/services/cloud-security/` and `/services/platform-engineering/` target overlapping intent | Consolidate or differentiate per `seo_rules.md` §3/§9 | Yes |
| P1-2 | `/services/saas-development/` and `/services/ai-enabled-product-engineering/` target overlapping intent | Consolidate or differentiate | Yes |
| P1-3 | `/services/middleware-integration/` omits ZCoupler, Zediant's most strongly evidenced product/case study (CS-01) and the anchor of campaign C4 | Add ZCoupler framing via a proper content brief | Yes |
| P1-4 | Blog content is generic and dated (most recent June 2025; topics like "Web Development Trends for 2024") and does not build authority on current core themes | Build a content roadmap around pods, AI-assisted delivery, platform engineering, and integration/middleware per `context/seo/content_strategy.md` | Yes (for publication) |
| P1-5 | No confirmed indexation of the three current-positioning service pages in a directional search check | Confirm actual indexation status via Google Search Console (not available in this session) | No (verification only) |
| P1-6 | www/non-www and redirect-chain canonicalization not verified at header level | Run a header-level crawl to confirm | No (verification only) |

## P2 — Meaningful optimization/content opportunities

| # | Finding | Recommendation | Approval |
|---|---|---|---|
| P2-1 | `/services/ecommerce-business/` and `/services/digital-presence/` are unmapped to the current 4-service catalog or C1–C5 taxonomy | Confirm strategic status (retain, retire, or fold into another service page) | Yes |
| P2-2 | 10 live case studies not individually verified against `case_studies.md` approved metrics in this pass | Run a dedicated verification pass before using any case study in new SEO content | No (verification only) |
| P2-3 | No ZCoupler-branded page/content exists despite being a named product | Scope a branded product page as a future content brief | Yes (for publication) |
| P2-4 | Competitor SERP observations suggest Zediant's "AI-enabled" positioning may be competing against generic Dubai "AI development company" listings rather than firms with comparable delivery-method framing | Differentiate content on AI-assisted delivery methodology rather than general AI-development claims, consistent with `policies/claims-and-compliance.md` §5 | No (strategy guidance) |

## P3 — Lower-impact enhancements

| # | Finding | Recommendation | Approval |
|---|---|---|---|
| P3-1 | SOC 2 wording should be checked sitewide for "aligned" vs. "certified" consistency once a full crawl is possible | Include in next full technical/content crawl | Yes (for any copy change) |
| P3-2 | About-section subpages (Team Culture, How We Work, Trust & Compliance) referenced in nav but not individually verified in this pass | Verify live status and content accuracy in next pass | No (verification only) |
| P3-3 | Full Core Web Vitals / mobile / structured-data assessment | Commission a dedicated technical crawl and connect Search Console | No (tooling only) |

---

## DATA GAPs

1. **work.zediant.com** — existence, ownership, and intended status are undocumented anywhere in the Revenue Engine. (P0-5)
2. **Search Console / Analytics access** — no connector available in this session; indexed page count, impressions, clicks, CTR, keyword rankings, and organic traffic are all UNKNOWN.
3. **Structured data / schema.org markup** — not assessable via the tools available in this session.
4. **Core Web Vitals / page speed / mobile rendering** — not assessable via the tools available in this session.
5. **Canonical tags and exact redirect chains** — not assessable at the HTML/header level with the tools available in this session.
6. **Live case-study page content vs. approved `case_studies.md` metrics** — not individually verified for all 10 case studies in this pass.
7. **Strategic status of `/services/ecommerce-business/` and `/services/digital-presence/`** — unclear whether these remain actively sold, standalone capabilities.
8. **Intended canonical URL for Zediant's primary Pods service** — unclear whether `/services/build-your-team/` should become the Pods page, or a new page should be created at `/services/dedicated-engineering-pods`.

## HUMAN APPROVAL REQUIRED items

Per `context/seo/seo_rules.md` §11 and `MASTER_SEO_PROMPT.md` §6, the following all require explicit human approval before implementation — none of them have been actioned:

- Fixing or republishing the Dedicated Engineering Pods page/link (P0-1)
- Regenerating the sitemap (P0-2)
- Rewriting the homepage title/meta description (P0-3)
- Any resolution of the `/services/digital-presence/` claims conflict (P0-4)
- Any SEO action involving `work.zediant.com` (P0-5)
- Any consolidation, redirect, or differentiation of the four overlapping page pairs (P1-1, P1-2, P1-3 partially, P2-1)
- Publication of any new or revised content (blog roadmap, ZCoupler page, Pods page, homepage copy)

---

## Executive Summary

Zediant's public website reflects two overlapping eras of company positioning at once: a newer, current set of pages (AI-Enabled Product Engineering, Platform Engineering, Enterprise Custom Development) that matches the company's documented services and differentiation, and an older, more generic "digital solutions agency" layer (homepage title/meta, e-commerce/digital-presence pages, and a separate `work.zediant.com` domain) that does not. The single highest-priority issue is that Zediant's actual primary, revenue-dominant service — Dedicated Engineering Pods — has no working page: the main navigation link to it 404s. Combined with a two-year-stale sitemap that lists dead URLs and omits the current service pages entirely, this creates real risk that both users and search engines are being routed toward outdated or broken paths instead of the business Zediant runs today. A previously undocumented parallel site, `work.zediant.com`, adds further uncertainty — it carries company statistics that do not match approved sources and its status is unknown. None of these require content creation to begin fixing; they are indexation, linking, and metadata issues that should be resolved first, before any keyword research or content investment, consistent with the discovery-before-content principle in `MASTER_SEO_PROMPT.md`. A preliminary keyword universe and directional competitor scan are included to inform planning, but both are explicitly marked as provisional pending a full keyword-research and Search-Console-connected pass — no search volume, ranking, or traffic figures were fabricated or assumed.

**No implementation, publication, or website change has occurred. This is a read-only baseline.**
