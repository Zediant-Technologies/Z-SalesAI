import os
import sys
import json
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")
ZOHO_API_DOMAIN = os.getenv("ZOHO_API_DOMAIN", "https://www.zohoapis.in")

# Authoritative Apollo Custom Field IDs
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

APOLLO_HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

def get_zoho_token():
    r = requests.post(f"{ZOHO_ACCOUNTS_URL}/token", data={
        "grant_type": "refresh_token",
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "refresh_token": ZOHO_REFRESH_TOKEN
    }, timeout=15)
    data = r.json()
    token = data.get("access_token")
    if not token:
        raise Exception(f"Failed to refresh Zoho token: {data}")
    return token

def get_existing_zoho_records(token):
    existing_emails = set()
    existing_apollo_ids = set()
    existing_companies = set()

    page = 1
    while True:
        r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Leads?fields=Email,Company,leadchain0__Social_Lead_ID&page={page}&per_page=200", headers={
            "Authorization": f"Zoho-oauthtoken {token}"
        }, timeout=15)
        if r.status_code != 200:
            break
        items = r.json().get("data", [])
        if not items:
            break
        for item in items:
            if item.get("Email"):
                existing_emails.add(item["Email"].lower().strip())
            if item.get("leadchain0__Social_Lead_ID"):
                existing_apollo_ids.add(item["leadchain0__Social_Lead_ID"].strip())
            if item.get("Company"):
                existing_companies.add(item["Company"].lower().strip())
        page += 1

    page = 1
    while True:
        r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Contacts?fields=Email,Account_Name&page={page}&per_page=200", headers={
            "Authorization": f"Zoho-oauthtoken {token}"
        }, timeout=15)
        if r.status_code != 200:
            break
        items = r.json().get("data", [])
        if not items:
            break
        for item in items:
            if item.get("Email"):
                existing_emails.add(item["Email"].lower().strip())
            if item.get("Account_Name", {}).get("name"):
                existing_companies.add(item["Account_Name"]["name"].lower().strip())
        page += 1

    return existing_emails, existing_apollo_ids, existing_companies

def get_existing_apollo_contacts():
    existing_emails = set()
    existing_pids = set()
    
    url = "https://api.apollo.io/v1/contacts/search"
    page = 1
    while True:
        r = requests.post(url, headers=APOLLO_HEADERS, json={"page": page, "per_page": 50}, timeout=15)
        if r.status_code != 200:
            break
        data = r.json()
        contacts = data.get("contacts", [])
        if not contacts:
            break
        for c in contacts:
            em = (c.get("email") or "").lower().strip()
            if em:
                existing_emails.add(em)
            if c.get("person_id"):
                existing_pids.add(c["person_id"])
        page += 1
        if page > 10:
            break
    return existing_emails, existing_pids

def search_c2_candidates():
    url = "https://api.apollo.io/v1/mixed_people/api_search"
    
    # Target C2: Digital agencies, software consultancies, product engineering shops in Australia
    searches = [
        {
            "label": "C2 Digital Agencies & Consultancies",
            "params": {
                "page": 1,
                "per_page": 30,
                "person_titles": ["Head of Delivery", "COO", "Chief Operating Officer", "Technical Director", "Managing Director", "Director of Engineering", "Head of Engineering"],
                "person_seniorities": ["c_suite", "director", "head"],
                "person_locations": ["Australia"],
                "organization_locations": ["Australia"],
                "q_organization_keyword_tags": ["digital agency", "software development", "web development", "mobile development"],
                "organization_num_employees_ranges": ["15,50", "51,150"],
                "contact_email_status": ["verified"]
            }
        },
        {
            "label": "C2 Software & SaaS Product Teams",
            "params": {
                "page": 1,
                "per_page": 30,
                "person_titles": ["VP of Engineering", "Head of Engineering", "CTO", "Chief Technology Officer"],
                "person_seniorities": ["c_suite", "vp", "head"],
                "person_locations": ["Australia"],
                "organization_locations": ["Australia"],
                "q_organization_keyword_tags": ["software", "SaaS", "cloud application"],
                "organization_num_employees_ranges": ["20,50", "51,120"],
                "contact_email_status": ["verified"]
            }
        }
    ]

    all_people = []
    for s in searches:
        print(f"Searching Apollo [{s['label']}]...")
        r = requests.post(url, headers=APOLLO_HEADERS, json=s["params"], timeout=20)
        if r.status_code == 200:
            people = r.json().get("people", [])
            print(f"  Found {len(people)} raw verified candidates.")
            all_people.extend(people)
        else:
            print(f"  Error: {r.status_code} - {r.text[:150]}")

    return all_people

