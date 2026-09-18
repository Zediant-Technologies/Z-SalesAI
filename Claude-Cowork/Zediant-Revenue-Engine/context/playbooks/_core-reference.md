# Core Reference — condensed from icp.md, company.md, services.md, case_studies.md, competitors.md

*Sources: `context/icp.md` (verified against its September 2026 ICP-Score-model fix), `context/company.md`, `context/services.md`, `context/case_studies.md`, `context/competitors.md` · condensed September 2026 for token efficiency. This is a summary for day-to-day scoring — for a genuinely novel edge case (a new excluded industry, a DATA CONFLICT, an escalation trigger not listed here), read the source file rather than guessing from this digest.*

## ICP Score — six weighted dimensions, 0-100 total

Set once at sourcing. Buying signal is **not** part of this score — it's PTB's job (see `ptb-scoring`), never combined or averaged with ICP Score.

| Dimension | Weight | What it measures |
|---|---:|---|
| Business Fit | 25 | Ongoing roadmap/recurring pipeline, constrained internal team, hiring/trying-to-hire, scaling/funded trajectory |
| Technical Fit | 20 | Stack overlap (.NET, Java, React, Node, PHP, mobile, cloud); work type (product dev, integration, modernization, platform — not AI/ML research, computer vision, speech AI); architecture (web/mobile/API/microservices — not firmware/real-time control/HPC) |
| Commercial Fit | 15 | Deal size viable (USD 10-20K fixed, or USD 80-150K+ annualised pod); accepts senior-rate positioning; supports ≥USD 25-30/hr blended rate; not demanding free POC/unpaid tender docs |
| Strategic & Growth Fit | 15 | New logo (reduces concentration) > dominant-client expansion; reference potential; AU/UAE depth; small-scope-with-expansion-surface pattern |
| Persona Fit | 15 | Founder/CEO, CTO, COO score highest; VP/Head of Eng good; CIO/IT Director workable (implies procurement); EM/PM-only weak; no named contact = flag for enrichment |
| Geography Fit | 10 | Australia or UAE = full marks; secondary markets (UK/US/South Africa) score lower |

**Verdict bands:** 80-100 QUALIFIED (Hot, act now) · 50-79 QUALIFIED (Warm, standard) · 30-49 RESEARCH_REQUIRED (name the specific evidence gap) · <30 REJECTED · **any hard disqualifier below = REJECTED regardless of score.**

## Hard disqualifiers — reject regardless of score

Needs 50+ engineers ramped immediately · core need is AI/ML research, model training, computer vision, or speech AI · needs low-code/no-code platform work · needs embedded/firmware/SCADA/industrial-control/robotics-control/telematics software · requires full on-site presence, non-negotiable · expects free POC or unpaid tender documentation · competing purely on lowest hourly rate · requires certifications Zediant can't evidence (ISO 27001, ISO 9001, CMMI) · public-sector tender without a Teaming Agreement · recruitment/staffing agency · university/college/bootcamp/individual learner · direct competitor seeking to resell capacity without a partner agreement · existing Zediant client (route to account management, not new pipeline).

**Soft disqualifiers (deprioritize, don't enrich, not an automatic reject):** under 20 employees with no funding · no engineering team/technical counterpart · already runs a captive offshore dev centre · recent material layoffs with contracting roadmap · excluded industry with no segment override (see below).

## Excluded industries (classify by what the company *is*, not by its customers)

Not ICPs: Healthcare (unproven, no case study, regulatory burden — opportunistic only), Education, Construction, Professional Services *as a buyer* (they're a partner-channel target, not an end client), Government (actively deprioritized, needs a Teaming Agreement), Media & Entertainment (unproven), Real Estate (unproven). A funded SaaS company that happens to sell into one of these is still a SaaS prospect — segment governs, not the customer's industry.

## Geography and capacity

**Primary: Australia and UAE only.** UK/US/South Africa are secondary/opportunistic, not a default target. Primary employee band: **20-200** (this is the daily-sourcing default, not an absolute cutoff — a strong sub-20 funded company or an unusually strong vertical-specific case can still qualify on merits; verticals like Automotive/Fintech/Manufacturing/Logistics/Retail carry their own wider documented bands).

**Zediant's capacity ceiling:** 25-35 total headcount, can onboard 5-7 additional developers within three months. Never promise or imply a ramp beyond that. ~90% of revenue concentrated in one dominant client — a new logo is worth more than its revenue suggests; never name the dominant client externally.

## Escalate to a human, don't answer directly

Request for the SOC 2 Type II attestation report or a security questionnaire requiring certification evidence · request for a client reference (most case studies are anonymised/restricted) · request for an SLA with financial penalties · request for 24/7 on-call coverage · enterprise deal requiring 12+ engineers · any request for free speculative work · a prospect that may be the existing dominant client or a competitor · an industry/segment `icp.md` doesn't cover.

**SOC 2 wording — always:** default to **"SOC 2 Type II aligned."** Never assert a completed attestation, never repeat "externally audited" or "we've passed the toughest security audit." Zediant's own materials inconsistently say aligned/certified/compliant — "aligned" is the safe, current default everywhere.

## Never cite these unsubstantiated figures

30-40% faster delivery/time-to-market · 99.99% availability · "millions of concurrent users" · 30% efficiency increase for UAE automotive partners (unverified as stated, distinct from CS-08's own documented, properly-attributed 30% traffic figure). A real, approved case-study metric (e.g. CS-06's 70%→93% test coverage) is fine to cite exactly as documented — the line above is about invented or generalized stats, not real ones.

## Not offered — never represent as a Zediant service

Low-code/no-code platform development, computer vision, speech AI, deep AI/ML research or foundation-model building, standalone data science consulting, brand/marketing strategy, content creation, SEO execution, data migration as a standalone service.

## Case study governance

Every case study in `case_studies.md` is marked confidentiality-restricted (anonymised or named-with-restrictions) and requires human approval before external use — **the existing BDM approval gate (`Lead_Status` → "Approved for Outreach") is that human approval**; no separate case-study sign-off step exists. Never invent a customer, metric, technology, or outcome. **CS-02 and CS-06 are the same customer/account — never present as two separate customers, never use both in one conversation.** Confidentiality is per-entry (some are named with restrictions, most are anonymised, describe by category only) — check the specific entry before naming anything. "ZCoupler" is C4's internal/context-only capability name; prospect-facing content always says **"Zediant Middleware"** or "integration and middleware engineering" instead.

## Competitors — there is no named-competitor exclusion list

`competitors.md` documents **zero specific named competitors** — it's a category/positioning reference (large IT services firms, offshore boutiques, freelance marketplaces, local agencies, staff-aug firms, iPaaS platforms, AI-native firms), not a screening list. The mechanism that actually screens out competitor-shaped candidates is **Partner/Overflow classification** (`apollo-search-builder` Step 6a) — software dev shops, IT consultancies, and MSPs get classified there, not routed to C1-C5.

## Concentration check

Zediant treats reducing single-client concentration as a standing priority ranked alongside growth. Where two leads are otherwise equal, the one that diversifies the client base is the better lead. An expansion opportunity at the already-dominant account is not new pipeline — flag it and route to account management instead of qualifying it as new.
