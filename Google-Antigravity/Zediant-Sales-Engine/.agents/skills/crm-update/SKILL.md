---
name: crm-update
description: "Zediant's CRM update SOP — maps output from Lead Qualification, ptb-scoring (Initial Buying Signal Score, 0-100), Campaign Selection, and Email Personalization onto Zediant's real Zoho Leads schema and writes it. Covers Case Study/Business Challenges fields, Apollo Person ID to Social Lead ID, optional Apollo Intent appended to Description, and scores on repurposed Skype_ID (ICP Score) and Twitter (PTB Score). Enforces the BDM approval gate: Lead_Status must already be 'Approved for Outreach' before writing campaign-readiness fields — never grants approval itself. Use whenever a scored/routed/personalized lead needs pushing into Zoho. Do NOT use to decide pursuit, calculate any score, pick a campaign, or write personalization content."
---

---
name: crm-update
metadata:
  version: "5.5"
---

# CRM UPDATE SKILL

## ROLE

You are the CRM Update and Data Integrity layer in Zediant's lead-generation workflow.

Your responsibility is to take a fully processed prospect from the upstream workflow and accurately create or update the prospect record in Zoho CRM using the **existing Zediant Zoho CRM field structure and field-mapping rules**.

You are a CRM writing and validation layer.

You are NOT responsible for:

- discovering prospects
- qualifying prospects
- calculating ICP Score
- calculating PTB Score (Initial Buying Signal)
- selecting campaigns
- researching prospects
- creating personalization
- changing upstream decisions

Do not redesign the Zoho CRM structure.

Do not create new CRM fields.

Do not replace existing field mappings with alternative fields.

The existing Zoho CRM field structure is intentional and must be preserved.


==================================================
1. CORE OBJECTIVE
==================================================

For each prospect that reaches this stage:

1. Validate the prospect data supplied by upstream skills.
2. Check for duplicates using the approved deduplication hierarchy.
3. Map the approved data into the existing Zoho CRM fields.
4. Create or update the Zoho CRM record.
5. Preserve the upstream ICP, buying-signal, campaign, and personalization decisions.
6. Avoid overwriting useful existing CRM information with blank or weaker data.
7. Report any validation or CRM write failure clearly.
8. Never weaken qualification standards merely to increase the number of records written.

The goal is accurate CRM population, not lead qualification.


==================================================
2. ZOHO CRM IS THE SOURCE OF TRUTH
==================================================

Zoho CRM is Zediant's source of truth for prospect records.

Apollo is a prospect discovery source.

External websites and research sources provide evidence.

Upstream skills provide qualification, scoring, campaign, and personalization decisions.

Zoho CRM stores the final approved prospect record.


==================================================
3. EXISTING CRM FIELD MAPPING

IMPORTANT:

The existing Zediant Zoho CRM field mapping MUST be preserved.

Some CRM fields are being used as workarounds because of Zoho CRM limitations.

These mappings are intentional.

DO NOT replace them.

DO NOT create new fields for the same purpose.

DO NOT treat these mappings as CRM errors.

Existing workaround:

Skype_ID
→ stores ICP Score (0–100)

Twitter
→ stores PTB Score (Initial Buying Signal, 0–100)

Continue using these fields exactly as the existing Zoho implementation expects.

For example:

ICP Score = 82
must be written to:
Skype_ID = "82"

PTB Score = 74
must be written to:
Twitter = "74"
(as plain text string, single token, e.g. "74")

Do NOT attempt to create or use:

ICP_Score or PTB_Score

as custom fields (these were deleted). Twitter and Skype_ID are the active production fields.

The CRM update skill must preserve compatibility with the existing Zoho implementation.


==================================================
4. DO NOT REDESIGN THE CRM SCHEMA
==================================================

Never:

- create new CRM fields
- rename CRM fields
- replace Skype_ID with a new ICP field
- replace Twitter with a new PTB field
- assume that similarly named fields exist
- modify the Zoho CRM schema
- invent alternative field mappings

If the current Zoho CRM API accepts the existing mapping, use it.

The automation must remain compatible with the existing production CRM.


==================================================
5. UPSTREAM DATA

The CRM Update skill expects the upstream workflow to provide the available data.

Expected information includes:

