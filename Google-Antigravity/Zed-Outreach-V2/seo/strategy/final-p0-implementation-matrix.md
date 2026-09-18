# Final P0 SEO Implementation Matrix — Zediant Technologies

Status: Planning only — NO implementation has occurred. No website, DNS, hosting, redirect, sitemap, metadata, CRM, scheduler, or content changes have been made as part of producing this document.
Date: 2026-08-20
Source: derived exclusively from `seo/strategy/p0-implementation-plan.md`, `seo/strategy/gate-1-decision-pack.md`, `seo/audits/technical/initial_technical_audit.md` (as corrected 2026-08-20), `context/company.md`, `context/services.md`, `context/case_studies.md`, `policies/claims-and-compliance.md`, and `policies/revenue-engine-policies.md`. No new discovery was performed and no new findings were introduced — this document classifies and sequences findings already on record.

Classification key:

- **GREEN** — Claude can implement after this matrix is approved. Mechanical/technical, low risk, no unresolved business/claims decision.
- **YELLOW** — Claude may prepare the change (draft copy, draft redirect map, draft file diffs, etc.), but human approval is required before implementation. A decision exists but is already made or narrow enough to prepare against.
- **RED** — A human/business/compliance decision is required before Claude can even prepare the implementation, because the decision itself is not yet resolved or depends on data not available in this session.

---

## Item 1 — Dedicated Engineering Pods canonical URL / navigation

