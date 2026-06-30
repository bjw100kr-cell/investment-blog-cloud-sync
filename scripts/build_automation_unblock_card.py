#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_PROGRESS_JSON = ROOT / "outputs/latest/automation-progress-board.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
GITHUB_MINIMUM_JSON = ROOT / "outputs/latest/github-minimum-launch-card.json"
OUTPUT_JSON = ROOT / "outputs/latest/automation-unblock-card.json"
OUTPUT_MD = ROOT / "outputs/latest/automation-unblock-card.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    progress = load_json(AUTOMATION_PROGRESS_JSON)
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    github_minimum = load_json(GITHUB_MINIMUM_JSON)

    recommended_single = first_approval.get("recommended_single", {})
    approval_command = recommended_single.get("approval_command", "")
    keyword = recommended_single.get("keyword", "")

    user_actions = progress.get("user_needed_actions", [])
    free_cloud = next((item for item in user_actions if item.get("name") == "free_cloud_automation"), {})
    wordpress = next((item for item in user_actions if item.get("name") == "wordpress_expansion"), {})

    return {
        "headline": "지금 자동화를 더 앞으로 밀기 위해 사용자 쪽에서 필요한 건 사실 2개입니다.",
        "main_candidate": {
            "keyword": keyword,
            "title": recommended_single.get("title", ""),
            "approval_command": approval_command,
        },
        "primary_actions": [
            {
                "id": f"approve_{keyword}" if keyword else "approve_candidate",
                "label": f"1. {keyword or '최우선 후보'} 승인",
                "why": "이 1건만 승인되면 Blogger draft loop 실검증으로 바로 넘어갈 수 있습니다.",
                "command": approval_command,
                "owner": "user",
            },
            {
                "id": "connect_github_repo",
                "label": "2. GitHub repo 연결",
                "why": "이 단계가 끝나야 컴퓨터가 꺼져 있어도 무료 클라우드 자동화가 돌아갑니다.",
                "command": free_cloud.get("next_action", ""),
                "owner": "user",
                "links": {
                    "repo_create_link": github_minimum.get("repo_create_link", "https://github.com/new"),
                    "web_checklist_md": str(ROOT / "outputs/latest/github-web-launch-checklist.md"),
                },
            },
        ],
        "later_actions": [
            {
                "label": "WordPress 연결",
                "why": "Blogger 루프 검증 뒤 붙여도 늦지 않습니다.",
                "status": wordpress.get("status", "blocked"),
            },
            {
                "label": "Search Console / GA4 / AdSense",
                "why": "수익화 측정 고도화 단계이며 지금 당장 첫 자동화 검증의 선행조건은 아닙니다.",
                "status": "later",
            },
        ],
        "shortcut_flow": {
            "preview": "python3 scripts/run_minimum_unblock_flow.py",
            "preview_with_repo": "python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO",
            "apply_with_repo": "python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO --apply",
        },
        "references": {
            "automation_progress_board_md": str(ROOT / "outputs/latest/automation-progress-board.md"),
            "first_approval_path_md": str(ROOT / "outputs/latest/first-approval-path.md"),
            "github_minimum_launch_card_md": str(ROOT / "outputs/latest/github-minimum-launch-card.md"),
            "minimum_unblock_flow_md": str(ROOT / "outputs/latest/minimum-unblock-flow.md"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Automation Unblock Card")
    lines.append("")
    lines.append(report.get("headline", ""))
    lines.append("")
    candidate = report.get("main_candidate", {})
    lines.append(f"- main_candidate: `{candidate.get('keyword', '')}` / {candidate.get('title', '')}")
    lines.append("")
    lines.append("## 지금 할 2개")
    lines.append("")
    for item in report.get("primary_actions", []):
        lines.append(f"- `{item.get('label', '')}`")
        lines.append(f"  - why: {item.get('why', '')}")
        if item.get("command"):
            lines.append(f"  - command: {item.get('command', '')}")
        links = item.get("links", {})
        for key, value in links.items():
            lines.append(f"  - {key}: {value}")
    lines.append("")
    lines.append("## 나중에 해도 되는 것")
    lines.append("")
    for item in report.get("later_actions", []):
        lines.append(f"- `{item.get('label', '')}` / status `{item.get('status', '')}`")
        lines.append(f"  - why: {item.get('why', '')}")
    lines.append("")
    lines.append("## Shortcut Flow")
    lines.append("")
    shortcut = report.get("shortcut_flow", {})
    lines.append(f"- preview: `{shortcut.get('preview', '')}`")
    lines.append(f"- preview_with_repo: `{shortcut.get('preview_with_repo', '')}`")
    lines.append(f"- apply_with_repo: `{shortcut.get('apply_with_repo', '')}`")
    lines.append("")
    lines.append("## References")
    lines.append("")
    for key, value in report.get("references", {}).items():
        lines.append(f"- `{key}`: `{value}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
