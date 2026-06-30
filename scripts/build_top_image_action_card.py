#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_LEVERAGE_BOARD_JSON = ROOT / "outputs/latest/image-leverage-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/top-image-action-card.json"
OUTPUT_MD = ROOT / "outputs/latest/top-image-action-card.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    payload = load_json(IMAGE_LEVERAGE_BOARD_JSON)
    lanes = payload.get("lanes", [])
    top_lane = lanes[0] if lanes else {}
    items = top_lane.get("top_items", [])

    grouped = {
        "main": [item for item in items if item.get("source_group") == "main"],
        "seo": [item for item in items if item.get("source_group") == "seo"],
    }

    return {
        "has_lane": bool(top_lane),
        "lane": top_lane,
        "shared_search_url": items[0].get("search_url", "") if items else "",
        "shared_license_url": items[0].get("license_url", "") if items else "",
        "shared_provider_name": items[0].get("provider_name", "") if items else "",
        "shared_search_query": items[0].get("search_query", "") if items else "",
        "shared_license_label": items[0].get("license_label", "") if items else "",
        "main_items": grouped["main"],
        "seo_items": grouped["seo"],
        "total_items": len(items),
        "expected_unlock_count": top_lane.get("unlock_count", 0),
        "revenue_hit": top_lane.get("revenue_hit", False),
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Top Image Action Card")
    lines.append("")
    lines.append("지금 가장 레버리지가 큰 이미지 라인을 바로 실행할 수 있게 묶어 놓은 카드입니다.")
    lines.append("")

    if not report.get("has_lane"):
        lines.append("- 현재는 이미지 실행 카드로 만들 라인이 없습니다.")
        OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
        return

    lane = report.get("lane", {})
    lines.append(f"- lane_label: `{lane.get('lane_label', '')}`")
    lines.append(f"- expected_unlock_count: `{report.get('expected_unlock_count', 0)}`")
    lines.append(f"- revenue_hit: `{report.get('revenue_hit', False)}`")
    lines.append(f"- why_now: {lane.get('why_now', '')}")
    if lane.get("capture_route"):
        lines.append(f"- capture_route: `{lane.get('capture_route', '')}`")
    lines.append("")
    lines.append("## Shared Search")
    lines.append("")
    lines.append(f"- provider: `{report.get('shared_provider_name', '')}`")
    lines.append(f"- query: `{report.get('shared_search_query', '')}`")
    lines.append(f"- search_url: {report.get('shared_search_url', '')}")
    lines.append(f"- license: {report.get('shared_license_label', '')} / {report.get('shared_license_url', '')}")
    lines.append("- usage_note: 같은 분위기의 이미지를 이 라인 글들에 맞춰 순차 적용하면 ready 후보 수를 빠르게 늘릴 수 있습니다.")
    lines.append("")
    lines.append("## Apply Order")
    lines.append("")
    lines.append("- 1순위: 메인 글부터 고릅니다.")
    lines.append("- 2순위: 같은 라인의 SEO 후속 글 2~3개까지 이어서 적용합니다.")
    lines.append("- 3순위: 적용 후 파이프라인을 다시 돌려 품질 게이트와 ready 상태를 확인합니다.")
    lines.append("")
    lines.append("## Main First")
    lines.append("")
    for item in report.get("main_items", []):
        lines.append(f"- `{item.get('keyword', '')}` / {item.get('title', '')}")
        lines.append(f"- helper: `{item.get('apply_helper', '')}`")
    if not report.get("main_items"):
        lines.append("- none")
    lines.append("")
    lines.append("## SEO Followups")
    lines.append("")
    for item in report.get("seo_items", []):
        lines.append(f"- `{item.get('keyword', '')}` / {item.get('title', '')}")
        lines.append(f"- helper: `{item.get('apply_helper', '')}`")
    if not report.get("seo_items"):
        lines.append("- none")
    lines.append("")
    lines.append("## After Image Apply")
    lines.append("")
    lines.append("- `bash scripts/run_pipeline.sh`")
    lines.append("- 확인 파일: `outputs/latest/pre-publish-quality-gate.md`")
    lines.append("- 확인 파일: `outputs/latest/platform-publish-plan.md`")
    lines.append("- 확인 파일: `outputs/latest/user-review-shortlist.md`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
