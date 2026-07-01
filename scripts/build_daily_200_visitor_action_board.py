#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VISITOR_PROOF_JSON = ROOT / "outputs/latest/visitor-proof-board.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
TRAFFIC_AMPLIFICATION_JSON = ROOT / "outputs/latest/traffic-amplification-plan.json"
PLATFORM_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
SEARCH_CONSOLE_CARD_JSON = ROOT / "outputs/latest/search-console-setup-card.json"
OUTPUT_JSON = ROOT / "outputs/latest/daily-200-visitor-action-board.json"
OUTPUT_MD = ROOT / "outputs/latest/daily-200-visitor-action-board.md"

TARGET_DAILY_VISITORS = 200


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def blogger_ready_count(platform_plan: dict) -> int:
    for channel in platform_plan.get("channels", []):
        if channel.get("name") == "blogger":
            return int(channel.get("ready_item_count", 0) or 0)
    return 0


def keyword_actions(keyword_board: dict) -> list[dict]:
    actions = []
    for item in keyword_board.get("query_watchlist", [])[:6]:
        queries = item.get("reader_search_queries") or [item.get("query", "")]
        actions.append(
            {
                "mapped_keyword": item.get("mapped_keyword", ""),
                "primary_query": queries[0] if queries else item.get("query", ""),
                "supporting_queries": queries[1:],
                "suggested_title": item.get("suggested_title", ""),
                "demand_signal_score": item.get("demand_signal_score", 0),
                "use_in": [
                    "title",
                    "first_h2",
                    "meta_description",
                    "internal_link_anchor",
                    "social_share_copy",
                ],
            }
        )
    return actions


def distribution_actions(traffic_plan: dict) -> list[dict]:
    actions = []
    for plan in traffic_plan.get("plans", []):
        checklist = plan.get("manual_execution_checklist", [])
        expected = sum(int(item.get("expected_visitors", 0) or 0) for item in checklist)
        actions.append(
            {
                "keyword": plan.get("keyword", ""),
                "title": plan.get("title", ""),
                "public_url": plan.get("public_url", ""),
                "manual_checklist_items": len(checklist),
                "expected_manual_visitors": expected,
                "first_channel": (checklist[0] or {}).get("channel", "") if checklist else "",
                "first_copy_variant": (checklist[0] or {}).get("copy_variant_to_use", "") if checklist else "",
            }
        )
    return actions


def build_board() -> dict:
    visitor = load_json(VISITOR_PROOF_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    traffic_plan = load_json(TRAFFIC_AMPLIFICATION_JSON)
    platform_plan = load_json(PLATFORM_PLAN_JSON)
    search_console = load_json(SEARCH_CONSOLE_CARD_JSON)

    actual = int(visitor.get("actual_verified_visitors", 0) or 0)
    gap = max(TARGET_DAILY_VISITORS - actual, 0)
    quality_ready = int(platform_plan.get("quality_ready_count", 0) or 0)
    ready_count = blogger_ready_count(platform_plan)
    manual_distribution_potential = sum(
        int(item.get("expected_manual_visitors", 0) or 0)
        for item in distribution_actions(traffic_plan)
    )
    distribution_action_items = distribution_actions(traffic_plan)

    measurement_missing = visitor.get("proof_status") == "measurement_missing"
    search_console_action = (
        search_console.get("next_action")
        or search_console.get("minimum_next_action")
        or search_console.get("minimum_action")
        or {}
    )

    if actual >= TARGET_DAILY_VISITORS:
        status = "target_verified"
    elif measurement_missing:
        status = "measurement_missing_keep_building"
    else:
        status = "traffic_gap_open"

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_daily_visitors": TARGET_DAILY_VISITORS,
        "status": status,
        "proof": {
            "proof_status": visitor.get("proof_status", ""),
            "actual_verified_visitors": actual,
            "gap_to_target": gap,
            "measurement_missing": measurement_missing,
        },
        "publishing_capacity": {
            "quality_ready_count": quality_ready,
            "blogger_ready_count": ready_count,
            "recommended_posts_next_run": min(3, ready_count),
            "rule": "품질 게이트 통과 글만 실행당 최대 3건",
        },
        "keyword_capture_actions": keyword_actions(keyword_board),
        "distribution_actions": distribution_action_items,
        "distribution_summary": {
            "planned_public_url_count": traffic_plan.get("planned_public_url_count", len(distribution_action_items)),
            "manual_checklist_item_count": sum(item.get("manual_checklist_items", 0) for item in distribution_action_items),
            "published_expansion_item_count": traffic_plan.get("published_expansion_item_count", 0),
        },
        "manual_distribution_potential_visitors": manual_distribution_potential,
        "measurement_action": {
            "required": measurement_missing,
            "action": search_console_action,
            "why": "200명 목표 달성 여부는 Search Console/GA4 실측 없이는 증명할 수 없습니다.",
        },
        "next_24h_operating_order": [
            "Search Console 속성 검증 또는 접근 권한 확인",
            "품질 통과 Blogger 후보를 최대 3건 게시 또는 업데이트",
            "공개 URL 전체의 수동 배포 체크리스트를 우선순위 순서대로 각 1회 실행",
            "reader_search_queries를 제목, 첫 소제목, 내부링크 앵커에 반영",
            "다음 실행에서 actual_verified_visitors와 top queries를 재확인",
        ],
    }


