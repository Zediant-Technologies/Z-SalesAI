# 03 — Content Gap Analysis

Status: Read-only. No pages created or modified. Per Section 21 of the brief, every gap below is classified A–D and only classified D (new page) when existing-page expansion is clearly insufficient.

## A — Existing page can cover it (no new content needed, just linking/emphasis)

| Topic / keyword | Existing page | Why A, not B/C/D |
|---|---|---|
| "hire dedicated development team" (transactional long-tail) | `/services/dedicated-engineering/` | Already the right page and largely the right content; this is a CTA/microcopy fit, not a content gap |
| "system integration services" | `/services/middleware-integration/` | Page exists and is topically correct; the gap is ZCoupler branding (see B) |
| Case study proof for each service | `/services/*` pages + `/case-studies/*` pages | Both sides already exist; the gap is purely the missing links between them (see `04-internal-linking-audit.md`) — not new content |

## B — Existing page needs expansion

| Topic / keyword | Existing page | What's missing | Priority |
|---|---|---|---|
| ZCoupler branded framing | `/services/middleware-integration/` | The commercial service page never names ZCoupler, despite 4+ blog posts already building a ZCoupler content cluster and CS-01 being the strongest case study on the site. This is the single clearest content gap found in this audit. | High |
| Legacy Modernisation depth | `/services/enterprise-custom-development/` | Already has an H3 with real content; could be expanded with named-stack specificity (.NET Framework migration, Java EE migration — both explicitly listed in `services.md`'s approved keyword list but not used on the live page) | Medium |
| Product-lifecycle / roadmap-vs-headcount framing | `/services/ai-enabled-product-engineering/` | `campaigns.md` C1's "roadmap versus headcount" messaging angle is well-written and does not appear on the live page at all — this is the fix for the positioning problem in `02-service-positioning-audit.md`, not a new page | High |
| Engagement-model / tiering clarity | `/services/platform-engineering/`, `/services/enterprise-custom-development/`, `/services/ai-enabled-product-engineering/` | Only Dedicated Engineering has named engagement tiers; the other three pages leave "what does working together actually look like" unanswered | Medium |
| Case-study cross-linking | All 4 service pages | Zero case studies linked from any service page — add 1–2 relevant, already-approved case studies per page | High |

## C — Blog/Insight opportunity (informational, not a new commercial page)

| Topic | Rationale | Priority |
|---|---|---|
| Staff augmentation vs. dedicated engineering pod (comparison) | Genuine commercial-investigation search intent per `context/seo/search_intent.md`'s own framework; differentiates campaign C2's two entry angles; no current page addresses it directly | Medium |
| "What is engineering as a service" — already exists (`/blogs/eaas-engineering-as-a-service/`) but is orphaned from the blog hub (see `06-blog-audit.md`) — fixing discoverability may be sufficient without new writing | Low (linking fix, not new content) |
| Named-stack legacy modernization deep-dives (.NET Framework, Java EE) | Supports the Enterprise Custom Development expansion above without overloading the commercial page itself | Low-Medium |

## D — Potential future commercial page (only where strongly justified)

No new commercial page is recommended at this time. Two candidates were evaluated and both fail the brief's own justification bar:

### Candidate 1: Standalone ZCoupler product page (`/zcoupler/` or similar)
- **Search intent:** Navigational/branded + commercial — genuine, low-competition (per `Zediant_SEO_Keyword_Map.xlsx` Competitors sheet, no competing branded content was found).
- **Business relevance:** High — ZCoupler is Zediant's most evidenced capability.
- **Why NOT recommended yet (classified B instead):** the content gap is that `/services/middleware-integration/` doesn't mention ZCoupler at all — expanding that existing page is the lower-risk, `seo_rules.md` §3-compliant fix ("existing page before new page"). A standalone product page could be justified later, but only after the expanded service page's performance is assessed — creating both at once risks self-competition between `/services/middleware-integration/` and a new `/zcoupler/` page for the same "ZCoupler" branded searches.
- **Potential cannibalization:** High, against the expanded service page, if built prematurely.
- **Recommended priority if revisited:** P2, after Item B above ships and is measured.

### Candidate 2: "Product Engineering Company" pillar/hub page
- **Search intent:** High commercial relevance, flagged directly in the prior keyword-map's Content Gaps sheet.
- **Why NOT recommended as a new page here:** the homepage already functions as the broad commercial hub per its own approved primary keyword ("product engineering services") — a second, separate pillar page competing for nearly the same phrase would itself create a new cannibalization pair on day one, which `seo_rules.md` §9 explicitly warns against.
- **Recommended treatment instead:** strengthen the homepage's own alignment to this intent (already scoped as OPTIMIZE in `01-page-audit.md`) rather than fork a new URL.

## No content gap was found that meets all of Section 21's four justification criteria (search intent + business relevance + differentiation + non-duplication) for a genuinely new page. This finding itself is worth reporting: Zediant's current architecture (Home / 4 Services / 4 About / Case Studies / Blogs) is close to sufficient for its current commercial priorities — the real gaps are internal linking, content expansion on existing pages, and the orphaned-blog discoverability bug, not missing pages.**
