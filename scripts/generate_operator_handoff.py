#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_REPORT = ROOT / "outputs/latest/setup-check-report.json"
PUBLISH_READY_REPORT = ROOT / "outputs/latest/publish-ready-report.json"
GITHUB_CHECKLIST = ROOT / "outputs/latest/github-secrets-checklist.md"
PUBLISH_QUEUE_REPORT = ROOT / "outputs/latest/publish-queue.json"
PUBLISH_INVENTORY_REPORT = ROOT / "outputs/latest/publish-inventory.json"
MONETIZATION_REPORT = ROOT / "outputs/latest/monetization-readiness-report.json"
GO_LIVE_REPORT = ROOT / "outputs/latest/go-live-readiness-report.json"
KEYWORD_BOARD_REPORT = ROOT / "outputs/latest/keyword-opportunity-board.json"
FIRST_LIVE_RUN_PLAN_REPORT = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_PLAN_REPORT = ROOT / "outputs/latest/github-launch-plan.json"
PLATFORM_PUBLISH_PLAN_REPORT = ROOT / "outputs/latest/platform-publish-plan.json"
FIRST_APPROVAL_PATH_REPORT = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_MD = ROOT / "outputs/latest/operator-handoff.md"
ENV_PATH = ROOT / ".env"


def parse_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(report: dict) -> dict:
    return {item["name"]: item for item in report.get("integrations", [])}


