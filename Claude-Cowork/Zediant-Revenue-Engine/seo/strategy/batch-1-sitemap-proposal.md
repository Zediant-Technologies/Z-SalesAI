# Batch 1 — Sitemap Proposal

Status: PREPARED ONLY — NOT DEPLOYED. The live `sitemap.xml` has not been modified.
Date: 2026-08-20
Method: The current live `sitemap.xml` (22 entries) was fetched directly today. Current live navigation, the `/services/` hub page, the case-studies hub, and the blogs hub were fetched directly today to establish the current indexable page set. Cross-referenced against `context/services.md`, the corrected `initial_technical_audit.md`, and `gate-1-decision-pack.md`. No canonical information has been invented — where a canonical relationship is not directly observed, it is marked DATA GAP.

---

## Current sitemap (as of today, 22 entries)

| # | URL (as listed) | lastmod | priority |
|---|---|---|---|
| 1 | /  | 2024-08-21 | 1.0 |
| 2 | /about-us/our-story | 2024-08-21 | 0.8 |
| 3 | /about-us/team-culture | 2024-08-21 | 0.8 |
| 4 | /about-us/how-we-work | 2024-08-21 | 0.8 |
| 5 | /about-us/careers | 2024-08-21 | 0.8 |
| 6 | /services/ecommerce-business | 2024-08-21 | 0.9 |
| 7 | /services/digital-presence | 2024-08-21 | 0.9 |
| 8 | /services/saas-development | 2024-08-21 | 0.9 |
| 9 | /services/middleware-integration | 2024-08-21 | 0.9 |
| 10 | /services/cloud-security | 2024-08-21 | 0.9 |
| 11 | /services/build-your-team | 2024-08-21 | 0.9 |
| 12 | /case-studies/wholesale | 2024-08-21 | 0.7 |
| 13 | /case-studies/wickets | 2024-08-21 | 0.7 |
| 14 | /case-studies/middleware | 2024-08-21 | 0.7 |
| 15 | /case-studies/lubricant | 2024-08-21 | 0.7 |
| 16 | /case-studies/team | 2024-08-21 | 0.7 |
| 17 | /case-studies/crypto | 2024-08-21 | 0.7 |
| 18 | /case-studies/poker | 2024-08-21 | 0.7 |
| 19 | /case-studies/bigcommerce | 2024-08-21 | 0.7 |
| 20 | /case-studies/redeveloping | 2024-08-21 | 0.7 |
| 21 | /privacy-policy | 2024-08-21 | 0.5 |
| 22 | /terms-of-use | 2024-08-21 | 0.5 |

## Additional finding surfaced during this pass (relevant to CORRECT/REMOVE below)

- **FACT** — Re-checking the live top-navigation "About Us" dropdown today shows it links to three URLs not present anywhere in the current sitemap: `/about-us/who-we-are`, `/about-us/engineering-excellence`, `/about-us/trust-compliance` (plus `/about-us/careers`, already in the sitemap). All three new URLs load successfully (200) with their own self-referencing canonical tags.
- **FACT** — The three sitemap-listed "old" About URLs (`/about-us/our-story`, `/about-us/team-culture`, `/about-us/how-we-work`) *also* still load successfully (200) today, each with its own self-referencing canonical tag (not pointing to the new URLs). This is a genuine live duplicate-content pattern — old and new About pages coexist as separate, independently-canonical, live pages — not a simple slug rename. This mirrors the previously-identified `/services/build-your-team/` vs `/services/dedicated-engineering/` overlap, but for the About section, and has not been previously documented in any prior audit. It is noted here because it directly affects which URLs belong in a corrected sitemap; resolving the duplicate-content pattern itself (e.g., redirecting the old About URLs) is a new item outside this batch's four approved tasks and is not proposed for action here.

---

## Proposed changes

### REMOVE

