import os
import sys
import json
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

APOLLO_HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

FIELD_ICP_SCORE = "6aa77b8749beb6001c395715"        # Number
FIELD_LEAD_SOURCE = "6aa77f1d3a845200202a56d6"      # Picklist: Apollo
FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"   # String
FIELD_COMPANY_TRIGGER = "6aa790eddc1736001c90b2cf"  # Textarea
FIELD_PAIN_POINT = "6aa790fa8c717000101fa55c"       # Textarea
FIELD_OUTREACH_ANGLE = "6aa79157e03659000e5b1889"   # Picklist
FIELD_PERSONALISED_EMAIL = "6aa79177f203040018e0af9d" # Textarea
FIELD_APPROVAL_STATUS = "6aa79220a06e87001c96131b"  # Picklist: New
FIELD_ZOHO_RECORD_ID = "6aa7924153f031001ce91b15"   # String
FIELD_ZOHO_SYNC_STATUS = "6aa7926fe82ec5000c4f65db" # Picklist: Not Synced

def main():
    print("==================================================")
    print("SCHEDULER 1: Creating & Enriching C2 Test Lead in Apollo")
    print("==================================================")

    # 1. Candidate Info
    first_name = "Jacinta"
    last_name = "Carne"
    email = "jacinta@inlight.com.au"
    title = "Chief Operating Officer"
    company = "Inlight"
    website = "http://www.inlight.com.au"
    linkedin_url = "http://www.linkedin.com/in/jacinta-carne-65796719"

    # 2. Check if contact already exists in Apollo
    search_url = "https://api.apollo.io/v1/contacts/search"
    res = requests.post(search_url, headers=APOLLO_HEADERS, json={"q_keywords": email})
    existing_contacts = res.json().get("contacts", [])
    
    contact_id = None
    if existing_contacts:
        contact_id = existing_contacts[0].get("id")
        print(f"Contact already exists in Apollo: {contact_id}")
    else:
        # Create contact in Apollo
        create_url = "https://api.apollo.io/v1/contacts"
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "title": title,
            "email": email,
            "organization_name": company,
            "website_url": website,
            "linkedin_url": linkedin_url
        }
        create_res = requests.post(create_url, headers=APOLLO_HEADERS, json=payload)
        if create_res.status_code == 200:
            contact_id = create_res.json().get("contact", {}).get("id")
            print(f"Created new contact in Apollo: {contact_id}")
        else:
            print(f"Failed to create contact: {create_res.status_code} - {create_res.text}")
            return

    # 3. Formulate strict 3-Beat Personalised Email & Lowercase Gerund Pain Point
    beat1 = "Saw the digital products Inlight has been shipping across headless web and mobile platforms for enterprise brands."
    beat2 = "When client demand ramps up, balancing active sprint commitments with senior engineering capacity usually forces a tough choice between turning down work or enduring a multi-month hiring cycle. We embed dedicated senior engineering pods in 2-3 weeks under your direction to absorb complex feature delivery without permanent overhead."
    beat3 = "Open to checking our pod onboarding playbook to see how we embed with similar digital product teams?"

    personalised_email_body = f"{beat1}\n\n{beat2}\n\n{beat3}"
    pain_point = "senior developer capacity bottlenecks and project delivery delays across client sprints"
    company_trigger = "Scaling digital product delivery and headless/composable builds at Inlight (49 employees)."

    # 4. Update custom fields on contact
    custom_fields = {
        FIELD_ICP_SCORE: 95.0,
        FIELD_LEAD_SOURCE: ["Apollo"],
        FIELD_TARGET_SEGMENT: "C2 - Engineering Pods & Staff Augmentation",
        FIELD_COMPANY_TRIGGER: company_trigger,
        FIELD_PAIN_POINT: pain_point,
        FIELD_OUTREACH_ANGLE: ["Engineering Capacity"],
        FIELD_PERSONALISED_EMAIL: personalised_email_body,
        FIELD_APPROVAL_STATUS: ["New"],
        FIELD_ZOHO_RECORD_ID: "",
        FIELD_ZOHO_SYNC_STATUS: ["Not Synced"]
    }

    update_url = f"https://api.apollo.io/v1/contacts/{contact_id}"
    update_res = requests.put(update_url, headers=APOLLO_HEADERS, json={"typed_custom_fields": custom_fields})
    if update_res.status_code == 200:
        c = update_res.json().get("contact", {})
        print(f"\nSuccessfully populated all 10 custom fields on Apollo Contact {contact_id}!")
        print(f"  Name: {c.get('first_name')} {c.get('last_name')}")
        print(f"  Email: {c.get('email')}")
        print(f"  Company: {c.get('organization_name')}")
        print(f"  Approval Status: {c.get('typed_custom_fields', {}).get(FIELD_APPROVAL_STATUS)}")
        print(f"  Zoho Sync Status: {c.get('typed_custom_fields', {}).get(FIELD_ZOHO_SYNC_STATUS)}")
    else:
        print(f"Error updating custom fields: {update_res.status_code} - {update_res.text}")

if __name__ == "__main__":
    main()