def main() -> int:
    setup = load_json(SETUP_REPORT)
    publish_ready = load_json(PUBLISH_READY_REPORT)
    publish_queue = load_json(PUBLISH_QUEUE_REPORT)
    publish_inventory = load_json(PUBLISH_INVENTORY_REPORT)
    monetization = load_json(MONETIZATION_REPORT)
    go_live = load_json(GO_LIVE_REPORT)
    keyword_board = load_json(KEYWORD_BOARD_REPORT)
    first_live_run_plan = load_json(FIRST_LIVE_RUN_PLAN_REPORT)
    github_launch_plan = load_json(GITHUB_LAUNCH_PLAN_REPORT)
    platform_publish_plan = load_json(PLATFORM_PUBLISH_PLAN_REPORT)
    first_approval_path = load_json(FIRST_APPROVAL_PATH_REPORT)
    integrations = integration_lookup(setup)
    breaking_candidates = keyword_board.get("breaking_candidates", [])
    seo_followups = keyword_board.get("seo_followups", [])
    env_values = parse_env(ENV_PATH)

    lines = []
    lines.append("# Operator Handoff")
    lines.append("")
    lines.append("블로그 자동화를 실제 발행 단계로 넘기기 전에 필요한 값과 현재 상태를 정리한 문서입니다.")
    lines.append("")
    lines.append("## 지금 상태")
    lines.append("")
    lines.append(f"- git origin: {setup.get('git', {}).get('origin', '(unknown)')}")
    lines.append(f"- .env present: {setup.get('env_file_exists', False)}")
    lines.append(f"- publish-ready items: {len(publish_ready.get('items', []))}")
    ready_count = sum(1 for item in publish_ready.get("items", []) if item.get("ready"))
    lines.append(f"- publish-ready actual HTML count: {ready_count}")
    lines.append(f"- publish queue ready count: {publish_queue.get('summary', {}).get('ready_count', 0)}")
    lines.append(f"- publish inventory ready count: {publish_inventory.get('summary', {}).get('ready_count', 0)}")
    lines.append(f"- monetization readiness score: {monetization.get('readiness_score', 0)}")
    lines.append(f"- first live run ready: {go_live.get('ready_for_first_live_run', False)}")
    if first_live_run_plan.get("status"):
        lines.append(f"- first live run plan status: {first_live_run_plan.get('status')}")
    if github_launch_plan.get("status"):
        lines.append(f"- github launch plan status: {github_launch_plan.get('status')}")
    lines.append("")
    lines.append("## 꼭 필요한 값")
    lines.append("")
    lines.append("- `BLOGGER_BLOG_ID`: 업로드할 Blogger 블로그 ID")
    lines.append("- `GOOGLE_CLIENT_ID`: Google OAuth client ID")
    lines.append("- `GOOGLE_CLIENT_SECRET`: Google OAuth client secret")
    lines.append("- `GOOGLE_REFRESH_TOKEN`: Blogger 업로드용 refresh token")
    lines.append("- `GitHub repository URL`: 클라우드 자동 실행 연결")
    lines.append("")
    lines.append("## 있으면 바로 좋아지는 값")
    lines.append("")
    lines.append("- `OPENAI_API_KEY`")
    lines.append("- `SEARCH_CONSOLE_SITE_URL`")
    lines.append("- `SEARCH_CONSOLE_CLIENT_ID`")
    lines.append("- `SEARCH_CONSOLE_CLIENT_SECRET`")
    lines.append("- `SEARCH_CONSOLE_REFRESH_TOKEN`")
    lines.append("- `NAVER_CLIENT_ID`")
    lines.append("- `NAVER_CLIENT_SECRET`")
    lines.append("- `BLOG_BASE_URL`")
    lines.append("- `GA4_MEASUREMENT_ID`")
    lines.append("- `ADSENSE_PUBLISHER_ID`")
    lines.append("- `ADSENSE_SITE_VERIFICATION`")
    lines.append("- `NEWSLETTER_SUBSCRIBE_URL`")
    lines.append("- `BLOGGER_SYNC_SITE_PAGES`")
    lines.append("- `BLOGGER_SITE_PAGES_PUBLISH`")
    lines.append("- `BLOGGER_AUTO_PUBLISH_POSTS`")
    lines.append("- `BLOGGER_PUBLISH_ONLY_DUE_POSTS`")
    lines.append("- `BLOGGER_MAX_POSTS_PER_RUN`")
    lines.append("- `WORDPRESS_SITE_URL`")
    lines.append("- `WORDPRESS_USERNAME`")
    lines.append("- `WORDPRESS_APPLICATION_PASSWORD`")
    lines.append("- `WORDPRESS_AUTO_PUBLISH_POSTS`")
    lines.append("- `WORDPRESS_PUBLISH_ONLY_DUE_POSTS`")
    lines.append("- `WORDPRESS_MAX_POSTS_PER_RUN`")
    lines.append("")
    lines.append("## 현재 미연결 항목")
    lines.append("")
    for name in ["openai_drafts", "blogger_upload", "wordpress_upload", "search_console", "naver_datalab"]:
        item = integrations.get(name, {})
        if item.get("ready"):
            lines.append(f"- {name}: ready")
        else:
            missing = ", ".join(item.get("missing", [])) or "unknown"
            lines.append(f"- {name}: missing {missing}")
    lines.append("")
    lines.append("## 자동 채널 운영 상태")
    lines.append("")
    lines.append("- 현재 공식 1차 자동 채널은 `blogger`입니다.")
    lines.append("- `wordpress`는 Blogger 검증 뒤 붙이는 2차 확장 채널입니다.")
    for channel in platform_publish_plan.get("channels", []):
        lines.append(
            f"- {channel.get('name')}: ready={channel.get('ready')} / approved_ready_items={channel.get('ready_item_count', 0)} / command {channel.get('command', '')}"
        )
    if not platform_publish_plan.get("channels"):
        lines.append("- 아직 플랫폼 배포 계획이 생성되지 않았습니다.")
    lines.append("")
    lines.append("## 연결 순서")
    lines.append("")
    lines.append("1. `.env.example`를 복사해서 `.env` 생성")
    lines.append("2. `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` 입력")
    lines.append("3. `python3 scripts/bootstrap_google_oauth_credentials.py`로 client json을 자동 반영")
    lines.append("4. `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py` 실행")
    lines.append("5. `python3 scripts/apply_google_oauth_result.py`로 refresh token 반영")
    lines.append("6. `GOOGLE_REFRESH_TOKEN`, `BLOGGER_BLOG_ID` 확인")
    blogger_sync_site_pages = env_values.get("BLOGGER_SYNC_SITE_PAGES", "false")
    blogger_site_pages_publish = env_values.get("BLOGGER_SITE_PAGES_PUBLISH", "false")
    blogger_auto_publish = env_values.get("BLOGGER_AUTO_PUBLISH_POSTS", "false")
    blogger_publish_only_due_posts = env_values.get("BLOGGER_PUBLISH_ONLY_DUE_POSTS", "true")
    blogger_max_posts_per_run = env_values.get("BLOGGER_MAX_POSTS_PER_RUN", "1")

    lines.append(
        f"7. `BLOGGER_SYNC_SITE_PAGES={blogger_sync_site_pages}`, `BLOGGER_SITE_PAGES_PUBLISH={blogger_site_pages_publish}`로 첫 테스트"
    )
    lines.append(
        f"8. `BLOGGER_AUTO_PUBLISH_POSTS={blogger_auto_publish}`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS={blogger_publish_only_due_posts}`, `BLOGGER_MAX_POSTS_PER_RUN={blogger_max_posts_per_run}`로 안전모드 설정"
    )
    lines.append("9. `bash scripts/prepare_initial_commit.sh` 실행")
    lines.append("10. GitHub 원격 연결 후 Actions Secrets/Variables 입력")
    lines.append("11. `python3 scripts/check_setup.py` 재실행")
    lines.append("12. `bash scripts/run_pipeline.sh` 재실행")
    lines.append("13. `outputs/latest/first-approval-path.md` 기준으로 첫 승인 keyword 결정")
    lines.append("14. Blogger 검증이 안정화된 뒤에만 WordPress 값과 OpenAI/GA4/AdSense/Newsletter를 순차 추가")
    lines.append("")
    lines.append("## 오늘 운영자가 바로 할 일")
    lines.append("")
    recommended_batch = first_approval_path.get("recommended_batch", {})
    recommended_single = first_approval_path.get("recommended_single", {})
    action_single = first_approval_path.get("recommended_single", {})
    if action_single.get("keyword"):
        lines.append(
            f"- 1순위 발행: `{action_single.get('keyword')}` / {action_single.get('title', '')} / urgency {action_single.get('freshness_status', 'default')}"
        )
        lines.append(f"- 1순위 액션: {action_single.get('freshness_recommendation', '사용자 검토 후 업로드 진행')}")
    if recommended_batch.get("item_count", 0):
        lines.append(
            f"- 추천 묶음 승인: `{recommended_batch.get('label', '')}` / command `{recommended_batch.get('approval_command', '')}`"
        )
    if recommended_single.get("keyword"):
        lines.append(
            f"- 단건 승인 시작점: `{recommended_single.get('keyword', '')}` / {recommended_single.get('title', '')} / command `{recommended_single.get('approval_command', '')}`"
        )
    if len(breaking_candidates) > 1:
        second = breaking_candidates[1]
        lines.append(f"- 2순위 준비: `{second.get('keyword')}` / {second.get('suggested_title')} / urgency {second.get('urgency')}")
    if seo_followups:
        lines.append(f"- 오늘 후속 SEO 후보: `{seo_followups[0].get('title')}`")
        lines.append(f"- 후속 검색 의도: {seo_followups[0].get('search_intent')}")
    ready_inventory = [item for item in publish_inventory.get("items", []) if item.get("ready_to_upload")]
    if ready_inventory:
        lines.append(f"- 전체 업로드 가능 재고: {len(ready_inventory)}개")
        lines.append(f"- 재고판 1순위: `{ready_inventory[0].get('title')}` ({ready_inventory[0].get('inventory_type')})")
    if platform_publish_plan.get("channels"):
        primary = next((item for item in platform_publish_plan.get("channels", []) if item.get("ready")), {})
        if primary:
            lines.append(f"- 현재 1차 자동 채널: `{primary.get('name')}` / 실행 명령 `{primary.get('command', '')}`")
    if not breaking_candidates and not seo_followups:
        lines.append("- 아직 오늘의 기회판이 생성되지 않았습니다. `python3 scripts/build_keyword_opportunity_board.py`를 먼저 실행합니다.")
    lines.append("")
    lines.append("## 수익화 기준에서 남은 것")
    lines.append("")
    for stage in monetization.get("stages", []):
        state = "ready" if stage.get("ready") else "not_ready"
        lines.append(f"- {stage.get('name')}: {state}")
        if not stage.get("ready"):
            lines.append(f"  - next: {stage.get('next_step', '')}")
    lines.append("")
    lines.append("## 참고 파일")
    lines.append("")
    lines.append(f"- setup report: `{SETUP_REPORT}`")
    lines.append(f"- publish-ready report: `{PUBLISH_READY_REPORT}`")
    lines.append(f"- publish queue: `{PUBLISH_QUEUE_REPORT}`")
    lines.append(f"- publish inventory: `{PUBLISH_INVENTORY_REPORT}`")
    lines.append(f"- monetization report: `{MONETIZATION_REPORT}`")
    lines.append(f"- go-live report: `{GO_LIVE_REPORT}`")
    lines.append(f"- keyword opportunity board: `{KEYWORD_BOARD_REPORT}`")
    lines.append(f"- first live run plan: `{FIRST_LIVE_RUN_PLAN_REPORT}`")
    lines.append(f"- github launch plan: `{GITHUB_LAUNCH_PLAN_REPORT}`")
    lines.append(f"- platform publish plan: `{PLATFORM_PUBLISH_PLAN_REPORT}`")
    lines.append(f"- first approval path: `{FIRST_APPROVAL_PATH_REPORT}`")
    lines.append(f"- github checklist: `{GITHUB_CHECKLIST}`")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
