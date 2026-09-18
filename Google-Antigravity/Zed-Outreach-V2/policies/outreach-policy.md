# Zediant Revenue Engine — Outreach Policy

Version: 1.0
Status: Active

---

# 1. PURPOSE

This policy governs the process from qualified prospect to approved
outreach.

It applies to:

- Apollo lead acquisition
- lead qualification
- PTB scoring
- campaign selection
- email personalization
- LinkedIn personalization
- Zoho CRM updates
- BDM approval
- Apollo outreach
- reply handling
- follow-up activities

The purpose is to ensure that no prospect enters outbound outreach
without meeting the required qualification, data-quality and approval
conditions.

---

# 2. OUTREACH PRINCIPLE

The Revenue Engine follows:

RESEARCH
→ QUALIFY
→ SCORE
→ SELECT CAMPAIGN
→ PERSONALIZE
→ APOLLO CONTACT CUSTOM FIELDS ENRICHMENT
→ HUMAN APPROVAL IN APOLLO
→ APOLLO OUTREACH
→ RESPONSE RECEIVED
→ ZOHO CRM SYNC (LEAD_STATUS = 'ENGAGED')

AI must not bypass the human approval gate.

---

# 3. APOLLO RESPONSIBILITY

Apollo is used primarily for:

- lead discovery
- company discovery
- contact discovery
- firmographic research
- technology research
- intent signals where available
- prospect enrichment

Apollo is not the system of record.

Apollo must not be treated as the final authority for:

- outreach approval
- campaign approval
- CRM status
- commercial decisions

Zoho CRM remains the system of record.

---

# 4. DUPLICATE CHECK

Before a new lead is considered for outreach:

1. Check Zoho CRM.
2. Determine whether the lead already exists.
3. Determine whether the company already exists where applicable.
4. Apply the current duplicate policy.
5. Do not create another record merely because Apollo found the prospect.

Existing Zoho leads must be excluded according to the active duplicate
policy.

---

# 5. QUALIFICATION

Lead qualification must use:

`context/icp.md`

and:

`skills/qualification/lead_qualification.md`

Do not create a qualification rule inside the outreach Skill that
contradicts the ICP source.

The qualification process should determine whether the prospect is a
reasonable Zediant ICP fit.

---

# 6. PTB / BUYING SIGNAL

PTB scoring should use:

`skills/qualification/ptb_scoring.md`

PTB score is an input into prioritization and campaign decisions.

PTB score does NOT equal:

APPROVED FOR OUTREACH

A high PTB score does not remove the human approval requirement.

---

# 7. CAMPAIGN SELECTION

Campaign selection must use:

`context/campaigns.md`

and:

`skills/campaign/campaign_selection.md`

The active campaign taxonomy is:

C1 — AI-Enabled Product Engineering

C2 — Engineering Pods / Staff Augmentation

C3 — Platform / Cloud / Infrastructure Engineering

C4 — Integration / API / Middleware Engineering

C5 — Legacy / Enterprise Modernisation

Campaign selection must be based on the prospect's dominant business
problem and available evidence.

Do not assign a campaign based only on company industry.

---

# 8. PERSONALIZATION

Personalization must use:

`skills/personalization/email_personalization.md`

Personalization must be:

- evidence-based
- concise
- relevant
- human sounding
- specific where evidence permits

Do not manufacture:

- hiring plans
- technology initiatives
- business challenges
- funding events
- product launches
- expansion plans
- engineering problems

If the evidence is weak:

use neutral personalization or leave the field empty rather than
inventing a statement.

---

# 9. REQUIRED CRM PERSONALIZATION FIELDS

Before a lead becomes eligible for outreach, the required personalization
fields defined by the current Zoho schema must be validated.

These may include fields such as:

- Email Personalised Opening
- Email Pain Points
- Case Study
- Business Challenges

The exact field names and required status must be determined from:

`skills/crm-update.skill` — FIELD MAPPING section

Do not assume a field is mandatory if the current schema does not say so.

Do not invent values merely to satisfy a required field.

If a mandatory field cannot be responsibly populated:

DATA GAP

