#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-blogger-verify-card.json"
OUTPUT_MD = ROOT / "outputs/latest/first-blogger-verify-card.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    single = first_approval.get("recommended_single", {})
    return {
        "headline": "GitHub 연결 전에도 로컬에서 첫 Blogger draft 검증까지 바로 확인할 수 있습니다.",
        "main_candidate": {
            "keyword": single.get("keyword", ""),
            "title": single.get("title", ""),
        },
        "shortcut_flow": {
            "preview": "python3 scripts/run_first_blogger_verify_flow.py",
            "apply": "python3 scripts/run_first_blogger_verify_flow.py --apply",
            "apply_skip_approval": "python3 scripts/run_first_blogger_verify_flow.py --apply --skip-approval",
            "apply_with_safety_check": "python3 scripts/run_first_blogger_verify_flow.py --apply --run-safety-check",
        },
        "references": {
            "first_publish_operator_run_md": str(ROOT / "outputs/latest/first-publish-operator-run.md"),
            "first_cloud_run_verification_md": str(ROOT / "outputs/latest/first-cloud-run-verification.md"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# First Blogger Verify Card")
    lines.append("")
    lines.append(report.get("headline", ""))
    lines.append("")
    candidate = report.get("main_candidate", {})
    lines.append(f"- main_candidate: `{candidate.get('keyword', '')}` / {candidate.get('title', '')}")
    lines.append("")
    lines.append("## Shortcut Flow")
    lines.append("")
    shortcut = report.get("shortcut_flow", {})
    lines.append(f"- preview: `{shortcut.get('preview', '')}`")
    lines.append(f"- apply: `{shortcut.get('apply', '')}`")
    lines.append(f"- apply_skip_approval: `{shortcut.get('apply_skip_approval', '')}`")
    lines.append(f"- apply_with_safety_check: `{shortcut.get('apply_with_safety_check', '')}`")
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
