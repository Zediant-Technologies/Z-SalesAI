"""
Zediant Revenue Engine - Scheduler 2 Production Runner
Queries Zoho Leads for 'Approved for Outreach', distributes to Saleshandy C1-C5 sequences,
tags with campaign and case study availability, flips Zoho status to 'Outreach Scheduled',
and posts mandatory aggregate-only summary to Zoho Cliq.
"""

import os
import sys
import json
import time
import requests
from dotenv import load_dotenv

ENV_PATH = r"c:\Work\Zediant\Sales\Google-Antigravity\Zediant-Sales-Engine\.env"
load_dotenv(ENV_PATH)

SALESHANDY_API_KEY = os.getenv("SALESHANDY_API_KEY")
SALESHANDY_BASE_URL = os.getenv("SALESHANDY_API_BASE_URL", "https://open-api.saleshandy.com/v1")

ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")
ZOHO_API_DOMAIN = os.getenv("ZOHO_API_DOMAIN", "https://www.zohoapis.in")

SH_HEADERS = {
    "x-api-key": SALESHANDY_API_KEY,
    "Content-Type": "application/json"
}

CAMPAIGN_MAP = {
    "C1 - AI-Enabled Product Engineering": {"seq": "68Pvv34nP7", "step": "gOwE9LAKwb", "tag": "C1-Campaign"},
    "C2 - Engineering Pods & Staff Augmentation": {"seq": "1qPBL69vzD", "step": "9KwOmq7Ra6", "tag": "C2-Campaign"},
    "C3 - Platform Engineering & Cloud Modernization": {"seq": "Mgw473olzA", "step": "Y8aL6gElwN", "tag": "C3-Campaign"},
    "C4 - Middleware & API Integration (ZCoupler)": {"seq": "glwGOA9Rw6", "step": "LGz3OEDxzr", "tag": "C4-Campaign"},
    "C5 - Enterprise Custom Development & Modernization": {"seq": "6vaKGDl4aW", "step": "7pzVpxXxPb", "tag": "C5-Campaign"}
}

def get_zoho_token():
    r = requests.post(f"{ZOHO_ACCOUNTS_URL}/token", data={
        "grant_type": "refresh_token",
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "refresh_token": ZOHO_REFRESH_TOKEN
    }, timeout=15)
    return r.json().get("access_token")

def build_prospect_item(lead):
    return {
        "First Name": lead.get("First_Name") or "",
        "Last Name": lead.get("Last_Name") or "",
        "Email": lead.get("Email") or "",
        "Job Title": lead.get("Designation") or lead.get("Title") or "",
        "Company": lead.get("Company") or "",
        "Email Personalised Opening": lead.get("Email_Personalised_Opening") or "",
        "Email Pain Points": lead.get("Email_Pain_Points") or "",
        "Business Challenge": lead.get("Business_Challenges") or "",
        "Case Study": lead.get("Case_Study") or ""
    }

def poll_import_status(request_id):
    url = f"{SALESHANDY_BASE_URL}/prospects/import-status/{request_id}"
    for _ in range(12):
        time.sleep(2)
        r = requests.get(url, headers=SH_HEADERS, timeout=15)
        if r.status_code == 200:
            payload = r.json().get("payload", {})
            if payload.get("isCompleted"):
                return True, payload
    return False, {}

