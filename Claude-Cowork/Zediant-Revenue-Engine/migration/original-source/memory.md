**Purpose & context**

Jay is building a fully automated AI-driven outbound B2B sales pipeline for Zediant Technologies, a software engineering services company positioned as a dedicated engineering partner for SaaS, ISV, and digital agency clients, primarily targeting Australia and UAE markets. The goal is an end-to-end system that sources, qualifies, enriches, and routes prospects into personalized cold outreach campaigns with minimal manual intervention, gated by a BDM approval step.

**Key team members:**
- **Rajeev** (Founder, rajeev@zedianttechnologies.com) — strategic accounts, discovery, closing
- **Pritamjit** (BDM, pritamjit@zedianttechnologies.com) — primary outbound, BDM approval gate
- **Manish** (Engineering lead, manish@zedianttechnologies.com) — technical conversations

**Core services / campaign offerings:**
- C1: AI-Enabled Product Engineering
- C2: Engineering Pods & Staff Augmentation
- C3: Platform Engineering & Cloud Modernization
- C4: Middleware & API Integration (ZCoupler)
- C5: Enterprise Custom Development & Modernization

---

**Current state**

**Stack:** Zoho CRM + Saleshandy (migration from Instantly complete as of Aug 5, 2026). Apollo.io retained for sourcing and enrichment only. Zoho Cliq for internal notifications. All orchestrated via Claude skills in Cowork.

**Active campaigns (Saleshandy):** C1–C5, each with 5-step sequences and 25 email templates. Sender assignments: manish@ → C1, C3; rajeev@ → C2, C5; pritamjit@ → C4.

