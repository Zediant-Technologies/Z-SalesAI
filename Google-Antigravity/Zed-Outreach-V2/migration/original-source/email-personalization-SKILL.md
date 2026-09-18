---
name: "email-personalization"
description: "Zediant's email + LinkedIn personalization SOP — generates Email Personalised Opening, Email Pain Points, Case Study, Business Challenges, and the merged LinkedIn Message & Follow-up field for every company that has cleared Lead Qualification, PTB Scoring, and Campaign Selection. LinkedIn content is now generated for every lead regardless of LinkedIn Status — Status (Ready to Connect / Not Required) is purely an outreach-priority flag for the top ~25 of every ~100, not a content gate. Use for \"personalize this email for X\", \"should X get LinkedIn outreach\", \"write the LinkedIn message for X\", \"run personalization on this batch\", or right after Campaign Selection names a campaign. Writes human-sounding copy with no AI-typical special characters. Produces variables for Zoho and Saleshandy — does NOT send anything. Never fabricates a fact, signal, or case study."
---

---
name: "email-personalization"
metadata:
  version: "2.3"
---

# Email + LinkedIn Personalization

Generate the specific, verified detail that makes one email — and, now, one LinkedIn touch for every qualified lead — read as written for this company rather than copy-pasted at it. Package it as Zoho field values, not prose.

## The one thing to understand before anything else

**The production model is two channels from one research pass, for every qualified lead.** Every qualified lead gets Email personalization **and** LinkedIn Message & Follow-up content. `LinkedIn Status` (`Ready to Connect` / `Not Required`) is a separate, batch-level **outreach priority flag** — it tells the BDM and the manual LinkedIn process which ~25 of every ~100 leads to actually work first on LinkedIn. It is not, as of this version, a gate that decides whether LinkedIn content gets written at all. Both channels come from the same underlying research and the same single outreach angle — see **The One Primary Angle** below. Do not treat LinkedIn Selection as a separate skill invocation from Email personalization; they happen in the same pass, for the same reason, off the same evidence.

**Why this changed:** earlier versions of this skill only generated LinkedIn content for `Ready to Connect` leads, leaving `Not Required` leads with a blank `LinkedIn_Message` field. In production this meant that if a `Not Required` lead's priority changed later (a new signal appeared, a BDM wanted to work it manually, or the batch ranking was revisited), there was no LinkedIn content sitting ready to use — the whole personalization pass would need to be re-run for that one lead. Generating the content for everyone up front removes that gap at effectively no extra cost, since the research and the single outreach angle (Step 5) are already being done for the Email channel regardless.

**`campaigns.md` already defines the messaging layer for each campaign** — its Messaging Angle, Recommended Email Tone, example Personalization Opportunities, Recommended CTA, the four-touch Email Sequence Strategy, and a Related Case Studies shortlist. That layer is generic to the campaign; it's the same for every company in C1, for instance.

This skill's job is the layer campaigns.md deliberately leaves blank: **which of those generic opportunities is actually true of this specific company, and what's the evidence.** Read the selected campaign's messaging layer first, then find the concrete fact that instantiates it. Don't invent a new messaging angle or CTA — those are already decided. Don't skip finding a real fact and write something generic that merely sounds personalized.

**This skill does not write the email itself.** The approved email structure lives in the live Saleshandy template. This skill fills in the merge-tag blanks in that template — `Email Personalised Opening` and `Email Pain Points` directly, plus `Business_Challenges`/`Case_Study` which also land as live merge tags further down the sequence — with real, checkable content — see **Saleshandy Template Compatibility** below. If the user explicitly asks for a full email draft, that's a different, larger request — flag that you're stepping outside the variable-generation scope before doing it.

## Scope — and the boundary that matters

**Owns:** producing verified Email and LinkedIn personalization content for one named company and contact, deciding whether that company is in the priority slice for active LinkedIn outreach as part of the current batch, and packaging it ready for `crm-update` to write.

**Does not own:**

