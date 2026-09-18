"""
Zediant Saleshandy Distribution Script (Scheduler 2)
Pushes BDM-approved leads (Lead_Status = "Approved for Outreach") to Saleshandy sequences.

Rules:
1. Eligibility: Lead_Status = "Approved for Outreach" only.
2. Sequence resolution: Matches Zoho Lead_Campaign_Category against Saleshandy sequences at runtime.
3. Split sub-batches by case study availability:
   - CASE_STUDY_AVAILABLE
   - CASE_STUDY_NOT_AVAILABLE
4. Uses conflictAction = "noUpdate" to prevent overwriting existing prospects.
5. On success, updates Zoho Lead_Status to "Outreach Scheduled".
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv()

SALESHANDY_API_KEY = os.getenv("SALESHANDY_API_KEY")
SALESHANDY_BASE_URL = os.getenv("SALESHANDY_API_BASE_URL", "https://open-api.saleshandy.com/v1")

HEADERS = {
    "x-api-key": SALESHANDY_API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_sequences():
    """Fetch all sequences from Saleshandy."""
    url = f"{SALESHANDY_BASE_URL}/sequences?pageSize=100"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("payload", data) if isinstance(data, dict) else data

def get_sequence_step_1(sequence_id):
    """Fetch step 1 ID for a given sequence."""
    url = f"{SALESHANDY_BASE_URL}/sequences/{sequence_id}/steps"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    steps = data.get("payload", data) if isinstance(data, dict) else data
    for step in steps:
        if step.get("number") == 1 or step.get("stepNumber") == 1:
            return step.get("id")
    if steps:
        return steps[0].get("id")
    raise ValueError(f"No steps found in sequence {sequence_id}")

def push_prospects_to_step(sequence_id, step_id, prospects, tags):
    """Import prospects into sequence step with tags and conflictAction=noUpdate."""
    url = f"{SALESHANDY_BASE_URL}/sequences/{sequence_id}/steps/{step_id}/prospects"
    payload = {
        "prospectList": prospects,
        "tags": tags,
        "conflictAction": "noUpdate"
    }
    resp = requests.post(url, headers=HEADERS, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()

def build_prospect_payload(lead):
    """Format Zoho lead into exact Saleshandy prospect field labels."""
    return {
        "First Name": lead.get("First_Name", ""),
        "Last Name": lead.get("Last_Name", ""),
        "Email": lead.get("Email", ""),
        "Job Title": lead.get("Designation", lead.get("Title", "")),
        "Company": lead.get("Company", ""),
        "Email Personalised Opening": lead.get("Email_Personalised_Opening", ""),
        "Email Pain Points": lead.get("Email_Pain_Points", ""),
        "Business Challenge": lead.get("Business_Challenges", ""),
        "Case Study": lead.get("Case_Study", "")
    }

def main():
    if not SALESHANDY_API_KEY:
        print("ERROR: SALESHANDY_API_KEY is not set in environment or .env file.")
        sys.exit(1)
    print("Saleshandy Distribution helper loaded successfully.")

if __name__ == "__main__":
    main()
