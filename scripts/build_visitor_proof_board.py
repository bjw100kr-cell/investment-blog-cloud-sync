#!/usr/bin/env python3
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH_CONSOLE_CSV = ROOT / "data/search_console_queries.csv"
SEARCH_CONSOLE_FETCH_JSON = ROOT / "outputs/latest/search-console-fetch-report.json"
SEARCH_CONSOLE_CONVERSION_JSON = ROOT / "outputs/latest/search-console-conversion-report.json"
PERFORMANCE_FEEDBACK_JSON = ROOT / "outputs/latest/performance-feedback.json"
DAILY_TRAFFIC_GOAL_JSON = ROOT / "outputs/latest/daily-traffic-goal.json"
TRAFFIC_AMPLIFICATION_PLAN_JSON = ROOT / "outputs/latest/traffic-amplification-plan.json"
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/visitor-proof-board.json"
OUTPUT_MD = ROOT / "outputs/latest/visitor-proof-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def sum_search_console_rows(path: Path) -> dict:
    if not path.exists():
        return {"clicks": 0, "impressions": 0, "top_queries": []}

    clicks = 0.0
    impressions = 0.0
    top_queries = []
    with path.open(newline="") as fp:
        for row in csv.DictReader(fp):
            row_clicks = float(row.get("clicks") or 0)
            row_impressions = float(row.get("impressions") or 0)
            clicks += row_clicks
            impressions += row_impressions
            top_queries.append(
                {
                    "query": row.get("query", ""),
                    "clicks": row_clicks,
                    "impressions": row_impressions,
                    "position": float(row.get("position") or 0),
                }
            )

    top_queries.sort(key=lambda item: (item["clicks"], item["impressions"]), reverse=True)
    return {
        "clicks": int(round(clicks)),
        "impressions": int(round(impressions)),
        "top_queries": top_queries[:10],
    }


def build_measurement_blockers(fetch_report: dict, setup: dict) -> list[str]:
    blockers = []
    if not fetch_report.get("available", False):
        reason = fetch_report.get("reason", "Search Console 데이터를 가져오지 못했습니다.")
        blockers.append(f"Search Console 실측 데이터 없음: {reason}")
        if fetch_report.get("accessible_sites") == [] and not fetch_report.get("accessible_sites_error"):
            blockers.append("Search Console 접근 가능 사이트가 0개입니다. 블로그 속성 등록/검증 또는 계정 권한 연결이 필요합니다.")
        if fetch_report.get("accessible_sites_error"):
            blockers.append(f"Search Console 사이트 목록 조회 실패: {fetch_report.get('accessible_sites_error')}")

    integrations = integration_lookup(setup)
    if not integrations.get("search_console", {}).get("ready", False):
        missing = ", ".join(integrations.get("search_console", {}).get("missing", []))
        if missing:
            blockers.append(f"Search Console 설정 미완료: {missing}")
    if not integrations.get("ga4", {}).get("ready", False):
        missing = ", ".join(integrations.get("ga4", {}).get("missing", []))
        if missing:
            blockers.append(f"GA4 설정 미완료: {missing}")
    return blockers


def build_next_actions(proof_status: str, blockers: list[str]) -> list[str]:
    if proof_status == "verified_achieved":
        return [
            "200명/일 이상을 만든 키워드와 글 구조를 다음 7일 편성표에 반복 적용합니다.",
            "Search Console 상위 쿼리를 내부링크와 후속 글 제목에 재사용합니다.",
        ]
    if proof_status == "measurement_connected_below_target":
        return [
            "클릭이 발생한 쿼리를 제목 첫머리와 H2에 반영해 같은 주제의 후속 글을 만듭니다.",
            "노출은 있으나 클릭률이 낮은 쿼리는 제목을 질문형/비교형으로 다시 테스트합니다.",
        ]
    actions = [
        "GitHub Actions secrets에 Search Console OAuth 값과 사이트 속성 URL을 연결해 실측 클릭을 가져옵니다.",
        "Search Console에서 `https://gimu-economy-insight.blogspot.com/` 속성을 같은 Google 계정으로 등록/검증합니다.",
        "GA4 측정 ID를 연결해 검색 외 직접/재방문 트래픽까지 확인합니다.",
        "그 전까지는 projected 값과 Blogger 공개 URL 기준 확산 계획을 참고하되, 목표 달성 증거로 보지는 않습니다.",
    ]
    if blockers:
        actions.append("측정 연결 후 이 보드에서 `proof_status=verified_achieved`가 나와야 목표 달성으로 판단합니다.")
    return actions


