#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
IMAGE_SELECTIONS_JSON = ROOT / "outputs/latest/image-selections.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/approval-dashboard.json"
OUTPUT_MD = ROOT / "outputs/latest/approval-dashboard.md"
APPROVAL_HELPER = ROOT / "scripts/set_review_approvals.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def keyword_command(keywords: list[str]) -> str:
    filtered = [keyword for keyword in keywords if keyword]
    return f"python3 {APPROVAL_HELPER} --keywords {' '.join(filtered)}" if filtered else ""


def select_items(review_items: list[dict], predicate) -> list[dict]:
    return [item for item in review_items if predicate(item)]


def load_quality_lookup() -> dict[str, dict]:
    payload = load_json(QUALITY_GATE_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        hero_image_selected = False
        for check in item.get("checks", []):
            if check.get("name") == "hero_image_selected":
                hero_image_selected = bool(check.get("ok"))
                break
        lookup[keyword] = {
            "status": item.get("status", ""),
            "hero_image_selected": hero_image_selected,
        }
    return lookup


def load_image_selection_lookup() -> dict[str, bool]:
    payload = load_json(IMAGE_SELECTIONS_JSON)
    lookup: dict[str, bool] = {}
    for item in payload.get("items", []):
        if item.get("slot") != "hero":
            continue
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        lookup[keyword] = bool(item.get("approved")) and bool(item.get("selected_url"))
    return lookup


def load_freshness_lookup() -> dict[str, dict]:
    payload = load_json(FRESHNESS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        lookup[keyword] = {
            "freshness_status": item.get("freshness_status", ""),
            "newest_evidence_age_days": item.get("newest_evidence_age_days", ""),
        }
    return lookup


def sort_review_items(
    items: list[dict], quality_lookup: dict[str, dict], image_lookup: dict[str, bool], freshness_lookup: dict[str, dict]
) -> list[dict]:
    def sort_key(item: dict) -> tuple:
        keyword = item.get("keyword", "")
        quality = quality_lookup.get(keyword, {})
        freshness = freshness_lookup.get(keyword, {})
        quality_status = quality.get("status", "")
        hero_image_selected = bool(quality.get("hero_image_selected")) or image_lookup.get(keyword, False)
        freshness_rank = {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}.get(
            freshness.get("freshness_status", "unknown"), 2
        )
        quality_rank = 0 if quality_status == "pass" else 1 if quality_status == "review_before_publish" else 2
        image_rank = 0 if hero_image_selected else 1
        publish_date = item.get("recommended_publish_date", "9999-99-99")
        return (freshness_rank, quality_rank, image_rank, publish_date, -float(item.get("priority_score", 0)))

    return sorted(items, key=sort_key)


def summarize_items(items: list[dict]) -> list[dict]:
    return [
        {
            "keyword": item.get("keyword", ""),
            "title": item.get("title", ""),
            "publish_date": item.get("recommended_publish_date", ""),
            "priority": item.get("priority_score", 0),
            "inventory_type": item.get("inventory_type", ""),
            "role": item.get("role", ""),
            "quality_status": item.get("quality_status", ""),
            "hero_image_selected": item.get("hero_image_selected", False),
            "ready_now": item.get("ready_now", False),
            "freshness_status": item.get("freshness_status", ""),
        }
        for item in items
    ]


def build_dashboard() -> dict:
    review = load_json(REVIEW_PACKET_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    quality_lookup = load_quality_lookup()
    image_lookup = load_image_selection_lookup()
    freshness_lookup = load_freshness_lookup()
    review_items = review.get("items", [])
    queue_lookup = {item.get("keyword"): item for item in queue.get("items", [])}

    enriched_items = []
    for item in review_items:
        keyword = item.get("keyword", "")
        quality = quality_lookup.get(keyword, {})
        quality_status = quality.get("status", "")
        hero_image_selected = bool(quality.get("hero_image_selected")) or image_lookup.get(keyword, False)
        ready_now = quality_status == "pass" and hero_image_selected
        enriched = dict(item)
        enriched["quality_status"] = quality_status
        enriched["hero_image_selected"] = hero_image_selected
        enriched["ready_now"] = ready_now
        enriched["freshness_status"] = freshness_lookup.get(keyword, {}).get("freshness_status", "")
        enriched_items.append(enriched)

    main_posts = select_items(enriched_items, lambda item: item.get("inventory_type") == "main_post")
    due_soon = [
        item for item in main_posts
        if queue_lookup.get(item.get("keyword", ""), {}).get("publish_bucket") in {"today_or_overdue", "tomorrow"}
    ]
    big_tech_lane = select_items(
        enriched_items,
        lambda item: item.get("keyword") == "us_big_tech" or item.get("keyword", "").startswith("seo_us_big_tech_"),
    )
    macro_lane = select_items(
        enriched_items,
        lambda item: item.get("keyword") == "fomc" or item.get("keyword", "").startswith("seo_fomc_"),
    )
    crypto_lane = select_items(
        enriched_items,
        lambda item: item.get("keyword") == "bitcoin" or item.get("keyword", "").startswith("seo_bitcoin_"),
    )

    batches = [
        {
            "id": "due_soon_main",
            "label": "가장 먼저 볼 메인 글",
            "reason": "발행일이 오늘 또는 내일인 메인 글이며, 품질/이미지 준비가 된 글을 위로 올렸습니다.",
            "keywords": [item.get("keyword", "") for item in due_soon],
            "items": summarize_items(sort_review_items(due_soon, quality_lookup, image_lookup, freshness_lookup)),
        },
        {
            "id": "big_tech_lane",
            "label": "미국 빅테크 수익 라인",
            "reason": "메인 글 1개와 후속 SEO 글 3개를 묶어 미국 주식 검색 유입을 노립니다.",
            "keywords": [item.get("keyword", "") for item in big_tech_lane],
            "items": summarize_items(sort_review_items(big_tech_lane, quality_lookup, image_lookup, freshness_lookup)),
        },
        {
            "id": "macro_lane",
            "label": "거시 해설 라인",
            "reason": "FOMC 메인 글과 후속 설명형 글 묶음입니다.",
            "keywords": [item.get("keyword", "") for item in macro_lane],
            "items": summarize_items(sort_review_items(macro_lane, quality_lookup, image_lookup, freshness_lookup)),
        },
        {
            "id": "crypto_lane",
            "label": "코인 해설 라인",
            "reason": "비트코인 메인 글과 후속 검색형 글 묶음입니다.",
            "keywords": [item.get("keyword", "") for item in crypto_lane],
            "items": summarize_items(sort_review_items(crypto_lane, quality_lookup, image_lookup, freshness_lookup)),
        },
    ]

    for batch in batches:
        batch["approval_command"] = keyword_command(batch["keywords"])
        batch["confirmation_command"] = batch["approval_command"]
        batch["ready_now_count"] = sum(1 for item in batch.get("items", []) if item.get("ready_now"))

    return {
        "summary": {
            "review_item_count": len(enriched_items),
            "main_post_count": len(main_posts),
            "due_soon_main_count": len(due_soon),
            "big_tech_lane_count": len(big_tech_lane),
            "ready_now_count": sum(1 for item in enriched_items if item.get("ready_now")),
        },
        "batches": batches,
    }


def write_markdown(payload: dict) -> None:
    lines = [
        "# Approval Dashboard",
        "",
        "사용자가 긴 리뷰 패킷을 다 읽지 않아도, 먼저 최종 확인할 묶음을 고르기 쉽게 만든 운영 대시보드입니다.",
        "",
        f"- 전체 검토 대상: `{payload.get('summary', {}).get('review_item_count', 0)}`",
        f"- 메인 글 수: `{payload.get('summary', {}).get('main_post_count', 0)}`",
        f"- 곧 발행할 메인 글 수: `{payload.get('summary', {}).get('due_soon_main_count', 0)}`",
        f"- 미국 빅테크 라인 글 수: `{payload.get('summary', {}).get('big_tech_lane_count', 0)}`",
        f"- 지금 바로 발행 가까운 글 수: `{payload.get('summary', {}).get('ready_now_count', 0)}`",
        "- 원칙: 사용자 최종 확인 전에는 실제 업로드를 실행하지 않습니다.",
        "",
    ]

    for batch in payload.get("batches", []):
        lines.append(f"## {batch['label']}")
        lines.append("")
        lines.append(f"- reason: {batch['reason']}")
        lines.append(f"- ready_now_count: `{batch.get('ready_now_count', 0)}`")
        lines.append(f"- user confirmation command: `{batch['confirmation_command']}`")
        for item in batch.get("items", []):
            lines.append(
                f"- `{item['keyword']}` / {item['title']} / {item['inventory_type']} / {item['role']} / publish {item['publish_date'] or 'unscheduled'} / priority {item['priority']} / freshness `{item['freshness_status'] or 'unknown'}` / quality `{item['quality_status'] or 'unknown'}` / hero_image_selected `{item['hero_image_selected']}` / ready_now `{item['ready_now']}`"
            )
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    payload = build_dashboard()
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    write_markdown(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