def run_scheduler2():
    print("=" * 75)
    print("Zediant Revenue Engine - Scheduler 2 Saleshandy Distribution")
    print("=" * 75)

    token = get_zoho_token()
    headers = {"Authorization": f"Zoho-oauthtoken {token}"}

    # Fetch Approved for Outreach leads
    url = f"{ZOHO_API_DOMAIN}/crm/v2/Leads/search?criteria=(Lead_Status:equals:Approved for Outreach)"
    r = requests.get(url, headers=headers, timeout=20)
    if r.status_code == 204:
        print("No leads currently in 'Approved for Outreach' status.")
        return

    data = r.json().get("data", [])
    print(f"Found {len(data)} leads in 'Approved for Outreach' status.")

    eligible = []
    skipped_campaign = []
    for lead in data:
        camp = lead.get("Lead_Campaign_Category")
        if camp in CAMPAIGN_MAP:
            eligible.append(lead)
        else:
            skipped_campaign.append((lead.get("id"), camp))

    print(f"Eligible for Distribution: {len(eligible)}")
    if skipped_campaign:
        print(f"Skipped due to campaign mismatch / non-standard label: {len(skipped_campaign)}")

    if not eligible:
        print("No eligible leads ready for distribution.")
        return

    # Group by campaign
    campaign_groups = {}
    for lead in eligible:
        camp = lead.get("Lead_Campaign_Category")
        campaign_groups.setdefault(camp, []).append(lead)

    successfully_imported_ids = []
    failed_imports = []
    cs_available_count = 0
    cs_not_available_count = 0

    for camp_name, leads in campaign_groups.items():
        cfg = CAMPAIGN_MAP[camp_name]
        step_id = cfg["step"]
        camp_tag = cfg["tag"]

        cs_avail = [l for l in leads if (l.get("Case_Study") or "").strip()]
        cs_not_avail = [l for l in leads if not (l.get("Case_Study") or "").strip()]

        cs_available_count += len(cs_avail)
        cs_not_available_count += len(cs_not_avail)

        for cs_tag, sub_list in [("CASE_STUDY_AVAILABLE", cs_avail), ("CASE_STUDY_NOT_AVAILABLE", cs_not_avail)]:
            if not sub_list:
                continue

            prospect_list = [build_prospect_item(l) for l in sub_list]
            payload = {
                "prospectList": prospect_list,
                "stepId": step_id,
                "tags": [camp_tag, cs_tag],
                "conflictAction": "noUpdate",
                "verifyProspects": False
            }

            resp = requests.post(f"{SALESHANDY_BASE_URL}/prospects/import-with-field-name", headers=SH_HEADERS, json=payload, timeout=30)
            if resp.status_code in [200, 201]:
                req_id = resp.json().get("payload", {}).get("requestId")
                completed, _ = poll_import_status(req_id)
                if completed:
                    for l in sub_list:
                        successfully_imported_ids.append(l["id"])
                else:
                    for l in sub_list:
                        failed_imports.append((l["id"], "Timeout"))
            else:
                for l in sub_list:
                    failed_imports.append((l["id"], f"HTTP {resp.status_code}"))

    print(f"\nImport Completed: {len(successfully_imported_ids)} succeeded, {len(failed_imports)} failed.")

    # Flip Zoho Status to "Outreach Scheduled"
    if successfully_imported_ids:
        token = get_zoho_token()
        zoho_update_url = f"{ZOHO_API_DOMAIN}/crm/v2/Leads"
        batch_size = 100
        for i in range(0, len(successfully_imported_ids), batch_size):
            batch_ids = successfully_imported_ids[i:i+batch_size]
            update_data = [{"id": rid, "Lead_Status": "Outreach Scheduled"} for rid in batch_ids]
            requests.put(zoho_update_url, headers={"Authorization": f"Zoho-oauthtoken {token}", "Content-Type": "application/json"}, json={"data": update_data}, timeout=30)
        print("Zoho CRM Lead_Status updated to 'Outreach Scheduled'.")

    # Step 7: Aggregate Cliq Notification
    camp_summary = " | ".join([f"{k.split(' - ')[0]}: {len(v)}" for k, v in sorted(campaign_groups.items())])
    cliq_msg = (
        f"📤 [Scheduler 2 — Saleshandy Distribution]\n\n"
        f"Approved for Outreach leads reviewed: {len(data)}\n"
        f"Eligible for distribution: {len(eligible)}\n"
        f"Saleshandy imports completed: {len(successfully_imported_ids)}\n"
        f"Saleshandy imports failed: {len(failed_imports)}\n"
        f"Case Study Available: {cs_available_count} | Not Available: {cs_not_available_count}\n"
        f"Campaigns distributed: {camp_summary}\n"
        f"Zoho status updated: {len(successfully_imported_ids)} -> Outreach Scheduled\n"
        f"Sequence activation: 0 (Manual BDM activation preserved)\n"
        f"Emails sent: 0\n\n"
        f"Note: Strict aggregate notification. Zero individual prospect identities posted."
    )

    try:
        from notify_cliq import send_cliq_notification
        print("\nSending aggregate notification to Zoho Cliq (#Z-Outreach-Auto-Update)...")
        res = send_cliq_notification(cliq_msg)
        print("Cliq Notification Result:", json.dumps(res))
    except Exception as e:
        print(f"Warning: Cliq notification failed: {e}")

if __name__ == "__main__":
    run_scheduler2()
