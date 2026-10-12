import os
import sys
import json
import time
import re
import requests
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")
ZOHO_API_DOMAIN = os.getenv("ZOHO_API_DOMAIN", "https://www.zohoapis.in")

# Custom Field IDs in Apollo
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

SEQUENCE_MAP = {
    "C1": "6aa7ec0e7c0f80000cbd7600",
    "C2": "6aa7eca553473f000c678940",
    "C3": "6aa7ecb31fd57300143fbfa7",
    "C4": "6aa7ecbea907dd00140753b2",
    "C5": "6aa7ecc953473f000c678b8e"
}

APOLLO_HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

GENERIC_KWS = {
    'saas', 'software', 'technology', 'enterprise', 'platform', 'b2b', 'services',
    'computer software', 'enterprises', 'information technology & services',
    'analytics', 'ux', 'user experience', 'business intelligence', 'cloud',
    'it', 'management', 'digital', 'consulting', 'solutions', 'app', 'application',
    'mobile', 'web', 'internet', 'online', 'data', 'security', 'compliance',
    'australia', 'united states', 'uae', 'dubai', 'sydney', 'melbourne', 'global',
    'corporation', 'business', 'customers', 'clients', 'products', 'commercial',
    'go to market', 'gtm', 'marketing', 'sales', 'strategy', 'innovation', 'leadership',
    'growth', 'lead generation', 'social media', 'seo', 'sem', 'advertising',
    'b2c', 'b2b saas', 'enterprise software', 'software solutions'
}

def clean_company_name(name):
    if not name:
        return ""
    clean = re.sub(r'\b(Pty\s+Ltd\.?|Pty\.?\s+Ltd\.?|Pty\.?|Ltd\.?|Inc\.?|LLC|Corp\.?|Corporation|Co\.?|PSC|OPC|FZE|FZ-LLC|L\.L\.C\.?|LLC)\b', '', name, flags=re.IGNORECASE)
    clean = re.sub(r'\s+', ' ', clean).strip(' ,.-')
    return clean

def get_zoho_token():
    try:
        r = requests.post(f"{ZOHO_ACCOUNTS_URL}/token", data={
            "grant_type": "refresh_token",
            "client_id": ZOHO_CLIENT_ID,
            "client_secret": ZOHO_CLIENT_SECRET,
            "refresh_token": ZOHO_REFRESH_TOKEN
        }, timeout=15)
        data = r.json()
        return data.get("access_token")
    except Exception as e:
        print(f"Warning: Could not refresh Zoho token: {e}")
        return None