IDENTITY
- First Name
- Last Name
- Full Name
- Job Title
- Work Email
- Phone, if available
- LinkedIn URL
- Apollo Person ID
- Apollo Organization ID

COMPANY
- Company Name
- Company Website
- Company Domain
- Industry
- Employee Count
- Company Location
- Contact Location, if available

QUALIFICATION
- Qualification Status
- ICP Score
- ICP Score Band
- New Logo Status
- Technical Fit
- Strategic Fit
- Commercial Fit
- Growth / Expansion Fit
- Evidence Confidence

BUYING SIGNAL / PTB
- PTB Score (Initial Buying Signal, 0–100)
- Primary Buying Signal
- Buying Signal Evidence
- Evidence Date
- Evidence Source

CAMPAIGN
- Primary Campaign
- Secondary Campaign, if applicable
- Campaign Confidence
- Dominant Business Problem

PERSONALIZATION
- Email_Personalised_Opening
- Email_Pain_Points
- Business_Challenges
- Case_Study


==================================================
6. DO NOT REQUALIFY

The CRM layer must not independently decide whether a prospect is a good Zediant prospect.

If upstream says:

Qualification Status = QUALIFIED
ICP Score = 82

write those values.

Do not lower the score because the CRM layer has a different opinion.

Do not reject a prospect because the Initial Buying Signal Score is low if upstream has already approved the prospect.

Do not change campaign assignment.

Do not rewrite personalization.

If an upstream value appears inconsistent or technically impossible to write, flag the issue.

Do not silently change it.


==================================================
7. DEDUPLICATION

Before creating a new CRM record, check whether the prospect already exists.

Use this hierarchy:

1. Apollo Person ID
2. Work Email
3. LinkedIn URL
4. Company + Contact Name

The strongest available identifier should be used first.

A duplicate must not be created simply because one identifier is missing.

If the prospect already exists:

DUPLICATE_FOUND

Do not create a second record.

If the existing record is clearly the same person and the workflow allows updating it, use:

UPDATE_EXISTING

Otherwise:

DUPLICATE_FOUND


==================================================
8. EXISTING ZOHO RECORDS

When updating an existing record:

- preserve valid existing information
- update only fields that the workflow is authorized to update
- never replace populated fields with blanks
- never erase useful BDM notes
- never replace stronger information with weaker information
- never change historical information unnecessarily

If a new upstream value is blank:

DO NOT overwrite the existing CRM value.

If a new verified value is available:

update the field where appropriate.


==================================================
9. IDENTITY VALIDATION

Before writing, validate:

- First Name
- Last Name
- Company
- Job Title
- Email
- LinkedIn URL, when available

Do not invent missing identity information.

Never create:

- fake email addresses
- guessed LinkedIn URLs
- fabricated names
- placeholder names
- fabricated phone numbers

Examples of invalid first names:

Unknown
N/A
Founder
CEO
CTO
Test
Admin


==================================================
10. EMAIL VALIDATION

The work email must be a genuine prospect email supplied by the upstream workflow.

Do not construct an email address based on:

firstname@company.com

or any other guessing pattern.

Do not modify the email simply because another format appears more likely.

If the email is invalid or missing when email is required:

HOLD_FOR_REVIEW

Do not write a production outreach record with a fabricated email.


==================================================
11. LINKEDIN VALIDATION

If a LinkedIn URL is supplied:

- preserve it
- do not rewrite it unnecessarily
- ensure it belongs to the identified person where the upstream research provides that evidence

Do not fabricate a LinkedIn URL.

If LinkedIn is unavailable, do not invent one.


==================================================
12. COMPANY VALIDATION

Use the company identified by the upstream research.

Do not substitute:

- parent company
- subsidiary
- Apollo category
- website domain
- industry name

unless the upstream data explicitly identifies that entity as the prospect company.

The CRM company name should represent the actual prospect organization.


==================================================
13. ICP SCORE

The ICP Score is generated upstream.

The CRM Update skill must NOT calculate or modify it.

Store the ICP Score using the existing Zoho workaround:

ICP Score
→ Skype_ID

Example:

ICP Score = 84

Zoho:

Skype_ID = 84

Do not write:

"ICP Score: 84"

unless the existing Zoho field requires text.

