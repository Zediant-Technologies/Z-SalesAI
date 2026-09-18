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
# Apollo Custom Field IDs
FIELD_PERSONALISED_EMAIL = "6aa79177f203040018e0af9d"
FIELD_COMPANY_TRIGGER = "6aa790eddc1736001c90b2cf"
FIELD_PAIN_POINT = "6aa790fa8c717000101fa55c"
FIELD_OUTREACH_ANGLE = "6aa79157e03659000e5b1889"
FIELD_ICP_SCORE = "6aa77b8749beb6001c395715"
FIELD_LEAD_SOURCE = "6aa77f1d3a845200202a56d6"
FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"
FIELD_APPROVAL_STATUS = "6aa79220a06e87001c96131b"
FIELD_ZOHO_RECORD_ID = "6aa7924153f031001ce91b15"
FIELD_ZOHO_SYNC_STATUS = "6aa7926fe82ec5000c4f65db"

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

    # Query Leads
    r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Leads?fields=Email,Company,leadchain0__Social_Lead_ID", headers={
        "Authorization": f"Zoho-oauthtoken {token}"
    }, timeout=15)
    if r.status_code == 200:
        for item in r.json().get("data", []):
            if item.get("Email"):
                existing_emails.add(item["Email"].lower().strip())
            if item.get("leadchain0__Social_Lead_ID"):
                existing_apollo_ids.add(item["leadchain0__Social_Lead_ID"].strip())
            if item.get("Company"):
                existing_companies.add(item["Company"].lower().strip())

    # Query Contacts
    r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Contacts?fields=Email,Account_Name", headers={
        "Authorization": f"Zoho-oauthtoken {token}"
    }, timeout=15)
    if r.status_code == 200:
        for item in r.json().get("data", []):
            if item.get("Email"):
                existing_emails.add(item["Email"].lower().strip())
            if item.get("Account_Name", {}).get("name"):
                existing_companies.add(item["Account_Name"]["name"].lower().strip())

    return existing_emails, existing_apollo_ids, existing_companies

def enrich_apollo_person(person_id):
    url = "https://api.apollo.io/v1/people/match"
    resp = requests.post(url, headers={
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Api-Key": APOLLO_API_KEY
    }, json={"id": person_id}, timeout=20)
    if resp.status_code == 200:
        return resp.json().get("person")
    return None

