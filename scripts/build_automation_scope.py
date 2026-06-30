#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/automation-scope.json"
OUTPUT_MD = ROOT / "outputs/latest/automation-scope.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    integrations = integration_lookup(setup)
    blogger_ready = integrations.get("blogger_upload", {}).get("ready", False)
    wordpress_ready = integrations.get("wordpress_upload", {}).get("ready", False)

    return {
        "automation_policy": "automation-first",
        "primary_channel": {
            "name": "blogger",
            "status": "active",
            "ready": blogger_ready,
            "why": "무료에 가깝고 GitHub Actions와 결합해 초안 자동 업로드를 검증하기 가장 단순합니다.",
        },
        "secondary_channel": {
            "name": "wordpress",
            "status": "optional_later",
            "ready": wordpress_ready,
            "why": "공식 REST API 기반 자동화가 가능하지만 초기 설정 복잡도가 Blogger보다 높습니다.",
        },
        "manual_only_channels": [
            {
                "name": "naver_blog",
                "status": "excluded_from_automation",
                "why": "현재 프로젝트에서는 안정적인 공식 자동 발행 경로로 보지 않고 수동 운영 채널로 분리합니다.",
            },
            {
                "name": "tistory",
                "status": "excluded_from_automation",
                "why": "초기 무자본 자동화 기준에서 운영 안정성이 낮아 1차 범위에서 제외합니다.",
            },
        ],
        "cloud_runtime": {
            "provider": "github_actions",
            "free_tier_bias": True,
            "reason": "로컬 컴퓨터가 꺼져 있어도 정기 실행과 아티팩트 저장이 가능합니다.",
        },
        "review_gate": {
            "required": True,
            "reason": "업로드 전 반드시 사용자가 내용을 검토하고 승인 keyword 를 지정해야 합니다.",
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Automation Scope")
    lines.append("")
    lines.append(f"- automation_policy: `{report.get('automation_policy', '')}`")
    lines.append(f"- cloud_runtime: `{report.get('cloud_runtime', {}).get('provider', '')}`")
    lines.append(f"- review_gate_required: `{report.get('review_gate', {}).get('required', False)}`")
    lines.append("")
    lines.append("## Active Now")
    lines.append("")
    primary = report.get("primary_channel", {})
    lines.append(
        f"- `{primary.get('name', '')}`: status={primary.get('status')} / ready={primary.get('ready')} / {primary.get('why', '')}"
    )
    lines.append("")
    lines.append("## Expand Later")
    lines.append("")
    secondary = report.get("secondary_channel", {})
    lines.append(
        f"- `{secondary.get('name', '')}`: status={secondary.get('status')} / ready={secondary.get('ready')} / {secondary.get('why', '')}"
    )
    lines.append("")
    lines.append("## Excluded From Automation")
    lines.append("")
    for item in report.get("manual_only_channels", []):
        lines.append(f"- `{item.get('name', '')}`: {item.get('why', '')}")
    lines.append("")
    lines.append("## Operating Rule")
    lines.append("")
    lines.append("- 자동화 기본 경로는 `Blogger -> 사용자 검토 -> 승인 후 draft 업로드 -> GitHub Actions 일일 실행` 입니다.")
    lines.append("- WordPress는 Blogger 검증이 끝난 뒤 두 번째 자동 채널로만 확장합니다.")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
