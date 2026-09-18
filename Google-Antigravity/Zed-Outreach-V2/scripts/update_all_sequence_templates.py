import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
HEADERS = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "X-Api-Key": APOLLO_API_KEY
}

CAMPAIGNS = {
    "C1": {
        "id": "6aa7ec0e7c0f80000cbd7600",
        "name": "C1 - AI-Enabled Product Engineering",
        "step1_subject": "{{company}}'s product roadmap",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><div style=\"white-space: pre-wrap;\">{{Personalised Email}}</div><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}.\n\nWe partner with engineering leaders on AI-accelerated delivery and senior product squads. Would love to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my note around {{Pain Point}}.\n\nWhen product teams aim to accelerate their delivery velocity, the bottleneck is rarely lack of ideas - it's complex data pipelines, workflow integrations, and senior engineers being pulled into maintenance rather than shipping new features.\n\nWe embed dedicated senior squads who take full ownership of feature execution, using modern tooling so your core team can hit roadmap milestones 30-40% faster.\n\nWorth sending over that 2-minute teardown, or is roadmap delivery well in hand this quarter?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my note around {{Pain Point}}.</p><p>When product teams aim to accelerate their delivery velocity, the bottleneck is rarely lack of ideas - it's complex data pipelines, workflow integrations, and senior engineers being pulled into maintenance rather than shipping new features.</p><p>We embed dedicated senior squads who take full ownership of feature execution, using modern tooling so your core team can hit roadmap milestones 30-40% faster.</p><p>Worth sending over that 2-minute teardown, or is roadmap delivery well in hand this quarter?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step4_note": "Thanks for connecting, {{first_name}}.\n\nCurious rather than pitching - what's the biggest constraint on {{company}}'s feature delivery right now: finding specialized senior engineers or keeping sprint velocity high?",
        "step5_body_text": "Hi {{first_name}},\n\nOne quick benchmark from our engineering sprint onboardings:\n\nMost teams trying to roll out complex product features lose 3-4 weeks just on setup: repo onboarding, environment parity, and architectural alignment.\n\nWhen our squads embed, we operate under a strict 14-day production readiness framework:\n1. Day 1-5: Repo onboarding, dev environment spin-up, and architecture sign-off.\n2. Day 6-10: First PR merged into staging under your CI/CD test suites.\n3. Day 11+: Full sprint velocity shipping production code alongside your team.\n\nWorth a quick 10-minute exchange on how this framework fits {{company}}'s roadmap, or is delivery fully covered for now?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>One quick benchmark from our engineering sprint onboardings:</p><p>Most teams trying to roll out complex product features lose 3-4 weeks just on setup: repo onboarding, environment parity, and architectural alignment.</p><p>When our squads embed, we operate under a strict 14-day production readiness framework:<br>1. Day 1-5: Repo onboarding, dev environment spin-up, and architecture sign-off.<br>2. Day 6-10: First PR merged into staging under your CI/CD test suites.<br>3. Day 11+: Full sprint velocity shipping production code alongside your team.</p><p>Worth a quick 10-minute exchange on how this framework fits {{company}}'s roadmap, or is delivery fully covered for now?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step6_body_text": "Hi {{first_name}},\n\nLast note from me. If roadmap acceleration or engineering capacity isn't an active priority for {{company}} right now, no worries at all.\n\nShould I check back in with you next quarter, or is delivery bandwidth pretty well locked in for the year?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step6_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If roadmap acceleration or engineering capacity isn't an active priority for {{company}} right now, no worries at all.</p><p>Should I check back in with you next quarter, or is delivery bandwidth pretty well locked in for the year?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
    },
    "C2": {
        "id": "6aa7eca553473f000c678940",
        "name": "C2 - Engineering Pods & Staff Augmentation",
        "step1_subject": "engineering bandwidth at {{company}}",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><div style=\"white-space: pre-wrap;\">{{Personalised Email}}</div><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}.\n\nWe help scaling software teams embed senior engineering pods within 2-3 weeks. Would like to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my earlier note around {{Pain Point}}.\n\nThe three questions engineering leaders ask us first:\n1. How senior? Five-plus years, and you interview and approve every developer.\n2. How fast? Squad live and delivering in two to three weeks.\n3. What engagement? Dedicated month-to-month, embedded in your ceremonies and repos.\n\nWorth a quick 15-minute chat to see if this solves any headcount bottlenecks at {{company}}?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my earlier note around {{Pain Point}}.</p><p>The three questions engineering leaders ask us first:<br>1. How senior? Five-plus years, and you interview and approve every developer.<br>2. How fast? Squad live and delivering in two to three weeks.<br>3. What engagement? Dedicated month-to-month, embedded in your ceremonies and repos.</p><p>Worth a quick 15-minute chat to see if this solves any headcount bottlenecks at {{company}}?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step4_note": "Thanks for connecting, {{first_name}}.\n\nCurious rather than pitching - what's the hardest engineering role to fill on your team right now: senior fullstack leads, frontend specialists, or cloud architects?",
        "step5_body_text": "Hi {{first_name}},\n\nQuick delivery insight when scaling engineering headcount:\n\nMost teams lose momentum when external hires need constant management. We structure our pods with autonomous senior leads who own sprint commitments, run PR reviews, and maintain test coverage.\n\nResult: your core in-house leads spend less time unblocking contractors and more time driving strategic architecture.\n\nOpen to reviewing our pod onboarding playbook to see how this fits {{company}}?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>Quick delivery insight when scaling engineering headcount:</p><p>Most teams lose momentum when external hires need constant management. We structure our pods with autonomous senior leads who own sprint commitments, run PR reviews, and maintain test coverage.</p><p>Result: your core in-house leads spend less time unblocking contractors and more time driving strategic architecture.</p><p>Open to reviewing our pod onboarding playbook to see how this fits {{company}}?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step6_body_text": "Hi {{first_name}},\n\nLast note from me. If adding senior engineering capacity isn't an active priority for {{company}} right now, no worries at all.\n\nShould I check back in with you next quarter, or is engineering headcount well covered for the year?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step6_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If adding senior engineering capacity isn't an active priority for {{company}} right now, no worries at all.</p><p>Should I check back in with you next quarter, or is engineering headcount well covered for the year?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
    },
    "C3": {
        "id": "6aa7ecb31fd57300143fbfa7",
        "name": "C3 - Platform Engineering & Cloud Modernization",
        "step1_subject": "{{company}}'s cloud infrastructure",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><div style=\"white-space: pre-wrap;\">{{Personalised Email}}</div><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}.\n\nWe partner with engineering teams on cloud modernization, Kubernetes, and platform resilience. Great to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my note around {{Pain Point}}.\n\nMany engineering leaders find their core developers spending 30%+ of their sprints wrestling with deployment pipelines, infrastructure debt, or rising cloud bills instead of shipping product features.\n\nOur platform engineers help automate CI/CD, optimize cloud spend, and harden multi-tenant environments so your product engineers can focus on shipping.\n\nWorth sending over that 2-minute teardown, or is cloud infrastructure well covered this quarter?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my note around {{Pain Point}}.</p><p>Many engineering leaders find their core developers spending 30%+ of their sprints wrestling with deployment pipelines, infrastructure debt, or rising cloud bills instead of shipping product features.</p><p>Our platform engineers help automate CI/CD, optimize cloud spend, and harden multi-tenant environments so your product engineers can focus on shipping.</p><p>Worth sending over that 2-minute teardown, or is cloud infrastructure well covered this quarter?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step4_note": "Glad to connect, {{first_name}}.\n\nQuick question - are deployment friction or infrastructure maintenance mostly handled by your core dev team right now, or do you have a dedicated DevOps squad?",
        "step5_body_text": "Hi {{first_name}},\n\nA quick metric from our cloud infrastructure audits:\n\nAcross modern SaaS stacks, an unoptimized Kubernetes cluster or unmonitored egress typically wastes 25-40% of monthly cloud budget, while manual deployment pipelines add hours of release friction.\n\nWe conduct 5-day infrastructure and CI/CD reviews that pinpoint deployment bottlenecks and optimize cloud spend without touching product logic.\n\nWould you be open to a 2-minute summary of how this audit works?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>A quick metric from our cloud infrastructure audits:</p><p>Across modern SaaS stacks, an unoptimized Kubernetes cluster or unmonitored egress typically wastes 25-40% of monthly cloud budget, while manual deployment pipelines add hours of release friction.</p><p>We conduct 5-day infrastructure and CI/CD reviews that pinpoint deployment bottlenecks and optimize cloud spend without touching product logic.</p><p>Would you be open to a 2-minute summary of how this audit works?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step6_body_text": "Hi {{first_name}},\n\nLast note from me. If platform modernization or cloud infrastructure isn't an active priority for {{company}} right now, no worries at all.\n\nShould I check back in with you next quarter, or are platform and DevOps workflows well in hand?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step6_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If platform modernization or cloud infrastructure isn't an active priority for {{company}} right now, no worries at all.</p><p>Should I check back in with you next quarter, or are platform and DevOps workflows well in hand?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
    },
    "C4": {
        "id": "6aa7ecbea907dd00140753b2",
        "name": "C4 - Middleware & API Integration (ZCoupler)",
        "step1_subject": "system integrations at {{company}}",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><div style=\"white-space: pre-wrap;\">{{Personalised Email}}</div><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}.\n\nWe specialize in enterprise API integrations and robust middleware. Let's connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my note around {{Pain Point}}.\n\nCustom integrations between enterprise platforms, CRMs, ERPs, and legacy databases often stall internal roadmaps because nobody wants to build and maintain fragile point-to-point glue code.\n\nOur integration engineers build robust, two-way, fault-tolerant middleware that syncs transaction data reliably in real time.\n\nWorth sending over that 2-minute teardown, or are your system integrations well covered this quarter?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my note around {{Pain Point}}.</p><p>Custom integrations between enterprise platforms, CRMs, ERPs, and legacy databases often stall internal roadmaps because nobody wants to build and maintain fragile point-to-point glue code.</p><p>Our integration engineers build robust, two-way, fault-tolerant middleware that syncs transaction data reliably in real time.</p><p>Worth sending over that 2-minute teardown, or are your system integrations well covered this quarter?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step4_note": "Thanks for connecting, {{first_name}}.\n\nQuick question - are third-party API syncs or data bridging creating friction in your workflows, or is your internal stack already well integrated?",
        "step5_body_text": "Hi {{first_name}},\n\nOne common pattern we see with enterprise integrations:\n\nWhen systems sync via direct webhook scripts without queuing or dead-letter handling, temporary third-party API rate limits cause silent data drops that require manual reconciliation.\n\nOur middleware framework implements automated retry logic, bi-directional sync validation, and schema mapping so data flows reliably without developer intervention.\n\nOpen to seeing a quick architecture teardown of an enterprise CRM/ERP sync we recently deployed?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>One common pattern we see with enterprise integrations:</p><p>When systems sync via direct webhook scripts without queuing or dead-letter handling, temporary third-party API rate limits cause silent data drops that require manual reconciliation.</p><p>Our middleware framework implements automated retry logic, bi-directional sync validation, and schema mapping so data flows reliably without developer intervention.</p><p>Open to seeing a quick architecture teardown of an enterprise CRM/ERP sync we recently deployed?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step6_body_text": "Hi {{first_name}},\n\nClosing the loop on this. If third-party integrations and data syncing aren't creating any bottlenecks for {{company}}, no worries at all.\n\nShould I check back in with you next quarter, or are your system integrations running smoothly for the year?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step6_body_html": "<p>Hi {{first_name}},</p><p>Closing the loop on this. If third-party integrations and data syncing aren't creating any bottlenecks for {{company}}, no worries at all.</p><p>Should I check back in with you next quarter, or are your system integrations running smoothly for the year?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
    },
    "C5": {
        "id": "6aa7ecc953473f000c678b8e",
        "name": "C5 - Enterprise Custom Development & Modernization",
        "step1_subject": "modernizing {{company}}'s core systems",
        "step1_body_text": "Hi {{first_name}},\n\n{{Personalised Email}}\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step1_body_html": "<p>Hi {{first_name}},</p><div style=\"white-space: pre-wrap;\">{{Personalised Email}}</div><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step2_note": "Hi {{first_name}} - noticed {{Company Trigger}} at {{company}}.\n\nWe partner with enterprises on incremental legacy system modernization and cloud architecture. Great to connect.",
        "step3_body_text": "Hi {{first_name}},\n\nFollowing up on my note around {{Pain Point}}.\n\nThe biggest risk with legacy system upgrades is the fear of breaking mission-critical operations during a monolithic rewrite.\n\nOur team specializes in the strangler pattern - decomposing legacy monoliths, modernizing frontend/backend components incrementally, and deploying microservices while keeping existing business operations uninterrupted.\n\nAre you evaluating any modernization initiatives this year?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step3_body_html": "<p>Hi {{first_name}},</p><p>Following up on my note around {{Pain Point}}.</p><p>The biggest risk with legacy system upgrades is the fear of breaking mission-critical operations during a monolithic rewrite.</p><p>Our team specializes in the strangler pattern - decomposing legacy monoliths, modernizing frontend/backend components incrementally, and deploying microservices while keeping existing business operations uninterrupted.</p><p>Are you evaluating any modernization initiatives this year?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step4_note": "Great to connect, {{first_name}}.\n\nQuick question - are legacy dependencies slowing down feature delivery at {{company}}, or is system maintenance well in hand?",
        "step5_body_text": "Hi {{first_name}},\n\nA quick perspective on legacy modernization risk:\n\nThe #1 reason monolithic refactors fail or exceed budget is attempting a \"big-bang\" cutover instead of progressive decoupling.\n\nWe deploy specialized squads who extract high-load modules one API contract at a time, establishing automated regression test suites around legacy code before refactoring.\n\nWould you be open to reviewing a short case breakdown of an incremental monolith decomposition we completed?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step5_body_html": "<p>Hi {{first_name}},</p><p>A quick perspective on legacy modernization risk:</p><p>The #1 reason monolithic refactors fail or exceed budget is attempting a \"big-bang\" cutover instead of progressive decoupling.</p><p>We deploy specialized squads who extract high-load modules one API contract at a time, establishing automated regression test suites around legacy code before refactoring.</p><p>Would you be open to reviewing a short case breakdown of an incremental monolith decomposition we completed?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
        "step6_body_text": "Hi {{first_name}},\n\nLast note from me. If refactoring legacy systems or core architectures isn't on {{company}}'s roadmap right now, no worries at all.\n\nShould I check back in with you later in the year, or is architecture maintenance well covered?\n\nBest,\nRajeev Jaiswal\nCo-Founder | Zediant Technologies",
        "step6_body_html": "<p>Hi {{first_name}},</p><p>Last note from me. If refactoring legacy systems or core architectures isn't on {{company}}'s roadmap right now, no worries at all.</p><p>Should I check back in with you later in the year, or is architecture maintenance well covered?</p><p>Best,<br>Rajeev Jaiswal<br>Co-Founder | Zediant Technologies</p>",
    }
}


