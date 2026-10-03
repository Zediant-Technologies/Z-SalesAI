import os
import requests
import json
import re
import time
from dotenv import load_dotenv

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
if not APOLLO_API_KEY:
    raise ValueError("APOLLO_API_KEY not found in environment!")

headers = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

FIELD_TARGET_SEGMENT = "6aa790d821b4e6001cb70994"
FIELD_PERSONALISED_EMAIL = "6aa79177f203040018e0af9d"

def clean_beat1(b1):
    # Remove informal 'you guys are' -> 'your team is'
    b1 = re.sub(r'\byou guys are\b', 'your team is', b1, flags=re.IGNORECASE)
    b1 = re.sub(r'\bhow you\'re\b', 'how your team is', b1, flags=re.IGNORECASE)
    # Replace 'Came across ' with 'Saw '
    if b1.startswith('Came across '):
        b1 = 'Saw ' + b1[len('Came across '):]
    return b1.strip()

def build_new_email(c):
    tcf = c.get('typed_custom_fields', {})
    camp = tcf.get(FIELD_TARGET_SEGMENT, '')
    curr_em = tcf.get(FIELD_PERSONALISED_EMAIL, '')
    beats = curr_em.split('\n\n') if curr_em else []
    
    org = c.get('organization_name') or ''
    
    # Extract or build Beat 1
    if len(beats) >= 1 and beats[0].strip():
        b1 = clean_beat1(beats[0].strip())
    else:
        b1 = f"Saw {org}'s product platform and your focus across the engineering roadmap."
    
    if 'C1' in camp:
        b2 = "When roadmap pressure spikes, your best engineers often get stuck firefighting maintenance instead of shipping core features. We embed dedicated senior engineering pods in 10 days to take full ownership of modules and ship 30-40% faster using AI-assisted delivery workflows."
        b3 = "Happy to share a 2-minute breakdown on how this works in practice?"
    elif 'C2' in camp:
        b2 = "While senior hiring locally takes months, roadmap deadlines don't pause. We embed dedicated senior fullstack pods in 10 days directly into your repo and sprint cycle, owning backlog delivery from day one."
        b3 = "Happy to send over a 2-minute breakdown on how the pod model works — or should I leave you in peace?"
    elif 'C3' in camp:
        b2 = "When deployment pipelines lag, senior developers end up babysitting releases and troubleshooting builds instead of shipping features. We embed dedicated senior DevOps pods in 10 days to automate CI/CD and eliminate deployment friction."
        b3 = "Happy to send over a 2-minute breakdown of how the pod model works?"
    elif 'C4' in camp:
        b2 = "Building custom partner connectors often pulls senior product engineers away from core roadmap priorities. We embed dedicated senior integration pods in 10 days to take full architectural ownership of custom connectors and pipelines."
        b3 = "Open to checking a 2-minute teardown of how we helped an enterprise team streamline connector architecture?"
    elif 'C5' in camp:
        if 'mbme' in org.lower():
            b1 = "Saw MBME Group's scale across self-service payment kiosks and your expansion into smart government payment touchpoints."
            b2 = "Updating legacy terminal software while maintaining 24/7 transaction uptime traps senior engineers in regression testing rather than shipping new kiosk features. We embed senior engineering pods in 10 days to safely decouple monolithic workflows, cutting modernization cycles by 40% with zero terminal downtime."
            b3 = "Worth a brief exchange on how you're handling terminal software updates this quarter?"
        elif 'red planet' in org.lower():
            b1 = "Saw what Red Planet Software has engineered with your Odyssey platform and how you handle complex insurance premium funding and ledger workflows."
            b2 = "Updating mission-critical loan administration and payment architectures while maintaining 24/7 transaction uptime traps senior engineers in regression testing rather than shipping new features. We embed senior engineering pods in 10 days to safely decouple monolithic workflows, cutting modernization cycles by 40% with zero financial downtime."
            b3 = "Worth a brief exchange on how you're handling core payment and ledger architecture updates this quarter?"
        else:
            b2 = "Updating legacy enterprise software while maintaining 24/7 operational uptime traps senior engineers in regression testing rather than shipping new features. We embed senior engineering pods in 10 days to safely decouple monolithic workflows, cutting modernization cycles by 40% with zero operational downtime."
            b3 = "Worth a brief exchange on how you're handling core system updates this quarter?"
    else:
        return None

    return f"{b1}\n\n{b2}\n\n{b3}"

def main():
    print("=" * 80)
    print("UPDATING ALL APOLLO CONTACTS: {{Personalised Email}} FIELD")
    print("Calibrated across C1-C5 with latest 9/10 benchmarks, 10-day pods & proof points")
    print("=" * 80)

    # 1. Fetch all contacts
    contacts = []
    page = 1
    while True:
        r = requests.post("https://api.apollo.io/v1/contacts/search", headers=headers, json={"page": page, "per_page": 100}, timeout=20)
        if r.status_code != 200:
            print(f"Error fetching page {page}: {r.status_code}")
            break
        data = r.json()
        batch = data.get("contacts", [])
        if not batch:
            break
        contacts.extend(batch)
        if page >= data.get("pagination", {}).get("total_pages", 1):
            break
        page += 1

    print(f"Total contacts retrieved from Apollo: {len(contacts)}")

    updated_count = 0
    skipped_count = 0
    error_count = 0
    by_campaign = {}

    for i, c in enumerate(contacts, 1):
        cid = c.get("id")
        name = c.get("name") or f"{c.get('first_name')} {c.get('last_name')}"
        company = c.get("organization_name") or ""
        camp = c.get("typed_custom_fields", {}).get(FIELD_TARGET_SEGMENT, "Unassigned")

        new_email = build_new_email(c)
        if not new_email:
            skipped_count += 1
            continue

        payload = {
            "typed_custom_fields": {
                FIELD_PERSONALISED_EMAIL: new_email
            }
        }

        retries = 3
        success = False
        while retries > 0:
            try:
                put_r = requests.put(f"https://api.apollo.io/v1/contacts/{cid}", headers=headers, json=payload, timeout=20)
                if put_r.status_code == 200:
                    success = True
                    break
                elif put_r.status_code == 429:
                    print(f"Rate limited on contact {cid}. Waiting 5s...")
                    time.sleep(5)
                    retries -= 1
                else:
                    print(f"Failed to update contact {cid} ({name}): {put_r.status_code} {put_r.text}")
                    break
            except Exception as e:
                print(f"Exception on contact {cid}: {e}")
                time.sleep(2)
                retries -= 1

        if success:
            updated_count += 1
            camp_code = camp.split(" - ")[0] if " - " in camp else camp
            by_campaign[camp_code] = by_campaign.get(camp_code, 0) + 1
        else:
            error_count += 1

        if i % 25 == 0 or i == len(contacts):
            print(f"Progress: [{i}/{len(contacts)}] | Updated: {updated_count} | Errors: {error_count} | Skipped: {skipped_count}")

        time.sleep(0.35)

    print("\n" + "=" * 80)
    print("APOLLO UPDATE COMPLETE")
    print(f"Successfully Updated Contacts: {updated_count}")
    print(f"Errors: {error_count}")
    print(f"Skipped: {skipped_count}")
    print("\nBreakdown by Campaign:")
    for camp_code, count in sorted(by_campaign.items()):
        print(f"  {camp_code}: {count} leads updated")
    print("=" * 80)

if __name__ == "__main__":
    main()