| Not this skill | Goes to |
|---|---|
| Deciding whether the company is worth pursuing | `lead-qualification` |
| Calculating the priority score | `ptb-scoring` |
| Choosing which campaign the company enters | `campaign-selection` |
| The campaign's messaging angle, tone, CTA, and sequence structure | Already decided in `campaigns.md` — read it, don't re-derive it |
| Writing the Saleshandy template itself, activating a campaign, or sending anything | Nobody, automatically. Saleshandy holds the approved templates; activation is an explicit human action |
| Writing personalization data into CRM fields, or writing `LinkedIn Status` to Zoho | `crm-update` skill — this skill decides the value, that skill writes it |
| Actually sending the LinkedIn connection request, message, or follow-up | A human, manually, using the content this skill produces — regardless of `LinkedIn Status` |
| Formal proposals or SOWs | `proposal-generation` |

## Context files — reference, never restate

| Document | What it supplies |
|---|---|
| `campaigns.md` | The selected campaign's Messaging Angle, Tone, example Personalization Opportunities, Recommended CTA, Email Sequence Strategy, Common Objections, and Related Case Studies shortlist |
| `services.md` | Which Zediant capability matches the confirmed business challenge, and the "Unsubstantiated performance claims" table of statistics that must never be cited |
| `case_studies.md` | The confidentiality tiers (never name Tier 3), the per-case-study selection metadata, and the structural warnings (CS-02/CS-06 same-client, concentration-risk overuse) |
| `company.md` | The SOC 2 Type II wording rule if the personalization touches security or compliance messaging |
| `pricing.md` | Commercial context if a personalization angle implies a pricing conversation |
| `campaign-selection` | Owns the selected campaign this skill reads rather than re-deciding |
| `ptb-scoring` | Owns the score this skill's LinkedIn Selection ranking and "high-value account" escalation trigger are defined against |

**Cite only sections that actually exist, by their real names.** A true fact with a fabricated citation is still a fabrication problem — it just fails a different way, on a spot-check rather than on the fact itself. Before finalizing output, mentally re-locate every named table or section you cited; if you can't, rephrase it as your own reasoning instead.

---

# REQUIRED INPUTS

