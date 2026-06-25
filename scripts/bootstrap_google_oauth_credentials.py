#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

from env_loader import load_env_file


ROOT = Path(__file__).resolve().parents[1]
DISCOVERY_JSON = ROOT / "outputs/latest/google-oauth-client-discovery.json"
TOKEN_JSON = ROOT / "outputs/latest/google-oauth-token-result.json"
OUTPUT_MD = ROOT / "outputs/latest/google-oauth-bootstrap-report.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover and import the latest Google OAuth client JSON, and optionally apply a saved refresh token."
    )
    parser.add_argument(
        "--apply-token-if-present",
        action="store_true",
        help="If outputs/latest/google-oauth-token-result.json exists, also apply it into .env.",
    )
    parser.add_argument(
        "--prefer-first-redirect",
        action="store_true",
        help="Pass through to import_google_oauth_client.py when importing the client JSON.",
    )
    return parser.parse_args()


def run_command(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def latest_candidate() -> dict:
    payload = load_json(DISCOVERY_JSON)
    candidates = payload.get("candidates", [])
    if not candidates:
        return {}
    return candidates[0]


def write_report(report: dict) -> None:
    lines = []
    lines.append("# Google OAuth Bootstrap Report")
    lines.append("")
    lines.append(f"- imported_client: `{report.get('imported_client', False)}`")
    lines.append(f"- applied_token: `{report.get('applied_token', False)}`")
    lines.append(f"- candidate_count: `{report.get('candidate_count', 0)}`")
    lines.append("")
    if report.get("selected_client_path"):
        lines.append(f"- selected_client_path: `{report.get('selected_client_path')}`")
        lines.append("")
    lines.append("## Steps")
    lines.append("")
    for step in report.get("steps", []):
        lines.append(f"- `{step['name']}`: returncode `{step['returncode']}`")
        if step.get("stdout"):
            lines.append(f"  - stdout: {step['stdout']}")
        if step.get("stderr"):
            lines.append(f"  - stderr: {step['stderr']}")
    lines.append("")
    lines.append("## Next Action")
    lines.append("")
    lines.append(f"- {report.get('next_action', 'No action computed.')}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    load_env_file(ROOT)

    steps: list[dict] = []
    discovery = run_command(["python3", "scripts/find_google_oauth_client.py"])
    steps.append(
        {
            "name": "find_google_oauth_client",
            "returncode": discovery.returncode,
            "stdout": discovery.stdout.strip(),
            "stderr": discovery.stderr.strip(),
        }
    )
    if discovery.returncode != 0:
        report = {
            "imported_client": False,
            "applied_token": False,
            "candidate_count": 0,
            "selected_client_path": "",
            "steps": steps,
            "next_action": "Google OAuth client 탐색 단계가 실패했습니다. client_secret JSON 다운로드 여부를 확인합니다.",
        }
        write_report(report)
        print(OUTPUT_MD)
        return discovery.returncode

    candidate = latest_candidate()
    imported_client = False
    applied_token = False
    next_action = "Google Cloud Console에서 OAuth client JSON을 다운로드한 뒤 다시 실행합니다."

    if candidate:
        command = ["python3", "scripts/import_google_oauth_client.py", candidate["path"]]
        if args.prefer_first_redirect:
            command.append("--prefer-first-redirect")
        imported = run_command(command)
        steps.append(
            {
                "name": "import_google_oauth_client",
                "returncode": imported.returncode,
                "stdout": imported.stdout.strip(),
                "stderr": imported.stderr.strip(),
            }
        )
        imported_client = imported.returncode == 0
        if imported_client:
            next_action = "GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py 를 실행해 refresh token을 발급합니다."
        else:
            next_action = "client_secret JSON은 찾았지만 .env 반영에 실패했습니다. import report를 확인합니다."

    if args.apply_token_if_present and TOKEN_JSON.exists():
        applied = run_command(["python3", "scripts/apply_google_oauth_result.py"])
        steps.append(
            {
                "name": "apply_google_oauth_result",
                "returncode": applied.returncode,
                "stdout": applied.stdout.strip(),
                "stderr": applied.stderr.strip(),
            }
        )
        applied_token = applied.returncode == 0
        if applied_token:
            next_action = "python3 scripts/check_setup.py 를 실행해 Blogger/Search Console 연결 상태를 다시 확인합니다."

    report = {
        "imported_client": imported_client,
        "applied_token": applied_token,
        "candidate_count": load_json(DISCOVERY_JSON).get("candidate_count", 0),
        "selected_client_path": candidate.get("path", "") if candidate else "",
        "steps": steps,
        "next_action": next_action,
    }
    write_report(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
