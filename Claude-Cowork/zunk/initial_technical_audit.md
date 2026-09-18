# Initial Technical SEO Audit — Zediant Technologies

Status: Draft / Read-only discovery
Date: 2026-08-19
Scope: www.zediant.com (public site), discovered via robots.txt, sitemap.xml, and direct page fetches. No website changes were made.

---

## 1. Crawlability

- `robots.txt` is present at `https://www.zediant.com/robots.txt`, permits all crawlers (`Disallow:` empty), and correctly declares the sitemap location. CONFIRMED.
- No crawl blocks or disallowed paths were observed.

## 2. Sitemap — P0

The declared sitemap (`https://www.zediant.com/sitemap.xml`) is stale and materially inaccurate:

- All 22 entries carry `lastmod: 2024-08-21` — roughly two years old relative to today.
- 3 of the current 4 published services referenced in company.md/services.md and in the live site's own navigation — AI-Enabled Product Engineering, Platform Engineering, Enterprise Custom Development — do **not** appear in the sitemap at all.
- The sitemap's case-study URLs use short slugs (e.g. `/case-studies/wholesale`) that return **404** on the live site. The live case-studies hub uses long descriptive slugs instead (e.g. `/case-studies/wholesale-parts-crm-for-automotive-dealers-and-oems`).
- The live case-studies hub lists 10 case studies; the sitemap lists 9, using the wrong slugs for all of them, and is missing the newest one (Real-Time Executive Dashboards / Zakaa Innovation Hub).
- The entire `/blogs/` section (7 live posts observed) is absent from the sitemap.

**Finding:** Evidence:  Impact: A sitemap this far out of sync likely wastes crawl budget on dead URLs, under-represents the pages that actually reflect Zediant's current positioning, and may be actively harming discovery of the newer service pages. Recommendation: regenerate the sitemap from the live site architecture. Priority: **P0**. Effort: Low (usually a CMS/sitemap-generator configuration fix). Approval: Sitemap regeneration is a technical fix, not a content or URL change — HUMAN APPROVAL REQUIRED per policy before implementation, since it is a website change.

## 3. Broken navigation link — P0

The primary navigation's "Dedicated Engineering Pods" service link resolves to `https://www.zediant.com/services/dedicated-engineering-pods`, which returns a **404**.

**Finding:** Zediant's own documentation (`company.md`) states Dedicated Engineering Pods is the company's "primary and preferred model," representing approximately 90% of billing. The corresponding page for the company's flagship, revenue-dominant service is broken on the live site. Evidence: direct fetch, 404 confirmed. Business Impact: severe — visitors and search engines following the main navigation for the company's core offer hit a dead end. SEO Impact: loses internal link equity to the intended page and signals a broken primary conversion path. Recommendation: identify the intended canonical URL for this service (candidate: `/services/build-your-team/`, which currently covers "IT Staff Augmentation" and partially overlaps) and fix the link, or publish the missing page. Priority: **P0**. Effort: Low to Medium depending on whether a page needs to be created or only relinked. Approval: **HUMAN APPROVAL REQUIRED** (URL/navigation change, and possibly a new commercial page).

## 4. Duplicate/parallel domain — P0 / DATA GAP

`work.zediant.com` is a live, separate site discovered via general web search, not referenced anywhere in Claude.md, company.md, services.md, or any other Revenue Engine context file.

- It presents overlapping service categories (Web Development, Mobile App Development, E-commerce Integrations, API Development, SaaS Products, Cloud Solutions, Staff Augmentation) under a different, more generic "technology solutions provider" positioning.
- It states company statistics not found in any approved source: **48 team members** (company.md documents 25–35), a **97% satisfaction rate**, and **100+ projects** — none of which are corroborated by `company.md`, `case_studies.md`, or any approved claims source.

**Finding:** This is a DATA GAP. Evidence: direct fetch confirms the site is live and publicly indexable. Business Impact: unknown until clarified — could be a legacy site pending decommission, a staging/portfolio subdomain, or an actively maintained parallel property; each has different SEO and compliance implications. SEO Impact: potential duplicate content, brand confusion, and split authority across two competing domains for overlapping search intents. Recommendation: escalate to a human owner to determine the status, ownership, and intended fate of `work.zediant.com` before any SEO action is taken involving it. Priority: **P0**. Approval: **HUMAN APPROVAL REQUIRED** — do not treat any of its content or stated figures as approved claims in the interim.

## 5. HTTPS and host canonicalization

- All fetched pages were served over HTTPS. CONFIRMED.
- Requests to `www.zediant.com` URLs consistently resolved to `zediant.com` (no `www`) in the fetched content. This is LIKELY a redirect or canonicalization rule but was not verified at the HTTP-header level with the tools available in this session. REQUIRES HUMAN VERIFICATION with a header-level crawl tool to confirm a single, consistent canonical host and check for redirect chains or loops.

## 6. Items not assessable in this discovery pass — UNKNOWN

The following require tools not available in this session (a dedicated crawler, Google Search Console, PageSpeed Insights, or mobile-emulation tooling) and are marked UNKNOWN rather than guessed:

- Canonical tag presence/correctness across pages
- Structured data / schema.org markup
- Duplicate or thin content at the HTML level (beyond the page-level overlap noted in the on-page and content audits)
- Mobile rendering and usability issues
- Core Web Vitals / page speed
- Exact redirect chains
- Indexed page count, impressions, clicks, CTR, and keyword rankings (no Search Console or Analytics connector was available)

**Recommendation:** commission a full technical crawl (e.g. Screaming Frog, Sitebulb) and connect Google Search Console before the next SEO cycle to close these gaps. Priority: **P1**.

## 7. Summary of P0/P1 technical items

| Item | Priority | Approval Required |
|---|---|---|
| Regenerate stale/broken sitemap | P0 | Yes |
| Fix or publish the Dedicated Engineering Pods page/link | P0 | Yes |
| Clarify status of work.zediant.com | P0 | Yes (escalation) |
| Verify www/non-www canonicalization and redirect chains | P1 | Yes (if a change is needed) |
| Full technical crawl + Search Console connection | P1 | No (tooling/process only) |
