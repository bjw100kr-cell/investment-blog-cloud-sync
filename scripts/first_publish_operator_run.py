#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-publish-operator-run.json"
OUTPUT_MD = ROOT / "outputs/latest/first-publish-operator-run.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or execute the first user confirmation -> Blogger upload -> verification operator flow."
    )
    parser.add_argument("--preview", action="store_true", help="Preview only. same as running without flags.")
    parser.add_argument("--apply", action="store_true", help="Actually run the confirmation and upload commands.")
    parser.add_argument(
        "--approval",
        choices=["auto_single", "auto_batch", "all"],
        default="auto_single",
        help="Which confirmation scope to use. auto_single uses the top recommended single keyword.",
    )
    parser.add_argument("--keywords", nargs="*", default=[], help="Override and confirm exactly these keywords.")
    parser.add_argument("--notes", default="", help="Optional note stored in review-approvals.json when applying.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def choose_keywords(args: argparse.Namespace, first_approval: dict) -> tuple[list[str], str]:
    if args.keywords:
        return [item for item in args.keywords if item], "manual_keywords"

    if args.approval == "all":
        return [], "all"

    if args.approval == "auto_batch":
        batch = (first_approval.get("recommended_batch") or {}).get("keywords", [])
        return [item for item in batch if item], "auto_batch"

    single = (first_approval.get("recommended_single") or {}).get("keyword", "")
    return ([single] if single else []), "auto_single"


def build_approval_command(mode: str, keywords: list[str], notes: str) -> list[str]:
    command = ["python3", "scripts/set_review_approvals.py"]
    if mode == "all":
        command.append("--all")
    else:
        command.append("--keywords")
        command.extend(keywords)
    if notes:
        command.extend(["--notes", notes])
    return command


def build_verification_command(approval_state: bool) -> list[str]:
    command = ["python3", "scripts/prepare_first_cloud_run_verification.py"]
    if approval_state:
        command.append("--allow-approved-state")
    return command


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


def build_report(args: argparse.Namespace) -> dict:
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    current_approvals = load_json(REVIEW_APPROVALS_JSON)
    keywords, mode = choose_keywords(args, first_approval)
    approval_command = build_approval_command(mode, keywords, args.notes)
    approval_state = bool(current_approvals.get("user_confirmed_all", current_approvals.get("approved_all", False)))
    approval_state = approval_state or bool(current_approvals.get("user_confirmed_keywords", current_approvals.get("approved_keywords", [])))
    needs_approved_state = approval_state or bool(keywords) or mode == "all"
    flow_commands = [
        approval_command,
        ["python3", "scripts/build_platform_publish_plan.py"],
        ["python3", "scripts/upload_blogger_drafts.py"],
        build_verification_command(needs_approved_state),
    ]

    results = []
    if args.apply:
        for command in flow_commands:
            results.append(run_command(command))

    return {
        "apply_mode": args.apply,
        "approval_mode": mode,
        "current_user_confirmed_all": bool(
            current_approvals.get("user_confirmed_all", current_approvals.get("approved_all", False))
        ),
        "current_user_confirmed_keywords": current_approvals.get(
            "user_confirmed_keywords", current_approvals.get("approved_keywords", [])
        ),
        "target_user_confirmed_keywords": keywords,
        "approved_keywords": keywords,
        "notes": args.notes,
        "planned_commands": [" ".join(command) for command in flow_commands],
        "results": results,
        "success": all(result.get("returncode") == 0 for result in results) if results else None,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# First Publish Operator Run")
    lines.append("")
    lines.append("사용자 최종 확인부터 Blogger 업로드 검증까지 이어지는 운영 실행 카드입니다.")
    lines.append("사용자 확인 전에는 실제 업로드를 실행하면 안 됩니다.")
    lines.append("")
    lines.append(f"- apply_mode: `{report.get('apply_mode', False)}`")
    lines.append(f"- approval_mode: `{report.get('approval_mode', '')}`")
    lines.append(
        f"- current_user_confirmed_keywords: `{json.dumps(report.get('current_user_confirmed_keywords', []), ensure_ascii=False)}`"
    )
    lines.append(
        f"- target_user_confirmed_keywords: `{json.dumps(report.get('target_user_confirmed_keywords', []), ensure_ascii=False)}`"
    )
    if report.get("notes"):
        lines.append(f"- notes: `{report.get('notes', '')}`")
    lines.append("")
    lines.append("## Planned Commands")
    lines.append("")
    for command in report.get("planned_commands", []):
        lines.append(f"- `{command}`")
    lines.append("")
    if report.get("results"):
        lines.append("## Execution Results")
        lines.append("")
        for result in report.get("results", []):
            state = "ok" if result.get("returncode") == 0 else "failed"
            lines.append(f"- `{state}` `{result.get('command', '')}`")
            if result.get("stdout"):
                lines.append(f"  - stdout: {result.get('stdout', '')}")
            if result.get("stderr"):
                lines.append(f"  - stderr: {result.get('stderr', '')}")
        lines.append("")
        lines.append(f"- success: `{report.get('success')}`")
        lines.append("")
    else:
        lines.append("## How To Execute")
        lines.append("")
        lines.append("- preview only: `python3 scripts/first_publish_operator_run.py`")
        lines.append("- apply single recommendation: `python3 scripts/first_publish_operator_run.py --apply`")
        lines.append("- apply batch recommendation: `python3 scripts/first_publish_operator_run.py --apply --approval auto_batch`")
        lines.append("- apply manual keywords: `python3 scripts/first_publish_operator_run.py --apply --keywords bitcoin`")
        lines.append("- shortest helper: `python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO --apply`")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    args = parse_args()
    if args.preview and args.apply:
        raise SystemExit("Cannot use --preview and --apply together.")
    report = build_report(args)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
