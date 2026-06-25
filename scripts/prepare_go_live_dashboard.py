#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
LOGIN_CHECKLIST_JSON = ROOT / "outputs/latest/login-launch-checklist.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
OAUTH_TOKEN_JSON = ROOT / "outputs/latest/google-oauth-token-result.json"
OAUTH_CLIENT_DISCOVERY_JSON = ROOT / "outputs/latest/google-oauth-client-discovery.json"
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
FIRST_LIVE_RUN_PLAN_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
OUTPUT_MD = ROOT / "outputs/latest/go-live-dashboard.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def discover_client_json_path() -> str:
    payload = load_json(OAUTH_CLIENT_DISCOVERY_JSON)
    candidates = payload.get("candidates", [])
    if not candidates:
        return ""
    return candidates[0].get("path", "")


def build_next_commands(setup: dict, go_live: dict) -> list[str]:
    commands = []
    git_origin = (setup.get("git") or {}).get("origin", "")
    has_commit = bool((setup.get("git") or {}).get("has_commit", False))
    env_filled = set(setup.get("env_keys_filled", []))
    discovered_client_json = discover_client_json_path()

    if "GOOGLE_CLIENT_ID" not in env_filled or "GOOGLE_CLIENT_SECRET" not in env_filled:
        commands.append("python3 scripts/open_login_setup_pages.py --open")
        commands.append("python3 scripts/bootstrap_google_oauth_credentials.py")
        if discovered_client_json:
            commands.append(f"python3 scripts/import_google_oauth_client.py {discovered_client_json}")
    if "GOOGLE_CLIENT_ID" in env_filled and "GOOGLE_CLIENT_SECRET" in env_filled and "GOOGLE_REFRESH_TOKEN" not in env_filled:
        if OAUTH_TOKEN_JSON.exists():
            commands.append("python3 scripts/bootstrap_google_oauth_credentials.py --apply-token-if-present")
        else:
            commands.append("GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py")
    if not has_commit:
        commands.append("bash scripts/prepare_initial_commit.sh")
    if has_commit and git_origin in {"", "(not configured)"}:
        commands.append("bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>")
    elif has_commit and any(key in env_filled for key in ["BLOGGER_BLOG_ID", "OPENAI_API_KEY", "GOOGLE_REFRESH_TOKEN"]):
        commands.append("python3 scripts/export_github_actions_sync_commands.py")
    if go_live.get("live_prerequisites", {}).get("blogger_connection_ready"):
        commands.append("bash scripts/run_pipeline.sh")
    return commands


