#!/usr/bin/env python3
import json
from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
SUCCESS_GATE_JSON = ROOT / "outputs/latest/success-gate.json"
PLATFORM_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
BLOGGER_UPLOAD_JSON = ROOT / "outputs/latest/blogger-upload-report.json"
WORDPRESS_UPLOAD_JSON = ROOT / "outputs/latest/wordpress-upload-report.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
APPROVAL_DASHBOARD_JSON = ROOT / "outputs/latest/approval-dashboard.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-cloud-run-verification.json"
OUTPUT_MD = ROOT / "outputs/latest/first-cloud-run-verification.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare first-cloud-run verification checks for either safety-first or approved state modes."
    )
    parser.add_argument(
        "--allow-approved-state",
        action="store_true",
        help="Skip first-run safety review check and allow non-empty approval state (게시 후 검증용).",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    success_gate = load_json(SUCCESS_GATE_JSON)
    platform_plan = load_json(PLATFORM_PLAN_JSON)
    blogger = load_json(BLOGGER_UPLOAD_JSON)
    wordpress = load_json(WORDPRESS_UPLOAD_JSON)
    review_packet = load_json(REVIEW_PACKET_JSON)
    approval_dashboard = load_json(APPROVAL_DASHBOARD_JSON)
    review_approvals = load_json(REVIEW_APPROVALS_JSON)

    blogger_items = blogger.get("items", [])
    wordpress_items = wordpress.get("items", [])
    blogger_summary = blogger.get("summary", {})
    wordpress_summary = wordpress.get("summary", {})
    approval_keywords = review_approvals.get("user_confirmed_keywords", review_approvals.get("approved_keywords", []))
    approval_all = bool(review_approvals.get("user_confirmed_all", review_approvals.get("approved_all", False)))

    blogger_blocked = any(item.get("reason") == "awaiting_user_review_approval" for item in blogger_items)
    wordpress_blocked = any(item.get("reason") == "credentials_missing_dry_run" for item in wordpress_items) or any(
        item.get("reason") == "awaiting_user_review_approval" for item in wordpress_items
    )
    approval_state_matches_report = (
        blogger_summary.get("approved_all", False) == approval_all
        and blogger_summary.get("approved_keywords", []) == approval_keywords
    )
    safe_first_run_review_state = (not approval_all) and not approval_keywords

    checks = [
        {
            "name": "workflow_snapshot_generated",
            "ready": bool(review_packet),
            "success_condition": "review-packet.json 이 생성되어 있어야 함",
        },
        {
            "name": "approval_dashboard_generated",
            "ready": bool(approval_dashboard),
            "success_condition": "approval-dashboard.json 이 생성되어 있어야 함",
        },
        {
            "name": "platform_publish_plan_generated",
            "ready": bool(platform_plan),
            "success_condition": "platform-publish-plan.json 이 생성되어 있어야 함",
        },
        {
            "name": "review_approval_state_is_safe",
            "ready": safe_first_run_review_state,
            "success_condition": "첫 클라우드 런 전에는 review-approvals.json 의 사용자 최종 확인 목록이 비어 있어야 함",
        },
        {
            "name": "blogger_report_matches_current_approval_file",
            "ready": approval_state_matches_report,
            "success_condition": "blogger-upload-report summary 가 현재 사용자 최종 확인 상태와 일치해야 함",
        },
        {
            "name": "blogger_safely_blocked_without_approval",
            "ready": blogger_blocked and safe_first_run_review_state,
            "success_condition": "사용자 최종 확인 전에는 Blogger 업로드가 awaiting_user_review_approval 로 차단되어야 함",
        },
        {
            "name": "wordpress_not_accidentally_publishing",
            "ready": wordpress_blocked or not wordpress_items,
            "success_condition": "WordPress 미연결 상태에서는 credentials_missing_dry_run 이거나 업로드 시도가 없어야 함",
        },
        {
            "name": "repo_prereq_still_visible",
            "ready": success_gate.get("github_launch_status") in {"needs_repo_creation", "ready_for_actions_sync", "needs_gh_cli"},
            "success_condition": "성공 게이트에서 GitHub 연결 상태가 계속 드러나야 함",
        },
    ]

    return {
        "all_core_checks_passed": all(item.get("ready") for item in checks),
        "checks": checks,
        "quick_read": {
            "review_item_count": review_packet.get("review_item_count", len(review_packet.get("items", []))),
            "approval_dashboard_count": approval_dashboard.get("review_item_count", 0) or approval_dashboard.get("summary", {}).get(
                "review_item_count", 0
            ),
            "review_approval_state": {
                "user_confirmed_all": approval_all,
                "user_confirmed_keywords": approval_keywords,
            },
            "platform_channels": [
                {
                    "name": item.get("name"),
                    "ready": item.get("ready"),
                    "ready_item_count": item.get("ready_item_count", 0),
                }
                for item in platform_plan.get("channels", [])
            ],
            "blogger_summary": blogger_summary,
            "wordpress_summary": wordpress_summary,
        },
        "next_manual_checks": [
            "GitHub Actions 실행 로그에서 failed step 이 없는지 확인",
            "outputs/latest/review-packet.md 가 최신 스냅샷으로 커밋됐는지 확인",
            "Blogger 초안이 승인 전 업로드되지 않았는지 확인",
        ],
    }


def build_report_with_mode(args: argparse.Namespace) -> dict:
    report = build_report()
    if args.allow_approved_state:
        blog_items = report.get("checks", [])
        for item in blog_items:
            if item.get("name") == "review_approval_state_is_safe":
                item["ready"] = True
                item["success_condition"] = "게시 후 검증 모드에서는 승인 상태가 차단되지 않아도 허용합니다."
            if item.get("name") == "blogger_safely_blocked_without_approval":
                item["ready"] = True
                item["success_condition"] = "게시 후 검증 모드에서는 awaiting_user_review_approval가 없어도 허용합니다."
        report["checks"] = blog_items
        report["all_core_checks_passed"] = all(item.get("ready") for item in report.get("checks", []))
        report["mode"] = "approved_run"
    else:
        report["mode"] = "first_run_safety"
    return report


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# First Cloud Run Verification")
    lines.append("")
    lines.append(f"- all_core_checks_passed: `{report.get('all_core_checks_passed', False)}`")
    lines.append("")
    lines.append("## Core Checks")
    lines.append("")
    for item in report.get("checks", []):
        lines.append(f"- `{item.get('name')}`: {item.get('ready')}")
        lines.append(f"  - success_condition: {item.get('success_condition')}")
    lines.append("")
    lines.append("## Quick Read")
    lines.append("")
    quick = report.get("quick_read", {})
    lines.append(f"- review_item_count: `{quick.get('review_item_count', 0)}`")
    lines.append(f"- approval_dashboard_count: `{quick.get('approval_dashboard_count', 0)}`")
    lines.append(f"- review_approval_state: `{json.dumps(quick.get('review_approval_state', {}), ensure_ascii=False)}`")
    for channel in quick.get("platform_channels", []):
        lines.append(
            f"- channel `{channel.get('name')}`: ready={channel.get('ready')} / ready_item_count={channel.get('ready_item_count', 0)}"
        )
    lines.append(f"- blogger_summary: `{json.dumps(quick.get('blogger_summary', {}), ensure_ascii=False)}`")
    lines.append(f"- wordpress_summary: `{json.dumps(quick.get('wordpress_summary', {}), ensure_ascii=False)}`")
    lines.append("")
    lines.append("## Next Manual Checks")
    lines.append("")
    for step in report.get("next_manual_checks", []):
        lines.append(f"- {step}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    args = parse_args()
    report = build_report_with_mode(args)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
