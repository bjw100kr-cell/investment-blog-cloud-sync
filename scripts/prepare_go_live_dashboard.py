#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
MONETIZATION_ROADMAP_JSON = ROOT / "outputs/latest/monetization-roadmap.json"
LOGIN_CHECKLIST_JSON = ROOT / "outputs/latest/login-launch-checklist.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
OAUTH_TOKEN_JSON = ROOT / "outputs/latest/google-oauth-token-result.json"
OAUTH_CLIENT_DISCOVERY_JSON = ROOT / "outputs/latest/google-oauth-client-discovery.json"
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
FIRST_LIVE_RUN_PLAN_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
AUTOMATION_SCOPE_JSON = ROOT / "outputs/latest/automation-scope.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
FIRST_PUBLISH_OPERATOR_RUN_JSON = ROOT / "outputs/latest/first-publish-operator-run.json"
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
TODAY_OPERATOR_CONSOLE_JSON = ROOT / "outputs/latest/today-operator-console.json"
OUTPUT_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
OUTPUT_MD = ROOT / "outputs/latest/go-live-dashboard.md"
GITHUB_MINIMUM_LAUNCH_CARD_MD = ROOT / "outputs/latest/github-minimum-launch-card.md"
PIPELINE_WORKFLOW_PARITY_MD = ROOT / "outputs/latest/pipeline-workflow-parity.md"
USER_REVIEW_CHECKPOINT_HTML = ROOT / "outputs/latest/user-review-checkpoint.html"
CLOUD_LAUNCH_PREFLIGHT_MD = ROOT / "outputs/latest/cloud-launch-preflight.md"


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
        commands.append("python3 scripts/open_login_setup_pages.py --open-next")
        commands.append("python3 scripts/bootstrap_google_oauth_credentials.py")
        if discovered_client_json:
            commands.append(f"python3 scripts/import_google_oauth_client.py {discovered_client_json}")
    if "GOOGLE_CLIENT_ID" in env_filled and "GOOGLE_CLIENT_SECRET" in env_filled and "GOOGLE_REFRESH_TOKEN" not in env_filled:
        if OAUTH_TOKEN_JSON.exists():
            commands.append("python3 scripts/bootstrap_google_oauth_credentials.py --apply-token-if-present")
        else:
            commands.append("GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py")
    blogger_ready = go_live.get("live_prerequisites", {}).get("blogger_connection_ready", False)
    wordpress_ready = go_live.get("live_prerequisites", {}).get("wordpress_connection_ready", False)
    if not blogger_ready and not wordpress_ready:
        commands.append("python3 scripts/open_login_setup_pages.py --open-next")
    if not has_commit:
        commands.append("bash scripts/prepare_initial_commit.sh")
    if has_commit and git_origin in {"", "(not configured)"}:
        commands.append("bash scripts/bootstrap_github_remote.sh <OWNER/REPO>")
    elif has_commit and any(key in env_filled for key in ["BLOGGER_BLOG_ID", "OPENAI_API_KEY", "GOOGLE_REFRESH_TOKEN"]):
        commands.append("python3 scripts/export_github_actions_sync_commands.py")
    if go_live.get("live_prerequisites", {}).get("at_least_one_auto_channel_ready"):
        commands.append("bash scripts/run_pipeline.sh")
    return commands


