import os
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

headers = {"X-Api-Key": os.getenv("APOLLO_API_KEY"), "Content-Type": "application/json"}
FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"
FIELD_COMPANY_TRIGGER = "6aa790eddc1736001c90b2cf"
FIELD_PAIN_POINT = "6aa790fa8c717000101fa55c"
FIELD_ICP_SCORE = "6aa77b8749beb6001c395715"

r = requests.post("https://api.apollo.io/v1/contacts/search", headers=headers, json={"per_page": 100})
contacts = r.json().get("contacts", [])

print("Sample of Enriched Contacts across AUS, UAE, US:")
for c in contacts[:15]:
    tcf = c.get("typed_custom_fields", {})
    print(f"- {c.get('first_name')} {c.get('last_name')} | {c.get('title')} | {c.get('organization_name')} ({c.get('country')})")
    print(f"  Email: {c.get('email')} | Target: {tcf.get(FIELD_TARGET_SEGMENT)} | ICP: {tcf.get(FIELD_ICP_SCORE)}")
    print(f"  Trigger: {tcf.get(FIELD_COMPANY_TRIGGER)}")
    print(f"  Pain Point: {tcf.get(FIELD_PAIN_POINT)}")
    print(f"  Sequences: {c.get('emailer_campaign_ids')}")
    print()
