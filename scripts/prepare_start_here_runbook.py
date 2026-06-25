#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_DASHBOARD_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
FIRST_LIVE_RUN_PLAN_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
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

    repo_connected = dashboard.get("repo_connected", False)
    first_live_status = first_live.get("status", "")
    github_status = github_plan.get("status", "")
    missing_credentials = first_live.get("required_credentials_missing", [])
    env_filled = set(setup.get("env_keys_filled", []))

    lines = []
    lines.append("# Start Here Runbook")
    lines.append("")
    lines.append("이 문서만 따라가면 첫 로그인부터 첫 Blogger 테스트 업로드와 GitHub 자동화 연결까지 진행할 수 있습니다.")
    lines.append("")
    lines.append("## 현재 상태")
    lines.append("")
    lines.append(f"- first_live_status: `{first_live_status or 'unknown'}`")
    lines.append(f"- github_status: `{github_status or 'unknown'}`")
    lines.append(f"- repo_connected: `{repo_connected}`")
    lines.append(f"- missing_credentials_count: `{len(missing_credentials)}`")
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
        lines.append(f"{step_no}. `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>`")
        step_no += 1

    lines.append(f"{step_no}. `python3 scripts/check_setup.py`")
    step_no += 1
    lines.append(f"{step_no}. `bash scripts/run_pipeline.sh`")
    step_no += 1
    lines.append(f"{step_no}. Blogger draft와 site page가 정상 생성됐는지 확인합니다.")
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
    lines.append(f"- [operator-handoff.md]({ROOT / 'outputs/latest/operator-handoff.md'})")
    lines.append(f"- [success-gate.md]({ROOT / 'outputs/latest/success-gate.md'})")
    return lines


def main() -> int:
    OUTPUT_MD.write_text("\n".join(build_lines()) + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