**Instantly campaign IDs** (retained for reference, per Jay's instructions):
- C1: `1b2052d8-6d33-420c-aa51-e24ef123ed99`
- C2: `d33c972e-d6f4-4da0-91e8-b6bbde1f9a6c`
- C3: `9edf6962-527f-40f4-a30e-46384ec26df1`
- C4: `ba47f6dc-ec08-4d48-8910-d5262de790df`
- C5: `9053afd4-07f6-43e1-857a-3b587fcea57f`
All Draft status (0), 5-email sequences with 3 subject line variants per step. AI SDR campaign (status -1) dropped.

**Scheduler architecture (approved Aug 5, 2026):**
- **Scheduler 1** (7:00 AM IST) — Lead Population: Apollo sourcing (default 50 leads, configurable) → Lead Qualification → Email-Personalization-Enrichment → PTB Scoring → Campaign Selection → Zoho write ("New Lead"). Skips Cold leads (PTB <50). Deduplicates via Zoho COQL batch query first, then Apollo. Batches all Zoho writes (3 API calls total). Logs to Cliq with breakdown by campaign + cold/failed leads. Default geography: Australia (configurable).
- **Scheduler 2** (8:00 AM IST) — Saleshandy Distribution: Pushes leads where `Lead_Status = "Approved for Outreach"` and `Skype_ID` is empty. Batches by C1–C5. Checks duplicates via `apollo_contacts_search`. Updates Zoho `Skype_ID` after push. Logs to Cliq. Both schedulers are loosely coupled, sharing Zoho state independently.

**BDM approval workflow:** S1 writes `Lead_Status = "New Lead"` → BDM (Pritamjit) reviews enrichment fields and can correct opening lines → manually sets `"Approved for Outreach"` → S2 pushes to Saleshandy → `"Outreach Scheduled"`. Reply-Tracker monitors Saleshandy and alerts zsales Cliq channel only (no individual @mentions); BDM manually updates to `"Engaged"`.

**Email-Personalization-Enrichment skill** (new, integrated into S1 after Lead Qualification, before PTB Scoring): Researches each qualified lead (company website, news, hiring, products, recent launches) and generates four mandatory Zoho custom fields for Saleshandy merge tags:
1. **Email Personalised Opening** (~15–25 words, one specific verifiable company observation)
2. **Email Pain Points** (~15–25 words, engineering/product pressure)
3. **Case Study** (~15–25 words, verified Zediant client example — three-tier fallback: direct match → adjacent match → generalized truthful statement)
4. **Business Challenge** (~15–25 words, client's actual challenge)

All fields must be specific, natural language, no marketing jargon, no unsupported claims. Validates all four fields before Zoho write. No invented information.

**Zoho CRM state:**
- Free edition, three user licenses, field cap of 10 custom fields per module (Leads module was at capacity, requiring workarounds)
- Workarounds applied: `Skype_ID` repurposed as "Instantly Campaign ID" / S2 duplicate gate; `Rating` repurposed as "Outreach Status"; `leadchain0__Social_Lead_ID` used for Apollo Contact ID (label unchangeable); `Description` used as shared textarea for AI Summary and Buyer Intent; `Personalization_Notes` added as final dedicated custom field
- Custom fields across Accounts, Contacts, Deals: `Technology_Stack`, `Existing_Customer`, `Strategic_Account`, `Decision_Maker`, `Competitor`
- C1–C5 picklist values confirmed added to `Lead_Campaign_Category` (Aug 5, 2026)
- `Qualifying_Status` field completely removed; `Lead_Status` is the sole workflow trigger
- Zoho Cliq channel ID: `P1064180000000316007` (fallback: look up unique name via channel list tool)

**Active skill set (Set B — Saleshandy architecture):**
- `scheduler-lead-population` v4.0
- `crm-update` v3.0
- `saleshandy-distribution`
- `saleshandy-reply-tracker`
- `email-personalization-enrichment` (new, ready for implementation)
- `email-personalization` v2.2
- `zediant-apollo-prospecting`, `zediant-zoho-pipeline`, `zediant-reply-notifications`

**Campaign 1 email sequence:** 5-email cold outreach for AI-Enabled Product Engineering targeting CTOs, VP Engineering, Heads of Engineering at 20–200 person SaaS/ISV/product companies. Progressive story arc: relevance → problem → credibility → alternative angle → polite close. Uses Saleshandy merge tags. Passed all 17 quality checks.

---

**On the horizon**

- **Email-Personalization-Enrichment implementation:** Skill is built and ready; estimated 3–4 hour implementation. Phased install with testing protocol and rollback plan documented.
- **Campaign email sequences for C2–C5:** Only C1 sequence is built; remaining four campaigns need sequences.
- **Zoho Free edition field cap:** A persistent constraint — any future CRM field additions require deliberate planning around the 10-field cap and potential repurposing of existing fields.
- **Mailbox warm-up:** Campaigns remain in Draft status pending mailbox readiness before activation.
- **Saleshandy workspace timezone:** Confirmed as India (UTC+5:30); campaign-level timezone adjustment optional per geography.

---

**Key learnings & principles**

- **Apollo enrichment timing:** Enrichment calls should happen only after all qualification gates (qualification, PTB scoring, campaign selection) to avoid spending credits on leads that don't survive screening.
- **Zoho deduplication efficiency:** Collapse per-lead `searchRecords` calls into one COQL batch query — critical for staying within API limits and token budgets.
- **Field repurposing over new fields:** On Zoho Free, repurposing stock fields (Skype_ID, Rating, Description) is a necessary workaround. Deleted fields still count against the cap until permanently purged from trash.
- **Skill ecosystem clarity:** Two competing skill sets (Instantly-based Set A and Saleshandy-based Set B) coexisted in the skills folder. Set B is the confirmed active architecture. Any new work should align with Set B.
- **Case Study fallback system:** Three-tier approach (direct match → adjacent → generalized truthful statement) ensures the field is almost always populated without fabrication — avoids leaving merge tags blank in emails.
- **Approved statistic protection:** The "40% faster" result claim in the C1 Day 2 email is approved and must not be altered or have competing performance claims added alongside it.
- **BDM review value:** Personalization enrichment runs in S1 (not S2) so Pritamjit can review and correct opening lines before approving — a deliberate human quality gate.
- **Banned language list:** A defined list of prohibited marketing language applies across all email copy and enrichment fields: "leverage," "seamless," "AI-powered," "transformative," "cutting-edge," em dashes, en dashes, and similar generic sales language.

---

**Approach & patterns**

- **Jay as decision-maker:** All major architectural choices (platform selection, field design, skill merging/splitting, workflow gates) are confirmed with Jay before implementation proceeds.
- **Cost minimization as a design constraint:** Both Claude token usage and Apollo API credit spend are explicit design constraints factored into every skill and workflow design decision.
- **Batch-first API design:** All CRM writes, Apollo searches, and Saleshandy pushes are batched wherever the API supports it; per-record loops are avoided.
- **Human gates over full automation:** The BDM approval step is intentionally preserved as a human checkpoint — the system is designed to assist, not bypass, human judgment on outreach decisions.
- **Skill modularity:** Skills are kept as separate files with clear responsibilities; merging is only done when explicitly justified by reducing redundancy.
- **Validation before write:** Enrichment skill validates all four generated fields before writing to Zoho — no partial writes.

---

**Tools & resources**

- **CRM:** Zoho CRM (Free edition, 3 users)
- **Outreach:** Saleshandy (C1–C5, 5-step sequences)
- **Sourcing/enrichment:** Apollo.io (Basic tier, 6 Bombora intent topics; credits reserved for post-qualification enrichment)
- **Notifications:** Zoho Cliq (zsales channel)
- **Orchestration:** Cowork scheduler (two daily scheduled tasks)
- **Skills platform:** Claude skills / MCP connectors (Zoho MCP, Saleshandy MCP, Apollo MCP, Instantly MCP retained)
- **Key Saleshandy MCP notes:** Prospects enroll at a *step* not a sequence — must call `list_sequence_steps(sequenceId)` to get Step 1 ID before `import_prospects_to_sequence_step`. `list_sequences` returns `payload[].id` and `payload[].active`; match by title prefix (e.g., "C1 - "), not exact title.
- **Key Apollo MCP notes:** `apollo_mixed_people_api_search` does not return emails — requires separate `apollo_people_bulk_match` (max 10/call, 1 credit/match). Never set `reveal_phone_number`, `run_waterfall_phone`, or `reveal_personal_emails` flags. Use `per_page=25` to reduce round trips.
- **Skill packaging:** `python3 -m scripts.package_skill` run as a module from the `/mnt/skills/examples/skill-creator` directory.