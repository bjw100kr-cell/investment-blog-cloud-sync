#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_PAGES_REPORT = ROOT / "outputs/latest/site-pages-report.json"
RULES_JSON = ROOT / "config/site_page_publish_rules.json"
OUTPUT_JSON = ROOT / "outputs/latest/site-page-publish-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/site-page-publish-plan.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_plan() -> dict:
    report = load_json(SITE_PAGES_REPORT)
    rules = load_json(RULES_JSON)
    priorities = rules.get("priority_by_slug", {})
    page_kinds = rules.get("recommended_page_kind", {})
    purposes = rules.get("purpose_by_slug", {})
    visibility = rules.get("visibility_by_kind", {})

    items = []
    for page in report.get("items", []):
        slug = page.get("slug", "")
        kind = page_kinds.get(slug, "support_page")
        items.append(
            {
                "slug": slug,
                "title": page.get("title", ""),
                "html_path": page.get("html_path", ""),
                "canonical_url": page.get("canonical_url", ""),
                "page_kind": kind,
                "visibility": visibility.get(kind, "public_recommended"),
                "purpose": purposes.get(slug, "운영 보조 페이지"),
                "priority_score": priorities.get(slug, 50),
            }
        )

    items.sort(key=lambda item: (-item["priority_score"], item["slug"]))
    for idx, item in enumerate(items, start=1):
        item["publish_sequence"] = idx

    return {
        "base_url": report.get("base_url", ""),
        "summary": {
            "page_count": len(items),
            "public_required_count": sum(1 for item in items if item["visibility"] == "public_required"),
        },
        "items": items,
    }


def write_markdown(plan: dict) -> None:
    lines = []
    lines.append("# 사이트 페이지 배포 플랜")
    lines.append("")
    lines.append(f"- 페이지 수: `{plan.get('summary', {}).get('page_count', 0)}`")
    lines.append(f"- 필수 공개 페이지 수: `{plan.get('summary', {}).get('public_required_count', 0)}`")
    lines.append("")
    for item in plan.get("items", []):
        lines.append(f"## {item['publish_sequence']}. {item['slug']}")
        lines.append("")
        lines.append(f"- 제목: {item['title']}")
        lines.append(f"- 종류: {item['page_kind']}")
        lines.append(f"- 공개 수준: {item['visibility']}")
        lines.append(f"- 목적: {item['purpose']}")
        lines.append(f"- canonical: {item['canonical_url']}")
        lines.append(f"- html: {item['html_path']}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    plan = build_plan()
    OUTPUT_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    write_markdown(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
