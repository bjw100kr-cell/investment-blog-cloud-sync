#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-blogger-verify-flow.json"
OUTPUT_MD = ROOT / "outputs/latest/first-blogger-verify-flow.md"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or apply the shortest local first Blogger verification flow after user confirmation."
    )
    parser.add_argument("--skip-approval", action="store_true", help="Skip applying the current recommended single approval.")
    parser.add_argument("--apply", action="store_true", help="Actually execute the flow. Without this, only preview the chain.")
    parser.add_argument(
        "--run-safety-check",
        action="store_true",
        help="Run first-cloud-run safety verification after upload. 기본은 off 입니다.",
    )
    parser.add_argument("--notes", default="", help="Optional note to store in review-approvals.json when applying approval.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def run_command(command: list[str]) -> dict:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def build_verification_command(include_approved_state: bool) -> list[str]:
    command = ["python3", "scripts/prepare_first_cloud_run_verification.py"]
    if include_approved_state:
        command.append("--allow-approved-state")
    return command


def build_command_chain(args: argparse.Namespace) -> list[list[str]]:
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    review_approvals = load_json(REVIEW_APPROVALS_JSON)
    approved_keywords = review_approvals.get("user_confirmed_keywords", review_approvals.get("approved_keywords", []))
    approval_all = bool(review_approvals.get("user_confirmed_all", review_approvals.get("approved_all", False)))
    include_verified_state = approval_all or bool(approved_keywords)
    approval_command = (first_approval.get("recommended_single") or {}).get("approval_command", "")
    commands: list[list[str]] = []
    if approval_command and not args.skip_approval and not approval_all:
        parsed = approval_command.split()
        if args.notes:
            parsed.extend(["--notes", args.notes])
        commands.append(parsed)
    commands.extend(
        [
            ["python3", "scripts/build_platform_publish_plan.py"],
            ["python3", "scripts/upload_blogger_drafts.py"],
        ]
    )
    if args.run_safety_check:
        commands.append(build_verification_command(include_verified_state))
    return commands


def build_report(args: argparse.Namespace) -> dict:
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    single = first_approval.get("recommended_single", {})
    commands = build_command_chain(args)
    results = []
    if args.apply:
        for command in commands:
            result = run_command(command)
            results.append(result)
            if result.get("returncode") != 0:
                break
    return {
        "headline": "사용자 확인 뒤 로컬 Blogger draft 검증까지 바로 이어지는 최소 실행 흐름입니다.",
        "apply_mode": args.apply,
        "main_candidate": {
            "keyword": single.get("keyword", ""),
            "title": single.get("title", ""),
        },
        "commands": [" ".join(command) for command in commands],
        "execution_results": results,
        "success": all(item.get("returncode") == 0 for item in results) if results else None,
        "how_to_use": {
            "preview": "python3 scripts/run_first_blogger_verify_flow.py",
            "apply": "python3 scripts/run_first_blogger_verify_flow.py --apply",
            "apply_skip_approval": "python3 scripts/run_first_blogger_verify_flow.py --apply --skip-approval",
            "apply_with_safety_check": "python3 scripts/run_first_blogger_verify_flow.py --apply --run-safety-check",
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# First Blogger Verify Flow")
    lines.append("")
    lines.append(report.get("headline", ""))
    lines.append("")
    lines.append(f"- apply_mode: `{report.get('apply_mode', False)}`")
    candidate = report.get("main_candidate", {})
    lines.append(f"- main_candidate: `{candidate.get('keyword', '')}` / {candidate.get('title', '')}")
    lines.append("")
    lines.append("## Command Chain")
    lines.append("")
    for command in report.get("commands", []):
        lines.append(f"- `{command}`")
    if not report.get("commands"):
        lines.append("- 현재 실행 명령이 없습니다.")
    lines.append("")
    if report.get("execution_results"):
        lines.append("## Execution Results")
        lines.append("")
        for result in report.get("execution_results", []):
            status = "ok" if result.get("returncode") == 0 else "failed"
            lines.append(f"- `{status}` `{result.get('command', '')}`")
            if result.get("stdout"):
                lines.append(f"  - stdout: {result.get('stdout', '')}")
            if result.get("stderr"):
                lines.append(f"  - stderr: {result.get('stderr', '')}")
        lines.append(f"- success: `{report.get('success')}`")
        lines.append("")
    lines.append("## How To Use")
    lines.append("")
    how = report.get("how_to_use", {})
    lines.append(f"- preview: `{how.get('preview', '')}`")
    lines.append(f"- apply: `{how.get('apply', '')}`")
    lines.append(f"- apply_skip_approval: `{how.get('apply_skip_approval', '')}`")
    lines.append(f"- apply_with_safety_check: `{how.get('apply_with_safety_check', '')}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    args = parse_args()
    report = build_report(args)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
