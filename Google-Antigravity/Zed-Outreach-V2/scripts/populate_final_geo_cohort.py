import os
import sys
import json
import time
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

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

COHORT = [
    # --- UAE ---
    {
        "geo": "UAE",
        "first_name": "Tariq",
        "last_name": "Hawi",
        "title": "Chief Technology Officer",
        "email": "tariq.alhawi@aletihadpayments.ae",
        "company": "Al Etihad Payments",
        "website_url": "https://aletihadpayments.ae",
        "campaign": "C4 - Middleware & API Integration (ZCoupler)",
        "angle": "Other",
        "icp_score": 96.0,
        "ptb_score": 85.0,
        "trigger": "scaling national instant payment rails and financial messaging APIs",
        "pain_point": "custom banking API integrations and high-throughput financial data synchronization",
        "beat1": "Saw what your team is building with Al Etihad Payments' national infrastructure and your focus across the instant payment rails.",
        "beat2": "Integrating core banking systems with high-throughput payment gateways while keeping transaction latency under 200ms usually pulls senior engineers into custom middleware maintenance. We supply dedicated senior middleware squads to build resilient API bridges and data pipelines under full architectural ownership.",
        "beat3": "Open to seeing how we streamlined high-volume integration architecture for a similar financial transaction platform?"
    },
    {
        "geo": "UAE",
        "first_name": "Desmond",
        "last_name": "Nyamador",
        "title": "Chief Technology Officer",
        "email": "desmond@wewire.com",
        "company": "WeWire",
        "website_url": "https://wewire.com",
        "campaign": "C4 - Middleware & API Integration (ZCoupler)",
        "angle": "Other",
        "icp_score": 94.0,
        "ptb_score": 82.0,
        "trigger": "scaling cross-border payment infrastructure and institutional liquidity APIs",
        "pain_point": "cross-border payment API integration complexity and liquidity settlement synchronization",
        "beat1": "Saw what WeWire is building across cross-border payment infrastructure and B2B settlement APIs.",
        "beat2": "Rolling out partner banking integrations while maintaining real-time FX and settlement accuracy often pulls senior engineers away from primary product goals. We embed senior middleware squads to build resilient API connectors and webhook pipelines, shipping 30-40% faster using modern tooling.",
        "beat3": "Open to checking a 2-minute teardown of how we helped a similar fintech product team accelerate integration cycles by 35%?"
    },
    {
        "geo": "UAE",
        "first_name": "Vinod",
        "last_name": "Kumar",
        "title": "Chief Technology Officer",
        "email": "vkumar@mbmepay.ae",
        "company": "MBME Group",
        "website_url": "https://mbme.biz",
        "campaign": "C5 - Enterprise Custom Development & Modernization",
        "angle": "Product Development",
        "icp_score": 92.0,
        "ptb_score": 80.0,
        "trigger": "modernizing self-service payment kiosk architectures and enterprise digital touchpoints",
        "pain_point": "legacy enterprise kiosk architecture modernization and transaction throughput bottlenecks",
        "beat1": "Saw MBME Group's scale across self-service payment kiosks and your expansion into smart government payment touchpoints.",
        "beat2": "Modernizing legacy kiosk terminal software while maintaining 24/7 transaction uptime across thousands of physical endpoints can easily create delivery bottlenecks. We embed dedicated senior engineering squads to decouple monolithic workflows and accelerate release velocity without operational risk.",
        "beat3": "Open to checking a 2-minute teardown of how we helped an enterprise team modernize legacy transaction systems 40% faster?"
    },

    # --- AUS ---
    {
        "geo": "AUS",
        "first_name": "Daniel",
        "last_name": "Slater",
        "title": "Chief Technology Officer",
        "email": "slater@relume.ai",
        "company": "Relume",
        "website_url": "https://relume.io",
        "campaign": "C1 - AI-Enabled Product Engineering",
        "angle": "Product Development",
        "icp_score": 95.0,
        "ptb_score": 88.0,
        "trigger": "scaling AI-driven component generation and Figma workflow integrations",
        "pain_point": "senior fullstack capacity constraints while rolling out new generative design modules",
        "beat1": "Saw what you guys are shipping with Relume's AI website builder and your focus on generative wireframing workflows.",
        "beat2": "Balancing generative AI feature releases with core platform speed usually stretches senior fullstack engineers thin. We embed dedicated senior engineering squads in 2-3 weeks to take complete architectural ownership of feature modules, shipping 30-40% faster using modern AI-accelerated workflows.",
        "beat3": "Open to checking a 2-minute teardown of how we helped a similar product team accelerate release cycles by 35%?"
    },
    {
        "geo": "AUS",
        "first_name": "Scott",
        "last_name": "Hancock",
        "title": "Chief Technology Officer",
        "email": "shancock@mobiledock.com",
        "company": "Mobiledock",
        "website_url": "https://mobiledock.com",
        "campaign": "C2 - Engineering Pods & Staff Augmentation",
        "angle": "Engineering Capacity",
        "icp_score": 93.0,
        "ptb_score": 82.0,
        "trigger": "scaling multi-tenant logistics and appointment scheduling platform features",
        "pain_point": "engineering sprint delivery bottlenecks while navigating senior technical hiring",
        "beat1": "Noticed your engineering leadership at Mobiledock and the scale of warehouse and dock appointment workflows you manage.",
        "beat2": "Keeping sprint velocity high while navigating senior technical hiring bottlenecks can easily delay critical roadmap commitments. We deploy dedicated senior fullstack pods that integrate into your repo and sprint rituals within 14 days to absorb complex backlog without hiring drag.",
        "beat3": "Open to a brief conversation on whether additional sprint bandwidth would be useful this quarter?"
    },
    {
        "geo": "AUS",
        "first_name": "Avner",
        "last_name": "Silberman",
        "title": "Chief Technology Officer",
        "email": "avnersilberman@simpology.com.au",
        "company": "Simpology Australia",
        "website_url": "https://simpology.com.au",
        "campaign": "C4 - Middleware & API Integration (ZCoupler)",
        "angle": "Other",
        "icp_score": 94.0,
        "ptb_score": 84.0,
        "trigger": "scaling digital loan origination workflows and broker API integrations",
        "pain_point": "complex lender API integrations and bi-directional credit data synchronization",
        "beat1": "Saw what Simpology Australia is building across digital loan origination and your deep integration with lender systems.",
        "beat2": "Maintaining complex lender API pipelines and compliance validation while shipping new origination features often pulls senior engineers in two directions. We supply dedicated senior middleware squads to build resilient bi-directional data layers under full architectural ownership.",
        "beat3": "Open to checking a 2-minute teardown of how we streamlined integration architecture for a high-volume financial platform?"
    },

    # --- US ---
    {
        "geo": "US",
        "first_name": "Stathis",
        "last_name": "Mytilinaios",
        "title": "Chief Technology Officer",
        "email": "stathis.mytilinaios@innit.com",
        "company": "Innit",
        "website_url": "https://innit.com",
        "campaign": "C1 - AI-Enabled Product Engineering",
        "angle": "Product Development",
        "icp_score": 95.0,
        "ptb_score": 86.0,
        "trigger": "scaling AI food intelligence engines and connected kitchen partner APIs",
        "pain_point": "senior engineering capacity bottlenecks while scaling AI-driven personalized food recommendations",
        "beat1": "Saw what you guys are building with Innit's personalized nutrition platform and your integrations across connected kitchen appliances.",
        "beat2": "Balancing AI culinary recommendation models with multi-partner appliance integrations usually stretches senior product engineers thin. We embed dedicated senior engineering squads in 2-3 weeks to take complete architectural ownership of feature modules, shipping 30-40% faster.",
        "beat3": "Open to checking a 2-minute teardown of how we helped a similar product team accelerate release cycles by 35%?"
    },
    {
        "geo": "US",
        "first_name": "Tom",
        "last_name": "Blackadar",
        "title": "Chief Technology Officer",
        "email": "tblackadar@aionbiosystems.com",
        "company": "AION Biosystems",
        "website_url": "https://aionbiosystems.com",
        "campaign": "C2 - Engineering Pods & Staff Augmentation",
        "angle": "Engineering Capacity",
        "icp_score": 93.0,
        "ptb_score": 84.0,
        "trigger": "scaling remote patient monitoring pipelines and infection detection telemetry",
        "pain_point": "senior backend engineering capacity bottlenecks on medical sensor data pipelines",
        "beat1": "Noticed AION Biosystems' work with the Itero remote patient monitoring platform and your focus on continuous clinical infection monitoring.",
        "beat2": "Scaling clinical sensor telemetry while maintaining strict medical device compliance often stretches internal engineering teams thin. We embed dedicated senior engineering pods in 2-3 weeks to take full ownership of backend data pipelines and mobile workflows under your direct oversight.",
        "beat3": "Open to a brief conversation on whether dedicated sprint bandwidth would help hit your upcoming roadmap milestones?"
    },
    {
        "geo": "US",
        "first_name": "Charles",
        "last_name": "Buck",
        "title": "Chief Technology Officer",
        "email": "chip@saasalerts.com",
        "company": "SaaS Alerts",
        "website_url": "https://saasalerts.com",
        "campaign": "C3 - Platform Engineering & Cloud Modernization",
        "angle": "Engineering Capacity",
        "icp_score": 94.0,
        "ptb_score": 85.0,
        "trigger": "scaling cloud telemetry throughput and multi-tenant security monitoring architecture",
        "pain_point": "cloud infrastructure throughput constraints and real-time security event latency bottlenecks",
        "beat1": "Noticed SaaS Alerts' platform footprint and the scale of real-time security events you process across Microsoft 365 and Google Workspace.",
        "beat2": "Managing high-throughput event streaming while keeping cloud query latency low often stretches senior platform and DevOps engineers thin. We deploy dedicated senior platform squads to harden distributed cloud architectures and optimize infrastructure without disrupting active development.",
        "beat3": "Worth a brief exchange on how you're handling platform throughput and cloud scalability this quarter?"
    },
    {
        "geo": "US",
        "first_name": "Leonidas",
        "last_name": "Ribeiro",
        "title": "Chief Technology Officer",
        "email": "leonidas.ribeiro@bmgmoney.com",
        "company": "BMG Money",
        "website_url": "https://bmgmoney.com",
        "campaign": "C4 - Middleware & API Integration (ZCoupler)",
        "angle": "Other",
        "icp_score": 94.0,
        "ptb_score": 83.0,
        "trigger": "expanding employer payroll API integrations and automated loan servicing workflows",
        "pain_point": "employer payroll API integrations and bi-directional loan deduction synchronization",
        "beat1": "Saw what BMG Money is building across automated loan servicing and your direct integration with employer payroll systems.",
        "beat2": "Building and maintaining custom payroll deduction APIs across hundreds of distinct public sector employers often pulls senior engineers away from core platform improvements. We supply dedicated middleware squads to build resilient bi-directional data pipelines under full architectural ownership.",
        "beat3": "Open to seeing how we streamlined integration architecture for a similar financial transaction platform?"
    }
]