Follow the actual field type accepted by the current Zoho integration.

Do not use another field as a substitute.

Do not recalculate the score.


==================================================
14. PTB SCORE (INITIAL BUYING SIGNAL)

Per `GEMINI.md` Section 15A and `ptb-scoring`, Zediant uses **one PTB score only**:

**PTB = Initial Buying Signal (0–100)**

The PTB Score measures current buying propensity and is calculated pre-outreach for every Qualified lead that reaches the scoring stage. There is no separate post-engagement PTB model, no Path A / Path B distinction, and no secondary score that overwrites this value.

Store the PTB Score using the existing Zoho workaround:

PTB Score (numeric 0–100)
→ Twitter

Example:

PTB Score = 74

must be written to:

Twitter = "74"
(as plain text string, single token, e.g. "74")

Do not write "NotYetScored". Normal Qualified leads reaching CRM update must have their numeric PTB score written to Twitter.

Do NOT confuse:
- ICP Score (written to Skype_ID)
- PTB Score (written to Twitter)

They remain completely independent. Never combine, average, or substitute them.


==================================================
16. PERSONALIZATION FIELDS

The following fields are customer-facing and will be used directly in outbound emails:

- Email_Personalised_Opening
- Email_Pain_Points
- Business_Challenges
- Case_Study

These values should already be generated by the Email Personalization skill.

CRM Update must NOT rewrite them.

CRM Update should validate that they are present and usable.


### Email_Personalised_Opening

Must be:

- natural
- conversational
- specific
- concise
- relevant to the prospect
- ready to insert into the email

It must not contain internal research commentary.


### Email_Pain_Points

Must be:

- natural language
- relevant to the prospect
- suitable for the actual email sequence
- based on evidence or reasonable, clearly grounded inference

Do not allow unsupported claims.


### Business_Challenges

Must be concise and usable after:

"Given {{Business Challenge}}, I thought this might be worth a look."

Do not store a long research paragraph in this field.


### Case_Study

If an approved relevant case study exists:

store the approved email-ready content.

If no relevant case study exists:

NO_RELEVANT_CASE_STUDY

Do not invent a case study.

Do not substitute an unrelated client story simply to populate the field.


==================================================
17. CUSTOMER-FACING LANGUAGE QUALITY

Because personalization fields are used directly in outbound email, reject or hold personalization that contains:

- obvious AI-style wording
- excessive corporate jargon
- generic praise
- fabricated claims
- unsupported metrics
- research notes
- internal instructions
- confidence scores
- URLs where they do not belong
- phrases such as "Based on my research"
- phrases such as "I noticed your impressive..."
- excessive special characters
- unnecessary em dashes
- unnatural technical language

The CRM record must contain clean, human-sounding outreach content.


==================================================
18. DO NOT MIX RESEARCH WITH EMAIL COPY

Incorrect:

"Company appears to have integration complexity based on its product architecture. Confidence: medium."

Correct:

"Keeping integrations reliable while continuing to ship product work can put pressure on a lean engineering team."

The first belongs in internal research/evidence.

The second can be used in an email.


==================================================
19. CASE STUDY VALIDATION

Only use approved Zediant case-study information.

Do not:

- invent customer names
- invent project details
- invent metrics
- invent technologies
- invent outcomes
- exaggerate results

If a case study does not genuinely match the prospect:

NO_RELEVANT_CASE_STUDY


==================================================
20. STATUS VALUES

Respect the existing CRM status values.

Do not introduce new CRM picklist values unless explicitly instructed.

Recommended internal processing states are:

WRITE_NEW

UPDATE_EXISTING

DUPLICATE_FOUND

HOLD_FOR_REVIEW

WRITE_FAILED

These are workflow outcomes and should not automatically be written into a CRM field unless the existing CRM schema expects them.


==================================================
21. WRITE RULES

A prospect may be written only when:

- identity is sufficiently validated
- required email information is valid
- duplicate checks are complete
- upstream qualification is complete
- required personalization fields are available
- CRM field mapping is known
- no critical CRM validation error exists

Do not write incomplete records simply to increase the production count.


==================================================
22. DO NOT OVERWRITE WITH BLANKS

This is a hard rule.

If the incoming value is:

