"""
Zediant Apollo Sequence Distribution Script (Scheduler 2 - v6.0)
Distributes BDM-approved contacts into native Apollo C1-C5 sequences.

Rules:
1. Eligibility: Contact in Apollo has 'Approval Status' (id: 6aa79220a06e87001c96131b) = 'Approved for Outreach'.
2. Resolves sequence dynamically by matching 'Target Segment' (id: 6aa790d821b4e6001cb70994) prefix (C1-C5) to Apollo sequence title.
3. Verifies email status is 'verified'.
4. Enrolls contact into sequence using active mailbox (APOLLO_EMAIL_ACCOUNT_ID).
5. Does NOT write to Zoho CRM (Zoho CRM receives leads only upon prospect response).
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
APOLLO_EMAIL_ACCOUNT_ID = os.getenv("APOLLO_EMAIL_ACCOUNT_ID", "6a70212e10bb20000cb56d8f")

# Apollo Custom Field IDs
FIELD_PERSONALISED_EMAIL = "6aa79177f203040018e0af9d"
FIELD_COMPANY_TRIGGER = "6aa790eddc1736001c90b2cf"
FIELD_PAIN_POINT = "6aa790fa8c717000101fa55c"
FIELD_OUTREACH_ANGLE = "6aa79157e03659000e5b1889"
FIELD_ICP_SCORE = "6aa77b8749beb6001c395715"
FIELD_LEAD_SOURCE = "6aa77f1d3a845200202a56d6"
FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"
FIELD_APPROVAL_STATUS = "6aa79220a06e87001c96131b"
FIELD_ZOHO_RECORD_ID = "6aa7924153f031001ce91b15"
FIELD_ZOHO_SYNC_STATUS = "6aa7926fe82ec5000c4f65db"

HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

def get_apollo_sequences():
    """Fetch active and draft sequences from Apollo."""
    url = "https://api.apollo.io/v1/emailer_campaigns/search"
    resp = requests.post(url, headers=HEADERS, json={"page": 1, "per_page": 50}, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("emailer_campaigns", [])

def resolve_sequence_for_target_segment(target_segment, sequences):
    """Match Target Segment prefix (e.g. C1, C2) to Apollo sequence name."""
    if not target_segment:
        return None
    prefix = target_segment.split("-")[0].strip() if "-" in target_segment else target_segment[:2].strip()
    for s in sequences:
        name = s.get("name", "")
        if name.startswith(prefix) or prefix in name:
            return s
    return None

def fetch_approved_contacts():
    """Fetch contacts from Apollo that have Approval Status = 'Approved for Outreach'."""
    url = "https://api.apollo.io/v1/contacts/search"
    payload = {
        "page": 1,
        "per_page": 100
    }
    resp = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    contacts = resp.json().get("contacts", [])
    
    approved = []
    for c in contacts:
        tcf = c.get("typed_custom_fields", {})
        status = tcf.get(FIELD_APPROVAL_STATUS)
        # picklist values may be list or string
        is_approved = False
        if isinstance(status, list) and "Approved for Outreach" in status:
            is_approved = True
        elif status == "Approved for Outreach":
            is_approved = True
            
        if is_approved:
            approved.append(c)
            
    return approved

def enroll_contact_in_sequence(contact_id, sequence_id):
    """Enroll contact into Apollo sequence."""
    url = f"https://api.apollo.io/v1/emailer_campaigns/{sequence_id}/add_contact_ids"
    payload = {
        "contact_ids": [contact_id],
        "emailer_campaign_id": sequence_id,
        "send_email_from_email_account_id": APOLLO_EMAIL_ACCOUNT_ID,
        "sequence_active_in_other_campaigns": False
    }
    resp = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()

def run_distribution():
    if not APOLLO_API_KEY:
        print("ERROR: APOLLO_API_KEY is not set.")
        sys.exit(1)
        
    print("Fetching live Apollo sequences...")
    sequences = get_apollo_sequences()
    print(f"Found {len(sequences)} sequences in Apollo.")
    
    print("Fetching contacts approved for outreach (Approval Status = 'Approved for Outreach')...")
    approved_contacts = fetch_approved_contacts()
    print(f"Found {len(approved_contacts)} approved contacts.")
    
    if not approved_contacts:
        print("No contacts currently pending sequence enrollment.")
        return
        
    enrolled_count = 0
    skipped_count = 0
    
    for c in approved_contacts:
        cid = c.get("id")
        name = f"{c.get('first_name')} {c.get('last_name')}"
        email = c.get("email")
        tcf = c.get("typed_custom_fields", {})
        target_segment = tcf.get(FIELD_TARGET_SEGMENT, "")
        
        # Check verified email
        if c.get("email_status") != "verified" and c.get("contact_email_status") != "verified":
            print(f"Skipping {name} ({email}): Email is not verified.")
            skipped_count += 1
            continue
            
        # Match sequence
        seq = resolve_sequence_for_target_segment(target_segment, sequences)
        if not seq:
            print(f"Skipping {name}: Could not match Target Segment '{target_segment}' to an Apollo sequence.")
            skipped_count += 1
            continue
            
        seq_id = seq.get("id")
        seq_name = seq.get("name")
        print(f"Enrolling {name} ({email}) into sequence '{seq_name}' ({seq_id})...")
        
        try:
            res = enroll_contact_in_sequence(cid, seq_id)
            print(f"  Enrolled successfully!")
            enrolled_count += 1
        except Exception as e:
            print(f"  [ERROR] Failed to enroll {name}: {e}")
            skipped_count += 1
            
    print("\n==========================================")
    print("DISTRIBUTION RUN SUMMARY")
    print("==========================================")
    print(f"Approved Contacts: {len(approved_contacts)}")
    print(f"Successfully Enrolled: {enrolled_count}")
    print(f"Skipped / Failed: {skipped_count}")

if __name__ == "__main__":
    run_distribution()
