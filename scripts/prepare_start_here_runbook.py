#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_DASHBOARD_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
FIRST_LIVE_RUN_PLAN_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
AUTOMATION_SCOPE_JSON = ROOT / "outputs/latest/automation-scope.json"
OUTPUT_MD = ROOT / "outputs/latest/start-here-runbook.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_lines() -> list[str]:
    setup = load_json(SETUP_JSON)
    dashboard = load_json(GO_LIVE_DASHBOARD_JSON)
    first_live = load_json(FIRST_LIVE_RUN_PLAN_JSON)
    github_plan = load_json(GITHUB_LAUNCH_PLAN_JSON)
    platform_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    automation_scope = load_json(AUTOMATION_SCOPE_JSON)

    repo_connected = dashboard.get("repo_connected", False)
    first_live_status = first_live.get("status", "")
    github_status = github_plan.get("status", "")
    missing_credentials = first_live.get("required_credentials_missing", [])
    env_filled = set(setup.get("env_keys_filled", []))

    lines = []
    lines.append("# Start Here Runbook")
    lines.append("")
    lines.append("이 문서만 따라가면 첫 로그인부터 첫 자동 채널 테스트 업로드와 GitHub 자동화 연결까지 진행할 수 있습니다.")
    lines.append("")
    lines.append("## 현재 상태")
    lines.append("")
    lines.append(f"- first_live_status: `{first_live_status or 'unknown'}`")
    lines.append(f"- github_status: `{github_status or 'unknown'}`")
    lines.append(f"- repo_connected: `{repo_connected}`")
    lines.append(f"- missing_credentials_count: `{len(missing_credentials)}`")
    lines.append("")
    lines.append("## 자동화 범위")
    lines.append("")
    lines.append(
        f"- 지금 당장 자동 운영하는 채널: `{automation_scope.get('primary_channel', {}).get('name', 'blogger')}`"
    )
    lines.append(
        f"- 나중에 붙일 두 번째 자동 채널: `{automation_scope.get('secondary_channel', {}).get('name', 'wordpress')}`"
    )
    lines.append("- 네이버/티스토리는 현재 자동 발행 범위에서 제외하고 수동 운영 채널로 둡니다.")
    lines.append("- 수동 채널 발행은 `cross-platform-publish-pack.md`의 채널별 단계에 따라 순차 진행하세요.")
    lines.append("  - 네이버: 복사 -> 붙여넣기 -> 카테고리/태그 설정 -> 발행 -> URL 기록")
    lines.append("  - 티스토리: 복사 -> 새 글 작성 -> 썸네일/태그 정리 -> 발행 -> URL 기록")
    lines.append("")
    lines.append("## 지금 바로 할 일")
    lines.append("")
    lines.append("로그인을 마치고 다시 돌아오면 먼저 이 명령을 실행해도 됩니다:")
    lines.append("- `python3 scripts/resume_after_login.py`")
    lines.append("")

    step_no = 1
    if "GOOGLE_CLIENT_ID" not in env_filled or "GOOGLE_CLIENT_SECRET" not in env_filled:
        lines.append(f"{step_no}. Google Cloud Console에서 OAuth client JSON을 다운로드합니다.")
        step_no += 1
        lines.append(f"{step_no}. `python3 scripts/bootstrap_google_oauth_credentials.py`")
        step_no += 1

    if "GOOGLE_REFRESH_TOKEN" not in env_filled:
        lines.append(f"{step_no}. `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py`")
        step_no += 1
        lines.append(f"{step_no}. `python3 scripts/apply_google_oauth_result.py`")
        step_no += 1

    if github_status == "needs_initial_commit":
        lines.append(f"{step_no}. `bash scripts/prepare_initial_commit.sh`")
        step_no += 1

    if not repo_connected:
        lines.append(f"{step_no}. GitHub에서 새 public repo를 만들고 URL을 복사합니다.")
        step_no += 1
        lines.append(f"{step_no}. `bash scripts/bootstrap_github_repo.py OWNER/REPO`")
        lines.append(
            "   (토큰이 없으면 토큰 발급 후 한 번만 브라우저에서 생성 또는 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` 사용)"
        )
        step_no += 1
        lines.append("")
        lines.append("GitHub 연결은 이 카드만 보면 바로 진행할 수 있습니다:")
        lines.append(f"- [github-minimum-launch-card.md]({ROOT / 'outputs/latest/github-minimum-launch-card.md'})")
        lines.append("")

    lines.append(f"{step_no}. `python3 scripts/check_setup.py`")
    step_no += 1
    lines.append(f"{step_no}. `bash scripts/run_pipeline.sh`")
    step_no += 1
    lines.append(f"{step_no}. 승인된 글이 있다면 자동 채널 draft가 정상 생성됐는지 확인합니다.")
    lines.append("")
    if (
        "WORDPRESS_SITE_URL" not in env_filled
        or "WORDPRESS_USERNAME" not in env_filled
        or "WORDPRESS_APPLICATION_PASSWORD" not in env_filled
    ):
        lines.append("## WordPress는 나중에 붙여도 됩니다")
        lines.append("")
        lines.append("- 지금 최소 실행 경로에는 WordPress가 필수가 아닙니다.")
        lines.append("- Blogger 실전 검증이 끝난 뒤 두 번째 자동 채널로 확장하면 됩니다.")
        lines.append("")

    if "OPENAI_API_KEY" not in env_filled:
        lines.append("## OpenAI 키 미입력 모드")
        lines.append("")
        lines.append("- OpenAI 키 없이도 템플릿 fallback 초안으로 일일 업로드를 시작할 수 있습니다.")
        lines.append("- 수익성/톤을 더 다듬으려면 `OPENAI_API_KEY`를 나중에 추가하고 같은 파이프라인을 재실행하세요.")
        lines.append("")

    lines.append("## 첫 업로드 목표")
    lines.append("")
    first_post = first_live.get("first_post_candidate", {})
    if first_post:
        lines.append(f"- 1차 테스트 글: `{first_post.get('title', '')}`")
        lines.append(f"- 유형: `{first_post.get('inventory_type', '')}`")
        lines.append(f"- CTA 포커스: {first_post.get('cta_focus', '')}")
    else:
        lines.append("- 아직 첫 업로드 후보가 없습니다.")
    lines.append("")
    lines.append("## 자동 채널 우선순위")
    lines.append("")
    for channel in platform_plan.get("channels", []):
        lines.append(
            f"- `{channel.get('name')}`: ready={channel.get('ready')} / command `{channel.get('command', '')}` / approved_ready_items={channel.get('ready_item_count', 0)}"
        )
    if not platform_plan.get("channels"):
        lines.append("- 아직 플랫폼 운영판이 없습니다.")
    lines.append("")

    lines.append("## 안전모드 확인")
    lines.append("")
    for key, value in (first_live.get("safe_mode_env") or {}).items():
        lines.append(f"- `{key}={value}`")
    lines.append("")

    lines.append("## 참고 문서")
    lines.append("")
    lines.append(f"- [first-live-run-plan.md]({ROOT / 'outputs/latest/first-live-run-plan.md'})")
    lines.append(f"- [github-launch-plan.md]({ROOT / 'outputs/latest/github-launch-plan.md'})")
    lines.append(f"- [go-live-dashboard.md]({ROOT / 'outputs/latest/go-live-dashboard.md'})")
    lines.append(f"- [platform-publish-plan.md]({ROOT / 'outputs/latest/platform-publish-plan.md'})")
    lines.append(f"- [automation-scope.md]({ROOT / 'outputs/latest/automation-scope.md'})")
    lines.append(f"- [cross-platform-publish-pack.md]({ROOT / 'outputs/latest/cross-platform-publish-pack.md'})")
    lines.append(f"- [current-reference-strategy.md]({ROOT / 'outputs/latest/current-reference-strategy.md'})")
    lines.append(f"- [reference-strength-benchmark.md]({ROOT / 'outputs/latest/reference-strength-benchmark.md'})")
    lines.append(f"- [keyword-capture-strategy.md]({ROOT / 'outputs/latest/keyword-capture-strategy.md'})")
    lines.append(f"- [first-approval-path.md]({ROOT / 'outputs/latest/first-approval-path.md'})")
    lines.append(f"- [daily-revenue-focus.md]({ROOT / 'outputs/latest/daily-revenue-focus.md'})")
    lines.append(f"- [traffic-cluster-board.md]({ROOT / 'outputs/latest/traffic-cluster-board.md'})")
    lines.append(f"- [popular-reads-board.md]({ROOT / 'outputs/latest/popular-reads-board.md'})")
    lines.append(f"- [retention-cta-board.md]({ROOT / 'outputs/latest/retention-cta-board.md'})")
    lines.append(f"- [monetization-roadmap.md]({ROOT / 'outputs/latest/monetization-roadmap.md'})")
    lines.append(f"- [first-publish-operator-run.md]({ROOT / 'outputs/latest/first-publish-operator-run.md'})")
    lines.append(f"- [user-review-shortlist.md]({ROOT / 'outputs/latest/user-review-shortlist.md'})")
    lines.append(f"- [review-preview-board.html]({ROOT / 'outputs/latest/review-preview-board.html'})")
    lines.append(f"- [operator-home.html]({ROOT / 'outputs/latest/operator-home.html'})")
    lines.append(f"- [draft-polish-board.md]({ROOT / 'outputs/latest/draft-polish-board.md'})")
    lines.append(f"- [pre-publish-quality-gate.md]({ROOT / 'outputs/latest/pre-publish-quality-gate.md'})")
    lines.append(f"- [today-operator-console.md]({ROOT / 'outputs/latest/today-operator-console.md'})")
    lines.append(f"- [github-web-launch-checklist.md]({ROOT / 'outputs/latest/github-web-launch-checklist.md'})")
    lines.append(f"- [github-minimum-launch-card.md]({ROOT / 'outputs/latest/github-minimum-launch-card.md'})")
    lines.append(f"- [cloud-launch-preflight.md]({ROOT / 'outputs/latest/cloud-launch-preflight.md'})")
    lines.append(f"- [first-run-values-card.md]({ROOT / 'outputs/latest/first-run-values-card.md'})")
    lines.append(f"- [pipeline-workflow-parity.md]({ROOT / 'outputs/latest/pipeline-workflow-parity.md'})")
    lines.append(f"- [first-cloud-run-verification.md]({ROOT / 'outputs/latest/first-cloud-run-verification.md'})")
    lines.append(f"- [operator-handoff.md]({ROOT / 'outputs/latest/operator-handoff.md'})")
    lines.append(f"- [success-gate.md]({ROOT / 'outputs/latest/success-gate.md'})")
    return lines


def main() -> int:
    OUTPUT_MD.write_text("\n".join(build_lines()) + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
