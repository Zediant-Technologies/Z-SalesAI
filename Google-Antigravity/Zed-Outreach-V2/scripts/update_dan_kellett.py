import os
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

headers = {
    "X-Api-Key": os.getenv("APOLLO_API_KEY"),
    "Content-Type": "application/json"
}

cid = "6aabb5d40030900018ce1e36"
seq_id = "6aa7ecbea907dd00140753b2"

b1 = "Saw what your team is building with FirstClose's equity settlement platform and your focus on automating lender closing workflows."
b2 = "Integrating diverse title and valuation vendor APIs while maintaining strict closing latency usually pulls senior engineers into ongoing middleware maintenance. We supply dedicated senior middleware squads to build resilient bi-directional data layers under full architectural ownership."
b3 = "Open to seeing how we streamlined integration architecture for a similar high-volume transaction platform?"
email_body = f"{b1}\n\n{b2}\n\n{b3}"

custom_fields = {
    "6aa77b8749beb6001c395715": 94.0,
    "6aa77f1d3a845200202a56d6": ["Apollo"],
    "6aa790d821b4e6001cb70994": "C4 - Middleware & API Integration (ZCoupler)",
    "6aa790eddc1736001c90b2cf": "scaling home equity settlement workflows and lender API integrations",
    "6aa790fa8c717000101fa55c": "custom lender API integrations and real-time title data synchronization",
    "6aa79157e03659000e5b1889": ["Other"],
    "6aa79177f203040018e0af9d": email_body,
    "6aa79220a06e87001c96131b": ["New"],
    "6aa7924153f031001ce91b15": "",
    "6aa7926fe82ec5000c4f65db": ["Not Synced"]
}

r1 = requests.put(f"https://api.apollo.io/v1/contacts/{cid}", headers=headers, json={"typed_custom_fields": custom_fields})
print("Update custom fields status:", r1.status_code)

r2 = requests.post(f"https://api.apollo.io/v1/emailer_campaigns/{seq_id}/add_contact_ids", headers=headers, json={
    "contact_ids": [cid],
    "emailer_campaign_id": seq_id,
    "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
    "sequence_active_in_other_campaigns": False
})
print("Add to sequence status:", r2.status_code)
