# Gate 1 — Decision Pack

Status: Verification and business-decision preparation only. NO website, CRM, scheduler, or metadata changes have been made. No content has been published. No redirects or canonical tags have been created or changed. sitemap.xml has not been touched.
Date: 2026-08-20
Scope: work.zediant.com; case-study claims verification; Dedicated Engineering Pods canonical-URL analysis; Digital Presence page decision analysis; SOC 2 sitewide wording audit. All evidence below comes from the current project files (`context/`, `policies/`, `seo/data/`, `seo/audits/`, `seo/strategy/`) and from directly and currently fetching public, unauthenticated pages on zediant.com / work.zediant.com. Nothing has been invented. Every finding is labeled **FACT**, **DATA GAP**, or **RECOMMENDATION**.

---

## 1. work.zediant.com

**Business decision confirmed (2026-08-20):** `work.zediant.com` is **not used by Zediant** and is **approved for retirement.**

- **Business decision:** RETIRE
- **Implementation:** NOT YET EXECUTED
- **Human approval:** REQUIRED (for the actual retirement/removal action itself — see Section 5 below)

This section is now documentation and **implementation planning only**. Per explicit instruction, `work.zediant.com` has not been removed, redirected, disabled, or otherwise modified in this pass, and will not be until a human explicitly authorizes the specific retirement action.

### 1.1 Current known state (already established in prior discovery)

