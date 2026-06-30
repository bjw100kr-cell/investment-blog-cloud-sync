#!/usr/bin/env python3
from typing import Optional
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
APPROVAL_DASHBOARD_JSON = ROOT / "outputs/latest/approval-dashboard.json"
PLATFORM_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
SAFE_IMAGE_SUGGESTIONS_JSON = ROOT / "outputs/latest/safe-image-suggestions.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
DAILY_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_MD = ROOT / "outputs/latest/first-approval-path.md"
APPROVAL_HELPER = ROOT / "scripts/set_review_approvals.py"
IMAGE_HELPER = ROOT / "scripts/set_image_selection.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_dashboard_item_lookup(batches: list[dict]) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for batch in batches:
        for item in batch.get("items", []):
            keyword = item.get("keyword", "")
            if keyword and keyword not in lookup:
                lookup[keyword] = item
    return lookup


def build_image_lookup() -> dict[str, dict]:
    payload = load_json(SAFE_IMAGE_SUGGESTIONS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        for image in item.get("image_plan", []):
            if image.get("slot") == "hero":
                lookup[keyword] = {
                    "provider_name": image.get("provider_name", ""),
                    "search_query": image.get("search_query", ""),
                    "search_url": image.get("search_url", ""),
                    "license_label": image.get("license_label", ""),
                    "license_url": image.get("license_url", ""),
                    "apply_helper": f'python3 {IMAGE_HELPER} --keyword {keyword} --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve',
                }
                break
    return lookup


def build_freshness_lookup() -> dict[str, dict]:
    payload = load_json(FRESHNESS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        lookup[keyword] = {
            "freshness_status": item.get("freshness_status", ""),
            "newest_evidence_age_days": item.get("newest_evidence_age_days", ""),
            "recommendation": item.get("recommendation", ""),
        }
    return lookup


def build_brand_lane_lookup() -> tuple[dict[str, str], dict[str, str]]:
    brief = load_json(DAILY_BRIEF_JSON)
    growth_rules = load_json(GROWTH_RULES_JSON)
    lane_labels = ((growth_rules.get("topic_mix_policy") or {}).get("brand_lane_labels") or {})
    lookup: dict[str, str] = {}
    for item in brief.get("top_briefs", []):
        keyword = item.get("keyword", "")
        lane = item.get("brand_lane", "")
        if keyword and lane:
            lookup[keyword] = lane
    fallback = {
        "fomc": "macro",
        "cpi": "macro",
        "pce": "macro",
        "jobs": "macro",
        "treasury_yields": "macro",
        "dollar": "macro",
        "oil": "macro",
        "bitcoin": "crypto",
        "ethereum": "crypto",
        "crypto_etf": "crypto",
        "ai_semiconductors": "us-stocks",
        "us_index_flow": "us-stocks",
        "us_big_tech": "us-stocks",
        "ai_growth_stocks": "us-stocks",
        "china": "world-flow",
        "tariffs_trade": "world-flow",
    }
    for keyword, lane in fallback.items():
        lookup.setdefault(keyword, lane)
    return lookup, lane_labels


def build_lane_preference_order() -> list[str]:
    rules = load_json(GROWTH_RULES_JSON)
    topic_mix = rules.get("topic_mix_policy") or {}
    fallback = ["macro", "us-stocks", "world-flow", "crypto"]
    if not isinstance(topic_mix, dict):
        return fallback
    order = topic_mix.get("top_brief_diversity_order") or []
    ordered: list[str] = [lane for lane in order if isinstance(lane, str)]
    for lane in fallback:
        if lane not in ordered:
            ordered.append(lane)
    return ordered[: len(fallback)]


def choose_primary_batch(batches: list[dict]) -> dict:
    ranked = sorted(
        batches,
        key=lambda item: (
            {"due_soon_main": 0, "macro_lane": 1, "crypto_lane": 2, "big_tech_lane": 3}.get(item.get("id"), 9),
            -sum(1 for candidate in item.get("items", []) if candidate.get("freshness_status") == "fresh"),
            -(item.get("ready_now_count", 0)),
            -sum(1 for candidate in item.get("items", []) if candidate.get("ready_now")),
        ),
    )
    for batch in ranked:
        if batch.get("items"):
            return batch
    return {}


def build_review_item_lookup(review_items: list[dict]) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for item in review_items:
        keyword = item.get("keyword", "")
        if keyword:
            lookup[keyword] = item
    return lookup


def infer_quality_status(item: dict) -> str:
    quality_status = item.get("quality_status", "")
    if quality_status:
        return quality_status
    verdict = item.get("review_verdict", "")
    return {"approve": "pass", "review_carefully": "review_before_publish", "revise": "needs_fix"}.get(verdict, "")


def queue_rank(queue_bucket: str) -> int:
    return {
        "today_or_overdue": 0,
        "tomorrow": 1,
        "this_week": 2,
        "later": 3,
        "ready_next_week": 4,
    }.get(queue_bucket, 9)


def freshness_rank(value: Optional[str]) -> int:
    return {"fresh": 0, "aging": 1, "unknown": 0, "": 0}.get(value or "", 2)


def enrich_for_selection(item: dict, freshness_lookup: dict[str, dict], review_lookup: dict[str, dict], brand_lane_lookup: dict[str, str]) -> dict:
    candidate = dict(item)
    keyword = item.get("keyword", "")
    review_item = review_lookup.get(keyword, {})
    freshness = freshness_lookup.get(keyword, {})
    candidate.setdefault("priority_score", review_item.get("priority_score", 0))
    candidate.setdefault("title", review_item.get("title", item.get("title", "")))
    candidate.setdefault("recommended_publish_date", review_item.get("recommended_publish_date", ""))
    candidate.setdefault("review_verdict", review_item.get("review_verdict", ""))
    candidate.setdefault("queue_bucket", review_item.get("queue_bucket", ""))
    candidate.setdefault("keyword", keyword)
    if freshness.get("freshness_status"):
        candidate["freshness_status"] = freshness.get("freshness_status")
    else:
        candidate["freshness_status"] = candidate.get("freshness_status", "unknown")
    candidate["quality_status"] = infer_quality_status(candidate)
    candidate.setdefault("hero_image_selected", False)
    candidate.setdefault("brand_lane", brand_lane_lookup.get(keyword, "macro"))
    return candidate


def select_actionable_batch(
    primary_batch: dict,
    freshness_lookup: dict[str, dict],
    brand_lane_lookup: dict[str, str],
) -> tuple[list[dict], list[dict], str]:
    items = list(primary_batch.get("items", []))
    if not items:
        return [], [], "추천 묶음을 만들 데이터가 아직 부족합니다."

    actionable = []
    deferred = []
    used_lanes: set[str] = set()

    ranked_items = sorted(
        items,
        key=lambda item: (
            freshness_rank(freshness_lookup.get(item.get("keyword", ""), {}).get("freshness_status", "unknown")),
            0 if item.get("quality_status") == "pass" else 1,
            0 if item.get("hero_image_selected") else 1,
            -float(item.get("priority", 0) or 0),
        ),
    )

    for item in ranked_items:
        keyword = item.get("keyword", "")
        freshness_status = freshness_lookup.get(keyword, {}).get("freshness_status", "unknown")
        lane = brand_lane_lookup.get(keyword, "macro")
        enriched = dict(item)
        enriched["brand_lane"] = lane
        if freshness_status == "stale":
            deferred.append(enriched)
            continue
        if lane in used_lanes:
            actionable.append(enriched)
            continue
        actionable.append(enriched)
        used_lanes.add(lane)

    reason = primary_batch.get("reason", "")
    if deferred:
        reason = f"{reason} 단, stale 글은 지금 승인 권장 묶음에서는 제외하고 보류 목록으로 분리했습니다.".strip()
    return actionable[:5], deferred[:5], reason


def choose_primary_item(
    review_items: list[dict],
    brand_lane_lookup: dict[str, str],
    freshness_lookup: dict[str, dict],
    review_lookup: dict[str, dict],
    primary_batch_items: Optional[list[dict]] = None,
    actionable_primary_batch_items: Optional[list[dict]] = None,
    lane_preference: Optional[list[str]] = None,
) -> dict:
    if not review_items:
        return {}

    batch_items = primary_batch_items or []
    batch_main = []
    for item in batch_items:
        keyword = item.get("keyword", "")
        if item.get("inventory_type", "").startswith("main_post") and keyword:
            batch_main.append(item)

    review_main = [item for item in review_items if item.get("inventory_type") == "main_post"]
    enriched_pool: list[dict] = []
    seen_keywords: set[str] = set()

    for item in batch_main + review_main:
        keyword = item.get("keyword", "")
        if not keyword or keyword in seen_keywords:
            continue
        enriched_pool.append(enrich_for_selection(item, freshness_lookup, review_lookup, brand_lane_lookup))
        seen_keywords.add(keyword)

    active_order = lane_preference or build_lane_preference_order()
    def select_key(item: dict) -> tuple:
        freshness_rank_value = freshness_rank(item.get("freshness_status"))
        quality_rank = {"pass": 0, "review_before_publish": 1, "needs_fix": 2}.get(item.get("quality_status", ""), 3)
        image_rank = 0 if item.get("hero_image_selected") else 1
        verdict_rank = {"approve": 0, "review_carefully": 1, "revise": 2}.get(item.get("review_verdict"), 3)
        publish_date = item.get("recommended_publish_date", "9999-99-99")
        return (
            freshness_rank_value,
            quality_rank,
            image_rank,
            queue_rank(item.get("queue_bucket", "")),
            verdict_rank,
            publish_date,
            -float(item.get("priority_score", 0)),
        )

    if actionable_primary_batch_items:
        actionable_candidates = [
            enrich_for_selection(item, freshness_lookup, review_lookup, brand_lane_lookup)
            for item in actionable_primary_batch_items
            if item.get("keyword")
        ]
        if actionable_candidates:
            return sorted(actionable_candidates, key=select_key)[0]

    non_stale_items = [item for item in enriched_pool if item.get("freshness_status", "unknown") != "stale"]
    candidate_pool = non_stale_items if non_stale_items else enriched_pool

    for lane in active_order:
        lane_candidates = [
            item
            for item in candidate_pool
            if item.get("keyword") and brand_lane_lookup.get(item.get("keyword", ""), "macro") == lane
        ]
        if lane_candidates:
            return sorted(lane_candidates, key=lambda item: (
                freshness_rank(item.get("freshness_status")),
                {"pass": 0, "review_before_publish": 1, "needs_fix": 2}.get(item.get("quality_status", ""), 3),
                0 if item.get("hero_image_selected") else 1,
                {"approve": 0, "review_carefully": 1, "revise": 2}.get(item.get("review_verdict"), 3),
                queue_rank(item.get("queue_bucket", "")),
                item.get("recommended_publish_date", "9999-99-99"),
                -float(item.get("priority_score", 0)),
            ))[0]

    fallback_pool = [enrich_for_selection(item, freshness_lookup, review_lookup, brand_lane_lookup) for item in review_items]
    return sorted(fallback_pool, key=select_key)[0]


def build_selection_basis(
    primary_item: dict,
    review_items: list[dict],
    dashboard_item_lookup: dict[str, dict],
    freshness_lookup: dict[str, dict],
    brand_lane_lookup: dict[str, str],
    lane_labels: dict[str, str],
    lane_preference: Optional[list[str]] = None,
) -> dict:
    keyword = primary_item.get("keyword", "")
    if not keyword:
        return {"summary": "", "comparison_notes": []}

    quality = dashboard_item_lookup.get(keyword, {})
    freshness_status = freshness_lookup.get(keyword, {}).get("freshness_status", "unknown")
    lane = brand_lane_lookup.get(keyword, "macro")
    lane_label = lane_labels.get(lane, lane)

    summary_parts = [
        f"`{keyword}`이 오늘 직접 발행 가능한 후보 중 가장 안전한 1순위입니다.",
        f"현재 브랜드 레인은 `{lane}` ({lane_label})이고 freshness는 `{freshness_status}`입니다.",
    ]
    if quality.get("quality_status") == "pass":
        summary_parts.append("품질 게이트가 통과 상태라 승인 후 업로드 경로가 가장 짧습니다.")
    if quality.get("hero_image_selected"):
        summary_parts.append("대표 이미지도 이미 선택되어 있어 추가 준비가 거의 없습니다.")
    if lane_preference:
        summary_parts.append(f"오늘 1순위 후보는 레인 우선순위 `{ ' > '.join(lane_preference) }` 기준에서 freshness와 검수 상태를 함께 반영해 고릅니다.")

    primary_priority = float(primary_item.get("priority_score", 0) or 0)
    comparison_notes: list[str] = []
    ranked_others = sorted(
        [item for item in review_items if item.get("keyword") and item.get("keyword") != keyword],
        key=lambda item: -float(item.get("priority_score", 0) or 0),
    )
    for item in ranked_others[:4]:
        other_keyword = item.get("keyword", "")
        other_freshness = freshness_lookup.get(other_keyword, {}).get("freshness_status", "unknown")
        other_quality = dashboard_item_lookup.get(other_keyword, {}).get("quality_status", "")
        other_lane = brand_lane_lookup.get(other_keyword, "macro")
        other_priority = float(item.get("priority_score", 0) or 0)
        if other_freshness == "stale":
            comparison_notes.append(
                f"`{other_keyword}`는 priority `{other_priority}`로 높지만 freshness가 `stale`라서 오늘 메인 직접 발행 후보에서 보류됐습니다."
            )
            continue
        if other_quality and other_quality != "pass":
            comparison_notes.append(
                f"`{other_keyword}`는 freshness는 괜찮아도 quality `{other_quality}` 상태라 바로 올리기보다 추가 검토가 먼저입니다."
            )
            continue
        if other_lane == lane and other_priority <= primary_priority:
            comparison_notes.append(
                f"`{other_keyword}`도 같은 `{other_lane}` 레인이지만 현재 점수와 발행 준비도 기준에서는 `{keyword}`가 앞섭니다."
            )
            continue
        if other_priority > primary_priority:
            comparison_notes.append(
                f"`{other_keyword}`는 priority는 더 높지만 현재 승인 경로 전체 기준에서는 `{keyword}`보다 직접 업로드 안전성이 낮습니다."
            )

    if not comparison_notes:
        comparison_notes.append("현재 shortlist 안에서는 이 글이 freshness와 발행 준비도 기준으로 가장 무난한 선택입니다.")

    return {
        "summary": " ".join(summary_parts),
        "comparison_notes": comparison_notes[:4],
    }


def build_report() -> dict:
    review = load_json(REVIEW_PACKET_JSON)
    dashboard = load_json(APPROVAL_DASHBOARD_JSON)
    platform_plan = load_json(PLATFORM_PLAN_JSON)
    setup = load_json(SETUP_JSON)

    review_items = review.get("items", [])
    batches = dashboard.get("batches", [])
    dashboard_item_lookup = build_dashboard_item_lookup(batches)
    review_lookup = build_review_item_lookup(review_items)
    image_lookup = build_image_lookup()
    freshness_lookup = build_freshness_lookup()
    brand_lane_lookup, lane_labels = build_brand_lane_lookup()

    for batch in batches:
        for item in batch.get("items", []):
            freshness = freshness_lookup.get(item.get("keyword", ""), {})
            item["freshness_status"] = freshness.get("freshness_status", "")

    for item in review_items:
        freshness = freshness_lookup.get(item.get("keyword", ""), {})
        item["freshness_status"] = freshness.get("freshness_status", "")
        item["freshness_recommendation"] = freshness.get("recommendation", "")
        item["quality_status"] = infer_quality_status(item)

    primary_batch = choose_primary_batch(batches)
    lane_preference = build_lane_preference_order()
    actionable_batch_items, deferred_batch_items, actionable_batch_reason = select_actionable_batch(primary_batch, freshness_lookup, brand_lane_lookup)
    primary_item = choose_primary_item(
        review_items,
        brand_lane_lookup,
        freshness_lookup,
        review_lookup,
        primary_batch.get("items", []),
        actionable_batch_items,
        lane_preference,
    )

    batch_keywords = [item.get("keyword", "") for item in actionable_batch_items if item.get("keyword")]
    single_keyword = primary_item.get("keyword", "")
    if single_keyword and single_keyword not in batch_keywords:
        single_item = enrich_for_selection(primary_item, freshness_lookup, review_lookup, brand_lane_lookup)
        actionable_batch_items = [single_item]
        deferred_batch_items = []
        batch_keywords = [single_keyword]
        actionable_batch_reason = (
            f"{primary_batch.get('label', '추천 묶음')}에서 단건 우선 기준으로 고른 `{single_keyword}`를 바로 확인할 수 있도록 "
            "묶음 승인 후보를 1건으로 재정렬했습니다."
        )

    selection_basis = build_selection_basis(
        primary_item,
        review_items,
        dashboard_item_lookup,
        freshness_lookup,
        brand_lane_lookup,
        lane_labels,
        lane_preference,
    )
    blogger_ready = any(
        item.get("name") == "blogger_upload" and item.get("ready")
        for item in setup.get("integrations", [])
    )

    batch_keywords = [item.get("keyword", "") for item in actionable_batch_items if item.get("keyword")]
    batch_approval_command = ""
    if batch_keywords:
        batch_approval_command = f"python3 {APPROVAL_HELPER} --keywords {' '.join(batch_keywords)}"

    single_keyword = primary_item.get("keyword", "")
    single_quality = dashboard_item_lookup.get(single_keyword, primary_item)
    single_image = image_lookup.get(single_keyword, {})
    single_freshness = freshness_lookup.get(single_keyword, {})
    single_approval_command = ""
    if single_keyword:
        single_approval_command = f"python3 {APPROVAL_HELPER} --keywords {single_keyword}"

    return {
        "blogger_ready": blogger_ready,
        "platform_primary_channel": platform_plan.get("primary_channel", "blogger"),
        "recommended_batch": {
            "id": primary_batch.get("id", ""),
            "label": primary_batch.get("label", ""),
            "reason": actionable_batch_reason,
            "keywords": batch_keywords,
            "approval_command": batch_approval_command,
            "item_count": len(actionable_batch_items),
            "ready_now_count": sum(1 for item in actionable_batch_items if item.get("ready_now")),
            "items": actionable_batch_items,
            "deferred_items": deferred_batch_items,
        },
        "recommended_single": {
            "keyword": primary_item.get("keyword", ""),
            "title": primary_item.get("title", ""),
            "publish_date": primary_item.get("recommended_publish_date", ""),
            "priority_score": primary_item.get("priority_score", 0),
            "review_verdict": primary_item.get("review_verdict", ""),
            "quality_status": single_quality.get("quality_status", ""),
            "freshness_status": single_freshness.get("freshness_status", ""),
            "freshness_recommendation": single_freshness.get("recommendation", ""),
            "hero_image_selected": single_quality.get("hero_image_selected", False),
            "hero_image_search_url": single_image.get("search_url", ""),
            "hero_image_search_query": single_image.get("search_query", ""),
            "hero_image_provider": single_image.get("provider_name", ""),
            "hero_image_license_label": single_image.get("license_label", ""),
            "hero_image_license_url": single_image.get("license_url", ""),
            "hero_image_apply_helper": single_image.get("apply_helper", ""),
            "brand_lane": brand_lane_lookup.get(single_keyword, "macro"),
            "brand_lane_label": lane_labels.get(brand_lane_lookup.get(single_keyword, "macro"), brand_lane_lookup.get(single_keyword, "macro")),
            "selection_summary": selection_basis.get("summary", ""),
            "comparison_notes": selection_basis.get("comparison_notes", []),
            "approval_command": single_approval_command,
        },
        "after_approval_commands": [
            "python3 scripts/build_platform_publish_plan.py",
            "python3 scripts/upload_blogger_drafts.py",
            "python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state",
        ],
    }


def write_markdown(report: dict) -> None:
    batch = report.get("recommended_batch", {})
    single = report.get("recommended_single", {})

    lines = []
    lines.append("# First Confirmation Path")
    lines.append("")
    lines.append("오늘 처음 사용자 최종 확인할 글을 고르는 가장 짧은 운영 경로입니다.")
    lines.append("")
    lines.append(f"- blogger_ready: `{report.get('blogger_ready', False)}`")
    lines.append(f"- platform_primary_channel: `{report.get('platform_primary_channel', 'blogger')}`")
    lines.append("- 원칙: 아래 글을 먼저 읽고 확인한 뒤에만 업로드 명령으로 넘어갑니다.")
    lines.append("")
    lines.append("## 추천 1순위 묶음")
    lines.append("")
    if batch.get("item_count", 0):
        lines.append(f"- label: `{batch.get('label', '')}`")
        lines.append(f"- reason: {batch.get('reason', '')}")
        lines.append(f"- item_count: `{batch.get('item_count', 0)}`")
        lines.append(f"- ready_now_count: `{batch.get('ready_now_count', 0)}`")
        if batch.get("approval_command"):
            lines.append(f"- user_confirmation_command: `{batch.get('approval_command', '')}`")
        else:
            lines.append("- user_confirmation_command: 지금 바로 권장할 묶음 승인 명령이 없습니다.")
        for item in batch.get("items", []):
            lines.append(
                f"- `{item.get('keyword', '')}` / {item.get('title', '')} / lane `{item.get('brand_lane', '')}` / publish {item.get('publish_date', '') or 'unscheduled'} / priority {item.get('priority', 0)} / freshness `{item.get('freshness_status', '')}` / quality `{item.get('quality_status', '')}` / hero_image_selected `{item.get('hero_image_selected', False)}`"
            )
        if batch.get("deferred_items"):
            lines.append("- deferred_due_to_freshness:")
            for item in batch.get("deferred_items", []):
                lines.append(
                    f"  - `{item.get('keyword', '')}` / {item.get('title', '')} / lane `{item.get('brand_lane', '')}` / freshness `{item.get('freshness_status', '')}`"
                )
    else:
        lines.append("- 아직 추천 묶음을 만들 데이터가 부족합니다.")
    lines.append("")
    lines.append("## 가장 먼저 단건 확인할 글")
    lines.append("")
    if single.get("keyword"):
        lines.append(f"- keyword: `{single.get('keyword', '')}`")
        lines.append(f"- title: `{single.get('title', '')}`")
        lines.append(f"- brand_lane: `{single.get('brand_lane', '')}` ({single.get('brand_lane_label', '')})")
        lines.append(f"- publish_date: `{single.get('publish_date', '') or 'unscheduled'}`")
        lines.append(f"- review_verdict: `{single.get('review_verdict', '')}`")
        lines.append(f"- priority_score: `{single.get('priority_score', 0)}`")
        lines.append(f"- freshness_status: `{single.get('freshness_status', '')}`")
        lines.append(f"- quality_status: `{single.get('quality_status', '')}`")
        if single.get("freshness_recommendation"):
            lines.append(f"- freshness_recommendation: {single.get('freshness_recommendation', '')}")
        lines.append(f"- hero_image_selected: `{single.get('hero_image_selected', False)}`")
        if not single.get("hero_image_selected") and single.get("hero_image_search_url"):
            lines.append(
                f"- next_image_search: {single.get('hero_image_provider', '')} / query `{single.get('hero_image_search_query', '')}` / {single.get('hero_image_search_url', '')}"
            )
            lines.append(
                f"- next_image_license: {single.get('hero_image_license_label', '')} / {single.get('hero_image_license_url', '')}"
            )
            lines.append(f"- next_image_apply_helper: `{single.get('hero_image_apply_helper', '')}`")
        if single.get("selection_summary"):
            lines.append(f"- selection_summary: {single.get('selection_summary', '')}")
        if single.get("comparison_notes"):
            lines.append("- why_not_other_topics:")
            for note in single.get("comparison_notes", []):
                lines.append(f"  - {note}")
        lines.append(f"- user_confirmation_command: `{single.get('approval_command', '')}`")
    else:
        lines.append("- 아직 단건 추천 글이 없습니다.")
    lines.append("")
    lines.append("## 사용자 확인 후 바로 실행")
    lines.append("")
    for command in report.get("after_approval_commands", []):
        lines.append(f"- `{command}`")
    lines.append("")
    lines.append("## 운영 메모")
    lines.append("")
    lines.append("- 첫 실전 검증은 `Blogger`만 봅니다.")
    lines.append("- WordPress는 이 승인 경로가 안정화된 뒤 두 번째 자동 채널로 붙입니다.")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
