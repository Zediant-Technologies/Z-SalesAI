---
name: apollo-search-builder
description: "Zediant's Apollo.io prospecting skill — sourcing, filter design, scoring, technology fit, dedup, enrichment, and handoff. Use this whenever the user wants to find prospects, build a target list, source leads, enrich contacts, get emails, find decision makers or CTOs/CEOs/COOs at companies, research a market, run a daily high-volume sourcing pass, or work on campaigns C1-C5. Also use when asked which Apollo filters to apply, when a search returns too few, too many, or off-ICP leads, when the written batch is far smaller than both the target and the available Apollo pool, or when diagnosing why lead quality is poor. Trigger even if the user doesn't say \"Apollo\" — any Zediant B2B contact discovery or enrichment request belongs here. Stops at scored, enriched, handoff-ready contacts; hand off to the crm-update skill for CRM writes, BDM approval, and campaign distribution."
---

# Apollo Search Builder

Zediant's end-to-end Apollo prospecting skill: turn a campaign brief into a precise search, build a wide enough candidate pool, score what comes back, enrich only what deserves it, and hand off a clean batch.

Apollo will happily return 50,000 leads that look like the ICP and are not. Volume is free; credits, sender reputation, and BDM attention are not. Optimise for **qualified prospects per credit**, never prospects per search.

## The core operating principle

Think like a senior B2B salesperson deciding who's worth a call today, not like a database scraper filling a quota.

