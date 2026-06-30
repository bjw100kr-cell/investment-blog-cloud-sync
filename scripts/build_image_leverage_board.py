#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_UPGRADE_QUEUE_JSON = ROOT / "outputs/latest/image-upgrade-queue.json"
APPROVAL_DASHBOARD_JSON = ROOT / "outputs/latest/approval-dashboard.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
KEYWORD_CAPTURE_STRATEGY_JSON = ROOT / "outputs/latest/keyword-capture-strategy.json"
OUTPUT_JSON = ROOT / "outputs/latest/image-leverage-board.json"
OUTPUT_MD = ROOT / "outputs/latest/image-leverage-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def lane_key(keyword: str) -> str:
    if keyword.startswith("seo_bitcoin_") or keyword == "bitcoin":
        return "bitcoin"
    if keyword.startswith("seo_fomc_") or keyword == "fomc":
        return "fomc"
    if keyword.startswith("seo_us_big_tech_") or keyword == "us_big_tech":
        return "us_big_tech"
    if keyword == "cpi":
        return "cpi"
    return keyword


def lane_label(key: str) -> str:
    return {
        "bitcoin": "비트코인 해설 라인",
        "fomc": "FOMC 해설 라인",
        "us_big_tech": "미국 빅테크 라인",
        "cpi": "CPI 해설 라인",
    }.get(key, key)


def build_capture_lookup() -> dict[str, dict]:
    payload = load_json(KEYWORD_CAPTURE_STRATEGY_JSON)
    lookup = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if keyword:
            lookup[keyword] = item
    return lookup


def build_dashboard_lookup() -> dict[str, dict]:
    payload = load_json(APPROVAL_DASHBOARD_JSON)
    lookup = {}
    for batch in payload.get("batches", []):
        for item in batch.get("items", []):
            keyword = item.get("keyword", "")
            if keyword and keyword not in lookup:
                lookup[keyword] = item
    return lookup


def build_revenue_lookup() -> dict[str, dict]:
    payload = load_json(DAILY_REVENUE_FOCUS_JSON)
    lookup = {}
    for item in payload.get("today_path", []):
        keyword = item.get("keyword", "")
        if keyword and keyword not in lookup:
            lookup[keyword] = item
    return lookup


def build_report() -> dict:
    queue = load_json(IMAGE_UPGRADE_QUEUE_JSON)
    capture_lookup = build_capture_lookup()
    dashboard_lookup = build_dashboard_lookup()
    revenue_lookup = build_revenue_lookup()

    grouped: dict[str, dict] = {}
    for item in queue.get("items", []):
        key = lane_key(item.get("keyword", ""))
        lane = grouped.setdefault(
            key,
            {
                "lane_key": key,
                "lane_label": lane_label(key),
                "main_count": 0,
                "seo_count": 0,
                "items": [],
                "provider_names": set(),
                "queries": set(),
                "revenue_hit": False,
                "demand_signal_score": 0,
                "capture_route": "",
            },
        )
        lane["items"].append(item)
        lane["provider_names"].add(item.get("provider_name", ""))
        lane["queries"].add(item.get("search_query", ""))
        if item.get("source_group") == "main":
            lane["main_count"] += 1
        else:
            lane["seo_count"] += 1

        if revenue_lookup.get(key) or revenue_lookup.get(item.get("keyword", "")):
            lane["revenue_hit"] = True

        capture = capture_lookup.get(key, {})
        lane["demand_signal_score"] = max(lane["demand_signal_score"], int(capture.get("demand_signal_score", 0) or 0))
        if capture.get("capture_route") and not lane["capture_route"]:
            lane["capture_route"] = capture.get("capture_route", "")

    lanes = []
    for lane in grouped.values():
        lane["provider_names"] = [name for name in sorted(lane["provider_names"]) if name]
        lane["queries"] = [query for query in sorted(lane["queries"]) if query]
        lane["unlock_count"] = lane["main_count"] + lane["seo_count"]
        lane["leverage_score"] = (
            lane["unlock_count"] * 100
            + lane["main_count"] * 30
            + (40 if lane["revenue_hit"] else 0)
            + min(lane["demand_signal_score"], 9999) // 100
        )
        lane["top_items"] = lane["items"][:4]
        lane["why_now"] = (
            "메인 글과 후속 글을 함께 밀어 올릴 수 있는 라인입니다."
            if lane["main_count"] and lane["seo_count"]
            else "메인 글 발행 준비를 빠르게 한 단계 끌어올릴 수 있습니다."
            if lane["main_count"]
            else "후속 SEO 글 묶음을 한 번에 정리하기 좋은 라인입니다."
        )
        lanes.append(lane)

    lanes.sort(key=lambda item: (-item["leverage_score"], -item["unlock_count"], item["lane_key"]))
    return {
        "lane_count": len(lanes),
        "lanes": lanes,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Image Leverage Board")
    lines.append("")
    lines.append("어느 라인에 이미지를 먼저 보완해야 ready 후보 수가 가장 빨리 늘어나는지 묶음 기준으로 보여주는 보드입니다.")
    lines.append("")
    lines.append(f"- lane_count: `{report.get('lane_count', 0)}`")
    lines.append("")
    for lane in report.get("lanes", []):
        lines.append(f"## {lane.get('lane_label', '')}")
        lines.append("")
        lines.append(f"- lane_key: `{lane.get('lane_key', '')}`")
        lines.append(f"- unlock_count: `{lane.get('unlock_count', 0)}`")
        lines.append(f"- main_count: `{lane.get('main_count', 0)}`")
        lines.append(f"- seo_count: `{lane.get('seo_count', 0)}`")
        lines.append(f"- leverage_score: `{lane.get('leverage_score', 0)}`")
        lines.append(f"- revenue_hit: `{lane.get('revenue_hit', False)}`")
        if lane.get("capture_route"):
            lines.append(f"- capture_route: `{lane.get('capture_route', '')}`")
        if lane.get("provider_names"):
            lines.append(f"- providers: {', '.join(lane.get('provider_names', []))}")
        if lane.get("queries"):
            lines.append(f"- shared_queries: {' / '.join(lane.get('queries', []))}")
        lines.append(f"- why_now: {lane.get('why_now', '')}")
        for item in lane.get("top_items", []):
            lines.append(
                f"- `{item.get('keyword', '')}` / {item.get('title', '')} / {item.get('source_group', '')} / {item.get('provider_name', '')}"
            )
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