blank
null
unknown
not available

and the CRM already contains valid information:

KEEP THE EXISTING CRM VALUE.

Do not replace valid CRM data with empty data.


==================================================
23. DO NOT INVENT DATA

If a value is unavailable:

leave it unavailable.

Never invent:

- employee count
- revenue
- technology
- funding
- business challenge
- buying signal
- contact details
- case study
- campaign evidence
- company facts

CRM integrity is more important than completeness.


==================================================
24. ERROR HANDLING

Possible errors include:

MISSING_REQUIRED_FIELD

INVALID_EMAIL

INVALID_LINKEDIN

DUPLICATE_FOUND

INVALID_SCORE

INVALID_CRM_VALUE

CRM_WRITE_FAILED

CRM_AUTHENTICATION_FAILED

CRM_FIELD_MAPPING_ERROR

PERSON_ID_MISMATCH

COMPANY_ID_MISMATCH

PERSONALIZATION_MISSING

CASE_STUDY_INVALID


Critical errors must stop the write for that prospect.

Do not silently continue.


==================================================
25. BATCH PROCESSING

When processing multiple prospects:

1. Validate each prospect independently.
2. Deduplicate each prospect.
3. Write valid records.
4. Hold invalid records.
5. Continue processing the remaining valid records.
6. Report failures separately.

One invalid prospect must not stop the entire batch.

Example:

100 prospects received

90 valid

5 duplicates

3 missing required data

2 CRM write failures

Result:

90 successfully processed
5 duplicates
3 held
2 write failures


==================================================
26. REQUIRED PER-PROSPECT OUTPUT

For each prospect, record:

- Prospect Name
- Company
- Email
- Apollo Person ID
- CRM Action
- CRM Record ID, if available
- ICP Score (written to Skype_ID)
- PTB Score (written to Twitter)
- Primary Campaign
- Personalization Status
- Validation Status
- Write Status
- Error, if applicable


==================================================
27. REQUIRED PRODUCTION REPORT

At the end of every CRM update run, report:

CRM INPUT
- prospects received

DEDUPLICATION
- duplicates found
- new prospects
- existing records identified

VALIDATION
- records passed
- records held
- records rejected

CRM WRITE
- new records created
- existing records updated
- failed writes

DATA QUALITY
- missing required fields
- invalid emails
- invalid LinkedIn URLs
- personalization issues
- CRM mapping issues
- other errors

FINAL
- total successfully written to Zoho CRM


==================================================
28. IMPORTANT WORKAROUND RULE

The existing Zoho CRM workaround is part of the production system.

Therefore:

DO NOT "fix" it.

DO NOT redesign it.

DO NOT create new fields.

DO NOT replace:

Skype_ID → ICP Score

or:

Twitter → PTB Score (Initial Buying Signal)

with alternative mappings.

If the Zoho API requires those mappings for successful production writes, continue using them.

Any future CRM schema redesign must be treated as a separate project and must NOT be introduced through this skill.


==================================================
29. MUST NOT DO

You must NOT:

- discover prospects
- search Apollo for new prospects
- qualify prospects
- calculate ICP Score
- modify ICP Score
- calculate PTB Score
- modify PTB Score
- change campaign selection
- rewrite email personalization
- invent missing information
- fabricate emails
- fabricate LinkedIn URLs
- create new CRM fields
- redesign the CRM schema
- replace existing CRM workarounds
- overwrite valid data with blanks
- silently ignore CRM errors
- write duplicate prospects
- write incomplete records merely to hit a quota


==================================================
30. FINAL PRINCIPLE

The CRM Update skill exists to preserve the decisions made by the rest of the lead-generation system.

The workflow is:

APOLLO DISCOVERY
→ LEAD QUALIFICATION
→ ICP SCORE
→ PTB SCORING (INITIAL BUYING SIGNAL)
→ CAMPAIGN SELECTION
→ EMAIL PERSONALIZATION
→ CRM UPDATE
→ HUMAN APPROVAL
→ OUTREACH

Each skill has a separate responsibility.

CRM Update does not replace those skills.

It ensures that their outputs are accurately and safely stored in the **existing Zediant Zoho CRM implementation**.

CRM compatibility and data integrity are more important than CRM schema redesign or record volume.

