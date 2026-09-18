# Batch 1 — Redirect Specification: `/services/build-your-team/`

Status: PREPARED ONLY — NOT DEPLOYED. No redirect has been created on the live website.
Date: 2026-08-20
Source priority followed: (1) business-confirmed decisions, (2) gate-1-decision-pack.md, (3) final-p0-implementation-matrix.md, (4) corrected initial_technical_audit.md, (5) context/, (6) policies/.

---

## Pre-check: live re-verification performed today

### 1. Current live status of both URLs

- **FACT** — `https://www.zediant.com/services/build-your-team/` — loads successfully (200 OK).
- **FACT** — `https://www.zediant.com/services/dedicated-engineering/` — loads successfully (200 OK). Confirmed live and correctly resolving; this is the confirmed canonical Dedicated Engineering Pods page. Its own canonical tag self-references `https://zediant.com/services/dedicated-engineering/`.
- **FACT** — `https://www.zediant.com/services/dedicated-engineering-pods/` was NOT re-tested in this pass — it is already established and documented as a 404 guessed URL, per the corrected technical audit, and is not part of this redirect (nothing should ever point there).

### 2. Current title/H1 of the old page

- **FACT** — Title: "Build Your Team | Zediant". H1: "IT Staff Augmentation". Meta description: "Strengthen your team with Zediant's expert staffing solutions. We help you find and integrate the right talent to drive your projects forward and achieve your business goals." Unchanged from the Gate 1 assessment.

### 3. Sitemap presence

- **FACT** — `https://www.zediant.com/services/build-your-team` is present in the current live `sitemap.xml` (`priority: 0.9`, `lastmod: 2024-08-21`). This is addressed in the companion sitemap proposal (`seo/strategy/batch-1-sitemap-proposal.md`), which proposes removing it.

### 4. Known internal links pointing to the old URL (re-verified today)

- **FACT** — The `/services/` hub page (a separate, legacy 6-card services listing distinct from the top-navigation "Services" dropdown) links to `https://www.zediant.com/services/build-your-team` via a card titled "Build Your Team" ("Start Building Your Dream Team Today").
- **FACT (updated from the Gate 1 assessment)** — The primary top-navigation "Services" dropdown, re-checked today, lists exactly four items — AI-enabled Product Engineering, Dedicated Engineering, Platform Engineering, Enterprise Custom Development — and does **not** currently include a link to `/services/build-your-team/`. This differs from the Gate 1 decision pack's earlier note that the nav dropdown linked to this page; today's direct re-check shows the nav dropdown's "Dedicated Engineering" item already points straight to `/services/dedicated-engineering/`. This discrepancy is recorded transparently rather than silently overwritten — it may reflect a nav update since Gate 1, an inconsistency between page templates, or a difference in how the two fetches rendered the menu; it has not been root-caused in this pass.
- **DATA GAP** — Whether any other page (blog post, case study, footer link, or a page outside the ones directly re-checked in this session) also links to `/services/build-your-team/` cannot be ruled out without a full-site crawl.

### 5. Canonical/indexing signals

- **FACT** — `/services/build-your-team/`'s own `<link rel="canonical">` self-references `https://zediant.com/services/build-your-team/` (no www). No `noindex` meta tag is present. The page is not currently redirected or de-indexed by any signal observed.
- **DATA GAP** — Whether Google has actually indexed this URL, and under what impressions/ranking, is unknown without Search Console access.

### 6. Data not invented

- **DATA GAP** — Search Console indexation/impressions/clicks data for this URL: unavailable in this session.
- **DATA GAP** — Backlink data (any external site linking to this URL): unavailable in this session.
- **DATA GAP** — Historical organic traffic or ranking data: unavailable in this session.

None of the above DATA GAPs are treated as blocking this redirect's preparation — the business decision to retire this page is already confirmed (`gate-1-decision-pack.md` §3) — but they should be closed before or shortly after deployment if that access becomes available, to catch any indexation/backlink value this redirect should be designed to preserve.

---

## Proposed Redirect Specification

| Field | Value |
|---|---|
| **Source URL** | `https://www.zediant.com/services/build-your-team/` (and its non-www / no-trailing-slash variants, if the CMS/server handles those as separate rules) |
| **Destination URL** | `https://www.zediant.com/services/dedicated-engineering/` |
| **HTTP status** | 301 (Moved Permanently) |
| **Reason** | Business-confirmed: `/services/build-your-team/` is obsolete and no longer an active Zediant service page. Its content (IT Staff Augmentation / team-building) substantially overlaps with the confirmed canonical Dedicated Engineering Pods page, which now covers the same underlying delivery model (same "30-40% faster delivery" claim, same team/pod framing) under Zediant's current positioning. |
| **SEO rationale** | A 301 (rather than a 410/removal) preserves any link equity this ~2-year-old, sitemap-listed, internally-linked page may hold, redirecting it to the page that most closely continues its subject matter for both users and search engines. This avoids a dead end for anyone who has bookmarked, linked to, or is currently ranking for this URL. |
| **Expected impact** | Any existing search visibility, internal link equity (from the `/services/` hub page), and direct traffic to the old URL should consolidate onto `/services/dedicated-engineering/` rather than being lost. No new content is created; no existing page's content is removed. |
| **Rollback** | The redirect rule can be removed or repointed at any time without data loss — no content is deleted as part of this specification. The current `/services/build-your-team/` page content should be archived (not deleted) before the redirect is implemented, so it can be restored if the decision is reversed. |
| **Verification steps** | After deployment: (1) fetch `/services/build-your-team/` directly and confirm it returns a 301 to `/services/dedicated-engineering/`; (2) confirm `/services/dedicated-engineering/` itself still returns 200; (3) update the `/services/` hub page card to point to `/services/dedicated-engineering/` instead of the retired URL (a separate, small content change also requiring approval); (4) confirm the corrected sitemap (see `batch-1-sitemap-proposal.md`) no longer lists `/services/build-your-team/` as a canonical/indexable entry; (5) if Search Console access becomes available, monitor for crawl errors and indexation of the redirect over the following weeks. |

**This redirect has NOT been implemented.** No DNS, hosting, CMS, or redirect-rule change has been made.