- **FACT** — `work.zediant.com` is live and publicly reachable (confirmed by direct fetch of its homepage, `/contact`, and `/ecommerce-integrations/`).
- **FACT** — It is authentically associated with Zediant: its published phone number, `+91 33 4001 2541`, and email, `info@zediant.com`, are identical to the phone and email documented in `context/company.md`. This is common ownership, not a third-party or unrelated site.
- **FACT** — It contains legacy/parallel website content: its own navigation and service list (Web Development, Mobile App Development, E-commerce Integrations, API Development, SaaS Products, Cloud Solutions, Staff Augmentation, plus About/Careers/Case Studies/Contact) differs in structure and wording from the current `www.zediant.com` navigation (About Us, Services [AI-enabled Product Engineering, Dedicated Engineering Pods, Platform Engineering, Enterprise Custom Development], Case Studies, Blogs). Footer copyright reads "© 2023 by Zediant Technologies," indicating the content predates the current site.
- **FACT** — It has its own Careers content, distinct from and not mirrored on the current `www.zediant.com` site.
- **FACT** — It has a different office address from current company context: its `/contact` page lists "Shaila Tower J1/16, EP Block, Salt Lake City, Sector-V, Kolkata," versus the HQ address documented in `context/company.md`, "Ergo Tower, Unit-1302, EP & GP Block, Salt Lake City, Sector-V, Kolkata, India" — same district, different building and unit.
- **FACT** — Other material discrepancies already identified during discovery: its `/contact` page states "Sydney - Opening Soon" (no Sydney office is documented anywhere in `context/company.md`); its homepage states 48 team members (vs. `company.md`'s documented 25–35), a 97% satisfaction rate, and 100+ projects — none of these figures appear in any approved source.

### 1.2 Technical actions that will eventually be required (assessed today, read-only)

1. **Is the subdomain controlled by Zediant?** **FACT** — Yes, ownership is confirmed by the matching phone/email in section 1.1 above. **DATA GAP** — which team/individual currently administers the domain, hosting account, and DNS is not documented in any `context/` or `policies/` file and is not determinable from a public page fetch.
2. **Hosting/platform, if accessible:** **DATA GAP** — not identifiable from a public page fetch alone; would require DNS/WHOIS lookup or hosting-panel access, neither available in this session.
3. **DNS configuration, if accessible:** **DATA GAP** — not identifiable from the tools available in this session (no DNS-lookup capability, no registrar/DNS-provider access).
4. **Is HTTP/HTTPS active?** **FACT** — HTTPS is active; the domain was successfully fetched over `https://work.zediant.com/` and returned content (confirmed again today).
5. **robots.txt/sitemap status:** **FACT** — `https://work.zediant.com/robots.txt` returns a 404 (no robots.txt file exists, re-confirmed today). There is therefore no declared sitemap and no explicit crawl directive either way — the domain is not technically blocked from indexing. No separate sitemap.xml was located for this subdomain in any prior or current check.
6. **Does any page on the main `www.zediant.com` site link to `work.zediant.com`?** **FACT** — No. The current `www.zediant.com` homepage HTML/text was checked today and contains no link, href, or mention of `work.zediant.com`. **FACT** — The current `www.zediant.com` sitemap.xml was checked today and contains no reference to `work.zediant.com`; all sitemap URLs use the primary domain only. **DATA GAP** — this confirms the homepage and sitemap specifically; a full site-wide crawl of every `www.zediant.com` page would be needed to rule out an isolated link elsewhere (e.g., an old blog post or footer variant), which has not been performed in this session.
7. **Should the subdomain be (A) 301 redirected to an appropriate main-domain destination, or (B) retired/removed with appropriate HTTP handling?** See Recommendation below.

### 1.3 DATA GAPS (explicitly not invented)

- **DATA GAP** — Backlink data: whether any external sites link to `work.zediant.com` is unknown; no backlink tool is available in this session.
- **DATA GAP** — Traffic/ranking data: whether `work.zediant.com` currently receives organic traffic, ranks for any queries, or is indexed in a way that competes with `www.zediant.com` cannot be confirmed without Search Console/Analytics access, which is not available in this session.
- **DATA GAP** — Hosting, DNS, and domain-administration details, as noted in 1.2 above.
- **DATA GAP** — Whether `work.zediant.com` is actively promoted or linked anywhere off-site (ads, business cards, partner directories, email signatures, social profiles) cannot be determined from the tools available in this session.

### RECOMMENDATION

Based only on the evidence available in this session, **Option B (retire/remove with appropriate HTTP handling, most likely a site-wide 301 to the corresponding page or the homepage on `www.zediant.com`) is the safer default direction**, since: (a) the business has confirmed the site is not in use, (b) no page on the current `www.zediant.com` site or its sitemap links to it, so removing it creates no known internal-linking breakage, and (c) a 301 (rather than a bare 410/removal) is the conservative choice if `work.zediant.com` turns out to hold any undiscovered backlink or indexation value, since a redirect preserves any such value while a hard removal would not. This is a directional recommendation only — the DATA GAPs above (backlinks, traffic, indexation, hosting/DNS control) should ideally be closed before finalizing between 301-redirect and 410/removal, and the actual destination URL(s) for a redirect (homepage vs. per-page mapping, e.g. its Careers content vs. a current careers page if one exists) has not been scoped in this pass.

**Actual retirement/removal of `work.zediant.com` — in any form (redirect, DNS change, hosting change, content removal, or disabling) — is HUMAN APPROVAL REQUIRED and has NOT been executed.**

---

## 2. Case-study claims verification

Method: each of the 10 live case-study pages under `https://www.zediant.com/case-studies/` was fetched directly and compared against its corresponding CS-01–CS-10 entry in `context/case_studies.md`.

### FACTS — matches (no discrepancy found)

- **FACT** — CS-01 (Middleware Integration for Multiple Large DMS): live page content (DMS platforms named ERA, CDK, Pentana; Zediant Middleware; qualitative-only outcomes; APAC/UK/USA reach) matches `case_studies.md` exactly. No metric appears on the live page, consistent with `case_studies.md`'s "No published metric."
- **FACT** — CS-02 (Wholesale Parts CRM): live page states "50+ dealers across ASPAC" and "5,700 customers" — matches `case_studies.md`'s documented metrics exactly. Team size (12) and duration (18 months) are not shown on the live page, consistent with `case_studies.md`'s Internal Notes marking the per-role split as unpublished.
- **FACT** — CS-04 (11Wickets): live page's technical description (EC2, Auto Scaling, Load Balancing, MySQL Galera Cluster) and qualitative-only outcomes match `case_studies.md` exactly. The live page does not display the unsupported "99.99% availability" figure that `case_studies.md` explicitly warns must never be attached to this engagement — good.
- **FACT** — CS-06 (Team Augmentation for Automotive Software): live page states test coverage improved "from 70% to 93%," the developer's manual was completed "after a month," the relationship spans "3+ years," and client scale figures (186 countries / 50 OEM manufacturers / 250,000+ industry experts) — every one of these matches `case_studies.md`'s documented metrics exactly.
- **FACT** — CS-09 (BigCommerce Integration): live page's qualitative description matches `case_studies.md`; it does not repeat the excluded "expert-level BigCommerce" claim that `case_studies.md` explicitly instructs must not be restated — good.
- **FACT** — CS-10 (WordPress Migration, poker platform): live page's qualitative outcomes (backend smooth, easier content updates, improved SEO/organic traffic, reduced load time) match `case_studies.md` exactly, and no client name appears — good.
- **FACT** — CS-05 (Real-Time Executive Dashboards / Diamond Professional Consultants): live page names "Diamond Professional Consultants," describes the work as executive dashboard development in business intelligence/performance management, and does not describe the customer as an Oil & Gas or Energy company — consistent with `case_studies.md`'s explicit restriction against that framing. Minor variance only: the live page says "Oracle Data Warehouse" where `case_studies.md` documents simply "Oracle" — a trivial specificity difference, not a fabrication.

### FACTS — discrepancies found

- **FACT / DISCREPANCY 1 — CS-07 (Cryptocurrency Trading Application), URL `/case-studies/development-of-crypto-apps-with-ionic`:**
  - `case_studies.md` documents: Team **3 people**, Duration **5 months**, country/company size **"not published."**
  - The live page states: team of **4** ("a project manager, two Ionic developers, and a testing engineer"), duration of **"three months,"** and identifies the customer as **"an Australian entrepreneur."**
  - This is a three-way mismatch: team size (3 vs. 4), duration (5 months vs. 3 months), and a disclosed country/persona detail ("Australian entrepreneur") that `case_studies.md` explicitly says is not published. App-store ratings (4.9 Google Play, 4.4 App Store) do match between the live page and `case_studies.md`.
- **FACT / DISCREPANCY 2 — likely CS-08 (Sitecore CMS Multisite Platform), URL `/case-studies/redeveloping-website-for-a-leading-material-handling-company-in-australia`:**
  - `case_studies.md` documents: Documented Metrics = **"30% increase in website traffic (company-stated)."** Team 5, Duration 6 months.
  - The live page states: **"50% increase in page views"** and **"20% increase in lead conversions compared to the previous website,"** and "launched in a record time of 6 months."
  - Duration (6 months) matches. But the live page displays two specific percentage metrics — 50% page views, 20% lead conversions — that do not appear anywhere in `case_studies.md`'s approved entry, which documents a different metric entirely (30% traffic increase). Per `policies/claims-and-compliance.md` §8, published metrics must be used exactly as documented, never invented, extrapolated, or substituted — this live page is currently displaying a metric not found in the approved source. Note: this URL-to-CS-ID mapping (redeveloping-website... = CS-08) is inferred from matching subject matter (Australian material-handling manufacturer, Sitecore) rather than an explicit ID on the page — flagged as a mapping assumption requiring confirmation.

### DATA GAPS

- **DATA GAP** — Whether CS-07's or CS-08's live-page figures are the *correct, current* ones and `case_studies.md` needs updating, or whether the live page contains stale/incorrect marketing copy that needs correcting to match the approved record, cannot be determined from this session — the underlying source data (original project records) is not accessible here.
- **DATA GAP** — The URL-to-case-study-ID mapping for CS-03 (Lubricant), CS-08 (Sitecore), and CS-09/CS-10 relies on subject-matter matching rather than an explicit ID shown on the live pages, since none of the live case-study pages display a "CS-0X" identifier. This mapping should be confirmed rather than assumed before any correction is made.
- **DATA GAP** — Whether the systemic fact that all 10 case studies are marked `External Use Approval: HUMAN APPROVAL REQUIRED` in `context/case_studies.md`, while all 10 are already live and published on the public website today, reflects (a) approval already granted at original publication time, predating this documentation, or (b) a genuine unresolved compliance gap, cannot be determined from the files available in this session.

### RECOMMENDATION

Two concrete corrections need a human decision before either the live page or `case_studies.md` is edited: CS-07's team size/duration/country disclosure, and CS-08's substituted percentage metrics. Do not correct either the live page or `case_studies.md` without confirming which one is authoritative — per `Claude.md` §2, current policy files and specialized context files outrank a website's own marketing copy, but the underlying figures still need a human who has access to the original project records to confirm which number is actually correct.

---

## 3. Dedicated Engineering Pods — canonical URL confirmed, `/services/build-your-team/` assessment

**Superseded by business confirmation (2026-08-20).** The business has confirmed:

- **Canonical page:** `/services/dedicated-engineering/`
- **Obsolete page:** `/services/build-your-team/` — no longer in use; must not be treated as an active Staff Augmentation service page.

No new page is to be created. `/services/build-your-team/` is not to be preserved as an active service page. No redirect has been implemented. This section replaces the prior Option A/Option B comparison, which is now moot — that comparison was written when the canonical Pods URL was believed to be unresolved. It also corrects a factual error from the original discovery: the earlier technical audit tested and reported a 404 at a guessed URL, `/services/dedicated-engineering-pods` (with "-pods" in the slug). That exact slug does 404, but it was never the real navigation target — it was an assumed URL this analysis constructed to probe the "Dedicated Engineering Pods" nav item, and the guess was wrong. Direct re-verification today shows the nav item has always pointed to `/services/dedicated-engineering/` (no "-pods"), which resolves normally. The original "broken navigation link — P0" finding in `seo/audits/technical/initial_technical_audit.md` §3 is therefore inaccurate as written and should be corrected in that file separately — flagged here, not fixed here, since this task's scope is this decision pack only.

### Read-only assessment of `/services/build-your-team/`

1. **Current HTTP status** — **FACT:** 200 OK. The page loads successfully; it is not a 404 and has not been redirected.
2. **Current page title/H1** — **FACT:** Title: "Build Your Team | Zediant." Meta description: "Strengthen your team with Zediant's expert staffing solutions. We help you find and integrate the right talent to drive your projects forward and achieve your business goals." H1: "IT Staff Augmentation."
3. **Sitemap appearance** — **FACT:** Yes. `/services/build-your-team` appears in `sitemap.xml` (`priority: 0.9`, `lastmod: 2024-08-21`), per `seo/data/seo_baseline.csv`.
4. **Internal linking on the current website** — **FACT:** Yes, confirmed twice today by direct fetch: (a) it is one of four items in the main "Services" navigation dropdown (labeled "Dedicated Engineering Pods Scale with Pods" in the menu markup, despite pointing to this URL rather than to `/services/dedicated-engineering/`), and (b) it is listed on the `/services` hub page alongside the other nine service links. **DATA GAP:** whether it is linked from anywhere else on the site (body content, footer, blog posts, case studies) is unknown without a full-site crawl.
5. **Original SEO discovery — broken or active?** — **FACT:** The original discovery (`seo/data/content_inventory.csv`, `seo/audits/onpage/initial_onpage_audit.md`) recorded this URL as **live and active** (200), not broken — it was flagged as a P1 overlap/cannibalization risk against the Pods concept, never as a 404. The 404 in the original discovery belongs to the separately-guessed `/services/dedicated-engineering-pods` slug, not to `/services/build-your-team/`. These are two different URLs and must not be conflated.
6. **Evidence of historical SEO value** — **FACT (partial):** it has been in `sitemap.xml` since at least the 2024-08-21 timestamp captured in the original discovery, and the nav/hub-page linking above confirms it currently receives internal link equity. **DATA GAP:** actual historical ranking positions, organic traffic, impressions, click-through, or external backlinks cannot be established — Search Console, Google Analytics, and a backlink tool are all unavailable in this session. Any claim about how much SEO value this URL has accumulated is therefore unverifiable, not merely low.
7. **Content overlap with `/services/dedicated-engineering/`** — **FACT:** substantial overlap confirmed by direct comparison of both pages fetched today. Both describe "self-contained engineering teams aligned to your product roadmap" with the same team composition (Tech Lead, Developers, QA, PM), both state a "30–40%" faster-delivery figure, and both reference AI-enabled/AI-augmented development workflows. `/services/dedicated-engineering/` additionally offers a more developed pod architecture (named roles: Strategist, Engine, Gatekeeper, Orchestrator) and three engagement tiers (Foundation/Growth/Enterprise Pod) that `/services/build-your-team/` does not have; `/services/build-your-team/` additionally documents a distinct 6-step staffing methodology (needs evaluation, candidate screening/filtering, on-demand staffing, documentation/onboarding, post-recruitment support) that does not appear on `/services/dedicated-engineering/`. The overlap is real and business-confirmed as obsolete on the `/services/build-your-team/` side, but the 6-step staffing methodology is content that does not currently exist anywhere else on the site — noted for whoever plans the eventual treatment, not as a reason to keep the page active.
8. **Recommended treatment** — **RECOMMENDATION**, not implemented: of the options listed (301 redirect to `/services/dedicated-engineering/`; 410/remove; leave temporarily; other), a **301 redirect to `/services/dedicated-engineering/`** is the option best supported by the facts above — the page has confirmed sitemap presence and confirmed internal linking (nav + hub page), so simply removing it (410) without a redirect would turn two currently-valid internal links into dead ends and would discard whatever accumulated authority the URL holds, which is unverifiable but not zero given its ~2-year sitemap presence. "Leave temporarily" is the only option consistent with today's explicit instruction not to implement a redirect yet, and is therefore the correct *immediate* state; it should not be read as a competing recommendation to 301, only as the necessary interim state until approval is given. Before a 301 is implemented, the internal nav and `/services` hub page links pointing at `/services/build-your-team/` also need updating to point at `/services/dedicated-engineering/` directly, since relying on the redirect alone leaves a stale link in place. **DATA GAP:** the final choice between 301 and 410 should ideally be informed by Search Console data on this URL's actual current search visibility, which is not available in this session — the recommendation above is the best available call without that data, not a substitute for it.

### DATA GAPS

- **DATA GAP** — Backlink count, current indexation status, historical rankings, and organic traffic/impressions for `/services/build-your-team/` — none available without Search Console/Analytics/a backlink tool.
- **DATA GAP** — Whether any page other than the nav and the `/services` hub links to `/services/build-your-team/` — requires a full-site crawl not performed in this session.
- **DATA GAP** — The CMS platform and its redirect-management mechanism are unidentified, so exact implementation effort for a future 301 cannot be estimated precisely.

### RECOMMENDATION summary

Canonical page: **`/services/dedicated-engineering/`** (business-confirmed, verified live and matching the confirmed positioning). Obsolete page: **`/services/build-your-team/`** (business-confirmed no longer in use; still technically live at 200, still internally linked from nav and the services hub, still in the stale sitemap). Recommended eventual treatment: 301 redirect to `/services/dedicated-engineering/`, paired with updating the nav and hub-page links directly — pending approval; nothing has been implemented.

---

## 4. Digital Presence page decision analysis

**Question posed:** can `/services/digital-presence/` be aligned with documented Zediant capabilities without inventing a new service category?

### FACTS

- **FACT** — The live page's content splits into two distinct groups of claims:
  1. **Alignable without inventing anything:** website development, mobile applications, progressive web applications, e-commerce solutions, and custom software development. These map directly to documented, currently-offered capabilities in `context/services.md`: #7 Mobile Application Development, #8 Web Application Development, #9 E-commerce & CMS Development, and the general custom-development capability described under Dedicated Engineering Pods / Enterprise Custom Development.
  2. **Not alignable without inventing a new capability:** "SEO to social media marketing," "brand identity creation," and "data-driven marketing campaigns." `context/services.md` §"Not offered" explicitly states: "Do not represent these as services: ... brand or marketing strategy, content creation, SEO execution ... data migration as a standalone service." These specific claims on the live page fall squarely within that excluded list.
- **FACT** — No page in the current service catalog (`ai-enabled-product-engineering`, `platform-engineering`, `enterprise-custom-development`, `build-your-team`, or the legacy set) documents marketing/SEO/brand-identity as a Zediant capability anywhere else on the site or in `context/services.md`.

### DATA GAP

- **DATA GAP** — Whether Zediant has, in fact, informally delivered marketing/SEO/brand-identity work for clients that simply was never documented in `services.md` cannot be confirmed or denied from the files available in this session. `policies/claims-and-compliance.md` §4 requires treating an undocumented capability as a `DATA GAP`, not as evidence of absence.

### RECOMMENDATION

The page **can** be aligned with documented capabilities without inventing anything, but only if the marketing/SEO/brand-identity portion is removed or clearly separated first. A defensible aligned version would retain and lead with the web/mobile/PWA/e-commerce/custom-development content (all documented), and either drop the marketing-services language entirely or hold it pending a human confirming it as a real, approved capability to be added to `services.md` through the proper business-context process — this document does not make that addition itself, since capability decisions belong to `context/services.md`'s owner, not to an SEO analysis.

---

## 5. SOC 2 sitewide wording audit

Method: every page fetched in this pass and the prior discovery pass was checked directly for the literal string "SOC 2," and the exact surrounding wording was captured. This covers the homepage and 9 service pages; it does not cover case-study pages, blog posts, or About/Careers subpages not yet fetched — see Data Gaps.

### FACTS — enumerated occurrences

| Page | Occurrence | Wording used |
|---|---|---|
| Homepage (`/`) | Header/credentials badge | "SOC 2 Type II Aligned" |
| Homepage (`/`) | "Why Choose Us" section | "Compliance-Ready: Processes aligned with SOC 2 and UK GDPR/DPA 2018 standards" — **aligned** |
| Homepage (`/`) | Footer badge image | Image asset (`SOC_NonCPA_Blk`) with no surrounding text qualifier — **unqualified** |
| Homepage (`/`) | Security Standards section | "SOC 2 type 2 compliance: We've passed the toughest security audit, proving our system is like Fort Knox for your data" — **compliance / "passed the toughest security audit"** — this exact phrasing is the one `context/services.md` explicitly warns must not be repeated |
| `/services/ai-enabled-product-engineering/` | Badge | "SOC 2 Type II Aligned" — **aligned** |
| `/services/ai-enabled-product-engineering/` | Body | "SOC 2 Type II aligned processes ensuring security and compliance" — **aligned** |
| `/services/ai-enabled-product-engineering/` | Body | "Zediant is a SOC 2 Type II **Certified** partner, ensuring your IP and data are protected" — **certified** |
| `/services/ai-enabled-product-engineering/` | Section heading | "SOC 2 Type II **Certified**" — **certified** |
| `/services/ai-enabled-product-engineering/` | Body | "By aligning with SOC 2 Type II standards, Zediant removes the 'offshore risk'" — **aligned** |
| `/services/platform-engineering/` | Trust line | "SOC 2 Type II **Certified**" | **certified** |
| `/services/platform-engineering/` | Body | "Embedding SOC 2 Type II aligned governance into every layer of your cloud estate" — **aligned** |
| `/services/platform-engineering/` | Subheading | "Security-First DevOps (SOC 2 Type II Aligned)" — **aligned** |
| `/services/platform-engineering/` | Body | "Zediant operates with SOC 2 Type II aligned processes..." — **aligned** |
| `/services/platform-engineering/` | Body | "Our SOC 2 Type II alignment ensures: Secure infrastructure and deployment processes" — **aligned** |
| `/services/enterprise-custom-development/` | Trust line | "Enterprise Standard: SOC 2 Type II **Certified**" — **certified** |
| `/services/enterprise-custom-development/` | Section heading | "SOC 2 Type II **Compliance**" — **compliant/heading**, immediately followed by body text using "alignment" (see next row) |
| `/services/enterprise-custom-development/` | Body (same section as above) | "Our SOC 2 Type II **alignment** ensures that your data protection and operational integrity meet global audit standards" — **aligned**, contradicting the heading immediately above it |
| `/services/enterprise-custom-development/` | Security section heading | "Security is Non-Negotiable: SOC 2 Type II **Certified**" — **certified** |
| `/services/enterprise-custom-development/` | Security section body | "Zediant operates as a SOC 2 Type II **certified** organization..." — **certified** |
| `/services/build-your-team/` | Footer/badge area | Image asset (`SOC_NonCPA_Blk`), no surrounding text qualifier — **unqualified** |
| `/services/cloud-security/` | — | SOC 2 not mentioned anywhere on this page |
| `/services/saas-development/` | — | SOC 2 not mentioned anywhere on this page (the only certification referenced is BigCommerce's own "ISO/IEC 27001:2013 & PCI DSS 3.2, Level 1," which is BigCommerce's certification, not Zediant's) |
| `/services/middleware-integration/` | — | SOC 2 not mentioned anywhere on this page |
| `/services/digital-presence/` | — | SOC 2 not named, but the same "We've passed the toughest security audit, proving our system is like Fort Knox for your data" phrasing appears without the "SOC 2" label attached |
| `/services/ecommerce-business/` | — | Same unattributed "passed the toughest security audit... Fort Knox" phrasing as above, without a SOC 2 label |
| `/about-us/our-story/` | — | SOC 2 not mentioned anywhere on this page |

This matches — and provides live, current confirmation of — `context/services.md`'s own "Critical accuracy warning for all AI agents," which already documented that Zediant's site uses "Aligned," "Certified," and "Compliant" inconsistently, sometimes within a single page. The Enterprise Custom Development page's heading/body contradiction ("SOC 2 Type II Compliance" heading immediately followed by "SOC 2 Type II alignment" body text) is independently reproduced in this live check exactly as `services.md` described it.

### Tally

- **"Aligned" wording (policy-compliant per `Claude.md` §13 / `policies/claims-and-compliance.md` §6):** 9 occurrences (homepage ×2, ai-enabled-product-engineering ×2, platform-engineering ×4, enterprise-custom-development ×1 body).
- **"Certified" wording (non-compliant — must not be used unless an attestation is explicitly confirmed, which no reviewed source confirms):** 6 occurrences (ai-enabled-product-engineering ×2, platform-engineering ×1, enterprise-custom-development ×3).
- **"Compliance/compliant" wording (ambiguous, also flagged by policy as not to be used interchangeably with "aligned"):** 2 occurrences (homepage's "SOC 2 type 2 compliance... passed the toughest security audit," enterprise-custom-development's "SOC 2 Type II Compliance" heading).
- **Unqualified SOC 2 references (badge images with no text):** 2 occurrences (homepage footer, build-your-team footer).
- **Pages with no SOC 2 mention:** 3 of the 9 checked (`cloud-security`, `saas-development`, `middleware-integration`) — plus `digital-presence`, `ecommerce-business`, and `our-story` mention no SOC 2 at all, though two of those repeat the unattributed "passed the toughest security audit" line.

### DATA GAPS

- **DATA GAP** — Case-study pages (10), blog posts (7), and other About subpages (Team Culture, How We Work, Trust & Compliance, Careers) referenced in navigation but not individually fetched for this specific wording check remain unverified. A full-site crawl (already recommended generally in `seo/audits/technical/initial_technical_audit.md` §6) would be needed to guarantee completeness.
- **DATA GAP** — Whether Zediant holds any completed SOC 2 Type II attestation report today is not established by any source reviewed — `context/company.md`, `context/services.md`, and `policies/claims-and-compliance.md` all instruct defaulting to "aligned" absent explicit confirmation, and no such confirmation exists in any file reviewed.

### RECOMMENDATION

Every "Certified" and "Compliance/compliant" occurrence identified above should be corrected to "aligned" wording, consistent with `Claude.md` §13, `policies/claims-and-compliance.md` §6, and `context/services.md`'s own warning — this is a public-claims correction requiring approval, not a discretionary style choice. The unattributed "passed the toughest security audit... Fort Knox" phrasing should also be reviewed regardless of whether "SOC 2" is explicitly named next to it, since it makes a comparably strong, unqualified security claim.

---

## A. Decisions required from Rajeev

1. **work.zediant.com** — business decision to RETIRE is confirmed. Remaining decision: approve the specific retirement mechanism (301 redirect vs. 410/removal) and, if redirect, the destination URL(s); then authorize execution.
2. **Dedicated Engineering Pods** — choose Option A (`/services/build-your-team/` becomes canonical) or Option B (new `/services/dedicated-engineering-pods/` page), and separately decide the fate of whichever page is not chosen.
3. **Digital Presence page** — decide whether to remove the marketing/SEO/brand-identity claims, or confirm (through the proper business-context process) that marketing services are in fact a real, approved Zediant capability that should be added to `context/services.md`.
4. **CS-07 and CS-08 discrepancies** — confirm which figures are correct (the live page's or `case_studies.md`'s) for team size/duration/country (CS-07) and the traffic/conversion metrics (CS-08).
5. **SOC 2 wording** — confirm approval to normalize all "Certified"/"Compliance" instances sitewide to "aligned," per already-standing policy.
6. **Case-study external-use approval status** — confirm whether the "HUMAN APPROVAL REQUIRED" status on all 10 case studies in `context/case_studies.md` reflects approval already granted at original publication, or an outstanding gap.

## B. Facts already established

- work.zediant.com: business-confirmed as not used by Zediant and approved for retirement. It is authentically owned by Zediant (matching phone/email), last stamped 2023, with a different office address than currently documented, undocumented Sydney office reference, unsupported team/satisfaction/project figures, its own Careers content, and no robots.txt. No page on `www.zediant.com` or its sitemap links to it. HTTPS is active. Hosting, DNS, backlink, and traffic/indexation data remain DATA GAPs. Directional recommendation: 301 redirect (Option B is safer than bare removal). Actual retirement execution is HUMAN APPROVAL REQUIRED and not yet performed.
- 8 of 10 live case studies match `context/case_studies.md` exactly; 2 (CS-07, CS-08) contain specific, quantifiable discrepancies.
- `/services/dedicated-engineering-pods` has zero prior URL history (never in any sitemap, currently 404); `/services/build-your-team/` has existing content and ~2 years of sitemap presence.
- The Digital Presence page's web/mobile/PWA/e-commerce/custom-development content is legitimately alignable with documented services; its marketing/SEO/brand-identity content is not.
- SOC 2 wording is inconsistent sitewide exactly as `context/services.md` already warned: 9 "aligned" occurrences (compliant), 6 "certified" occurrences (non-compliant), 2 "compliance" occurrences (ambiguous), across the pages checked in this pass.

## C. Items Claude can implement after approval

- Correcting "Certified"/"Compliance" SOC 2 wording to "aligned" across the enumerated pages, once approved.
- Rewriting/repointing either `/services/build-your-team/` or publishing `/services/dedicated-engineering-pods/`, once the canonical-URL decision is made and a content brief is approved.
- Removing or rescoping the marketing/SEO/brand-identity claims on `/services/digital-presence/`, once the capability decision is made.
- Regenerating `sitemap.xml` (already scoped in `seo/strategy/p0-implementation-plan.md` Item 2), independent of the above.
- Retiring `work.zediant.com` (301 redirect or 410/removal, per the confirmed business decision), once the specific mechanism and destination are approved.

## D. Items requiring access/credentials

- Google Search Console / Analytics, to confirm indexation and traffic impact for work.zediant.com, the Pods URL options, and post-correction monitoring.
- CMS/website admin access, to identify exactly where each piece of copy and metadata lives before editing.
- A backlink tool, to properly assess internal/external link equity for the Pods URL decision.
- Access to the original CS-07 and CS-08 project records, to determine which figures (live page vs. `case_studies.md`) are correct.
- Domain/hosting/DNS access for `work.zediant.com`, to confirm current hosting platform, DNS configuration, and administering party before executing retirement.

## E. Items requiring website developer involvement

- Any edit to page copy, metadata, or the SOC 2 badge component (platform unidentified — may or may not require a developer depending on CMS capability).
- Any redirect or nav-link change resulting from the Pods URL decision.
- Sitemap regeneration.
- Executing the work.zediant.com retirement (DNS change, hosting change, redirect rule, or content removal), once the mechanism is approved — requires whoever administers that domain's DNS/hosting.

---

**No implementation has occurred.** This pack is evidence and decision-routing only, built from currently accessible project files and live, public, unauthenticated page fetches.
