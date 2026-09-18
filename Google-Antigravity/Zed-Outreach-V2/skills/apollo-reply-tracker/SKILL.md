---
name: "apollo-reply-tracker"
description: "Zediant's reply monitoring & Zoho CRM sync engine — monitors incoming replies and sequence response events in Apollo. When a prospect replies, automatically marks Apollo contact as 'Responded', calls crm-update to create the lead in Zoho CRM with Lead_Status = 'Engaged', syncs the new Zoho Record ID back to Apollo with Zoho Sync Status = 'Synced', and alerts the team via Cliq #Z-Outreach-Auto-Update. Prevents cold lead pollution in Zoho CRM. Use: 'Check Apollo replies', 'sync engaged prospects to Zoho', 'process sequence responses'."
metadata:
  version: "3.0"
---

# Apollo Reply Tracker & Post-Response Zoho CRM Sync Engine

Monitors incoming sequence replies in Apollo, triggers lead creation in Zoho CRM for engaged prospects, updates Apollo contact custom fields (`Zoho Record ID`, `Zoho Sync Status = "Synced"`, `Approval Status = "Responded"`), and posts actionable team alerts to Zoho Cliq.

---

## Architecture & Trigger Flow

```
Prospect Replies to Apollo Sequence
  ↓
Apollo halts sequence progression automatically
  ↓
apollo-reply-tracker detects reply event
  ↓
1. Update Apollo Contact: Approval Status = "Responded"
2. Call crm-update:
   - Check Zoho CRM for existing record by email (dedup)
   - Create Lead in Zoho CRM with Lead_Status = "Engaged"
   - Map intelligence fields (Skype_ID=ICP, Twitter=PTB, Business_Challenges=Pain Point)
   - Capture Zoho Lead Record ID
3. Update Apollo Contact:
   - Zoho Record ID = {zoho_lead_id}
   - Zoho Sync Status = "Synced"
4. Post Team Alert to Cliq #Z-Outreach-Auto-Update with Zoho Lead link
```

---

## Scope

**Owns:**
- Monitoring Apollo sequence reply activities (`emailer_campaigns` activities / mailbox replies)
- Extracting respondent message body and timestamp
- Orchestrating the post-response CRM sync via `crm-update`
- Writing back `Zoho Record ID` and `Zoho Sync Status = "Synced"` to the Apollo contact
- Posting rich, actionable notifications to Zoho Cliq

**Does not own:**
- Auto-responding to the prospect (BDM owns human dialogue)
- Pre-outreach lead population (Scheduler 1 owns this)
- Modifying sequence steps or schedules

---

## Exact Apollo Field Updates on Response

When an outreach reply is detected:

```json
{
  "typed_custom_fields": {
    "6aa79220a06e87001c96131b": "Responded",
    "6aa7924153f031001ce91b15": "{zoho_lead_id}",
    "6aa7926fe82ec5000c4f65db": "Synced"
  }
}
```

---

## Cliq Notification Format

Post to `#Z-Outreach-Auto-Update`:

```markdown
🚨 **NEW ENGAGED PROSPECT — OUTREACH REPLY RECEIVED**
- **Prospect**: {first_name} {last_name} ({title})
- **Company**: {company}
- **Campaign / Target Segment**: {target_segment}
- **Outreach Angle**: {outreach_angle}
- **ICP Score**: {icp_score} | **PTB Score**: {ptb_score}
- **Zoho Lead Created**: [View in Zoho CRM](https://crm.zoho.com/crm/org.../tab/Leads/{zoho_lead_id})
- **Apollo Contact**: [View in Apollo](https://app.apollo.io/#/contacts/{apollo_contact_id})

**Reply Snippet**:
> "{reply_body_text}"

*Action Required: BDM to review and respond to the thread today.*
```