| URL | Status | Reason | Evidence source |
|---|---|---|---|
| `/services/build-your-team` | Live (200), but business-confirmed obsolete | Confirmed obsolete/no longer an active service page (gate-1-decision-pack.md §3); candidate 301 to `/services/dedicated-engineering/` prepared in `batch-1-redirect-build-your-team.md`. Should not remain indexable as a distinct page once the redirect is approved and live. | Business-confirmed decision; live re-check today |
| `/about-us/our-story` | Live (200), self-canonical, not linked from current nav | No longer linked from the current top-navigation "About Us" dropdown, which now points to `/about-us/who-we-are` instead. Retained here as REMOVE-from-sitemap (not a claim that the underlying page should be deleted — that is a separate decision, flagged above as new and out of this batch's scope). | Live re-check today |
| `/about-us/team-culture` | Live (200), self-canonical, not linked from current nav | Same pattern as above — current nav points to `/about-us/engineering-excellence` instead. | Live re-check today |
| `/about-us/how-we-work` | Live (200), self-canonical, not linked from current nav | Same pattern as above — current nav points to `/about-us/trust-compliance` instead. | Live re-check today |

No sitemap entries were found to be dead/404 in this pass — the previously-known 404 case-study slugs (see CORRECT below) are corrected rather than simply removed, since a live, current page exists for each.

### ADD

| URL | Status | Reason | Canonical status | Evidence source |
|---|---|---|---|---|
| `/services/ai-enabled-product-engineering/` | Live (200) | Current top-nav service, entirely absent from sitemap | Self-canonical (not independently re-verified this pass; consistent with nav) | Live nav re-check today; `initial_technical_audit.md` §2 |
| `/services/dedicated-engineering/` | Live (200) | Confirmed canonical Dedicated Engineering Pods page; currently absent from sitemap entirely | Self-canonical: `https://zediant.com/services/dedicated-engineering/` (verified today) | Live re-check today; business-confirmed decision |
| `/services/platform-engineering/` | Live (200) | Current top-nav service, absent from sitemap | DATA GAP (not independently re-verified this pass) | Live nav re-check today; `initial_technical_audit.md` §2 |
| `/services/enterprise-custom-development/` | Live (200) | Current top-nav service, absent from sitemap | DATA GAP (not independently re-verified this pass) | Live nav re-check today; `initial_technical_audit.md` §2 |
| `/about-us/who-we-are/` | Live (200) | Current nav target, absent from sitemap | Self-canonical: `https://zediant.com/about-us/who-we-are/` (verified today) | Live re-check today |
| `/about-us/engineering-excellence/` | Live (200) | Current nav target, absent from sitemap | Self-canonical: `https://zediant.com/about-us/engineering-excellence/` (verified today) | Live re-check today |
| `/about-us/trust-compliance/` | Live (200) | Current nav target, absent from sitemap | Self-canonical: `https://zediant.com/about-us/trust-compliance/` (verified today) | Live re-check today |
| `/case-studies/` (hub page) | Live | Case-studies index/hub page, not separately listed in current sitemap | DATA GAP (not independently checked) | Live re-check today |
| `/case-studies/real-time-executive-dashboards-zakaa-innovation-hub` | Live | Newest case study; entirely absent from the current sitemap (already flagged in `initial_technical_audit.md` §2) | DATA GAP | `initial_technical_audit.md` §2; live case-studies hub re-check today |
| `/blogs/` (hub page) | Live | Blog index page; entire `/blogs/` section absent from sitemap | DATA GAP | Live re-check today; `initial_technical_audit.md` §2 |
| `/blogs/zcoupler-our-integration-platform-now-supports-7lyuc/` | Live (per hub listing; individual page not separately fetched) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/simplifying-complex-systems-with-plug-and-play-middleware-that-accelerates-deployment-and-drives-business-agility/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/emerging-tech-in-action-how-new-technologies-are-reshaping-business-operations/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/why-deal-with-demanding-technical-projects-and-handle-busy-development-periods-yourself/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/the-evolution-and-importance-of-web-development-in-todays-digital-age/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/case-study-zediant-technologies-helps-a-school-boost-admissions-with-scalable-website/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |
| `/blogs/the-future-of-web-and-app-development/` | Live (per hub listing) | Live blog post, absent from sitemap | DATA GAP | Live blogs hub re-check today |

**Note:** the 7 individual blog URLs above were confirmed present as links on the live `/blogs/` hub page but were not individually fetched to verify each returns 200 in this pass — recommended as a quick confirmation step before deployment (DATA GAP: individual blog-post HTTP status).

### CORRECT

| Old sitemap URL | Corrected URL | Reason | Evidence source |
|---|---|---|---|
| `/case-studies/wholesale` | `/case-studies/wholesale-parts-crm-for-automotive-dealers-and-oems` | Old slug 404s; live case-studies hub uses the long-form slug | `initial_technical_audit.md` §2; live case-studies hub re-check today |
| `/case-studies/wickets` | `/case-studies/11wickets-scalability-and-performance-optimization-with-zediant` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/middleware` | `/case-studies/middleware-integration-for-multiple-large-dms` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/lubricant` | `/case-studies/lubricant-recommendation-tool-for-the-worlds-leading-brands` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/team` | `/case-studies/team-augmentation-for-automotive-software` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/crypto` | `/case-studies/development-of-crypto-apps-with-ionic` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/poker` | `/case-studies/upgrading-online-poker-game-website-to-wordpress` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/bigcommerce` | `/case-studies/bigcommerce-integration-for-australias-biggest-office-supply-brand` | Same pattern | Live case-studies hub re-check today |
| `/case-studies/redeveloping` | `/case-studies/redeveloping-website-for-a-leading-material-handling-company-in-australia` | Same pattern | Live case-studies hub re-check today |

**Note on case-study claims content:** CS-07 (crypto) and CS-08 (redeveloping) contain unresolved factual discrepancies against `context/case_studies.md` per `gate-1-decision-pack.md` §2 and are classified RED in `final-p0-implementation-matrix.md` Item 8. This sitemap correction fixes only the URL slug so the entry is not a 404 — it does not touch, endorse, or resolve the underlying claims discrepancy, which remains untouched pending a separate business decision.

### KEEP (no change proposed)

| URL | Status | Reason | Evidence source |
|---|---|---|---|
| `/` (homepage) | Live (200) | Correct, current, no change needed at the sitemap level (title/meta addressed separately in `batch-1-homepage-metadata.md`) | Live re-check today |
| `/about-us/careers` | Live (200) | Still current and nav-linked | Live nav re-check today |
| `/services/ecommerce-business` | Live (200) | Live and indexable, but not part of the current top-nav "Services" dropdown (only linked from the legacy `/services/` hub page). No business decision to retire this page exists (unlike `/services/build-your-team/`). Flagged for a future decision, not acted on here — outside this batch's four approved tasks. | Live re-check today |
| `/services/digital-presence` | Live (200) | Same pattern as above. Also separately tracked as `final-p0-implementation-matrix.md` Item 6 (RED — claims-alignment decision pending). No sitemap removal proposed while that decision is open. | Live re-check today; final-p0-implementation-matrix.md Item 6 |
| `/services/saas-development` | Live (200) | Same pattern — legacy hub-linked page, no retirement decision on record. | Live re-check today |
| `/services/cloud-security` | Live (200) | Same pattern. | Live re-check today |
| `/services/middleware-integration` | Live (200) | Same pattern. | Live re-check today |
| `/privacy-policy` | Live (200) | Standard legal page, current and correct | Live re-check today |
| `/terms-of-use` | Live (200) | Standard legal page, current and correct | Live re-check today |

### EXCLUDE (confirmed, nothing to list)

No 404 URLs, redirects, obsolete pages, duplicate URLs, or non-canonical URLs are proposed for inclusion in the corrected sitemap. Specifically excluded: `/services/dedicated-engineering-pods/` (confirmed 404, never a real page — see corrected technical audit); `/services/build-your-team` (see REMOVE, pending its redirect); the old-slug case-study URLs (see CORRECT — the new slugs replace them, the old ones are not dual-listed); `/about-us/our-story`, `/about-us/team-culture`, `/about-us/how-we-work` (see REMOVE).

---

## Summary

- **CURRENT SITEMAP COUNT:** 22
- **PROPOSED SITEMAP COUNT:** 35
- **URLs REMOVED:** 4 (`/services/build-your-team`, `/about-us/our-story`, `/about-us/team-culture`, `/about-us/how-we-work`)
- **URLs ADDED:** 17 (4 current service pages, 3 current About pages, case-studies hub, 1 newest case study, blogs hub, 7 individual blog posts)
- **URLs CORRECTED:** 9 (all case-study slugs, old short slug → live long-form slug)
- **URLs UNCHANGED (KEEP):** 9 (homepage, careers, 5 legacy/non-nav service pages left as-is pending a separate retirement decision, privacy-policy, terms-of-use)

**No changes have been made to the live `sitemap.xml`.** This is a proposal only, pending human approval of both this sitemap correction and, where applicable, the underlying decisions it depends on (the build-your-team redirect in `batch-1-redirect-build-your-team.md`, and the newly-surfaced About-section duplicate-content pattern, which is flagged for awareness but not proposed for resolution in this batch).
