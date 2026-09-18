# 07 — Priority Action Plan & Executive Summary

Status: Read-only recommendations. **No website, metadata, navigation, or content changes have been made.** Everything below requires human approval before implementation, per this task's own instructions and `context/seo/seo_rules.md` §11.

## What is already good

- **Global navigation and footer** are consistent, complete, and give every core page (Home, 4 Services, 4 About, Case Studies, Blogs) mutual reachability.
- **Nav dropdown taglines** ("Built with AI," "Scale with Pods," "Core That Scales," "Built for Your Business") are sharp, differentiated micro-copy — better than most of the body content beneath them.
- **Anchor text discipline** — no "click here"/"read more" found anywhere in this pass; anchors are consistently descriptive.
- **Dedicated Engineering Pods page** — the site's best-executed service page: a named, ownable pod-role model (Strategist/Engine/Gatekeeper/Orchestrator) and three named tiers (Foundation/Growth/Enterprise Pod).
- **Engineering Excellence page** — a genuinely specific, credible delivery-lifecycle framework, currently underused elsewhere on the site.
- **Case-study metric discipline** — 7 of 10 case studies match `context/case_studies.md` exactly, including two pages that correctly *omit* figures the approved record explicitly warns against.
- **Case-study confidentiality handling** — appropriately restrained naming/detail on 9 of 10 case studies.

## Critical problems

1. **SOC 2 wording is wrong, and more widespread than previously documented.** "Certified" (non-compliant) appears repeatedly across the Homepage, all 4 service pages, and — most seriously — the dedicated Trust & Compliance page itself, which flatly states "Zediant is a SOC 2 Type II certified organization." Policy requires "aligned" absent a confirmed attestation (`policies/claims-and-compliance.md` §6). This is the single highest-priority content fix in this audit.
2. **13 of ~20 live blog posts are orphaned** — unreachable from `/blogs/` due to a hub template/pagination defect (`/blogs/2/` 404s). Several of the site's best on-strategy posts (the full ZCoupler comparison cluster) are among them.
3. **Zero internal links exist between service pages and case studies, in either direction**, across all 4 services and all 10 case studies.
4. **Enterprise Custom Development's H1 narrows its audience to "Public Limited Companies (PLCs)"** — unsupported by the page's own body content or by `campaigns.md` C5's actual documented ICP.
5. **AI-Enabled Product Engineering's positioning drifts toward generic "AI-first engineering firm" claims** rather than the AI-assisted-delivery-methodology framing `policies/claims-and-compliance.md` §5 requires, and its H1 never uses "product engineering."
6. **Platform Engineering claims "99.99% availability"** — the exact figure explicitly prohibited elsewhere in the approved record for lack of evidentiary support.
7. **Two unresolved case-study data conflicts** (CS-07 team/duration/country; CS-08 traffic/conversion metrics) — reconfirmed live, unchanged since the 2026-08-20 decision pack; still awaiting a human with access to original project records.
8. **The four service pages share a near-identical structural template** (same 30–40% stat, same 4-icon "AI workflow" grid shape) that undercuts the differentiation Section 12 of this brief specifically asked to check for.

## High-priority changes

- Correct SOC 2 wording sitewide (Critical Problem 1).
- Fix the blog-hub pagination/listing defect (Critical Problem 2) — requires developer/CMS access; flagged, not diagnosed to root cause in this pass.
- Add case-study ↔ service-page cross-links in both directions (Critical Problem 3) — no new content required, pure linking work.
- Rewrite the Enterprise Custom Development H1 to drop the PLC-only framing (Critical Problem 4).
- Reframe AI-Enabled Product Engineering's hero/H1 and remove generic AI-depth claims (Critical Problem 5).
- Correct or remove the Platform Engineering "99.99% availability" claim (Critical Problem 6).

## Medium-priority changes

- Add named engagement tiers to Platform Engineering and Enterprise Custom Development (Dedicated Engineering already has this).
- Expand `/services/middleware-integration/` with ZCoupler branded framing (the clearest genuine content gap found — see `03-content-gap-analysis.md`).
- Remove/replace the homepage's "Ready to ditch ecommerce headaches?" section.
- Add named-stack legacy-modernization content (.NET Framework, Java EE) to Enterprise Custom Development.
- Resolve CS-07/CS-08 data conflicts (requires a human with original project records, not a content decision this audit can make).

## Low-priority changes

- Consolidate terminology ("AI-enabled" vs. "AI-powered" vs. "AI-first"; "Bespoke" vs. "Custom").
- Consider consolidating the three overlapping ZCoupler-in-industry blog posts into one deeper canonical piece (future consideration only — nothing deleted now).
- Verify homepage testimonial quotes against an approved source.
- Verify the "Elite 1% of engineers" claim on the Careers page.
- Refresh the 3 generic/dated "web development trends" blog posts, or reassess their strategic fit.
- Investigate whether `/about-us/team-culture` and `/about-us/how-we-work` (present in the stale sitemap but absent from current nav) still resolve, and if not, ensure they're excluded from the sitemap regeneration already scoped in prior audits.

## Pages that should NOT be changed

