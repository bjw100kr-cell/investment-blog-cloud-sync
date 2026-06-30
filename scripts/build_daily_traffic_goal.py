#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
SEARCH_DEMAND_JSON = ROOT / "outputs/latest/search-demand-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/daily-traffic-goal.json"
OUTPUT_MD = ROOT / "outputs/latest/daily-traffic-goal.md"


TARGET_DAILY_VISITORS = 200


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def quality_lookup(report: dict) -> dict:
    return {item.get("keyword"): item for item in report.get("items", []) if item.get("keyword")}


def queue_lookup(report: dict) -> dict:
    return {item.get("keyword"): item for item in report.get("items", []) if item.get("keyword")}


def estimate_daily_visitors(item: dict, queue_item: dict, quality_item: dict) -> int:
    if not queue_item.get("ready_to_upload") or quality_item.get("status") != "pass":
        return 0
    demand = int(item.get("demand_signal_score", 0) or 0)
    total = float(item.get("total_score", 0) or 0)
    base = 8
    demand_component = min(demand // 120, 55)
    score_component = min(int(total // 4), 25)
    readiness_component = 15
    quality_component = 12
    lane_component = 8 if item.get("brand_lane") in {"crypto", "macro", "us-stocks"} else 4
    estimate = base + demand_component + score_component + readiness_component + quality_component + lane_component
    return max(0, min(int(estimate), 95))


def build_report() -> dict:
    daily = load_json(DAILY_BRIEF_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    publish_plan = load_json(PUBLISH_PLAN_JSON)
    quality = load_json(QUALITY_GATE_JSON)
    monetization = load_json(MONETIZATION_JSON)
    demand = load_json(SEARCH_DEMAND_JSON)

    q_lookup = queue_lookup(queue)
    gate_lookup = quality_lookup(quality)
    topic_items = []
    for item in daily.get("top_briefs", []):
        queue_item = q_lookup.get(item.get("keyword"), {})
        quality_item = gate_lookup.get(item.get("keyword"), {})
        estimate = estimate_daily_visitors(item, queue_item, quality_item)
        topic_items.append(
            {
                "keyword": item.get("keyword", ""),
                "brand_lane": item.get("brand_lane", ""),
                "title": (item.get("title_candidates") or [""])[0],
                "demand_signal_score": item.get("demand_signal_score", 0),
                "total_score": item.get("total_score", 0),
                "quality_status": quality_item.get("status", "unknown"),
                "ready_to_upload": bool(queue_item.get("ready_to_upload")),
                "estimated_daily_visitors": estimate,
                "recommended_action": build_topic_action(item, queue_item, quality_item),
            }
        )

    topic_items.sort(key=lambda row: (-row["estimated_daily_visitors"], -float(row.get("total_score", 0)), row["keyword"]))
    ready_path = [item for item in topic_items if item["estimated_daily_visitors"] > 0]
    top_path = ready_path[:4]
    projected_visitors = sum(item["estimated_daily_visitors"] for item in top_path)
    gap = max(TARGET_DAILY_VISITORS - projected_visitors, 0)
    publish_channels = publish_plan.get("channels", [])
    blogger = next((channel for channel in publish_channels if channel.get("name") == "blogger"), {})
    stages = monetization.get("stages", [])
    analytics_ready = next((stage for stage in stages if stage.get("name") == "analytics_stack"), {}).get("ready", False)
    retention_ready = next((stage for stage in stages if stage.get("name") == "retention_stack"), {}).get("ready", False)

    bottlenecks = []
    if gap:
        bottlenecks.append(f"상위 4개 글 예상 합계가 {projected_visitors}명으로 목표보다 {gap}명 부족합니다.")
    if not analytics_ready:
        bottlenecks.append("GA4/Search Console 연결 전이라 실제 200명 달성 여부를 자동 측정하기 어렵습니다.")
    if not retention_ready:
        bottlenecks.append("뉴스레터/텔레그램 재방문 동선이 없어 첫 방문자를 반복 방문으로 쌓기 어렵습니다.")
    if blogger.get("ready_item_count", 0) < 1:
        bottlenecks.append("오늘 바로 발행할 Blogger ready item이 없습니다.")
    if quality.get("summary", {}).get("needs_fix_count", 0):
        bottlenecks.append("품질 게이트 needs_fix 글이 있어 발행 후보가 줄어듭니다.")

    next_actions = [
        "오늘은 예상 방문자 기여도가 가장 큰 1개 글을 먼저 발행하고, 같은 클러스터 후속 글 2개를 내부링크로 묶습니다.",
        "검색 수요 점수 3,000 이상 키워드는 메인 해설 1개 + 초보자/FAQ/ETF·규제 후속 글로 묶어 체류시간을 늘립니다.",
        "GA4_MEASUREMENT_ID와 SEARCH_CONSOLE_SITE_URL을 연결하면 200명/일 달성 여부를 추정이 아니라 실제 지표로 전환합니다.",
    ]
    if gap:
        next_actions.insert(1, "부족분은 evergreen 후속 글보다 당일 이슈형 제목을 1개 더 만들어 보강합니다.")

    return {
        "generated_at": daily.get("generated_at", ""),
        "target_daily_visitors": TARGET_DAILY_VISITORS,
        "projected_daily_visitors": projected_visitors,
        "gap_to_target": gap,
        "status": build_status(projected_visitors, analytics_ready),
        "top_path": top_path,
        "topic_items": topic_items,
        "ready_topic_count": len(ready_path),
        "search_demand_summary": demand.get("summary", {}),
        "keyword_board_summary": {
            "breaking_candidates": len(keyword_board.get("breaking_candidates", [])),
            "query_watchlist": len(keyword_board.get("query_watchlist", [])),
        },
        "publishing_summary": {
            "blogger_ready": bool(blogger.get("ready")),
            "blogger_ready_item_count": blogger.get("ready_item_count", 0),
            "daily_publish_cap": 1,
        },
        "measurement_summary": {
            "analytics_ready": bool(analytics_ready),
            "retention_ready": bool(retention_ready),
        },
        "bottlenecks": bottlenecks,
        "next_actions": next_actions,
    }


def build_topic_action(item: dict, queue_item: dict, quality_item: dict) -> str:
    if quality_item.get("status") == "needs_fix":
        return "품질 게이트 수정 후 발행 후보로 복귀"
    if not queue_item.get("ready_to_upload"):
        return "발행 가능한 manifest/이미지/신선도 상태 보강"
    if item.get("brand_lane") == "crypto":
        return "코인 시장 신호와 ETF/규제 후속 글을 내부링크로 묶어 발행"
    if item.get("brand_lane") == "macro":
        return "금리·달러·주식·코인 영향까지 한 번에 설명하는 evergreen 허브로 연결"
    if item.get("brand_lane") == "us-stocks":
        return "대표 종목/실적/지수 흐름 후속 글로 페이지뷰 확장"
    return "세계 흐름 해설 뒤 관련 섹터/환율 글로 연결"


def build_status(projected_visitors: int, analytics_ready: bool) -> str:
    if projected_visitors < TARGET_DAILY_VISITORS:
        return "needs_more_distribution"
    if not analytics_ready:
        return "estimated_on_track_measurement_missing"
    return "measured_on_track"


def write_markdown(report: dict) -> None:
    lines = [
        "# Daily Traffic Goal",
        "",
        f"- 목표: 하루 최소 `{report['target_daily_visitors']}`명 방문",
        f"- 현재 예상 합계: `{report['projected_daily_visitors']}`명",
        f"- 목표까지 부족분: `{report['gap_to_target']}`명",
        f"- 상태: `{report['status']}`",
        "",
        "## 200명 목표를 위한 오늘의 글 경로",
        "",
    ]
    for idx, item in enumerate(report.get("top_path", []), start=1):
        lines.append(
            f"{idx}. `{item['keyword']}` {item['title']} "
            f"/ 예상 `{item['estimated_daily_visitors']}`명 "
            f"/ 수요 `{item['demand_signal_score']}` "
            f"/ 품질 `{item['quality_status']}`"
        )
        lines.append(f"   - action: {item['recommended_action']}")
    lines.extend(["", "## 병목", ""])
    for item in report.get("bottlenecks", []):
        lines.append(f"- {item}")
    if not report.get("bottlenecks"):
        lines.append("- 현재 200명 목표 기준 큰 병목은 없습니다. 실제 측정 연결이 다음 우선순위입니다.")
    lines.extend(["", "## 다음 액션", ""])
    for item in report.get("next_actions", []):
        lines.append(f"- {item}")
    lines.extend(["", "## 후보 전체", ""])
    for item in report.get("topic_items", []):
        lines.append(
            f"- `{item['keyword']}` lane `{item['brand_lane']}` / 예상 `{item['estimated_daily_visitors']}`명 / ready `{item['ready_to_upload']}` / quality `{item['quality_status']}`"
        )
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    if not ready_path:
        bottlenecks.append("발행 준비와 품질 통과를 동시에 만족하는 트래픽 후보가 없습니다.")