def build_dashboard() -> dict:
    setup = load_json(SETUP_JSON)
    go_live = load_json(GO_LIVE_JSON)
    monetization = load_json(MONETIZATION_JSON)
    monetization_roadmap = load_json(MONETIZATION_ROADMAP_JSON)
    login = load_json(LOGIN_CHECKLIST_JSON)
    publish_queue = load_json(PUBLISH_QUEUE_JSON)
    publish_inventory = load_json(PUBLISH_INVENTORY_JSON)
    client_discovery = load_json(OAUTH_CLIENT_DISCOVERY_JSON)
    seo_backlog = load_json(SEO_BACKLOG_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    first_live_run_plan = load_json(FIRST_LIVE_RUN_PLAN_JSON)
    github_launch_plan = load_json(GITHUB_LAUNCH_PLAN_JSON)
    platform_publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    automation_scope = load_json(AUTOMATION_SCOPE_JSON)
    first_approval_path = load_json(FIRST_APPROVAL_PATH_JSON)
    daily_revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)
    first_publish_operator_run = load_json(FIRST_PUBLISH_OPERATOR_RUN_JSON)
    user_review_shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    today_operator_console = load_json(TODAY_OPERATOR_CONSOLE_JSON)
    github_connected = bool(github_launch_plan.get("repo_connected", False))

    next_commands = build_next_commands(setup, go_live)
    queue_items = publish_queue.get("items", [])
    seo_items = seo_backlog.get("items", [])

    return {
        "ready_for_first_live_run": go_live.get("ready_for_first_live_run", False),
        "monetization_score": monetization.get("readiness_score", 0),
        "repo_connected": github_connected,
        "credentials_missing": go_live.get("required_credentials", []),
        "growth_keys_missing": go_live.get("optional_growth_keys", []),
        "top_post_keywords": go_live.get("posts", {}).get("top_keywords", []),
        "top_page_sequence": go_live.get("site_pages", {}).get("top_sequence", []),
        "login_pages_count": len(login.get("pages", [])),
        "oauth_client_candidate_count": len(client_discovery.get("candidates", [])),
        "publish_queue_ready_count": publish_queue.get("summary", {}).get("ready_count", 0),
        "publish_inventory_ready_count": publish_inventory.get("summary", {}).get("ready_count", 0),
        "auto_channel_ready_count": go_live.get("automated_channels", {}).get("ready_count", 0),
        "automation_policy": automation_scope.get("automation_policy", "automation-first"),
        "active_channel_now": automation_scope.get("primary_channel", {}).get("name", "blogger"),
        "expand_channel_later": automation_scope.get("secondary_channel", {}).get("name", "wordpress"),
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
        "platform_channels": platform_publish_plan.get("channels", []),
        "first_approval_path": first_approval_path,
        "daily_revenue_focus": daily_revenue_focus,
        "monetization_roadmap": monetization_roadmap,
        "first_publish_operator_run": first_publish_operator_run,
        "user_review_shortlist": user_review_shortlist,
        "today_operator_console": today_operator_console,
        "github_minimum_launch_card_md": str(GITHUB_MINIMUM_LAUNCH_CARD_MD),
        "pipeline_workflow_parity_md": str(PIPELINE_WORKFLOW_PARITY_MD),
        "user_review_checkpoint_html": str(USER_REVIEW_CHECKPOINT_HTML),
        "cloud_launch_preflight_md": str(CLOUD_LAUNCH_PREFLIGHT_MD),
        "minimum_cloud_blocker_summary": {
            "repo_connected": github_connected,
            "required_secrets_count": 4,
            "required_variables_count": 7,
            "wordpress_required_now": False,
            "openai_required_now": False,
        },
        "pipeline_workflow_parity": load_json(OUTPUT_JSON.parent / "pipeline-workflow-parity.json"),
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
    lines.append(f"- auto_channel_ready_count: `{dashboard['auto_channel_ready_count']}`")
    lines.append(f"- automation_policy: `{dashboard['automation_policy']}`")
    lines.append(f"- active_channel_now: `{dashboard['active_channel_now']}`")
    lines.append(f"- expand_channel_later: `{dashboard['expand_channel_later']}`")
    if dashboard.get("first_live_run_status"):
        lines.append(f"- first_live_run_status: `{dashboard['first_live_run_status']}`")
    if dashboard.get("github_launch_status"):
        lines.append(f"- github_launch_status: `{dashboard['github_launch_status']}`")
    lines.append("")
    lines.append("## Minimum Cloud Blocker")
    lines.append("")
    minimum = dashboard.get("minimum_cloud_blocker_summary", {})
    lines.append(f"- repo_connected: `{minimum.get('repo_connected', False)}`")
    lines.append(f"- required_secrets_count: `{minimum.get('required_secrets_count', 0)}`")
    lines.append(f"- required_variables_count: `{minimum.get('required_variables_count', 0)}`")
    lines.append(f"- wordpress_required_now: `{minimum.get('wordpress_required_now', False)}`")
    lines.append(f"- openai_required_now: `{minimum.get('openai_required_now', False)}`")
    lines.append(f"- github minimum launch card: `{dashboard.get('github_minimum_launch_card_md', '')}`")
    lines.append(f"- user review checkpoint: `{dashboard.get('user_review_checkpoint_html', '')}`")
    lines.append(f"- cloud launch preflight: `{dashboard.get('cloud_launch_preflight_md', '')}`")
    parity = dashboard.get("pipeline_workflow_parity", {})
    lines.append(f"- pipeline_workflow_parity: `{dashboard.get('pipeline_workflow_parity_md', '')}`")
    lines.append(f"- parity_all_core_scripts_present: `{parity.get('all_core_scripts_present', False)}`")
    lines.append(f"- parity_order_aligned: `{parity.get('order_aligned', False)}`")
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
    lines.append("## Automated Channels")
    lines.append("")
    lines.append("- 현재 기본 운영 경로는 Blogger 단일 자동화입니다.")
    lines.append("- WordPress는 Blogger 검증 후 두 번째 자동 채널로만 확장합니다.")
    for item in dashboard.get("platform_channels", []):
        lines.append(
            f"- `{item.get('name')}`: ready={item.get('ready')} / approved_ready_items={item.get('ready_item_count', 0)} / command `{item.get('command', '')}`"
        )
    if not dashboard.get("platform_channels"):
        lines.append("- 아직 플랫폼 배포 계획이 생성되지 않았습니다.")
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
    lines.append("## First Approval Path")
    lines.append("")
    batch = (dashboard.get("first_approval_path") or {}).get("recommended_batch", {})
    single = (dashboard.get("first_approval_path") or {}).get("recommended_single", {})
    if batch.get("item_count", 0):
        lines.append(
            f"- 추천 묶음: `{batch.get('label', '')}` / {batch.get('item_count', 0)}건 / command `{batch.get('approval_command', '')}`"
        )
    if single.get("keyword"):
        lines.append(
            f"- 단건 추천: `{single.get('keyword', '')}` / {single.get('title', '')} / command `{single.get('approval_command', '')}`"
        )
    if not batch.get("item_count", 0) and not single.get("keyword"):
        lines.append("- 아직 첫 승인 경로가 생성되지 않았습니다.")
    lines.append("")
    lines.append("## Daily Revenue Focus")
    lines.append("")
    revenue_path = (dashboard.get("daily_revenue_focus") or {}).get("today_path", [])
    if revenue_path:
        for item in revenue_path[:3]:
            lines.append(
                f"- `{item.get('step', '')}` / `{item.get('title', '')}` / revenue `{item.get('why_revenue', '')}`"
            )
    else:
        lines.append("- 아직 오늘의 수익화 경로 카드가 생성되지 않았습니다.")
    lines.append("")
    lines.append("## Monetization Roadmap")
    lines.append("")
    roadmap = (dashboard.get("monetization_roadmap") or {}).get("phases", [])
    for phase in roadmap[:3]:
        lines.append(f"- `{phase.get('phase', '')}` / gate `{phase.get('gate', '')}`")
    if not roadmap:
        lines.append("- 아직 수익화 로드맵이 생성되지 않았습니다.")
    lines.append("")
    lines.append("## First Publish Operator Run")
    lines.append("")
    operator_run = dashboard.get("first_publish_operator_run") or {}
    if operator_run.get("planned_commands"):
        lines.append(f"- approval_mode: `{operator_run.get('approval_mode', '')}`")
        for command in operator_run.get("planned_commands", [])[:4]:
            lines.append(f"- `{command}`")
    else:
        lines.append("- 아직 첫 발행 실행 카드가 생성되지 않았습니다.")
    lines.append("")
    lines.append("## User Review Shortlist")
    lines.append("")
    shortlist = (dashboard.get("user_review_shortlist") or {}).get("shortlist", [])
    for item in shortlist[:3]:
        lines.append(f"- `{item.get('title', '')}` / keyword `{item.get('keyword', '')}` / verdict `{item.get('review_verdict', '')}`")
    if not shortlist:
        lines.append("- 아직 사용자 검토 축약본이 생성되지 않았습니다.")
    lines.append("")
    lines.append("## Today Operator Console")
    lines.append("")
    console_state = (dashboard.get("today_operator_console") or {}).get("top_state", {})
    if console_state:
        lines.append(
            f"- ready `{console_state.get('ready_for_first_live_run', False)}` / repo_connected `{console_state.get('repo_connected', False)}` / github `{console_state.get('github_launch_status', '')}`"
        )
    else:
        lines.append("- 아직 오늘 운영 콘솔이 생성되지 않았습니다.")
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
