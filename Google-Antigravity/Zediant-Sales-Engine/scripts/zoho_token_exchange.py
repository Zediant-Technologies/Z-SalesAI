"""
Zoho CRM OAuth Token Generator for India Datacenter (accounts.zoho.in)
Captures OAuth callback on http://localhost:8080/callback and updates .env and .gemini/mcp_config.json
"""

import os
import sys
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, urlencode
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
USER_MCP_CONFIG_PATH = os.path.expanduser(r"~/.gemini/config/mcp_config.json")
WORKSPACE_MCP_CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".gemini", "mcp_config.json"))

load_dotenv(ENV_PATH)

CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI", "http://localhost:8080/callback")
ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2")
API_DOMAIN = os.getenv("ZOHO_API_DOMAIN", "https://www.zohoapis.in")
SCOPE = os.getenv("ZOHO_SCOPE", "ZohoCRM.modules.ALL,ZohoCRM.users.READ")

auth_code = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query_components = parse_qs(urlparse(self.path).query)
        if "code" in query_components:
            auth_code = query_components["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Authorization Successful!</h1><p>You can close this window now. Antigravity is saving your tokens.</p>")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Authorization Failed</h1><p>No code returned in callback.</p>")

    def log_message(self, format, *args):
        return

def exchange_code(code):
    print(f"Exchanging code for tokens with {ACCOUNTS_URL}/token...")
    resp = requests.post(
        f"{ACCOUNTS_URL}/token",
        data={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "code": code
        },
        timeout=30
    )
    if resp.status_code != 200:
        print(f"Error from Zoho: {resp.status_code} - {resp.text}")
        sys.exit(1)
    
    tokens = resp.json()
    if "error" in tokens:
        print(f"Zoho Error: {tokens}")
        sys.exit(1)

    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    
    print("\nTokens successfully received!")
    print(f"Access Token: {access_token[:15]}...")
    if refresh_token:
        print(f"Refresh Token: {refresh_token[:15]}...")
    else:
        print("Note: Refresh token was not returned (Zoho only returns it on first consent or with prompt=consent).")

    # Update .env
    update_env(access_token, refresh_token)
    
    # Update .gemini/mcp_config.json
    update_mcp_config(access_token, refresh_token)
    print("\nSetup complete! Zoho CRM MCP server is fully configured.")

def update_env(access_token, refresh_token):
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if "ZOHO_ACCESS_TOKEN=" in content:
        import re
        content = re.sub(r"ZOHO_ACCESS_TOKEN=.*", f"ZOHO_ACCESS_TOKEN={access_token}", content)
        if refresh_token:
            content = re.sub(r"ZOHO_REFRESH_TOKEN=.*", f"ZOHO_REFRESH_TOKEN={refresh_token}", content)
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {ENV_PATH}")

def update_mcp_config(access_token, refresh_token):
    for cfg_path in [USER_MCP_CONFIG_PATH, WORKSPACE_MCP_CONFIG_PATH]:
        if not os.path.exists(cfg_path):
            continue
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            
            zoho_env = config.get("mcpServers", {}).get("zoho-crm", {}).get("env", {})
            zoho_env["ZOHO_CLIENT_ID"] = CLIENT_ID
            zoho_env["ZOHO_CLIENT_SECRET"] = CLIENT_SECRET
            zoho_env["ZOHO_REDIRECT_URI"] = REDIRECT_URI
            zoho_env["ZOHO_API_DOMAIN"] = API_DOMAIN
            zoho_env["ZOHO_ACCOUNTS_URL"] = ACCOUNTS_URL
            zoho_env["ZOHO_ACCESS_TOKEN"] = access_token
            if refresh_token:
                zoho_env["ZOHO_REFRESH_TOKEN"] = refresh_token
            
            with open(cfg_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
            print(f"Updated {cfg_path}")
        except Exception as e:
            print(f"Failed to update {cfg_path}: {e}")

def main():
    if not CLIENT_ID or CLIENT_ID == "your_zoho_client_id_here":
        print("ERROR: Please set ZOHO_CLIENT_ID in your .env file first.")
        sys.exit(1)
    if not CLIENT_SECRET or CLIENT_SECRET == "your_zoho_client_secret_here":
        print("ERROR: Please set ZOHO_CLIENT_SECRET in your .env file first.")
        sys.exit(1)

    auth_params = {
        "scope": SCOPE,
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = f"{ACCOUNTS_URL}/auth?{urlencode(auth_params)}"

    print("=" * 60)
    print("Zoho CRM OAuth Token Generator")
    print("=" * 60)
    print(f"\nStarting callback server on port 8080...")
    
    server = HTTPServer(("localhost", 8080), OAuthCallbackHandler)
    print(f"\nOpening browser for authorization:\n{auth_url}\n")
    webbrowser.open(auth_url)
    
    print("Waiting for callback on http://localhost:8080/callback ...")
    server.handle_request()
    
    if auth_code:
        exchange_code(auth_code)
    else:
        print("Failed to capture authorization code.")

if __name__ == "__main__":
    main()
