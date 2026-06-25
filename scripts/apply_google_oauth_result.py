#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
TOKEN_JSON = ROOT / "outputs/latest/google-oauth-token-result.json"
OUTPUT_MD = ROOT / "outputs/latest/google-oauth-apply-report.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply the latest Google OAuth token result into .env.")
    parser.add_argument("--token-json", default=str(TOKEN_JSON), help="Path to google-oauth-token-result.json")
    parser.add_argument("--env-file", default=str(ENV_PATH), help="Path to .env file")
    parser.add_argument("--include-access-token", action="store_true", help="Also write GOOGLE_ACCESS_TOKEN and SEARCH_CONSOLE_ACCESS_TOKEN")
    return parser.parse_args()


def parse_env_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text().splitlines()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


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


def write_report(env_file: Path, token_file: Path, applied: dict[str, str], skipped: list[str]) -> None:
    lines = []
    lines.append("# Google OAuth Apply Report")
    lines.append("")
    lines.append(f"- env_file: `{env_file}`")
    lines.append(f"- token_file: `{token_file}`")
    lines.append("")
    lines.append("## Applied")
    lines.append("")
    if applied:
        for key in applied:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 새로 반영한 값이 없습니다.")
    lines.append("")
    lines.append("## Skipped")
    lines.append("")
    if skipped:
        for key in skipped:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 없음")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    token_path = Path(args.token_json)
    env_path = Path(args.env_file)

    if not token_path.exists():
        raise SystemExit(f"Token JSON not found: {token_path}")

    payload = load_json(token_path)
    env_lines = parse_env_lines(env_path)
    if not env_lines and not env_path.exists():
        raise SystemExit(f".env file not found: {env_path}")

    refresh_token = (payload.get("refresh_token") or "").strip()
    access_token = (payload.get("access_token") or "").strip()

    applied: dict[str, str] = {}
    skipped: list[str] = []

    if refresh_token:
        env_lines = set_env_value(env_lines, "GOOGLE_REFRESH_TOKEN", refresh_token)
        env_lines = set_env_value(env_lines, "SEARCH_CONSOLE_REFRESH_TOKEN", refresh_token)
        applied["GOOGLE_REFRESH_TOKEN"] = refresh_token
        applied["SEARCH_CONSOLE_REFRESH_TOKEN"] = refresh_token
    else:
        skipped.extend(["GOOGLE_REFRESH_TOKEN", "SEARCH_CONSOLE_REFRESH_TOKEN"])

    if args.include_access_token:
        if access_token:
            env_lines = set_env_value(env_lines, "GOOGLE_ACCESS_TOKEN", access_token)
            env_lines = set_env_value(env_lines, "SEARCH_CONSOLE_ACCESS_TOKEN", access_token)
            applied["GOOGLE_ACCESS_TOKEN"] = access_token
            applied["SEARCH_CONSOLE_ACCESS_TOKEN"] = access_token
        else:
            skipped.extend(["GOOGLE_ACCESS_TOKEN", "SEARCH_CONSOLE_ACCESS_TOKEN"])

    env_path.write_text("\n".join(env_lines) + "\n")
    write_report(env_path, token_path, applied, skipped)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
