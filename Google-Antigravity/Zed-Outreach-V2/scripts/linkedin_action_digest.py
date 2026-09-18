"""
Zediant LinkedIn Action Digest Generator (v6.0)

Purpose:
Fetches pending LinkedIn manual tasks (Step 2: linkedin_step_connect, Step 4: linkedin_step_message)
from Apollo, extracts the contact profile links and pre-drafted notes, and formats a clean,
ready-to-paste daily digest for the BDM (console and Zoho Cliq).
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
HEADERS = {
    "X-Api-Key": APOLLO_API_KEY,
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

def fetch_open_linkedin_tasks():
    """Query Apollo for open LinkedIn connection and messaging tasks."""
    url = "https://api.apollo.io/v1/tasks/search"
    payload = {
        "page": 1,
        "per_page": 50,
        "status": ["open", "pending"]
    }
    resp = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    if resp.status_code != 200:
        print(f"Error fetching tasks: {resp.status_code} {resp.text}")
        return []
    
    tasks = resp.json().get("tasks", [])
    # Filter for LinkedIn tasks
    linkedin_tasks = [t for t in tasks if "linkedin" in (t.get("type") or "").lower()]
    return linkedin_tasks

def generate_digest():
    if not APOLLO_API_KEY:
        print("ERROR: APOLLO_API_KEY is not set.")
        sys.exit(1)
        
    print("Fetching open LinkedIn tasks from Apollo...")
    tasks = fetch_open_linkedin_tasks()
    
    if not tasks:
        print("No pending LinkedIn outreach tasks due today. All caught up!")
        return
        
    print(f"\n==========================================")
    print(f"DAILY LINKEDIN ACTION DIGEST ({len(tasks)} Tasks Due)")
    print(f"==========================================")
    
    for i, t in enumerate(tasks, 1):
        contact = t.get("contact", {})
        first_name = contact.get("first_name", "Prospect")
        last_name = contact.get("last_name", "")
        company = contact.get("organization_name", contact.get("company", "Target Company"))
        title = contact.get("title", "")
        linkedin_url = contact.get("linkedin_url", "N/A")
        task_type = "Connection Request" if "connect" in t.get("type", "").lower() else "Direct Message"
        note = t.get("note") or t.get("description") or "Use standard campaign playbook copy."
        
        print(f"\n[{i}] {task_type}: {first_name} {last_name} ({title} @ {company})")
        print(f"  🔗 LinkedIn Profile: {linkedin_url}")
        print(f"  📝 Copy to Paste:")
        print(f"  --------------------------------------------------")
        print(f"  {note}")
        print(f"  --------------------------------------------------")

if __name__ == "__main__":
    generate_digest()
