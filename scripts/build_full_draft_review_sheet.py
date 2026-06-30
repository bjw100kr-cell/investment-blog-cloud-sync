#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
OUTPUT_JSON = ROOT / "outputs/latest/full-draft-review-sheet.json"
OUTPUT_MD = ROOT / "outputs/latest/full-draft-review-sheet.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def resolve_workspace_path(path_str: str) -> Path:
    path = Path(path_str)
    if path.exists():
        return path
    marker = "investment-blog-cloud-sync/"
    if marker in path_str:
        relative = path_str.split(marker, 1)[1]
        return ROOT / relative
    return path


def build_review_lookup() -> dict[str, dict]:
    payload = load_json(REVIEW_PACKET_JSON)
    return {item.get("keyword", ""): item for item in payload.get("items", []) if item.get("keyword")}


def read_text(path_str: str) -> str:
    if not path_str:
        return ""
    path = resolve_workspace_path(path_str)
    if not path.exists():
        return ""
    return path.read_text().strip()


def build_report() -> dict:
    shortlist_payload = load_json(USER_REVIEW_SHORTLIST_JSON)
    review_lookup = build_review_lookup()
    items = []

    for card in shortlist_payload.get("shortlist", []):
        keyword = card.get("keyword", "")
        review = review_lookup.get(keyword, {})
        draft_path = review.get("draft_path", "")
        items.append(
            {
                "keyword": keyword,
                "title": card.get("title", ""),
                "publish_date": card.get("publish_date", ""),
                "priority_score": card.get("priority_score", 0),
                "review_verdict": card.get("review_verdict", ""),
                "quality_status": card.get("quality_status", ""),
                "hero_image_selected": card.get("hero_image_selected", False),
                "ready_now": card.get("ready_now", False),
                "intent": card.get("intent", ""),
                "cta_focus": card.get("cta_focus", ""),
                "draft_path": draft_path,
                "html_path": review.get("html_path", ""),
                "review_score": review.get("review_score", 0),
                "review_warnings": review.get("review_warnings", []),
                "retention_cta_enabled": review.get("retention_cta_enabled", False),
                "retention_cta": review.get("retention_cta", {}),
                "image_slots": review.get("image_slots", []),
                "full_draft_text": read_text(draft_path),
            }
        )

    return {
        "item_count": len(items),
        "single_approval_command": shortlist_payload.get("single_approval_command", ""),
        "batch_approval_command": shortlist_payload.get("batch_approval_command", ""),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Full Draft Review Sheet")
    lines.append("")
    lines.append("사용자가 발행 전에 실제 초안 전문을 읽고 확인할 수 있도록 만든 검토 시트입니다.")
    lines.append("- 원칙: 이 시트에서 내용을 확인한 글만 사용자 최종 확인 대상으로 넘깁니다.")
    lines.append("- 상태: 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    if report.get("single_approval_command"):
        lines.append(f"- single confirmation: `{report.get('single_approval_command', '')}`")
    if report.get("batch_approval_command"):
        lines.append(f"- batch confirmation: `{report.get('batch_approval_command', '')}`")
    lines.append("")

    for index, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {index}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- publish_date: `{item.get('publish_date', '')}`")
        lines.append(f"- priority_score: `{item.get('priority_score', 0)}`")
        lines.append(f"- review_verdict: `{item.get('review_verdict', '')}` / score `{item.get('review_score', 0)}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- hero_image_selected: `{item.get('hero_image_selected', False)}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- intent: {item.get('intent', '')}")
        lines.append(f"- CTA focus: {item.get('cta_focus', '')}")
        if item.get("retention_cta_enabled"):
            retention_cta = item.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        lines.append(f"- draft_path: `{item.get('draft_path', '')}`")
        lines.append(f"- html_path: `{item.get('html_path', '')}`")
        if item.get("review_warnings"):
            lines.append(f"- review_warnings: {' / '.join(item.get('review_warnings', []))}")
        if item.get("image_slots"):
            for image in item.get("image_slots", []):
                lines.append(
                    f"- image {image.get('slot_label', image.get('slot', ''))}: {image.get('provider_name', '')} / `{image.get('search_query', '')}` / {image.get('license_label', '')}"
                )
        lines.append("")
        lines.append("### Draft Body")
        lines.append("")
        lines.append("```md")
        lines.append(item.get("full_draft_text", ""))
        lines.append("```")
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
