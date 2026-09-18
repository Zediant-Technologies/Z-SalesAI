---
name: email-personalization
description: "Zediant's email + LinkedIn personalization SOP - generates Email Personalised Opening, Email Pain Points, Case Study, Business Challenges, and the merged LinkedIn Message & Follow-up field for every qualified lead past Campaign Selection. Reads zediant_outreach_natural_language_blacklist.md before drafting, applying its avoid-list and 15-25 word target during generation, not after. LinkedIn CONNECT is the real connection request (no Zediant mention, no pitch, no CTA, no meeting ask), built on a verified signal or an honest fallback, never fabricated. FOLLOW-UP may carry soft context but never pitches or asks for a meeting. Generated for every lead regardless of LinkedIn Status (priority flag, not a gate). Use for \"personalize this email for X\", \"should X get LinkedIn outreach\", \"write the LinkedIn message for X\". Literal, ready-to-send copy - no analytical/AI phrasing, no em dash, no LinkedIn cliche phrasing. Zoho/Apollo variables only, does NOT send. Never fabricates a fact, signal, or case study."
---

---
name: "email-personalization"
metadata:
  version: "3.0"
---

# Email + LinkedIn Personalization

Generate the specific, verified detail that makes one email — and, now, one LinkedIn touch for every qualified lead — read as written for this company rather than copy-pasted at it. Package it as Zoho field values, not prose.

## The one thing to understand before anything else

**The production model is two channels from one research pass, for every qualified lead.** Every qualified lead gets Email personalization **and** LinkedIn Message & Follow-up content. `LinkedIn Status` (`Ready to Connect` / `Not Required`) is a separate, batch-level **outreach priority flag** — it tells the BDM and the manual LinkedIn process approximately the top quarter of the written batch to actually work first on LinkedIn. It is not, as of this version, a gate that decides whether LinkedIn content gets written at all. Both channels come from the same underlying research and the same single outreach angle — see **The One Primary Angle** below. Do not treat LinkedIn Selection as a separate skill invocation from Email personalization; they happen in the same pass, for the same reason, off the same evidence.

**Why this changed:** earlier versions of this skill only generated LinkedIn content for `Ready to Connect` leads, leaving `Not Required` leads with a blank `LinkedIn_Message` field. In production this meant that if a `Not Required` lead's priority changed later (a new signal appeared, a BDM wanted to work it manually, or the batch ranking was revisited), there was no LinkedIn content sitting ready to use — the whole personalization pass would need to be re-run for that one lead. Generating the content for everyone up front removes that gap at effectively no extra cost, since the research and the single outreach angle (Step 5) are already being done for the Email channel regardless.

**`campaigns.md` already defines the messaging layer for each campaign** — its Messaging Angle, Recommended Email Tone, example Personalization Opportunities, Recommended CTA, the four-touch Email Sequence Strategy, and a Related Case Studies shortlist. That layer is generic to the campaign; it's the same for every company in C1, for instance.

This skill's job is the layer campaigns.md deliberately leaves blank: **which of those generic opportunities is actually true of this specific company, and what's the evidence.** Read the selected campaign's messaging layer first, then find the concrete fact that instantiates it. Don't invent a new messaging angle or CTA — those are already decided. Don't skip finding a real fact and write something generic that merely sounds personalized.

**This skill does not write the email itself.** The approved email structure lives in the live Apollo template. This skill fills in the merge-tag blanks in that template — `Email Personalised Opening` and `Email Pain Points` directly, plus `Business_Challenges`/`Case_Study` which also land as live merge tags further down the sequence — with real, checkable content — see **Apollo Template Compatibility** below. If the user explicitly asks for a full email draft, that's a different, larger request — flag that you're stepping outside the variable-generation scope before doing it.

## Scope — and the boundary that matters

**Owns:** producing verified Email and LinkedIn personalization content for one named company and contact, deciding whether that company is in the priority slice for active LinkedIn outreach as part of the current batch, and packaging it ready for `crm-update` to write.

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Deciding whether the company is worth pursuing | `lead-qualification` |
| Calculating the priority score | `ptb-scoring` |
| Choosing which campaign the company enters | `campaign-selection` |
| The campaign's messaging angle, tone, CTA, and sequence structure | Already decided in `campaigns.md` — read it, don't re-derive it |
| Writing the Apollo template itself, activating a campaign, or sending anything | Nobody, automatically. Apollo holds the approved templates; activation is an explicit human action |
| Writing personalization data into CRM fields, or writing `LinkedIn Status` to Zoho | `crm-update` skill — this skill decides the value, that skill writes it |
| Actually sending the LinkedIn connection request, message, or follow-up | A human, manually, using the content this skill produces — regardless of `LinkedIn Status` |
| Formal proposals or SOWs | `proposal-generation` |

## Context files — reference, never restate

**For day-to-day personalization, read `context/playbooks/C{1-5}.md` (that lead's campaign) and `context/playbooks/_blacklist-digest.md` instead of the full source docs below** — the playbook carries the campaign's Messaging Angle, Tone, Personalization Opportunities, CTA, and its case study(ies) with confidentiality/disclosure notes already resolved, pre-extracted from the same sources. Open the full docs only for a genuinely novel edge case.

| Document | What it supplies |
|---|---|
| `zediant_outreach_natural_language_blacklist.md` | The full avoid-list and per-field rules behind `_blacklist-digest.md` — read this directly only if the digest doesn't resolve a specific phrase question. **Read the digest (or this file) first, every time, before generating or updating any of the four content fields — see the mandatory pre-generation step below.** |
| `campaigns.md` | The selected campaign's Messaging Angle, Tone, example Personalization Opportunities, Recommended CTA, Email Sequence Strategy, Common Objections, and Related Case Studies shortlist — condensed into that campaign's playbook |
| `services.md` | Which Zediant capability matches the confirmed business challenge, and the "Unsubstantiated performance claims" table of statistics that must never be cited — condensed into `_core-reference.md` |
| `case_studies.md` | Each case study's actual disclosure status (`ANONYMISED`/`NAMED`) and usage restrictions, and the structural warnings (CS-02/CS-06 same-client, concentration-risk overuse) — condensed per-campaign into the playbooks' Case study sections |
| `company.md` | The SOC 2 Type II wording rule if the personalization touches security or compliance messaging — condensed into `_core-reference.md` |
| `pricing-public.md` | Commercial context if a personalization angle implies a pricing conversation |
| `campaign-selection` | Owns the selected campaign this skill reads rather than re-deciding |
| `ptb-scoring` | Owns the single numeric PTB Score (Initial Buying Signal, 0–100) used for prioritization |

**Cite only sections that actually exist, by their real names.** A true fact with a fabricated citation is still a fabrication problem — it just fails a different way, on a spot-check rather than on the fact itself. Before finalizing output, mentally re-locate every named table or section you cited; if you can't, rephrase it as your own reasoning instead.

## Workflow position & Email-Only Execution Standard

This skill sits here in the finalized pipeline: **Lead → Lead Qualification → ICP Score → PTB Score (`ptb-scoring`) → Campaign Selection → Email Personalization.** 

A newly Qualified lead reaches this skill carrying a single numeric **PTB Score (Initial Buying Signal, 0–100)** calculated pre-outreach. `ptb-scoring` is the sole authority for this score.

**Email-Only Priority Rule:**
During this production phase, outbound outreach is focused 100% on cold email deliverability and sequence execution. Generating manual LinkedIn tasks is de-emphasized to eliminate friction in the BDM review queue. The priority outputs for every lead are:
1. `Email_Personalised_Opening` (15–25 words, natural, evidence-based, bans AI clichés)
2. `Email_Pain_Points` (specific technical/operational challenge matching the campaign)
3. `Business_Challenges` (concise summary of the verified challenge)
4. `Case_Study` (relevant anonymized or named case study from `case_studies.md` if applicable)

**Low-Friction Call to Action (CTA) Requirement:**
Touch 1 emails must **never** ask for a 30-minute meeting or push a calendar link. The CTA must be low-friction, permission/curiosity-based:
- *"Open to checking a 2-minute teardown of how we built this for [similar client/domain]?"*
- *"Worth a quick chat to compare notes on this, or should I leave you in peace?"*
- *"Would you be open to seeing our benchmark on this setup?"*

---

# REQUIRED INPUTS

Company Name · Company Website · Industry · Business Description · Country · Employee Count · Buying Signals · Business Challenges (`Business_Challenges`, carried forward from `lead-qualification`'s Step 6 finding) · Selected Campaign (C1-C5) · Decision Maker · Recent News (if available) · Case Studies · numeric PTB Score (from `ptb-scoring`) · ICP fit.

Nearly all of this already exists from the `lead-qualification` and `campaign-selection` passes that got the company here, plus `ptb-scoring`'s output. Re-read those outputs before searching for anything new — this skill's genuinely new research is narrow: confirming the personalization angle is still current, and finding the one or two specific facts that make the opening line concrete.

**Do not invent:** funding, hiring activity, technology usage, product launches, company initiatives, business problems, budgets, projects, customer problems, growth figures, or technology platforms. If a specific signal cannot be verified, use a broader but credible business/engineering observation and say so.

---

# WORKFLOW

## Step 0 — Read the natural-language blacklist before writing anything

Before generating or updating any of the four fields this skill produces or feeds — `Email_Personalised_Opening`, `Email_Pain_Points`, `Case_Study`, and `Business_Challenges` — read `context/playbooks/_blacklist-digest.md` (or the full `zediant_outreach_natural_language_blacklist.md` if a specific phrase question isn't resolved by the digest) and hold its rules in mind through Steps 1-9. This is not a filter run after the fact: the blacklist's avoid-list, natural-writing examples, and per-field guidance (Rules for the Four Zoho Fields) shape the wording as it's written, the same way `campaigns.md`'s messaging layer does. Generating content first and blacklist-checking it afterward produces the same promotional-sounding draft with a few words swapped out — the goal is content that never reads that way to begin with.

The file is explicit that it's a language-quality guide, not a literal spam filter: a true, necessary fact about the prospect or the case study is never distorted or dropped just because a word on the list would otherwise describe it accurately — rewrite the sentence around it instead. Its Final Quality Check (10 items) and closing test — *"Would this sound normal if a Zediant salesperson personally typed this email to one CTO?"* — are folded into this skill's own Validation and the human-writing test at the end of Step 9 below, not run as a separate pass.

## Step 1 — Read the selected campaign's messaging layer

From `context/playbooks/C{1-5}.md` (that lead's selected campaign), pull the Messaging Angle, Tone, Personalization Opportunities, CTA, and Case study section — pre-extracted from `campaigns.md`. Don't introduce a Zediant service unrelated to the selected campaign. Open `campaigns.md` directly only if the playbook's Messaging Angle genuinely doesn't cover a detail you need.

## Step 2 — Confirm the company profile

Industry, business model, and growth stage should already be established. Read the qualification, `ptb-scoring`, and campaign-selection outputs rather than re-researching from scratch.

## Step 3 — Find the recipient's actual context

Determine role, likely responsibilities, and likely priorities from what's genuinely available (title, LinkedIn headline if provided, the campaign's documented persona). Job title and public professional activity are fair game; personal life, family, or anything scraped from a non-professional context is not, regardless of whether it was technically findable — see "Never over-personalize" below.

## Step 4 — Find the specific fact that instantiates the campaign's angle

The campaign's Personalization Opportunities section names *categories* (recent hiring, a product launch, an expansion, a specific technology). Find the actual instance for this company.

**Decision order when more than one candidate fact exists:**

1. Verified recent news (funding, acquisition, launch, expansion) — most timely, strongest opener
2. Verified hiring activity, especially matching the campaign's target signal
3. A specific, verifiable detail from the company's own site or public materials
4. Industry-level personalization as the fallback, if nothing company-specific and verifiable turned up

Don't skip straight to industry-level personalization because it's easier. Only use it when a genuine search came back empty, and say so rather than presenting industry-level content as if it were company-specific.

## Step 5 — Identify the one primary outreach angle

Before generating any content, identify **one** primary angle with three parts:

- **Trigger** — what is happening at the company/prospect (from Step 4)
- **Pain Point** — the business or engineering challenge that plausibly results from the trigger
- **Zediant Relevance** — which Zediant capability, per the selected campaign, addresses it

Example: Trigger — the company is expanding its engineering team. Pain Point — the internal team may need additional engineering capacity to maintain delivery velocity while hiring continues. Zediant Relevance — C2, engineering pods.

**All content fields (Email Opening, Email Pain Points, LinkedIn Message, LinkedIn Follow-up) come from this one angle, for every qualified lead.** Don't create multiple unrelated angles for one company; the wording differs by channel, the underlying strategy doesn't.

**`Case_Study` and `Business_Challenges` extend the same angle rather than starting a new one.** Read top to bottom, the four Zoho fields should read as one line of reasoning, not four disconnected sentences that happen to sit in the same record: the company observation (Opening) implies a likely pressure (Pain Points), which is the kind of problem the selected case study speaks to (Case Study), whose client faced a specific version of it (Business_Challenges). When picking the case study in Step 7, prefer the one whose own business problem genuinely echoes this lead's Pain Point over one that merely shares an industry — that's what keeps the sequence coherent rather than four separate, independently-true facts bolted together.

## Step 6 — Match the confirmed challenge to a Zediant capability

Use `services.md`'s Business Problems Solved for the campaign's Recommended Services to find the specific capability that addresses the confirmed challenge from Step 5.

## Step 7 — Select the case study

Zoho field: `Case_Study`. Start from the selected campaign's Case study section in `context/playbooks/C{1-5}.md` (pre-selected from `campaigns.md`'s Related Case Studies shortlist), and let the confirmed Business Challenges from Step 5 drive the pick where more than one option exists, not shared industry alone — two companies in the same industry with different challenges should not automatically get the same case study.

Before using it, check: **Disclosure status** — `case_studies.md`'s actual, current framework is `ANONYMISED` (describe only by category, never name) or `NAMED` (safe to name — currently CS-04/11Wickets and CS-05/Diamond Professional Consultants only). Both still require the same `HUMAN APPROVAL REQUIRED` external-use gate, satisfied by the existing BDM `Lead_Status` approval — see `_core-reference.md`. (An older Tier 1/2/3 confidentiality scheme appears in historical material; `case_studies.md` explicitly marks that scheme `UNKNOWN`/not mapped for every entry — don't use it, use ANONYMISED/NAMED as documented above.) **The CS-02/CS-06 overlap** — same client, use one not both. **Concentration balance** — vary the proof point where context allows.

**This is the single most fabrication-prone field in the whole skill, so the rule is absolute: only select a case study that actually exists in approved Zediant content.** Never invent a customer name, a metric, a technology, or an outcome to make a case study "fit" better. **Before accepting a blank field, exhaust the research first** — re-check the campaign playbook's full case study section (not just the first candidate), re-read the confirmed Business Challenges finding for a less obvious angle of fit, and re-check `case_studies.md` directly if the playbook's set genuinely doesn't surface a fit. Only after that genuinely turns up nothing does `Case_Study` stay blank — and a blank field, reached that way, is still the correct, expected output (this is C1 and C5's normal state), not a gap to paper over with something plausible-sounding. Research harder, never fabricate to avoid a blank.

