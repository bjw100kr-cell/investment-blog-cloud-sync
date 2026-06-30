#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN_ASSETS_JSON = ROOT / "outputs/latest/publishing-assets.json"
SEO_ASSETS_JSON = ROOT / "outputs/latest/seo-publishing-assets.json"
IMAGE_SELECTIONS_JSON = ROOT / "outputs/latest/image-selections.json"
OUTPUT_JSON = ROOT / "outputs/latest/safe-image-suggestions.json"
OUTPUT_MD = ROOT / "outputs/latest/safe-image-suggestions.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def collect_items(path: Path, source_group: str) -> list[dict]:
    payload = load_json(path)
    items = []
    for item in payload.get("items", []):
        items.append(
            {
                "source_group": source_group,
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "category": item.get("category", ""),
                "image_plan": item.get("image_plan", []),
                "image_usage_checklist": item.get("image_usage_checklist", []),
                "image_blocked_subjects": item.get("image_blocked_subjects", []),
            }
        )
    return items


def load_selection_lookup() -> dict[tuple[str, str], dict]:
    payload = load_json(IMAGE_SELECTIONS_JSON)
    lookup: dict[tuple[str, str], dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        slot = item.get("slot", "")
        if keyword and slot:
            lookup[(keyword, slot)] = item
    return lookup


def build_report() -> dict:
    selection_lookup = load_selection_lookup()
    items = collect_items(MAIN_ASSETS_JSON, "main") + collect_items(SEO_ASSETS_JSON, "seo")
    for item in items:
        for image in item.get("image_plan", []):
            selection = selection_lookup.get((item.get("keyword", ""), image.get("slot", "")), {})
            if selection:
                image["selected_url"] = selection.get("selected_url", "")
                image["selected_credit"] = selection.get("selected_credit", "")
                image["approved"] = bool(selection.get("approved", False))
    return {
        "item_count": len(items),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Safe Image Suggestions")
    lines.append("")
    lines.append("저작권과 라이선스 기준으로 상대적으로 안전한 이미지 탐색 링크와 검색어를 자동 정리한 카드입니다.")
    lines.append("")
    for item in report.get("items", []):
        lines.append(f"## {item.get('title', '')}")
        lines.append("")
        lines.append(f"- source_group: `{item.get('source_group', '')}`")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- category: `{item.get('category', '')}`")
        for image in item.get("image_plan", []):
            lines.append(
                f"- {image.get('slot_label', image.get('slot', ''))}: {image.get('provider_name', '')} / query `{image.get('search_query', '')}` / search {image.get('search_url', '')}"
            )
            lines.append(f"- license: {image.get('license_label', '')} / {image.get('license_url', '')}")
            lines.append(f"- alt text: {image.get('alt_text', '')}")
            if image.get("selected_url"):
                lines.append(f"- selected_url: {image.get('selected_url', '')}")
                lines.append(f"- selected_credit: {image.get('selected_credit', '')}")
                lines.append(f"- approved: {image.get('approved', False)}")
        if item.get("image_usage_checklist"):
            lines.append(f"- usage checklist: {' / '.join(item.get('image_usage_checklist', []))}")
        if item.get("image_blocked_subjects"):
            lines.append(f"- blocked subjects: {' / '.join(item.get('image_blocked_subjects', []))}")
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
