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
OUTPUT_MD = ROOT / "outputs/latest/operator-handoff.md"


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
    integrations = integration_lookup(setup)
    breaking_candidates = keyword_board.get("breaking_candidates", [])
    seo_followups = keyword_board.get("seo_followups", [])

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
    lines.append("- `OPENAI_API_KEY`: 실제 블로그 초안 생성")
    lines.append("- `BLOGGER_BLOG_ID`: 업로드할 Blogger 블로그 ID")
    lines.append("- `GOOGLE_CLIENT_ID`: Google OAuth client ID")
    lines.append("- `GOOGLE_CLIENT_SECRET`: Google OAuth client secret")
    lines.append("- `GOOGLE_REFRESH_TOKEN`: Blogger 업로드용 refresh token")
    lines.append("- `GitHub repository URL`: 클라우드 자동 실행 연결")
    lines.append("")
    lines.append("## 있으면 바로 좋아지는 값")
    lines.append("")
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
    lines.append("")
    lines.append("## 현재 미연결 항목")
    lines.append("")
    for name in ["openai_drafts", "blogger_upload", "search_console", "naver_datalab"]:
        item = integrations.get(name, {})
        if item.get("ready"):
            lines.append(f"- {name}: ready")
        else:
            missing = ", ".join(item.get("missing", [])) or "unknown"
            lines.append(f"- {name}: missing {missing}")
    lines.append("")
    lines.append("## 연결 순서")
    lines.append("")
    lines.append("1. `.env.example`를 복사해서 `.env` 생성")
    lines.append("2. `OPENAI_API_KEY` 입력")
    lines.append("3. `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` 입력")
    lines.append("4. `python3 scripts/bootstrap_google_oauth_credentials.py`로 client json을 자동 반영")
    lines.append("5. `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py` 실행")
    lines.append("6. `python3 scripts/apply_google_oauth_result.py`로 refresh token 반영")
    lines.append("7. `GOOGLE_REFRESH_TOKEN`, `BLOGGER_BLOG_ID` 확인")
    lines.append("8. `BLOGGER_SYNC_SITE_PAGES=true`, `BLOGGER_SITE_PAGES_PUBLISH=false`로 첫 테스트")
    lines.append("9. `BLOGGER_AUTO_PUBLISH_POSTS=false`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`, `BLOGGER_MAX_POSTS_PER_RUN=1`로 안전모드 설정")
    lines.append("10. `GA4_MEASUREMENT_ID`, `ADSENSE_PUBLISHER_ID`, `ADSENSE_SITE_VERIFICATION`, `NEWSLETTER_SUBSCRIBE_URL` 입력")
    lines.append("11. 필요하면 Search Console / Naver 값 입력")
    lines.append("12. `bash scripts/prepare_initial_commit.sh` 실행")
    lines.append("13. GitHub 원격 연결 후 Actions Secrets/Variables 입력")
    lines.append("14. `python3 scripts/check_setup.py` 재실행")
    lines.append("15. `bash scripts/run_pipeline.sh` 재실행")
    lines.append("")
    lines.append("## 오늘 운영자가 바로 할 일")
    lines.append("")
    if breaking_candidates:
        top = breaking_candidates[0]
        lines.append(f"- 1순위 발행: `{top.get('keyword')}` / {top.get('suggested_title')} / urgency {top.get('urgency')}")
        lines.append(f"- 1순위 액션: {top.get('operator_action')}")
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
    lines.append(f"- github checklist: `{GITHUB_CHECKLIST}`")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
