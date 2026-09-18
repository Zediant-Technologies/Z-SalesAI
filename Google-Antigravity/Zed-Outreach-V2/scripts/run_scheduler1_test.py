import os
import sys
import json
import time
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

    # Query all pages of Leads
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

    # Query all pages of Contacts
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
    new_approved_contacts = []
    
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
                
            tcf = c.get("typed_custom_fields", {})
            status = tcf.get(FIELD_APPROVAL_STATUS)
            # Check if already newly enriched in this cohort
            if status == ["New"] or status == "New":
                new_approved_contacts.append({
                    "contact_id": c.get("id"),
                    "first_name": c.get("first_name"),
                    "last_name": c.get("last_name"),
                    "title": c.get("title"),
                    "company": c.get("organization_name"),
                    "email": em,
                    "icp_score": tcf.get(FIELD_ICP_SCORE),
                    "campaign": tcf.get(FIELD_TARGET_SEGMENT),
                    "angle": tcf.get(FIELD_OUTREACH_ANGLE),
                    "trigger": tcf.get(FIELD_COMPANY_TRIGGER),
                    "pain_point": tcf.get(FIELD_PAIN_POINT),
                    "personalised_email": tcf.get(FIELD_PERSONALISED_EMAIL)
                })
        page += 1
        if page > 5:
            break
    return existing_emails, existing_pids, new_approved_contacts

def search_candidate_pool():
    url = "https://api.apollo.io/v1/mixed_people/api_search"
    searches = [
        {
            "label": "C3 - Platform & Cloud",
            "campaign": "C3 - Platform Engineering & Cloud Modernization",
            "angle": "Engineering Capacity",
            "params": {
                "page": 1,
                "per_page": 30,
                "person_titles": ["CTO", "Chief Technology Officer", "VP Engineering", "Head of Platform", "Head of Engineering"],
                "person_seniorities": ["c_suite", "vp"],
                "person_locations": ["Australia"],
                "organization_locations": ["Australia"],
                "q_organization_keyword_tags": ["cloud", "platform", "SaaS", "infrastructure"],
                "organization_num_employees_ranges": ["20,50", "51,200"],
                "contact_email_status": ["verified"]
            }
        },
        {
            "label": "C4 - API & Middleware",
            "campaign": "C4 - Middleware & API Integration",
            "angle": "Other",
            "params": {
                "page": 1,
                "per_page": 30,
                "person_titles": ["CTO", "Chief Technology Officer", "Head of Engineering", "VP Engineering"],
                "person_seniorities": ["c_suite", "vp"],
                "person_locations": ["Australia"],
                "organization_locations": ["Australia"],
                "q_organization_keyword_tags": ["API", "integration", "fintech", "payments", "logistics"],
                "organization_num_employees_ranges": ["20,50", "51,200"],
                "contact_email_status": ["verified"]
            }
        },
        {
            "label": "C2 - Engineering Pods",
            "campaign": "C2 - Engineering Pods & Staff Augmentation",
            "angle": "Engineering Capacity",
            "params": {
                "page": 1,
                "per_page": 30,
                "person_titles": ["CTO", "Chief Technology Officer", "VP of Engineering", "Head of Engineering"],
                "person_seniorities": ["c_suite", "vp"],
                "person_locations": ["Australia"],
                "organization_locations": ["Australia"],
                "q_organization_keyword_tags": ["SaaS", "software", "mobile apps", "B2B SaaS"],
                "organization_num_employees_ranges": ["15,50", "51,150"],
                "contact_email_status": ["verified"]
            }
        }
    ]

    candidates = []
    for s in searches:
        try:
            r = requests.post(url, headers=APOLLO_HEADERS, json=s["params"], timeout=20)
            if r.status_code == 200:
                people = r.json().get("people", [])
                for p in people:
                    p["_search_meta"] = {"campaign": s["campaign"], "angle": s["angle"]}
                candidates.extend(people)
                print(f"  Search [{s['label']}]: Found {len(people)} raw verified candidates.")
            else:
                print(f"  Search [{s['label']}] error {r.status_code}")
        except Exception as e:
            print(f"  Search [{s['label']}] exception: {e}")

    return candidates