def update_template(tid, subject, body_text, body_html):
    url = f"https://api.apollo.io/v1/emailer_templates/{tid}"
    payload = {
        "body_text": body_text,
        "body_html": body_html
    }
    if subject:
        payload["subject"] = subject
    res = requests.put(url, headers=HEADERS, json=payload)
    if res.status_code == 200:
        data = res.json().get("emailer_template", {})
        return True, data.get("subject"), (data.get("body_text") or "")[:60]
    return False, None, None


def main():
    for code, spec in CAMPAIGNS.items():
        cid = spec["id"]
        name = spec["name"]
        print(f"\n==========================================")
        print(f"Updating Templates for {name} ({cid})")
        print(f"==========================================")
        
        camp_res = requests.get(f"https://api.apollo.io/v1/emailer_campaigns/{cid}", headers=HEADERS)
        camp_data = camp_res.json()
        
        touches = camp_data.get("emailer_touches", [])
        steps = camp_data.get("emailer_campaign", {}).get("emailer_steps", [])
        
        step_id_to_pos = {s.get("id"): s.get("position") for s in steps}
        touch_by_pos = {}
        for t in touches:
            sid = t.get("emailer_step_id")
            pos = step_id_to_pos.get(sid)
            if pos:
                touch_by_pos[pos] = t
                
        # Touch 1 (Step 1 auto_email)
        if 1 in touch_by_pos:
            tid = touch_by_pos[1].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, spec["step1_subject"], spec["step1_body_text"], spec["step1_body_html"])
            print(f"Step 1 updated: {ok} | Subj: {subj} | Snippet: {snippet}")
            
        # Touch 2 (Step 2 linkedin_step_connect)
        if 2 in touch_by_pos:
            tid = touch_by_pos[2].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, None, spec["step2_note"], f"<p>{spec['step2_note']}</p>")
            print(f"Step 2 updated: {ok} | Snippet: {snippet}")
            
        # Touch 3 (Step 3 auto_email)
        if 3 in touch_by_pos:
            tid = touch_by_pos[3].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, None, spec["step3_body_text"], spec["step3_body_html"])
            print(f"Step 3 updated: {ok} | Snippet: {snippet}")
            
        # Touch 4 (Step 4 linkedin_step_message)
        if 4 in touch_by_pos:
            tid = touch_by_pos[4].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, None, spec["step4_note"], f"<p>{spec['step4_note']}</p>")
            print(f"Step 4 updated: {ok} | Snippet: {snippet}")
            
        # Touch 5 (Step 5 auto_email)
        if 5 in touch_by_pos:
            tid = touch_by_pos[5].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, "", spec["step5_body_text"], spec["step5_body_html"])
            print(f"Step 5 updated: {ok} | Snippet: {snippet}")

        # Touch 6 (Step 6 auto_email)
        if 6 in touch_by_pos:
            tid = touch_by_pos[6].get("emailer_template_id")
            ok, subj, snippet = update_template(tid, "", spec["step6_body_text"], spec["step6_body_html"])
            print(f"Step 6 updated: {ok} | Snippet: {snippet}")

if __name__ == "__main__":
    main()
