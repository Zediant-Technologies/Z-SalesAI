# 04 — Internal Linking Audit

Status: Read-only. No links added or changed.

## Headline finding: 13 of ~20 live blog posts are orphaned from the blog hub

`/blogs/` renders exactly 7 posts with no pagination (`/blogs/2/` returns a 404). The other 13 posts in scope — all present in the approved keyword file and all confirmed live and fetchable by direct URL in this pass — are **not linked from `/blogs/` and have no other on-site path leading to them** (the global header/footer only link to the `/blogs/` hub itself, not to individual posts). This is a genuine crawl-discoverability and user-navigation defect, not merely a content-freshness issue:

**Orphaned (not listed on the live `/blogs/` hub):**
1. `/blogs/connect-everything-break-nothing-the-zcoupler-integration-formula/`
2. `/blogs/driving-success-with-staff-augmentation-strategies/`
3. `/blogs/eaas-engineering-as-a-service/`
4. `/blogs/empower-your-team-save-resources-leverage-the-power-of-it-outsourcing/`
5. `/blogs/global-growth-in-it-services-consulting-unlocking-new-frontiers/`
6. `/blogs/harnessing-the-potential-of-progressive-web-apps-pwas-for-superior-user-engagement/`
7. `/blogs/how-an-in-house-middleware-platform-is-helping-enterprises-in-automobile-oil-gas-and-ecommerce-move-from-fragmentation-to-full-integration/`
8. `/blogs/leveraging-sitecore-for-scalable-e-commerce-and-cms-solutions/`
9. `/blogs/making-the-old-new-again-how-zediant-technologies-middleware-solutions-can-breathe-life-into-your-legacy-systems/`
10. `/blogs/the-invisible-backbone-system-integration/`
11. `/blogs/when-ai-learns-to-survive-alarming-signals-we-cant-ignore/`
12. `/blogs/why-middleware-integration-is-the-hidden-hero-of-scalable-systems/`
13. `/blogs/zcoupler-vs-traditional-middleware-what-sets-it-apart/`

**Still shown on the hub (7):** the ZCoupler multi-database announcement, plug-and-play middleware, emerging tech, staff augmentation for demanding projects, evolution of web development, the school-website case study, and future of web/app development.

This matters because several of the orphaned posts are among the *better-targeted* pieces on the site — `zcoupler-vs-traditional-middleware`, `why-middleware-integration-is-the-hidden-hero`, and `making-the-old-new-again` are all genuinely on-strategy ZCoupler/integration content that a crawler or a site visitor currently cannot reach except by direct URL, search, or the external LinkedIn cross-post. This is a **P0/P1 technical finding**, distinct from and in addition to the sitemap staleness already documented in prior audits — fixing the sitemap alone will not fix this, since the sitemap doesn't include the blog section at all; this needs a blog-hub template/pagination fix.

Whether this is a CMS bug, a manual curation choice, or a "Featured" vs. "All posts" filtering issue that simply isn't exposing an "all posts" view is unknown — **DATA GAP**, since source code isn't available in this session. Recommend this be the first thing checked with actual CMS/repo access.

## Orphan and weakly-connected pages (beyond the blog issue)

| Page | Inbound internal links found | Assessment |
|---|---|---|
| The 13 orphaned blog posts above | 0 from any on-site page (only reachable by direct URL) | **Orphaned** |
| Individual case studies (all 10) | 1 (from `/case-studies/` hub) + 2–3 "Related" links from other case studies | Weakly connected — no inbound links from any service page |
| `/about-us/our-story/` | Present in every page's footer ("About Us" link) | Adequately linked |
| `/privacy-policy/`, `/terms-of-use/` | Footer on every page | Adequately linked (appropriately minimal, as legal pages should be) |

No page was found with *zero* internal links other than the 13 orphaned blog posts — the global header/footer means every other page in scope has at least hub-level and often full-nav-level linking.

## Missing contextual links (the biggest opportunity, by volume)

### Service pages → Case studies (currently: none)
Recommended pairings, based on actual content match found in `05-case-study-audit.md`:

| Service page | Should link to |
|---|---|
| `/services/dedicated-engineering/` | Team Augmentation for Automotive Software (CS-06) |
| `/services/platform-engineering/` | 11Wickets Scalability & Performance Optimization (CS-04) |
| `/services/middleware-integration/` | Middleware Integration for Multiple Large DMS (CS-01); Wholesale Parts CRM (CS-02) |
| `/services/enterprise-custom-development/` | Redeveloping Website for Material Handling Company (CS-08, once its figures are resolved — see `05`); BigCommerce Integration (CS-09) |
| `/services/ai-enabled-product-engineering/` | Real-Time Executive Dashboards for Zakaa (CS-05) — closest available fit, though imperfect (see `05`) |

### Case studies → Service pages (currently: none)
The reverse of the above — every case study page currently ends with only "Related Articles" (other case studies). Each should link back to the one service page it best evidences.

### Blog → Service pages (currently: partial — several posts already do this well)
Already good: `connect-everything-zcoupler-integration-formula` → Platform Engineering; `driving-success-with-staff-augmentation-strategies` → Dedicated Engineering; `global-growth-in-it-services-consulting` → all four service pages; `harnessing-pwas` → AI-Enabled Product Engineering; `how-an-in-house-middleware-platform` → Platform Engineering; `leveraging-sitecore` → Enterprise Custom Development; `making-the-old-new-again` → Enterprise Custom Development + Platform Engineering; `when-ai-learns-to-survive` → AI-Enabled Product Engineering (this pairing is weak — see `06-blog-audit.md`); `why-middleware-integration-is-the-hidden-hero` → Platform Engineering; `zcoupler-vs-traditional-middleware` → Platform Engineering + Enterprise Custom Development.
Missing: `eaas-engineering-as-a-service`, `empower-your-team-...it-outsourcing`, and the school-website case-study post do not link to any specific service page (generic nav only).

### Blog → Case studies (currently: essentially none observed)
No blog post in this pass was found linking to a specific case study, even where an obvious pairing exists (e.g. `leveraging-sitecore-for-scalable-e-commerce-and-cms-solutions` describes the same engagement as the material-handling case study, CS-08, but does not link to it).

## Anchor text audit

No instances of "click here," "read more," or "learn more" as a standalone anchor were found in this pass — anchor text throughout is already descriptive (e.g. "Dedicated Engineering Pods," "Trust & Compliance," "AI-enabled Product Engineering"). This is a **genuine strength** — see `07-priority-action-plan.md` "Do NOT change." The one repeated non-descriptive pattern is case-study "Discover More" / "Related Articles" links, which are acceptable in a card/list UI context but do not carry topical anchor-text value; recommend, when case studies gain service-page links, using descriptive anchors there (e.g. "how a dedicated engineering pod supported this automotive software team") rather than "Discover More."

## Summary

Zediant's internal linking is strong at the *global navigation* layer (every core page reachable from every other core page, descriptive anchors throughout) and weak at the *contextual* layer (case studies and services never reference each other; 13 blog posts are unreachable by navigation at all). Fixing the blog-hub bug and adding service↔case-study cross-links are the two highest-leverage, lowest-risk internal-linking changes available — neither requires new content, only linking work.
