# P0 SEO Implementation Plan — Zediant Technologies

Status: Draft / Planning only — NO implementation has occurred
Date: 2026-08-20
Source: derived exclusively from `seo/data/seo_baseline.csv`, `seo/data/content_inventory.csv`, `seo/audits/technical/initial_technical_audit.md`, `seo/audits/onpage/initial_onpage_audit.md`, `seo/audits/content/initial_content_audit.md`, `seo/strategy/seo_priorities.md`, and current `context/`/`policies/` files. No new research, no new keyword data, and no invented facts have been introduced. Where the discovery marked something UNKNOWN, it remains UNKNOWN here.

This document sequences the seven confirmed P0 items into an implementation-ready plan. It recommends actions; it does not execute any of them. Per `context/seo/seo_rules.md` §11 and `MASTER_SEO_PROMPT.md` §6, every item below that touches a live URL, redirect, canonical, or public claim requires explicit human approval before implementation — none of it has been granted or acted on here.

---

## 1. Dedicated Engineering Pods navigation / 404

**Current state:** The primary site navigation's "Dedicated Engineering Pods" link resolves to `https://www.zediant.com/services/dedicated-engineering-pods`, which returns a 404. No live page exists at this URL. A related, overlapping page exists at `/services/build-your-team/` (H1: "IT Staff Augmentation"), which partially but not fully represents the same underlying service.

**Evidence from discovery:** `seo/audits/technical/initial_technical_audit.md` §3 ("Broken navigation link — P0"); `seo/data/content_inventory.csv` row for `https://www.zediant.com/services/dedicated-engineering-pods` (Indexable: No — 404); `seo/data/seo_baseline.csv` row "Nav-linked service page missing entirely."

**Business/SEO impact:** `company.md` documents Dedicated Engineering Pods as Zediant's primary and preferred delivery model, approximately 90% of billing. The main navigation's link to the company's flagship, revenue-dominant service is broken. This is a severed primary conversion path and a loss of internal link equity to whatever page should hold this content.

**Recommended action:** A human decides between two paths: (a) designate `/services/build-your-team/` as the canonical Dedicated Engineering Pods page (retitle/reframe it), with a 301 redirect from any legacy path if applicable, or (b) publish a new page at `/services/dedicated-engineering-pods` and update the nav link to point to it, ideally with `/services/build-your-team/` then redirected or clearly differentiated to avoid the P1 overlap already logged in `seo/audits/onpage/initial_onpage_audit.md` §2. This plan does not select between (a) and (b) — that decision is exactly what requires human approval below, since it is a service-positioning and possibly a redirect/canonicalization decision, not a mechanical fix.

**Exact URL(s) affected:** `https://www.zediant.com/services/dedicated-engineering-pods` (currently 404); `https://www.zediant.com/services/build-your-team/` (currently live); main site navigation component (all pages, since nav is likely global).

**Exact files/assets likely to require modification:** CMS navigation/menu configuration (asset not identified in discovery — CMS platform itself is UNKNOWN per `seo/data/seo_baseline.csv`); the service page template/content for whichever URL becomes canonical; if a redirect is used, server/CMS redirect rules (asset location UNKNOWN — requires developer access, see §E below).

**Nature of change:** Business decision (which URL is canonical) + content (page copy) + potentially redirect + navigation/technical.

**Dependencies:** Requires the business decision in "Recommended action" before any technical work starts. Depends on content approval per `context/seo/content_strategy.md` (target keyword, intent, brief) if new/rewritten copy is needed.

**Risk:** Low technical risk once the canonical-URL decision is made (a link fix and/or a redirect are routine). Risk is concentrated in the decision itself: publishing new claims on this page must stay within `services.md`'s documented capabilities and `policies/claims-and-compliance.md` (no exaggerated capacity, headcount, or delivery claims).

**Rollback approach:** If a redirect is added, it can be removed/repointed without data loss. If new content is published, keep the prior page content archived before replacing it so it can be restored if the change underperforms.

**Human approval required:** YES — service-positioning decision, and any redirect/URL change.

