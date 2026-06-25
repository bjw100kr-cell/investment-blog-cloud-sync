#!/usr/bin/env python3
import json
import os
import secrets
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs/latest"
OUTPUT_JSON = OUTPUT_DIR / "google-oauth-token-result.json"
AUTH_BASE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
DEFAULT_REDIRECT_URI = "http://127.0.0.1:8765/oauth2callback"

SCOPE_PRESETS = {
    "blogger": [
        "https://www.googleapis.com/auth/blogger",
    ],
    "search_console": [
        "https://www.googleapis.com/auth/webmasters.readonly",
    ],
    "combined": [
        "https://www.googleapis.com/auth/blogger",
        "https://www.googleapis.com/auth/webmasters.readonly",
    ],
}


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        self.server.oauth_code = query.get("code", [""])[0]
        self.server.oauth_state = query.get("state", [""])[0]
        self.server.oauth_error = query.get("error", [""])[0]

        body = (
            "<html><body><h1>Authorization received</h1>"
            "<p>Codex helper received the Google OAuth response.</p>"
            "<p>You can return to the terminal now.</p>"
            "</body></html>"
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, format, *args):  # noqa: A003
        return


def env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def load_env_file() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() not in os.environ:
            os.environ[key.strip()] = value.strip().strip("'").strip('"')


def build_auth_url(client_id: str, redirect_uri: str, state: str, scopes: list[str]) -> str:
    query = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(scopes),
        "access_type": "offline",
        "include_granted_scopes": "true",
        "prompt": "consent",
        "state": state,
    }
    return f"{AUTH_BASE_URL}?{urlencode(query)}"


def exchange_code(client_id: str, client_secret: str, redirect_uri: str, code: str) -> dict:
    response = requests.post(
        TOKEN_URL,
        timeout=30,
        data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        },
    )
    response.raise_for_status()
    return response.json()


def run_local_server(host: str, port: int) -> tuple[HTTPServer, threading.Thread]:
    server = HTTPServer((host, port), OAuthCallbackHandler)
    server.oauth_code = ""
    server.oauth_state = ""
    server.oauth_error = ""
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()
    return server, thread


def main() -> int:
    load_env_file()

    preset = env("GOOGLE_OAUTH_PRESET", "combined").lower()
    if preset not in SCOPE_PRESETS:
        raise SystemExit(f"Unsupported GOOGLE_OAUTH_PRESET: {preset}")

    client_id = env("GOOGLE_CLIENT_ID")
    client_secret = env("GOOGLE_CLIENT_SECRET")
    redirect_uri = env("GOOGLE_REDIRECT_URI", DEFAULT_REDIRECT_URI)
    open_browser = env("GOOGLE_OAUTH_OPEN_BROWSER", "false").lower() in {"1", "true", "yes", "y"}

    if not client_id or not client_secret:
        raise SystemExit("GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must be set in .env or environment.")

    parsed_redirect = urlparse(redirect_uri)
    if parsed_redirect.scheme != "http" or parsed_redirect.hostname not in {"127.0.0.1", "localhost"}:
        raise SystemExit("GOOGLE_REDIRECT_URI must be a local loopback URL such as http://127.0.0.1:8765/oauth2callback")

    host = parsed_redirect.hostname or "127.0.0.1"
    port = parsed_redirect.port or 80
    state = secrets.token_urlsafe(24)
    scopes = SCOPE_PRESETS[preset]

    server, thread = run_local_server(host, port)
    auth_url = build_auth_url(client_id, redirect_uri, state, scopes)

    print("Google OAuth helper")
    print()
    print(f"- preset: {preset}")
    print(f"- redirect_uri: {redirect_uri}")
    print(f"- scopes: {', '.join(scopes)}")
    print()
    print("1. Open this URL in your browser and approve access:")
    print(auth_url)
    print()
    print("2. Google will redirect back to your local machine.")
    print("3. This script will exchange the code for tokens and print the refresh token.")
    print()

    if open_browser:
        webbrowser.open(auth_url)

    thread.join(timeout=300)
    if thread.is_alive():
        server.server_close()
        raise SystemExit("Timed out waiting for Google OAuth callback after 300 seconds.")

    if server.oauth_error:
        server.server_close()
        raise SystemExit(f"Google returned an OAuth error: {server.oauth_error}")

    if server.oauth_state != state:
        server.server_close()
        raise SystemExit("OAuth state mismatch. Aborting.")

    if not server.oauth_code:
        server.server_close()
        raise SystemExit("No authorization code was received.")

    token_payload = exchange_code(client_id, client_secret, redirect_uri, server.oauth_code)
    server.server_close()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(token_payload, ensure_ascii=False, indent=2))

    print("Token exchange complete.")
    print()
    print(f"- output_json: {OUTPUT_JSON}")
    print(f"- access_token_present: {'yes' if token_payload.get('access_token') else 'no'}")
    print(f"- refresh_token_present: {'yes' if token_payload.get('refresh_token') else 'no'}")
    print()

    refresh_token = token_payload.get("refresh_token", "")
    if refresh_token:
        print("Use this refresh token in both places when needed:")
        print(f"- GOOGLE_REFRESH_TOKEN={refresh_token}")
        if preset in {"search_console", "combined"}:
            print(f"- SEARCH_CONSOLE_REFRESH_TOKEN={refresh_token}")
    else:
        print("No refresh token was returned.")
        print("Try again with prompt=consent, make sure this is the first consent for this client, or revoke the app and rerun.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