- **Issue:** Original technical audit reported the "Dedicated Engineering Pods" nav link as broken (404), logged as P0.
- **Current verified state:** Corrected 2026-08-20 (`seo/audits/technical/initial_technical_audit.md` §3, Correction/Changelog). The 404 was on a guessed URL, `/services/dedicated-engineering-pods/`, never the real nav target. The actual canonical page, `/services/dedicated-engineering/`, is live and resolves successfully. This was a false positive — there is no broken link.
- **Desired state:** Documentation and any downstream references consistently reflect `/services/dedicated-engineering/` as canonical; no new page created at the guessed `-pods` URL.
- **Exact URL(s):** Canonical: `https://www.zediant.com/services/dedicated-engineering/`. Do not create: `https://www.zediant.com/services/dedicated-engineering-pods/`.
- **Exact file/page affected:** None on the live website (no change needed — the page and link already work). Documentation of record: `seo/audits/technical/initial_technical_audit.md` (already corrected), `seo/strategy/gate-1-decision-pack.md` §3 (already updated), `seo/strategy/p0-implementation-plan.md` §1 (still describes the pre-correction state and should be read alongside the correction, not edited under this matrix's scope).
- **Classification: GREEN**
- **Why:** The underlying finding was false. There is nothing to implement on the live site — the "action" is confirming no page/link/redirect work is needed at all. Recording this as GREEN means: no further approval gate blocks anyone from treating `/services/dedicated-engineering/` as canonical going forward.
- **Required human decision:** None remaining for the canonical URL itself — already confirmed by the business (see gate-1-decision-pack.md §3). Confirm this matrix's disposition (no action) once, for the record.
- **Required access:** None.
- **Dependencies:** None. Item 2 (build-your-team retirement) depends on this being settled, which it is.
- **SEO risk:** None — no change is being made to a working page/link.
- **Business/compliance risk:** None.
- **Rollback approach:** Not applicable — no change is made.
- **Implementation owner:** N/A (no implementation required).
- **Verification method after implementation:** N/A. If ever re-verified, a direct fetch of `/services/dedicated-engineering/` confirming 200 OK is sufficient.

---

## Item 2 — `/services/build-your-team/` retirement (redirect to Dedicated Engineering Pods)

- **Issue:** `/services/build-your-team/` is confirmed obsolete/not in use but is still live, in the sitemap, and internally linked (nav + `/services` hub), overlapping substantially with `/services/dedicated-engineering/`.
- **Current verified state:** Per `seo/strategy/gate-1-decision-pack.md` §3: live (200 OK), titled "Build Your Team | Zediant" / H1 "IT Staff Augmentation," present in sitemap (`priority: 0.9`, `lastmod: 2024-08-21`), internally linked from the main nav dropdown and the `/services` hub, substantial content overlap with `/services/dedicated-engineering/` (same team model, same "30-40%" claim, same AI-workflow theme). Business has confirmed it is obsolete and must not be treated as an active service page. No new Pods page is to be created (see Item 1). No redirect implemented yet.
- **Desired state:** `/services/build-your-team/` no longer presented as an active Zediant service page. Candidate treatment: 301 redirect to `/services/dedicated-engineering/`.
- **Exact URL(s):** From: `https://www.zediant.com/services/build-your-team/`. To (candidate): `https://www.zediant.com/services/dedicated-engineering/`.
- **Exact file/page affected:** The `/services/build-your-team/` page itself; the main nav dropdown entry currently pointing to it; the `/services` hub page listing; redirect rule/config (CMS/server mechanism unidentified — DATA GAP per gate-1-decision-pack.md).
- **Classification: YELLOW**
- **Why:** The business decision to retire this page and treat `/services/dedicated-engineering/` as canonical is already made. Claude can prepare the redirect mapping, the nav/hub link updates, and an archived snapshot of the current page — but implementing a live 301 redirect, removing a live page, and editing global nav is a website change requiring explicit sign-off on the exact mechanism and timing, consistent with `policies/revenue-engine-policies.md`'s standing rule that live-site changes require human approval.
- **Required human decision:** Approve the 301 redirect (vs. 410/removal vs. continued temporary leave-as-is) and its exact destination; approve the timing of execution.
- **Required access:** CMS/website admin access to implement the redirect and edit the nav/hub links; ideally Search Console/backlink data to confirm no indexation/traffic risk is being ignored (flagged as DATA GAP in gate-1-decision-pack.md — recommended but not blocking, since the business decision is already made).
- **Dependencies:** Depends on Item 1 (canonical URL confirmed — done). Should be sequenced with sitemap regeneration (Item 4) so the sitemap doesn't need a second pass.
- **SEO risk:** Low-moderate. A 301 preserves any existing link equity; the page has ~2 years of sitemap presence and internal linking, so an uninformed 410/removal instead of a redirect would be higher risk. Not yet known whether this page holds meaningful external backlinks (DATA GAP).
- **Business/compliance risk:** Low — retiring a confirmed-obsolete page carries no compliance exposure; the risk is purely SEO-continuity, addressed by using a redirect rather than a hard removal.
- **Rollback approach:** Archive the current `/services/build-your-team/` page content before any change; a 301 redirect can be removed/repointed without data loss if it underperforms.
- **Implementation owner:** Claude prepares (redirect map, nav/hub link diff, archived snapshot) after approval; a website developer or CMS admin executes the live redirect and nav change.
- **Verification method after implementation:** Direct fetch of `/services/build-your-team/` confirming it 301s to `/services/dedicated-engineering/`; confirm nav dropdown and `/services` hub no longer link to the retired URL; confirm sitemap.xml no longer lists the retired URL as canonical (or lists it only as a redirect source per sitemap conventions).

---

## Item 3 — work.zediant.com retirement

- **Issue:** `work.zediant.com` is a live, separate, authentically Zediant-owned site with legacy/parallel content, an outdated office address, unsupported statistics, and its own Careers section — not documented anywhere in the Revenue Engine.
- **Current verified state:** Per `seo/strategy/gate-1-decision-pack.md` §1: business-confirmed as not used and approved for retirement. No page or sitemap entry on `www.zediant.com` links to it. HTTPS active, no robots.txt (404), no separate sitemap found. Hosting, DNS, backlink, and traffic/indexation data are DATA GAPs.
- **Desired state:** Domain retired via 301 redirect (directionally recommended in gate-1-decision-pack.md) or 410/removal, pending final mechanism approval.
- **Exact URL(s):** `https://work.zediant.com/` and its subpages (not individually enumerated in prior discovery — only the homepage, `/contact`, `/ecommerce-integrations/`, `/about`, and `/robots.txt` have been directly checked).
- **Exact file/page affected:** None yet — no technical change has been made. Eventually: DNS configuration, hosting configuration, and/or redirect rules for the `work.zediant.com` subdomain (mechanism and current administrator unidentified).
- **Classification: RED**
- **Why:** The retirement *decision* is made, but the retirement *mechanism* is not yet determinable — hosting platform, DNS control, and who currently administers the domain are all unknown (DATA GAPs), and no data confirms whether a redirect target/mapping is even feasible without that access. This is not a page edit Claude can prepare a diff for; it requires someone with domain/hosting/DNS access to first establish what levers exist before any implementation, draft or otherwise.
- **Required human decision:** Confirm who administers `work.zediant.com`'s DNS/hosting; approve the retirement mechanism (site-wide 301 vs. 410/removal) and, if a redirect, the destination mapping (homepage vs. per-page, including its Careers content).
- **Required access:** Domain registrar/DNS access; hosting/CMS access for `work.zediant.com`; ideally Search Console/backlink data for the subdomain (currently unavailable).
- **Dependencies:** None on other items — can proceed in parallel, but is currently blocked on access/ownership discovery, not on other P0 work.
- **SEO risk:** Moderate — unknown backlink/indexation profile means either 301 or 410 carries some risk of losing undiscovered value; a 301 is the more conservative default once execution is possible.
- **Business/compliance risk:** Low-moderate while it remains live and undocumented (outdated address, unsupported stats visible to any prospect who finds it); risk decreases once retired.
- **Rollback approach:** Not applicable until access is established and a mechanism is chosen; whatever action is taken should be preceded by an archived snapshot of the domain's current content.
- **Implementation owner:** Whoever currently administers the domain's DNS/hosting (identity unknown — a business/IT question, not a CMS-content one); Claude can prepare the archived snapshot and destination-mapping proposal once ownership is identified.
- **Verification method after implementation:** Direct fetch of `work.zediant.com` confirming the chosen HTTP behavior (301 to specified destination, or 410/removed); re-confirm `www.zediant.com`'s sitemap and pages still contain no reference to it (already true today).

---

## Item 4 — Sitemap regeneration

- **Issue:** `sitemap.xml` is stale (all entries dated `lastmod: 2024-08-21`), omits 3 current service pages and the entire `/blogs/` section, and lists case-study URLs using short slugs that 404 on the live site.
- **Current verified state:** Per `seo/audits/technical/initial_technical_audit.md` §2 (unchanged by the 2026-08-20 correction, which only affected §3): stale, materially inaccurate sitemap, 22 entries, missing current-architecture URLs.
- **Desired state:** Sitemap regenerated to reflect the current, approved site architecture — correct case-study slugs, current service pages (including Item 2's outcome once executed), blog URLs, accurate `lastmod` values.
- **Exact URL(s):** `https://www.zediant.com/sitemap.xml`; indirectly, every URL it should list.
- **Exact file/page affected:** `sitemap.xml` (CMS/sitemap-generator mechanism unidentified — UNKNOWN per `seo/data/seo_baseline.csv`).
- **Classification: YELLOW**
- **Why:** The correct target-state URL list is fully determinable from already-approved sources (current live navigation/architecture, `context/services.md`) — Claude can prepare the exact regenerated sitemap content. But sitemap.xml is a live website file; per `policies/revenue-engine-policies.md` and the standing instruction in this and prior tasks, any live-site file change requires explicit human approval before deployment, even when mechanically low-risk.
- **Required human decision:** Approve deployment of the regenerated sitemap; confirm whether to regenerate now or wait for Item 2's redirect to land first (to avoid a second pass).
- **Required access:** CMS/sitemap-generator access to deploy (mechanism UNKNOWN, requires developer/CMS-admin).
- **Dependencies:** Best sequenced after Item 2 (build-your-team retirement) so the sitemap reflects the post-redirect URL set in one pass; not strictly blocked by it.
- **SEO risk:** Low — an accurate sitemap can only help crawl efficiency and discovery; the main risk is a wasted second regeneration pass if sequenced before Item 2.
- **Business/compliance risk:** None.
- **Rollback approach:** Retain a copy of the current stale sitemap.xml content (already captured in `seo/data/seo_baseline.csv`) before replacing it.
- **Implementation owner:** Claude prepares the corrected sitemap content; a developer/CMS admin deploys it.
- **Verification method after implementation:** Fetch `sitemap.xml` and confirm: all current service pages present, correct long-form case-study slugs (spot-check a sample against the live case-studies hub), `/blogs/` section present, no dead/404 URLs listed, `lastmod` values updated.

---

## Item 5 — Homepage title/meta alignment

- **Issue:** Homepage `<title>` and meta description describe a generic "digital solutions" agency and do not mention the current four published services or the H1's "AI-Enabled Product Engineering" positioning.
- **Current verified state:** Per `seo/audits/onpage/initial_onpage_audit.md` §1 / `seo/strategy/p0-implementation-plan.md` §3: Title = "Innovative Digital Solutions for Business Growth - Zediant Technologies." Meta description references "SaaS development, e-commerce, cloud solutions" — none of which match the current four service names (AI-Enabled Product Engineering, Dedicated Engineering Pods, Platform Engineering, Enterprise Custom Development). H1 is unchanged and not flagged.
- **Desired state:** Title/meta rewritten to reflect current positioning and lead service names, consistent with the H1 and `context/services.md`.
- **Exact URL(s):** `https://www.zediant.com/`.
- **Exact file/page affected:** Homepage `<title>` and `<meta name="description">` tags (CMS page-settings field — exact location UNKNOWN).
- **Classification: YELLOW**
- **Why:** The target positioning is fully grounded in already-approved sources (`context/services.md`, the live H1), so Claude can draft exact replacement copy. But it is live, public-facing copy on the homepage — per the claims-and-compliance discipline, any new copy must be checked against `policies/claims-and-compliance.md` before publication, and any homepage change requires human approval regardless of risk level.
- **Required human decision:** Approve the exact drafted title/meta text before publication; confirm sequencing relative to Item 7 (SOC 2 wording) so the copy isn't revisited twice if the homepage badge/claim wording also changes.
- **Required access:** CMS/developer access to edit the title/meta fields (location UNKNOWN).
- **Dependencies:** Best drafted after Item 1 (Pods positioning confirmed — done) and sequenced alongside/after Item 7 (SOC 2 wording), so the final copy doesn't need a second revision.
- **SEO risk:** Low — a title/meta change is easily reverted and carries no structural risk to the site.
- **Business/compliance risk:** Low, provided the new copy is checked against `policies/claims-and-compliance.md` before publication (no new unsupported claim, e.g. no certification language introduced here).
- **Rollback approach:** The exact current title/meta text is already captured verbatim in `seo/data/seo_baseline.csv`; restore from there if needed.
- **Implementation owner:** Claude drafts the replacement copy; a developer/CMS admin deploys it after approval.
- **Verification method after implementation:** Fetch the homepage and confirm the new `<title>`/`<meta description>` match the approved copy and reference current, `services.md`-documented capabilities only.

---

## Item 6 — Digital Presence page claims alignment

- **Issue:** `/services/digital-presence/` advertises "SEO to social media marketing" and broader digital-marketing services that are explicitly excluded in `context/services.md`'s "Not offered" list.
- **Current verified state:** Per `seo/audits/onpage/initial_onpage_audit.md` §3: live page (H1 "Digital Presence Lab") claims SEO/social-media-marketing capability not documented as an approved Zediant service. Per `seo/strategy/gate-1-decision-pack.md`, the page's web/mobile/PWA/e-commerce/custom-development content is legitimately alignable with documented services; its marketing/SEO/brand-identity content is not.
- **Desired state:** Legitimate development-related content (web/mobile/PWA/e-commerce/custom-development) retained. Unsupported SEO/social-media/brand-identity positioning removed, unless a human separately approves adding digital marketing as a formally documented Zediant capability.
- **Exact URL(s):** `https://www.zediant.com/services/digital-presence/`.
- **Exact file/page affected:** The page's body content and meta description (CMS — location UNKNOWN); potentially `context/services.md` only if the business chooses to formally add the capability (a business-context change, outside SEO-Skill scope regardless of outcome).
- **Classification: RED**
- **Why:** Which parts of the page's content are "legitimate development-related content to retain" versus "unsupported marketing positioning to remove" is directly determinable and could be prepared — but the overarching business question (is digital marketing a real, to-be-documented Zediant capability, or is this page simply overclaiming?) is not resolved, and rewriting the page before that question is answered risks either under- or over-stating what Zediant offers. This is a business-capability decision, not a copy-editing task.
- **Required human decision:** Decide whether digital/social-media marketing is a real, approved Zediant capability that should be added to `context/services.md` through the proper business-context process, or whether the page should be retired/rescoped to remove the unsupported claims entirely.
- **Required access:** None beyond the business decision itself; CMS access once the direction is set.
- **Dependencies:** Must be resolved before this page is used in any keyword targeting, internal linking, or content-brief work elsewhere in the SEO program.
- **SEO risk:** Moderate — leaving it as-is continues to risk mismatched-expectation enquiries; changing it without the capability decision risks mis-describing Zediant's actual offer either direction.
- **Business/compliance risk:** Moderate — an active claims-policy conflict per `policies/claims-and-compliance.md` §4 until resolved.
- **Rollback approach:** Archive current page content before any edit; if retired, a redirect decision would follow separately (its own approval gate).
- **Implementation owner:** Rajeev/business owner decides capability status; Claude prepares the content rewrite (retain vs. remove split) once the decision is made.
- **Verification method after implementation:** Fetch the page and confirm remaining content matches `context/services.md`'s documented capabilities exactly, with no SEO/social-media/brand-identity claims unless `services.md` has been formally updated to include them.

---

## Item 7 — SOC 2 terminology normalization

- **Issue:** Zediant's public site uses "Aligned," "Certified," and "Compliant" inconsistently to describe SOC 2 Type II status, sometimes on the same page.
- **Current verified state:** Per `seo/strategy/gate-1-decision-pack.md` §5 (live re-verification across 9 checked service pages plus homepage): 9 "aligned" occurrences (policy-compliant), 6 "certified" occurrences (non-compliant), 2 "compliance/compliant" occurrences (ambiguous), 2 unqualified badge-image occurrences, across the pages checked; case-study pages, blog posts, and remaining About subpages not yet individually checked (DATA GAP for full-site completeness). No source reviewed (`context/company.md`, `context/services.md`, `policies/claims-and-compliance.md`) confirms an actual completed SOC 2 attestation.
- **Desired state:** All public wording normalized to "SOC 2 Type II aligned" per `policies/claims-and-compliance.md` §6 and `Claude.md` §13. "Certified" and unqualified "compliant" language removed unless a completed attestation is independently verified and explicitly approved.
- **Exact URL(s):** At minimum the pages already enumerated in gate-1-decision-pack.md §5: homepage, `/services/ai-enabled-product-engineering/`, `/services/platform-engineering/`, `/services/enterprise-custom-development/`, `/services/build-your-team/` (badge only — note this page is separately being retired per Item 2). Case studies, blog posts, and remaining About subpages remain unchecked (DATA GAP).
- **Exact file/page affected:** Page copy and the credential/badge component (shared component vs. per-page copy is unconfirmed — CMS location UNKNOWN) on each affected page.
- **Classification: YELLOW**
- **Why:** The correction rule itself is unambiguous and already-approved policy ("aligned," never "certified" or unqualified "compliant" absent explicit attestation) — Claude can prepare the exact wording fix for every already-identified occurrence. Implementation is withheld pending approval because it is live public claims copy across multiple pages, and because a full-site completeness check (case studies, blog, remaining About subpages) has not yet been done — approval should cover both the enumerated fixes and how to handle the DATA GAP pages.
- **Required human decision:** Approve normalizing all enumerated "certified"/"compliant" instances to "aligned"; decide whether to commission a full-site crawl first to close the completeness DATA GAP, or proceed with the already-identified pages now and correct any remaining instances found later.
- **Required access:** CMS/developer access to edit page copy and the credential/badge component, especially if it is a shared component rather than per-page copy.
- **Dependencies:** None blocking — can proceed independently once approved. Best sequenced before/alongside Item 5 (homepage title/meta) if the homepage badge wording is also being touched, to avoid two separate homepage edits.
- **SEO risk:** Low — a wording normalization has no negative SEO impact and removes an inconsistency that itself could read as untrustworthy to a careful visitor.
- **Business/compliance risk:** High if left uncorrected — "certified" and unqualified "compliant" are live overclaims per standing policy, independent of SEO performance; this is the most compliance-sensitive item in this matrix.
- **Rollback approach:** Archive current wording per page before correction.
- **Implementation owner:** Claude drafts the exact per-page wording corrections; a developer/CMS admin deploys them.
- **Verification method after implementation:** Fetch each affected page and confirm every SOC 2 reference reads "SOC 2 Type II aligned" (or equivalent policy-compliant phrasing), with no remaining "certified" or unqualified "compliant"/"compliance" instances; re-check the badge component specifically.

---

## Item 8 — CS-07 and CS-08 case-study discrepancies

- **Issue:** Two live case-study pages contain figures that do not match the approved record in `context/case_studies.md`.
- **Current verified state:** Per `seo/strategy/gate-1-decision-pack.md` §2: CS-07 (`/case-studies/development-of-crypto-apps-with-ionic`) — live page states team of 4, duration "three months," and discloses "an Australian entrepreneur," versus `case_studies.md`'s documented team of 3, duration 5 months, and country/company explicitly marked "not published." CS-08 (`/case-studies/redeveloping-website-for-a-leading-material-handling-company-in-australia`, mapping inferred from subject matter) — live page states "50% increase in page views" and "20% increase in lead conversions," versus `case_studies.md`'s documented "30% increase in website traffic (company-stated)." Which source (live page or `case_studies.md`) holds the correct figures is unresolved — the underlying original project records are not accessible in this session.
- **Desired state:** Live pages and `case_studies.md` in agreement, using whichever figures are confirmed correct by someone with access to the original project records, per `policies/claims-and-compliance.md` §8 (published metrics must be used exactly as documented, never invented, extrapolated, or substituted).
- **Exact URL(s):** `https://www.zediant.com/case-studies/development-of-crypto-apps-with-ionic` (CS-07); `https://www.zediant.com/case-studies/redeveloping-website-for-a-leading-material-handling-company-in-australia` (CS-08, mapping to be confirmed).
- **Exact file/page affected:** The two live case-study pages (CMS — location UNKNOWN); `context/case_studies.md` (a business-context file — edits to it are a business-context change, outside SEO-Skill scope regardless of outcome).
- **Classification: RED**
- **Why:** Neither this session nor any project file can determine which set of figures is factually correct. Editing either the live pages or `case_studies.md` without that confirmation risks enshrining a wrong number as the new "approved" record. Per explicit instruction in this task, public claims on these pages must not be modified until the correct business facts are confirmed.
- **Required human decision:** Confirm, from original project records, the correct team size/duration/country disclosure for CS-07 and the correct traffic/conversion metric for CS-08; confirm the CS-08 URL-to-case-study-ID mapping (currently inferred from subject matter, not an explicit on-page ID).
- **Required access:** Original project records/delivery documentation for both engagements (not available in this session).
- **Dependencies:** None on other items.
- **SEO risk:** Low — no change is being made; the risk of inaction is compliance-facing, not SEO-facing.
- **Business/compliance risk:** Moderate — per `policies/claims-and-compliance.md` §8, a live page currently displays at least one metric (CS-08) not found in the approved source; this is an open compliance question until resolved, but correcting it incorrectly (guessing which side is right) would itself create a new compliance problem.
- **Rollback approach:** Not applicable — no change is being made pending the human decision. Once a correction is authorized, archive the pre-correction text on whichever side is changed.
- **Implementation owner:** A human with access to original project records makes the factual determination; Claude prepares the resulting page/`case_studies.md` correction once told which figures are correct.
- **Verification method after implementation:** Once corrected, re-fetch both live pages and confirm exact figure agreement with the (possibly updated) `context/case_studies.md` entries.

---

## Implementation Sequence

| Phase | Items | Rationale |
|---|---|---|
| **Phase 1 — Safe technical fixes** | Item 1 (Dedicated Engineering Pods — no action needed, confirm disposition only) | GREEN item with no live-site change required; establishes the confirmed canonical URL as the reference point for every later item that touches Pods positioning. |
| **Phase 2 — Approved content/metadata fixes** | Item 4 (sitemap regeneration — draft), Item 5 (homepage title/meta — draft), Item 7 (SOC 2 wording — draft) | All three are YELLOW: target state is fully determinable from already-approved sources, so Claude can prepare exact diffs now. Sequenced before Phase 3 so the sitemap and homepage copy only need to be touched once, after Item 2's redirect outcome is known where relevant. Deployment of each still requires its own approval, per each item's classification. |
| **Phase 3 — Redirect/retirement actions** | Item 2 (`/services/build-your-team/` → `/services/dedicated-engineering/` redirect), Item 3 (work.zediant.com retirement) | Both involve retiring/redirecting a live URL or domain. Item 2 is YELLOW (decision made, mechanism to be approved); Item 3 is RED (decision made, but mechanism blocked on unresolved access/ownership). Sequenced after Phase 2 so sitemap regeneration (Item 4) can reflect Item 2's outcome in one pass rather than two. |
| **Phase 4 — Claims/case-study corrections** | Item 6 (Digital Presence claims), Item 8 (CS-07/CS-08 discrepancies) | Both RED — blocked on a business-capability decision (Item 6) or missing original-source facts (Item 8) that this session cannot resolve. Sequenced last among "current P0 scope" items since neither has a technical dependency on Phases 1–3, but both require an external decision/input before any drafting can safely proceed. |
| **Phase 5 — SEO growth work** | Not in scope of this P0 matrix. | New keyword targeting, new content, internal-linking expansion, and backlink work should not begin until Items 6 and 8 are resolved (per `seo/strategy/p0-implementation-plan.md`'s own sequencing notes — unresolved claims/case-study pages should not be used as reference content for new SEO work). Explicitly deferred, not part of this P0 implementation pass. |

---

## Explicitly Out of Scope

The following must NOT be touched, modified, or acted on during P0 implementation of this matrix, regardless of any P0 item's approval status:

- Zoho CRM (records, fields, schema, or configuration)
- Scheduler (Scheduler 1 / Scheduler 2 configuration or runs)
- Saleshandy (sequences, campaigns, sending configuration)
- Apollo (searches, enrichment, sequences, tasks)
- Email sequences and outreach content
- LinkedIn outreach workflows
- Revenue Engine runtime skills (`skills/*.skill`, `skills/seo/*.skill` logic itself — as distinct from the SEO content those skills may reference)
- Any website page not explicitly listed in Items 1–8 above
- New SEO content, new keyword targeting, or new content briefs (Phase 5, explicitly deferred)
- Backlink acquisition or outreach for links
- Paid advertising (search, social, or display)

---

**No implementation has occurred.** This matrix is a classification and sequencing document only, built entirely from already-approved project files listed in the Source line above. STOP — awaiting approval before any GREEN or YELLOW item proceeds to implementation, and awaiting the underlying decisions for every RED item.