**Recommended priority:** P0 (highest — blocks the primary conversion path for Zediant's dominant revenue service).

---

## 2. Sitemap

**Current state:** `https://www.zediant.com/sitemap.xml` is dated `lastmod: 2024-08-21` on all 22 entries — roughly two years stale relative to session date. It omits the three current-positioning service pages (`ai-enabled-product-engineering`, `platform-engineering`, `enterprise-custom-development`), omits the entire `/blogs/` section (7 live posts), and lists case-study URLs using short slugs (e.g. `/case-studies/wholesale`) that 404 on the live site — the live case-studies hub uses long descriptive slugs instead.

**Evidence from discovery:** `seo/audits/technical/initial_technical_audit.md` §2 ("Sitemap — P0"); `seo/data/seo_baseline.csv` rows "Sitemap lastmod date," "Sitemap URL count," "Sitemap case-study URLs functional," "Current live service pages missing from sitemap," "Blog section... present in sitemap: No," "New case study... present in sitemap: No."

**Business/SEO impact:** Search engines are likely being pointed at dead URLs and are under-informed about the pages that reflect Zediant's current business. This wastes crawl budget and may suppress discovery/indexation of the pages that matter most now.

**Recommended action:** Regenerate `sitemap.xml` from the live, current site architecture — correct case-study slugs, add the current service pages and blog URLs, remove dead entries, and set accurate `lastmod` values. This is a technical/content-accuracy fix, not a positioning decision, but it is still a live-site change.

**Exact URL(s) affected:** `https://www.zediant.com/sitemap.xml`. Indirectly, every URL it should list (all current service, case-study, blog, about, and legal pages).

**Exact files/assets likely to require modification:** The sitemap source/generator (CMS platform and sitemap-generation mechanism are UNKNOWN per discovery — requires developer/CMS-admin access to identify and regenerate).

**Nature of change:** Technical.

**Dependencies:** None on other P0 items — this can proceed independently once approved. Benefits from Item 1's canonical-URL decision being resolved first so the regenerated sitemap doesn't need a second pass.

**Risk:** Low — sitemap regeneration is low-risk and reversible (the old sitemap can be restored from this discovery's record of its 22 entries if needed).

**Rollback approach:** Retain a copy of the current stale sitemap.xml content (already captured in `seo/data/seo_baseline.csv`) before replacing it.

**Human approval required:** YES — it is a live website file change, even though low-risk.

**Recommended priority:** P0.

---

## 3. Homepage title/meta

**Current state:** Homepage `<title>`: "Innovative Digital Solutions for Business Growth - Zediant Technologies." Meta description: "Zediant offers cutting-edge digital solutions to drive your business forward. Explore our services in SaaS development, e-commerce, cloud solutions, and more to transform your business." H1 (unchanged, not flagged as a problem): "Your Global AI-Enabled Product Engineering Partner."

**Evidence from discovery:** `seo/audits/onpage/initial_onpage_audit.md` §1 ("Homepage — P0"); `seo/data/seo_baseline.csv` rows "Homepage title tag," "Homepage meta description."

**Business/SEO impact:** The title and meta description — the text that actually appears in search results — describe a generic "digital solutions" agency and do not mention pods, AI-enabled engineering, platform engineering, or enterprise custom development, the four services Zediant currently publishes. This mismatches the H1 and current positioning, and likely suppresses relevance and click-through for the searches that matter to the current business.

**Recommended action:** Rewrite the homepage `<title>` and meta description to reflect current positioning and lead service names, consistent with the H1. Per `context/seo/seo_rules.md` §5–6, avoid keyword stuffing and unsupported claims; per `policies/claims-and-compliance.md`, do not introduce any new company claim (e.g., certification wording) beyond what is already approved. This plan does not draft the exact replacement copy — that is a content-approval step, not something to invent here without a content brief per `context/seo/content_strategy.md`.

**Exact URL(s) affected:** `https://www.zediant.com/`.

**Exact files/assets likely to require modification:** Homepage `<title>` and `<meta name="description">` tags (CMS page-settings field — exact CMS/location UNKNOWN, requires developer/CMS-admin access).

**Nature of change:** Metadata/content.

**Dependencies:** None technically, but the new copy should be consistent with whatever is decided for Item 1 (Pods) and Item 6/7 (claims/SOC 2 wording), so drafting should happen after those are scoped, even if the deployment can happen independently.

**Risk:** Low — a title/meta change is easily reverted and carries no structural risk. The only risk is introducing a new unsupported claim if the rewrite isn't checked against `policies/claims-and-compliance.md`.

**Rollback approach:** Record the exact current title/meta text (already captured verbatim in `seo/data/seo_baseline.csv`) before changing it, so it can be restored.

**Human approval required:** YES — live homepage copy change.

**Recommended priority:** P0.

---

## 4. Digital Presence page

**Current state:** `https://www.zediant.com/services/digital-presence/` (H1: "Digital Presence Lab") advertises "SEO to social media marketing" and broader digital-marketing services in its meta description and body content.

**Evidence from discovery:** `seo/audits/onpage/initial_onpage_audit.md` §3 ("Claims-policy conflict on `/services/digital-presence/` — P0"); `seo/data/content_inventory.csv` row for this URL (Content Quality: "Claims SEO and social media marketing services not documented in services.md's offered capabilities").

**Business/SEO impact:** `context/services.md` §"Not offered" explicitly excludes standalone SEO execution, standalone content marketing, and brand/marketing strategy from Zediant's service catalog. Per `policies/claims-and-compliance.md` §4, a capability not documented in `services.md` must not be claimed — this is treated as a DATA GAP. This page may be generating enquiries for work Zediant is not resourced or positioned to deliver, and it cannot be used as a reference for any new SEO content until resolved.

**Recommended action:** Escalate this page's status to a human for a decision: retire it, rescope its content to match an actually-approved capability, or (if digital marketing is in fact a real, approved capability not yet reflected in `services.md`) update `services.md` first through the proper business-context process — this plan does not assume that outcome. No content edit should proceed until the underlying capability question is resolved.

**Exact URL(s) affected:** `https://www.zediant.com/services/digital-presence/`.

**Exact files/assets likely to require modification:** The page's content and meta description (CMS — location UNKNOWN); potentially `context/services.md` if the business decision is to formally add this capability (a business-context change, out of scope for an SEO Skill per `Claude.md` §5 Knowledge Ownership).

**Nature of change:** Business decision (capability/claims), then content/metadata if retained.

**Dependencies:** Must be resolved before this page is used in any keyword targeting, internal linking, or content-brief work.

**Risk:** Moderate — leaving it as-is risks continuing to generate mismatched-expectation enquiries and a documented claims-policy conflict; changing it without the underlying capability decision risks either under- or over-stating what Zediant offers.

**Rollback approach:** Archive current page content before any edit; if retired, consider whether a redirect is warranted (a separate redirect decision, itself requiring approval).

**Human approval required:** YES — public claims and service positioning.

**Recommended priority:** P0.

---

## 5. work.zediant.com

**Current state:** `work.zediant.com` is a live, separate site, discovered via general web search, not referenced anywhere in `Claude.md` or any `context/` file. It presents overlapping service categories under different, more generic "technology solutions provider" positioning, and states company statistics — 48 team members, 97% satisfaction rate, 100+ projects — that are not corroborated by `company.md` (which documents 25–35 headcount) or any other approved source.

**Evidence from discovery:** `seo/audits/technical/initial_technical_audit.md` §4 ("Duplicate/parallel domain — P0 / DATA GAP"); `seo/data/seo_baseline.csv` row "Secondary/parallel domain discovered"; `seo/data/content_inventory.csv` row for `https://work.zediant.com/`.

**Business/SEO impact:** Unknown until clarified. Potential outcomes range from a harmless legacy/staging property to an actively duplicating, authority-splitting domain making unsupported claims that could create compliance and consistency risk if a prospect compares it against the main site or approved company facts.

**Recommended action:** Escalate to a human owner to determine: (a) what this domain is (legacy, staging, actively maintained, abandoned), (b) who owns it, and (c) its intended fate (retire, redirect to zediant.com, consolidate, or formally document as a distinct, intentional property). No SEO action should treat any of its content or stated figures as approved until this is resolved.

**Exact URL(s) affected:** `https://work.zediant.com/` and its subpages (not individually enumerated in the discovery pass — only the homepage was fetched).

**Exact files/assets likely to require modification:** None yet — this item is a decision/escalation, not an edit. Depending on the decision: DNS/hosting configuration, redirect rules, or content edits on that domain (all requiring access this session does not have — see §D/§E below).

**Nature of change:** Business decision (external domain).

**Dependencies:** None — this can and should be escalated independently and in parallel with the other items.

**Risk:** High if left unresolved indefinitely — the longer an undocumented domain with unsupported claims stays live, the more it can be cited by a prospect or picked up in search results as if it were approved company information.

**Rollback approach:** Not applicable until a decision is made; whatever action is chosen should be preceded by an archived snapshot of the domain's current content.

**Human approval required:** YES — external domain change and unresolved claims.

**Recommended priority:** P0.

---

## 6. Public claims verification

**Current state:** Two specific unverified-claim issues are already logged: (a) `work.zediant.com`'s 48-staff / 97%-satisfaction / 100+-projects figures (Item 5, above), and (b) the live case-studies hub (10 case studies) has not been individually verified line-by-line against the 10 approved case studies (CS-01–CS-10) documented in `context/case_studies.md`.

**Evidence from discovery:** `seo/audits/onpage/initial_onpage_audit.md` §6 ("Case study pages — spot-check recommendation — P2," noted here because it feeds directly into this P0 claims-verification item); `seo/audits/content/initial_content_audit.md` §7 ("Content evidence check"); `seo/data/content_inventory.csv` row for `https://www.zediant.com/case-studies/`.

**Business/SEO impact:** Per `policies/claims-and-compliance.md` §8, case-study metrics must be used exactly as documented — never improved, rounded, reinterpreted, or extrapolated. Until each live case-study page is checked against `case_studies.md`, Zediant cannot be certain its own live site is compliant with its own claims policy, and none of these pages should be used as SEO proof content, internally linked as authoritative, or referenced in new content briefs.

**Recommended action:** Run a dedicated, page-by-page verification pass comparing each of the 10 live case-study pages against the corresponding CS-01–CS-10 entry in `context/case_studies.md` — metrics, customer names, and confidentiality handling, with particular care on CS-02 and CS-06, which `policies/confidentiality.md` §9 flags as requiring special handling and prohibits combining without explicit approval. This is a verification task, not itself a content change — it should be scheduled as its own work item before any of these pages are used in the P0 execution above.

**Exact URL(s) affected:** All 10 live case-study URLs under `https://www.zediant.com/case-studies/` (see `seo/data/content_inventory.csv` and the case-studies hub listing captured in `seo/audits/technical/initial_technical_audit.md`/`seo_baseline.csv`).

**Exact files/assets likely to require modification:** None for the verification step itself. Any page found to contain an inaccurate or over-claimed metric would then require a content edit (CMS — location UNKNOWN).

**Nature of change:** Verification (no site change) → potentially content, if a discrepancy is found.

**Dependencies:** None — can run independently and in parallel with other items. Should complete before any case study is used as a reference in Items 1–4's content work.

**Risk:** Low for the verification step itself. If a discrepancy is found and left uncorrected, risk is the same as any unsupported claim under `policies/claims-and-compliance.md`.

**Rollback approach:** Not applicable to the verification step. Any resulting correction should preserve the prior text until the correction is confirmed accurate.

**Human approval required:** YES for any resulting public claim correction (per the "public claims" trigger in this task's instructions); the verification pass itself does not change anything and can proceed without a separate approval gate beyond the standing read-only/no-publish constraint already in force.

**Recommended priority:** P0 (as a precondition for the site containing accurate, policy-compliant claims — not because it is itself high-effort).

---

## 7. SOC 2 terminology consistency

**Current state:** Not independently re-verified page-by-page in the SEO discovery pass (the discovery's technical/on-page audits did not sample every page for this specific wording). However, `context/services.md`'s own "Critical accuracy warning for all AI agents" documents that Zediant's published materials describe SOC 2 Type II status three different ways — "Aligned," "Certified," and "Compliant" — sometimes on the same page (e.g., the Enterprise Custom Development page reportedly contains both a heading reading "SOC 2 Type II Compliance" and body text reading "Our SOC 2 Type II alignment ensures..."). The homepage was observed in this discovery to display a "SOC 2 Type II" credential badge (exact wording not captured in the fetched summary).

**Evidence from discovery:** `context/services.md` §"Critical accuracy warning for all AI agents" (root context, not a new claim invented here); `seo/strategy/seo_priorities.md` P3-1 ("SOC 2 wording should be checked sitewide for 'aligned' vs. 'certified' consistency once a full crawl is possible"); homepage summary in the original discovery noted a "SOC 2 Type II" badge in the Credentials Section without capturing the exact qualifier used.

**Business/SEO impact:** Per `Claude.md` §13 and `policies/claims-and-compliance.md` §6, Zediant must default to "SOC 2 Type II aligned" and must never write or imply "certified" or "compliant" unless a completed attestation is explicitly confirmed — which the source material states is not currently confirmed. Any page using "certified" or unqualified "compliant" language is a live, public overclaim risk, independent of SEO performance — this is a compliance issue that happens to surface through the SEO audit.

**Recommended action:** Commission a full-site text audit (beyond what the initial SEO discovery pass covered) specifically for every instance of "SOC 2," and normalize all instances to "SOC 2 Type II aligned," removing "certified" and unqualified "compliant" wording, consistent with `services.md`'s own warning and `Claude.md` §13. This plan does not enumerate every page/instance, since the initial discovery did not perform a full-site crawl — that enumeration is itself a prerequisite research step (technical crawl, already flagged as a general P1 gap in `seo/audits/technical/initial_technical_audit.md` §6) before the wording fix can be scoped exactly.

**Exact URL(s) affected:** At minimum, the homepage (badge) and, per `services.md`'s own documentation, the Dedicated Engineering, Enterprise Custom Development, Platform Engineering, and AI-Enabled Product Engineering pages — but this list is drawn from `services.md`'s note about the *previous* site structure and should be re-confirmed against the current live page set (Item 1's outcome may change which URLs these map to) rather than assumed to transfer exactly.

**Exact files/assets likely to require modification:** Page copy and any credential/badge component across the affected pages (CMS — location UNKNOWN).

**Nature of change:** Content/metadata; public claims.

**Dependencies:** Depends on a full-site crawl (not yet performed) to produce an exact, page-by-page instance list before correction. Should be sequenced after the crawl recommended in `seo/audits/technical/initial_technical_audit.md` §6.

**Risk:** Moderate — this is a compliance-adjacent claim, not merely an SEO nicety; leaving "certified" language live carries reputational/commercial risk independent of search performance.

**Rollback approach:** Archive current wording per page before correction.

**Human approval required:** YES — public claims and, per `Claude.md` §13, potential escalation if any prospect-facing certification question arises.

**Recommended priority:** P0.

---

## A. Recommended execution order

1. **work.zediant.com escalation** (Item 5) — start immediately; it is pure escalation with no technical dependency and the longest potential resolution time (external domain, ownership unclear).
2. **Case-study claims verification** (Item 6) — start in parallel; it is a verification task with no site-change risk and unblocks safe reuse of case studies in every other item's eventual content work.
3. **Dedicated Engineering Pods canonical-URL decision** (Item 1) — the highest-impact business decision; should be resolved early since Items 3 and 7's content drafting benefit from knowing the final Pods positioning.
4. **Sitemap regeneration** (Item 2) — can proceed as soon as Item 1's canonical URL is chosen (or in parallel, accepting a possible second pass).
5. **Homepage title/meta rewrite** (Item 3) — sequence after Item 1's decision and after Item 7's SOC 2 wording is settled, so the new copy doesn't need to be revisited.
6. **SOC 2 full-site audit and correction** (Item 7) — commission the crawl now; correction itself can run in parallel with Items 3–4 once the instance list exists.
7. **Digital Presence page resolution** (Item 4) — lowest technical urgency but should not be left indefinitely, given the standing claims-policy conflict; sequence after the capability question is answered.

## B. Items that can be safely automated (once approved)

- Sitemap regeneration (Item 2) — mechanical once the correct URL list is confirmed; low risk, easily reversible.
- Homepage title/meta deployment (Item 3) — mechanical once final copy is approved.
- Redirect/link-fix mechanics for Item 1 — mechanical once the canonical-URL decision is made (the decision itself is not automatable).

None of these should be executed without the human approval already flagged — "safely automated" here means low-risk and reversible once approved, not exempt from approval.

## C. Items requiring human decision

- Which URL becomes the canonical Dedicated Engineering Pods page, and whether a redirect is used (Item 1).
- work.zediant.com's status, ownership, and fate (Item 5).
- Digital Presence page's capability status — retire, rescope, or formally add to `services.md` (Item 4).
- Final approval of homepage title/meta copy (Item 3) and any SOC 2 wording correction (Item 7), per `policies/claims-and-compliance.md`.
- Any case-study correction arising from Item 6's verification.

## D. Items requiring access/credentials not available in this session

- CMS/website admin access to edit navigation, page content, meta tags, and the sitemap (platform unidentified in discovery — see `seo/data/seo_baseline.csv` "Structured data" and "Canonical tags" rows, both UNKNOWN for the same reason).
- Google Search Console and Analytics access, needed to confirm actual indexation and traffic impact of Items 1–3 before and after implementation (currently UNKNOWN per `seo_baseline.csv`).
- Access to `work.zediant.com`'s hosting/DNS and content management, to investigate and act on Item 5.
- A rank-tracking or SERP tool, to properly scope Item 7's full-site SOC 2 audit efficiently (a manual page-by-page check is possible without it, only slower).

## E. Items requiring website developer involvement

- Item 1: navigation link fix and/or new page publication, and any redirect implementation.
- Item 2: sitemap regeneration (unless the CMS exposes this to a non-developer admin).
- Item 3: title/meta tag edit (platform-dependent; may or may not require a developer).
- Item 4: content/metadata edit once the business decision is made.
- Item 5: any technical action on `work.zediant.com` (DNS, redirect, hosting) once its fate is decided.
- Item 7: sitewide find/replace of SOC 2 wording across templates or CMS content blocks, especially if the wording lives in a shared component (e.g., the homepage credential badge) rather than per-page copy.

---

**No implementation has occurred.** This plan is a sequencing and approval-routing document only, built entirely from `seo/data/`, `seo/audits/`, `seo/strategy/seo_priorities.md`, and current `context/`/`policies/` files already on record.
