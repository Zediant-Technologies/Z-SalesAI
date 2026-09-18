---
name: "apollo-distribution"
description: "Zediant Scheduler 2 — distributes all BDM-approved Apollo contacts into their corresponding native Apollo sequence (C1–C5). Queries Apollo directly for contacts where Approval Status = 'Approved for Outreach', resolves sequence by Target Segment, validates verified email, prevents duplicate enrollment, enrolls contact with active mailbox rajeev@zedianttechnologies.info, and reports aggregate results to Cliq. Does not write to Zoho CRM (Zoho is reserved for post-response engaged leads). Use: 'Run Scheduler 2', 'distribute approved leads', 'enroll in sequences'."
---

# Apollo Sequence Distribution — Scheduler 2 (v6.0)

Pushes BDM-approved contacts directly from Apollo into their assigned C1–C5 multichannel sequences.

---

## Overview

**What it does:**
1. **Fetch approved contacts directly from Apollo**:
   Queries contacts where:
   - `Approval Status` (`6aa79220a06e87001c96131b`) = `"Approved for Outreach"`
   - `contact_email_status` = `['verified']`
   - Not already enrolled in an active sequence.
2. **Resolve Target Sequence**:
   Reads `Target Segment` (`6aa790d821b4e6001cb70994`) from the contact:
   - `C1 - AI-Enabled Product Engineering` → `6aa7ec0e7c0f80000cbd7600`
   - `C2 - Engineering Pods & Staff Augmentation` → `6aa7eca553473f000c678940`
   - `C3 - Platform Engineering & Cloud Modernization` → `6aa7ecb31fd57300143fbfa7`
   - `C4 - Middleware & API Integration (ZCoupler)` → `6aa7ecbea907dd00140753b2`
   - `C5 - Enterprise Custom Development & Modernization` → `6aa7ecc953473f000c678b8e`
3. **Verify Custom Fields are Populated**:
   Ensures `Personalised Email`, `Pain Point`, and `Company Trigger` are non-empty.
4. **Enroll in Sequence**:
   Adds contact to the matched sequence using mailbox `rajeev@zedianttechnologies.info` (`6a70212e10bb20000cb56d8f`).
5. **Report Summary to Cliq**:
   Sends aggregate counts to `#Z-Outreach-Auto-Update`.

---

## Eligibility Gate

**Approval Status = "Approved for Outreach"** on the Apollo Contact record.

No contact may enter an active Apollo sequence without this explicit human approval state set in Apollo. High ICP or PTB score is NOT a substitute for human approval.

---

## Workflow Steps

### Step 1: Query Approved Contacts from Apollo
```python
payload = {
    "page": 1,
    "per_page": 100,
    "typed_custom_field_filter": {
        "6aa79220a06e87001c96131b": ["Approved for Outreach"]
    }
}
```

### Step 2: Check Sequence Membership
Ensure the contact is not already enrolled or completed in any campaign.

### Step 3: Match Sequence by Target Segment
Read `Target Segment` custom field (`6aa790d821b4e6001cb70994`). Match prefix `C1`, `C2`, `C3`, `C4`, or `C5` to resolve sequence ID.

### Step 4: Enroll Contact
Call `POST https://api.apollo.io/v1/emailer_campaigns/{sequence_id}/add_contact_ids`:
```json
{
  "contact_ids": ["{contact_id}"],
  "emailer_campaign_id": "{sequence_id}",
  "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
  "sequence_active_in_other_campaigns": false
}
```

### Step 5: Post Summary to Cliq
Post run summary to `#Z-Outreach-Auto-Update`:
- Total Approved Contacts Found
- Enrolled Count by Campaign (C1–C5)
- Skipped / Already Enrolled Count
- Mailbox pacing reminder