**Ramp-up production target is 7–10 high-intent qualified leads per daily run** (aligned with Zediant's single-mailbox deliverability limit: 25–35 emails/day total, 300–480s randomized spacing, 0 tracking pixels, strict email verification). Sourcing targets 25–50 raw verified candidates to find the best 7–10 prospects. The long-term production ceiling remains up to 80 qualified prospects per run once multiple warmed sending mailboxes/domains are activated. Never loosen a filter, lower a score threshold, or pad a category to reach a round number — a shortfall reported honestly is a successful run; a padded batch that gets rejected at BDM review is not. Reporting "only 6 genuinely qualified today" is the correct outcome when that's what's true, not a failure to explain away.

**A shortfall is only acceptable when it's genuine.** A written batch of 2-3 against a target of 7-10, or 8-10 against an 80 target, with an available Apollo pool in the thousands, is very rarely a genuine shortfall — it is almost always a pipeline mechanics problem (too few raw candidates actually pulled, over-aggressive deduplication, or real prospects scored down to Cold by data gaps rather than actual poor fit). See the Volume Diagnostic below before concluding a market segment is simply thin.

## Where this skill starts and stops

**Owns:** campaign interpretation, filter design, candidate pool sizing, search execution, technology fit assessment, exclusion screening, deduplication, ICP scoring, signal enrichment, enrichment, quality diagnosis, handoff packaging.

**Hands off:** CRM writes, BDM approval gate, campaign distribution → `crm-update` skill. PTB scoring → `ptb-scoring` skill — `ptb-scoring` is the sole authority that calculates or assigns any PTB points, tier, or score. This skill collects and preserves raw buying-signal evidence (including the trigger/signal assessment below) as evidence only; it does not calculate PTB, assign PTB points, or produce a PTB score or tier. PTB is a single 0–100 score (Initial Buying Signal) calculated pre-outreach for qualified leads; there is no separate post-engagement PTB model and no Path A / Path B distinction. Outreach copy → `email-personalization` skill, via `crm-update`.

This skill replaced the retired `zediant-apollo-prospecting`. If another skill or document references that name, it means this one.

## Context files — reference, never restate

**For day-to-day sourcing, read the condensed playbooks instead of the full source docs — they're pre-extracted from the same source and cost far less to open:**
- `context/playbooks/C{1-5}.md` — that campaign's title set, keyword tags, employee band, target ICP, business problems, buying/disqualification signals, messaging angle, case study
- `context/playbooks/_core-reference.md` — the shared ICP Score model, hard disqualifiers, excluded industries, geography/capacity ceiling, escalation triggers, unsubstantiated-claims list, competitor-screening note

Open the full source docs directly only for a genuinely novel edge case the playbooks don't cover (a DATA CONFLICT, an excluded industry not listed, a scoring dispute): `icp.md` segments, verticals, scoring model, exclusions, geography priority · `campaigns.md` campaign definitions, personas · `services.md` capability boundaries → technology exclusions · `company.md` capacity ceiling · `pricing-public.md` commercial viability floor · `case_studies.md` vertical proof depth · `competitors.md` competitor positioning

Duplicating ICP content into this skill is how it goes stale. Read the file (or its playbook).

**On employee bands specifically:** `icp.md` sets segment-specific bands — agencies 10–100, SaaS 10–200, CTO-led product companies 20–200. For the daily SaaS/product-focused sourcing motion (see Candidate Pool Strategy below), **20–200 is the default starting filter**, but it does not override `icp.md`'s wider bands for agencies (C2 default profile) or override the ability to keep a strong sub-20 or funded early-stage company that clears qualification on other grounds — a real case from this pipeline: an 11-person Dubai SaaS startup with a credible product and a named CTO cleared qualification despite sitting under the default floor. Treat 20–200 as a search-efficiency default, not a hard qualification rule; the hard rule is still `icp.md`'s own exception language (rare, and only for unusually strong strategic reasons).

---

# DECISION GUIDE

Fastest route from what the user said to what to do.

| User says | Do this |
|---|---|
| "Find leads / prospects for C1-C5" | Full workflow, Steps 1–8 |
| "Run today's daily sourcing pass" / "populate today's leads" | This skill's Steps 1–8 feed directly into `scheduler-lead-population`'s orchestration — see that skill for the full daily pipeline including CRM write |
| "Which filters should I use for [market]?" | Steps 1–4, return the filter block, stop before execution |
| "Why is this search returning bad leads?" | Step 8 diagnostic table |
| "I asked for 100 and got 8-10, but Apollo shows thousands available" | **Volume Diagnostic** below — run it before concluding the segment is thin |
| "Are we already talking to [company]?" | `search_people(q_organization_name="...")` — free, answer directly |
| "Enrich these people" | Step 7 scoring first, then Step 6 enrichment. Hot/Warm only |
| "Is [company] hiring engineers?" | See the hiring-signal problem below — Apollo filters are gated |
| "How many credits do we have?" | Check Apollo account profile / credit usage |
| "Find me some leads" (no campaign named) | **Ask which campaign first.** An unscoped search wastes search and enrichment budget |
| "Source a referral / partner-introduced lead" | Stop. Referral/partner-sourced leads are never sourced through Apollo — hand straight to `lead-qualification` with Source = Referral |
| "Is this company a prospect or a partner?" | See Partner / Engineering Overflow classification below |
| "Add these to a campaign" | Not this skill → `crm-update` skill |
| "Social Lead ID / Apollo ID is missing on written leads" | See Apollo Person ID Capture below |

---

# OPERATING RULES

## Deliverability First — Verified Emails Only

**Every Apollo search must enforce `contact_email_status: ["verified"]`.** Never include guessed, unavailable, or bounced emails. To protect Zediant's domain and mailbox reputation (< 1% bounce target), only prospect records with verified email addresses may enter the qualification and enrichment pipeline.

## Cost-order — never invert

Work cheapest-first. This ordering exists because the expensive steps are irreversible.

| Order | Action | Tool | Cost |
|---|---|---|---|
| 1 | Check existing contacts / people | `search_people` | **Free** |
| 2 | Net-new people search | `search_people(contact_email_status=["verified"])` | Search only, **returns no emails** |
| 3 | Enrich a scored shortlist | `bulk_enrich_people` / `enrich_person` | **1 credit/match, 0 if not found** |
| 4 | Company firmographics | `enrich_organization` / `search_organizations` | 1 credit/matched company |

## Never set these parameters

`reveal_phone_number: true` · `reveal_personal_emails: true`

Zediant sources work email and LinkedIn only. Each of these adds credit cost against data Zediant's process doesn't use.

## Confirm before enrichment, every time

State exact scope and cost, then wait for an explicit yes:

> "This will enrich [N] people and use up to [N] credits (1 per match, no charge if not found). Proceed?"

Enrichment is the only irreversible spend in this workflow — a wrong batch cannot be refunded, and careless runs waste monthly credits.

## Batch discipline

`bulk_enrich_people` takes **max 10 per call**. Never loop individual enrichment per person when bulk is possible — identical cost, far fewer round trips.

Use `per_page=25` for a normal scoped search. For a daily candidate-pool build (see below), pagination across multiple pages is expected and mandatory — see Candidate Pool Strategy.

For 20–30+ people, flag that a persisted Apollo record collection beats tracking batches in conversation — conversational tracking has no resumability, no persistence, and no export path, so an interrupted run loses everything.

Never paste raw Apollo JSON. Summarise: count, tier breakdown, and only name, title, company, email, LinkedIn, signal, score.

## Apollo Person ID capture — mandatory, checked at handoff

**A blank Social Lead ID on an Apollo-sourced lead is a bug, not a normal outcome.** The Apollo Person ID is the value that ends up in `leadchain0__Social_Lead_ID` in Zoho, and it must be captured immediately, not reconstructed later.

- The identifier lives on the **search result object** returned by `search_people` (each candidate has an `id` field — capture it into the working record the moment the search returns, not after enrichment).
- It is confirmed again on the **enrichment response** from `bulk_enrich_people` (the matched person object also carries `id` — depending on the specific response shape this can appear at the top level or nested as `person.id`; check the actual response the first time you call it in a session and use whichever key is populated).
- Carry this value through every downstream stage — scoring, technology fit, signal enrichment, handoff — as its own field (`apollo_person_id`), never derived or guessed from name+company after the fact.
- **Before handoff, check every contact has a non-null `apollo_person_id`.** If one is missing despite the person coming from a successful search/enrichment call, don't silently hand it off blank — flag it explicitly ("Apollo Person ID missing for [name] at [company] despite a successful match — investigate before write") so `crm-update` and the BDM know this needs a second look rather than assuming the person simply has no ID.
- If a lead reaches this skill from a source other than a live Apollo search/enrichment call this session (e.g., a re-scored existing Zoho record), and no `apollo_person_id` was ever captured historically, that's a legitimate blank — say so, don't invent one.

---

# CANDIDATE POOL STRATEGY — for daily / high-volume sourcing runs

For a scoped, small request ("find me 15 CTOs at funded Sydney SaaS companies"), Steps 1–7 below are sufficient as written. For the daily production pass feeding `scheduler-lead-population`:
- During the current ramp-up phase (7–10 qualified leads/day written target), retrieve **25–50 raw verified candidates** across the day's rotated searches.
- When scaling up toward the full 80-lead ceiling (multi-mailbox production), build wider (**300–500 raw candidates**).

Build wider, then funnel — this produces a high-conversion final batch at minimal credit cost, because every filtering stage before enrichment is free.

| Stage | Action | Cost |
|---|---|---|
| 1 | Retrieve candidate pool (25–50 for ramp-up, 300–500 for full ceiling) with `contact_email_status: ["verified"]` | Free |
| 2 | Remove Zoho duplicates — full cascade, see Deduplication below | Free |
| 3 | Apply basic ICP filters (geography, employee band, segment) | Free |
| 4 | Apply Technology Fit assessment (see below) | Free — uses data already in the search response |
| 5 | Run the Signal Enrichment Pass (see below) — fill real Buying Signal and Technology Fit data before scoring, rather than defaulting to Unknown | Mostly free |
| 6 | Score every survivor per Step 7 | Free |
| 7 | Deep-research the strongest survivors only where the Signal Enrichment Pass didn't already resolve the question (Step 6 below) | Free (web search) |
| 8 | Enrich the final selected list (7–10 top survivors during ramp-up; up to 80 at ceiling) | Paid — this is the only stage that costs credits |

The point of building a funnel pool is that stages 2–6 eliminate non-fits for free, and what survives to Stage 8 is a much stronger pool than trying to hand-pick from a single unvetted search.

## Mandatory pagination & verified filtering

**Stage 1 requires proper filtering and pagination.** `search_people` at `per_page=25` returns 25 candidates per call. Always set `contact_email_status: ["verified"]` to ensure deliverability. If a search returns fewer candidates than needed, iterate `page` (page 1, 2, etc.) until the target candidate pool is gathered or the segment is genuinely exhausted.

For a daily run:
- Set `per_page=25` or practical maximum (up to 100), setting `contact_email_status: ["verified"]`.
- Iterate the `page` parameter across rotated searches until the target pool (25–50 for ramp-up, up to 300–500 for full scale) is reached or the segment is exhausted.
- Track pages already pulled per geography/segment/technology combination (see Search Rotation) so a resumed rotation continues from where it left off rather than re-pulling page 1 every day.

## Search Rotation

Never run the same search two days running — pools exhaust, and a repeat search mostly returns contacts already screened out or already in Zoho. Rotate the dimensions: geography, technology, title/seniority, and signal focus.

Example weekly rotation (adapt to actual pool depletion, don't follow blindly once a pool runs dry):

| Day | Focus |
|---|---|
| A | Australia + SaaS + .NET/Azure + CTO/Engineering leadership |
| B | Australia + product companies + React/Java + Engineering leadership |
| C | UAE + SaaS + Cloud/API + CTO/Engineering |
| D | UAE + product companies + .NET/Java + Product leadership |
| E | Australia + explicit engineering-hiring signal (manual verification, see the hiring-signal problem below) |

Track where each geography/segment/technology combination left off (last page requested, approximate pool size) so rotation resumes rather than restarts. If a pool is verified exhausted (see Known regional pool sizes), rotate to the next geography rather than re-running it or loosening filters to extract more from a dry pool.

## Campaign Coverage Rotation — don't default to C1/C2 only

The Search Rotation table above rotates geography and technology; it does not by itself guarantee all five campaigns get sourced. Left to default judgment, a run tends to gravitate toward C1 (funded SaaS) and C2 (agencies) because their sourcing profiles are the most familiar and fastest to build — this is a real observed pattern from this pipeline (a live run sourced C1/C2 only and left C3–C5 unsourced without being asked to), not a hypothetical, and it means C3, C4, and C5 can go unsourced for extended periods purely from habit, not because they're a worse fit for Zediant.

**Unless the user names a single specific campaign, a daily run should source across multiple campaigns in the same pass**, using the title sets (Step 3) and keyword tags (Step 4) already defined for C1–C5 below. This split should mirror `campaigns.md`'s official Campaign Portfolio Allocation (25/25/15/25/10):

| Campaign | Target share of written batch | Sourcing note |
|---|---|---|
| C1 — Funded SaaS | 25% | Requires external funding verification (Step 6) — don't skip it to save time |
| C2 — Agencies / hiring-signal SaaS | 25% | Two distinct title sets exist for this one campaign — pick one profile or split further |
| C3 — Platform/cloud modernization | 15% | Technology Fit tier (Step 6) carries more scoring weight here than funding signal |
| C4 — Middleware/API integration | 25% | Same technology-fit-led scoring approach as C3 |
| C5 — Product/enterprise modernization | 10% | Persona skews slightly senior (CIO/IT Director/Enterprise Architect) — don't reuse C1's CTO-only title set |

These are planning targets for the raw pool split, not a hard per-lead gate — `campaigns.md`'s own rule still applies: never move an individual lead into a weaker-fit campaign merely to satisfy a percentage, and never withhold a lead from its strongest-fit campaign because that campaign is already at or above target. For a smaller, ceiling-constrained run (e.g. 7–10 leads/day during ramp-up), narrow the *raw pool size pulled per campaign* proportionally, keeping the same 25/25/15/25/10 ratio, so the written batch still reflects a genuine cross-section of C1–C5.

If the user does ask for a specific campaign only, that instruction overrides this section entirely.

## Signal Enrichment Pass — recover real scores instead of defaulting to Unknown

Evidence-dependent qualification should never guess. A genuinely good-fit company can appear under-evidenced when Buying Signal or Technology Fit has not yet been checked, so the fix is to close that evidence gap before final qualification rather than lowering a threshold. **This pass strengthens the evidence behind ICP/fit scoring and the raw signal evidence handed downstream — it does not compute or finalize a PTB score.** This skill does not calculate PTB. It passes raw pre-engagement signal evidence downstream to `ptb-scoring` to calculate the numeric 0–100 PTB Score (Initial Buying Signal).

After Stage 4 (free ICP + technology filters), and before finalizing ICP/fit scoring, run a lightweight verification pass across the surviving pool:

- **Headcount growth** — available from `bulk_enrich_people`'s response fields (`organization_headcount_six_month_growth` etc.) once enrichment happens; for pre-enrichment triage, a quick company-site or LinkedIn company-page check substitutes.
- **Buying signal** — a short, templated web search per surviving company ("[company] funding", "[company] careers engineering", "[company] technology migration") rather than an open-ended research pass.
- **Technology fit** — cross-check technology results against `services.md`, don't leave it unchecked.

This pass is bounded, not exhaustive — prioritize companies that cleared ICP/geography/employee-band filters. The goal is closing Unknowns on real candidates.

**This does not change any scoring threshold.** A company that's genuinely weak after real signal data was gathered stays weak. The fix is data completeness before scoring is final, not leniency in the score itself. Apollo Search collects evidence only; `ptb-scoring` remains the sole authority for calculating the PTB score (Initial Buying Signal).

---

# WORKFLOW

## Step 1 — Establish the campaign

Everything downstream depends on this. Get it before filtering.

| Question | If unanswered |
|---|---|
| Which campaign? | **Ask.** Never guess — the wrong campaign produces a plausible, useless list |
| Which geography? | Default Australia or UAE per `icp.md` |
| How many prospects? | Default 7–10 during ramp-up (up to 80 at full scale) |
| Net-new or top-up? | Check Zoho deduplication and existing contacts |

| Campaign | Segment | Dominant signal | Persona |
|---|---|---|---|
| C1 | Funded SaaS | Funding announced within 6 months → product roadmap scaling | CTO, Founder, VP Engineering |
| C2 | Digital agencies (default routing) | Capacity pressure | Founder, COO, MD, Head of Delivery |
| C2 | SaaS / product with open senior eng roles | Active hiring, 60+ days open | CTO, VP Eng, Eng Manager |
| C3 | SaaS / product companies | Platform, cloud, or DevOps modernization need | CTO, Head of Platform Engineering, VP Infrastructure |
| C4 | SaaS / product companies | Integration, middleware, or data-flow work | CTO, Head of Integration, VP Engineering |
| C5 | Product companies (bootstrapped or acquired) | Feature outsourcing or legacy modernization | CTO, CIO, IT Director, Enterprise Architect |
| — | Referral / partner | **Not sourced through Apollo** | — |

C2 carries two distinct sourcing profiles — agencies by default, or SaaS/product companies with a hiring signal. Both route to C2 downstream in `campaign-selection`, but they need different title sets at search time (Step 3).

### A note on "trigger category" language

If a brief describes a prospect type as "Product Engineering," "Engineering Expansion," "Integration/API," "Modernisation," or "Growth/Product Signals," these are **not** a fourth campaign taxonomy — they map onto the C1–C5 registry above and describe *why* a prospect is being sourced, not which CRM value gets written. Use this language freely as a search-planning and rotation label; never write it to `Lead_Campaign_Category` in Zoho. That field takes C1–C5 only, per `crm-update`'s live schema constraint. A rough mapping for planning purposes:

| Trigger-category label | Maps to |
|---|---|
| Product Engineering | C1 (funded SaaS) or C4/C5 (product companies with a specific build need) |
| Engineering Expansion | C2 (SaaS/product hiring-signal profile) |
| Integration/API/Platform | C3 or C4 |
| Legacy/Enterprise Modernisation | C5 |
| Growth/Product/Technology Signals | Whichever of C1–C5 the segment otherwise indicates — this label describes signal strength, not segment |

## Step 2 — Map ICP to filter dimensions

| Dimension | Apollo filter |
|---|---|
| Industry / segment | `q_organization_keyword_tags` |
| Geography | `person_locations` **and** `organization_locations` |
| Company size | `organization_num_employees_ranges` |
| Persona | `person_titles` + `person_seniorities` |
| Technology | `currently_using_any_of_technology_uids` |

**Segment governs, not vertical.** A funded SaaS company selling into healthcare is searched as SaaS, not healthcare. Verticals select the case study you reference in outreach, not the filter set you search with.

## Step 3 — Title sets

**C1 — funded SaaS**
```
person_titles: ["Founder","Co-Founder","CEO","CTO","Chief Technology Officer",
                "VP Engineering","Head of Engineering"]
person_seniorities: ["founder","c_suite","vp"]
```

**C2 — agencies (default sourcing profile)**
```
person_titles: ["Founder","Co-Founder","CEO","Managing Director","COO",
                "Chief Operating Officer","Head of Delivery"]
person_seniorities: ["founder","c_suite"]
```

**C2 — SaaS / product, hiring signal**
```
person_titles: ["CTO","Chief Technology Officer","VP Engineering",
                "Head of Engineering","Engineering Manager","Director of Engineering"]
person_seniorities: ["c_suite","vp","director","manager"]
```

**C3 — platform / cloud modernization**
```
person_titles: ["CTO","Chief Technology Officer","VP Engineering",
                "Head of Platform Engineering","Head of Infrastructure",
                "VP Infrastructure","Director of DevOps","Head of DevOps"]
person_seniorities: ["c_suite","vp","director"]
```

**C4 — middleware / API integration**
```
person_titles: ["CTO","Chief Technology Officer","VP Engineering",
                "Head of Integration","Integration Architect",
                "Head of Engineering","Director of Engineering"]
person_seniorities: ["c_suite","vp","director"]
```

**C5 — product companies / enterprise modernization**
```
person_titles: ["CTO","Chief Technology Officer","Head of Engineering","CIO",
                "IT Director","Head of Technology","Enterprise Architect",
                "Founder","Managing Director"]
person_seniorities: ["founder","c_suite","vp","director"]
```

Leave `include_similar_titles` at its default of true. Setting it false to force strict matching drops legitimate variants — "CTO / Managing Director" and "Co-Founder & CTO" are both real titles observed in live Zediant searches, and strict matching would have lost both. Small agencies and startups combine roles constantly; strict title matching is a filter tuned for enterprises.

Never target junior or individual-contributor titles. Zediant's deal size needs someone who can commit budget without procurement, which is why `icp.md` puts the persona at founder, C-suite, or VP.

## Step 4 — Build the filter set

### The geography trap

`person_locations` and `organization_locations` are **independent and ANDed**:

- `person_locations` = where the **person** lives
- `organization_locations` = where their **employer is headquartered**

Set only `organization_locations` and you get employees of Australian companies living anywhere on earth — a Melbourne agency's developer in Manila, a Sydney SaaS company's contractor in Bengaluru. They match the firmographic filter perfectly and are useless: wrong timezone, no local context, and a sequence written about the Australian market that reads as obviously untargeted.

You pay a credit per head to discover this, because search doesn't return emails — enrichment does. So the error surfaces only after you've spent. **Always set both filters.**

Verified working values: `"Australia"` (country-wide — the default starting value for any Australian search), `"United Arab Emirates"`, and, only when narrowing is actually needed, the state-level values `"Queensland, Australia"`, `"Western Australia, Australia"`, `"New South Wales, Australia"`, `"Victoria, Australia"`.

**Default to the country-level value.** Set both `person_locations` and `organization_locations` to `"Australia"` as the starting filter, not a single state. A state-only default silently shrinks the candidate pool to whichever state was picked and re-works the same names run after run — this is a real, observed failure from this pipeline (a production run defaulted straight to New South Wales for two of its five campaign searches, which mostly matched contacts already sitting in Zoho from prior runs), and `icp.md`'s own ICP definition never asked for anything narrower than the whole country in the first place. Narrow to one state only for a specific reason: the country-wide pool is oversized (see Step 8's "Over 1,000 results" diagnostic), or a specific state genuinely needs isolating for rotation-freshness (see Known regional pool sizes below for which state pools are small and exhaust fast). Metro-level values like `"Melbourne, Victoria, Australia"` are a second, tighter narrowing step below state-level — go country, then state, then metro, in that order, never starting at state or metro. If a state or metro search returns under ~40 entries, widen back out a step rather than loosening the segment or title filters — loosening the wrong dimension is how a targeted list becomes a generic one. Also confirm this isn't simply an unpaginated single-page result before widening geography — see Mandatory pagination above.

### Standard block

```
search_people(
  person_titles: [...],
  person_seniorities: [...],
  person_locations: ["<geo>"],
  organization_locations: ["<geo>"],
  q_organization_keyword_tags: [...],
  organization_num_employees_ranges: ["20,50","51,200"],
  contact_email_status: ["verified"],
  per_page: 25,
  page: 1
)
```

For a daily run, iterate `page` across rotated searches — see Mandatory pagination.

### Keyword tags

| Campaign | Tags |
|---|---|
| C1 — Funded SaaS | `["SaaS","software","technology","platform"]` |
| C2 — Agencies | `["digital agency","web development","software development","UI/UX","web design","digital marketing agency"]` |
| C2 — SaaS/product hiring signal | `["SaaS","software","technology","platform"]` |
| C3 — Platform/cloud modernization | `["SaaS","cloud","platform","DevOps","infrastructure","technology"]` |
| C4 — Middleware/API integration | `["SaaS","API","integration","middleware","technology","platform"]` |
| C5 — Product/enterprise modernization | `["software","technology","platform","enterprise software"]` |
| Vertical add-on: Automotive | `["automotive","dealer management","automotive software"]` |
| Vertical add-on: Logistics | `["logistics","supply chain","freight","transport"]` |

### Filter reference — verified behaviour

| Parameter | Status |
|---|---|
| `person_titles`, `person_seniorities` | Available |
| `person_locations`, `organization_locations` | Available — ANDed, set both |
| `organization_num_employees_ranges` | Available — string ranges `"11,50"` |
| `q_organization_keyword_tags` | Available — primary segment filter |
| `q_organization_domains_list` | Available — named accounts |
| `person_linkedin_urls` | Available |
| `contact_email_status` | Available — `["verified"]` narrows to deliverable |
| `currently_using_any_of_technology_uids` | Available — underscores for spaces |
| `organization_ids` | Available — must come from `apollo_mixed_companies_search` |
| `revenue_range` | Available but unreliable for private companies — prefer employee count |
| `organization_num_jobs_range` | **PLAN-GATED** — "Cannot access advanced filters on free plan" |
| `q_organization_job_titles` | **PLAN-GATED** — same error |
| `organization_department_or_subdepartment_counts` | **PLAN-GATED** |
| `organization_founded_year_range` | **PLAN-GATED** |
| `organization_headcount_growth_range` | Untested — likely gated, test with a small call first |
| `page` | Available — paginate to build a wide pool, see Mandatory pagination |

### The hiring-signal problem

**C2's hiring-signal sourcing profile depends on a hiring signal, and Apollo's hiring filters are gated on the current plan.** Both `organization_num_jobs_range` and `q_organization_job_titles` return upgrade-required errors.

This matters more than it first appears: C2's hiring-signal profile targets the most specific and most personalisable signal in the whole outbound set — a named role, open for a known number of days — and the filter that would find it is unavailable. That's a reason to work around it, not to abandon the campaign.

**Multiple simultaneous openings are a stronger version of this signal than one role.** A 100-person SaaS company hiring 3 backend engineers, 2 frontend engineers, 1 QA, and 1 DevOps engineer at once is stronger buying-signal evidence than a company with a single open role — this is raw pre-engagement signal evidence; it is not an ICP Score dimension and it does not itself produce either buying-propensity score. `ptb-scoring` remains the sole authority for PTB, calculated only once genuine engagement evidence exists.

| Method | Cost | Quality |
|---|---|---|
| Manual LinkedIn Jobs / careers page check on the shortlist | Free, slow | **Best** — confirms role count, seniority, and how long roles have been open |
| `apollo_organizations_job_postings` per company | 1 credit each | Good, expensive at scale |
| Headcount growth from enrichment output | Free once enriched | Proxy only — growth ≠ open roles |
| Web search "[company] careers engineering" | Free | Moderate |

Source the segment through Apollo, verify hiring manually on the shortlist, then score. Verifying 25 companies by hand is slower than a filter but it produces a signal you can quote in the first line of an email, which the filter never would have.

## Step 5 — Exclusions and dedupe, before enrichment

Screening after enrichment means paying for leads you then discard. Full exclusion rules in `icp.md`; Apollo implementation here.

| Category | Implementation |
|---|---|
| Recruitment / staffing agencies | Screen company names |
| Educational institutions | Screen `.edu`, `.ac.` domains |
| Freelancers, sub-10 companies | Employee range floor |
| Competitors | Check Partner/Overflow classification (Step 6a) for software dev shops/IT consultancies/MSPs — `competitors.md` documents zero named competitors (it's a category/positioning reference, not a screening list), so Partner/Overflow is the actual mechanism that catches this |
| Existing contacts | **`apollo_contacts_search` first** |
| Out-of-scope countries | Both location filters |
| Government | Screen `.gov` and names |
| Healthcare, education, construction | Not ICPs — see `icp.md` |
| IT services firms, software dev shops, consultancies | Not primary end-client prospects — see Partner / Engineering Overflow below, don't reject outright |

Name screen: `recruitment, recruiting, staffing, talent, headhunt, placement, university, college, institute, academy, bootcamp`

### Deduplication — the full cascade, not just HQ filtering

Zero duplicates is a tracked KPI, and re-enriching or re-importing a contact Zediant already holds spends a credit and creates a CRM duplicate for nothing. **Zoho is the permanent master exclusion database.** If a person or company already exists there under this workflow's matching rules, they are excluded permanently from Apollo daily prospecting — a higher score, a new trigger, a changed title, or a different campaign fit never overrides this.

Check in this order, and prefer exclusion over risking a duplicate when a match is uncertain — **but distinguish a confident match from a loose guess**, since over-matching is also a real cause of a batch coming back much smaller than the available pool warrants:

| Order | Match on | Zoho field | If matched |
|---|---|---|---|
| 1 | Apollo Person ID | `leadchain0__Social_Lead_ID` | Exclude — exact match only |
| 2 | Email | `Email` | Exclude — exact match only |
| 3 | LinkedIn URL | `LinkedIN_Link` | Exclude — exact match only |
| 4 | Company domain + person name | `Website` + `First_Name`/`Last_Name` | Exclude — domain must match exactly, name match should tolerate minor formatting differences (middle initials, nicknames) but not different people |
| 5 | Company name + person name, strong match | `Company` + `First_Name`/`Last_Name` | Exclude only on a genuinely strong match (same company, same person) — a shared surname, a generic company name fragment, or a partial string overlap is not a strong match. When in doubt on tier 5 specifically, treat as not-a-match rather than excluding — this tier is the fuzziest one and the most likely to over-exclude if applied loosely |

Run `apollo_contacts_search` before every net-new search — it is free. That covers Apollo-side duplication; the Zoho cascade above is what actually enforces the permanent-exclusion rule, since Apollo's own contact list and Zoho can drift out of sync.

**If dedupe is removing a large majority of a search-result page, verify it isn't over-matching before accepting that as the real duplicate rate.** A single day's search shouldn't ordinarily find that most of a fresh geography/segment rotation is already in Zoho unless that segment was worked very recently — check tier 5 matches specifically for false positives if the dedupe-exclusion count looks disproportionate to how much of that segment has actually been worked before.

**HQ filtering alone is not enough.** The obvious dedupe works for simple repeats — filtering `organization_locations` to Victoria structurally excludes agencies headquartered in Queensland or WA. But multi-office national agencies carry location records in several places: an agency headquartered in Brisbane with a Melbourne studio can surface in a Victoria search as apparently new, when its Brisbane MD was already worked six weeks ago. The prospect remembers even if a location filter doesn't match — and a second cold approach to the same firm from a different angle reads as either disorganised or automated.

Two things catch what HQ filtering misses:

- **Domain-level suppression.** Build a running list of domains already worked and screen every result set against it, regardless of the location filter. Domain is the stable identifier; office location is not.
- **Parent-brand suppression** where agencies trade under several names. Group holding companies operate multiple agency brands; a hit on one is effectively a hit on all of them for outreach purposes.

When running a geography sequence — Brisbane, then Perth, then Melbourne — carry the domain list forward across all of them rather than trusting each state's filter to be self-cleaning.

### Apollo-side processed list — secondary protection only

Where the account supports it (check `apollo_labels_index` / `apollo_labels_create`), maintain an Apollo label such as `Zediant - Processed Prospects` and add a prospect to it after a successful Zoho import. This catches the case where the same person resurfaces in a later Apollo search before Zoho has been re-synced.

**This is secondary protection, not the source of truth.** Zoho's dedup cascade above is the permanent record. If the Apollo label and Zoho ever disagree, Zoho wins — never import solely because a person doesn't carry the Apollo label, and never skip a person solely because they lack it if Zoho shows them un-imported.

## Step 6 — Optimise on signal, then enrich

### Technology Fit — an explicit scoring dimension, not a checkbox

`currently_using_any_of_technology_uids` lets Apollo filter on a company's live technology stack at search time, at no extra cost. Use it during initial prospecting rather than researching every company's stack manually after the fact.

Relevant technology areas (cross-reference `services.md`'s Technical Capabilities tables — this list should never drift from that document):

| Area | Examples |
|---|---|
| Application engineering | .NET, ASP.NET, C#, Java, Spring/Spring Boot, Python, Node.js |
| Frontend | React, Angular, JavaScript/TypeScript |
| Mobile | Flutter, Android, iOS |
| Cloud/platform | Azure, AWS, Google Cloud, containerisation |
| Integration/API | REST APIs, middleware, CRM/ERP integration, data integration |
| Enterprise systems | CRM, ERP, customer portals |

Assess fit in three tiers, and record which tier and why — this is raw evidence for ICP/fit assessment (Technology Fit is not a PTB category; PTB is calculated separately, only post-engagement, by `ptb-scoring`), so the reasoning needs to survive the handoff, not just live in this skill's working notes:

| Tier | Meaning |
|---|---|
| **Strong** | Company uses multiple relevant technologies with a clear connection to Zediant's capabilities (e.g., .NET + Azure + React) |
| **Medium** | At least one relevant technology present, but the business relevance to a Zediant engagement isn't yet clear |
| **Weak** | No meaningful technology connection found |

**Missing technology data is not automatically a negative signal.** Apollo's technology data coverage is incomplete — a company with no technology tags might still be an excellent SaaS/product fit. Don't reject a strong prospect on ICP and buyer-relevance grounds just because Apollo's technology field is empty; mark Technology Fit "Unknown" and let the other scoring dimensions carry the decision, same as `ptb-scoring`'s own Unknown-category discipline — but run the Signal Enrichment Pass above first, since a quick check often resolves what would otherwise sit as Unknown.

**Zoho has no dedicated Technology Fit field** (see crm-update's field mapping — the custom-field cap is at capacity). Carry the tier and the specific technologies found forward into the handoff table below; `crm-update` folds it into `Description`'s "Tech stack" line, same place `Technology_Stack` used to live before that field was retired.

### Signal priority

| Signal | Source | Strength |
|---|---|---|
| Recent funding | Web search, Crunchbase, Tracxn | **Highest** |
| Multiple simultaneous open senior eng roles | LinkedIn Jobs, careers page | **Highest** |
| Open senior eng roles (single) | LinkedIn Jobs, careers page | High |
| Acquisition / merger | Web search | High |
| Product launch / v2 | Company site | High |
| Technology modernisation initiative (legacy replacement, cloud migration announcement) | Web search, careers page (hiring for migration/platform roles) | High |
| Outage / scaling complaint | Status page, reviews | High |
| Headcount growth | **Enrichment output — free** | Moderate |
| Technology match (Strong tier) | `currently_using_any_of_technology_uids` | Moderate |

This table is the single source for signal strength — it is raw evidence that `ptb-scoring` evaluates to calculate the single numeric 0–100 PTB Score (Initial Buying Signal); it is not an ICP Score component, and it's the raw evidence handed downstream as context. There is no separate "Trigger Score" anywhere in this pipeline; a distinct trigger number was considered and deliberately not built, to avoid running parallel signal-scoring systems that could disagree with each other. Apollo Search collects raw signal evidence only; `ptb-scoring` is the sole authority for calculating the PTB score.

### Headcount growth — a free signal already in the enrichment response

`bulk_enrich_people` returns these at no extra cost, so there is no reason not to read them:
```
organization_headcount_six_month_growth
organization_headcount_twelve_month_growth
organization_headcount_twenty_four_month_growth
```

| 24-month growth | Read | Action |
|---|---|---|
| > +15% | Genuine growth, capacity pressure likely | Strong positive |
| +5% to +15% | Steady | Neutral positive |
| −5% to +5% | Flat | Verify other signals before scoring |
| < −15% | Contracting | **Flag it** — see below |

A sharply contracting company is genuinely ambiguous, and the ambiguity is worth surfacing rather than resolving silently. Either they cut the internal bench and now need external delivery capacity — which makes them a strong prospect for exactly Zediant's offer — or the business is shrinking and there is no budget behind the need. Both look identical in the data.

Score it Warm rather than Hot, note the ambiguity in the score rationale, and flag it for the BDM to qualify hard on the first conversation. Do not silently drop it; a bench-cutting agency is a real opportunity. Do not silently promote it either.

### Verify funding externally before scoring C1

Apollo does not carry reliable funding data. Web-search each shortlisted C1 candidate first — it costs nothing and it changes the score.

Companies that look like funded SaaS frequently turn out to be bootstrapped. Scoring one as "funded and scaling" produces outreach whose first line the prospect knows is false, and a wrong opening line is worse than no outreach — it tells them nobody looked. When a company turns out to be bootstrapped, that is not a disqualification: reframe to cost-efficiency, since a company growing without a raise scrutinises every hire.

## Step 6a — Partner / Engineering Overflow classification

Software development companies, IT consultancies, and technology service/managed-service providers are **not part of the primary end-client campaigns (C1–C5)**, even when they otherwise look like a technology company with the right size and buyer.

This surfaces more often than it might seem — a real example from this pipeline: an Australian IT consultancy offering cloud, cybersecurity, and AI advisory services scored well on every ICP dimension except one unresolved question — is it a genuine capacity-extension prospect, or a company competing in an adjacent part of Zediant's own market?

When a candidate's own business is software/IT delivery:

1. Do not route it into C1–C5 by default.
2. Classify it separately as **Partner / Engineering Overflow** — relevant for white-label development, delivery partnerships, subcontracting, or capacity partnerships, not as an end-client.
3. If genuinely ambiguous (offers services that overlap with Zediant's own, no clear signal either way), flag it as `RESEARCH_REQUIRED` with the specific question named, same as `lead-qualification`'s `RESEARCH_REQUIRED` discipline — don't force a campaign category to make the batch numbers work.
4. Never silently merge these into the standard prospect count without the classification note — a BDM scanning the batch needs to see "Partner/Overflow" distinctly from "C2 — Agency."

## Step 7 — Score before spending

Apply the ICP scoring model from `icp.md`. Score every result **before** enrichment — that ordering is the whole point, because scoring is free and enrichment is not.

| Score | Tier | Action |
|---|---|---|
| 80–100 | Hot | Enrich. Prioritise. Loop in Founder |
| 65–79 | Warm | Enrich. Standard sequence |
| 50–64 | Warm | Enrich only if batch size requires it |
| < 50 | Cold | **Do not enrich.** Nurture or reject |

Write a one-line reason for every score — specific, not generic. **It's the rationale a BDM reads when deciding whether to approve, and downstream it folds into the `Description` field in Zoho** (via `crm-update` — as of August 8, 2026 there is no standalone `Scoring_Reason` field to write to; it was deleted to make room for the LinkedIn outreach fields). *"C1 fit, funded 2mo ago, CTO reached, AU-based, Strong tech fit (.NET/Azure/React)"* tells them something. *"Good fit"* wastes the line and makes the approval gate a rubber stamp.

### Freshness / Why-Now Test — apply before ranking, not after

Before a candidate advances past scoring, answer plainly: **why might this company need Zediant in the next 3–12 months?**

- No credible answer → lower priority regardless of ICP score. A high-ICP company with no buying signal ranks below a slightly lower-ICP company showing real engineering demand — don't simply sort by ICP score.
- A credible, evidenced answer → raise priority.
- An exceptionally strong, evidenced answer (multiple simultaneous signals — e.g., funded + hiring + technology fit all present) → prioritise heavily, loop in the Founder per the Hot tier.

This is the same evidence discipline `lead-qualification` applies more formally at its own stage (Step 6, Business Challenges), applied earlier and more informally here at sourcing — it's a cheap filter before the expensive research step, not a replacement for that later qualification pass. This is evidence-gathering only; it is not PTB scoring, which `ptb-scoring` calculates separately as the single numeric 0–100 Initial Buying Signal Score before outreach.

### Batch health

| Metric | Healthy | Investigate |
|---|---|---|
| Hot + Warm share | > 70% | < 50% — filters too loose |
| Median score | > 70 | < 60 |
| Persona match | > 90% | < 75% — title set wrong |
| Geography match | 100% | Anything less — location filters misconfigured |
| Duplicates | 0% | Dedupe step skipped |
| Written batch as % of raw candidate pool | Roughly 15-30% is typical for a healthy, tightly-targeted daily run | Under 5% — run the Volume Diagnostic below before accepting it as a genuinely thin segment |

### Enrichment yield

Runs around 94%. Budget for 5–10% returning no usable email — `email_status: "unavailable"`, 0 credits charged for the miss. Keep a substitute from the next-highest scored candidate ready so a batch of 10 doesn't quietly become a batch of 8.

### Post-enrichment data traps

| Trap | Detail | Action |
|---|---|---|
| **Email domain ≠ website domain** | A company on `example.com` may send mail from `@example.io` or `@example.com.au`. Observed on roughly 1 in 5 real Zediant enrichments | Use the enriched email exactly. **Never construct one from the website** — a constructed address bounces, and bounces damage sender reputation for every campaign on that domain |
| **Catch-all domains** | `email_domain_catchall: true` | Deliverable but unconfirmed at mailbox level. A non-bounce proves the domain accepts mail, not that a human received it. Flag it in the handoff so a silent non-reply isn't read as rejection |
| **Masked last names** | Some plans obfuscate in search results | Expected, doesn't block enrichment — pass the person `id` |
| **Stale titles** | Check `last_refreshed_at` | Over 6 months old, verify before personalising on the title. Opening an email with a title someone left a year ago is worse than not personalising at all |
| **Missing `apollo_person_id`** | See Apollo Person ID Capture above | Not expected on a successful match — flag for investigation, don't leave silently blank |

## Step 8 — Diagnose and recommend

| Symptom | Cause | Fix |
|---|---|---|
| Under 20 results | Keyword tags too narrow | Broaden tags, add adjacent terms |
| Over 1,000 results | Segment too broad | Add employee range, narrow geography, tighten titles |
| Wrong personas | Seniority too loose | Tighten `person_seniorities`, drop `manager` |
| People in wrong country | `person_locations` unset | **Set both location filters** |
| Low Hot/Warm share | No signal in the filter set | Verify signals manually before scoring, run the Signal Enrichment Pass |
| Many contracting companies | No growth screen | Use headcount growth post-enrichment |
| Yield below 85% | Companies too small or obscure | Raise the employee floor |
| Duplicates appearing | Dedupe skipped, or HQ-only dedupe | Domain-level suppression — see Step 5 |
| Daily batch stuck well under 100 | Pool genuinely exhausted, or filters too tight | Check Known regional pool sizes; rotate geography per Search Rotation. **Do not loosen quality filters to compensate** — a small honest batch is a correct outcome |
| Written batch far below target *and* far below what the raw Apollo total suggests is available (e.g., 8-10 written against a 7,000-record segment) | Almost never genuine thinness — see Volume Diagnostic below | Run the Volume Diagnostic before concluding the segment is thin |

### Volume Diagnostic — when the written batch is far smaller than both the target and the available Apollo pool

If Apollo reports thousands of records in a segment but the written batch lands at single digits or low teens against a 100 target, check these in order — this combination should not read as "the market is thin," because a genuinely thin market shows up as a small *raw* pool, not a small pool after a large raw pull:

| Check | What to look for | Fix |
|---|---|---|
| 1. Was the pool actually paginated? | If only one `apollo_mixed_people_api_search` call was made (default `per_page=25`, no `page` iteration), the working pool was 25, not thousands — everything downstream inherited that | Apply Mandatory pagination above: raise `per_page`, iterate `page` until 300-500 raw candidates are actually pulled |
| 2. Is dedupe over-matching? | A large fraction of the (small) raw pool being marked as Zoho duplicates on a rotation segment that hasn't been worked recently | Re-check tier 4/5 matches specifically for false positives — a shared surname or partial company-name overlap is not a duplicate. See Deduplication above |
| 3. Are signal/Technology Fit Unknowns sinking real prospects? | Many companies appearing under-evidenced because signal and/or Technology Fit are Unknown, not because their fundamental fit is weak | Run the Signal Enrichment Pass above before finalizing scores — this recovers real data, it does not lower any threshold |
| 4. Are filters stacked too tightly for the segment? | Employee band + geography + title set + keyword tags together collapse a large segment to a small candidate set even before dedupe/scoring | Loosen one dimension at a time and re-check pool size — start with employee band width or metro-vs-state geography, not campaign or persona fit |
| 5. Is the campaign/title combination simply narrow for this market? | Some segment + title combinations (e.g., a specific vertical + C-suite-only titles) are genuinely narrow even before employee/geography filters | Confirm against `icp.md`/`campaigns.md` whether the title set should include VP/Director-level roles for this campaign, not just C-suite |

Report which of these was the actual cause once diagnosed — "today's shortfall was pagination (only page 1 was pulled)" is a very different finding from "today's shortfall was a genuinely thin segment," and the fix and the write-up should say which one it was rather than defaulting to the safer-sounding "market was thin."

### Known regional pool sizes

| Geography | Segment | Total |
|---|---|---|
| Queensland | Digital agencies | 222 |
| Queensland | SaaS / software | 1,374 |
| Western Australia | Digital agencies | 92 |
| Western Australia | SaaS / software | 619 |

Agency pools are small and exhaust fast — WA at 92 total depletes within days at the production maximum. When a pool runs dry, rotate geography. Do not loosen filters to hit a number; that produces exactly the generic list this skill exists to prevent, and it is the failure mode that looks like success in the daily metric.

Where a pool size isn't verified, say so. Estimating "Victoria is probably 250–400" is fine as a planning figure if labelled as an estimate; presenting it as verified is not.

**C3/C4/C5 pool sizes are not yet independently verified in this pipeline.** The SaaS/software totals above (1,374 Queensland, 619 WA) are the same underlying company universe C1, C2's hiring-signal profile, and C3–C5 all draw from — they differ by title and technology filter, not by company pool. Actual C3–C5 candidate counts will be tighter than the raw SaaS total once title/technology filters apply. Confirm with a real paginated pull the first time each is sourced rather than assuming parity with C1's observed pool size.

---

# DECISION RULES

| Condition | Action |
|---|---|
| Under 10 employees, unfunded | Reject |
| 10–19 employees, funded or strong other signal | Score on merits — don't reject purely on the count; see the employee-band note above |
| Would need 12+ engineers | Flag and escalate — exceeds Zediant's 5–7 developer, three-month ramp |
| Excluded industry | Reject |
| Software dev shop / IT consultancy / MSP | Classify as Partner/Overflow, don't route to C1–C5 by default — see Step 6a |
| No qualifying persona at the company | Suggest alternative titles there; if none, drop |
| Only a below-decision-level contact | Score persona low — usually falls under the enrichment threshold |
| No observable buying signal after the Signal Enrichment Pass | Score signal low — likely Cold, do not enrich |
| Multiple campaigns match (sourcing/search-priority only — not a final campaign assignment) | Prioritize per `campaigns.md` for sourcing purposes. **Referral/partner source overrides all** for sourcing priority. `campaign-selection` remains the sole authority for the final, single C1–C5 Primary Campaign assignment |
| Already in Apollo or Zoho | Skip, do not re-enrich, do not re-import regardless of new score or trigger |
| Domain already worked in a previous geography run | Skip — see Step 5 dedupe |
| No email returned | Log unmatched, substitute next-highest scored, disclose the swap |
| Catch-all domain | Proceed, flag in handoff |
| Insufficient credits | Report balance, propose a reduced batch, wait |
| Daily pool smaller than the 80 maximum production limit | Import what's genuinely qualified, report the shortfall plainly — never pad with weaker leads. Confirm via the Volume Diagnostic that the shortfall is genuine before reporting it as such |

---

# OUTPUT FORMAT

For a **search-design request**, return the filter block plus quality estimate, plan limitations, and optimisation suggestions.

For a **full sourcing run**, return:

```
## Search Summary
[Campaign, geography, segment, and — for a daily run — pool size at each funnel stage, including how many raw candidates were actually pulled via pagination]

## Filters Applied
[Exact parameter block, including per_page/page values used]

## Results
[Count, then a scored table: name, title, company, signal, technology fit, ICP score]

## Scoring Rationale
[One line per contact — specific, feeds crm-update's Description field]

## Enrichment
[Confirmed scope and cost before running. After: matched/unmatched, catch-all flags, apollo_person_id confirmed present for every matched contact]

## Partner/Overflow flagged
[Any candidates classified separately per Step 6a, with the specific reason]

## Handoff Package
[Field list below]

## Plan Limitations
[Any gated filter that would have improved this, and the workaround used]

## Credit Cost
[Search: 0. Enrichment: N used. Balance remaining: X]
```

For a **daily run feeding `scheduler-lead-population`**, additionally report the funnel breakdown (candidates reviewed → duplicates removed → ICP-rejected → weak-tech-fit → low-signal → deep-researched → qualified → imported) so the daily Cliq summary has real numbers to report against — see that skill's Step 9. If the written batch lands far below target relative to the raw pool, report the Volume Diagnostic finding explicitly rather than leaving it implied.

Keep the scored table compact. The BDM reading it wants to decide, not to read JSON.

---

# VALIDATION

Before returning a search or a batch:

- Every filter traceable to `icp.md`
- All titles carry budget authority at Zediant's deal size
- No excluded industries present
- **Both** `person_locations` and `organization_locations` set
- **`contact_email_status: ["verified"]` enforced on all candidate search queries**
- For a daily run, the raw candidate pool was actually built via pagination (25–50 for ramp-up, up to 300–500 for full ceiling), not a single default-sized page
- Employee floor excludes sub-viable companies, but a strong sub-20/sub-employee-band candidate wasn't rejected purely on headcount
- Zoho deduplication cascade applied, with domain suppression across prior geography runs, and tier-5 fuzzy matches double-checked for false positives
- The Signal Enrichment Pass ran on ICP-surviving candidates before finalizing ICP/fit scores (this pass produces raw evidence, which `ptb-scoring` uses downstream to calculate the numeric PTB Score)
- No phone or waterfall flags set
- `per_page`/`page` values used are stated, not just assumed
- Credit cost stated with the real current balance
- Every contact has a specific one-line scoring rationale, including Technology Fit tier where determinable
- **`apollo_person_id` confirmed present for every contact that came from a successful search/enrichment match** — missing ones flagged explicitly, not silently blank
- Software dev shops / IT consultancies flagged as Partner/Overflow, not silently routed to C1–C5
- Estimates labelled as estimates, verified figures labelled as verified
- Plan limitations disclosed where they affected the result
- Daily batch size reported honestly even when well under 100 — never padded, and any large shortfall relative to the raw pool traced to a specific cause via the Volume Diagnostic
- For a run not scoped to a single named campaign, the batch reflects coverage across C1-C5 per Campaign Coverage Rotation, not an unprompted default to just C1/C2

---

# ERROR HANDLING

| Error | Response |
|---|---|
| Campaign not specified | Ask. Never guess |
| Campaign unknown | "That isn't in `campaigns.md`. Current campaigns are C1-C5. Which applies?" |
| ICP undeterminable | "I can't map this to an ICP in `icp.md`. Can you clarify the segment?" |
| **"Cannot access advanced filters on free plan"** | Expected on gated filters. Remove it, apply the manual workaround, **disclose the limitation** in output |
| Zero results | Report and diagnose via Step 8. **Do not silently loosen filters** |
| Over 5,000 results | Too broad. Narrow before enriching anything |
| No email on enrichment | Log unmatched (0 credits), substitute, disclose |
| Insufficient credits | Report, propose reduced batch, wait |
| Rate limited / API error | Report. Do not retry blindly |
| Result exceeds context | Summarise. Never paste raw JSON |
| Candidate is a software dev shop / IT consultancy | Classify Partner/Overflow, don't reject outright, don't route to C1-C5 |
| Written batch far below target and far below the raw Apollo total | Run the Volume Diagnostic before reporting a thin-market conclusion |
| `apollo_person_id` missing on a matched contact | Flag for investigation, don't write blank silently — see Apollo Person ID Capture |

---

# ESCALATE

Stop and hand to a human when: a new market or geography is requested · a new service or capability is implied · campaign definitions conflict · the ICP can't be determined · enrichment would exceed available credits · the batch exceeds ~30 people (for a scoped request — daily runs are expected to be larger, see Candidate Pool Strategy) · the request implies phone numbers · a plan upgrade is implied · a referral/partner-sourced list is requested · an existing client or the dominant account appears in results · a Partner/Overflow candidate is genuinely ambiguous between partner and end-client classification · the Volume Diagnostic points at something beyond this skill's fix (e.g., a suspected Apollo account/plan issue).

---

# HANDOFF

Hand off per contact:

```
first_name, last_name, title, company, domain, work_email, email_status,
email_domain_catchall, linkedin_url, apollo_person_id, apollo_contact_id,
icp_score, tier, campaign_category, scoring_rationale, technology_fit_tier,
technologies_found, headcount_growth_24m, city, state, country,
partner_overflow_flag (if applicable), apollo_intent (if the account/plan
supports it, else omit entirely — never fabricate)
```

`apollo_person_id` is the value `crm-update` writes into `leadchain0__Social_Lead_ID` (Social Lead ID) in Zoho — always include it when available, it's the only Apollo identifier that persists downstream, and per Apollo Person ID Capture above it should be present for every contact that came from a real search/enrichment match this session. There is no Zoho field for `apollo_organization_id`, import date, or a batch/search ID — if any of these need to be preserved for traceability, fold them into the `Description` line `crm-update` writes, don't invent a new field to hold them.

**`apollo_intent` (new, optional) — Apollo's third-party buying-intent data (topic, signal/category, and/or score), when Apollo's response actually includes it.** This is a plan-gated Apollo feature, not guaranteed available on every account — most searches will not return it, and that is the normal, expected case, not a gap to flag. **Never fabricate, infer, or estimate an intent topic, signal, or score to fill this field** — include it only when Apollo's own response genuinely supplied it, verbatim. This is a distinct concept from ICP Score, Technology Fit, or either buying-propensity score `ptb-scoring` calculates — it must never be relabeled as one of those on the way through. `crm-update` appends it to `Description` when present; there is no dedicated Zoho field for it (same capacity constraint as Technology Fit and Apollo Organization ID, see Known Limitations).

Downstream, the `crm-update` skill handles CRM intake and enforces the BDM approval gate before campaign distribution. **No lead enters a campaign without `Lead_Status = Approved for Outreach`** — that gate is not this skill's to bypass or pre-empt. (This corrects an earlier version of this skill that named the gate `Qualifying_Status = Approved`; that field was retired and has since been deleted from Zoho. `Lead_Status` is the live gate — see `crm-update`.)

---

# SUCCESS CRITERIA

Hot + Warm share > 70% · enrichment match rate > 85% · verified email rate > 95% · zero duplicates · geography accuracy 100% · persona accuracy > 90% · **zero credits spent on Cold leads** · plan limitations disclosed on every affected search · under 20% of batches rejected at BDM approval · daily batch size reported honestly even when under the 80 maximum production limit, with zero instances of quality lowered to pad the count · **`apollo_person_id` present on 100% of matched contacts, missing cases flagged not silently blank** · a written batch under 5% of a large raw Apollo total triggers the Volume Diagnostic before being reported as a thin-market outcome · a non-campaign-scoped run reflects coverage across C1-C5, not an unprompted default to two campaigns.

The skill is working when the BDM approves most of what reaches them and the Founder never has to ask why a prospect is on the list.

---

# KNOWN LIMITATIONS

1. **Hiring-signal filters are plan-gated** — C2's hiring-signal sourcing profile can't be built on Apollo filters alone
2. **Funding data isn't in Apollo** — verify externally before scoring C1
3. **`organization_headcount_growth_range` untested** — likely gated
4. **Revenue filtering unreliable** for private companies — use employee count
5. **Agency pools are small** — WA 92, Queensland 222. Plan rotation
6. **Enrichment yield ~94%** — carry a substitute buffer
7. **No Zoho field for Technology Fit, Apollo Organization ID, import date, batch ID, or Apollo Intent** — all fold into `Description` via `crm-update`. This is a documented capacity constraint, not an oversight; revisit if the custom-field cap is ever raised.
8. **`per_page` defaults are small** — a search call without an explicit `per_page`/`page` strategy silently under-pulls a large segment. This was the primary driver behind an observed real-world case of an 8-10 lead written batch against a 7,000-record segment; see Mandatory pagination and the Volume Diagnostic.
9. **C3/C4/C5 pool sizes not yet independently verified** — see Known regional pool sizes note.
10. **Apollo Intent is plan-gated and often unavailable** — most searches will not return it; that's expected, not a defect, and it's never fabricated to fill the gap.

Version 1.9 · September 2026

**Changes in 1.9 — consistency pass (SURGICAL, EDIT-ONLY):**
- Corrected the production ceiling from a stale 200 (and, in one changelog note, 100) to 80 in every place it appeared (core operating principle, Candidate Pool Strategy, the daily-pool-shortfall diagnostic row, and Success Criteria), matching `scheduler-lead-population`'s current binding ceiling — this skill's own ceiling language had drifted out of sync with the orchestrator it feeds
- Corrected the Campaign Coverage Rotation table from its own approximate ranges (20-25/20-25/15-20/15-20/15-20) to the exact official Campaign Portfolio Allocation from `campaigns.md` (25/25/15/25/10) — the prior ranges under-targeted C4 and over-targeted C5 relative to the authoritative split
- Reworded the Step 5 "Competitors" exclusion row: it previously implied `competitors.md` is a named-company screening list, but that document explicitly states it names zero specific competitors (it's a category/positioning reference). Repointed the row at the Partner/Overflow classification (Step 6a), which is the mechanism that actually does this screening in practice
- Removed "senders" from the `campaigns.md` Context files summary — per explicit human instruction (September 2026), per-campaign sender/mailbox assignment is no longer tracked anywhere in the Revenue Engine; `campaigns.md` and `campaign-selection` v3.1 made the matching removal
- No changes to search filters, dedup cascade, scoring models, Partner/Overflow classification logic, Technology Fit tiers, or any other section

Version 1.8 · Filter behaviour, plan gating, pool sizes, and campaign rotation coverage verified against live Apollo searches, August 2026.

**Changes in 1.8 — optional Apollo Intent capture (EDIT-ONLY architecture update):**
- Added `apollo_intent` as an optional Handoff field — Apollo's third-party buying-intent data (topic/signal/category/score), captured only when the account/plan actually returns it, never fabricated or estimated when it doesn't. This is a distinct concept from ICP Score, Technology Fit, and either buying-propensity score `ptb-scoring` calculates
- Noted in Known Limitations (new item 10) that Apollo Intent is plan-gated and typically absent — that is the normal, expected case
- Updated Known Limitations item 7 to include Apollo Intent alongside the other fields with no dedicated Zoho slot, all folding into `Description` via `crm-update`
- No changes to scoring, filters, pagination, dedup, Partner/Overflow classification, or any other section — `crm-update` v5.2 is the corresponding downstream change that actually writes this data into `Description`

**Changes in 1.7 — Campaign Coverage Rotation:**
- Added a Campaign Coverage Rotation section (after Search Rotation) in direct response to a live run that sourced only C1 and C2 without being asked to, leaving C3–C5 unsourced by default habit rather than by any deliberate fit judgment
- Documented a default target-share split across C1–C5 for a ~100-lead-ceiling run, and how to scale that split down proportionally for a smaller ceiling-constrained run rather than collapsing to just the two fastest campaigns
- Flagged C3/C4/C5 pool sizes as not yet independently verified in Known regional pool sizes, distinct from the observed C1/C2 figures
- This section is explicitly overridden whenever the user names a specific campaign — it exists to prevent an unprompted default, not to force diversity against an explicit request

**Changes in 1.6 — Apollo Person ID capture, low-volume diagnosis, dedupe precision:**
- Added Apollo Person ID Capture as a mandatory, checked-at-handoff requirement, in direct response to a live run where `leadchain0__Social_Lead_ID` came back blank in Zoho despite Apollo-sourced leads. Root-caused to the ID not being consistently captured at search/enrichment time and carried forward as its own field, rather than reconstructed later
- Added Mandatory pagination guidance to Candidate Pool Strategy, naming under-pulled `per_page`/`page` defaults as the most likely cause of a written batch landing far below target despite a large available Apollo pool — a live run returned only 8-10 leads against a 100 target from a 7,000-record segment, traced to this
- Added the Signal Enrichment Pass — a bounded, free/cheap verification step run on ICP-surviving candidates before PTB-relevant scoring finalizes, to close Buying Signal/Technology Fit Unknowns that would otherwise sink real prospects to Cold. Explicitly does not lower any scoring threshold — recovers data, not leniency
- Added the Volume Diagnostic (Step 8) and a Decision Guide entry for "requested 100, got 8-10, Apollo shows thousands" — walks pagination, dedupe over-matching, PTB Unknown-sinking, filter stacking, and title/segment narrowness in that order
- Tightened Deduplication tier 5 (company name + person name) guidance to require a genuinely strong match, not a loose fuzzy one, since over-matching is a second plausible cause of an unexpectedly small written batch
- Added a "Written batch as % of raw candidate pool" row to Batch health, and Success Criteria now includes both the `apollo_person_id` completeness target and the sub-5%-of-raw-pool diagnostic trigger

**Changes in 1.5 — daily high-volume sourcing, technology fit, dedup cascade, partner classification:**
- Added Candidate Pool Strategy (wide-pool-then-funnel approach for daily runs feeding `scheduler-lead-population`) and Search Rotation, replacing ad hoc daily search planning
- Made Technology Fit an explicit three-tier scored dimension (Strong/Medium/Weak), cross-referenced to `services.md`'s capability tables and feeding `ptb-scoring`'s existing Technology Fit category — no new field, folds into `Description`
- Formalised the Zoho deduplication cascade (Apollo Person ID → Email → LinkedIn URL → domain+name → company+name) as the permanent exclusion mechanism; documented Apollo-side processed-list labelling as secondary protection only, Zoho remains master
- Added Step 6a — Partner / Engineering Overflow classification for software dev shops, IT consultancies, and MSPs that otherwise pass ICP screening but aren't primary end-client prospects
- Added the Freshness / Why-Now Test as an explicit pre-ranking gate
- Clarified that "Trigger Score" is not a separate score in this pipeline — signal strength folds into `ptb-scoring`'s existing Buying Signals category; a standalone trigger number was considered and deliberately not built
- Clarified the employee-band relationship between a 20–200 daily-sourcing default and `icp.md`'s wider per-segment bands, using a real sub-20 qualified lead from this pipeline as the reference case
- Made explicit that 100 leads/day is an indicative ceiling, never a quota — reporting a genuine shortfall is a successful outcome, never a reason to lower thresholds
- Added the "trigger category" label mapping table (Product Engineering/Engineering Expansion/Integration/Modernisation/Growth → C1–C5) so this planning language never gets written to `Lead_Campaign_Category` by mistake

**Changes in 1.4:** Retired the List A-E sourcing taxonomy entirely — it was stale and no longer matched live campaign routing. Step 1 segment table, Step 3 title sets, and the keyword tags table now key directly off `campaign-selection` v2.1's C1-C5 registry and Segment/Signal precedence walk (C1 funded SaaS, C2 agencies or hiring signal, C3 platform/cloud modernization, C4 middleware/integration, C5 product/enterprise modernization). All List A-E references removed from the Decision Guide, Decision Rules, Error Handling, Escalate, and Known Limitations sections.