---

# 10. EMAIL QUALITY

Before outreach approval, email content should be checked for:

- relevance
- accuracy
- personalization
- grammar
- clarity
- length
- unsupported claims
- inappropriate sales language
- incorrect customer assumptions
- case-study restrictions
- commercial commitments

The objective is to create credible and human-sounding outreach.

---

# 11. LINKEDIN QUALITY

LinkedIn messages must follow the same evidence and confidentiality
requirements as email.

Do not reveal:

- internal scoring
- internal research
- CRM notes
- confidential customer information
- internal commercial information

LinkedIn personalization should be appropriate for a direct prospect
interaction.

---

# 12. HUMAN APPROVAL GATE

This is a mandatory control point.

AI may prepare:

- lead
- qualification
- ICP score
- PTB score
- campaign
- personalization
- LinkedIn message
- CRM values
- outreach recommendation

AI must NOT infer human approval from these values.

The lead becomes eligible for outbound sending only when the required
human approval has been explicitly recorded.

---

# 13. APPROVAL STATE

The system must distinguish between:

NOT REVIEWED

REVIEWED

APPROVED FOR OUTREACH

REJECTED

Do not treat:

REVIEWED

as:

APPROVED FOR OUTREACH.

Do not treat:

HIGH ICP SCORE

as:

APPROVED FOR OUTREACH.

Do not treat:

HIGH PTB SCORE

as:

APPROVED FOR OUTREACH.

---

# 14. REJECTION

If a BDM rejects a lead:

Do not automatically re-add it to the same outreach workflow.

Respect the rejection decision.

If the prospect is reconsidered later because new evidence materially
changes the situation:

record the new reason and require the appropriate review again.

---

# 15. APOLLO OUTREACH & RESPONSE GATE

Apollo is the active outbound execution and prospect intelligence platform.

A prospect may be added to an Apollo sequence only when the required
outreach approval state has been achieved in Apollo (`Approval Status = "Approved for Outreach"`).

Conceptually:

Apollo Contact
→ Approval Status = "Approved for Outreach"
→ Target Segment
→ Campaign Registry
→ Apollo Sequence
→ Outreach Send
→ Response Received
→ Zoho CRM Lead Creation (`Lead_Status = "Engaged"`)
→ Apollo Sync (`Zoho Record ID`, `Zoho Sync Status = "Synced"`)

Leads are added to Zoho CRM ONLY upon receiving a response. Cold uncontacted leads remain in Apollo.

---

# 16. APOLLO CAMPAIGN MAPPING

Do not hard-code business campaign logic around Apollo sequence IDs.

Use:

`context/campaigns.md` — LIVE CAMPAIGN REGISTRY section

The registry should map:

Zediant Campaign
→ Apollo Sequence

If the required Apollo sequence mapping does not exist:

DATA GAP

Do not guess the sequence.

---

# 17. SENDER SELECTION

Sender selection must follow:

`context/campaigns.md` — LIVE CAMPAIGN REGISTRY section

Do not randomly select a sender.

Do not infer sender ownership from previous campaigns.

If the sender mapping is missing or ambiguous:

DATA GAP

---

# 18. OUTREACH VOLUME

Lead volume targets are operational goals, not a reason to lower
qualification standards.

For example:

A target of 100 leads per day does NOT mean:

"Find 100 leads regardless of quality."

If only 45 leads meet the required standards:

return 45 qualified leads.

Quality must not be sacrificed to meet an indicative volume target.

---

# 19. EMAIL SEQUENCE

Email sequences must follow the active campaign configuration.

Do not invent new sequence steps simply because a prospect has not
responded.

Follow the current Apollo campaign configuration.

---

# 20. FOLLOW-UP

Follow-ups must respect:

- campaign sequence
- sending schedule
- opt-out status
- reply status
- customer engagement
- negative response
- meeting status

Do not continue automated outreach after a clear opt-out or equivalent
stop condition.

---

# 21. REPLIES

When a prospect replies:

The outreach workflow must recognize that the prospect has engaged.

Do not continue blindly sending the normal sequence if the reply
requires a different response.