def build_dashboard() -> dict:
    setup = load_json(SETUP_JSON)
    go_live = load_json(GO_LIVE_JSON)
    monetization = load_json(MONETIZATION_JSON)
    login = load_json(LOGIN_CHECKLIST_JSON)
    publish_queue = load_json(PUBLISH_QUEUE_JSON)
    publish_inventory = load_json(PUBLISH_INVENTORY_JSON)
    client_discovery = load_json(OAUTH_CLIENT_DISCOVERY_JSON)
    seo_backlog = load_json(SEO_BACKLOG_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    first_live_run_plan = load_json(FIRST_LIVE_RUN_PLAN_JSON)
    github_launch_plan = load_json(GITHUB_LAUNCH_PLAN_JSON)

    next_commands = build_next_commands(setup, go_live)
    queue_items = publish_queue.get("items", [])
    seo_items = seo_backlog.get("items", [])

    return {
        "ready_for_first_live_run": go_live.get("ready_for_first_live_run", False),
        "monetization_score": monetization.get("readiness_score", 0),
        "repo_connected": bool((setup.get("git") or {}).get("origin") not in {"", "(not configured)"}),
        "credentials_missing": go_live.get("required_credentials", []),
        "growth_keys_missing": go_live.get("optional_growth_keys", []),
        "top_post_keywords": go_live.get("posts", {}).get("top_keywords", []),
        "top_page_sequence": go_live.get("site_pages", {}).get("top_sequence", []),
        "login_pages_count": len(login.get("pages", [])),
        "oauth_client_candidate_count": len(client_discovery.get("candidates", [])),
        "publish_queue_ready_count": publish_queue.get("summary", {}).get("ready_count", 0),
        "publish_inventory_ready_count": publish_inventory.get("summary", {}).get("ready_count", 0),
        "next_commands": next_commands,
        "first_live_run_status": first_live_run_plan.get("status", ""),
        "github_launch_status": github_launch_plan.get("status", ""),
        "first_queue_actions": [
            {
                "keyword": item.get("keyword"),
                "title": item.get("title"),
                "cta_target": item.get("cta_focus"),
            }
            for item in queue_items[:3]
        ],
        "top_follow_up_targets": [
            {
                "title": item.get("title"),
                "source_keyword": item.get("source_keyword"),
                "priority_score": item.get("priority_score"),
            }
            for item in seo_items[:3]
        ],
        "daily_keyword_opportunities": [
            {
                "keyword": item.get("keyword"),
                "title": item.get("suggested_title"),
                "urgency": item.get("urgency"),
            }
            for item in keyword_board.get("breaking_candidates", [])[:3]
        ],
    }


def write_markdown(dashboard: dict) -> None:
    lines = []
    lines.append("# Go Live Dashboard")
    lines.append("")
    lines.append(f"- ready_for_first_live_run: `{dashboard['ready_for_first_live_run']}`")
    lines.append(f"- monetization_score: `{dashboard['monetization_score']}`")
    lines.append(f"- repo_connected: `{dashboard['repo_connected']}`")
    lines.append(f"- login_pages_count: `{dashboard['login_pages_count']}`")
    lines.append(f"- oauth_client_candidate_count: `{dashboard['oauth_client_candidate_count']}`")
    lines.append(f"- publish_queue_ready_count: `{dashboard['publish_queue_ready_count']}`")
    lines.append(f"- publish_inventory_ready_count: `{dashboard['publish_inventory_ready_count']}`")
    if dashboard.get("first_live_run_status"):
        lines.append(f"- first_live_run_status: `{dashboard['first_live_run_status']}`")
    if dashboard.get("github_launch_status"):
        lines.append(f"- github_launch_status: `{dashboard['github_launch_status']}`")
    lines.append("")
    lines.append("## Missing Before First Live Run")
    lines.append("")
    if dashboard["credentials_missing"]:
        for key in dashboard["credentials_missing"]:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 필수 자격값은 모두 채워졌습니다.")
    lines.append("")
    lines.append("## Growth Gaps")
    lines.append("")
    if dashboard["growth_keys_missing"]:
        for key in dashboard["growth_keys_missing"]:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 성장용 보조 키도 모두 채워졌습니다.")
    lines.append("")
    lines.append("## First Content Targets")
    lines.append("")
    for keyword in dashboard["top_post_keywords"]:
        lines.append(f"- `{keyword}`")
    lines.append("")
    lines.append("## Daily Opportunity Board")
    lines.append("")
    for item in dashboard.get("daily_keyword_opportunities", []):
        lines.append(f"- `{item.get('keyword')}`: {item.get('title')} / urgency {item.get('urgency')}")
    if not dashboard.get("daily_keyword_opportunities"):
        lines.append("- 아직 생성된 키워드 기회판이 없습니다.")
    lines.append("")
    lines.append("## First Page Targets")
    lines.append("")
    for slug in dashboard["top_page_sequence"]:
        lines.append(f"- `{slug}`")
    lines.append("")
    lines.append("## Next Commands")
    lines.append("")
    if dashboard["next_commands"]:
        for command in dashboard["next_commands"]:
            lines.append(f"- `{command}`")
    else:
        lines.append("- 바로 `bash scripts/run_pipeline.sh` 를 다시 실행할 수 있습니다.")
    lines.append("- `python3 scripts/resume_after_login.py`")
    lines.append("- `python3 scripts/prepare_first_live_run_plan.py`")
    lines.append("- `python3 scripts/prepare_github_launch_plan.py`")
    lines.append("")
    lines.append("## First Queue Actions")
    lines.append("")
    for item in dashboard["first_queue_actions"]:
        lines.append(f"- `{item.get('keyword')}`: {item.get('title')} / CTA {item.get('cta_target')}")
    lines.append("")
    lines.append("## Next SEO Follow-ups")
    lines.append("")
    for item in dashboard["top_follow_up_targets"]:
        lines.append(f"- `{item.get('source_keyword')}` -> {item.get('title')} / score {item.get('priority_score')}")
    if not dashboard["top_follow_up_targets"]:
        lines.append("- 아직 생성된 후속 글 백로그가 없습니다.")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    dashboard = build_dashboard()
    OUTPUT_JSON.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2))
    write_markdown(dashboard)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
