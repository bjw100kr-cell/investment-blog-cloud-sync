#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
SUCCESS_GATE_JSON = ROOT / "outputs/latest/success-gate.json"
GITHUB_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
PLATFORM_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
BLOGGER_UPLOAD_JSON = ROOT / "outputs/latest/blogger-upload-report.json"
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
DAILY_REVENUE_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
EDITORIAL_CALENDAR_JSON = ROOT / "outputs/latest/editorial-calendar.json"
OUTPUT_JSON = ROOT / "outputs/latest/automation-progress-board.json"
OUTPUT_MD = ROOT / "outputs/latest/automation-progress-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict[str, dict]:
    return {item.get("name", ""): item for item in setup.get("integrations", []) if item.get("name")}


def stage(name: str, status: str, summary: str, proof: list[str], next_action: str = "", owner: str = "agent") -> dict:
    return {
        "name": name,
        "status": status,
        "summary": summary,
        "proof": proof,
        "next_action": next_action,
        "owner": owner,
    }


def build_report() -> dict:
    go_live = load_json(GO_LIVE_JSON)
    success_gate = load_json(SUCCESS_GATE_JSON)
    github = load_json(GITHUB_PLAN_JSON)
    platform = load_json(PLATFORM_PLAN_JSON)
    blogger = load_json(BLOGGER_UPLOAD_JSON)
    setup = load_json(SETUP_JSON)
    approvals = load_json(REVIEW_APPROVALS_JSON)
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    revenue = load_json(DAILY_REVENUE_JSON)
    editorial = load_json(EDITORIAL_CALENDAR_JSON)

    integrations = integration_lookup(setup)
    user_keywords = approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", []))
    recommended_single = (first_approval.get("recommended_single") or {}).get("keyword", "")
    today_path = revenue.get("today_path", [])
    editorial_coverage = editorial.get("coverage_summary", [])

    blogger_items = blogger.get("items", [])
    blogger_blockers = [item for item in blogger_items if item.get("reason")]
    openai_ready = bool(integrations.get("openai_drafts", {}).get("ready", False))
    search_console_ready = bool(integrations.get("search_console", {}).get("ready", False))
    repo_connected = bool(github.get("repo_connected", False))
    blogger_ready = bool(integrations.get("blogger_upload", {}).get("ready", False))
    first_live_ready = bool(go_live.get("ready_for_first_live_run", False))
    wordpress_ready = bool(integrations.get("wordpress_upload", {}).get("ready", False))

    stages = [
        stage(
            "content_engine",
            "complete" if editorial_coverage and today_path else "in_progress",
            "주제 선정, 레인 균형, 수익화 경로, 검토 패킷 생성 루프가 로컬에서 돌아갑니다.",
            [
                f"editorial coverage entries `{len(editorial_coverage)}`",
                f"today path entries `{len(today_path)}`",
                f"recommended single `{recommended_single or 'none'}`",
            ],
            next_action="필요 시 source 수집과 점수 로직을 계속 보강",
            owner="agent",
        ),
        stage(
            "blogger_draft_loop",
            "in_progress" if blogger_ready and not user_keywords else "complete" if blogger_ready and user_keywords else "blocked",
            "Blogger 자동 채널은 준비됐지만, 실제 draft 업로드는 사용자 최종 확인 keyword가 있어야 진행됩니다.",
            [
                f"blogger_ready `{blogger_ready}`",
                f"user_confirmed_keywords `{user_keywords}`",
                f"success_gate `{success_gate.get('first_live_status', '')}`",
            ],
            next_action=f"`{(first_approval.get('recommended_single') or {}).get('approval_command', '')}`" if blogger_ready and not user_keywords else "",
            owner="user" if blogger_ready and not user_keywords else "agent",
        ),
        stage(
            "free_cloud_automation",
            "blocked" if not repo_connected else "in_progress",
            "컴퓨터가 꺼져도 도는 무료 자동화는 repo 연결이 끝났고, 이제 Actions Secrets와 첫 수동 실행 검증만 남았습니다."
            if repo_connected
            else "컴퓨터가 꺼져도 도는 무료 자동화는 GitHub repo 연결 전까지 막혀 있습니다.",
            [
                f"repo_connected `{repo_connected}`",
                f"github_status `{github.get('status', '')}`",
                f"sync_ready_keys `{len(github.get('sync_ready_keys', []))}`",
            ],
            next_action="`bash scripts/bootstrap_github_remote.sh <OWNER/REPO>`" if not repo_connected else "GitHub Actions 첫 수동 실행 검증",
            owner="user" if not repo_connected else "agent",
        ),
        stage(
            "measurement_and_growth",
            "in_progress",
            "Search Console, GA4, AdSense 같은 성장/수익 측정 스택은 일부만 준비돼 있고 현재는 fallback 로직으로 운영 중입니다.",
            [
                f"search_console_ready `{search_console_ready}`",
                f"openai_ready `{openai_ready}`",
                f"monetization_score `{go_live.get('monetization_score', 0)}`",
            ],
            next_action="Search Console site URL, GA4, AdSense 연결을 순차적으로 보강",
            owner="agent",
        ),
        stage(
            "wordpress_expansion",
            "blocked" if not wordpress_ready else "in_progress",
            "WordPress는 2차 확장 채널이며 현재 필수 자격값이 없어 막혀 있습니다.",
            [
                f"wordpress_ready `{wordpress_ready}`",
                f"missing `{', '.join(integrations.get('wordpress_upload', {}).get('missing', []))}`",
            ],
            next_action="WordPress는 Blogger 루프 검증 후 연결",
            owner="user" if not wordpress_ready else "agent",
        ),
    ]

    status_counts = {
        "complete": sum(1 for item in stages if item["status"] == "complete"),
        "in_progress": sum(1 for item in stages if item["status"] == "in_progress"),
        "blocked": sum(1 for item in stages if item["status"] == "blocked"),
    }

    user_needed = [item for item in stages if item.get("owner") == "user" and item.get("next_action")]
    agent_next = [item for item in stages if item.get("owner") == "agent" and item.get("next_action")]

    return {
        "summary": {
            "first_live_ready": first_live_ready,
            "repo_connected": repo_connected,
            "status_counts": status_counts,
            "current_main_candidate": recommended_single,
        },
        "stages": stages,
        "user_needed_actions": user_needed,
        "agent_next_actions": agent_next,
        "references": {
            "first_approval_path_md": str(ROOT / "outputs/latest/first-approval-path.md"),
            "daily_revenue_focus_md": str(ROOT / "outputs/latest/daily-revenue-focus.md"),
            "editorial_calendar_md": str(ROOT / "outputs/latest/editorial-calendar.md"),
            "github_launch_plan_md": str(ROOT / "outputs/latest/github-launch-plan.md"),
        },
        "operator_notes": [
            "현재 사용자 최종 확인 전 실제 업로드는 계속 차단됩니다.",
            "bitcoin이 direct publish 기준 1순위이고, stale fomc는 direct path에서 제외된 상태입니다.",
            f"blogger blockers observed `{len(blogger_blockers)}`",
        ],
    }


