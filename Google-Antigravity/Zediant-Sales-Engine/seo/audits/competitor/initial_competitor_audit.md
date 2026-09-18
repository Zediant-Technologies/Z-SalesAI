# Initial Competitor (SEO) Audit — Zediant Technologies

Status: Draft / Read-only discovery
Date: 2026-08-19

---

## 1. Method and limitations

This pass used general web search on two representative query patterns aligned to Zediant's primary services and target geographies (Australia, UAE), per `context/seo/seo_strategy.md`'s geographic priorities. This is **not** a substitute for proper SERP-tracking or rank-tracking tooling, and results are directional only. No search-volume, ranking-position, or traffic data was available. `context/competitors.md` documents zero named competitors internally (by design — see that file's "central fact about this landscape") and organizes competition by category instead; this audit cross-references observed search results against those categories rather than inventing new named competitors as established fact.

## 2. Queries run and observations

| Query | Notable results (Market listing / observed only — not verified) | Notes |
|---|---|---|
| "dedicated engineering pods company Australia SaaS" | Appsierra, Mobisoft Infotech, Offshore247, 9series, Brain Station 23, Taazaa | Several of these firms explicitly market "engineering pod" or "product acceleration pod" language similar to Zediant's own positioning — this is Category 3 (Offshore Boutique Software Companies) and Category 2 (Mid-Tier Global Engineering Firms) territory per `competitors.md`, which that document already flags as the most frequent and second-most-frequent categories Zediant meets. |
| "AI-enabled product engineering services company UAE" | Goodfirms/DesignRush/Masterofcode directory listings, Appinventiv, TechGropse, Shurutech, Apptunix | Results skewed toward Dubai-based "AI development company" positioning (Category 9, AI-Native Engineering Firms, per competitors.md) rather than Zediant's "AI-assisted delivery method applied to product engineering" framing — suggesting a possible positioning/query mismatch worth validating in full keyword research. |

Neither query surfaced Zediant's own site among visible results in this pass — consistent with (but not proof of) the indexation concerns already flagged as UNKNOWN/REQUIRES HUMAN VERIFICATION in the technical audit.

## 3. Mapping to documented competitor categories

| Category (from competitors.md) | Observed in this pass? | Notes |
|---|---|---|
| 1 — Large Global IT Services Firms | No | Not surfaced in these two queries; expected only on larger enterprise-scale searches |
| 2 — Mid-Tier Global Engineering Firms | Likely (e.g. Brain Station 23-type firms) | Market listing only |
| 3 — Offshore Boutique Software Companies | Likely — most results fall here | Consistent with competitors.md's own assessment that this is the "real battleground" |
| 4 — Freelance & Marketplace Developers | No | Not surfaced in these two queries |
| 5 — Local In-Country Hiring | No | Not applicable to organic search queries of this type |
| 6 — Local Digital Agencies & Consultancies | No | — |
| 7 — Staff Augmentation & IT Staffing Firms | Possibly (Appsierra-type results) | Relevant to campaign C2 |
| 8 — Specialist Integration & Platform Vendors | No | Not surfaced; worth a dedicated query pass once ZCoupler content exists |
| 9 — AI-Native Engineering Firms | Likely (Dubai "AI development company" results) | competitors.md already flags Zediant's position here as "Low on genuine AI product work" — reinforces the AI-capability-claims caution already documented in `policies/claims-and-compliance.md` §5 |

## 4. Content and service gaps (preliminary)

- No content gap can be confirmed at the keyword level without dedicated keyword research (next phase, owned by `keyword_research.skill`).
- Directionally, competitor results for "AI-enabled product engineering" skew toward generic "AI development company" positioning, while Zediant's actual differentiation (per `services.md` and `context/seo/seo_strategy.md`) is AI-assisted delivery **method** applied to full product engineering, with an explicit internal caution against overclaiming deep AI product experience. This suggests Zediant's SEO content should differentiate on delivery methodology and evidenced outcomes rather than competing head-on for generic "AI development" queries where Category 9 competitors are stronger and where claims-policy risk is highest.
- No competitor content specifically targeting "dedicated engineering pods" branded terminology was observed, which is LIKELY a distinctive positioning opportunity for Zediant once the corresponding page (currently 404) is restored.

## 5. What was not done

Per policy, this audit does not state or imply any competitor's market share, customer count, pricing, satisfaction, retention, or win rate, and does not repeat any competitor's self-published marketing statistics as fact. No competitor content was scraped or reproduced beyond publicly visible search-result titles and URLs.

## 6. Recommendation

Commission a full keyword-research pass (via `keyword_research.skill`) using an actual keyword/rank-tracking tool before finalizing competitive priorities. This audit's SERP observations should be treated as a starting hypothesis, not a validated competitive map. Priority: **P1**. No approval required for the research itself; approval is required before any resulting content is published.
