import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
HEADERS = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "X-Api-Key": APOLLO_API_KEY
}

TEMPLATE_SEQUENCE_ID = "6a6f4cfea0044c000cce2c26"

OLD_EMPTY_IDS = [
    "6aa7e5a9b1e7b90010255877",
    "6aa7e5b2fc90ff0018a4ed6b",
    "6aa7e5b307b4af0020bd350d",
    "6aa7e5b4e40c9e00188c4c39",
    "6aa7e5b61012aa000cdd3ff0",
]

CAMPAIGN_SPECS = [
    {
        "code": "C1",
        "name": "C1 - AI-Enabled Product Engineering",
        "step1_subject": "{{company}}'s product roadmap",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}. We partner with tech teams on AI-enabled architecture and high-velocity engineering squads. Would love to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my earlier note regarding {{Pain Point}}.\n\nWhen software teams look to accelerate their AI roadmap, the blocker is rarely the model itself - it's data pipelines, integration into core product workflows, and senior engineering capacity.\n\nWe deploy dedicated squads (senior developers, tech leads) in 2-3 weeks who take full ownership of feature velocity without overhead.\n\nOpen to seeing how we could support {{company}}'s next milestone?\n\nBest,\nRajeev",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my earlier note regarding {{Pain Point}}.</p><p>When software teams look to accelerate their AI roadmap, the blocker is rarely the model itself - it's data pipelines, integration into core product workflows, and senior engineering capacity.</p><p>We deploy dedicated squads (senior developers, tech leads) in 2-3 weeks who take full ownership of feature velocity without overhead.</p><p>Open to seeing how we could support {{company}}'s next milestone?</p><p>Best,<br>Rajeev</p>",
        "step4_note": "Thanks for connecting, {{first_name}}. Curious - is {{Pain Point}} currently the primary constraint on {{company}}'s delivery velocity, or is your internal team pretty well resourced?",
        "step5_body_text": "Hi {{first_name}},\n\nLast note from me. If addressing {{Pain Point}} or roadmap bandwidth isn't an active priority for {{company}} right now, no worries at all.\n\nWe recently partnered with a scaling SaaS platform facing a similar delivery bottleneck, deploying a dedicated pod of 4 senior engineers in 3 weeks and shipping their production MVP in 60 days with zero disruption to their existing stack.\n\nIf it becomes a priority this quarter, let me know.\n\nBest,\nRajeev",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If addressing {{Pain Point}} or roadmap bandwidth isn't an active priority for {{company}} right now, no worries at all.</p><p>We recently partnered with a scaling SaaS platform facing a similar delivery bottleneck, deploying a dedicated pod of 4 senior engineers in 3 weeks and shipping their production MVP in 60 days with zero disruption to their existing stack.</p><p>If it becomes a priority this quarter, let me know.</p><p>Best,<br>Rajeev</p>",
    },
    {
        "code": "C2",
        "name": "C2 - Engineering Pods & Staff Augmentation",
        "step1_subject": "engineering bandwidth at {{company}}",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}. We help scaling software teams embed senior engineering pods within 2-3 weeks. Would like to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my earlier note regarding {{Pain Point}}.\n\nThe three questions engineering leaders ask us first:\n1. How senior? Five-plus years, and you interview and approve every developer.\n2. How fast? Squad live and delivering in two to three weeks.\n3. What engagement? Dedicated month-to-month, embedded in your ceremonies and repos.\n\nWorth a quick 15-minute chat to see if this solves any headcount bottlenecks at {{company}}?\n\nBest,\nRajeev",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my earlier note regarding {{Pain Point}}.</p><p>The three questions engineering leaders ask us first:<br>1. How senior? Five-plus years, and you interview and approve every developer.<br>2. How fast? Squad live and delivering in two to three weeks.<br>3. What engagement? Dedicated month-to-month, embedded in your ceremonies and repos.</p><p>Worth a quick 15-minute chat to see if this solves any headcount bottlenecks at {{company}}?</p><p>Best,<br>Rajeev</p>",
        "step4_note": "Thanks for connecting, {{first_name}}. Curious rather than pitching - what's the hardest role to fill on your team right now to address {{Pain Point}}? For most software CTOs we speak with, it's senior fullstack or cloud leads.",
        "step5_body_text": "Hi {{first_name}},\n\nLast one from me. If {{company}}'s hiring pipeline is healthy and {{Pain Point}} is well in hand, please ignore this.\n\nIf there's a roadmap item that keeps slipping because nobody's free to own it, I'm happy to show you how our embedded pods operate.\n\nBest,\nRajeev",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Last one from me. If {{company}}'s hiring pipeline is healthy and {{Pain Point}} is well in hand, please ignore this.</p><p>If there's a roadmap item that keeps slipping because nobody's free to own it, I'm happy to show you how our embedded pods operate.</p><p>Best,<br>Rajeev</p>",
    },
    {
        "code": "C3",
        "name": "C3 - Platform Engineering & Cloud Modernization",
        "step1_subject": "{{company}}'s cloud infrastructure",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}. We partner with engineering teams on cloud modernization, Kubernetes, and platform resilience. Great to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my previous note regarding {{Pain Point}}.\n\nMany engineering leaders find their core developers spending 30%+ of their sprints wrestling with deployment pipelines, infrastructure debt, or rising AWS/GCP bills instead of shipping product features.\n\nOur platform engineers help automate CI/CD, optimize cloud spend, and harden multi-tenant environments so your product engineers can focus on shipping.\n\nWorth comparing notes on {{company}}'s setup?\n\nBest,\nRajeev",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my previous note regarding {{Pain Point}}.</p><p>Many engineering leaders find their core developers spending 30%+ of their sprints wrestling with deployment pipelines, infrastructure debt, or rising AWS/GCP bills instead of shipping product features.</p><p>Our platform engineers help automate CI/CD, optimize cloud spend, and harden multi-tenant environments so your product engineers can focus on shipping.</p><p>Worth comparing notes on {{company}}'s setup?</p><p>Best,<br>Rajeev</p>",
        "step4_note": "Glad to connect, {{first_name}}. Quick question - is {{Pain Point}} mostly handled by your core dev team right now, or do you have a dedicated platform/DevOps squad?",
        "step5_body_text": "Hi {{first_name}},\n\nLast check-in. If your platform and cloud setup is running smoothly with no headaches around {{Pain Point}}, feel free to archive this.\n\nIf you do need senior DevOps/cloud engineering muscle to unblock a migration or modernize your architecture, let me know.\n\nBest,\nRajeev",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Last check-in. If your platform and cloud setup is running smoothly with no headaches around {{Pain Point}}, feel free to archive this.</p><p>If you do need senior DevOps/cloud engineering muscle to unblock a migration or modernize your architecture, let me know.</p><p>Best,<br>Rajeev</p>",
    },
    {
        "code": "C4",
        "name": "C4 - Middleware & API Integration (ZCoupler)",
        "step1_subject": "system integrations at {{company}}",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}. We specialize in enterprise API integrations and robust middleware (ZCoupler). Let's connect.",
        "step3_body_text": "Hi {{first_name}},\n\nReaching back out regarding {{Pain Point}}.\n\nCustom integrations between enterprise platforms, CRMs, ERPs, and legacy databases often stall internal roadmaps because nobody wants to build and maintain fragile point-to-point glue code.\n\nWith ZCoupler and our integration engineering practice, we build robust, two-way, fault-tolerant middleware that syncs data in real time.\n\nDo you have any complex integration projects currently on the back burner?\n\nBest,\nRajeev",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Reaching back out regarding {{Pain Point}}.</p><p>Custom integrations between enterprise platforms, CRMs, ERPs, and legacy databases often stall internal roadmaps because nobody wants to build and maintain fragile point-to-point glue code.</p><p>With ZCoupler and our integration engineering practice, we build robust, two-way, fault-tolerant middleware that syncs data in real time.</p><p>Do you have any complex integration projects currently on the back burner?</p><p>Best,<br>Rajeev</p>",
        "step4_note": "Thanks for connecting, {{first_name}}. Regarding {{Pain Point}} - are legacy third-party integrations or manual data bridges creating friction in your workflows, or is your stack mostly unified?",
        "step5_body_text": "Hi {{first_name}},\n\nClosing the loop on this. If {{Pain Point}} is resolved and all your system integrations are running seamlessly, disregard this note.\n\nIf an integration bottleneck pops up down the road, feel free to reach out.\n\nBest,\nRajeev",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Closing the loop on this. If {{Pain Point}} is resolved and all your system integrations are running seamlessly, disregard this note.</p><p>If an integration bottleneck pops up down the road, feel free to reach out.</p><p>Best,<br>Rajeev</p>",
    },
    {
        "code": "C5",
        "name": "C5 - Enterprise Custom Development & Modernization",
        "step1_subject": "modernizing {{company}}'s core systems",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nZediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><p>{{Personalised Email}}</p><p>Best,<br>Rajeev Jaiswal<br>Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}. We partner with enterprises on incremental legacy system modernization and cloud architecture. Great to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my note regarding {{Pain Point}}.\n\nThe biggest risk with legacy system upgrades is the fear of breaking mission-critical operations during a monolithic rewrite.\n\nOur team specializes in the strangler pattern - decomposing legacy monoliths, modernizing frontend/backend components incrementally, and deploying microservices while keeping existing business operations uninterrupted.\n\nAre you evaluating any modernization initiatives this year?\n\nBest,\nRajeev",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my note regarding {{Pain Point}}.</p><p>The biggest risk with legacy system upgrades is the fear of breaking mission-critical operations during a monolithic rewrite.</p><p>Our team specializes in the strangler pattern - decomposing legacy monoliths, modernizing frontend/backend components incrementally, and deploying microservices while keeping existing business operations uninterrupted.</p><p>Are you evaluating any modernization initiatives this year?</p><p>Best,<br>Rajeev</p>",
        "step4_note": "Great to connect, {{first_name}}. Regarding {{Pain Point}} - are legacy dependencies slowing down feature delivery at {{company}}, or is maintenance well in hand?",
        "step5_body_text": "Hi {{first_name}},\n\nLast note from me. If technical debt around {{Pain Point}} isn't an active concern for {{company}}, feel free to ignore this.\n\nIf you do need specialized engineering capability to refactor core systems safely, keep us in mind.\n\nBest,\nRajeev",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If technical debt around {{Pain Point}} isn't an active concern for {{company}}, feel free to ignore this.</p><p>If you do need specialized engineering capability to refactor core systems safely, keep us in mind.</p><p>Best,<br>Rajeev</p>",
    }
]


