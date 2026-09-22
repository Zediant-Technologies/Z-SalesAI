import os
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

headers = {
    "X-Api-Key": os.getenv("APOLLO_API_KEY"),
    "Content-Type": "application/json"
}

FIELD_ICP_SCORE = "6aa77b8749beb6001c395715"
FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"
FIELD_APPROVAL_STATUS = "6aa79220a06e87001c96131b"
FIELD_ZOHO_SYNC_STATUS = "6aa7926fe82ec5000c4f65db"
FIELD_COMPANY_TRIGGER = "6aa790eddc1736001c90b2cf"
FIELD_PAIN_POINT = "6aa790fa8c717000101fa55c"
FIELD_PERSONALISED_EMAIL = "6aa79177f203040018e0af9d"

all_contacts = []
page = 1
while True:
    r = requests.post("https://api.apollo.io/v1/contacts/search", headers=headers, json={"page": page, "per_page": 50})
    if r.status_code != 200:
        break
    data = r.json()
    contacts = data.get("contacts", [])
    if not contacts:
        break
    all_contacts.extend(contacts)
    page += 1
    if page > 5:
        break

print(f"Total Contacts Verified: {len(all_contacts)}")

c_breakdown = {}
geo_breakdown = {}
approval_breakdown = {}
seq_populated = 0
email_word_counts = []

for c in all_contacts:
    tcf = c.get("typed_custom_fields", {})
    camp = tcf.get(FIELD_TARGET_SEGMENT, "Unassigned")
    c_breakdown[camp] = c_breakdown.get(camp, 0) + 1

    geo = c.get("country") or "Unknown"
    geo_breakdown[geo] = geo_breakdown.get(geo, 0) + 1

    app = str(tcf.get(FIELD_APPROVAL_STATUS))
    approval_breakdown[app] = approval_breakdown.get(app, 0) + 1

    if c.get("emailer_campaign_ids"):
        seq_populated += 1

    email_body = tcf.get(FIELD_PERSONALISED_EMAIL, "")
    if email_body:
        email_word_counts.append(len(email_body.split()))

print("\n--- Summary Breakdown ---")
print(f"Total Verified Contacts: {len(all_contacts)}")
print(f"Native 'Sequences' Field Populated: {seq_populated}/{len(all_contacts)}")
print(f"Average Email Word Count: {sum(email_word_counts)/len(email_word_counts):.1f} words (Target: 50-90 words)")

print("\n--- Campaign Distribution ---")
for k, v in sorted(c_breakdown.items()):
    print(f"  {k}: {v} leads ({v/len(all_contacts)*100:.1f}%)")

print("\n--- Geographic Distribution ---")
for k, v in sorted(geo_breakdown.items()):
    print(f"  {k}: {v} leads ({v/len(all_contacts)*100:.1f}%)")

print("\n--- Approval Status (Apollo BDM Gate) ---")
for k, v in sorted(approval_breakdown.items()):
    print(f"  {k}: {v} leads")