- `/services/dedicated-engineering/` structure and pod-role/tier model (light SOC2 wording fix only).
- `/about-us/engineering-excellence/` (light SOC2 wording fix only).
- Global nav/footer structure and dropdown taglines.
- Case-study page template/structure (Overview → Challenges → Solution → Result → Conclusion).
- `/privacy-policy/`, `/terms-of-use/` — standard legal pages, no SEO action needed.
- `/about-us/careers/` structure (flag the one unverified claim only; the page's purpose and format are sound).

## Potential new pages

**None recommended at this time.** See `03-content-gap-analysis.md` — two candidates (a standalone ZCoupler product page, a "product engineering company" pillar page) were evaluated and both fail the brief's own justification bar in favor of expanding existing pages instead. This is itself a notable finding: Zediant's current 11-page architecture (Home / 4 Services / 4 About / Case Studies / Blogs) is close to sufficient for its current commercial priorities.

## Recommended implementation order

1. **SOC 2 wording correction sitewide** (highest compliance risk, lowest implementation effort, touches the most pages).
2. **Blog-hub pagination/listing fix** (technical investigation with real CMS/repo access — needed before any blog content strategy work is worth doing).
3. **Case-study ↔ service-page cross-linking**, using the pairings in `04-internal-linking-audit.md` and `08-page-content-blueprints.md` (no new content, pure linking).
4. **Enterprise Custom Development H1 fix** and **Platform Engineering "99.99%" claim correction** (both are narrow, contained edits).
5. **AI-Enabled Product Engineering rewrite** (the most substantial single-page content project in this plan).
6. **ZCoupler expansion of `/services/middleware-integration/`** (the one genuine content-gap build recommended in this audit).
7. Medium/low-priority items, sequenced opportunistically.
8. **CS-07/CS-08 data-conflict resolution and the sitemap regeneration** already scoped in `seo/strategy/final-p0-implementation-matrix.md` remain owned by that document's existing approval process — this audit does not duplicate or re-decide them, only reconfirms they're still open.

---

## Final output to Rajeev (Section 32)

1. **Website pages audited (live-fetched):** 25 — Homepage, 4 service pages, 4 About pages, Case Studies hub, Blogs hub, 10 individual case studies, 20 individual blog posts, plus sitemap.xml and robots.txt as technical assets. (25 content pages + 2 technical assets.)
2. **SEO-mapped pages (in the approved Excel file):** 44 of 44 successfully mapped to a live page. **0 UNMAPPED.**
3. **Page classification counts** (core pages only — the 10 case studies and 20 blog posts are individually classified in `05` and `06` rather than folded into this count, since none of them require a distinct KEEP/OPTIMIZE/REWRITE/MERGE/REVIEW/CREATE call beyond "add missing cross-links," which is a shared, uniform recommendation across all 30):
   - **KEEP:** 4 (`/services/dedicated-engineering/`'s structure, `/about-us/engineering-excellence/`, `/privacy-policy/`, `/terms-of-use/`)
   - **OPTIMIZE:** 6 (Homepage, `/services/platform-engineering/`, `/services/dedicated-engineering/` for case-study linking, `/about-us/who-we-are/`, `/about-us/trust-compliance/`, `/case-studies/` hub)
   - **REWRITE:** 3 (`/services/ai-enabled-product-engineering/`, `/services/enterprise-custom-development/`, `/blogs/` hub)
   - **MERGE:** 0 (no merge candidates identified among the current-architecture pages in scope; the previously-documented legacy-page cannibalization pairs — saas-development/cloud-security/build-your-team/digital-presence — are outside this audit's scope, which was limited to the current approved 4-service architecture per the brief's own instruction)
   - **REVIEW:** 1 (`/about-us/careers/` — one unverified claim only, otherwise fine)
   - **CREATE:** 0
4. **Top 10 SEO/content issues:** (1) sitewide SOC2 "certified" vs. "aligned" wording, worst on the Trust & Compliance page itself; (2) 13 orphaned blog posts; (3) zero case-study↔service cross-links; (4) Enterprise Custom Development's PLC-only H1; (5) AI-Enabled Product Engineering's generic-AI positioning drift; (6) Platform Engineering's unsupported "99.99% availability" claim; (7) four service pages sharing a near-identical structural template; (8) unresolved CS-07/CS-08 data conflicts; (9) homepage's leftover "ecommerce headaches" section; (10) stale, 22-URL sitemap unchanged since 2024-08-21 (already documented, reconfirmed).
5. **Top 10 content opportunities:** (1) ZCoupler expansion of the Middleware Integration service page; (2) fixing blog-hub discoverability; (3) case-study cross-linking; (4) roadmap-vs-headcount content for AI-Enabled Product Engineering; (5) named engagement tiers for Platform Engineering and Enterprise Custom Development; (6) named-stack legacy-modernization content; (7) staff-augmentation-vs-pods comparison content; (8) featuring the ZCoupler blog cluster once discoverable; (9) leveraging the Engineering Excellence delivery framework on more pages; (10) expanding homepage case-study coverage beyond the current 4 featured.
6. **Top internal-linking opportunities:** service↔case-study cross-links (both directions, all 4 services); fixing the blog-hub listing bug; linking `leveraging-sitecore` blog post directly to its matching CS-08 case study; linking EaaS and IT-outsourcing posts to their single best-fit service page rather than a generic set.
7. **Top service-positioning issues:** AI-Enabled Product Engineering's drift toward generic AI-development claims; Enterprise Custom Development's PLC-only audience framing; structural near-duplication across all four service pages; inconsistent SOC2 terminology undermining the Trust & Compliance page's own credibility.
8. **Recommended priority sequence:** SOC2 wording → blog-hub fix → case-study cross-linking → Enterprise Custom Development H1 + Platform Engineering claim fix → AI-Enabled Product Engineering rewrite → ZCoupler expansion → remaining medium/low items.
9. **Files created in `seo-audit/`:** `01-page-audit.md`, `02-service-positioning-audit.md`, `03-content-gap-analysis.md`, `04-internal-linking-audit.md`, `05-case-study-audit.md`, `06-blog-audit.md`, `07-priority-action-plan.md` (this file), `08-page-content-blueprints.md`.

**No website, CRM, navigation, metadata, or content changes were made in producing this audit.**