def build_report() -> dict:
    fetch_report = load_json(SEARCH_CONSOLE_FETCH_JSON)
    conversion_report = load_json(SEARCH_CONSOLE_CONVERSION_JSON)
    performance_feedback = load_json(PERFORMANCE_FEEDBACK_JSON)
    traffic_goal = load_json(DAILY_TRAFFIC_GOAL_JSON)
    amplification = load_json(TRAFFIC_AMPLIFICATION_PLAN_JSON)
    setup = load_json(SETUP_JSON)
    actual = sum_search_console_rows(SEARCH_CONSOLE_CSV) if fetch_report.get("available", False) else {"clicks": 0, "impressions": 0, "top_queries": []}

    target = int(traffic_goal.get("target_daily_visitors", amplification.get("target_daily_visitors", 200)) or 200)
    verified_clicks = int(actual.get("clicks", 0))
    verified_impressions = int(actual.get("impressions", 0))
    if fetch_report.get("available", False) and verified_clicks >= target:
        proof_status = "verified_achieved"
    elif fetch_report.get("available", False):
        proof_status = "measurement_connected_below_target"
    else:
        proof_status = "measurement_missing"

    blockers = build_measurement_blockers(fetch_report, setup)
    projected = int(traffic_goal.get("projected_daily_visitors", 0) or 0)
    projected_with_amplification = int(amplification.get("projected_with_amplification", projected) or projected)
    potential_with_manual_amplification = int(amplification.get("potential_with_manual_amplification", projected_with_amplification) or projected_with_amplification)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_daily_visitors": target,
        "actual_verified_visitors": verified_clicks,
        "actual_verified_impressions": verified_impressions,
        "gap_to_verified_target": max(0, target - verified_clicks),
        "proof_status": proof_status,
        "evidence_window": {
            "start_date": fetch_report.get("start_date", ""),
            "end_date": fetch_report.get("end_date", ""),
            "source": "Google Search Console query clicks",
            "site_url": fetch_report.get("site_url", ""),
            "site_url_source": fetch_report.get("site_url_source", ""),
        },
        "measurement": {
            "search_console_fetch": fetch_report,
            "search_console_conversion": conversion_report,
            "performance_feedback_available": performance_feedback.get("available", False),
            "blockers": blockers,
        },
        "projection_summary": {
            "projected_daily_visitors": projected,
            "projected_with_amplification": projected_with_amplification,
            "potential_with_manual_amplification": potential_with_manual_amplification,
            "projection_is_proof": False,
            "traffic_goal_status": traffic_goal.get("status", ""),
            "amplification_status": amplification.get("status", ""),
        },
        "top_verified_queries": actual.get("top_queries", []),
        "next_actions": build_next_actions(proof_status, blockers),
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Visitor Proof Board")
    lines.append("")
    lines.append("하루 200명 목표를 `예상`이 아니라 `실측 증거`로 확인하기 위한 보드입니다.")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(f"- proof_status: `{report.get('proof_status', '')}`")
    lines.append(f"- target_daily_visitors: `{report.get('target_daily_visitors', 200)}`")
    lines.append(f"- actual_verified_visitors: `{report.get('actual_verified_visitors', 0)}`")
    lines.append(f"- actual_verified_impressions: `{report.get('actual_verified_impressions', 0)}`")
    lines.append(f"- gap_to_verified_target: `{report.get('gap_to_verified_target', 0)}`")
    lines.append("")
    lines.append("## Evidence Window")
    lines.append("")
    evidence = report.get("evidence_window", {})
    lines.append(f"- source: `{evidence.get('source', '')}`")
    lines.append(f"- site_url: `{evidence.get('site_url', '')}`")
    lines.append(f"- site_url_source: `{evidence.get('site_url_source', '')}`")
    lines.append(f"- start_date: `{evidence.get('start_date', '')}`")
    lines.append(f"- end_date: `{evidence.get('end_date', '')}`")
    lines.append("")
    lines.append("## Projection Is Not Proof")
    lines.append("")
    projection = report.get("projection_summary", {})
    lines.append(f"- projected_daily_visitors: `{projection.get('projected_daily_visitors', 0)}`")
    lines.append(f"- projected_with_amplification: `{projection.get('projected_with_amplification', 0)}`")
    lines.append(f"- potential_with_manual_amplification: `{projection.get('potential_with_manual_amplification', 0)}`")
    lines.append(f"- projection_is_proof: `{projection.get('projection_is_proof', False)}`")
    lines.append("")
    lines.append("## Measurement Blockers")
    lines.append("")
    blockers = report.get("measurement", {}).get("blockers", [])
    if blockers:
        for blocker in blockers:
            lines.append(f"- {blocker}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Top Verified Queries")
    lines.append("")
    top_queries = report.get("top_verified_queries", [])
    if top_queries:
        for item in top_queries[:10]:
            lines.append(f"- `{item.get('query', '')}` / clicks `{item.get('clicks', 0)}` / impressions `{item.get('impressions', 0)}` / position `{item.get('position', 0)}`")
    else:
        lines.append("- 아직 실측 쿼리 데이터가 없습니다.")
    lines.append("")
    lines.append("## Next Actions")
    lines.append("")
    for action in report.get("next_actions", []):
        lines.append(f"- {action}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