def get_existing_zoho_records(token):
    existing_emails = set()
    existing_companies = set()
    if not token:
        return existing_emails, existing_companies

    try:
        page = 1
        while True:
            r = requests.get(f"{ZOHO_API_DOMAIN}/crm/v2/Leads?fields=Email,Company&page={page}&per_page=200", headers={
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
                if item.get("Company"):
                    existing_companies.add(clean_company_name(item["Company"]).lower())
            page += 1
    except Exception as e:
        print(f"Warning loading Zoho leads: {e}")

    return existing_emails, existing_companies

def get_existing_apollo_contacts():
    existing_emails = set()
    existing_pids = set()
    existing_companies = set()
    
    url = "https://api.apollo.io/v1/contacts/search"
    page = 1
    while True:
        r = requests.post(url, headers=APOLLO_HEADERS, json={"page": page, "per_page": 100}, timeout=20)
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

def search_raw_candidates(country, keyword_groups):
    url = "https://api.apollo.io/v1/mixed_people/api_search"
    all_people = []
    seen_ids = set()

    for kw in keyword_groups:
        for page in range(1, 6):
            payload = {
                "page": page,
                "per_page": 50,
                "person_titles": [
                    "CTO", "Chief Technology Officer", "VP of Engineering", "VP Engineering",
                    "Head of Engineering", "Chief Operating Officer", "Director of Engineering",
                    "Head of Technology", "VP Technology", "VP of Technology"
                ],
                "person_seniorities": ["c_suite", "vp", "head", "director"],
                "person_locations": [country],
                "organization_locations": [country],
                "contact_email_status": ["verified"],
                "organization_num_employees_ranges": ["15,50", "51,200", "201,500"],
                "q_organization_keyword_tags": kw
            }
            try:
                r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
                if r.status_code == 200:
                    people = r.json().get("people", [])
                    for p in people:
                        pid = p.get("id")
                        if pid and pid not in seen_ids:
                            seen_ids.add(pid)
                            p["_search_kw"] = kw
                            all_people.append(p)
                    if len(people) < 50:
                        break
                else:
                    break
            except Exception as e:
                print(f"  Search error: {e}")
                break
            time.sleep(0.3)
    return all_people

def enrich_person(person_id):
    url = "https://api.apollo.io/v1/people/match"
    try:
        r = requests.post(url, headers=APOLLO_HEADERS, json={"id": person_id}, timeout=20)
        if r.status_code == 200:
            return r.json().get("person")
    except Exception:
        pass
    return None

def extract_clean_nouns(keywords):
    valid = []
    for k in keywords:
        k_clean = k.strip().lower()
        if k_clean in GENERIC_KWS:
            continue
        words = k_clean.split()
        if len(words) > 4 or len(k_clean) < 3:
            continue
        if any(bad in k_clean for bad in ['marketing', 'sales', 'gtm', 'strategy', 'recruiting', 'staffing', 'agency', 'consulting']):
            continue
        if all(w in GENERIC_KWS for w in words):
            continue
        valid.append(k_clean)
    return valid

def determine_campaign_and_copy(org_name, org_desc, keywords, tech_list, title):
    desc_low = (org_desc or "").lower()
    raw_kws_str = " ".join(keywords).lower()
    clean_kws = extract_clean_nouns(keywords)
    
    # Identify primary domain nouns for research grounding
    domain_nouns = []
    for k in clean_kws:
        if len(k.split()) >= 2:
            domain_nouns.append(k)
    if not domain_nouns and clean_kws:
        domain_nouns = clean_kws[:2]

    # Concrete noun fallback from tech
    valid_tech = [t for t in tech_list if t not in ['AIOSEO', 'Akismet', 'All in One SEO', 'Google Analytics', 'Google Tag Manager', 'WordPress.org', 'reCAPTCHA', 'Font Awesome', 'Yoast SEO']]
    tech_str = " and ".join(valid_tech[:2]) if valid_tech else ""

    # Campaign classification & research-grounded copy
    if any(term in desc_low or term in raw_kws_str for term in ["artificial intelligence", "machine learning", "generative ai", "ai platform", "ai-powered", "deep learning", "llm", "analytics ai", "predictive"]):
        camp_code = "C1"
        campaign = "C1 - AI-Enabled Product Engineering"
        angle = "Product Development"
        
        if domain_nouns:
            feature_noun = domain_nouns[0]
            beat1 = f"Noticed {org_name}'s recent work scaling {feature_noun} across your product platform."
            trigger = f"scaling {feature_noun} capabilities and automated product workflows"
            pain_point = f"senior engineering capacity bottlenecks while scaling {feature_noun} workflows"
        elif tech_str:
            beat1 = f"Saw {org_name}'s platform architecture is heavily built around {tech_str}."
            trigger = f"scaling core product workflows and {tech_str} architecture"
            pain_point = f"senior engineering capacity bottlenecks while scaling core product modules"
        else:
            beat1 = f"Noticed {org_name}'s recent expansion scaling automated feature workflows for enterprise users."
            trigger = f"scaling core feature capabilities and automated product workflows"
            pain_point = f"senior engineering capacity bottlenecks while rolling out core product modules"

        beat2 = "When roadmap pressure spikes, your best engineers often get stuck firefighting maintenance instead of shipping core features. We embed dedicated senior engineering pods in 10 days to take full ownership of modules and ship 30-40% faster using AI-assisted delivery workflows."
        beat3 = "Happy to share a 2-minute breakdown on how this works in practice?"

    elif any(term in desc_low or term in raw_kws_str for term in ["cloud", "infrastructure", "devops", "kubernetes", "platform architecture", "cloud security", "microservices", "telemetry", "sre", "observability"]):
        camp_code = "C3"
        campaign = "C3 - Platform Engineering & Cloud Modernization"
        angle = "Engineering Capacity"
        
        if domain_nouns:
            feature_noun = domain_nouns[0]
            beat1 = f"Noticed {org_name}'s platform architecture and the increasing demands across your {feature_noun} infrastructure."
            trigger = f"scaling {feature_noun} infrastructure and platform throughput"
            pain_point = f"infrastructure throughput constraints and {feature_noun} latency bottlenecks"
        elif tech_str:
            beat1 = f"Saw {org_name}'s cloud infrastructure is built around {tech_str}."
            trigger = f"platform throughput demands across {tech_str} infrastructure"
            pain_point = f"deployment pipeline friction and infrastructure scaling constraints"
        else:
            beat1 = f"Noticed {org_name}'s platform architecture and the increasing throughput demands on your cloud infrastructure."
            trigger = f"platform throughput demands and cloud infrastructure scaling"
            pain_point = f"infrastructure throughput constraints and platform latency bottlenecks"

        beat2 = "When deployment pipelines lag, senior developers end up babysitting releases and troubleshooting builds instead of shipping features. We embed dedicated senior DevOps pods in 10 days to automate CI/CD and eliminate deployment friction."
        beat3 = "Happy to send over a 2-minute breakdown of how the pod model works?"

    elif any(term in desc_low or term in raw_kws_str for term in ["api", "integration", "payments", "payment", "middleware", "fintech", "payroll", "edi", "banking", "billing", "gateway"]):
        camp_code = "C4"
        campaign = "C4 - Middleware & API Integration (ZCoupler)"
        angle = "Other"
        
        if domain_nouns:
            feature_noun = domain_nouns[0]
            beat1 = f"Saw {org_name}'s platform footprint and your focus connecting multi-system {feature_noun} data flows."
            trigger = f"scaling {feature_noun} API integrations and transaction data workflows"
            pain_point = f"custom API integration complexity across {feature_noun} workflows"
        else:
            beat1 = f"Saw {org_name}'s platform footprint and your work connecting complex multi-system environments."
            trigger = f"expanding ecosystem partner integrations and transaction data workflows"
            pain_point = f"custom API integration complexity and cross-platform synchronization delays"

        beat2 = "Building custom partner connectors often pulls senior product engineers away from core roadmap priorities. We embed dedicated senior integration pods in 10 days to take full architectural ownership of custom connectors and pipelines."
        beat3 = "Open to checking a 2-minute teardown of how we helped an enterprise team streamline connector architecture?"

    elif any(term in desc_low or term in raw_kws_str for term in ["legacy", "modernization", "enterprise software", "erp", "crm modernization", "digital transformation", "mainframe", "core system"]):
        camp_code = "C5"
        campaign = "C5 - Enterprise Custom Development & Modernization"
        angle = "Product Development"
        
        if domain_nouns:
            feature_noun = domain_nouns[0]
            beat1 = f"Saw {org_name}'s scale across {feature_noun} and your expansion into modern digital touchpoints."
            trigger = f"modernizing enterprise {feature_noun} systems and legacy workflows"
            pain_point = f"legacy system modernization drag across {feature_noun} architectures"
        else:
            beat1 = f"Saw {org_name}'s focus on modernizing core enterprise systems and expanding digital workflow capabilities."
            trigger = f"modernizing enterprise core systems and legacy workflows"
            pain_point = f"legacy system modernization drag and technical debt accumulation"

        beat2 = "Updating legacy software while maintaining 24/7 operational uptime traps senior engineers in regression testing rather than shipping new features. We embed senior engineering pods in 10 days to safely decouple monolithic workflows, cutting modernization cycles by 40% with zero operational downtime."
        beat3 = "Worth a brief exchange on how you're handling core system updates this quarter?"

    else:
        camp_code = "C2"
        campaign = "C2 - Engineering Pods & Staff Augmentation"
        angle = "Engineering Capacity"
        
        if domain_nouns:
            feature_noun = domain_nouns[0]
            beat1 = f"Saw {org_name}'s digital delivery work and the pace of feature releases across {feature_noun}."
            trigger = f"maintaining sprint velocity while scaling {feature_noun} roadmap"
            pain_point = f"engineering sprint delivery bottlenecks while scaling {feature_noun} features"
        else:
            beat1 = f"Saw {org_name}'s digital delivery work and the pace of delivery across your engineering roadmap."
            trigger = f"maintaining sprint velocity while scaling engineering roadmap"
            pain_point = f"engineering sprint delivery bottlenecks while navigating technical hiring"

        beat2 = "While senior hiring locally takes months, roadmap deadlines don't pause. We embed dedicated senior fullstack pods in 10 days directly into your repo and sprint cycle, owning backlog delivery from day one."
        beat3 = "Happy to send over a 2-minute breakdown on how the pod model works — or should I leave you in peace?"

    return camp_code, campaign, angle, trigger, pain_point, beat1, beat2, beat3

def create_or_get_apollo_contact(person_data, clean_org_name):
    search_url = "https://api.apollo.io/v1/contacts/search"
    email = person_data.get("email", "").strip()
    if email:
        sr = requests.post(search_url, headers=APOLLO_HEADERS, json={"q_keywords": email}, timeout=15)
        if sr.status_code == 200:
            c_list = sr.json().get("contacts", [])
            if c_list:
                return c_list[0].get("id")

    url = "https://api.apollo.io/v1/contacts"
    payload = {
        "first_name": person_data.get("first_name", ""),
        "last_name": person_data.get("last_name", ""),
        "title": person_data.get("title", ""),
        "email": email,
        "organization_name": clean_org_name,
        "website_url": person_data.get("organization", {}).get("website_url", "") if person_data.get("organization") else "",
        "linkedin_url": person_data.get("linkedin_url", "")
    }
    r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        c = r.json().get("contact", {})
        return c.get("id")
    return None

def update_apollo_contact_custom_fields(contact_id, custom_fields):
    url = f"https://api.apollo.io/v1/contacts/{contact_id}"
    payload = {"typed_custom_fields": custom_fields}
    r = requests.put(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        return True, r.json().get("contact", {})
    return False, r.text

def enroll_in_sequence(contact_id, seq_id):
    url = f"https://api.apollo.io/v1/emailer_campaigns/{seq_id}/add_contact_ids"
    payload = {
        "contact_ids": [contact_id],
        "emailer_campaign_id": seq_id,
        "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
        "sequence_active_in_other_campaigns": False
    }
    try:
        r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
        return r.status_code == 200
    except Exception:
        return False

def main():
    print("=" * 80)
    print("SCHEDULER 1: COMPLETING 100 HIGH-INTENT LEADS WITH PROPER RESEARCH")
    print("Geographies: Australia (AUS: 33), UAE (UAE: 26 remaining), United States (US: 34)")
    print("Enforcing Concrete Noun Research Grounding & All 10 Apollo Custom Fields")
    print("=" * 80)

    # 1. Master Exclusions
    print("\n[Step 1] Loading master exclusions...")
    zoho_token = get_zoho_token()
    z_emails, z_comps = get_existing_zoho_records(zoho_token)
    print(f"  Zoho CRM Exclusions: {len(z_emails)} emails, {len(z_comps)} companies.")

    a_emails, a_pids, a_comps = get_existing_apollo_contacts()
    print(f"  Apollo Contact Exclusions: {len(a_emails)} emails, {len(a_comps)} companies.")

    agency_keywords = [
        "software development", "it services", "staffing", "consulting", "agency",
        "digital agency", "custom software", "outsourcing", "offshore", "recruiting",
        "consultancy", "development studio", "technology partners", "solutions",
        "managed services", "it consulting", "marketing agency", "creative agency",
        "software engineering agency", "talent", "staff", "headhunting", "advisory",
        "system integrator", "staffing agency", "cloud consulting", "web development",
        "mobile app development", "it consulting firm", "software house"
    ]

    # 7 were already created today for UAE, so target 26 to hit 33 for UAE
    target_per_geo = {"UAE": 26, "AUS": 33, "US": 34}

    geo_configs = {
        "UAE": {
            "country": "United Arab Emirates",
            "keyword_groups": [
                ["fintech", "payments", "SaaS", "logistics"],
                ["cloud", "infrastructure", "platform", "DevOps"],
                ["AI", "intelligence", "analytics"],
                ["enterprise", "e-commerce", "proptech", "modernization"]
            ]
        },
        "AUS": {
            "country": "Australia",
            "keyword_groups": [
                ["fintech", "SaaS", "B2B SaaS"],
                ["cloud", "platform", "infrastructure"],
                ["AI", "machine learning", "product"],
                ["API", "integration", "payments", "logistics"],
                ["healthtech", "proptech", "enterprise software"]
            ]
        },
        "US": {
            "country": "United States",
            "keyword_groups": [
                ["fintech", "SaaS", "B2B SaaS"],
                ["cloud", "infrastructure", "security", "DevOps"],
                ["AI", "machine learning", "analytics"],
                ["healthtech", "enterprise software", "API", "integration"]
            ]
        }
    }

    all_enriched_leads = []
    seen_companies = set(z_comps).union(a_comps)
    seen_emails = set(z_emails).union(a_emails)
    seen_pids = set(a_pids)

    # 2. Sourcing & Enriching per Geo
    for geo, conf in geo_configs.items():
        quota = target_per_geo[geo]
        print(f"\n" + "-" * 70)
        print(f"PROCESSING GEOGRAPHY: {geo} ({conf['country']}) — Target: {quota} Leads")
        print("-" * 70)

        raw_candidates = search_raw_candidates(conf["country"], conf["keyword_groups"])
        print(f"  Total raw candidates retrieved for {geo}: {len(raw_candidates)}")

        screened = []
        for p in raw_candidates:
            pid = p.get("id")
            if not pid or pid in seen_pids:
                continue

            org = p.get("organization") or {}
            raw_org_name = org.get("name") or ""
            clean_org = clean_company_name(raw_org_name)
            if not clean_org:
                continue

            clean_lower = clean_org.lower()
            if clean_lower in seen_companies:
                continue

            if any(kw in clean_lower for kw in agency_keywords):
                continue

            desc = (org.get("short_description") or "").lower()
            if any(kw in desc for kw in ["software development agency", "custom software development", "it consulting", "outsourcing", "web development"]):
                continue

            title = (p.get("title") or "").lower()
            score = 75
            if "chief technology officer" in title or "cto" in title:
                score += 15
            elif "vp of engineering" in title or "vp engineering" in title:
                score += 12
            elif "head of engineering" in title:
                score += 10
            elif "coo" in title or "chief operating officer" in title:
                score += 8

            p["_score"] = score
            p["_clean_org"] = clean_org
            screened.append(p)

        screened.sort(key=lambda x: x["_score"], reverse=True)
        print(f"  Screened non-agency candidates ready for {geo}: {len(screened)}")

        geo_enriched = 0
        for cand in screened:
            if geo_enriched >= quota:
                break

            pid = cand["id"]
            clean_org = cand["_clean_org"]
            clean_lower = clean_org.lower()

            if clean_lower in seen_companies:
                continue

            person = enrich_person(pid)
            if not person:
                continue

            email = (person.get("email") or "").lower().strip()
            if not email or "@" not in email or email in seen_emails:
                continue

            first_name = (person.get("first_name") or "").strip()
            last_name = (person.get("last_name") or "").strip()
            title = (person.get("title") or cand.get("title") or "").strip()
            org = person.get("organization") or cand.get("organization") or {}
            employees = org.get("estimated_num_employees") or 35
            website = org.get("website_url") or ""
            linkedin_url = person.get("linkedin_url") or ""
            org_desc = org.get("short_description") or ""
            keywords = org.get("keywords") or []
            tech_list = org.get("technology_names") or []

            # Post-enrichment agency check
            if any(kw in clean_lower for kw in agency_keywords):
                continue
            if any(kw in org_desc.lower() for kw in ["software development agency", "it consulting", "outsourcing company", "web development agency"]):
                continue

            # ICP Fit Scoring (1-100)
            icp_score = 80
            if 20 <= employees <= 180:
                icp_score += 10
            elif employees > 200:
                icp_score -= 4

            t_low = title.lower()
            if "cto" in t_low or "chief technology officer" in t_low:
                icp_score += 6
            elif "vp" in t_low or "head of engineering" in t_low:
                icp_score += 4

            if geo in ["AUS", "UAE"]:
                icp_score += 4
            else:
                icp_score += 2
            icp_score = min(98, max(75, icp_score))

            # Determine Campaign, Concrete Noun Research & 3-Beat Email Copy
            camp_code, campaign, angle, trigger, pain_point, b1, b2, b3 = determine_campaign_and_copy(
                clean_org, org_desc, keywords, tech_list, title
            )
            personalised_email = f"{b1}\n\n{b2}\n\n{b3}"

            # Create or get contact in Apollo
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
                continue

            # Write All 10 Custom Fields
            custom_fields = {
                FIELD_ICP_SCORE: icp_score,
                FIELD_LEAD_SOURCE: ["Apollo"],
                FIELD_TARGET_SEGMENT: campaign,
                FIELD_COMPANY_TRIGGER: trigger,
                FIELD_PAIN_POINT: pain_point,
                FIELD_OUTREACH_ANGLE: [angle],
                FIELD_PERSONALISED_EMAIL: personalised_email,
                FIELD_APPROVAL_STATUS: ["New"],
                FIELD_ZOHO_RECORD_ID: "",
                FIELD_ZOHO_SYNC_STATUS: ["Not Synced"]
            }
            success, res = update_apollo_contact_custom_fields(cid, custom_fields)
            if not success:
                continue

            # Populate native "Sequences" field via Sequence enrollment
            seq_id = SEQUENCE_MAP.get(camp_code)
            seq_enrolled = False
            if seq_id:
                seq_enrolled = enroll_in_sequence(cid, seq_id)

            geo_enriched += 1
            seen_companies.add(clean_lower)
            seen_emails.add(email)
            seen_pids.add(pid)

            lead_meta = {
                "geo": geo,
                "contact_id": cid,
                "first_name": first_name,
                "last_name": last_name,
                "title": title,
                "company": clean_org,
                "email": email,
                "campaign": campaign,
                "campaign_code": camp_code,
                "angle": angle,
                "icp_score": icp_score,
                "trigger": trigger,
                "pain_point": pain_point,
                "opener": b1,
                "seq_enrolled": seq_enrolled,
                "email_words": len(personalised_email.split())
            }
            all_enriched_leads.append(lead_meta)
            safe_name = f"{first_name} {last_name}".encode("ascii", "replace").decode("ascii")
            safe_org = clean_org.encode("ascii", "replace").decode("ascii")
            print(f"  [{geo} {geo_enriched}/{quota}] Populated Contact {cid}: {safe_name} ({email}) @ {safe_org} -> {camp_code}")
            safe_b1 = b1.encode("ascii", "replace").decode("ascii")
            print(f"    Opener: \"{safe_b1}\"")
            time.sleep(0.35)

        print(f"Completed {geo}: {geo_enriched}/{quota} leads populated.")

    print("\n" + "=" * 80)
    print(f"SCHEDULER 1 COMPLETED: EXACTLY {len(all_enriched_leads)} LEADS POPULATED IN APOLLO")
    print("=" * 80)

    # Save summary log to disk
    log_path = os.path.join(os.path.dirname(__file__), "..", "scheduler1_100_leads_batch_run.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(all_enriched_leads, f, indent=2)
    print(f"Batch metadata saved to {log_path}")

    # Campaign breakdown
    c_counts = {}
    for l in all_enriched_leads:
        c = l["campaign_code"]
        c_counts[c] = c_counts.get(c, 0) + 1
    print("\nFinal Campaign Breakdown:")
    for c, cnt in sorted(c_counts.items()):
        print(f"  {c}: {cnt} leads ({cnt/len(all_enriched_leads)*100:.1f}%)")

if __name__ == "__main__":
    main()
