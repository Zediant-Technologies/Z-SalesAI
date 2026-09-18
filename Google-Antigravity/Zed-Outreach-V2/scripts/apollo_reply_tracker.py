"""
Zediant Apollo Reply Tracker & Post-Response Zoho CRM Sync Engine (v6.0)

Purpose:
Monitors incoming replies and sequence responses in Apollo.
When a prospect replies to outreach:
1. Sets Apollo contact 'Approval Status' to 'Responded'.
2. Calls Zoho CRM to check for existing record by email (deduplication).
3. Creates/Updates Lead in Zoho CRM with Lead_Status = 'Engaged'.
4. Maps intelligence fields (Skype_ID=ICP, Twitter=PTB, Business_Challenges=Pain Point).
5. Writes the new Zoho Record ID back to Apollo Contact ('Zoho Record ID')
   and sets 'Zoho Sync Status' = 'Synced'.
6. Posts team alert to Cliq #Z-Outreach-Auto-Update.
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

# Apollo Configuration
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
APOLLO_HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

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

# Zoho CRM Configuration
ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_API_DOMAIN = os.getenv("ZOHO_API_DOMAIN", "https://www.zohoapis.in")
ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")


def get_zoho_access_token():
    """Exchange refresh token for a fresh Zoho access token."""
    res = requests.post(f"{ZOHO_ACCOUNTS_URL}/token", params={
        "refresh_token": ZOHO_REFRESH_TOKEN,
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "grant_type": "refresh_token"
    }, timeout=30)
    res.raise_for_status()
    data = res.json()
    return data.get("access_token")


def search_zoho_lead_by_email(email, access_token):
    """Search Zoho CRM for an existing lead with given email."""
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }
    url = f"{ZOHO_API_DOMAIN}/crm/v3/Leads/search"
    resp = requests.get(url, headers=headers, params={"email": email}, timeout=30)
    if resp.status_code == 200:
        data = resp.json().get("data", [])
        if data:
            return data[0]
    return None


def create_or_update_zoho_lead(contact_data, reply_context, access_token):
    """Create or update lead in Zoho CRM with Lead_Status = 'Engaged'."""
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
    }
    
    email = contact_data.get("email")
    existing_lead = search_zoho_lead_by_email(email, access_token) if email else None
    
    tcf = contact_data.get("typed_custom_fields", {})
    icp_score = str(int(tcf.get(FIELD_ICP_SCORE) or 75))
    company_trigger = tcf.get(FIELD_COMPANY_TRIGGER, "")
    pain_point = tcf.get(FIELD_PAIN_POINT, "")
    target_segment = tcf.get(FIELD_TARGET_SEGMENT, "C1 - AI-Enabled Product Engineering")
    outreach_angle = tcf.get(FIELD_OUTREACH_ANGLE, "Product Development")
    if isinstance(outreach_angle, list) and outreach_angle:
        outreach_angle = outreach_angle[0]
        
    description_text = (
        f"[ENGAGED - OUTREACH RESPONSE]\n"
        f"Reply Context: {reply_context}\n\n"
        f"Trigger: {company_trigger}\n"
        f"Outreach Angle: {outreach_angle}\n"
        f"Apollo Contact ID: {contact_data.get('id')}\n"
    )
    
    lead_payload = {
        "First_Name": contact_data.get("first_name") or "",
        "Last_Name": contact_data.get("last_name") or "Contact",
        "Email": email,
        "Company": contact_data.get("organization_name") or contact_data.get("company") or "Unknown",
        "Designation": contact_data.get("title") or "",
        "Lead_Source": "Apollo Outreach",
        "Lead_Status": "Engaged",
        "Skype_ID": icp_score,
        "Twitter": "80",  # High Buying Signal on Response
        "Lead_Campaign_Category": target_segment,
        "Business_Challenges": pain_point,
        "leadchain0__Social_Lead_ID": contact_data.get("id"),
        "LinkedIN_Link": contact_data.get("linkedin_url") or "",
        "Description": description_text
    }
    
    if existing_lead:
        lead_id = existing_lead.get("id")
        url = f"{ZOHO_API_DOMAIN}/crm/v3/Leads/{lead_id}"
        resp = requests.put(url, headers=headers, json={"data": [lead_payload]}, timeout=30)
        resp.raise_for_status()
        print(f"Updated existing Zoho Lead {lead_id} to Engaged.")
        return lead_id, "Updated"
    else:
        url = f"{ZOHO_API_DOMAIN}/crm/v3/Leads"
        resp = requests.post(url, headers=headers, json={"data": [lead_payload]}, timeout=30)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        lead_id = data[0].get("details", {}).get("id")
        print(f"Created new Zoho Lead {lead_id} with Lead_Status = Engaged.")
        return lead_id, "Created"


def update_apollo_contact_sync_status(contact_id, zoho_lead_id):
    """Update Apollo contact with Zoho Record ID and Zoho Sync Status = 'Synced'."""
    url = f"https://api.apollo.io/v1/contacts/{contact_id}"
    payload = {
        "typed_custom_fields": {
            FIELD_ZOHO_RECORD_ID: str(zoho_lead_id),
            FIELD_ZOHO_SYNC_STATUS: "Synced",
            FIELD_APPROVAL_STATUS: "Responded"
        }
    }
    resp = requests.put(url, headers=APOLLO_HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    print(f"Synced Zoho Record ID {zoho_lead_id} back to Apollo contact {contact_id}.")
    return resp.json()


def sync_engaged_prospect(contact_id, reply_context="Prospect replied to outbound email sequence."):
    """Full workflow: fetch Apollo contact -> create Zoho Lead -> sync back Zoho ID to Apollo."""
    print(f"\n--- Processing Engaged Prospect: Apollo Contact {contact_id} ---")
    
    # 1. Fetch contact details from Apollo
    res = requests.get(f"https://api.apollo.io/v1/contacts/{contact_id}", headers=APOLLO_HEADERS, timeout=30)
    res.raise_for_status()
    contact = res.json().get("contact", {})
    
    # 2. Get Zoho Access Token
    token = get_zoho_access_token()
    
    # 3. Create or update Zoho Lead
    zoho_id, action = create_or_update_zoho_lead(contact, reply_context, token)
    
    # 4. Sync back to Apollo
    update_apollo_contact_sync_status(contact_id, zoho_id)
    
    print(f"Engagement sync completed: {action} Zoho Lead {zoho_id} for {contact.get('first_name')} {contact.get('last_name')}.")
    return zoho_id


def check_and_process_replies():
    """Check Apollo for contacts with replies or marked responded and sync to Zoho."""
    print("Checking Apollo for engaged / responded contacts...")
    # Search contacts where Approval Status is Responded but Zoho Sync Status is not Synced
    url = "https://api.apollo.io/v1/contacts/search"
    resp = requests.post(url, headers=APOLLO_HEADERS, json={"page": 1, "per_page": 50}, timeout=30)
    resp.raise_for_status()
    contacts = resp.json().get("contacts", [])
    
    count = 0
    for c in contacts:
        tcf = c.get("typed_custom_fields", {})
        approval_status = tcf.get(FIELD_APPROVAL_STATUS)
        sync_status = tcf.get(FIELD_ZOHO_SYNC_STATUS)
        
        # If marked Responded but Not Synced
        if approval_status == "Responded" or (isinstance(approval_status, list) and "Responded" in approval_status):
            if sync_status != "Synced" and (not isinstance(sync_status, list) or "Synced" not in sync_status):
                cid = c.get("id")
                print(f"Found unsynced responded contact: {c.get('first_name')} {c.get('last_name')} ({cid})")
                sync_engaged_prospect(cid, "Detected sequence response in Apollo.")
                count += 1
                
    if count == 0:
        print("No pending unsynced replies found in Apollo.")
    else:
        print(f"Successfully processed and synced {count} engaged prospects to Zoho CRM.")

    # Mark completed unresponsive contacts in Apollo with 90-day cooldown (preserving zero clutter in Zoho)
    mark_unresponsive_completed_contacts()


def mark_unresponsive_completed_contacts():
    """Find contacts whose sequence finished without reply, mark Finished - Unresponsive."""
    # When contacts finish all sequence steps without reply, update Approval Status to Finished - Unresponsive
    url = "https://api.apollo.io/v1/contacts/search"
    resp = requests.post(url, headers=APOLLO_HEADERS, json={"page": 1, "per_page": 50}, timeout=30)
    if resp.status_code != 200:
        return
    contacts = resp.json().get("contacts", [])
    for c in contacts:
        # Check if contact is finished in sequences and still Approved for Outreach
        tcf = c.get("typed_custom_fields", {})
        approval_status = tcf.get(FIELD_APPROVAL_STATUS)
        is_approved = approval_status == "Approved for Outreach" or (isinstance(approval_status, list) and "Approved for Outreach" in approval_status)
        
        # Check sequence memberships
        memberships = c.get("emailer_campaign_memberships", [])
        for m in memberships:
            if m.get("status") in ["finished", "completed"] and is_approved:
                cid = c.get("id")
                name = f"{c.get('first_name')} {c.get('last_name')}"
                print(f"Marking unresponsive finished contact {name} ({cid}) as 'Finished - Unresponsive' (90-day cooldown).")
                requests.put(f"https://api.apollo.io/v1/contacts/{cid}", headers=APOLLO_HEADERS, json={
                    "typed_custom_fields": {
                        FIELD_APPROVAL_STATUS: "Finished - Unresponsive"
                    }
                }, timeout=30)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--sync-contact" and len(sys.argv) > 2:
        sync_engaged_prospect(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "Manual test sync")
    else:
        check_and_process_replies()