def create_or_get_apollo_contact(lead):
    # Check if contact already exists by email
    search_url = "https://api.apollo.io/v1/contacts/search"
    sr = requests.post(search_url, headers=APOLLO_HEADERS, json={"q_keywords": lead["email"]}, timeout=15)
    if sr.status_code == 200:
        c_list = sr.json().get("contacts", [])
        if c_list:
            cid = c_list[0].get("id")
            print(f"  Existing contact found for {lead['email']}: {cid}")
            return cid

    # Create contact in Apollo
    url = "https://api.apollo.io/v1/contacts"
    payload = {
        "first_name": lead["first_name"],
        "last_name": lead["last_name"],
        "title": lead["title"],
        "email": lead["email"],
        "organization_name": lead["company"],
        "website_url": lead["website_url"]
    }
    r = requests.post(url, headers=APOLLO_HEADERS, json=payload, timeout=20)
    if r.status_code == 200:
        cid = r.json().get("contact", {}).get("id")
        print(f"  Created new contact in Apollo for {lead['email']}: {cid}")
        return cid
    else:
        print(f"  Error creating contact: {r.status_code} - {r.text}")
        return None

def update_contact_fields(cid, lead):
    personalised_email = f"{lead['beat1']}\n\n{lead['beat2']}\n\n{lead['beat3']}"
    custom_fields = {
        FIELD_ICP_SCORE: lead["icp_score"],
        FIELD_LEAD_SOURCE: ["Apollo"],
        FIELD_TARGET_SEGMENT: lead["campaign"],
        FIELD_COMPANY_TRIGGER: lead["trigger"],
        FIELD_PAIN_POINT: lead["pain_point"],
        FIELD_OUTREACH_ANGLE: [lead["angle"]],
        FIELD_PERSONALISED_EMAIL: personalised_email,
        FIELD_APPROVAL_STATUS: ["New"],
        FIELD_ZOHO_RECORD_ID: "",
        FIELD_ZOHO_SYNC_STATUS: ["Not Synced"]
    }
    url = f"https://api.apollo.io/v1/contacts/{cid}"
    r = requests.put(url, headers=APOLLO_HEADERS, json={"typed_custom_fields": custom_fields}, timeout=20)
    if r.status_code == 200:
        return True, r.json().get("contact", {})
    return False, r.text