def write_markdown(board: dict) -> None:
    proof = board.get("proof", {})
    capacity = board.get("publishing_capacity", {})
    lines = [
        "# Daily 200 Visitor Action Board",
        "",
        f"- 생성 시각: `{board.get('generated_at', '')}`",
        f"- 목표: 하루 `{board.get('target_daily_visitors', 200)}`명",
        f"- 상태: `{board.get('status', '')}`",
        f"- 실측 방문자: `{proof.get('actual_verified_visitors', 0)}`",
        f"- 남은 갭: `{proof.get('gap_to_target', 0)}`",
        f"- 측정 누락: `{proof.get('measurement_missing', False)}`",
        "",
        "## 오늘 운영 상한",
        "",
        f"- 품질 통과 글: `{capacity.get('quality_ready_count', 0)}`",
        f"- Blogger 준비 글: `{capacity.get('blogger_ready_count', 0)}`",
        f"- 다음 실행 권장 게시 수: `{capacity.get('recommended_posts_next_run', 0)}`",
        f"- 규칙: {capacity.get('rule', '')}",
        "",
        "## 검색 유입용 키워드 표현",
        "",
    ]
    for item in board.get("keyword_capture_actions", []):
        lines.append(f"### {item.get('primary_query', '')}")
        lines.append("")
        lines.append(f"- mapped_keyword: `{item.get('mapped_keyword', '')}`")
        lines.append(f"- suggested_title: {item.get('suggested_title', '')}")
        if item.get("supporting_queries"):
            lines.append(f"- supporting_queries: {', '.join(item.get('supporting_queries', []))}")
        lines.append(f"- use_in: {', '.join(item.get('use_in', []))}")
        lines.append("")

    lines.append("## 공개 URL 배포 액션")
    lines.append("")
    distribution_summary = board.get("distribution_summary", {})
    lines.append(f"- 공개 URL 수: `{distribution_summary.get('planned_public_url_count', 0)}`")
    lines.append(f"- 수동 체크리스트 수: `{distribution_summary.get('manual_checklist_item_count', 0)}`")
    lines.append(f"- 공개 SEO 확장 글 수: `{distribution_summary.get('published_expansion_item_count', 0)}`")
    lines.append(f"- 전체 수동 배포 잠재 방문자: `{board.get('manual_distribution_potential_visitors', 0)}`")
    lines.append("")
    for item in board.get("distribution_actions", []):
        lines.append(f"- `{item.get('keyword', '')}`: {item.get('manual_checklist_items', 0)}개 체크 / 예상 {item.get('expected_manual_visitors', 0)}명 / 첫 채널 {item.get('first_channel', '')} / {item.get('public_url', '')}")
    lines.append("")
    lines.append("## 다음 24시간 순서")
    lines.append("")
    for action in board.get("next_24h_operating_order", []):
        lines.append(f"- {action}")
    lines.append("")

    measurement = board.get("measurement_action", {})
    lines.append("## 측정 액션")
    lines.append("")
    lines.append(f"- required: `{measurement.get('required', False)}`")
    lines.append(f"- why: {measurement.get('why', '')}")
    if measurement.get("action"):
        action = measurement.get("action")
        if isinstance(action, dict):
            label = action.get("label", "")
            open_url = action.get("open_url", "")
            property_value = action.get("property_value", "")
            lines.append(f"- action: `{label}`")
            if property_value:
                lines.append(f"- property_value: `{property_value}`")
            if open_url:
                lines.append(f"- open_url: {open_url}")
        else:
            lines.append(f"- action: `{action}`")
    lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    board = build_board()
    OUTPUT_JSON.write_text(json.dumps(board, ensure_ascii=False, indent=2))
    write_markdown(board)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
