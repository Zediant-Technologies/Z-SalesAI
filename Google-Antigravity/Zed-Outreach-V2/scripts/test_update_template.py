import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("APOLLO_API_KEY")
headers = {"Content-Type": "application/json", "Cache-Control": "no-cache", "X-Api-Key": api_key}

cid = "6aa7ec0e7c0f80000cbd7600"
res = requests.get(f"https://api.apollo.io/v1/emailer_campaigns/{cid}", headers=headers)
touches = res.json().get("emailer_touches", [])
print(f"Touches count: {len(touches)}")
t1 = touches[0]
tid = t1.get("emailer_template_id")
touch_id = t1.get("id")
print(f"Touch ID: {touch_id}, Template ID: {tid}")

# Inspect touch
print("Touch keys:", list(t1.keys()))

# Get template
tres = requests.get(f"https://api.apollo.io/v1/emailer_templates/{tid}", headers=headers)
tdata = tres.json().get("emailer_template", {})
print("Current subject:", tdata.get("subject"))
print("Current body snippet:", (tdata.get("body_text") or "")[:80])

# Try updating template directly
payload = {
    "name": "C1 Step 1 Template",
    "subject": "{{company}}'s product roadmap",
    "body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
    "body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies"
}
put1 = requests.put(f"https://api.apollo.io/v1/emailer_templates/{tid}", headers=headers, json=payload)
print("PUT flat status:", put1.status_code)
print("PUT flat response subject:", put1.json().get("emailer_template", {}).get("subject"))
print("PUT flat response body:", (put1.json().get("emailer_template", {}).get("body_text") or "")[:80])

# What if wrapped in emailer_template?
put2 = requests.put(f"https://api.apollo.io/v1/emailer_templates/{tid}", headers=headers, json={"emailer_template": payload})
print("PUT nested status:", put2.status_code)
print("PUT nested response subject:", put2.json().get("emailer_template", {}).get("subject"))
