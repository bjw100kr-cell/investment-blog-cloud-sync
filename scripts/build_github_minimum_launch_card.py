#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKLIST_JSON = ROOT / "outputs/latest/github-web-launch-checklist.json"
LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/github-minimum-launch-card.json"
OUTPUT_MD = ROOT / "outputs/latest/github-minimum-launch-card.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    checklist = load_json(CHECKLIST_JSON)
    launch = load_json(LAUNCH_PLAN_JSON)
    minimum = checklist.get("minimum_path_summary", {})
    links = checklist.get("links", {})

    return {
        "repo_connected": launch.get("repo_connected", False),
        "github_status": launch.get("status", ""),
        "repo_slug": launch.get("repo_slug", ""),
        "repo_create_link": links.get("repo_home", "https://github.com/new"),
        "actions_secrets_link": links.get("actions_secrets", "https://github.com/new"),
        "workflow_run_link": links.get("actions_runs", "https://github.com/new"),
        "required_secrets_count": minimum.get("required_secrets_count", 4),
        "required_variables_count": minimum.get("required_variables_count", 7),
        "wordpress_required_now": minimum.get("wordpress_required_now", False),
        "openai_required_now": minimum.get("openai_required_now", False),
        "first_goal": minimum.get("first_goal", ""),
        "steps": [
            "GitHub에서 새 public repo를 만듭니다.",
            "로컬에서 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` 를 실행합니다.",
            "GitHub 웹 UI에서 Secrets 4개와 Variables 7개만 먼저 입력합니다.",
            "Actions에서 `Daily Investment Intake`를 수동 실행합니다.",
            "Blogger draft가 1건만 안전모드로 생성됐는지 확인합니다.",
        ],
        "copy_refs": {
            "web_checklist_md": str(ROOT / "outputs/latest/github-web-launch-checklist.md"),
            "values_card_md": str(ROOT / "outputs/latest/first-run-values-card.md"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# GitHub Minimum Launch Card")
    lines.append("")
    lines.append("무료 클라우드 자동화를 붙일 때 지금 바로 따라가면 되는 최소 실행 카드입니다.")
    lines.append("")
    lines.append(f"- repo_connected: `{report.get('repo_connected', False)}`")
    lines.append(f"- github_status: `{report.get('github_status', '')}`")
    lines.append(f"- repo_slug: `{report.get('repo_slug', '') or 'OWNER/REPO 필요'}`")
    lines.append(f"- 지금 필요한 Secrets 수: `{report.get('required_secrets_count', 0)}`")
    lines.append(f"- 지금 필요한 Variables 수: `{report.get('required_variables_count', 0)}`")
    lines.append(f"- WordPress 지금 필수 여부: `{report.get('wordpress_required_now', False)}`")
    lines.append(f"- OpenAI 지금 필수 여부: `{report.get('openai_required_now', False)}`")
    lines.append(f"- 첫 목표: {report.get('first_goal', '')}")
    lines.append("")
    lines.append("## Links")
    lines.append("")
    lines.append(f"- repo_create_link: {report.get('repo_create_link', '')}")
    lines.append(f"- actions_secrets_link: {report.get('actions_secrets_link', '')}")
    lines.append(f"- workflow_run_link: {report.get('workflow_run_link', '')}")
    lines.append("")
    lines.append("## Steps")
    lines.append("")
    for idx, step in enumerate(report.get("steps", []), start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    lines.append("## Reference")
    lines.append("")
    lines.append(f"- web checklist: `{report.get('copy_refs', {}).get('web_checklist_md', '')}`")
    lines.append(f"- values card: `{report.get('copy_refs', {}).get('values_card_md', '')}`")
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
