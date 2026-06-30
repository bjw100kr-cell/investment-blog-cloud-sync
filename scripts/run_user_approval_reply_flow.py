#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLY_HELPER = ROOT / "scripts/apply_user_approval_reply.py"
OUTPUT_JSON = ROOT / "outputs/latest/user-approval-reply-flow.json"
OUTPUT_MD = ROOT / "outputs/latest/user-approval-reply-flow.md"
REPLY_PLAN_JSON = ROOT / "outputs/latest/user-approval-reply-plan.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or apply the flow from a short user approval reply to refreshed publish artifacts."
    )
    parser.add_argument("--reply", required=True, help='Natural-language reply like "fomc 글 먼저 진행"')
    parser.add_argument("--apply", action="store_true", help="Apply the approval reply before refreshing downstream artifacts.")
    return parser.parse_args()


def run_command(command: str) -> dict:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def preview_reply_plan(reply: str) -> dict:
    command = f'python3 {REPLY_HELPER} --reply {json.dumps(reply, ensure_ascii=False)}'
    result = run_command(command)
    plan = load_json(REPLY_PLAN_JSON)
    return {
        "command_result": result,
        "plan": plan,
    }


def verification_command_with_state(plan: dict) -> str:
    approved_keywords = plan.get("approved_keywords", [])
    review_approval_state = bool(approved_keywords)
    if review_approval_state:
        return "python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state"
    return "python3 scripts/prepare_first_cloud_run_verification.py"


def build_command_chain(reply: str, clear: bool, apply: bool) -> list[str]:
    preview_cmd = f'python3 {REPLY_HELPER} --reply {json.dumps(reply, ensure_ascii=False)}'
    apply_cmd = f'python3 {REPLY_HELPER} --reply {json.dumps(reply, ensure_ascii=False)} --apply'
    plan = load_json(REPLY_PLAN_JSON)
    chain = [preview_cmd]
    if apply and clear:
        chain.extend(
            [
                apply_cmd,
                "python3 scripts/build_platform_publish_plan.py",
                "python3 scripts/upload_blogger_drafts.py",
                verification_command_with_state(plan),
            ]
        )
    return chain


def build_report(args: argparse.Namespace) -> dict:
    preview = preview_reply_plan(args.reply)
    plan = preview.get("plan", {})
    clear = bool(plan.get("clear_enough_to_apply"))
    commands = build_command_chain(args.reply, clear, args.apply)
    apply_chain_preview = build_command_chain(args.reply, clear, True) if clear else []

    execution_results = []
    if args.apply and clear:
        for command in commands[1:]:
            result = run_command(command)
            execution_results.append(result)
            if result.get("returncode") != 0:
                break

    return {
        "reply": args.reply,
        "apply_mode": args.apply,
        "clear_enough_to_apply": clear,
        "approved_keywords": plan.get("approved_keywords", []),
        "held_keywords": plan.get("held_keywords", []),
        "ambiguous_keywords": plan.get("mentioned_but_ambiguous_keywords", []),
        "safety_note": "이 flow는 preview 에서는 멈추고, apply 일 때만 approval 반영 -> 게시 후보 재계산 -> Blogger draft 업로드 -> 검증 리포트 생성까지 이어집니다.",
        "command_chain": commands,
        "apply_chain_preview": apply_chain_preview,
        "preview_result": preview.get("command_result", {}),
        "execution_results": execution_results,
        "success": all(item.get("returncode") == 0 for item in execution_results) if execution_results else None,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# User Approval Reply Flow")
    lines.append("")
    lines.append("짧은 사용자 답변을 승인 반영과 게시 후보 재계산 흐름으로 잇는 preview/apply 결과입니다.")
    lines.append("")
    lines.append(f"- reply: `{report.get('reply', '')}`")
    lines.append(f"- apply_mode: `{report.get('apply_mode', False)}`")
    lines.append(f"- clear_enough_to_apply: `{report.get('clear_enough_to_apply', False)}`")
    lines.append(f"- approved_keywords: `{', '.join(report.get('approved_keywords', [])) or 'none'}`")
    lines.append(f"- held_keywords: `{', '.join(report.get('held_keywords', [])) or 'none'}`")
    lines.append(f"- ambiguous_keywords: `{', '.join(report.get('ambiguous_keywords', [])) or 'none'}`")
    lines.append(f"- safety_note: {report.get('safety_note', '')}")
    lines.append("")
    lines.append("## Command Chain")
    lines.append("")
    for command in report.get("command_chain", []):
        lines.append(f"- `{command}`")
    if not report.get("command_chain"):
        lines.append("- none")
    lines.append("")
    if report.get("apply_chain_preview"):
        lines.append("## Apply Chain Preview")
        lines.append("")
        for command in report.get("apply_chain_preview", []):
            lines.append(f"- `{command}`")
        lines.append("")
    lines.append("## Preview Result")
    lines.append("")
    preview_result = report.get("preview_result", {})
    lines.append(f"- returncode: `{preview_result.get('returncode', '')}`")
    if preview_result.get("stdout"):
        lines.append(f"- stdout: `{preview_result.get('stdout', '')}`")
    if preview_result.get("stderr"):
        lines.append(f"- stderr: `{preview_result.get('stderr', '')}`")
    lines.append("")
    if report.get("execution_results"):
        lines.append("## Execution Results")
        lines.append("")
        for result in report.get("execution_results", []):
            state = "ok" if result.get("returncode") == 0 else "failed"
            lines.append(f"- `{state}` `{result.get('command', '')}`")
            if result.get("stdout"):
                lines.append(f"  - stdout: {result.get('stdout', '')}")
            if result.get("stderr"):
                lines.append(f"  - stderr: {result.get('stderr', '')}")
        lines.append("")
        lines.append(f"- success: `{report.get('success')}`")
    else:
        lines.append("## How To Use")
        lines.append("")
        lines.append(f"- preview: `python3 scripts/run_user_approval_reply_flow.py --reply {json.dumps(report.get('reply', ''), ensure_ascii=False)}`")
        lines.append(f"- apply: `python3 scripts/run_user_approval_reply_flow.py --reply {json.dumps(report.get('reply', ''), ensure_ascii=False)} --apply`")
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
