import os
import sys
import json
import time
import re
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

def clean_company_name(name):
    if not name:
        return ""
    clean = re.sub(r'\b(Pty\s+Ltd\.?|Pty\.?\s+Ltd\.?|Pty\.?|Ltd\.?|Inc\.?|LLC|Corp\.?|Corporation|Co\.?)\b', '', name, flags=re.IGNORECASE)
    clean = re.sub(r'\s+', ' ', clean).strip(' ,.-')
    return clean

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
                existing_companies.add(clean_company_name(item["Company"]).lower())
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
                existing_companies.add(clean_company_name(item["Account_Name"]["name"]).lower())
        page += 1

    return existing_emails, existing_apollo_ids, existing_companies

def get_existing_apollo_contacts():
    existing_emails = set()
    existing_pids = set()
    existing_companies = set()
    
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
            comp = clean_company_name(c.get("organization_name") or "")
            if comp:
                existing_companies.add(comp.lower())
        page += 1
        if page > 10:
            break
    return existing_emails, existing_pids, existing_companies

def search_candidates_for_geo(geo_name, country_param, search_configs):
    url = "https://api.apollo.io/v1/mixed_people/api_search"
    candidates = []
    for sc in search_configs:
        payload = {
            "page": 1,
            "per_page": 20,
            "person_titles": ["CTO", "Chief Technology Officer", "VP of Engineering", "VP Engineering", "Head of Engineering", "Chief Operating Officer"],
            "person_seniorities": ["c_suite", "vp", "head"],
            "person_locations": [country_param],
            "organization_locations": [country_param],
            "contact_email_status": ["verified"],
            "organization_num_employees_ranges": ["20,50", "51,200"],
            "q_organization_keyword_tags": sc["keywords"]
        }
        try:
            r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
            if r.status_code == 200:
                people = r.json().get("people", [])
                for p in people:
                    p["_geo"] = geo_name
                    p["_campaign_hint"] = sc["campaign_hint"]
                    p["_angle_hint"] = sc["angle_hint"]
                candidates.extend(people)
                print(f"  [{geo_name}] {sc['label']}: retrieved {len(people)} raw verified candidates.")
            else:
                print(f"  [{geo_name}] {sc['label']} HTTP error: {r.status_code}")
        except Exception as e:
            print(f"  [{geo_name}] {sc['label']} exception: {e}")
    return candidates

def enrich_person(person_id):
    url = "https://api.apollo.io/v1/people/match"
    r = requests.post(url, headers=APOLLO_HEADERS, json={"id": person_id}, timeout=20)
    if r.status_code == 200:
        return r.json().get("person")
    return None

