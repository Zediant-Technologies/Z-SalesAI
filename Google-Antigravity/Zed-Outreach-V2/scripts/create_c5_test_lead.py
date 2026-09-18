import os
import requests
import json
from dotenv import load_dotenv

ENV_PATH = r"c:\Work\Zediant\Sales\Google-Antigravity\Zed-Outreach-V2\.env"
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
    print("SCHEDULER 1: Creating & Enriching C5 Test Lead in Apollo")
    print("==================================================")

    first_name = "Reeve"
    last_name = "Vaughan"
    email = "reevev@redplanetsoftware.com"
    title = "Chief Technology Officer"
    company = "Red Planet Software"
    website = "http://www.redplanetsoftware.com"
    linkedin_url = "http://www.linkedin.com/in/reeve-vaughan-4b184020a"

    # 1. Check if contact already exists
    search_url = "https://api.apollo.io/v1/contacts/search"
    res = requests.post(search_url, headers=APOLLO_HEADERS, json={"q_keywords": email})
    existing_contacts = res.json().get("contacts", [])
    
    contact_id = None
    if existing_contacts:
        contact_id = existing_contacts[0].get("id")
        print(f"Contact already exists in Apollo: {contact_id}")
    else:
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

    # 2. Formulate 3-Beat Personalised Email & Lowercase Gerund Pain Point
    beat1 = "Saw what Red Planet Software has engineered with your Odyssey platform and how you handle complex insurance premium funding and ledger workflows."
    beat2 = "Upgrading mission-critical loan administration and payment architectures usually stalls when engineering teams have to balance core modernization against the fear of disrupting live financial transactions. We deploy specialized senior squads to refactor high-load modules incrementally using the strangler pattern, keeping daily operations completely uninterrupted."
    beat3 = "Open to reviewing a short case breakdown of an incremental monolith decomposition we completed for an enterprise platform?"

    personalised_email_body = f"{beat1}\n\n{beat2}\n\n{beat3}"
    pain_point = "monolithic architecture refactoring risks and maintaining uptime across core financial workflows"
    # Note: Trigger without company name so "noticed {{Company Trigger}} at {{company}}" renders cleanly
    company_trigger = "ongoing modernization of Odyssey's core loan administration and payment platform"

    # 3. Update custom fields
    custom_fields = {
        FIELD_ICP_SCORE: 92.0,
        FIELD_LEAD_SOURCE: ["Apollo"],
        FIELD_TARGET_SEGMENT: "C5 - Enterprise Custom Development & Modernization",
        FIELD_COMPANY_TRIGGER: company_trigger,
        FIELD_PAIN_POINT: pain_point,
        FIELD_OUTREACH_ANGLE: ["Product Development"],
        FIELD_PERSONALISED_EMAIL: personalised_email_body,
        FIELD_APPROVAL_STATUS: ["New"],
        FIELD_ZOHO_RECORD_ID: "",
        FIELD_ZOHO_SYNC_STATUS: ["Not Synced"]
    }

    update_url = f"https://api.apollo.io/v1/contacts/{contact_id}"
    update_res = requests.put(update_url, headers=APOLLO_HEADERS, json={
        "organization_name": company,
        "typed_custom_fields": custom_fields
    })
    
    if update_res.status_code == 200:
        c = update_res.json().get("contact", {})
        print(f"\nSuccessfully populated all 10 custom fields on Apollo Contact {contact_id}!")
        print(f"  Name: {c.get('first_name')} {c.get('last_name')}")
        print(f"  Email: {c.get('email')}")
        print(f"  Company: {c.get('organization_name')}")
        print(f"  Target Segment: {c.get('typed_custom_fields', {}).get(FIELD_TARGET_SEGMENT)}")
        print(f"  Approval Status: {c.get('typed_custom_fields', {}).get(FIELD_APPROVAL_STATUS)}")
        print(f"  Zoho Sync Status: {c.get('typed_custom_fields', {}).get(FIELD_ZOHO_SYNC_STATUS)}")
        print(f"  Pain Point: {c.get('typed_custom_fields', {}).get(FIELD_PAIN_POINT)}")
    else:
        print(f"Error updating custom fields: {update_res.status_code} - {update_res.text}")

if __name__ == "__main__":
    main()