Company Name · Company Website · Industry · Business Description · Country · Employee Count · Buying Signals · Business Challenges (as a real CRM field now — `Business_Challenges`, carried forward from `lead-qualification`'s Step 6 finding; read it rather than re-deriving it) · Selected Campaign (C1-C5) · Decision Maker · Recent News (if available) · LinkedIn Profile (if available) · Case Studies · PTB Score and tier · ICP fit · **the full batch of qualified leads currently being processed together, for LinkedIn Selection ranking** (see Section 4).

Nearly all of this already exists from the `lead-qualification`, `ptb-scoring`, and `campaign-selection` passes that got the company here. Re-read those outputs before searching for anything new — this skill's genuinely new research is narrow: confirming the personalization angle is still current, and finding the one or two specific facts that make the opening line concrete.

**Do not invent:** funding, hiring activity, technology usage, product launches, company initiatives, business problems, budgets, projects, customer problems, growth figures, or technology platforms. If a specific signal cannot be verified, use a broader but credible business/engineering observation and say so.

---

# WORKFLOW

## Step 1 — Read the selected campaign's messaging layer

From `campaigns.md`, pull that campaign's Messaging Angle, Recommended Email Tone, example Personalization Opportunities, Recommended CTA, and Related Case Studies shortlist. For C1 (AI-Enabled Product Engineering), focus on product engineering, product development, engineering capacity, roadmap, development velocity, scaling product teams. For C2 (Engineering Pods & Staff Augmentation), focus on engineering capacity, team augmentation, scaling delivery, hiring constraints, development bandwidth, dedicated engineering teams. Don't introduce a Zediant service unrelated to the selected campaign.

## Step 2 — Confirm the company profile

Industry, business model, and growth stage should already be established. Read the qualification, PTB, and campaign-selection outputs rather than re-researching from scratch.

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

**All four content fields (Email Opening, Email Pain Points, LinkedIn Message, LinkedIn Follow-up) come from this one angle, for every qualified lead.** Don't create multiple unrelated angles for one company; the wording differs by channel, the underlying strategy doesn't.

## Step 6 — Match the confirmed challenge to a Zediant capability

Use `services.md`'s Business Problems Solved for the campaign's Recommended Services to find the specific capability that addresses the confirmed challenge from Step 5.

## Step 7 — Select the case study

Zoho field: `Case_Study` (new as of today). Start from the selected campaign's Related Case Studies shortlist in `campaigns.md`, and let the confirmed Business Challenges from Step 5 drive the pick, not shared industry alone — two companies in the same industry with different challenges should not automatically get the same case study.

Before using it, check: **Confidentiality tier** (Tier 1 named directly; Tier 2 quoted testimonial only, never extended; Tier 3 described by category only, never named). **The CS-02/CS-06 overlap** — same client, use one not both. **Concentration balance** — vary the proof point where context allows.

**This is the single most fabrication-prone field in the whole skill, so the rule is absolute: only select a case study that actually exists in approved Zediant content.** Never invent a customer name, a metric, a technology, or an outcome to make a case study "fit" better. If no case study genuinely fits, or if no approved case study content is available to select from at all, leave `Case_Study` blank and say so plainly — a blank field is the correct, expected output here, not a gap to paper over with something plausible-sounding.

`Case_Study` is written verbatim by `crm-update` when populated. It is available to both Email and LinkedIn content where it genuinely fits the sequence — never force it into every touch just because a value exists.

**Write it as one self-contained sentence that can stand entirely on its own.** Like `Business_Challenges`, this value is merged directly into live Saleshandy templates, not just stored in Zoho — in four of the five campaigns it lands as `{{Case Study}}` on its own line, immediately after an intro sentence like "We've worked with teams facing something similar before." A fragment or noun phrase reads as broken there. (One template slot, C5's final message, uses `{{Case Study}}` as a sentence subject instead — that's a known, accepted exception, not something to write around; don't compromise the other five slots to accommodate it.)

## Step 8 — Generate Email Personalised Opening

Zoho field: `Email_Personalised_Opening`. This is **not** a complete email.

Requirements: 1-2 sentences, approximately 25-45 words, specific to the prospect/company, based on the strongest credible trigger, natural and conversational, starts with prospect/company context. Do not start with generic compliments. Do not mention Zediant. Do not include the main sales pitch, the signature, the main CTA, or a direct repeat of the pain point. **No AI-typical special characters** (em dashes, en dashes, curly quotes used decoratively, etc.) — write it the way a person would actually type it.

Potential triggers: engineering team growth, hiring, product expansion, product development, new product launch, funding/growth, technology transformation, digital transformation, API/integration initiatives, legacy modernization, cloud initiatives, scaling engineering operations, a relevant responsibility of the prospect.

## Step 9 — Generate Email Pain Points

Zoho field: `Email_Pain_Points`. Identifies the most relevant business/engineering problem tied to the trigger, grounded in the `Business_Challenges` CRM field carried forward from `lead-qualification`'s Step 6 — don't contradict what that field already says, and don't invent a different challenge that sounds better.

Requirements: 1-2 sentences, approximately 25-45 words, must logically follow the Opening (don't repeat it), focus on the business/engineering challenge, no unsupported claims, no exaggeration, don't mention Zediant unless the live Saleshandy template specifically requires it. **No AI-typical special characters.**

Use language like "can create," "may put pressure on," "often creates," "can become challenging." Potential pain areas: engineering capacity, product delivery velocity, hiring and onboarding experienced engineers, scaling development teams, product roadmap execution, integration complexity, legacy modernization, technical delivery bandwidth, maintaining development velocity during growth.

**Must be self-contained — no backward reference to the Opening.** This is not optional stylistic advice, it's a template-compatibility requirement: every live Saleshandy sequence reuses `Email_Pain_Points` a second time, days later, in a separate follow-up email that does **not** include `Email_Personalised_Opening` — it appears alone after a lead-in like "Following up on something from my last note - {{Email Pain Points}}" or "Coming back to something from my last note — {{Email Pain Points}}". A sentence like "Moving into new verticals **like that** can put pressure on..." reads fine in Step 1, next to the Opening it's pointing back to, but dangles when it resurfaces alone in the follow-up. Avoid demonstrative pronouns ("that," "this," "such a shift") whose antecedent lives only in the Opening — restate the specific trigger detail in a few words instead of gesturing back at it. The sentence has to make complete sense to someone who never saw the Opening at all.

## Step 10 — LinkedIn Selection (batch-level priority ranking — see Section 4 for full detail)

Evaluate this company against the rest of the current batch on PTB Score, ICP fit, buying intent, prospect seniority, LinkedIn profile availability and relevance, and quality of personalization opportunity. Set `LinkedIn Status = Ready to Connect` only for approximately the top 25 out of every ~100 qualified leads, on quality — not by taking the first 25 or by LinkedIn-profile-presence alone. Otherwise, `LinkedIn Status = Not Required`. Full criteria in Section 4.

**This decision no longer controls whether LinkedIn content gets generated (see Step 11) — it controls priority and sequencing only.** `Ready to Connect` tells the BDM and the manual LinkedIn process "work this one now." `Not Required` means "not in this batch's active LinkedIn push," not "no LinkedIn content exists for this lead."

## Step 11 — Generate LinkedIn Message and Follow-up (for every qualified lead, regardless of LinkedIn Status)

Zoho field: `LinkedIn_Message` — relabeled **LinkedIn Message & Follow-up** in Zoho, and now holds both pieces of content in one field, not two. Generate both messages here **for every qualified lead that reached this step**, using the same Step 5 angle already produced for the Email channel — this is not additional research, it's the same angle expressed in LinkedIn's tone and format. Then write them into the field using the fixed two-part format `crm-update` expects:

```
CONNECT:
[the connection message]

FOLLOW-UP:
[the follow-up message]
```

**Connect message.** This is the first message after the connection has been accepted, not the connection request itself. 40-70 words maximum, conversational, natural LinkedIn tone, based on the same Trigger/Pain Point as the email but must not copy the email or the Opening. Briefly position Zediant only where relevant — no long company description, no aggressive pitch, no unnecessary compliments. Prefer a soft conversational question/CTA; don't push for a meeting unless the buying signal is exceptionally strong.

**Follow-up message.** Continues the conversation if the prospect connected but hasn't responded to the first message. 35-60 words maximum, must add a new point, insight, or angle — not copy the connect message or the email. Must NOT say "just following up," "checking if you saw my message," or "wanted to follow up." Don't become more aggressive; keep it conversational with a soft CTA that adds value rather than just requesting a response.

**No AI-typical special characters in either half**, and the `CONNECT:`/`FOLLOW-UP:` labels plus the blank line between them are the only structural formatting allowed — no bullets, no decorative separators.

**On the rare occasion the batch is so large that generating LinkedIn content for every single lead is genuinely impractical in one pass**, prioritize generation in PTB Score order (highest first) and say explicitly which leads' LinkedIn content is still outstanding — don't silently skip the bottom of the batch and let it look like every lead was covered.

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

LinkedIn Message & Follow-up (one field, two-part format):
CONNECT:
"Hi John, noticed the growth in ABC's engineering organization alongside the product expansion. We work with SaaS teams that need additional engineering capacity without adding significant hiring overhead. Curious how you're approaching that as the roadmap grows."

FOLLOW-UP:
"One area where we typically help is providing an experienced engineering pod that can plug into an existing roadmap while the internal team continues hiring. Thought that might be relevant given ABC's current growth."
```

Wording differs across channels; the underlying strategy does not.

---

# SECTION 4 — LINKEDIN SELECTION STRATEGY

**LinkedIn Status is a priority flag, not a content gate.** As of v2.3, every qualified lead gets LinkedIn Message & Follow-up content generated (Step 11). This section decides which ~25 of every ~100 leads are flagged `Ready to Connect` — meaning "the BDM/manual LinkedIn process should actively work this lead now" — versus `Not Required` — meaning "content exists and is ready if needed, but this lead isn't in the current active push." LinkedIn execution effort is still the scarce resource being rationed here; content generation is not.

For every batch of qualified leads: evaluate all of them, review PTB Score, review ICP fit, review buying intent, review prospect seniority, review LinkedIn profile availability and relevance, review quality of personalization opportunity, rank by LinkedIn priority, then select approximately the top 25 strongest as `Ready to Connect`.

**Quality over hitting exactly 25.** If only 18 leads are genuinely strong enough for the active push, mark 18 as `Ready to Connect`. If more than 25 are strong, still mark approximately the top 25 — don't force the number in either direction. Every lead outside that slice still gets its LinkedIn content generated and stored; it simply isn't flagged for the current active push.

## LinkedIn Status = Ready to Connect

Set when the lead has a strong combination of: high PTB Score, strong ICP fit, strong or credible buying/intent signal, senior or decision-making role, strong relevance to the selected campaign, a relevant LinkedIn profile, strong personalization opportunity, and a business/engineering problem Zediant can credibly address. Typical high-priority roles: CTO, CIO, VP Engineering, VP Technology, Head of Engineering, Head of Product, Engineering Director, and other senior decision-makers directly relevant to the campaign — but don't restrict selection to title alone; overall lead quality matters more.

## LinkedIn Status = Not Required

Set when: PTB isn't sufficiently high, ICP fit is moderate or weak, intent is weak or unclear, prospect seniority/relevance is insufficient, LinkedIn profile is unavailable or unsuitable, personalization opportunity is weak, the prospect isn't among the highest-priority leads in the current batch, or email alone is judged sufficient for now. **Email = active, LinkedIn = not in this batch's active push is an expected, normal outcome** — it is not a downgrade, and it does not mean the LinkedIn content is missing.

## Status values at this stage — exactly two, never more

At the lead-generation stage, this skill decides only between `Ready to Connect` and `Not Required`. Never set an execution status (`Connection Sent`, `Connected`, `Message Sent`, `Follow-up Due`, `Follow-up Sent`, `Response Received`, or similar) — those belong to the later manual LinkedIn execution process a human runs, and are written directly in Zoho by that person, not by this skill or `crm-update`.

## Generation — unconditional as of v2.3

For all qualified leads: generate `Email_Personalised_Opening`, `Email_Pain_Points`, **and** the merged `LinkedIn_Message` content (connect message plus follow-up, in the two-part format), regardless of the `LinkedIn Status` value. `LinkedIn Status` still controls priority/sequencing for the manual outreach process, and it's still a real, meaningful decision — it just no longer withholds content. On an update to an existing record, don't overwrite valid LinkedIn content already sitting there from a prior cycle with a lower-effort regeneration; regenerate fully or leave it as-is.

---

# SALESHANDY TEMPLATE COMPATIBILITY

The live Saleshandy templates control the overall email structure, and they are the real, binding spec for how every field this skill produces actually gets read — checked directly against all five campaigns' live templates on August 11, 2026, not assumed from the field names.

**Four fields this skill touches or feeds end up merged into live templates, not just stored in Zoho:** `Email_Personalised_Opening`, `Email_Pain_Points`, `Business_Challenges` (Saleshandy label: `Business Challenge`, singular — a naming mismatch to be aware of, not a different field), and `Case_Study` (Saleshandy label: `Case Study`). All four need the same "reads like something a person typed" bar — a fabricated or awkward Business Challenges or Case Study value is just as visible to the prospect as a bad Opening.

The first email in every sequence looks roughly like this:

```
Hi {{First Name}},

{{Email Personalised Opening}}

{{Email Pain Points}}

[Existing Zediant campaign messaging]
[Existing CTA]
[Existing signature]
```

But `Email_Pain_Points` and `Case_Study`/`Business_Challenges` don't stop there — every campaign reuses `Email_Pain_Points` a second time in a later follow-up, and `Business_Challenges`/`Case_Study` appear in a dedicated proof-point email, in the grammatical forms documented in Steps 7 and 9 above. This skill's output for all four fields never includes: the greeting line, a subject line, a signature, a sign-off, a full email, a duplicate CTA, a duplicate Zediant introduction, or additional paragraphs that belong to the Saleshandy template. Each field is an independent, self-contained content block that has to make sense wherever the live template drops it in — including the second, later placement, without the other fields present alongside it.

---

# WRITING STYLE — write like a human, not like an AI

Every generated field (Opening, Pain Points, the connect message, the follow-up message, and Business Challenges/Case Study when this skill touches them) must read as something a person actually typed. Concretely: no em dashes, no en dashes used as a substitute for a comma or period, no other AI-typical punctuation tics. Use plain commas, periods, and ordinary sentence structure instead. This is a hard requirement checked at Validation and again by `crm-update` before the write — if a generated field contains one, rewrite it rather than leaving it for the next skill to catch.

---

# PERSONALIZATION RULES

| Rule | What it actually prevents |
|---|---|
| **Never fabricate a fact.** | Don't invent a funding round, a headcount, a product launch, or a quote that wasn't actually found. If a search came back empty, say so rather than writing something plausible-sounding |
| **Never pretend to know internal company information.** | Frame observations as external inference ("your careers page shows...") not internal knowledge |
| **Never over-personalize.** | Professional and company-level detail is fair game. Personal-life detail reads as invasive and measurably hurts reply rates |
| **Never mention information that cannot be verified.** | Either verify it before using it or note the uncertainty rather than stating it as fact |
| **Never cite a statistic from the "Unsubstantiated performance claims" table in `services.md`.** | Those numbers aren't backed by evidence Zediant can defend if a prospect asks |

---

# VALIDATION

Before returning output, confirm:

- Every fact in the Opening and Pain Points is traceable to something actually found, not inferred from industry stereotype
- The Relevant Service genuinely addresses the confirmed Business Challenge, per `services.md`
- The Case Study respects its confidentiality tier and doesn't repeat the CS-02/CS-06 double-count
- No statistic from `services.md`'s Unsubstantiated performance claims table appears anywhere in the output
- Opening, Pain Points, and both halves of the LinkedIn Message & Follow-up field contain **no em dash, en dash, or other AI-typical special character**
- Opening and Pain Points meet their word-count ranges (25-45 words each); the connect message is 40-70 words; the follow-up is 35-60 words
- The connect message does not copy the email or the Opening; the follow-up does not copy the connect message or the email
- The follow-up does not use "just following up" or equivalent
- The merged LinkedIn field uses the CONNECT / FOLLOW-UP two-part format, nothing else
- `LinkedIn Status` reflects a genuine batch-level priority ranking, not "has a LinkedIn URL" or first-25 selection
- **The merged LinkedIn field was generated for every qualified lead in the batch, independent of `LinkedIn Status`** — a `Not Required` lead with a blank `LinkedIn_Message` field is a defect, not an expected outcome, as of v2.3
- `Case_Study` is either an approved, real case study or blank — never fabricated
- All content fields trace back to the same single Trigger → Pain Point → Zediant Relevance angle, and to the same `Business_Challenges` value where relevant
- `Email_Pain_Points` makes complete sense read in isolation, with no demonstrative pronoun ("that," "this," "such a shift") whose antecedent only exists in `Email_Personalised_Opening` — it gets reused alone in a later follow-up email
- `Case_Study` (where populated) is one self-contained, standalone sentence, not a noun phrase or fragment — it merges directly into a live Saleshandy template as its own line in four of five campaigns

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
[Written exactly as it should be stored in Email_Personalised_Opening]

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
CONNECT: / FOLLOW-UP: two-part format]

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

If the user explicitly asks for a full email draft rather than variables, produce it using the selected campaign's documented tone and CTA, but say plainly that this is outside the skill's normal output and that the live Saleshandy template remains the source of truth for anything actually sent.

---

# EXCEPTION HANDLING

| Situation | Action |
|---|---|
| Insufficient company information exists even after a genuine search | Fall back to industry-level messaging, say so explicitly, reflect it in a Low or Medium Confidence Score |
| No case study genuinely fits | Say "no strong match" rather than stretching a mismatched story |
| Technology stack is unknown | Avoid technical assumptions in the Opening or Relevant Service — a wrong technical guess is worse than a generic angle |
| Recent news or LinkedIn data can't be verified from a second source | Either drop it or note the uncertainty explicitly |
| A generated field contains an em dash or similar AI-typical character | Rewrite it before returning output — don't ship it and rely on `crm-update` to catch it |
| Fewer than ~15 leads in a batch genuinely qualify for `Ready to Connect` | Flag fewer than 25 as `Ready to Connect`. Don't lower the bar to hit the target number. Every lead still gets LinkedIn content generated regardless |
| More than ~35 leads in a batch genuinely qualify | Still narrow the `Ready to Connect` flag to approximately the top 25 by ranking — flag that the batch was unusually strong rather than marking all of them `Ready to Connect`. Every lead still gets LinkedIn content generated regardless |
| Batch is large enough that generating LinkedIn content for every lead in one pass is genuinely impractical | Prioritize by PTB Score, generate as many as practical, and explicitly list which leads' LinkedIn content is still outstanding — don't silently leave gaps that look like coverage |
| No LinkedIn profile found for a contact | Still generate the LinkedIn Message & Follow-up content from the same angle — the content isn't gated on profile availability, only the `Ready to Connect` priority decision considers profile availability/relevance |

---

# ESCALATION

Escalate to a human rather than finalizing personalization:

- Manual research is genuinely required beyond what a reasonable search can surface
- Company information conflicts across sources and no source is clearly more reliable
- Industry is unknown or not covered by `icp.md`
- **High-value enterprise account** — PTB Score of 90 or above (Excellent Opportunity) — have a human sanity-check the angle before it goes out
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
| Generated content containing em dashes or other AI-typical special characters | Zero |
| LinkedIn Status selections based on batch ranking rather than quota or profile-presence alone | 100% |
| Merged LinkedIn Message & Follow-up content generated for every qualified lead, regardless of `LinkedIn Status` | 100% |
| `Not Required` leads left with a blank `LinkedIn_Message` field | Zero — this is now a defect, reversed from the pre-v2.3 target |
| `Case_Study` containing a fabricated case study | Zero |
| Reply rate lift attributable to personalization quality | Tracked, not yet targeted |

---

# VERSION

Version 2.3 · Owner: Zediant AI Sales Team · August 12, 2026

**Changes in V2.3 — LinkedIn content generation decoupled from LinkedIn Status:**
- Reversed the prior behavior where `LinkedIn_Message` was only generated for `Ready to Connect` leads and left blank for `Not Required` leads. As of this version, **every qualified lead gets LinkedIn Message & Follow-up content generated (Step 11)**, using the same Step 5 angle already produced for the Email channel — no additional research pass required
- `LinkedIn Status` (`Ready to Connect` / `Not Required`) is now explicitly documented as a **priority/sequencing flag only** — it tells the BDM and the manual LinkedIn execution process which ~25 of every ~100 leads to actively work first. It no longer gates whether content exists
- Section 4 rewritten to separate "what gets generated" (everyone) from "what gets prioritized for active outreach" (~top 25) — these were previously conflated into a single gate
- Updated Validation, Exception Handling, Output Format, Related Skills, and Success Criteria to match — a blank `LinkedIn_Message` on a `Not Required` lead is now a defect to catch, not an expected outcome
- Added guidance for the edge case where generating LinkedIn content for an entire large batch in one pass is impractical: prioritize by PTB Score and explicitly disclose which leads are still outstanding, rather than silently leaving gaps
- Rationale: real-world use showed `Not Required` leads had no LinkedIn content sitting ready when priority later shifted (new signal, BDM manual pickup, batch re-ranking), forcing a full skill re-run for a single lead. Generating up front removes that gap at effectively no extra research cost, since the single outreach angle underlying both channels is already built for the Email fields regardless of LinkedIn Status

**Changes in V2.2 — grammatical fit against the live Saleshandy templates:**
- Pulled and reviewed the actual live template content for all five campaigns' active sequence steps (not assumed from field names) to find where each merge tag really lands
- Added a hard requirement to Step 9: `Email_Pain_Points` must read as fully self-contained, with no demonstrative back-reference to `Email_Personalised_Opening` — every campaign reuses Pain Points a second time in a later follow-up email where the Opening is not present, and a dangling "like that" or "this shift" only makes sense in the first placement
- Added a hard requirement to Step 7: `Case_Study` must be one standalone, self-contained sentence — it merges directly into a live template as its own line in four of five campaigns; noted the one accepted exception (C5's final message) as a known limitation, not something to design around
- Rewrote the Saleshandy Template Compatibility section, which previously described only `Email Personalised Opening`/`Email Pain Points` as merge-tag-facing. It was stale: `Business_Challenges` and `Case_Study` are also live merge tags (`{{Business Challenge}}`, `{{Case Study}}`), reused in a second location each, and subject to the same human-sounding, grammatically-correct bar
- Companion fix: `Business_Challenges`' own dual-use grammatical requirement (standalone sentence vs. subordinate clause after "Given" in C1) is now documented at its actual authoring point, `lead-qualification` Step 6 (v1.3), since that skill's wording carries forward unedited — this skill reads the value rather than rewriting it, so the rule lives there, not here
- Companion fix: `saleshandy-distribution` v1.6 now actually pushes `Case_Study`/`Business_Challenges` as Saleshandy merge variables — previously the live templates referenced `{{Case Study}}`/`{{Business Challenge}}` but the push payload never sent them, so those fields rendered blank in any email that reached those steps

**Changes in V2.1 — Case Study/Business Challenges fields, LinkedIn field merge:**
- `Business_Challenges` is now a real CRM field, carried forward from `lead-qualification`'s Step 6 finding — this skill reads it as a required input for Email Pain Points rather than re-deriving a challenge
- `Case_Study` is now a real CRM field (Step 7 rewritten) — selection is driven by the confirmed Business Challenges, not shared industry alone, and the no-fabrication rule is absolute: blank is the correct output when nothing approved fits
- `LinkedIn_Follow_up` deleted from Zoho. Steps 11-12 merged into one step generating both the connect message and the follow-up, written into the single `LinkedIn_Message` field (relabeled LinkedIn Message & Follow-up) using a CONNECT/FOLLOW-UP two-part format
- Output Format, Validation, Related Skills, and Success Criteria updated to match

**Changes in V2.0 — LinkedIn outreach:**
- Added the full LinkedIn Selection Strategy (Section 4): batch-level ranking to approximately the top 25 of every ~100, eligibility and not-required criteria, and the two-value-only status rule
- Added LinkedIn Message and LinkedIn Follow-up generation, originally gated on `LinkedIn Status = Ready to Connect` (reversed in V2.3 — see above)
- Replaced the old Opening Observation / Business Challenge / Subject Line / CTA / Follow-up Angle / merge-variable model with the current Zoho fields: `Email_Personalised_Opening`, `Email_Pain_Points`, `LinkedIn_Message`, `LinkedIn_Follow_up`
- Replaced stale references to the prior sending platform with Saleshandy, and List B/List C campaign references with C1-C5, to match `campaign-selection` v2.0 and `crm-update` v4.0
- Added the "write like a human" rule: no em dashes or other AI-typical special characters in any generated field, checked at Validation
- Introduced the single Trigger → Pain Point → Zediant Relevance angle requirement feeding all four content fields

This skill still does not decide tone, angle category, or CTA — those are read from `campaigns.md`. Its job is finding the real, verifiable fact that makes the campaign's generic angle true of one specific company, deciding that company's LinkedIn outreach priority, and packaging Email plus LinkedIn content for every qualified lead as field-ready content rather than prose.
</content>

