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

## 3. Dedicated Engineering Pods navigation link — CORRECTED (was: "Broken navigation link — P0")

> **CORRECTION (2026-08-20):** This finding was a **false positive**. See the "Correction / Changelog" section at the end of this document for the full audit trail. It is retained here, struck through in substance, so the record of what was originally reported is not lost — it is no longer an active finding and carries no priority.

~~The primary navigation's "Dedicated Engineering Pods" service link resolves to `https://www.zediant.com/services/dedicated-engineering-pods`, which returns a **404**.~~

~~**Finding:** ... Priority: P0. Approval: HUMAN APPROVAL REQUIRED (URL/navigation change, and possibly a new commercial page).~~ **(superseded — see correction below)**

**Verified facts (2026-08-20):**

- Canonical page: `/services/dedicated-engineering/` — this URL is live and resolves successfully. It is, and has always been, the actual navigation target.
- Incorrect/guessed URL: `/services/dedicated-engineering-pods/` — this is the URL that returns a 404. It was a guessed slug used during the original discovery pass, not the real navigation target, and was never actually present in the site's navigation.
- Result: 404 on the guessed URL, but this does **not** represent a broken navigation link. The primary navigation for Dedicated Engineering Pods — Zediant's flagship, revenue-dominant service — is functioning correctly.

**Status: No active finding. No action required.**

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
| ~~Fix or publish the Dedicated Engineering Pods page/link~~ — **REMOVED, false positive (see §3 and Correction/Changelog)** | — | — |
| Clarify status of work.zediant.com | P0 | Yes (escalation) |
| Verify www/non-www canonicalization and redirect chains | P1 | Yes (if a change is needed) |
| Full technical crawl + Search Console connection | P1 | No (tooling/process only) |

---

## Correction / Changelog

**2026-08-20 — False-positive correction to §3, "Dedicated Engineering Pods navigation link":**

- **Original finding (2026-08-19):** Reported as "Broken navigation link — P0," stating the primary navigation's Dedicated Engineering Pods link resolves to `/services/dedicated-engineering-pods` and returns a 404.
- **Root cause of the error:** During the original discovery pass, `/services/dedicated-engineering-pods` (with "-pods") was a **guessed URL**, used as a best-effort candidate for the nav target rather than the actual href read from the live navigation. It does 404, but it was never the real navigation target.
- **Verified facts (2026-08-20):**
  - Canonical page: `/services/dedicated-engineering/`
  - Incorrect/guessed URL: `/services/dedicated-engineering-pods/`
  - Result: 404 on guessed URL, but this does NOT represent a broken navigation link.
- **Correction:** The finding is a **false positive** and has been removed from the active P0 findings and from the summary table in §7. §3 has been retained with its original text struck through, plus the verified facts, for audit-trail purposes — it is no longer an active issue and carries no priority or approval requirement.
- **Scope of this correction:** Documentation-only, confined to this file (`seo/audits/technical/initial_technical_audit.md`). No website, DNS, redirect, sitemap, metadata, CRM, or scheduler change was made or is required as a result of this correction. No other finding in this document (sitemap staleness, work.zediant.com, HTTPS/canonicalization, or the UNKNOWN items) was altered.