Reply handling should move toward:

Apollo
→ Reply Classification
→ CRM Update
→ Appropriate Human / Sales Action

---

# 22. POSITIVE REPLY

A positive or potentially interested reply should be treated as a sales
engagement event.

Where appropriate:

1. Stop or adjust the normal outbound sequence.
2. Classify the reply.
3. Update Zoho.
4. Identify the next action.
5. Notify the appropriate human.
6. Continue according to the sales process.

Do not assume a positive reply automatically means:

QUALIFIED OPPORTUNITY

Qualification may still be required.

---

# 23. NEGATIVE REPLY

If a prospect clearly declines:

- respect the response
- stop inappropriate follow-up
- update the appropriate CRM status
- do not repeatedly re-enter the prospect into the same campaign without
  a legitimate new reason

---

# 24. UNSUBSCRIBE / OPT-OUT

A clear unsubscribe or opt-out request must be respected.

Do not continue outbound email after a valid opt-out.

Where the available system supports suppression or unsubscribe status,
use the appropriate mechanism.

If the correct suppression mechanism is unclear:

STOP

and request human/system review.

---

# 25. LINKEDIN AUTOMATION

LinkedIn activity must not be represented as fully autonomous unless
the active connected platform explicitly supports and authorizes the
specific action.

Where Apollo creates a LinkedIn task that requires human
execution:

treat it as a HUMAN TASK.

Do not claim that Claude has automatically sent the LinkedIn action unless
the connector confirms that the action was actually executed.

---

# 26. OUTREACH STATUS

Use explicit states.

Examples:

NOT READY

READY FOR REVIEW

APPROVED FOR OUTREACH

SCHEDULED

ACTIVE

REPLIED

MEETING

PAUSED

REJECTED

OPTED OUT

COMPLETED

Do not infer status from the existence of a record alone.

---

# 27. CRM WRITE RESPONSIBILITY

`crm_update.md` owns business-process CRM writes.

The outreach Skills may prepare data but should hand CRM updates to the
CRM write process.

Do not duplicate Zoho write logic across:

- Apollo Skill
- qualification Skill
- campaign Skill
- personalization Skill
- Apollo Skill

---

# 28. DATA PRESERVATION

Before updating a CRM outreach field:

1. Read the existing value.
2. Determine whether it is still valid.
3. Determine whether new evidence justifies replacement.
4. Update only when appropriate.

Do not overwrite valid human-entered information unnecessarily.

---

# 29. OUTREACH SAFETY CHECK

Before a prospect is sent to Apollo, verify:

[ ] Lead exists in Zoho

[ ] Duplicate check completed

[ ] ICP qualification completed

[ ] PTB evaluation completed where required

[ ] Campaign selected

[ ] Required personalization fields completed

[ ] Claims checked

[ ] Case-study restrictions checked

[ ] Sender identified

[ ] Apollo sequence identified

[ ] Human approval recorded

[ ] No opt-out / suppression condition

[ ] CRM data is valid

If any mandatory condition fails:

DO NOT SEND.

Return the appropriate:

DATA GAP

POLICY BLOCK

or

HUMAN APPROVAL REQUIRED

---

# 30. NO SILENT BYPASS

No Skill may silently bypass:

- CRM validation
- duplicate checks
- qualification
- campaign selection
- personalization validation
- human approval
- suppression checks

If an exceptional workflow is required:

HUMAN APPROVAL REQUIRED

---

# 31. OUTREACH PRINCIPLE

The objective is not:

SEND MORE EMAILS.

The objective is:

SEND BETTER, APPROVED, RELEVANT OUTREACH.

Quality, credibility and customer trust take priority over volume.

---

# 32. FINAL RULE

The Revenue Engine must never send an outreach message simply because
the AI believes the prospect is a good opportunity.

The correct sequence is:

DISCOVER
→ QUALIFY
→ SCORE
→ SELECT
→ PERSONALIZE
→ VALIDATE
→ CRM
→ HUMAN APPROVAL
→ APOLLO
→ OUTREACH

Human approval is the gate between:

PREPARED

and:

SENT.