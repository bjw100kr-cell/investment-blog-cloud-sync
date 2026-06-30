#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
SAFE_IMAGE_SUGGESTIONS_JSON = ROOT / "outputs/latest/safe-image-suggestions.json"
OUTPUT_JSON = ROOT / "outputs/latest/image-upgrade-queue.json"
OUTPUT_MD = ROOT / "outputs/latest/image-upgrade-queue.md"
IMAGE_HELPER = ROOT / "scripts/set_image_selection.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_image_lookup() -> dict[str, dict]:
    payload = load_json(SAFE_IMAGE_SUGGESTIONS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        hero = {}
        for image in item.get("image_plan", []):
            if image.get("slot") == "hero":
                hero = image
                break
        if not hero:
            continue
        lookup[keyword] = {
            "title": item.get("title", ""),
            "source_group": item.get("source_group", ""),
            "provider_name": hero.get("provider_name", ""),
            "search_query": hero.get("search_query", ""),
            "search_url": hero.get("search_url", ""),
            "license_label": hero.get("license_label", ""),
            "license_url": hero.get("license_url", ""),
            "selected_url": hero.get("selected_url", ""),
            "approved": bool(hero.get("approved", False)),
            "apply_helper": f'python3 {IMAGE_HELPER} --keyword {keyword} --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve',
        }
    return lookup


def build_queue() -> dict:
    quality = load_json(QUALITY_GATE_JSON)
    image_lookup = build_image_lookup()
    items = []
    for entry in quality.get("items", []):
        keyword = entry.get("keyword", "")
        if not keyword:
            continue
        checks = {check.get("name"): check for check in entry.get("checks", [])}
        hero_image_ok = bool((checks.get("hero_image_selected") or {}).get("ok"))
        high_fail = any((not check.get("ok")) and check.get("severity") == "high" for check in entry.get("checks", []))
        if entry.get("status") != "review_before_publish":
            continue
        if high_fail or hero_image_ok:
            continue
        image = image_lookup.get(keyword, {})
        if not image:
            continue
        items.append(
            {
                "keyword": keyword,
                "title": entry.get("title", ""),
                "source_group": entry.get("source_group", image.get("source_group", "")),
                "provider_name": image.get("provider_name", ""),
                "search_query": image.get("search_query", ""),
                "search_url": image.get("search_url", ""),
                "license_label": image.get("license_label", ""),
                "license_url": image.get("license_url", ""),
                "apply_helper": image.get("apply_helper", ""),
                "selected_url": image.get("selected_url", ""),
                "approved": image.get("approved", False),
                "upgrade_reason": "대표 이미지 1장만 선택하면 품질 게이트 pass에 더 가까워지는 글입니다.",
            }
        )

    items.sort(key=lambda item: (0 if item.get("source_group") == "main" else 1, item.get("keyword", "")))
    return {
        "item_count": len(items),
        "main_count": sum(1 for item in items if item.get("source_group") == "main"),
        "seo_count": sum(1 for item in items if item.get("source_group") == "seo"),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Image Upgrade Queue")
    lines.append("")
    lines.append("대표 이미지 하나만 보완하면 발행 준비 상태가 빠르게 올라가는 글만 따로 모은 큐입니다.")
    lines.append("")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    lines.append(f"- main_count: `{report.get('main_count', 0)}`")
    lines.append(f"- seo_count: `{report.get('seo_count', 0)}`")
    lines.append("")
    for item in report.get("items", []):
        lines.append(f"## {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- source_group: `{item.get('source_group', '')}`")
        lines.append(f"- reason: {item.get('upgrade_reason', '')}")
        lines.append(
            f"- next_image_search: {item.get('provider_name', '')} / query `{item.get('search_query', '')}` / {item.get('search_url', '')}"
        )
        lines.append(f"- next_image_license: {item.get('license_label', '')} / {item.get('license_url', '')}")
        lines.append(f"- next_image_apply_helper: `{item.get('apply_helper', '')}`")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_queue()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