def main():
    print("=" * 80)
    print("POPULATING HIGH-INTENT BDM COHORT ACROSS AUS, UAE, AND US")
    print("=" * 80)

    results = []
    for i, lead in enumerate(COHORT):
        print(f"\n[{i+1}/{len(COHORT)}] [{lead['geo']}] Processing {lead['first_name']} {lead['last_name']} @ {lead['company']}...")
        cid = create_or_get_apollo_contact(lead)
        if not cid:
            continue
        success, res = update_contact_fields(cid, lead)
        if success:
            print(f"  Successfully populated all 10 custom fields for contact {cid}!")
            print(f"    Campaign: {lead['campaign']} | Angle: {lead['angle']} | ICP: {lead['icp_score']}")
            print(f"    Pain Point: \"{lead['pain_point']}\"")
            
            # Populate native 'Sequences' field by adding to corresponding Apollo sequence
            seq_map = {
                "C1": "6aa7ec0e7c0f80000cbd7600",
                "C2": "6aa7eca553473f000c678940",
                "C3": "6aa7ecb31fd57300143fbfa7",
                "C4": "6aa7ecbea907dd00140753b2",
                "C5": "6aa7ecc953473f000c678b8e"
            }
            camp_key = lead["campaign"][:2]
            seq_id = seq_map.get(camp_key)
            if seq_id:
                try:
                    s_url = f"https://api.apollo.io/v1/emailer_campaigns/{seq_id}/add_contact_ids"
                    s_res = requests.post(s_url, headers=APOLLO_HEADERS, json={
                        "contact_ids": [cid],
                        "emailer_campaign_id": seq_id,
                        "send_email_from_email_account_id": "6a70212e10bb20000cb56d8f",
                        "sequence_active_in_other_campaigns": False
                    }, timeout=15)
                    if s_res.status_code == 200:
                        print(f"    -> Native 'Sequences' field populated with sequence {camp_key} ({seq_id})")
                    else:
                        print(f"    -> Warning: Failed to populate Sequences field: {s_res.status_code}")
                except Exception as ex:
                    print(f"    -> Exception enrolling in sequence: {ex}")
            
            lead["contact_id"] = cid
            results.append(lead)
        else:
            print(f"  Failed to update contact {cid}: {res}")
        time.sleep(0.3)

    print("\n" + "=" * 80)
    print(f"VERIFYING ALL {len(results)} ENRICHED RECORDS IN APOLLO")
    print("=" * 80)
    for lead in results:
        cid = lead["contact_id"]
        v_url = f"https://api.apollo.io/v1/contacts/{cid}"
        vr = requests.get(v_url, headers=APOLLO_HEADERS, timeout=15)
        if vr.status_code == 200:
            c = vr.json().get("contact", {})
            tcf = c.get("typed_custom_fields", {})
            status = tcf.get(FIELD_APPROVAL_STATUS)
            target = tcf.get(FIELD_TARGET_SEGMENT)
            score = tcf.get(FIELD_ICP_SCORE)
            sync = tcf.get(FIELD_ZOHO_SYNC_STATUS)
            pain = tcf.get(FIELD_PAIN_POINT)
            angle = tcf.get(FIELD_OUTREACH_ANGLE)
            email_body = tcf.get(FIELD_PERSONALISED_EMAIL)
            word_count = len(email_body.split()) if email_body else 0
            print(f"[{lead['geo']}] {lead['first_name']} {lead['last_name']} ({lead['email']}) @ {lead['company']}")
            print(f"  Target: {target} | Angle: {angle} | ICP: {score} | Approval: {status} | Sync: {sync}")
            print(f"  Trigger: \"{tcf.get(FIELD_COMPANY_TRIGGER)}\"")
            print(f"  Pain Point: \"{pain}\"")
            print(f"  3-Beat Email Body Word Count: {word_count} words")
            print("-" * 60)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
