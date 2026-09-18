import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("APOLLO_API_KEY")
headers = {"Content-Type": "application/json", "Cache-Control": "no-cache", "X-Api-Key": api_key}

# 1. Search for 1 contact in Apollo to test custom fields on
res = requests.post("https://api.apollo.io/v1/contacts/search", headers=headers, json={"page": 1, "per_page": 1})
contacts = res.json().get("contacts", [])
if not contacts:
    print("No contacts found to test with.")
    exit(0)

contact = contacts[0]
cid = contact.get("id")
name = f"{contact.get('first_name')} {contact.get('last_name')}"
print(f"Testing custom fields update on Contact: {name} (ID: {cid})")

# 2. Prepare all 10 custom fields
typed_custom_fields = {
    "6aa77b8749beb6001c395715": 85,                             # ICP Score (Number)
    "6aa77f1d3a845200202a56d6": "Apollo",                       # Lead Source (Picklist: Apollo, LinkedIn, Other)
    "6aa790d821b4e6001cb70994": "C1 - AI-Enabled Product Engineering", # Target Segment (String)
    "6aa790eddc1736001c90b2cf": "Accelerating LLM feature rollout for enterprise customers with 3 senior hires active", # Company Trigger (Textarea)
    "6aa790fa8c717000101fa55c": "Senior fullstack and AI engineering capacity constraints delaying product milestones", # Pain Point (Textarea)
    "6aa79157e03659000e5b1889": "Product Development",         # Outreach Angle (Picklist: Product Development, Engineering Capacity, Other)
    "6aa79220a06e87001c96131b": "New",                         # Approval Status (Picklist: New, Approved for Outreach, Responded)
    "6aa7924153f031001ce91b15": "",                            # Zoho Record ID (String)
    "6aa7926fe82ec5000c4f65db": "Not Synced",                  # Zoho Sync Status (Picklist: Synced, Not Synced)
    "6aa79177f203040018e0af9d": "Saw what you are shipping on the product roadmap. Scaling enterprise AI features while maintaining core delivery velocity is tough. We deploy dedicated senior pods to help product teams hit their roadmap milestones without hiring friction." # Personalised Email (Textarea)
}

payload = {
    "typed_custom_fields": typed_custom_fields
}

put_res = requests.put(f"https://api.apollo.io/v1/contacts/{cid}", headers=headers, json=payload)
print("PUT status:", put_res.status_code)
if put_res.status_code == 200:
    updated_contact = put_res.json().get("contact", {})
    tcf = updated_contact.get("typed_custom_fields", {})
    print("\nVerified populated custom fields on contact:")
    field_names = {
        "6aa77b8749beb6001c395715": "ICP Score",
        "6aa77f1d3a845200202a56d6": "Lead Source",
        "6aa790d821b4e6001cb70994": "Target Segment",
        "6aa790eddc1736001c90b2cf": "Company Trigger",
        "6aa790fa8c717000101fa55c": "Pain Point",
        "6aa79157e03659000e5b1889": "Outreach Angle",
        "6aa79220a06e87001c96131b": "Approval Status",
        "6aa7924153f031001ce91b15": "Zoho Record ID",
        "6aa7926fe82ec5000c4f65db": "Zoho Sync Status",
        "6aa79177f203040018e0af9d": "Personalised Email"
    }
    for fid, label in field_names.items():
        val = tcf.get(fid)
        print(f"  {label} ({fid}): {val}")
else:
    print("Error:", put_res.text)