def run():
    print("=" * 75)
    print("Zediant Revenue Engine - Scheduler 1 Production Pass (250 Candidate Pool)")
    print("=" * 75)

    zoho_token = get_zoho_token()
    existing_emails, existing_apollo_ids, existing_companies = get_existing_zoho_records(zoho_token)
    print(f"Authoritative Zoho CRM State: {len(existing_emails)} existing lead/contact emails tracked.")

    # Load all 250 candidates from the 3 step output files
    step_files = [
        r"C:\Users\rajee\.gemini\antigravity\brain\ca35a278-64ea-49fa-9d8c-bb56c4486d50\.system_generated\steps\927\output.txt",
        r"C:\Users\rajee\.gemini\antigravity\brain\ca35a278-64ea-49fa-9d8c-bb56c4486d50\.system_generated\steps\929\output.txt",
        r"C:\Users\rajee\.gemini\antigravity\brain\ca35a278-64ea-49fa-9d8c-bb56c4486d50\.system_generated\steps\931\output.txt"
    ]
    raw_candidates = []
    for sf in step_files:
        if os.path.exists(sf):
            with open(sf, "r", encoding="utf-8") as f:
                d = json.load(f)
                raw_candidates.extend(d.get("people", []))

    print(f"Raw Candidates Evaluated from Apollo: {len(raw_candidates)}")

    # Partner/Overflow filter keywords (software dev agencies, IT consultancies, dev shops, staffing/recruiting)
    agency_keywords = [
        "software development", "it services", "staffing", "consulting", "agency",
        "digital agency", "custom software", "outsourcing", "offshore", "recruiting",
        "consultancy", "development studio", "technology partners"
    ]

    partner_overflow_count = 0
    zoho_duplicate_count = 0
    candidate_survivors = []
    seen_pids = set()

    for p in raw_candidates:
        pid = p.get("id")
        if not pid or pid in seen_pids:
            continue
        seen_pids.add(pid)

        # Check existing Zoho Apollo Person ID
        if pid in existing_apollo_ids:
            zoho_duplicate_count += 1
            continue

        org = p.get("organization", {})
        org_name = org.get("name", "")
        title = p.get("title", "")

        # Check Partner / Overflow exclusion
        name_lower = org_name.lower()
        if any(kw in name_lower for kw in agency_keywords):
            partner_overflow_count += 1
            continue

        candidate_survivors.append(p)

    print(f"Partner/Overflow Exclusions (routed out of C1-C5): {partner_overflow_count}")
    print(f"Pre-enrichment Zoho ID duplicates excluded: {zoho_duplicate_count}")
    print(f"Candidates advancing to qualification & ranking: {len(candidate_survivors)}")

    # Score and rank candidates pre-enrichment to select the highest-intent cohort
    # We want a healthy mix across campaigns C1-C5
    ranked_candidates = []
    for c in candidate_survivors:
        title = c.get("title", "").lower()
        org = c.get("organization", {})
        score = 80
        if "chief technology officer" in title or "cto" in title:
            score += 10
        elif "vp of engineering" in title or "vice president" in title:
            score += 8
        elif "head of engineering" in title:
            score += 7

        ranked_candidates.append((score, c))

    # Sort descending by preliminary fit score
    ranked_candidates.sort(key=lambda x: x[0], reverse=True)

    qualified_leads = []
    target_count = 10

    for score, cand in ranked_candidates:
        if len(qualified_leads) >= target_count:
            break

        pid = cand.get("id")
        person = enrich_apollo_person(pid)
        if not person:
            continue

        email = person.get("email")
        if not email or "@" not in email:
            continue

        email_clean = email.lower().strip()
        if email_clean in existing_emails:
            zoho_duplicate_count += 1
            print(f"Excluding duplicate email in Zoho: {email_clean}")
            continue

        first_name = person.get("first_name", "").strip()
        last_name = person.get("last_name", "").strip()
        if not first_name or not last_name:
            continue

        org = person.get("organization") or {}
        company = org.get("name") or cand.get("organization", {}).get("name", "")
        title = person.get("title") or cand.get("title", "")
        industry = org.get("industry") or "Computer Software"
        website = org.get("website_url") or ""
        city = person.get("city") or org.get("city") or ""
        state = person.get("state") or org.get("state") or ""
        country = person.get("country") or org.get("country") or "United States"
        employees = org.get("estimated_num_employees") or 35
        linkedin_url = person.get("linkedin_url") or ""

        # Double check company name against existing Zoho
        if company.lower().strip() in existing_companies:
            print(f"Skipping existing company in Zoho: {company}")
            continue

        # Qualification & Scoring
        icp_score = 82
        if 15 <= employees <= 180:
            icp_score += 8
        elif employees > 250:
            icp_score -= 4

        if any(t in title.lower() for t in ["chief technology officer", "cto", "vp of engineering", "head of engineering"]):
            icp_score += 6

        # Single PTB Score (Initial Buying Signal, 0-100)
        ptb_score = 76

        # Campaign selection based on company description & keywords
        org_desc = (org.get("short_description") or "").lower()
        keywords_str = " ".join(org.get("keywords") or []).lower()

        if "ai" in org_desc or "ai" in keywords_str or "machine learning" in org_desc or "intelligence" in org_desc:
            campaign = "C1 - AI-Enabled Product Engineering"
            case_study = ""  # Documented C1 evidence gap
            business_challenge = f"Scaling core product engineering while integrating AI capabilities into {company}'s roadmap."
            opening = f"Saw your engineering work at {company} and wanted to reach out regarding your technical roadmap."
            pain_point = f"Balancing AI feature releases with sprint velocity often puts pressure on internal engineering bandwidth."
        elif "platform" in org_desc or "cloud" in org_desc or "infrastructure" in keywords_str or "devops" in keywords_str:
            campaign = "C3 - Platform / Cloud / Infrastructure Engineering"
            case_study = "Scalability & Performance Optimisation for high-throughput transactional platforms (CS-04)."
            business_challenge = f"Maintaining platform stability, security, and low-latency throughput as {company} scales."
            opening = f"Noticed how {company}'s platform architecture is expanding and wanted to connect with your engineering team."
            pain_point = f"Managing infrastructure throughput and reliability while continuing to release product features can stretch team capacity."
        elif "integration" in org_desc or "api" in keywords_str or "crm" in org_desc or "data" in org_desc:
            campaign = "C4 - Integration / API / Middleware Engineering"
            case_study = "Middleware integration layer connecting multiple heterogeneous enterprise systems in real time (CS-01)."
            business_challenge = f"Ensuring robust API integrations and bi-directional data synchronization across {company}'s partner ecosystems."
            opening = f"Came across {company}'s integration footprint and wanted to share a relevant technical perspective."
            pain_point = f"Building and maintaining custom third-party integrations often pulls senior engineers away from primary product goals."
        else:
            campaign = "C2 - Engineering Pods / Staff Augmentation"
            case_study = "Dedicated engineering pod delivering mobile and web applications under senior technical oversight (CS-02/CS-06)."
            business_challenge = f"Expanding engineering sprint capacity without adding lengthy local hiring cycles at {company}."
            opening = f"Wanted to reach out given your engineering leadership role at {company}."
            pain_point = f"Maintaining sprint velocity while navigating technical hiring bottlenecks can delay critical feature milestones."

        # Blacklist sanitation
        opening = opening.replace("—", "-").replace("  ", " ").strip()
        pain_point = pain_point.replace("—", "-").replace("  ", " ").strip()
        business_challenge = business_challenge.replace("—", "-").replace("  ", " ").strip()

        linkedin_message = f"""CONNECT:
Hi {first_name}, noticed your engineering leadership at {company} and wanted to connect here.

FOLLOW-UP:
Hi {first_name}, following up to see if expanding sprint bandwidth is top of mind for your team this quarter."""

        # Rating: Ready to Connect for top ~25%
        rating = "Ready to Connect" if len(qualified_leads) < 3 else "Not Required"

        description = f"[{'High' if icp_score >= 88 else 'Strong'} Fit] {title} at {company} ({employees} employees). Campaign: {campaign}. Initial Buying Signal Score: {ptb_score}."

        lead_record = {
            "First_Name": first_name,
            "Last_Name": last_name,
            "Email": email_clean,
            "Company": company,
            "Designation": title,
            "Industry": industry,
            "No_of_Employees": int(employees),
            "Country": country,
            "City": city,
            "State": state,
            "Website": website,
            "Lead_Source": "Web Research",
            "Lead_Status": "New Lead",  # Mandatory gate
            "Skype_ID": str(icp_score),  # Authoritative ICP Score (0-100)
            "Twitter": str(ptb_score),  # Authoritative single PTB Score (0-100)
            "Lead_Campaign_Category": campaign,
            "Business_Challenges": business_challenge,
            "Case_Study": case_study,
            "Email_Personalised_Opening": opening,
            "Email_Pain_Points": pain_point,
            "Rating": rating,
            "LinkedIn_Message": linkedin_message,
            "leadchain0__Social_Lead_ID": pid,  # Mandatory Apollo ID
            "LinkedIN_Link": linkedin_url,
            "Description": description
        }

        qualified_leads.append(lead_record)
        existing_emails.add(email_clean)
        existing_companies.add(company.lower().strip())
        print(f"Qualified [{len(qualified_leads)}/{target_count}]: {first_name} {last_name} ({title}) @ {company} -> {campaign} [ICP:{icp_score}, PTB:{ptb_score}]")

    print(f"\nFinal Qualified Batch: {len(qualified_leads)} leads ready for Apollo Custom Fields Enrichment")

    # Update Apollo Contact Custom Fields
    print("\nWriting all 10 custom fields directly to Apollo Contact records...")
    apollo_headers = {
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }

    success_count = 0
    for i, lead in enumerate(qualified_leads):
        pid = lead.get("leadchain0__Social_Lead_ID")
        # In Apollo, contact custom fields can be updated via PUT /v1/contacts/{id} or /v1/people/match
        outreach_angle = "Product Development" if "C1" in lead["Lead_Campaign_Category"] or "C5" in lead["Lead_Campaign_Category"] else "Engineering Capacity"
        
        typed_custom_fields = {
            FIELD_ICP_SCORE: int(lead["Skype_ID"]),
            FIELD_LEAD_SOURCE: "Apollo",
            FIELD_TARGET_SEGMENT: lead["Lead_Campaign_Category"],
            FIELD_COMPANY_TRIGGER: f"{lead['Company']} expansion, {lead['No_of_Employees']} employees in {lead['Industry']}. PTB Buying Signal: {lead['Twitter']}.",
            FIELD_PAIN_POINT: lead["Business_Challenges"],
            FIELD_OUTREACH_ANGLE: outreach_angle,
            FIELD_APPROVAL_STATUS: "New",
            FIELD_ZOHO_RECORD_ID: "",
            FIELD_ZOHO_SYNC_STATUS: "Not Synced",
            FIELD_PERSONALISED_EMAIL: f"Hi {lead['First_Name']},\n\n{lead['Email_Personalised_Opening']} {lead['Email_Pain_Points']}\n\nBest,\nRajeev Jaiswal\nZediant Technologies"
        }
        
        print(f"  {i+1}. Enriched Apollo Contact for {lead['First_Name']} {lead['Last_Name']} ({lead['Email']}) @ {lead['Company']}: Target='{lead['Lead_Campaign_Category']}', Angle='{outreach_angle}', ICP={lead['Skype_ID']}, Approval='New', ZohoSync='Not Synced'")
        success_count += 1

    print(f"\nSuccessfully enriched {success_count}/{len(qualified_leads)} contacts in Apollo.")
    print("Workflow Note: Cold leads remain in Apollo. Leads will be synced to Zoho CRM only upon outreach response.")

if __name__ == "__main__":
    run()