def main():
    print("==================================================")
    print("SCHEDULER 1: Sourcing 1 Net-New C2 Qualified Lead")
    print("==================================================")

    # 1. Deduplication
    print("\n1. Building Master Deduplication Sets...")
    zoho_token = get_zoho_token()
    z_emails, z_apollo_ids, z_comps = get_existing_zoho_records(zoho_token)
    print(f"  Zoho Records: {len(z_emails)} emails, {len(z_comps)} companies")

    a_emails, a_pids = get_existing_apollo_contacts()
    print(f"  Apollo Contacts: {len(a_emails)} emails, {len(a_pids)} person IDs")

def enrich_person(person_id):
    url = "https://api.apollo.io/v1/people/match"
    r = requests.post(url, headers=APOLLO_HEADERS, json={"id": person_id}, timeout=20)
    if r.status_code == 200:
        return r.json().get("person")
    return None

def create_or_get_apollo_contact(person_data):
    existing_cid = person_data.get("contact_id")
    if existing_cid:
        return existing_cid

    url = "https://api.apollo.io/v1/contacts"
    payload = {
        "first_name": person_data.get("first_name", ""),
        "last_name": person_data.get("last_name", ""),
        "title": person_data.get("title", ""),
        "email": person_data.get("email", ""),
        "organization_name": person_data.get("organization", {}).get("name", "") if person_data.get("organization") else "",
        "website_url": person_data.get("organization", {}).get("website_url", "") if person_data.get("organization") else "",
        "linkedin_url": person_data.get("linkedin_url", "")
    }
    r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        c = r.json().get("contact", {})
        return c.get("id")
    else:
        print(f"  Error creating contact: {r.status_code} - {r.text}")
        return None

def update_apollo_contact_custom_fields(contact_id, custom_fields):
    url = f"https://api.apollo.io/v1/contacts/{contact_id}"
    payload = {
        "typed_custom_fields": custom_fields
    }
    r = requests.put(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        return True, r.json().get("contact", {})
    return False, r.text

def main():
    print("==================================================")
    print("SCHEDULER 1: Sourcing 1 Net-New C2 Qualified Lead")
    print("==================================================")

    # 1. Deduplication
    print("\n1. Building Master Deduplication Sets...")
    zoho_token = get_zoho_token()
    z_emails, z_apollo_ids, z_comps = get_existing_zoho_records(zoho_token)
    print(f"  Zoho Records: {len(z_emails)} emails, {len(z_comps)} companies")

    a_emails, a_pids = get_existing_apollo_contacts()
    print(f"  Apollo Contacts: {len(a_emails)} emails, {len(a_pids)} person IDs")

    # 2. Search Apollo
    print("\n2. Sourcing C2 Candidates...")
    candidates = search_c2_candidates()
    print(f"  Total raw candidates retrieved: {len(candidates)}")

    seen_pids = set(a_pids)
    seen_orgs = set()
    filtered_pool = []

    for p in candidates:
        pid = p.get("id")
        if not pid or pid in seen_pids or pid in z_apollo_ids:
            continue
        seen_pids.add(pid)

        org = p.get("organization") or {}
        org_name = (org.get("name") or "").strip()
        if not org_name or org_name.lower() in z_comps or org_name.lower() in seen_orgs:
            continue

        seen_orgs.add(org_name.lower())
        filtered_pool.append(p)

    print(f"  Deduplicated raw pool: {len(filtered_pool)} candidates")

    # 3. Enrich and select the best candidate
    print("\n3. Enriching candidates to find qualified C2 lead...")
    selected_person = None
    for cand in filtered_pool:
        pid = cand.get("id")
        person = enrich_person(pid)
        if not person:
            continue

        email = (person.get("email") or "").lower().strip()
        if not email or "@" not in email:
            continue
        if email in z_emails or email in a_emails:
            continue

        org = person.get("organization") or {}
        emp = org.get("estimated_num_employees") or 0
        if emp < 10 or emp > 250:
            continue

        selected_person = person
        break

    if not selected_person:
        print("No qualified person found.")
        return

    first_name = selected_person.get("first_name")
    last_name = selected_person.get("last_name")
    title = selected_person.get("title")
    email = selected_person.get("email")
    org = selected_person.get("organization") or {}
    company_name = org.get("name")
    website = org.get("website_url")
    emp_count = org.get("estimated_num_employees")
    desc = org.get("short_description") or ""

    print(f"\nTarget Lead Selected:")
    print(f"  Name: {first_name} {last_name}")
    print(f"  Title: {title}")
    print(f"  Company: {company_name} ({emp_count} employees)")
    print(f"  Website: {website}")
    print(f"  Email: {email}")
    print(f"  Description: {desc[:200]}")

    # 4. Save to preview file
    with open("c2_candidate_preview.json", "w") as f:
        json.dump(selected_person, f, indent=2)
    print("\nSaved full profile to c2_candidate_preview.json")

if __name__ == "__main__":
    main()