def create_or_get_apollo_contact(person_data, clean_org_name):
    existing_cid = person_data.get("contact_id")
    if existing_cid:
        return existing_cid

    # Search existing contact by email
    search_url = "https://api.apollo.io/v1/contacts/search"
    sr = requests.post(search_url, headers=APOLLO_HEADERS, json={"q_keywords": person_data.get("email", "")}, timeout=15)
    if sr.status_code == 200:
        c_list = sr.json().get("contacts", [])
        if c_list:
            return c_list[0].get("id")

    url = "https://api.apollo.io/v1/contacts"
    payload = {
        "first_name": person_data.get("first_name", ""),
        "last_name": person_data.get("last_name", ""),
        "title": person_data.get("title", ""),
        "email": person_data.get("email", ""),
        "organization_name": clean_org_name,
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
    payload = {"typed_custom_fields": custom_fields}
    r = requests.put(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        return True, r.json().get("contact", {})
    return False, r.text

def run_scheduler_geo():
    print("=" * 80)
    print("Zediant Revenue Engine — Scheduler 1 Lead Factory (AUS, UAE, US)")
    print("=" * 80)

    # Step 1: Deduplication master sets
    print("\n[Step 1] Loading master deduplication exclusions from Zoho CRM and Apollo...")
    zoho_token = get_zoho_token()
    z_emails, z_pids, z_comps = get_existing_zoho_records(zoho_token)
    print(f"  Zoho CRM exclusions: {len(z_emails)} emails, {len(z_comps)} companies.")

    a_emails, a_pids, a_comps = get_existing_apollo_contacts()
    print(f"  Apollo exclusions: {len(a_emails)} emails, {len(a_comps)} companies.")

    # Agency keywords for Partner/Overflow exclusion
    agency_keywords = [
        "software development", "it services", "staffing", "consulting", "agency",
        "digital agency", "custom software", "outsourcing", "offshore", "recruiting",
        "consultancy", "development studio", "technology partners", "solutions",
        "managed services", "it consulting", "marketing agency", "creative agency",
        "software engineering agency", "talent", "staff"
    ]

    # Search configurations across AUS, UAE, US
    geo_searches = {
        "UAE": {
            "country": "United Arab Emirates",
            "searches": [
                {
                    "label": "C1/C4 - FinTech, Payments & Logistics SaaS",
                    "campaign_hint": "C1 - AI-Enabled Product Engineering",
                    "angle_hint": "Product Development",
                    "keywords": ["fintech", "payments", "logistics", "SaaS"]
                },
                {
                    "label": "C3/C4 - Cloud Platforms & Infrastructure",
                    "campaign_hint": "C3 - Platform Engineering & Cloud Modernization",
                    "angle_hint": "Engineering Capacity",
                    "keywords": ["cloud", "platform", "infrastructure", "DevOps"]
                },
                {
                    "label": "C2/C5 - Enterprise Product & Digital Platforms",
                    "campaign_hint": "C2 - Engineering Pods & Staff Augmentation",
                    "angle_hint": "Engineering Capacity",
                    "keywords": ["enterprise software", "proptech", "e-commerce platform"]
                }
            ]
        },
        "AUS": {
            "country": "Australia",
            "searches": [
                {
                    "label": "C1 - AI & Product Engineering",
                    "campaign_hint": "C1 - AI-Enabled Product Engineering",
                    "angle_hint": "Product Development",
                    "keywords": ["AI", "fintech", "machine learning", "product"]
                },
                {
                    "label": "C4 - Integration & API Middleware",
                    "campaign_hint": "C4 - Middleware & API Integration (ZCoupler)",
                    "angle_hint": "Other",
                    "keywords": ["API", "integration", "payments", "fintech"]
                },
                {
                    "label": "C3/C2 - Cloud & Engineering Pods",
                    "campaign_hint": "C3 - Platform Engineering & Cloud Modernization",
                    "angle_hint": "Engineering Capacity",
                    "keywords": ["SaaS", "platform", "cloud", "B2B SaaS"]
                }
            ]
        },
        "US": {
            "country": "United States",
            "searches": [
                {
                    "label": "C1/C2 - FinTech & HealthTech Product SaaS",
                    "campaign_hint": "C1 - AI-Enabled Product Engineering",
                    "angle_hint": "Product Development",
                    "keywords": ["fintech", "healthtech", "SaaS", "B2B"]
                },
                {
                    "label": "C3 - Cloud Infrastructure & Platform SaaS",
                    "campaign_hint": "C3 - Platform Engineering & Cloud Modernization",
                    "angle_hint": "Engineering Capacity",
                    "keywords": ["cloud", "platform", "infrastructure", "security"]
                },
                {
                    "label": "C4/C5 - Enterprise API & System Modernization",
                    "campaign_hint": "C4 - Middleware & API Integration (ZCoupler)",
                    "angle_hint": "Other",
                    "keywords": ["enterprise software", "API", "integration", "logistics"]
                }
            ]
        }
    }

    # Step 2: Retrieve raw candidates per geo
    print("\n[Step 2] Sourcing candidate pool from Apollo API across AUS, UAE, and US...")
    raw_by_geo = {}
    for geo, cfg in geo_searches.items():
        print(f"\nSearching {geo} ({cfg['country']})...")
        raw_by_geo[geo] = search_candidates_for_geo(geo, cfg["country"], cfg["searches"])
        print(f"Total raw candidates for {geo}: {len(raw_by_geo[geo])}")

    # Step 3: Screen & Filter per geo
    print("\n[Step 3] Cheap pre-screening: Deduplication and Partner/Overflow routing...")
    seen_pids = set(a_pids).union(z_pids)
    seen_comps = set(a_comps).union(z_comps)

    filtered_by_geo = {}
    for geo, cands in raw_by_geo.items():
        valid = []
        for p in cands:
            pid = p.get("id")
            if not pid or pid in seen_pids:
                continue

            org = p.get("organization") or {}
            org_name = org.get("name") or ""
            clean_org = clean_company_name(org_name)
            if not clean_org:
                continue

            clean_lower = clean_org.lower()
            if clean_lower in seen_comps:
                continue

            # Agency / dev shop check
            if any(kw in clean_lower for kw in agency_keywords):
                continue
            desc = (org.get("short_description") or "").lower()
            if any(kw in desc for kw in ["we are a software development agency", "custom software development company", "it consulting firm", "staffing agency"]):
                continue

            title = (p.get("title") or "").lower()
            # Prioritize senior tech leadership
            score = 75
            if "chief technology officer" in title or "cto" in title:
                score += 15
            elif "vp of engineering" in title or "vp engineering" in title:
                score += 12
            elif "head of engineering" in title:
                score += 10
            elif "chief operating officer" in title or "coo" in title:
                score += 8

            p["_pre_score"] = score
            p["_clean_org"] = clean_org
            valid.append(p)

        # Sort descending by preliminary score
        valid.sort(key=lambda x: x["_pre_score"], reverse=True)
        filtered_by_geo[geo] = valid
        print(f"  {geo}: {len(valid)} verified non-agency candidates ready for enrichment.")

    # Step 4: Select balanced cohort (Target: ~3 UAE, ~3 AUS, ~3-4 US = Total 9-10 leads)
    print("\n[Step 4] Selecting and enriching high-intent cohort across AUS, UAE, and US...")
    target_quotas = {"UAE": 3, "AUS": 3, "US": 4}
    enriched_cohort = []

    for geo, target in target_quotas.items():
        print(f"\nProcessing {geo} (Target: {target})...")
        geo_count = 0
        for cand in filtered_by_geo[geo]:
            if geo_count >= target:
                break

            pid = cand.get("id")
            clean_org = cand["_clean_org"]
            clean_lower = clean_org.lower()

            if clean_lower in seen_comps:
                continue

            person = enrich_person(pid)
            if not person:
                continue

            email = (person.get("email") or "").lower().strip()
            if not email or "@" not in email:
                continue

            if email in z_emails or email in a_emails:
                continue

            first_name = (person.get("first_name") or "").strip()
            last_name = (person.get("last_name") or "").strip()
            title = (person.get("title") or cand.get("title") or "").strip()
            org = person.get("organization") or cand.get("organization") or {}
            employees = org.get("estimated_num_employees") or 35
            industry = org.get("industry") or "Computer Software"
            website = org.get("website_url") or ""
            linkedin_url = person.get("linkedin_url") or ""
            city = person.get("city") or org.get("city") or ""
            state = person.get("state") or org.get("state") or ""
            country = person.get("country") or org.get("country") or cand.get("_geo")

            # Final agency guard
            if any(kw in clean_lower for kw in agency_keywords):
                continue

            # ICP Fit Scoring (1-100)
            icp_score = 80
            if 20 <= employees <= 180:
                icp_score += 10
            elif employees > 200:
                icp_score -= 4

            t_low = title.lower()
            if "chief technology officer" in t_low or "cto" in t_low:
                icp_score += 6
            elif "vp" in t_low or "head of engineering" in t_low:
                icp_score += 4

            if geo in ["AUS", "UAE"]:
                icp_score += 4  # Primary geographic markets
            else:
                icp_score += 2

            icp_score = min(98, max(75, icp_score))

            # PTB Score (0-100, Initial Buying Signal)
            ptb_score = 78
            if employees > 30:
                ptb_score += 4

            # Determine Campaign and Personalization
            desc = (org.get("short_description") or "").lower()
            keywords = [k.lower() for k in (org.get("keywords") or [])]
            kw_str = " ".join(keywords)

            camp_hint = cand.get("_campaign_hint", "")
            angle_hint = cand.get("_angle_hint", "")

            # Decide campaign based on actual domain & description
            if "ai" in desc or "machine learning" in desc or "intelligence" in desc or "C1" in camp_hint:
                campaign = "C1 - AI-Enabled Product Engineering"
                angle = "Product Development"
                core_domain = "AI-driven product capabilities and automated workflows"
                company_trigger = f"Scaling core product roadmap and AI feature velocity"
                pain_point = "senior engineering capacity bottlenecks while scaling product features"
                beat1 = f"Saw what you guys are building with {clean_org}'s product platform and your focus across the engineering roadmap."
                beat2 = f"Rolling out new feature capabilities while keeping core platform performance fast usually pulls senior developers in two directions. We embed dedicated senior engineering squads in 2-3 weeks to take full architectural ownership of modules, shipping 30-40% faster using modern workflows."
                beat3 = f"Open to checking a 2-minute teardown of how we helped a similar product team accelerate release velocity by 35%?"

            elif "cloud" in desc or "infrastructure" in desc or "devops" in desc or "platform" in desc or "C3" in camp_hint:
                campaign = "C3 - Platform Engineering & Cloud Modernization"
                angle = "Engineering Capacity"
                company_trigger = f"Platform throughput and cloud reliability demands scaling"
                pain_point = "infrastructure throughput constraints and platform latency bottlenecks"
                beat1 = f"Noticed {clean_org}'s platform architecture and the increasing throughput demands on your cloud infrastructure."
                beat2 = f"Balancing high-throughput reliability with rapid product release cycles often stretches senior platform engineers thin. We deploy dedicated senior cloud and platform squads to harden architecture and automate CI/CD without disrupting active sprints."
                beat3 = f"Worth a brief exchange on how you're handling platform scalability this quarter?"

            elif "integration" in desc or "api" in desc or "payments" in desc or "crm" in desc or "C4" in camp_hint:
                campaign = "C4 - Middleware & API Integration (ZCoupler)"
                angle = "Other"
                company_trigger = f"Expanding ecosystem integrations and multi-system data flows"
                pain_point = "custom API integration complexity and cross-platform synchronization delays"
                beat1 = f"Came across {clean_org}'s platform footprint and your work connecting complex multi-system transaction environments."
                beat2 = f"Building and maintaining custom partner integrations often pulls senior product engineers away from core roadmap priorities. We supply senior middleware squads to build resilient bi-directional data bridges under full architectural ownership."
                beat3 = f"Open to seeing how we streamlined integration architecture for a high-volume platform?"

            elif "modern" in desc or "legacy" in desc or "enterprise" in desc or "C5" in camp_hint:
                campaign = "C5 - Enterprise Custom Development & Modernization"
                angle = "Product Development"
                company_trigger = f"Modernizing enterprise systems and legacy core workflows"
                pain_point = "legacy system modernization drag and technical debt accumulation"
                beat1 = f"Saw {clean_org}'s focus on modernizing core enterprise systems and expanding customer-facing capabilities."
                beat2 = f"Refactoring legacy architectures while maintaining day-to-day business continuity can easily stall strategic feature development. We embed senior engineering squads to incrementally decouple monoliths and accelerate delivery without operational disruption."
                beat3 = f"Open to checking a 2-minute teardown of how we helped an enterprise team modernize legacy systems 40% faster?"

            else:
                campaign = "C2 - Engineering Pods & Staff Augmentation"
                angle = "Engineering Capacity"
                company_trigger = f"Maintaining sprint velocity while scaling engineering roadmap"
                pain_point = "engineering sprint delivery bottlenecks while navigating technical hiring"
                beat1 = f"Noticed your engineering leadership at {clean_org} and the pace of delivery across your product roadmap."
                beat2 = f"Keeping sprint velocity high while navigating senior technical hiring bottlenecks can easily delay critical release milestones. We provide dedicated senior fullstack pods that integrate into your repo and sprint rituals within 14 days."
                beat3 = f"Open to a brief conversation on whether additional sprint bandwidth would be useful this quarter?"

            personalised_email = f"{beat1}\n\n{beat2}\n\n{beat3}"

            # Ensure contact in Apollo
            person_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "title": title,
                "email": email,
                "linkedin_url": linkedin_url,
                "organization": org
            }
            cid = create_or_get_apollo_contact(person_dict, clean_org)
            if not cid:
                print(f"  Failed to get/create contact ID for {first_name} {last_name}")
                continue

            custom_fields = {
                FIELD_ICP_SCORE: icp_score,
                FIELD_LEAD_SOURCE: ["Apollo"],
                FIELD_TARGET_SEGMENT: campaign,
                FIELD_COMPANY_TRIGGER: company_trigger,
                FIELD_PAIN_POINT: pain_point,
                FIELD_OUTREACH_ANGLE: [angle],
                FIELD_PERSONALISED_EMAIL: personalised_email,
                FIELD_APPROVAL_STATUS: ["New"],
                FIELD_ZOHO_RECORD_ID: "",
                FIELD_ZOHO_SYNC_STATUS: ["Not Synced"]
            }

            success, updated_data = update_apollo_contact_custom_fields(cid, custom_fields)
            if success:
                # Populate native 'Sequences' field by adding contact to corresponding Apollo sequence
                seq_map = {
                    "C1": "6aa7ec0e7c0f80000cbd7600",
                    "C2": "6aa7eca553473f000c678940",
                    "C3": "6aa7ecb31fd57300143fbfa7",
                    "C4": "6aa7ecbea907dd00140753b2",
                    "C5": "6aa7ecc953473f000c678b8e"
                }
                camp_key = campaign[:2]
                seq_id = seq_map.get(camp_key)
                if seq_id:
                    try:
                        s_url = f"https://api.apollo.io/v1/emailer_campaigns/{seq_id}/add_contact_ids"
                        requests.post(s_url, headers=APOLLO_HEADERS, json={
                            "contact_ids": [cid],
                            "emailer_campaign_id": seq_id,
                            "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
                            "sequence_active_in_other_campaigns": False
                        }, timeout=15)
                    except Exception:
                        pass

                geo_count += 1
                seen_comps.add(clean_lower)
                seen_pids.add(pid)
                a_emails.add(email)
                record_summary = {
                    "geo": geo,
                    "contact_id": cid,
                    "first_name": first_name,
                    "last_name": last_name,
                    "title": title,
                    "company": clean_org,
                    "email": email,
                    "campaign": campaign,
                    "angle": angle,
                    "icp_score": icp_score,
                    "ptb_score": ptb_score,
                    "trigger": company_trigger,
                    "pain_point": pain_point,
                    "personalised_email": personalised_email
                }
                enriched_cohort.append(record_summary)
                print(f"  [{geo} {geo_count}/{target}] Populated Apollo Contact {cid}: {first_name} {last_name} ({email}) @ {clean_org} -> {campaign} (Sequences & Custom Fields set)")
            else:
                print(f"  Failed to update Apollo custom fields for {cid}: {updated_data}")

    print("\n" + "=" * 80)
    print(f"Scheduler 1 Complete: {len(enriched_cohort)} Qualified Leads Populated in Apollo")
    print("=" * 80)

    # Verification pass
    print("\n[Step 5] Verifying enriched contacts directly from Apollo API:")
    for lead in enriched_cohort:
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
            print(f"  [{lead['geo']}] ID {cid}: {lead['first_name']} {lead['last_name']} @ {lead['company']}")
            print(f"    Target: {target} | ICP: {score} | Approval: {status} | Zoho Sync: {sync}")
            print(f"    Pain Point: \"{pain}\"")
        time.sleep(0.3)

    return enriched_cohort

if __name__ == "__main__":
    run_scheduler_geo()
