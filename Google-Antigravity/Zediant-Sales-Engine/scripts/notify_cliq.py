"""
Zediant Revenue Engine - Zoho Cliq Notification Utility
Authoritative Target Channel: #Z-Outreach-Auto-Update (P1064180000001095002)

Supports:
1. Incoming Webhook (Recommended): CLIQ_WEBHOOK_URL in .env
2. OAuth Fallback: ZohoCliq.Messages.CREATE scope on Zoho OAuth refresh token
"""

import os
import sys
import json
import re
import requests
from dotenv import load_dotenv

ENV_PATH = r"c:\Work\Zediant\Sales\Google-Antigravity\Zediant-Sales-Engine\.env"
load_dotenv(ENV_PATH)

DEFAULT_CHANNEL_ID = "P1064180000001095002"  # #Z-Outreach-Auto-Update
CLIQ_API_BASE = os.getenv("CLIQ_API_DOMAIN", "https://cliq.zoho.in/api/v2")


def send_cliq_notification(message_text: str, channel_id: str = DEFAULT_CHANNEL_ID) -> dict:
    """
    Sends an aggregate-only summary notification to Zoho Cliq.
    Enforces format discipline: No individual emails.
    """
    # Safety sanity check: Never allow individual email addresses to be posted in the Cliq channel
    emails_found = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', message_text)
    prospect_emails = [e for e in emails_found if not e.endswith("@zediant.com") and not e.endswith("@zedianttechnologies.info")]
    if prospect_emails:
        raise ValueError(f"Cliq Policy Violation: Message contains individual prospect email addresses: {prospect_emails}")

    webhook_url = os.getenv("CLIQ_WEBHOOK_URL")

    # Strategy 1: Incoming Webhook (Preferred & zero OAuth scope conflict)
    if webhook_url and webhook_url.strip():
        try:
            resp = requests.post(
                webhook_url.strip(),
                headers={"Content-Type": "application/json"},
                json={"text": message_text},
                timeout=15
            )
            if resp.status_code in [200, 204]:
                return {"status": "success", "method": "webhook", "http_code": resp.status_code}
            else:
                return {
                    "status": "error",
                    "method": "webhook",
                    "http_code": resp.status_code,
                    "response": resp.text
                }
        except Exception as e:
            return {"status": "error", "method": "webhook", "error": str(e)}

    # Strategy 2: OAuth API Call (Requires ZohoCliq.Messages.CREATE scope)
    client_id = os.getenv("ZOHO_CLIENT_ID")
    client_secret = os.getenv("ZOHO_CLIENT_SECRET")
    refresh_token = os.getenv("ZOHO_REFRESH_TOKEN")
    accounts_url = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")

    if not (client_id and client_secret and refresh_token):
        return {
            "status": "error",
            "method": "none",
            "error": "Neither CLIQ_WEBHOOK_URL nor Zoho OAuth credentials configured."
        }

    # Fetch access token
    try:
        r = requests.post(f"{accounts_url}/token", data={
            "grant_type": "refresh_token",
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token
        }, timeout=15)
        token_data = r.json()
        access_token = token_data.get("access_token")
        if not access_token:
            return {
                "status": "error",
                "method": "oauth",
                "error": f"Failed to refresh Zoho token: {token_data}"
            }

        # Try channel unique name first, then channel ID
        urls_to_try = [
            f"{CLIQ_API_BASE}/channelsbyname/zoutreachautoupdate/message",
            f"{CLIQ_API_BASE}/channels/{channel_id}/message"
        ]
        last_resp = None
        for post_url in urls_to_try:
            msg_resp = requests.post(
                post_url,
                headers={
                    "Authorization": f"Zoho-oauthtoken {access_token}",
                    "Content-Type": "application/json"
                },
                json={"text": message_text},
                timeout=15
            )
            last_resp = msg_resp
            if msg_resp.status_code in [200, 201, 204]:
                return {"status": "success", "method": "oauth", "http_code": msg_resp.status_code, "data": msg_resp.json() if msg_resp.text else "Message posted successfully"}

        return {
            "status": "error",
            "method": "oauth",
            "http_code": last_resp.status_code if last_resp else None,
            "response": last_resp.json() if (last_resp and "application/json" in last_resp.headers.get("Content-Type", "")) else (last_resp.text if last_resp else None)
        }
    except Exception as e:
        return {"status": "error", "method": "oauth", "error": str(e)}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_msg = sys.argv[1]
    else:
        test_msg = "🤖 [Zediant Revenue Engine] Notification Test: System check."

    print(f"Attempting to post notification to Cliq Channel {DEFAULT_CHANNEL_ID}...")
    result = send_cliq_notification(test_msg)
    print("Result:", json.dumps(result, indent=2))
