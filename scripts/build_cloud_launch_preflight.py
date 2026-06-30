#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
PIPELINE_WORKFLOW_PARITY_JSON = ROOT / "outputs/latest/pipeline-workflow-parity.json"
FIRST_CLOUD_RUN_VERIFICATION_JSON = ROOT / "outputs/latest/first-cloud-run-verification.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
GITHUB_MINIMUM_LAUNCH_CARD_JSON = ROOT / "outputs/latest/github-minimum-launch-card.json"
OUTPUT_JSON = ROOT / "outputs/latest/cloud-launch-preflight.json"
OUTPUT_MD = ROOT / "outputs/latest/cloud-launch-preflight.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict[str, dict]:
    return {item.get("name", ""): item for item in setup.get("integrations", []) if item.get("name")}


def build_gate(name: str, passed: bool, why: str, next_action: str = "") -> dict:
    return {
        "name": name,
        "passed": passed,
        "why": why,
        "next_action": next_action,
    }


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    github_plan = load_json(GITHUB_LAUNCH_PLAN_JSON)
    parity = load_json(PIPELINE_WORKFLOW_PARITY_JSON)
    cloud_verify = load_json(FIRST_CLOUD_RUN_VERIFICATION_JSON)
    approvals = load_json(REVIEW_APPROVALS_JSON)
    publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    minimum = load_json(GITHUB_MINIMUM_LAUNCH_CARD_JSON)

    integrations = integration_lookup(setup)
    git = setup.get("git", {})
    env_filled = set(setup.get("env_keys_filled", []))
    approved_keywords = approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", []))
    approval_all = bool(approvals.get("user_confirmed_all", approvals.get("approved_all", False)))
    blogger_ready = bool(integrations.get("blogger_upload", {}).get("ready", False))
    repo_connected = bool(github_plan.get("repo_connected", False))
    has_commit = bool(git.get("has_commit", False))
    required_secret_keys = github_plan.get(
        "sync_ready_keys",
        ["BLOGGER_BLOG_ID", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"],
    )
    present_required_secrets = [key for key in required_secret_keys if key in env_filled]

    has_approved_state = bool(approved_keywords) or approval_all
    verification_gate_passed = bool(cloud_verify.get("all_core_checks_passed", False))
    cloud_mode = cloud_verify.get("mode", "first_run_safety")

    gates = [
        build_gate(
            "repo_connected",
            repo_connected,
            "GitHub 저장소가 연결돼야 컴퓨터가 꺼져 있어도 GitHub Actions가 계속 돌 수 있습니다.",
            "bash scripts/bootstrap_github_remote.sh <OWNER/REPO>" if not repo_connected else "",
        ),
        build_gate(
            "has_commit",
            has_commit,
            "클라우드 실행 전에 최소 1회 커밋이 있어야 workflow가 참조할 기준 상태가 생깁니다.",
            "bash scripts/prepare_initial_commit.sh" if not has_commit else "",
        ),
        build_gate(
            "required_blogger_secrets_present_locally",
            len(present_required_secrets) == len(required_secret_keys),
            "Blogger 핵심 Secrets 4개가 로컬에 있어야 GitHub로 옮길 값도 확정됩니다.",
            "outputs/latest/github-minimum-launch-card.md 확인" if len(present_required_secrets) != len(required_secret_keys) else "",
        ),
        build_gate(
            "blogger_channel_ready",
            blogger_ready,
            "최소 자동 채널은 Blogger이므로 이 채널 준비가 안 되면 무료 자동화 첫 실행 가치가 떨어집니다.",
            "python3 scripts/check_setup.py" if not blogger_ready else "",
        ),
        build_gate(
            "workflow_parity_ok",
            bool(parity.get("all_core_scripts_present")) and bool(parity.get("order_aligned")),
            "로컬 파이프라인과 GitHub workflow 순서가 맞아야 같은 산출물이 안정적으로 생성됩니다.",
            "python3 scripts/build_pipeline_workflow_parity.py" if not (bool(parity.get("all_core_scripts_present")) and bool(parity.get("order_aligned"))) else "",
        ),
        build_gate(
            "review_state_safe_before_first_cloud_run",
            (not has_approved_state) or (cloud_mode == "approved_run"),
            "첫 클라우드 실행 전에는 승인 목록이 비어 있어야 의도치 않은 게시가 나가지 않습니다.",
            "python3 scripts/set_review_approvals.py --clear" if (approval_all or approved_keywords) else "",
        ),
        build_gate(
            "first_cloud_safety_checks_green",
            verification_gate_passed,
            "현재 업로드 차단/승인 게이트/보고서 정합성이 초록 상태여야 첫 GitHub Actions 검증이 안전합니다.",
            "python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state" if not verification_gate_passed else "",
        ),
    ]

    blockers = [gate for gate in gates if not gate.get("passed")]
    next_action = blockers[0].get("next_action", "") if blockers else "GitHub Actions -> Daily Investment Intake -> Run workflow"

    return {
        "ready_to_click_run_workflow": not blockers,
        "blocker_count": len(blockers),
        "repo_connected": repo_connected,
        "github_status": github_plan.get("status", ""),
        "has_commit": has_commit,
        "required_secret_keys": required_secret_keys,
        "present_required_secret_keys": present_required_secrets,
        "required_variables_count": minimum.get("required_variables_count", 7),
        "approved_ready_count": publish_plan.get("approved_ready_count", 0),
        "quality_ready_count": publish_plan.get("quality_ready_count", 0),
        "review_approval_state": {
            "user_confirmed_all": approval_all,
            "user_confirmed_keywords": approved_keywords,
        },
        "gates": gates,
        "blockers": blockers,
        "next_action": next_action,
        "references": {
            "github_minimum_launch_card_md": str(ROOT / "outputs/latest/github-minimum-launch-card.md"),
            "pipeline_workflow_parity_md": str(ROOT / "outputs/latest/pipeline-workflow-parity.md"),
            "first_cloud_run_verification_md": str(ROOT / "outputs/latest/first-cloud-run-verification.md"),
            "user_review_checkpoint_html": str(ROOT / "outputs/latest/user-review-checkpoint.html"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Cloud Launch Preflight")
    lines.append("")
    lines.append("GitHub Actions의 `Run workflow`를 눌러도 되는지 사전에 확인하는 점검 카드입니다.")
    lines.append("")
    lines.append(f"- ready_to_click_run_workflow: `{report.get('ready_to_click_run_workflow', False)}`")
    lines.append(f"- blocker_count: `{report.get('blocker_count', 0)}`")
    lines.append(f"- repo_connected: `{report.get('repo_connected', False)}`")
    lines.append(f"- github_status: `{report.get('github_status', '')}`")
    lines.append(f"- has_commit: `{report.get('has_commit', False)}`")
    lines.append(f"- approved_ready_count: `{report.get('approved_ready_count', 0)}`")
    lines.append(f"- quality_ready_count: `{report.get('quality_ready_count', 0)}`")
    lines.append(f"- review_approval_state: `{json.dumps(report.get('review_approval_state', {}), ensure_ascii=False)}`")
    lines.append(f"- next_action: `{report.get('next_action', '')}`")
    lines.append("")
    lines.append("## Core Gates")
    lines.append("")
    for gate in report.get("gates", []):
        lines.append(f"- `{gate.get('name', '')}`: `{gate.get('passed', False)}`")
        lines.append(f"  - why: {gate.get('why', '')}")
        if gate.get("next_action"):
            lines.append(f"  - next_action: `{gate.get('next_action', '')}`")
    lines.append("")
    lines.append("## References")
    lines.append("")
    refs = report.get("references", {})
    lines.append(f"- github minimum launch card: `{refs.get('github_minimum_launch_card_md', '')}`")
    lines.append(f"- pipeline workflow parity: `{refs.get('pipeline_workflow_parity_md', '')}`")
    lines.append(f"- first cloud run verification: `{refs.get('first_cloud_run_verification_md', '')}`")
    lines.append(f"- user review checkpoint: `{refs.get('user_review_checkpoint_html', '')}`")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