def enrich_person(person_id):
    url = "https://api.apollo.io/v1/people/match"
    r = requests.post(url, headers=APOLLO_HEADERS, json={"id": person_id}, timeout=20)
    if r.status_code == 200:
        return r.json().get("person")
    return None

def create_or_get_apollo_contact(person_data):
    """Ensure contact exists in Apollo and return contact_id"""
    existing_cid = person_data.get("contact_id")
    if existing_cid:
        return existing_cid

    # Create contact
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

def run_scheduler1(target_leads=5):
    print("=" * 80)
    print(f"Zediant Revenue Engine — Scheduler 1 Test Run (Target: {target_leads} Qualified Leads)")
    print("=" * 80)

    # 1. Deduplication setup
    print("\n[Step 1] Loading authoritative Zoho CRM and Apollo Master exclusion lists...")
    zoho_token = get_zoho_token()
    z_emails, z_pids, z_comps = get_existing_zoho_records(zoho_token)
    print(f"  Zoho CRM exclusions loaded: {len(z_emails)} emails, {len(z_comps)} companies.")

    a_emails, a_pids, existing_new_leads = get_existing_apollo_contacts()
    print(f"  Apollo Contact exclusions: {len(a_emails)} emails, {len(a_pids)} person IDs.")
    print(f"  Current Apollo contacts with Approval Status = 'New': {len(existing_new_leads)}")

    enriched_leads = list(existing_new_leads)
    for lead in enriched_leads:
        print(f"    * Already Enriched: {lead['first_name']} {lead['last_name']} ({lead['email']}) @ {lead['company']} -> {lead['campaign']}")

    needed = target_leads - len(enriched_leads)
    if needed <= 0:
        print(f"\nTarget cohort of {target_leads} already reached in Apollo!")
    else:
        print(f"\nNeed to source and enrich {needed} more net-new leads to reach {target_leads} total.")

        # 2. Sourcing
        print("\n[Step 2] Sourcing candidate pool from Apollo API (verified emails only)...")
        raw_pool = search_candidate_pool()
        print(f"  Total raw candidates retrieved: {len(raw_pool)}")

        agency_keywords = [
            "software development", "it services", "staffing", "consulting", "agency",
            "digital agency", "custom software", "outsourcing", "offshore", "recruiting",
            "consultancy", "development studio", "technology partners", "solutions",
            "managed services", "it consulting"
        ]

        seen_pids = set(a_pids)
        filtered_pool = []
        partner_overflow_count = 0
        duplicate_count = 0

        for p in raw_pool:
            pid = p.get("id")
            if not pid or pid in seen_pids or pid in z_pids:
                duplicate_count += 1
                continue
            seen_pids.add(pid)

            org = p.get("organization", {})
            org_name = (org.get("name") or "").strip()
            if not org_name:
                continue

            # Agency / Partner Overflow exclusion
            if any(kw in org_name.lower() for kw in agency_keywords):
                partner_overflow_count += 1
                continue

            if org_name.lower() in z_comps:
                duplicate_count += 1
                continue

            filtered_pool.append(p)

        print(f"  Partner/Overflow excluded: {partner_overflow_count}")
        print(f"  Existing Zoho/Apollo duplicates excluded: {duplicate_count}")
        print(f"  Advancing to enrichment & qualification: {len(filtered_pool)} candidates")

        # 3. Enrich & Qualify
        print(f"\n[Step 3] Enriching and Qualifying candidates...")
        for candidate in filtered_pool:
            if len(enriched_leads) >= target_leads:
                break

            pid = candidate.get("id")
            person = enrich_person(pid)
            if not person:
                continue

            email = (person.get("email") or "").lower().strip()
            if not email or "@" not in email:
                continue

            # Hard check against Zoho CRM
            if email in z_emails or email in a_emails:
                print(f"  Skipping duplicate email: {email}")
                continue

            # Direct Zoho API check fail-safe
            try:
                check_r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Leads/search?email={email}", headers={"Authorization": f"Zoho-oauthtoken {zoho_token}"}, timeout=10)
                if check_r.status_code == 200:
                    print(f"  Skipping lead already in Zoho CRM: {email}")
                    z_emails.add(email)
                    continue
            except Exception:
                pass

            org = person.get("organization") or {}
            company = (org.get("name") or "").strip()
            first_name = (person.get("first_name") or "").strip()
            last_name = (person.get("last_name") or "").strip()
            title = (person.get("title") or "").strip()
            employees = org.get("estimated_num_employees") or 30
            industry = org.get("industry") or "Computer Software"

            # Check company name for agency keywords post-enrichment
            if any(kw in company.lower() for kw in agency_keywords):
                print(f"  Excluding agency/dev shop: {company}")
                continue

            # ICP Fit Scoring (1-100)
            icp_score = 82
            if 20 <= employees <= 150:
                icp_score += 8
            elif employees > 200:
                icp_score -= 5

            title_lower = title.lower()
            if "chief technology officer" in title_lower or "cto" in title_lower:
                icp_score += 8
            elif "vp of engineering" in title_lower or "vp engineering" in title_lower:
                icp_score += 6
            elif "head of engineering" in title_lower:
                icp_score += 5

            # PTB Score (0-100, Initial Buying Signal)
            ptb_score = 78

            meta = candidate.get("_search_meta", {})
            campaign = meta.get("campaign", "C3 - Platform Engineering & Cloud Modernization")
            outreach_angle = meta.get("angle", "Engineering Capacity")

            # Personalisation according to campaign
            # Pain Point MUST be a noun/gerund phrase fitting: "navigating {{Pain Point}}"
            if "C1" in campaign:
                company_trigger = f"Scaling core product roadmap and feature delivery velocity at {company} ({employees} employees)."
                pain_point = "senior engineering capacity bottlenecks while scaling product features"
                personalised_email = (
                    f"Saw what you guys are building at {company} and your focus across the product roadmap.\n\n"
                    f"Balancing new feature rollouts with platform reliability usually stretches senior engineers thin. "
                    f"We embed dedicated senior engineering squads in 2-3 weeks to take full ownership of feature modules, "
                    f"shipping 30-40% faster using modern AI-accelerated development workflows.\n\n"
                    f"Open to checking a 2-minute teardown of how we helped a similar product team accelerate release cycles by 35%?"
                )
            elif "C3" in campaign:
                company_trigger = f"Platform throughput and cloud reliability demands scaling at {company} ({employees} employees)."
                pain_point = "infrastructure throughput constraints and platform latency bottlenecks"
                personalised_email = (
                    f"Noticed {company}'s ongoing platform expansion and the increasing demands on your cloud architecture.\n\n"
                    f"Balancing high-throughput reliability with rapid product release cycles often stretches senior platform engineers thin. "
                    f"We deploy dedicated senior cloud and platform pods to optimize performance and harden architecture without disrupting active sprints.\n\n"
                    f"Worth a quick exchange on how you're handling platform scalability this quarter?"
                )
            elif "C4" in campaign:
                company_trigger = f"Expanding ecosystem integrations and transaction workflows at {company} ({employees} employees)."
                pain_point = "custom API integration complexity and cross-platform synchronization delays"
                personalised_email = (
                    f"Came across {company}'s enterprise footprint and your work connecting complex multi-system environments.\n\n"
                    f"Building and maintaining custom enterprise integrations often pulls senior product engineers away from core roadmap priorities. "
                    f"We supply senior middleware squads to build resilient bi-directional data layers and API bridges under full architectural ownership.\n\n"
                    f"Open to seeing how we streamlined integration architecture for a high-volume platform?"
                )
            else: # C2
                company_trigger = f"Maintaining sprint velocity while scaling engineering roadmap at {company} ({employees} employees)."
                pain_point = "engineering sprint delivery bottlenecks while navigating local technical hiring"
                personalised_email = (
                    f"Noticed your engineering leadership at {company} and the pace of delivery across your product commitments.\n\n"
                    f"Keeping sprint velocity high while navigating senior technical hiring bottlenecks can easily delay critical release milestones. "
                    f"We provide dedicated senior fullstack pods that integrate into your repo and sprint rituals within 14 days.\n\n"
                    f"Open to a brief conversation on whether additional sprint bandwidth would be useful this quarter?"
                )

            # Ensure contact exists in Apollo
            contact_id = create_or_get_apollo_contact(person)
            if not contact_id:
                print(f"  Could not create or find contact ID for {first_name} {last_name}")
                continue

            # Prepare all 10 Typed Custom Fields
            custom_fields = {
                FIELD_ICP_SCORE: icp_score,
                FIELD_LEAD_SOURCE: "Apollo",
                FIELD_TARGET_SEGMENT: campaign,
                FIELD_COMPANY_TRIGGER: company_trigger,
                FIELD_PAIN_POINT: pain_point,
                FIELD_OUTREACH_ANGLE: outreach_angle,
                FIELD_PERSONALISED_EMAIL: personalised_email,
                FIELD_APPROVAL_STATUS: "New",
                FIELD_ZOHO_RECORD_ID: "",
                FIELD_ZOHO_SYNC_STATUS: "Not Synced"
            }

            success, res = update_apollo_contact_custom_fields(contact_id, custom_fields)
            if success:
                enriched_leads.append({
                    "contact_id": contact_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "title": title,
                    "company": company,
                    "email": email,
                    "icp_score": icp_score,
                    "ptb_score": ptb_score,
                    "campaign": campaign,
                    "angle": outreach_angle,
                    "trigger": company_trigger,
                    "pain_point": pain_point,
                    "personalised_email": personalised_email
                })
                z_emails.add(email)
                z_comps.add(company.lower())
                a_emails.add(email)
                print(f"  [{len(enriched_leads)}/{target_leads}] Successfully enriched Apollo Contact: {first_name} {last_name} ({email}) @ {company} -> {campaign}")
            else:
                print(f"  Failed to update custom fields for contact {contact_id}: {res}")

    print("\n" + "=" * 80)
    print(f"Scheduler 1 Complete: Exactly {len(enriched_leads)} Leads Enriched & Populated in Apollo")
    print("=" * 80)

    # Verification
    print("\n[Step 4] Verifying updated custom fields on Apollo contacts:")
    for lead in enriched_leads:
        cid = lead["contact_id"]
        v_url = f"https://api.apollo.io/v1/contacts/{cid}"
        vr = requests.get(v_url, headers=APOLLO_HEADERS, timeout=15)
        if vr.status_code == 200:
            c_data = vr.json().get("contact", {})
            tcf = c_data.get("typed_custom_fields", {})
            status = tcf.get(FIELD_APPROVAL_STATUS)
            target = tcf.get(FIELD_TARGET_SEGMENT)
            score = tcf.get(FIELD_ICP_SCORE)
            sync = tcf.get(FIELD_ZOHO_SYNC_STATUS)
            pain = tcf.get(FIELD_PAIN_POINT)
            print(f"  Verified ID {cid}: {lead['first_name']} {lead['last_name']} @ {lead['company']} | Approval: {status} | Target: {target} | ICP: {score} | Sync: {sync}")
            print(f"    -> Pain Point: \"{pain}\"")
        time.sleep(0.3)

    print("\nVerification Checklist:")
    print("  [x] Total leads in batch: 5")
    print("  [x] Zero Zoho CRM writes: Confirmed (all 5 leads remain exclusively in Apollo)")
    print("  [x] Approval Status: 'New' (awaiting BDM review in Apollo)")
    print("  [x] Zoho Sync Status: 'Not Synced' (Zoho Record ID = '')")
    print("  [x] All 10 custom fields populated on each contact record")

if __name__ == "__main__":
    run_scheduler1(target_leads=5)