def archive_old_empty_sequences():
    print("--- Archiving old empty sequence shells ---")
    for cid in OLD_EMPTY_IDS:
        url = f"https://api.apollo.io/v1/emailer_campaigns/{cid}/archive"
        res = requests.post(url, headers=HEADERS, json={})
        print(f"Archive {cid}: status {res.status_code}")


def update_template(tid, subject, body_text, body_html):
    url = f"https://api.apollo.io/v1/emailer_templates/{tid}"
    payload = {
        "emailer_template": {
            "body_text": body_text,
            "body_html": body_html
        }
    }
    if subject:
        payload["emailer_template"]["subject"] = subject
    res = requests.put(url, headers=HEADERS, json=payload)
    if res.status_code != 200:
        print(f"  [ERROR] Updating template {tid}: {res.status_code} {res.text[:100]}")
    return res.status_code == 200


def build_sequences():
    archive_old_empty_sequences()
    
    results = {}
    
    for spec in CAMPAIGN_SPECS:
        code = spec["code"]
        name = spec["name"]
        print(f"\n==========================================")
        print(f"Creating / configuring {name} ({code})")
        print(f"==========================================")
        
        # If C1 already has test cloned 6aa7ec0e7c0f80000cbd7600, reuse it; otherwise clone template
        if code == "C1":
            cloned_id = "6aa7ec0e7c0f80000cbd7600"
            print(f"Reusing existing cloned C1 sequence: {cloned_id}")
        else:
            print(f"Cloning template {TEMPLATE_SEQUENCE_ID}...")
            clone_res = requests.post(f"https://api.apollo.io/v1/emailer_campaigns/{TEMPLATE_SEQUENCE_ID}/clone", headers=HEADERS, json={})
            if clone_res.status_code != 200:
                print(f"[ERROR] Failed to clone for {code}: {clone_res.status_code} {clone_res.text}")
                continue
            cloned_id = clone_res.json().get("emailer_campaign", {}).get("id")
            print(f"Cloned successfully! New ID: {cloned_id}")
            time.sleep(1)
        
        # Rename sequence
        rename_res = requests.put(f"https://api.apollo.io/v1/emailer_campaigns/{cloned_id}", headers=HEADERS, json={"name": name})
        print(f"Renamed sequence to '{name}': status {rename_res.status_code}")
        
        # Fetch sequence details to get touches and templates
        time.sleep(1)
        camp_res = requests.get(f"https://api.apollo.io/v1/emailer_campaigns/{cloned_id}", headers=HEADERS)
        camp_data = camp_res.json()
        
        touches = camp_data.get("emailer_touches", [])
        steps = camp_data.get("emailer_campaign", {}).get("emailer_steps", [])
        num_steps = camp_data.get("emailer_campaign", {}).get("num_steps", len(steps))
        print(f"Found {num_steps} steps and {len(touches)} touches in sequence {cloned_id}.")
        
        # Map touches by step id or position
        step_id_to_pos = {s.get("id"): s.get("position") for s in steps}
        touch_by_pos = {}
        for t in touches:
            sid = t.get("emailer_step_id")
            pos = step_id_to_pos.get(sid)
            if pos:
                touch_by_pos[pos] = t
        
        # Update Step 1 (Auto email, Touch 1)
        if 1 in touch_by_pos:
            t1 = touch_by_pos[1]
            tid1 = t1.get("emailer_template_id")
            ok = update_template(tid1, spec["step1_subject"], spec["step1_body_text"], spec["step1_body_html"])
            print(f"  Step 1 (Auto Email) template {tid1} updated: {ok}")
        
        # Update Step 2 (LinkedIn Connect, Touch 2)
        if 2 in touch_by_pos:
            t2 = touch_by_pos[2]
            tid2 = t2.get("emailer_template_id")
            ok = update_template(tid2, None, spec["step2_note"], f"<p>{spec['step2_note']}</p>")
            print(f"  Step 2 (LinkedIn Connect) template {tid2} updated: {ok}")
            
        # Update Step 3 (Auto email reply, Touch 3)
        if 3 in touch_by_pos:
            t3 = touch_by_pos[3]
            tid3 = t3.get("emailer_template_id")
            ok = update_template(tid3, None, spec["step3_body_text"], spec["step3_body_html"])
            print(f"  Step 3 (Auto Email Follow-up) template {tid3} updated: {ok}")
            
        # Update Step 4 (LinkedIn Message, Touch 4)
        if 4 in touch_by_pos:
            t4 = touch_by_pos[4]
            tid4 = t4.get("emailer_template_id")
            ok = update_template(tid4, None, spec["step4_note"], f"<p>{spec['step4_note']}</p>")
            print(f"  Step 4 (LinkedIn Message) template {tid4} updated: {ok}")
            
        # Update Step 5 (Auto email reply, Touch 5)
        if 5 in touch_by_pos:
            t5 = touch_by_pos[5]
            tid5 = t5.get("emailer_template_id")
            ok = update_template(tid5, None, spec["step5_body_text"], spec["step5_body_html"])
            print(f"  Step 5 (Auto Email Case Study / Breakup) template {tid5} updated: {ok}")
            
        results[code] = {
            "id": cloned_id,
            "name": name,
            "num_steps": num_steps,
            "touches": len(touches)
        }
    
    print("\n==========================================")
    print("FINAL RESULTS SUMMARY")
    print("==========================================")
    for code, info in results.items():
        print(f"{code}: ID={info['id']} | Steps={info['num_steps']} | Touches={info['touches']} | Name={info['name']}")

if __name__ == "__main__":
    build_sequences()