def write_markdown(report: dict) -> None:
    summary = report.get("summary", {})
    lines = []
    lines.append("# Automation Progress Board")
    lines.append("")
    lines.append("투자/경제 블로그 자동화 목표 기준으로 지금 어디까지 왔는지 한 장으로 보는 진행 보드입니다.")
    lines.append("")
    lines.append(f"- first_live_ready: `{summary.get('first_live_ready', False)}`")
    lines.append(f"- repo_connected: `{summary.get('repo_connected', False)}`")
    lines.append(f"- current_main_candidate: `{summary.get('current_main_candidate', '')}`")
    counts = summary.get("status_counts", {})
    lines.append(f"- status_counts: complete `{counts.get('complete', 0)}` / in_progress `{counts.get('in_progress', 0)}` / blocked `{counts.get('blocked', 0)}`")
    lines.append("")
    lines.append("## Stage Status")
    lines.append("")
    for item in report.get("stages", []):
        lines.append(f"- `{item.get('name', '')}` / status `{item.get('status', '')}` / owner `{item.get('owner', '')}`")
        lines.append(f"  - summary: {item.get('summary', '')}")
        for proof in item.get("proof", []):
            lines.append(f"  - proof: {proof}")
        if item.get("next_action"):
            lines.append(f"  - next_action: {item.get('next_action', '')}")
    lines.append("")
    lines.append("## User Needed Actions")
    lines.append("")
    for item in report.get("user_needed_actions", []):
        lines.append(f"- `{item.get('name', '')}` -> {item.get('next_action', '')}")
    if not report.get("user_needed_actions"):
        lines.append("- none")
    lines.append("")
    lines.append("## Agent Next Actions")
    lines.append("")
    for item in report.get("agent_next_actions", []):
        lines.append(f"- `{item.get('name', '')}` -> {item.get('next_action', '')}")
    if not report.get("agent_next_actions"):
        lines.append("- none")
    lines.append("")
    lines.append("## References")
    lines.append("")
    refs = report.get("references", {})
    for key, value in refs.items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Operator Notes")
    lines.append("")
    for note in report.get("operator_notes", []):
        lines.append(f"- {note}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