`Case_Study` is written verbatim by `crm-update` when populated. It is available to both Email and LinkedIn content where it genuinely fits the sequence — never force it into every touch just because a value exists.

Apply `zediant_outreach_natural_language_blacklist.md` (Step 0) while writing this sentence, same as the other three fields: keep it factual, plain, and specific to the case study client (never the words on the avoid list dressed up as a description of Zediant's work), target 15-25 words, and describe only what `case_studies.md` actually documents — never a result, challenge, technology, or scope that record doesn't state.

**Write it as one self-contained sentence that can stand entirely on its own.** Like `Business_Challenges`, this value is merged directly into live Apollo templates, not just stored in Zoho — in four of the five campaigns it lands as `{{Case Study}}` on its own line, immediately after an intro sentence like "We've worked with teams facing something similar before." A fragment or noun phrase reads as broken there. (One template slot, C5's final message, uses `{{Case Study}}` as a sentence subject instead — that's a known, accepted exception, not something to write around; don't compromise the other five slots to accommodate it.)

## Step 8 — Generate Apollo "Personalised Email" Body (Step 1 Email Body Only)

Apollo custom field: `Personalised Email` (id: `6aa79177f203040018e0af9d`), mirrored to Zoho field: `Email_Personalised_Opening`.

**The Architectural Purpose:** In Apollo, Google Antigravity crafts the **`Personalised Email` custom field as the complete, cohesive first-step email body** (approx. 50–90 words). The Apollo Step 1 sequence template permanently surrounds this field with the salutation and signature:

```text
Hi {{first_name}},

{{Personalised Email}}

Best,
Rajeev Jaiswal
Co-Founder | Zediant Technologies
```

> [!IMPORTANT]
> ### EMAIL BODY ONLY RULE (STRICTLY ENFORCED)
> The `Personalised Email` custom field MUST ONLY contain the **Email Body paragraphs**.
> - **DO NOT include greetings or salutations:** NEVER start with `Hi {{first_name}},`, `Hello John,`, `Hi Curtis,`, or `Dear [Name],`. The salutation is already rendered by the sequence template.
> - **DO NOT include sign-offs or signatures:** NEVER end with `Best,`, `Regards,`, `Cheers,`, `Rajeev Jaiswal`, or `Zediant Technologies`. The signature is already rendered by the sequence template.
> - Including greetings or signatures inside this field will cause duplicate salutations and duplicate sign-offs in prospect inboxes. Start immediately with Beat 1, and end with Beat 3.

**The 3-Beat Micro-Structure (Visual Spacing Standard):**
The `Personalised Email` custom field must ALWAYS be formatted into **3 distinct visual beats separated by double newlines (`\n\n`)**:

1. **Beat 1: The Product-Grounded Observation (Standalone paragraph, 1 sentence):**
   Opens directly with verified, domain-specific research naming the company's real core platform, product line, or technical function.
   * **Rule:** Must cite what the company actually builds (e.g., Open's embedded insurance platform, GTS Group's real-time industrial telemetry and OSIsoft PI/SCADA systems, Codafication's Crunchwork claims management platform).
   * **Banned:** Generic consulting fluff, "Noticed your ongoing platform expansion...", "Saw your company website...", or superficial flattery.
   * *Example (C1 - Fintech):* `Saw what you guys are building with Open's embedded insurance platform and how you're scaling instant policy integration for enterprise partners.`
   * *Example (C3 - Telemetry/IoT):* `Noticed GTS Group's real-time industrial data platforms and the scale of OSIsoft PI and SCADA integrations you manage across mining and energy assets.`

2. **Beat 2: The Operational Bottleneck & Senior Pod Solution (1–2 sentences):**
   Transitions smoothly to the engineering tension between rapid feature release cycles and senior capacity / maintenance drag, introducing Zediant's senior engineering pod capability.
   * **Rule:** Must specify the operational friction (e.g., pulling senior engineers into maintenance, deployment pipeline drag, integration backlog) and present Zediant's pods embedding in 2–3 weeks to take full architectural ownership, shipping 30–40% faster using modern tooling / AI-assisted workflows without disrupting active sprints.
   * *Example (C1):* `Rolling out partner APIs while keeping the core rating engine fast usually pulls senior engineers in two directions. We embed senior squads in 2-3 weeks to take complete architectural ownership of feature modules, using modern tooling to ship about 35% faster.`
   * *Example (C3):* `Balancing high-throughput telemetry data with rock-solid cloud platform uptime often stretches senior infrastructure engineers thin. We embed senior platform and DevOps squads to optimize cloud performance and automate CI/CD pipelines without disrupting live client environments.`

3. **Beat 3: The Standalone 2-Minute Teardown Ask (Standalone paragraph, 1 sentence):**
   Closes with a single permission-based question standing on its own line for maximum visual contrast.
   * **Rule:** Low-friction curiosity offer (the 2-minute teardown or benchmark). Never push a 30-minute meeting or Calendly link in the body.
   * *Example (C1):* `Open to checking a 2-minute teardown of how we helped a similar fintech product team accelerate release cycles by 35%?`
   * *Example (C3):* `Open to checking a 2-minute teardown of how we helped a high-throughput platform team eliminate release friction and optimize cloud spend?`

---

## Step 9 — Generate Apollo "Pain Point" Custom Field (Step 3 Merge Tag Standard)

Apollo custom field: `Pain Point` (id: `6aa790fa8c717000101fa55c`).

**The Architectural Purpose:** In the Apollo sequence cadence, Step 3 (Touch 3 - Follow-up Email) begins with this exact sentence:
```text
Hi {{first_name}},

Following up on my note around {{Pain Point}}.
```

> [!IMPORTANT]
> ### PAIN POINT SYNTAX & GRAMMAR RULES (CRITICAL FOR LIVE MERGES)
> Because `{{Pain Point}}` is injected directly after `"Following up on my note around "`, it MUST be formatted as a **lowercase gerund or noun phrase (6–15 words)** that completes the sentence with complete grammatical fluidity.
> 
> 1. **Must start with a lowercase letter** (unless the first word is an acronym or proper noun like AWS, Kubernetes, or API).
>    * *Good:* `senior engineering capacity bottlenecks while scaling...`
>    * *Bad:* `Senior engineering capacity bottlenecks...` (Capital letter looks like an automated template merge).
> 2. **NO trailing period or punctuation:**
>    * *Good:* `platform latency bottlenecks across high-volume telemetry feeds`
>    * *Bad:* `platform latency bottlenecks across high-volume telemetry feeds.` (Double period at end of sentence: `...telemetry feeds..`).
> 3. **NO duplicate prepositions:**
>    * Never start with `"around"`, `"regarding"`, `"about"`, or `"with"`.
>    * *Bad:* `around infrastructure throughput constraints` -> Merges to: *"Following up on my note around around infrastructure throughput constraints."*
> 4. **Self-contained noun/gerund phrase (NOT a full sentence):**
>    * *Good:* `senior developer hiring delays and sprint delivery bottlenecks`
>    * *Bad:* `We noticed that your team is having hiring delays` (Breaks sentence grammar completely).

### Approved `Pain Point` Models Across C1–C5:
* **C1 (AI-Enabled Product Engineering):**
  * `senior engineering capacity bottlenecks while scaling embedded insurance API workflows`
  * `delivery velocity constraints and senior engineering bandwidth on your product roadmap`
  * `senior fullstack capacity constraints while rolling out new core product modules`
* **C2 (Engineering Pods & Staff Augmentation):**
  * `senior developer hiring delays and sprint delivery bottlenecks`
  * `senior backend engineering capacity bottlenecks on your active client sprints`
  * `engineering headcount constraints and slow contractor ramp-up times`
* **C3 (Platform Engineering & Cloud Modernization):**
  * `infrastructure throughput constraints and platform latency bottlenecks across high-volume telemetry feeds`
  * `deployment pipeline friction and unoptimized cloud infrastructure spend`
  * `Kubernetes scaling bottlenecks and release friction pulling developers from product work`
* **C4 (Middleware & API Integration):**
  * `fragile point-to-point API glue code and sync failures across enterprise systems`
  * `manual data reconciliation delays and third-party API rate limit bottlenecks`
  * `middleware integration bottlenecks connecting CRM, ERP, and legacy databases`
* **C5 (Enterprise Custom Development & Modernization):**
  * `legacy monolithic refactoring risks and feature release slowdowns`
  * `technical debt in core architectures stalling new feature rollouts`
  * `monolith decoupling complexities while maintaining uninterrupted business operations`

*(Note: In Zoho CRM, `Email_Pain_Points` and `Business_Challenges` are also preserved upon response sync).*

Requirements: 1-2 sentences, approximately 15-25 words, must logically follow the Opening (don't repeat it), focus on the business/engineering challenge, no unsupported claims, no exaggeration, don't mention Zediant unless the live Apollo template specifically requires it. **No AI-typical special characters.**

Use language like "can create," "may put pressure on," "often creates," "can become challenging." Potential pain areas: engineering capacity, product delivery velocity, hiring and onboarding experienced engineers, scaling development teams, product roadmap execution, integration complexity, legacy modernization, technical delivery bandwidth, maintaining development velocity during growth.

Apply `zediant_outreach_natural_language_blacklist.md` (Step 0) while drafting: tie the pressure to roadmap pressure, engineering capacity, hiring, product complexity, delivery workload, or maintaining existing systems while building new functionality, per that file's Rules for the Four Zoho Fields, and use cautious, hedged language ("can," "may," "often") when the pressure is inferred rather than confirmed — never a stacked buzzword sentence from its Corporate/Marketing avoid list.

**Same second-person rule as Step 8 applies here whenever this field addresses the recipient directly** — don't drift into "Jason's team may find..." after Step 8 correctly used "your team." Keep person consistent across both fields.

**Final human-writing test — run this on Opening, Pain Points, Case Study, and Business_Challenges before moving on:** *"Would this sentence sound normal if a Zediant salesperson personally typed this email to one CTO or VP Engineering?"* If the answer is no, rewrite it before proceeding — don't accept a field merely because it's grammatically correct or technically blacklist-clean. This is `zediant_outreach_natural_language_blacklist.md`'s own closing test, restated here because it's the test that actually catches what a mechanical word-swap misses: naturalness and relevance matter more than sophisticated wording.

**Must be self-contained — no backward reference to the Opening.** This is not optional stylistic advice, it's a template-compatibility requirement: every live Apollo sequence reuses `Email_Pain_Points` a second time, days later, in a separate follow-up email that does **not** include `Email_Personalised_Opening` — it appears alone after a lead-in like "Following up on something from my last note - {{Email Pain Points}}" or "Coming back to something from my last note — {{Email Pain Points}}". A sentence like "Moving into new verticals **like that** can put pressure on..." reads fine in Step 1, next to the Opening it's pointing back to, but dangles when it resurfaces alone in the follow-up. Avoid demonstrative pronouns ("that," "this," "such a shift") whose antecedent lives only in the Opening — restate the specific trigger detail in a few words instead of gesturing back at it. The sentence has to make complete sense to someone who never saw the Opening at all.

## Step 10 — LinkedIn Selection (batch-level priority ranking — see Section 4 for full detail)

Evaluate this company against the rest of the current batch on the Buying Signal factor (normally the numeric Initial Buying Signal Score pre-engagement, or the numeric Post-Engagement PTB Score once genuine engagement exists), ICP fit, buying intent, prospect seniority, LinkedIn profile availability and relevance, and quality of personalization opportunity. Set `LinkedIn Status = Ready to Connect` only for approximately the approximately the top quarter of the qualified batch, on quality — not by taking the first 25 or by LinkedIn-profile-presence alone. Otherwise, `LinkedIn Status = Not Required`. Full criteria in Section 4.

**This decision no longer controls whether LinkedIn content gets generated (see Step 11) — it controls priority and sequencing only.** `Ready to Connect` tells the BDM and the manual LinkedIn process "work this one now." `Not Required` means "not in this batch's active LinkedIn push," not "no LinkedIn content exists for this lead."

## Step 11 — Generate LinkedIn Connection Request and Follow-up (for every qualified lead, regardless of LinkedIn Status)

Zoho field: `LinkedIn_Message` — relabeled **LinkedIn Message & Follow-up** in Zoho, and now holds both pieces of content in one field, not two. Generate both messages here **for every qualified lead that reached this step**, using the same underlying research already done for the Email channel — this is not a separate research pass, it's the same evidence expressed in LinkedIn's tone and format, governed by the verified-signal framework immediately below. Then write them into the field using the fixed two-part format `crm-update` expects:

```
CONNECT:
[the connection request note]

FOLLOW-UP:
[the follow-up message]
```

Only the actual message text belongs in either half of the field — no research notes, no evidence explanations, no scoring commentary, and no internal reasoning about why a signal was or wasn't found. A note about missing evidence belongs in `Data Gaps` at the end of the output, never inside `LinkedIn_Message` itself.

### The verified-signal framework — authoritative, governs both CONNECT and FOLLOW-UP

Every CONNECT and FOLLOW-UP message is built on one of three states. There is no other option, and no message may blend them:

- **State A** — a strong recent verified signal exists → **Path 1** below.
- **State B** — no recent signal, but verified person/company context provides a genuine reason to connect → **Path 2** below.
- **State C** — neither a meaningful recent signal nor sufficiently specific, verified person/company context exists → do not manufacture personalization. Use the most factual, restrained connection note the evidence actually supports, and flag the lead in `Data Gaps` for insufficient LinkedIn personalization evidence rather than inventing a reason or silently shipping a generic message. This is a rare, expected outcome for a genuinely evidence-thin lead, not a defect to paper over.

**Path 1 — VERIFIED SIGNAL → SPECIFIC OBSERVATION → GENUINE REASON → SIMPLE CONNECTION.** Use this path only when a genuine, verifiable personalization signal exists for this specific person or company — something actually found and traceable to a source, not a plausible guess. In priority order, a verifiable signal is one of:

1. A recent LinkedIn post written by the person
2. Recent LinkedIn activity or a comment by the person
3. A recent company announcement
4. A product launch or update
5. A new technology or product direction
6. Hiring activity that reveals a meaningful direction (not hiring in general)
7. Market or geography expansion
8. A funding or investment announcement
9. An acquisition or partnership announcement
10. An interview, podcast, webinar, or speaking appearance
11. An article published by, or featuring, the person or company
12. A clearly identifiable professional responsibility — what this person's role actually owns
13. A specific product or platform area the person owns or leads
14. Other recent, verifiable professional information about the person or company

When a signal exists, build the message in this order: the specific observation (what was actually found, described concretely, not vaguely), the genuine reason it's worth connecting over (why a real professional would notice and care), and a simple, low-key connection request — nothing beyond those three parts.

**Path 2 — NO VERIFIED RECENT SIGNAL → VERIFIED PERSON/COMPANY CONTEXT → HONEST REASON FOR INTEREST → SIMPLE CONNECTION.** Use this path when nothing from the 14-item signal list above can be verified for this person or company. **A missing recent signal does not collapse to a generic industry message.** The fallback must still be built on something genuinely known and verified about *this specific* person or company. Acceptable fallback evidence includes: the person's actual professional responsibility, the person's role in the company, the company's actual product, the company's actual platform, the company's actual business model, a clearly documented technology or product area, a specific market the company actually operates in, a clearly verified company initiative, or another factual professional/company characteristic that makes the connection reasonable. **Honest and simple is always better than fake personalization** — but honest and simple still means specific to this person or company, never specific to their industry alone. Do not write "I noticed" or "I saw" unless the observation behind it was actually verified.

*Fallback example (verified company/product context, no recent signal):* "Hi Mohammad, came across Connexion Mobility while looking into connected mobility platforms. I had a look at the telematics side of what you're building and found it interesting. Would be good to connect." — references the actual company and a specific, verified product area, not just the industry.

**Hard rule — no generic industry-only fallback.** A fallback built only on shared industry or role category, with no specific verified person or company fact attached, is prohibited, not merely discouraged. Never generate a fallback using only language like "people building in the mobility space," "professionals in the SaaS space," "people working in technology," "leaders in the software industry," "people in the connected mobility space," "others working in fintech," "professionals in this industry," "people building interesting products," or a close variant. Industry context may appear only alongside a specific, verified person/company fact — never on its own.

*Bad:* "Hi Mohammad, always good to connect with people building in the mobility/telematics space. Look forward to staying in touch." — this could be sent to almost anyone in the industry; nothing in it is specific to Mohammad or Connexion Mobility, so it fails Path 2 even though nothing in it is technically false.

**Before generating a fallback message, answer internally: "Why would Rajeev genuinely want to connect with this particular person?"** The answer must come from verified information. "Because he works in the same industry" is insufficient on its own. "Because he leads the telematics platform at Connexion Mobility, and Rajeev has a genuine professional interest in how connected mobility platforms are being built" is sufficient. This internal reasoning is never written into `LinkedIn_Message` itself — only the final message text is stored (see the field-hygiene rule above). Also do not confuse personalization with merely inserting the person's name and company name: "Hi Mohammad, came across Connexion Mobility. Would be good to connect." is not sufficiently personalized on its own, and neither is "Hi Mohammad, your work at Connexion Mobility caught my attention" unless the message also identifies what about that work actually caught it.

**Hard rule — never fabricate personalization from an unverified assumption.** Do not infer interest merely from industry membership. Do not infer a technology change, an expansion, a hiring push, a post, a launch, or a business challenge unless it was actually verified against the list above. If it wasn't found, it does not go in the message — use Path 2's verified person/company context instead, or State C when even that isn't available. Never a bare industry statement standing in for either.

**Personalization depth restraint — one observation only, never a research summary.** Use exactly one observation per message, even when more than one verified signal exists. Never combine multiple signals into something that reads like a research summary — no stacking several facts, no citing multiple posts, no describing a detailed technology stack, no reciting funding history, no citing employee growth figures, no long company description. A message that reads like a dossier fails this restraint regardless of how accurate every individual fact in it is.

### CONNECT — the connection-request note, sent before acceptance

Because it's a note between two people, not a message, it must read as short and natural, never as outreach:

- No mention of Zediant, anywhere — not the company name, not "we," not a service, not a category of work
- No pitch of any kind — nothing describing software development, engineering, staff augmentation, AI work, or integration work, and nothing else Zediant does or could do
- No CTA of any kind
- No meeting or call request, and no mention of Calendly or any scheduling link
- No asking about business requirements, pain points, or whether the prospect is hiring developers
- No "explore synergies," "explore opportunities," "potential collaboration," "I believe there could be opportunities," "I'd love to explore synergies," generic praise, exaggerated compliments, or corporate-networking language
- Grounded in Path 1's observation when a verified signal exists, Path 2's verified person/company-specific fallback when it doesn't, or State C's restrained note when neither is available — never a blend, and never a bare industry statement standing in for personalization
- Must not copy the email Opening or Pain Points, though it may draw on the same underlying Trigger when one is verified
- **Target 20-45 words, 55 words absolute maximum.** Shorter and more natural is always preferable to longer; if a draft lands at or near 55 words, cut content rather than trim punctuation to fit

### FOLLOW-UP — the first real message, sent after the connection is accepted

Relationship warming, not a second sales touch. It may carry soft, non-promotional context about what Zediant does, but the same hard prohibitions apply beyond that narrow allowance:

- Must never ask for a meeting or a call, and must never mention Calendly or any scheduling link
- Must never pitch a Zediant service directly or use a sales CTA of any kind
- Must never ask about development needs, hiring plans, or technical requirements
- Must never use "explore synergies," "potential collaboration," or any phrase from the banned list below
- Should, where possible, connect back to the same observation used in CONNECT rather than introducing an unrelated one — a coherent thread across both messages reads as one person following up, not a second, disconnected sequence step
- Must be based on verified information, never an invented conversational continuation (e.g. implying an exchange or a shared context that didn't actually happen)
- Must add a new point, insight, or angle beyond the connection note — not copy the connect note or the email. Must NOT say "just following up," "checking if you saw my message," or "wanted to follow up"
- 40-70 words maximum

### Banned phrases — LinkedIn CONNECT and FOLLOW-UP specifically

Distinct from the analytical/AI-summary phrase list in Writing Style below, which applies to all content fields. These are relationship-cliché and sales-cliché phrases specific to LinkedIn outreach — never use any of them, or a close variant, in CONNECT or FOLLOW-UP: "I came across your impressive profile," "your impressive background," "your impressive journey," "I'd love to explore synergies," "I believe there could be opportunities," "potential synergies," "potential collaboration," "mutually beneficial," "leverage our expertise," "explore how we can," "I'd love to learn more about your business," "would love to discuss," "would love to schedule," "connect and explore," "see how we can help," "help you scale," "support your growth," "drive innovation," "transform your business."

Generic openers — "Hope you're doing well," "Hope all is well," "Great to connect," "Happy to connect," "Nice to meet you" — are also banned unless the specific context of a genuine follow-up genuinely calls for one; don't default to them as a safe opening line.

### Rajeev's voice

Every CONNECT and FOLLOW-UP message should read as if a specific person, Rajeev Jaiswal, personally wrote it: professional, curious, calm, genuine, concise, observant, conversational. Not promotional, not corporate, not scripted, not AI-generated, not sales-oriented. If a draft could have been generated by any SDR tool for any prospect in the same industry, it hasn't found Rajeev's voice yet — rewrite it. **No AI-typical language** — no overly polished corporate prose, no unnecessary adjectives, no long explanations, no structured sales language, no artificial enthusiasm, no analytical description of the prospect (see the banned analytical-phrase list in Writing Style below, which applies here too). **No em dash, en dash, or double hyphen** in either message, same as every other content field.

### The 12-point LinkedIn Quality Test

Before accepting any CONNECT or FOLLOW-UP message, confirm all twelve:

1. Is the reason for connecting genuinely verifiable, not assumed?
2. Is the observation traceable to something actually found, not inferred?
3. Does it sound like one person writing to another, not a company writing to a lead?
4. Does it avoid any feeling of sales outreach?
5. Does CONNECT avoid any mention of Zediant?
6. Does it avoid any meeting or call request?
7. Is it concise — well within the word limits above?
8. Is it free of generic praise or exaggerated compliments?
9. Is it free of AI-style or corporate language?
10. Would Rajeev genuinely send this message manually, as himself?
11. If the personalization observation were removed, would the remaining sentence still be honest — i.e., it doesn't lean on the observation to disguise something false?
12. If no strong signal existed, did the message correctly use the honest fallback (Path 2) instead of stretching or inventing one?

If any answer is no, rewrite before returning output. This test runs in addition to, not instead of, the existing LinkedIn Personalization Quality Test below.

### Fallback-specific checks — required whenever Path 2 or State C is used

In addition to the 12-point test above, confirm all seven:

1. Does the message contain a specific, verified person or company context, not just industry?
2. If a recent signal is claimed, can it be directly, specifically verified?
3. If no recent signal exists, does the fallback still contain a factual reason specific to this person or company?
4. Could this exact message be sent to 100 unrelated people in the same industry without changing the wording? If yes, fail it.
5. Does the message answer, implicitly or explicitly, why Rajeev is interested in connecting with this particular person? If no, fail it.
6. Is the message based on verified facts rather than assumptions? If no, fail it.
7. Is the message honest enough that Rajeev could personally stand behind every sentence? If no, fail it.

If any of these seven fail, do not ship the message — rebuild it from genuinely verified person/company context, or fall back to State C's restrained, `Data Gaps`-flagged note rather than a generic industry statement.

**The LinkedIn Personalization Quality Test: would a reader who received this — either message — recognize it as a genuine, individual attempt to connect with them personally, or would it read as an SDR sequence?** If it reads like a sequence step, rewrite it. This applies to both CONNECT and FOLLOW-UP, but CONNECT is held to the stricter bar since it can contain literally none of the outreach machinery (no company name, no pitch, no CTA) that FOLLOW-UP is cautiously allowed a narrow amount of.

**No em dash, en dash, double hyphen, or other AI-typical special characters in either half**, no banned analytical/AI-summary phrasing, no use of "AI" as a framing device (see Writing Style above) — and the `CONNECT:`/`FOLLOW-UP:` labels plus the blank line between them are the only structural formatting allowed — no bullets, no decorative separators.

**On the rare occasion the batch is so large that generating LinkedIn content for every single lead is genuinely impractical in one pass**, prioritize generation by whichever Buying Signal factor exists for the batch (Initial Buying Signal Score or Post-Engagement PTB Score, highest first) and say explicitly which leads' LinkedIn content is still outstanding — don't silently skip the bottom of the batch and let it look like every lead was covered.

## Step 13 — Assemble the output

Assemble the Output Format below. Every field should be traceable: a human reading it should be able to find where the fact came from.

---

# THE ONE PRIMARY ANGLE — cross-channel consistency

All content fields for one company represent one coherent outreach strategy, expressed differently per channel:

```
Trigger: ABC is expanding its engineering organization.

Email Personalised Opening:
"I noticed ABC has been expanding its engineering team while continuing to build out its SaaS platform."

Email Pain Points:
"That kind of growth can put pressure on delivery capacity, particularly when the product roadmap expands faster than the team can hire and onboard experienced engineers."

LinkedIn Message & Follow-up (one field, two-part format — Path 1, verified signal is a recent company hiring post, signal #6):
CONNECT:
"Hi John, saw ABC's recent post about the new engineering hires for the platform team. Good to see the growth. Would be great to connect."

FOLLOW-UP:
"Thanks for connecting. That hiring push into the platform team says a lot about where ABC's headed. We work alongside engineering teams going through similar growth, mostly on the product delivery side. Be curious to hear how the roadmap's shaping up as the team scales."
```

Wording differs across channels; the underlying strategy does not. Note that CONNECT contains no mention of Zediant, no pitch, and no CTA — it is a genuine one-to-one note, not outreach, and it uses exactly one observation rather than a research summary. FOLLOW-UP carries the soft context CONNECT deliberately withholds, still stops short of a meeting ask or sales CTA, and connects back to the same observation CONNECT used. When no verified signal exists for a lead, see Step 11's Path 2 for the honest-fallback equivalent of both messages.

---

# SECTION 4 — LINKEDIN SELECTION STRATEGY

**LinkedIn Status is a priority flag, not a content gate.** As of v2.3, every qualified lead gets LinkedIn Message & Follow-up content generated (Step 11). This section decides which approximately the top quarter of the written batch leads are flagged `Ready to Connect` — meaning "the BDM/manual LinkedIn process should actively work this lead now" — versus `Not Required` — meaning "content exists and is ready if needed, but this lead isn't in the current active push." LinkedIn execution effort is still the scarce resource being rationed here; content generation is not.

For every batch of qualified leads: evaluate all of them, review the Buying Signal factor (Initial Buying Signal Score, Post-Engagement PTB Score, or true N/A — whichever applies to that lead), review ICP fit, review buying intent, review prospect seniority, review LinkedIn profile availability and relevance, review quality of personalization opportunity, rank by LinkedIn priority, then select approximately the top quarter of the strongest leads as `Ready to Connect`.

**The normal case for a batch from Scheduler 1 is a numeric Initial Buying Signal Score for every lead** — use it as a genuine ranking input, the same way a Post-Engagement PTB Score would be used for a post-engagement lead. Do not treat the Initial Buying Signal Score as equivalent to, or a proxy for, the Post-Engagement PTB Score — they are different measurements of different evidence and should be read as what they actually are.

**When the true `N/A / Not Yet Scored` state applies to a lead in the batch (now a rare case):** do not treat `N/A` as `0`, do not treat it as Cold, do not penalize the lead for lacking a score, and do not invent or estimate one to fill the gap. Simply rank that lead on the remaining criteria — ICP fit, buying/intent evidence already verified during qualification, prospect seniority/relevance, LinkedIn profile availability and relevance, and quality of personalization opportunity — with the Buying Signal factor contributing no numeric signal to the ranking. This is not a new scoring formula or a replacement weighting scheme; it's the existing criteria list minus the one input that isn't available yet. A lead can rank `Ready to Connect` on this reduced evidence alone if the rest of it is strong.

**Quality over hitting exactly 25.** If only 18 leads are genuinely strong enough for the active push, mark 18 as `Ready to Connect`. If more than a quarter are strong, still mark approximately the top quarter — don't force the number in either direction. Every lead outside that slice still gets its LinkedIn content generated and stored; it simply isn't flagged for the current active push.

## LinkedIn Status = Ready to Connect

Set when the lead has a strong combination of: a high Buying Signal factor score **when a numeric one exists** (Initial Buying Signal Score or Post-Engagement PTB Score, whichever applies — see the true-N/A handling above when neither does), strong ICP fit, strong or credible buying/intent signal, senior or decision-making role, strong relevance to the selected campaign, a relevant LinkedIn profile, strong personalization opportunity, and a business/engineering problem Zediant can credibly address. Typical high-priority roles: CTO, CIO, VP Engineering, VP Technology, Head of Engineering, Head of Product, Engineering Director, and other senior decision-makers directly relevant to the campaign — but don't restrict selection to title alone; overall lead quality matters more.

## LinkedIn Status = Not Required

Set when: the Buying Signal factor exists but isn't sufficiently high, ICP fit is moderate or weak, intent is weak or unclear, prospect seniority/relevance is insufficient, LinkedIn profile is unavailable or unsuitable, personalization opportunity is weak, the prospect isn't among the highest-priority leads in the current batch, or email alone is judged sufficient for now. **True `N/A / Not Yet Scored` is not by itself a reason to set `Not Required`** — a lead with no score yet is ranked on the remaining criteria and can still be `Ready to Connect` if they're strong. **Email = active, LinkedIn = not in this batch's active push is an expected, normal outcome** — it is not a downgrade, and it does not mean the LinkedIn content is missing.

## Status values at this stage — exactly two, never more

At the lead-generation stage, this skill decides only between `Ready to Connect` and `Not Required`. Never set an execution status (`Connection Sent`, `Connected`, `Message Sent`, `Follow-up Due`, `Follow-up Sent`, `Response Received`, or similar) — those belong to the later manual LinkedIn execution process a human runs, and are written directly in Zoho by that person, not by this skill or `crm-update`.

## Generation — unconditional as of v2.3

For all qualified leads: generate `Email_Personalised_Opening`, `Email_Pain_Points`, **and** the merged `LinkedIn_Message` content (the connection request note plus the follow-up message, in the two-part format), regardless of the `LinkedIn Status` value. `LinkedIn Status` still controls priority/sequencing for the manual outreach process, and it's still a real, meaningful decision — it just no longer withholds content. On an update to an existing record, don't overwrite valid LinkedIn content already sitting there from a prior cycle with a lower-effort regeneration; regenerate fully or leave it as-is.

---

# APOLLO SEQUENCE TEMPLATE COMPATIBILITY

The live Apollo templates control the overall email structure, and they are the real, binding spec for how every field this skill produces actually gets read — checked directly against all five campaigns' live templates on August 11, 2026, not assumed from the field names.

**Four fields this skill touches or feeds end up merged into live templates, not just stored in Zoho:** `Email_Personalised_Opening`, `Email_Pain_Points`, `Business_Challenges` (Apollo label: `Business Challenge`, singular — a naming mismatch to be aware of, not a different field), and `Case_Study` (Apollo label: `Case Study`). All four need the same "reads like something a person typed" bar — a fabricated or awkward Business Challenges or Case Study value is just as visible to the prospect as a bad Opening.

The first email in every sequence looks roughly like this:

```
Hi {{First Name}},

{{Email Personalised Opening}}

{{Email Pain Points}}

[Existing Zediant campaign messaging]
[Existing CTA]
[Existing signature]
```

**Because this template greets the recipient by name immediately before `{{Email Personalised Opening}}`, every field that follows it inherits the "talking to you" frame the greeting sets — see the second-person requirement in Step 8.** A field that switches to third person about the same person the greeting just addressed is the specific defect that requirement exists to prevent, and it's only visible when the field is read inside this exact template structure, not in isolation.

But `Email_Pain_Points` and `Case_Study`/`Business_Challenges` don't stop there — every campaign reuses `Email_Pain_Points` a second time in a later follow-up, and `Business_Challenges`/`Case_Study` appear in a dedicated proof-point email, in the grammatical forms documented in Steps 7 and 9 above. This skill's output for all four fields never includes: the greeting line, a subject line, a signature, a sign-off, a full email, a duplicate CTA, a duplicate Zediant introduction, or additional paragraphs that belong to the Apollo template. Each field is an independent, self-contained content block that has to make sense wherever the live template drops it in — including the second, later placement, without the other fields present alongside it.

---

# WRITING STYLE — write like a human, not like an AI

Every generated field (Opening, Pain Points, the connection request, the follow-up message, and Business Challenges/Case Study when this skill touches them) must read as **literal, ready-to-send email or LinkedIn text**, not a summary of research about the prospect. The test for every one of these fields: **could a BDM copy this exact text into a real email or LinkedIn message and send it, without rewriting it first?** If the answer is no — if it reads like a note explaining what was found rather than a message written to the prospect — rewrite it before returning output. This is the **Email Quality Test**, checked at Validation.

**Banned analytical/AI-summary phrasing — never use, in any content field:** "The company appears to...", "The prospect likely...", "This indicates...", "Based on available signals...", "It seems that...", "They may be facing...", and any close variant of these. These phrases describe the prospect to a third party; they don't talk to the prospect, and a BDM would have to rewrite around them before sending. Say the thing directly and personally instead — e.g. not "The company appears to be expanding its engineering team" but "I noticed your engineering team has been growing."

**Never use "AI" as a personalization or outreach framing device** — do not write copy that pitches, references, or leans on AI as part of the outreach angle itself (e.g. "as an AI-driven analysis of your company shows," "I used AI to look into your company," "this AI-generated note"). The one narrow exception: a factual mention of AI as the **prospect's own** product, technology, or business (e.g. "your team's AI-powered platform") is fine — that's a fact about them, not a framing device for how the outreach was produced.

**No em dash, en dash, or double hyphen (`--`) anywhere in a content field.** Concretely: no em dashes, no en dashes used as a substitute for a comma or period, no double hyphens used as a dash substitute, no other AI-typical punctuation tics. Use plain commas, periods, and ordinary sentence structure instead. This is a hard requirement checked at Validation and again by `crm-update` before the write — if a generated field contains one, rewrite it rather than leaving it for the next skill to catch.

---

# PERSONALIZATION RULES

| Rule | What it actually prevents |
|---|---|
| **Never fabricate a fact.** | Don't invent a funding round, a headcount, a product launch, or a quote that wasn't actually found. If a search came back empty, say so rather than writing something plausible-sounding |
| **Never pretend to know internal company information.** | Frame observations as external inference ("your careers page shows...") not internal knowledge |
| **Never over-personalize.** | Professional and company-level detail is fair game. Personal-life detail reads as invasive and measurably hurts reply rates |
| **Never mention information that cannot be verified.** | Either verify it before using it or note the uncertainty rather than stating it as fact |
| **Never cite a statistic from the "Unsubstantiated performance claims" table in `services.md`.** | Those numbers aren't backed by evidence Zediant can defend if a prospect asks |
| **Never refer to the recipient in third person by their own first name in a field that follows the `Hi {{First Name}},` greeting.** | The recipient reads as being talked about rather than talked to — the exact bug this version was created to fix (see Step 8) |
| **Never use banned analytical/AI-summary phrasing** ("The company appears to...", "The prospect likely...", "This indicates...", "Based on available signals...", "It seems that...", "They may be facing...", or a close variant). | These describe the prospect to a third party instead of writing to them — the field fails the Email Quality Test and a BDM has to rewrite it before sending |
| **Never use "AI" as a personalization/outreach framing device** (narrow exception: a factual mention of AI as the prospect's own product/technology is fine). | Referencing AI as part of how the outreach was produced reads as generated, not personal, and undermines the "written by a person, for this person" quality the whole skill exists to produce |

---

# VALIDATION

Before returning output, confirm:

- **`zediant_outreach_natural_language_blacklist.md` was read before drafting (Step 0), not consulted only as an after-the-fact check** — Opening, Pain Points, Case Study, and Business_Challenges (where this skill touches its wording) contain no phrase from that file's Complete Avoid List, unless the phrase is genuinely necessary to state a verified fact accurately, in which case the sentence is rewritten around it rather than the fact being dropped or distorted
- Opening, Pain Points, and Case Study each land at approximately 15-25 words, per the blacklist file's own Final Quality Check — not the previous 25-45 word range
- Each of the four fields reads naturally aloud, avoids unnecessary repetition of another field, fits the exact live-template slot it's inserted into (see Apollo Template Compatibility), and avoids unsupported claims and promotional or sales-heavy language
- The four fields read as one connected line of reasoning — company observation → likely pressure → relevant case study → that case study's own challenge — not four independently-true sentences with no thread between them (see Step 5)
- **Every field passes the final human-writing test** (Step 9): would this sound normal if a Zediant salesperson personally typed it to one CTO or VP Engineering? If not, it was rewritten, not shipped as-is because it was grammatically correct
- **None of the four fields is blank without having exhausted research first.** A blank `Case_Study` (the only one of the four that can legitimately end up blank) only happens after checking the full campaign shortlist and re-reading `case_studies.md`, per Step 7 — never accepted as a first-pass shortcut, and never filled with an invented case study just to avoid the blank. `Business_Challenges`, `Email_Personalised_Opening`, and `Email_Pain_Points` are not optional — if a genuinely confident version of one of these three can't be produced, that's a signal to research the company further, not a reason to guess
- Every fact in the Opening and Pain Points is traceable to something actually found, not inferred from industry stereotype
- The Relevant Service genuinely addresses the confirmed Business Challenge, per `services.md`
- The Case Study respects its confidentiality tier and doesn't repeat the CS-02/CS-06 double-count
- No statistic from `services.md`'s Unsubstantiated performance claims table appears anywhere in the output
- Opening, Pain Points, and both halves of the LinkedIn Message & Follow-up field contain **no em dash, en dash, double hyphen (`--`), or other AI-typical special character**
- No banned analytical/AI-summary phrasing appears in any content field ("The company appears to...", "The prospect likely...", "This indicates...", "Based on available signals...", "It seems that...", "They may be facing...", or a close variant)
- "AI" is not used anywhere as a personalization/outreach framing device (a factual mention of AI as the prospect's own product/technology is the only exception)
- **Email Quality Test: could a BDM copy each content field's exact text into a real email or LinkedIn message and send it, without rewriting it first?** If not, rewrite before returning output
- Opening and Pain Points meet their word-count ranges (approximately 15-25 words each, per `zediant_outreach_natural_language_blacklist.md`); CONNECT meets its word-count range (target 20-45 words, 55 words absolute maximum — see Step 11); the follow-up is 40-70 words
- **CONNECT and FOLLOW-UP each follow one of Step 11's three states — Path 1 (verified signal → specific observation → genuine reason → simple connection), Path 2 (no verified signal → verified person/company context → honest reason → simple connection), or State C (neither exists → restrained note + `Data Gaps` flag) — and never blend states or fabricate one when another genuinely applies**
- **Path 2 fallbacks are grounded in a specific, verified person/company fact — never a bare industry-only statement** (see Step 11's generic-fallback prohibition and its bad/better examples); a fallback passes only if it also clears the seven fallback-specific checks in Step 11
- Each message uses exactly one observation, not multiple signals stacked into a research-summary feel (no multiple facts, posts, tech-stack detail, funding history, employee-growth figures, or long company description)
- No phrase from Step 11's LinkedIn-specific banned-phrase list (or generic opener list) appears in CONNECT or FOLLOW-UP
- CONNECT and FOLLOW-UP both pass the 12-point LinkedIn Quality Test in Step 11, in addition to the LinkedIn Personalization Quality Test below
- **Read the Opening and Pain Points as if pasted directly into the live template right after `Hi {{First Name}},` — confirm neither one drifts into third person about the same recipient the greeting just addressed** (e.g., "Jason's team," "under Mahesh's leadership"). Second person ("your team," "you're") is correct; third person about the company itself is fine; third person about the recipient is the defect
- The CONNECT note does not copy the email or the Opening; the FOLLOW-UP does not copy the CONNECT note or the email
- **The CONNECT note contains no mention of Zediant, no pitch, no CTA, and no meeting/call request** — it is a genuine, short, one-to-one connection note, not outreach
- **The FOLLOW-UP does not pitch, ask for a meeting/call, or use a sales CTA** — soft non-promotional context about Zediant is the most it carries
- Both CONNECT and FOLLOW-UP pass the LinkedIn Personalization Quality Test — they read as a genuine attempt to connect personally, not an SDR sequence
- The follow-up does not use "just following up" or equivalent
- The merged LinkedIn field uses the CONNECT / FOLLOW-UP two-part format, nothing else
- `LinkedIn Status` reflects a genuine batch-level priority ranking, not "has a LinkedIn URL" or first-25 selection
- **The merged LinkedIn field was generated for every qualified lead in the batch, independent of `LinkedIn Status`** — a `Not Required` lead with a blank `LinkedIn_Message` field is a defect, not an expected outcome, as of v2.3
- `Case_Study` is either an approved, real case study or blank — never fabricated
- All content fields trace back to the same single Trigger → Pain Point → Zediant Relevance angle, and to the same `Business_Challenges` value where relevant
- `Email_Pain_Points` makes complete sense read in isolation, with no demonstrative pronoun ("that," "this," "such a shift") whose antecedent only exists in `Email_Personalised_Opening` — it gets reused alone in a later follow-up email
- `Case_Study` (where populated) is one self-contained, standalone sentence, not a noun phrase or fragment — it merges directly into a live Apollo template as its own line in four of five campaigns

---

# OUTPUT FORMAT

```
## Company Summary
[2-3 sentences: what this company does, size, market]

## Recipient Summary
[Role and likely priorities, based on title and campaign persona]

## Primary Outreach Angle
Trigger: [...]
Pain Point: [...]
Zediant Relevance: [...]

## Email Personalised Opening
[Written exactly as it should be stored in Email_Personalised_Opening —
second person ("you/your"), never third person about the recipient]

## Email Pain Points
[Written exactly as it should be stored in Email_Pain_Points]

## Relevant Service
[From services.md, matched to the confirmed challenge]

## Relevant Case Study
[Name if Tier 1, quoted testimonial language if Tier 2, category
description only if Tier 3 — or "no strong match" if none fit]

## LinkedIn Selection
Status: Ready to Connect | Not Required
[The specific reasoning against the batch-level priority criteria in
Section 4 — not just "high PTB score". This is a priority decision,
not a content-generation gate]

## LinkedIn Message & Follow-up
[Generated for every qualified lead regardless of LinkedIn Status —
written exactly as it should be stored in LinkedIn_Message, using the
CONNECT: / FOLLOW-UP: two-part format. Built on Step 11's verified-signal
framework: Path 1 (verified signal -> specific observation -> genuine
reason -> simple connection) when a real signal exists, or Path 2 (no
verified signal -> honest fallback -> simple connection) when it doesn't.
CONNECT is the actual first-touch connection request: no Zediant mention,
no pitch, no CTA, no meeting request, 20-45 words target/55 max. FOLLOW-UP
may carry soft non-promotional context but never pitches or asks for a
meeting/call. No research notes, evidence explanations, or scoring
commentary belong in this field]

## Confidence Score
High | Medium | Low
[High: Opening is a verified, company-specific fact. Medium: some
verified detail but leaning partly on industry-level fallback.
Low: no company-specific fact was found and the whole angle is
industry-level]

## Data Gaps
[What would strengthen the personalization if found]
```

When processing a batch, lead with a compact table — company, LinkedIn Status, confidence — then expand full output per company below it.

If the user explicitly asks for a full email draft rather than variables, produce it using the selected campaign's documented tone and CTA, but say plainly that this is outside the skill's normal output and that the live Apollo template remains the source of truth for anything actually sent.

---

# EXCEPTION HANDLING

| Situation | Action |
|---|---|
| Insufficient company information exists even after a genuine search | Fall back to industry-level messaging, say so explicitly, reflect it in a Low or Medium Confidence Score |
| No case study genuinely fits | Say "no strong match" rather than stretching a mismatched story |
| Technology stack is unknown | Avoid technical assumptions in the Opening or Relevant Service — a wrong technical guess is worse than a generic angle |
| Recent news or LinkedIn data can't be verified from a second source | Either drop it or note the uncertainty explicitly |
| A generated field contains an em dash or similar AI-typical character | Rewrite it before returning output — don't ship it and rely on `crm-update` to catch it |
| A generated field refers to the recipient in third person by their own first name (e.g., "Jason's team," "under Mahesh's leadership") | Rewrite to second person ("your team," "under your leadership") before returning output — don't ship it and assume a later review will catch it. This was previously an unwritten expectation; it is now a hard Validation gate as of v2.4 |
| Fewer than ~15 leads in a batch genuinely qualify for `Ready to Connect` | Flag fewer than 25 as `Ready to Connect`. Don't lower the bar to hit the target number. Every lead still gets LinkedIn content generated regardless |
| More than ~35 leads in a batch genuinely qualify | Still narrow the `Ready to Connect` flag to approximately the top quarter by ranking — flag that the batch was unusually strong rather than marking all of them `Ready to Connect`. Every lead still gets LinkedIn content generated regardless |
| Batch is large enough that generating LinkedIn content for every lead in one pass is genuinely impractical | Prioritize by the Buying Signal factor (Initial Buying Signal Score or Post-Engagement PTB Score, whichever applies), generate as many as practical, and explicitly list which leads' LinkedIn content is still outstanding — don't silently leave gaps that look like coverage |
| No LinkedIn profile found for a contact | Still generate the LinkedIn Message & Follow-up content from the same angle — the content isn't gated on profile availability, only the `Ready to Connect` priority decision considers profile availability/relevance |
| No verifiable recent signal (Step 11's 14-item list) can be found for a lead's CONNECT/FOLLOW-UP | Use Path 2 — build the fallback from verified person/company context (role, product, platform, market, business model, initiative), never a generic industry-only statement. Never stretch a weak candidate signal or invent one to avoid the fallback |
| Neither a verifiable recent signal (Path 1) nor sufficiently specific, verified person/company context (Path 2) exists for a lead | Use State C: ship the most factual, restrained connection note the evidence actually supports and flag the lead in `Data Gaps` for insufficient LinkedIn personalization evidence, rather than inventing a reason or silently shipping a generic industry message |

---

# ESCALATION

Escalate to a human rather than finalizing personalization:

- Manual research is genuinely required beyond what a reasonable search can surface
- Company information conflicts across sources and no source is clearly more reliable
- Industry is unknown or not covered by `icp.md`
- **High-value enterprise account** — a numeric **Post-Engagement PTB Score** of 90 or above (Excellent Opportunity) — have a human sanity-check the angle before it goes out. **This trigger applies to the Post-Engagement PTB Score specifically, never to the Initial Buying Signal Score** — a high pre-engagement Initial Buying Signal Score (even 90+) does not by itself trigger this escalation, since it reflects pre-engagement evidence strength, not the same thing a Post-Engagement PTB Score of 90+ represents. **When the Buying Signal factor is a numeric Initial Buying Signal Score, or is true `N/A / Not Yet Scored`, this escalation does not trigger** — don't treat either state as equivalent to a high Post-Engagement PTB Score, don't fabricate a tier to decide one way or the other, and don't withhold personalization while waiting for one. Continue applying the other escalation criteria on this list as normal; once a numeric Post-Engagement PTB Score exists later, evaluate this trigger against it in the usual way
- The personalization angle would require touching SOC 2, an SLA, or 24/7 coverage claims

---

# RELATED SKILLS

| Skill | Relationship |
|---|---|
| `lead-qualification` | Upstream. Establishes the company is worth pursuing, and supplies `Business_Challenges` this skill reads rather than re-deriving — that skill's Step 6 also owns the phrasing rule keeping the value compatible with its two live-template slots |
| `ptb-scoring` | Upstream. Its score feeds this skill's LinkedIn Selection priority ranking and "high-value account" escalation trigger |
| `campaign-selection` | Immediately upstream. Supplies the campaign whose messaging layer this skill instantiates |
| `crm-update` | Downstream. Writes `Email_Personalised_Opening`, `Email_Pain_Points`, `Case_Study`, the merged `LinkedIn_Message` field (now for every lead, not just `Ready to Connect`), and `LinkedIn Status` (`Rating`) into Zoho verbatim — this skill decides the content and the LinkedIn priority decision, that skill only writes it |
| `proposal-generation` | Downstream, later in the funnel. A different, larger deliverable than a personalized outreach touch |

---

# SUCCESS CRITERIA

| Measure | Target |
|---|---|
| Personalization facts traceable to a real, statable source | 100% |
| Fabricated facts, signals, or case studies | Zero |
| Tier 2/3 confidentiality violations | Zero |
| Generated content containing em dashes, en dashes, double hyphens, or other AI-typical special characters | Zero |
| Generated content referring to the recipient in third person by their own first name after a direct greeting | Zero |
| Generated content containing banned analytical/AI-summary phrasing, or using "AI" as an outreach framing device | Zero |
| Content fields failing the Email Quality Test (a BDM would need to rewrite before sending) | Zero |
| CONNECT messages mentioning Zediant, pitching, using a CTA, or requesting a meeting/call | Zero |
| FOLLOW-UP messages pitching, using a sales CTA, or requesting a meeting/call | Zero |
| LinkedIn Status selections based on batch ranking rather than quota or profile-presence alone | 100% |
| Merged LinkedIn Message & Follow-up content generated for every qualified lead, regardless of `LinkedIn Status` | 100% |
| `Not Required` leads left with a blank `LinkedIn_Message` field | Zero — this is now a defect, reversed from the pre-v2.3 target |
| CONNECT/FOLLOW-UP messages built on a fabricated, stretched, or unverified personalization signal | Zero |
| Path 2 fallback built only on a generic industry/role category with no specific, verified person or company fact attached | Zero |
| Leads with insufficient LinkedIn personalization evidence (State C) shipped as a generic message instead of a restrained note plus a `Data Gaps` flag | Zero |
| CONNECT/FOLLOW-UP messages combining more than one observation into a research-summary feel | Zero |
| CONNECT messages exceeding 55 words | Zero |
| LinkedIn-specific banned phrases (Step 11) appearing in CONNECT or FOLLOW-UP | Zero |
| `Case_Study` containing a fabricated case study | Zero |
| `zediant_outreach_natural_language_blacklist.md` read before drafting Opening, Pain Points, Case Study, or Business_Challenges wording | 100% |
| Blacklisted phrases appearing in Opening, Pain Points, or Case Study without being genuinely necessary to state a verified fact | Zero |
| Opening, Pain Points, or Case Study landing outside the 15-25 word target without a stated reason | Rare, flagged when it happens |
| `Business_Challenges`, `Email_Personalised_Opening`, or `Email_Pain_Points` left blank without further research having been attempted | Zero |
| `Case_Study` left blank without first checking the full campaign shortlist and `case_studies.md` | Zero |
| Reply rate lift attributable to personalization quality | Tracked, not yet targeted |

---

# VERSION

Version 2.9 · Owner: Zediant AI Sales Team · September 2026

**Changes in V2.9 — token-optimization + case-study confidentiality fix (SURGICAL, EDIT-ONLY):**
- Repointed Context files, Step 0, and Step 1 at `context/playbooks/C{1-5}.md` and `context/playbooks/_blacklist-digest.md` as the normal day-to-day reference, with the full source docs kept as the fallback for edge cases the playbooks don't resolve — pure token-efficiency change, no rule changed
- **Corrected Step 7's case-study confidentiality language.** It previously instructed checking a "Tier 1 named directly / Tier 2 quoted testimonial / Tier 3 category only" scheme — but `case_studies.md` explicitly marks that historical tier scheme `UNKNOWN`/not mapped to any current framework for every single entry. The actual, current, operative distinction in `case_studies.md` is `ANONYMISED` (describe by category, never name) vs. `NAMED` (currently only CS-04/11Wickets and CS-05/Diamond Professional Consultants) — both still gated by `HUMAN APPROVAL REQUIRED` for external use, which the existing BDM `Lead_Status` approval satisfies (confirmed in `case_studies.md`, September 2026). Step 7 now checks disclosure status against reality instead of a scheme that was never actually resolved
- No changes to the writing workflow, the verified-signal framework, word limits, blacklist rules, or any other section

**Changes in V2.8 — mandatory natural-language blacklist pre-read for the four content fields (SURGICAL, EDIT-ONLY, Email/Case-Study-content-only):**
- Added `zediant_outreach_natural_language_blacklist.md` to Context files and a new **Step 0**, requiring it be read before Steps 1-9 begin, every run — not consulted as an after-the-fact check once content is already drafted. Covers `Email_Personalised_Opening`, `Email_Pain_Points`, `Case_Study`, and (where this skill's wording touches it) `Business_Challenges`.
- **Word count changed from 25-45 to approximately 15-25 words** for Opening, Pain Points, and Case Study, matching the blacklist file's own Final Quality Check. This is a real behavior change, not additive — updated Steps 8, 9, 7, and both word-count lines in Validation.
- Step 5 (The One Primary Angle) extended to explicitly cover `Case_Study` and `Business_Challenges`: the four fields now have to read as one connected line of reasoning (observation → pressure → case study → case study's own challenge), not four independently-true, disconnected sentences — new guidance on preferring a case study whose business problem echoes this lead's Pain Point over one that only shares an industry.
- Steps 7, 8, and 9 each gained a line pointing back to the blacklist's per-field guidance (Rules for the Four Zoho Fields) for what to focus the sentence on and what to avoid, plus the "AI" framing rule (only when the prospect's own verified activity makes it relevant, never because the campaign is C1).
- Added a **final human-writing test** at the end of Step 9, applied to all four fields: "Would this sentence sound normal if a Zediant salesperson personally typed this email to one CTO or VP Engineering?" — restating the blacklist file's own closing test as a named gate, not left implicit in the existing Email Quality Test.
- **Case_Study's blank-field rule tightened, without weakening the anti-fabrication rule it sits next to.** Step 7 and Validation now require exhausting research (full campaign shortlist, a re-read of `case_studies.md`) before accepting a blank `Case_Study` — but the underlying rule that a blank field beats a fabricated one is unchanged and still absolute. Extended the same "research further before accepting a gap" expectation to `Business_Challenges`, `Email_Personalised_Opening`, and `Email_Pain_Points`, which were never meant to end up blank in the first place.
- Updated Validation (new blacklist-read check, word-count line, story-coherence check, human-writing-test check, non-blank-without-research check) and Success Criteria (five new rows) to match.
- **Preserved unchanged:** the absolute never-fabricate-a-case-study rule, all LinkedIn CONNECT/FOLLOW-UP content and word limits (20-45/55 max, 40-70), the second-person requirement, the em-dash/AI-phrasing/AI-framing bans, the confidentiality-tier rules, Apollo Template Compatibility, LinkedIn Selection Strategy (Section 4), and every unrelated section. This was a file-only edit — no Zoho, Apollo, Apollo, or Cliq activity occurred as part of making this change.

**Changes in V2.7 — strengthen the Path 2 LinkedIn fallback (SURGICAL, EDIT-ONLY, LinkedIn-fallback-only):**
- Root cause: v2.6's Path 2 fallback was honest but could still be fully generic — e.g. "Hi Mohammad, always good to connect with people building in the mobility/telematics space. Look forward to staying in touch." — since the rule only required avoiding a claimed-but-unverified observation, not requiring the fallback itself to be person/company-specific.
- **Path 2 redefined**: now NO VERIFIED RECENT SIGNAL → **VERIFIED PERSON/COMPANY CONTEXT** → HONEST REASON FOR INTEREST → SIMPLE CONNECTION, with an explicit list of acceptable fallback evidence (professional responsibility, role, actual product/platform/business model, a specific market, a verified initiative, or another factual person/company characteristic).
- **Added a hard rule prohibiting generic industry-only fallbacks**, with the exact banned generic-industry phrasing patterns and a bad/better worked example (Mohammad/Connexion Mobility).
- **Added the internal "why would Rajeev genuinely want to connect with this particular person" check** — must be answerable from verified information before a fallback message is generated; the reasoning itself is never written into `LinkedIn_Message`. Also clarified that inserting a name and company alone, without a genuine reason, does not count as personalization.
- **Introduced State C** (formalizing the three-state model: State A = Path 1, State B = Path 2, State C = neither exists): when no recent signal and no sufficiently specific verified person/company context exist, the system must not manufacture personalization — it ships the most factual, restrained note the evidence supports and flags the lead in `Data Gaps` for insufficient LinkedIn personalization evidence, rather than forcing a generic message.
- **Added seven fallback-specific checks** (does it name specific verified context; is a claimed signal actually verifiable; is the fallback reason person/company-specific; would it work unmodified for 100 unrelated people in the industry; does it answer "why this person"; is it fact-based; could Rajeev personally stand behind it) as a mandatory gate whenever Path 2 or State C is used, run in addition to the existing 12-point LinkedIn Quality Test.
- Replaced the old fully-generic fallback worked example with a verified-company-context example, and updated Validation, Exception Handling (split into a Path 2 row and a new State C row), and Success Criteria to match.
- **Preserved unchanged**: Path 1's architecture and 14-item signal list, the personalization depth restraint (one observation only), all CONNECT hard prohibitions (no Zediant, no pitch, no CTA, no meeting/Calendly, no dev-needs questions, no synergy language), the LinkedIn-specific banned-phrase list, CONNECT's 20-45/55-word limits, FOLLOW-UP's architecture and 40-70 word limit, Rajeev's voice guidance, the existing 12-point Quality Test and the LinkedIn Personalization Quality Test, the CONNECT:/FOLLOW-UP: two-part output format, and the field-hygiene rule (no research notes/scoring commentary in `LinkedIn_Message`).
- **No changes to**: ICP scoring, Initial Buying Signal Score, Post-Engagement PTB, campaign selection or the C1-C5 taxonomy, campaign/sender allocation, Apollo search logic or credit rules, deduplication, lead qualification, CRM field mappings or write logic, Scheduler 1/2, Apollo, Case Study logic, Email channel personalization rules, Cliq rules, BDM approval rules, or Section 4's LinkedIn Selection priority ranking. This was a file-only edit — no Apollo, Zoho, Apollo, or Cliq activity occurred as part of making this change.

**Changes in V2.6 — LinkedIn CONNECT/FOLLOW-UP verified-signal framework (SURGICAL, EDIT-ONLY, LinkedIn-content-only):**
- Root cause: a live run's CONNECT text for one lead ("Hi Mohammad, came across Connexion Mobility and the telematics platform. Would be good to connect.") was generic and untethered to any specific, verifiable fact — it read as filler personalization rather than a genuine observation, because Step 11 previously named a Trigger requirement but gave no priority-ordered definition of what counts as a verifiable signal, no explicit fallback for when none exists, and no restraint against combining research into a summary-style note.
- **Added the verified-signal framework as a first-class, permanent rule in Step 11** (not just examples): **Path 1 — VERIFIED SIGNAL → SPECIFIC OBSERVATION → GENUINE REASON → SIMPLE CONNECTION**, with a 14-item priority-ordered list of what counts as a verifiable signal (recent LinkedIn post/activity/comment, company announcement, product launch/direction, meaningful hiring activity, market/geography expansion, funding/investment, acquisition/partnership, interview/podcast/speaking, published article, identifiable professional responsibility, owned product/platform area, other verifiable professional information); and **Path 2 — NO VERIFIED SIGNAL → HONEST FALLBACK → SIMPLE CONNECTION**, used whenever nothing on that list can be verified, with an explicit "honest and simple is always better than fake personalization" principle and a rule against using "I noticed"/"I saw" without a real observation behind them.
- **Added a hard rule against fabricating personalization from unverified assumptions** (industry membership alone, or an unverified tech change/expansion/hiring push/post/launch/challenge) and a **personalization depth restraint** requiring exactly one observation per message, never a stacked research-summary feel.
- **Extended CONNECT's hard prohibitions**: explicit bans on pitching software development/engineering/staff augmentation/AI/integration work, on Calendly or any scheduling link, on asking about business requirements/pain points/hiring, and on "explore synergies"/"potential collaboration"/similar corporate-networking language, alongside the pre-existing no-Zediant/no-pitch/no-CTA/no-meeting rules.
- **Added a LinkedIn-specific banned-phrase list** (distinct from the existing analytical/AI-summary phrase list in Writing Style, which is unchanged) covering relationship- and sales-cliché phrases ("I'd love to explore synergies," "potential collaboration," "leverage our expertise," "help you scale," etc.) and a conditionally-banned generic-opener list ("Hope you're doing well," "Great to connect," etc.).
- **Added explicit CONNECT word-count limits**: target 20-45 words, 55 words absolute maximum (previously "no fixed word count, but well under LinkedIn's character limit"). FOLLOW-UP's existing 40-70 word range is unchanged.
- **Added "Rajeev's voice" tone guidance** (professional, curious, calm, genuine, concise, observant, conversational — sounds like one named person, not a sequence) and a **12-point LinkedIn Quality Test**, run in addition to the pre-existing LinkedIn Personalization Quality Test.
- **Added an explicit output-hygiene rule**: `LinkedIn_Message` holds only the CONNECT and FOLLOW-UP message text — no research notes, evidence explanations, scoring commentary, or internal reasoning; any such note belongs in `Data Gaps` instead.
- Rewrote the worked CONNECT/FOLLOW-UP example under "THE ONE PRIMARY ANGLE" to demonstrate Path 1 against a named signal (a hiring-related company post), and added a short Path 2 fallback example inline in Step 11.
- Updated Validation (new checks for Path 1/Path 2 compliance, one-observation restraint, banned-phrase absence, the 12-point Quality Test, and the revised CONNECT word count), Exception Handling (new row for "no verifiable signal found"), Success Criteria (new rows for fabricated-signal, research-summary, over-length CONNECT, and banned-phrase defects), and the Output Format instructional text for `LinkedIn Message & Follow-up`, to match.
- Lightly updated the frontmatter `description` to reflect the verified-signal/honest-fallback framework.
- **No changes to**: ICP scoring, the Initial Buying Signal Score model or its 25/20/15/15/15/10 weighting, Post-Engagement PTB, campaign taxonomy (C1-C5), campaign allocation, Apollo search logic or credit rules, deduplication, CRM field mappings, `crm-update`'s write behavior, the Email channel's core structure (Steps 1-9), the second-person requirement, case study selection or confidentiality-tier rules, Apollo Template Compatibility, Section 4's LinkedIn Selection priority ranking (the ~top-25 batch ranking logic), BDM approval rules, Scheduler 1/2 logic, or the existing analytical/AI-summary banned-phrase list in Writing Style (which still applies to all fields, unchanged, alongside the new LinkedIn-specific list). This was a file-only edit — no Apollo, Zoho, Apollo, or Cliq activity occurred as part of making this change.

**Changes in V2.5 — Initial Buying Signal Score integration, literal-copy email quality bar, LinkedIn connection-request redefinition (EDIT-ONLY architecture update):**
- **Buying Signal factor terminology.** Every reference to PTB being `N/A / Not Yet Scored` as the normal pre-engagement state was updated: `ptb-scoring` Path A now calculates a numeric **Initial Buying Signal Score** for essentially every lead reaching this skill from Scheduler 1, so that is now the normal input, and true `N/A / Not Yet Scored` is a rare fallback. Updated: frontmatter description, Context files table, Workflow position, Required Inputs, Step 2, Step 10, Section 4, and Related Skills. The Post-Engagement PTB Score (`ptb-scoring` Path B) is unchanged and still gates the Escalation section's high-value-account trigger specifically — the Initial Buying Signal Score never triggers that escalation, and the two scores are never confused or converted into each other anywhere in this skill's output.
- **Literal, ready-to-send content requirement (new).** Added the **Email Quality Test** ("could a BDM copy this exact text into a real email or LinkedIn message and send it, without rewriting it first?") as a hard Validation gate. Added an explicit banned analytical/AI-summary phrase list ("The company appears to...", "The prospect likely...", "This indicates...", "Based on available signals...", "It seems that...", "They may be facing...") to Writing Style, Personalization Rules, and Validation. Added a rule against using "AI" as a personalization/outreach framing device, with a narrow carve-out for factual mentions of AI as the prospect's own product/technology. Extended the existing em-dash/en-dash ban to also cover the double hyphen (`--`).
- **LinkedIn first-touch redefinition (reversal of prior behavior).** Step 11's CONNECT message was previously defined as the first message *after* the connection was accepted, and was allowed to briefly position Zediant and use a soft CTA. This is reversed: **CONNECT is now the actual connection-request note**, sent before acceptance, and must contain no mention of Zediant, no pitch, no CTA, and no meeting/call request — a short, natural, one-to-one note only. FOLLOW-UP is now the first real message after acceptance; it may carry soft, non-promotional context about what Zediant does, but the prior "soft CTA" allowance is removed — FOLLOW-UP must never pitch, ask for a meeting/call, or use a sales CTA. Added the **LinkedIn Personalization Quality Test** (would this read as a genuine personal connection, or an SDR sequence?). Rewrote the worked example under "The One Primary Angle," the Exception Handling batch-size row, Validation, Output Format, and Success Criteria to match.
- No changes to the Email channel's core structure (Steps 1-9), the case study rules, the confidentiality tiers, the second-person requirement, the Apollo Template Compatibility mapping, or any unrelated section.
- Root cause: a live 88-lead batch generated on August 13, 2026 wrote `Email_Personalised_Opening` content that referred to the recipient in third person by first name (e.g., "Jason's team," "Nicki is probably feeling") even though the live Apollo template greets the recipient directly (`Hi {{First Name}},`) immediately beforehand. Caught by a human reading the field inside the actual template rather than in isolation, on the Jason Elston / Snug.com record
- Added an explicit, hard second-person requirement to Step 8, with a wrong/right example drawn from the real bug
- Extended the same rule to Step 9 (`Email_Pain_Points`) for consistency of person across both fields
- Added a cross-reference in Apollo Template Compatibility explaining *why* this only surfaces when a field is read inside the template structure, not on its own
- Added a new row to Personalization Rules, Exception Handling, Validation, and Success Criteria so this is now a checked gate, not an implicit expectation
- Audited the other four fields this skill or its downstream partners write into the live email sequence (`Email_Pain_Points`, `LinkedIn_Message` connect/follow-up, `Business_Challenges`, `Case_Study`) against the same 195-record production pool used to find the original bug — no third-person self-reference issues found in any of them. `LinkedIn_Message` already used second person by convention (Step 11's example content); `Business_Challenges` and `Case_Study` are written about the company, not addressed to the recipient, so the failure mode doesn't apply to them the same way. No changes were needed to Steps 7 or 11 as a result, only this explicit confirmation
- All 88 affected `Email_Personalised_Opening` records from the source batch were corrected and re-written to Zoho outside this skill's normal flow, as a one-time remediation — this version change is what prevents the same defect in future runs, not a retroactive fix mechanism

**Changes in V2.3 — LinkedIn content generation decoupled from LinkedIn Status:**
- Reversed the prior behavior where `LinkedIn_Message` was only generated for `Ready to Connect` leads and left blank for `Not Required` leads. As of this version, **every qualified lead gets LinkedIn Message & Follow-up content generated (Step 11)**, using the same Step 5 angle already produced for the Email channel — no additional research pass required
- `LinkedIn Status` (`Ready to Connect` / `Not Required`) is now explicitly documented as a **priority/sequencing flag only** — it tells the BDM and the manual LinkedIn execution process approximately the top quarter of the written batch to actively work first. It no longer gates whether content exists
- Section 4 rewritten to separate "what gets generated" (everyone) from "what gets prioritized for active outreach" (approximately the top quarter) — these were previously conflated into a single gate
- Updated Validation, Exception Handling, Output Format, Related Skills, and Success Criteria to match — a blank `LinkedIn_Message` on a `Not Required` lead is now a defect to catch, not an expected outcome
- Added guidance for the edge case where generating LinkedIn content for an entire large batch in one pass is impractical: prioritize by PTB Score and explicitly disclose which leads are still outstanding, rather than silently leaving gaps
- Rationale: real-world use showed `Not Required` leads had no LinkedIn content sitting ready when priority later shifted (new signal, BDM manual pickup, batch re-ranking), forcing a full skill re-run for a single lead. Generating up front removes that gap at effectively no extra research cost, since the single outreach angle underlying both channels is already built for the Email fields regardless of LinkedIn Status

**Changes in V2.2 — grammatical fit against the live Apollo templates:**
- Pulled and reviewed the actual live template content for all five campaigns' active sequence steps (not assumed from field names) to find where each merge tag really lands
- Added a hard requirement to Step 9: `Email_Pain_Points` must read as fully self-contained, with no demonstrative back-reference to `Email_Personalised_Opening` — every campaign reuses Pain Points a second time in a later follow-up email where the Opening is not present, and a dangling "like that" or "this shift" only makes sense in the first placement
- Added a hard requirement to Step 7: `Case_Study` must be one standalone, self-contained sentence — it merges directly into a live template as its own line in four of five campaigns; noted the one accepted exception (C5's final message) as a known limitation, not something to design around
- Rewrote the Apollo Template Compatibility section, which previously described only `Email Personalised Opening`/`Email Pain Points` as merge-tag-facing. It was stale: `Business_Challenges` and `Case_Study` are also live merge tags (`{{Business Challenge}}`, `{{Case Study}}`), reused in a second location each, and subject to the same human-sounding, grammatically-correct bar
- Companion fix: `Business_Challenges`' own dual-use grammatical requirement (standalone sentence vs. subordinate clause after "Given" in C1) is now documented at its actual authoring point, `lead-qualification` Step 6 (v1.3), since that skill's wording carries forward unedited — this skill reads the value rather than rewriting it, so the rule lives there, not here
- Companion fix: `apollo-distribution` v1.6 now actually pushes `Case_Study`/`Business_Challenges` as Apollo merge variables — previously the live templates referenced `{{Case Study}}`/`{{Business Challenge}}` but the push payload never sent them, so those fields rendered blank in any email that reached those steps

**Changes in V2.1 — Case Study/Business Challenges fields, LinkedIn field merge:**
- `Business_Challenges` is now a real CRM field, carried forward from `lead-qualification`'s Step 6 finding — this skill reads it as a required input for Email Pain Points rather than re-deriving a challenge
- `Case_Study` is now a real CRM field (Step 7 rewritten) — selection is driven by the confirmed Business Challenges, not shared industry alone, and the no-fabrication rule is absolute: blank is the correct output when nothing approved fits
- `LinkedIn_Follow_up` deleted from Zoho. Steps 11-12 merged into one step generating both the connect message and the follow-up, written into the single `LinkedIn_Message` field (relabeled LinkedIn Message & Follow-up) using a CONNECT/FOLLOW-UP two-part format
- Output Format, Validation, Related Skills, and Success Criteria updated to match

**Changes in V2.0 — LinkedIn outreach:**
- Added the full LinkedIn Selection Strategy (Section 4): batch-level ranking to approximately the top quarter of the written batch, eligibility and not-required criteria, and the two-value-only status rule
- Added LinkedIn Message and LinkedIn Follow-up generation, originally gated on `LinkedIn Status = Ready to Connect` (reversed in V2.3 — see above)
- Replaced the old Opening Observation / Business Challenge / Subject Line / CTA / Follow-up Angle / merge-variable model with the current Zoho fields: `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message`, `LinkedIn_Follow_up`
- Replaced stale Instantly references with Apollo, and List B/List C campaign references with C1-C5, to match `campaign-selection` v2.0 and `crm-update` v4.0
- Added the "write like a human" rule: no em dashes or other AI-typical special characters in any generated field, checked at Validation
- Introduced the single Trigger → Pain Point → Zediant Relevance angle requirement feeding all four content fields

This skill still does not decide tone, angle category, or CTA — those are read from `campaigns.md`. Its job is finding the real, verifiable fact that makes the campaign's generic angle true of one specific company, deciding that company's LinkedIn outreach priority, and packaging Email plus LinkedIn content for every qualified lead as field-ready content rather than prose.

