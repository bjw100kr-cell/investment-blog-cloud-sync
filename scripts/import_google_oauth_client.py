#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUTPUT_MD = ROOT / "outputs/latest/google-oauth-client-import-report.md"
DEFAULT_REDIRECT_URI = "http://127.0.0.1:8765/oauth2callback"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import Google OAuth client credentials JSON into .env.")
    parser.add_argument("client_json", help="Path to the downloaded Google OAuth client JSON file.")
    parser.add_argument("--env-file", default=str(ENV_PATH), help="Path to the target .env file.")
    parser.add_argument("--prefer-first-redirect", action="store_true", help="Use the first redirect URI from the JSON instead of the default loopback URI.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def parse_env_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text().splitlines()


def set_env_value(lines: list[str], key: str, value: str) -> list[str]:
    updated = False
    rendered = f"{key}={value}"
    out = []
    for raw_line in lines:
        stripped = raw_line.strip()
        if stripped.startswith(f"{key}="):
            out.append(rendered)
            updated = True
        else:
            out.append(raw_line)
    if not updated:
        out.append(rendered)
    return out


def extract_client_payload(payload: dict) -> dict:
    if "web" in payload:
        return payload["web"]
    if "installed" in payload:
        return payload["installed"]
    raise SystemExit("Unsupported Google OAuth client JSON format. Expected top-level 'web' or 'installed'.")


def choose_redirect_uri(client_payload: dict, prefer_first_redirect: bool) -> str:
    redirect_uris = client_payload.get("redirect_uris", []) or []
    if prefer_first_redirect and redirect_uris:
        return redirect_uris[0]
    if DEFAULT_REDIRECT_URI in redirect_uris or not redirect_uris:
        return DEFAULT_REDIRECT_URI
    loopback_candidates = [uri for uri in redirect_uris if uri.startswith("http://127.0.0.1") or uri.startswith("http://localhost")]
    if loopback_candidates:
        return loopback_candidates[0]
    return DEFAULT_REDIRECT_URI


def write_report(env_path: Path, client_json: Path, applied: dict[str, str], redirect_candidates: list[str]) -> None:
    lines = []
    lines.append("# Google OAuth Client Import Report")
    lines.append("")
    lines.append(f"- env_file: `{env_path}`")
    lines.append(f"- client_json: `{client_json}`")
    lines.append("")
    lines.append("## Applied")
    lines.append("")
    for key in applied:
        lines.append(f"- `{key}`")
    lines.append("")
    lines.append("## Redirect URIs In Source JSON")
    lines.append("")
    if redirect_candidates:
        for uri in redirect_candidates:
            lines.append(f"- `{uri}`")
    else:
        lines.append("- 없음")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    client_json = Path(args.client_json)
    env_path = Path(args.env_file)

    if not client_json.exists():
        raise SystemExit(f"Client JSON not found: {client_json}")

    payload = load_json(client_json)
    client_payload = extract_client_payload(payload)
    client_id = (client_payload.get("client_id") or "").strip()
    client_secret = (client_payload.get("client_secret") or "").strip()
    if not client_id or not client_secret:
        raise SystemExit("client_id or client_secret missing in OAuth client JSON.")

    redirect_uri = choose_redirect_uri(client_payload, args.prefer_first_redirect)
    env_lines = parse_env_lines(env_path)
    if not env_lines and not env_path.exists():
        raise SystemExit(f".env file not found: {env_path}")

    env_lines = set_env_value(env_lines, "GOOGLE_CLIENT_ID", client_id)
    env_lines = set_env_value(env_lines, "GOOGLE_CLIENT_SECRET", client_secret)
    env_lines = set_env_value(env_lines, "SEARCH_CONSOLE_CLIENT_ID", client_id)
    env_lines = set_env_value(env_lines, "SEARCH_CONSOLE_CLIENT_SECRET", client_secret)
    env_lines = set_env_value(env_lines, "GOOGLE_REDIRECT_URI", redirect_uri)
    env_path.write_text("\n".join(env_lines) + "\n")

    applied = {
        "GOOGLE_CLIENT_ID": client_id,
        "GOOGLE_CLIENT_SECRET": client_secret,
        "SEARCH_CONSOLE_CLIENT_ID": client_id,
        "SEARCH_CONSOLE_CLIENT_SECRET": client_secret,
        "GOOGLE_REDIRECT_URI": redirect_uri,
    }
    write_report(env_path, client_json, applied, client_payload.get("redirect_uris", []) or [])
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
