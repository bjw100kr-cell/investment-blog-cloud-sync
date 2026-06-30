#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
KEYWORD_CAPTURE_STRATEGY_JSON = ROOT / "outputs/latest/keyword-capture-strategy.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
OUTPUT_JSON = ROOT / "outputs/latest/traffic-cluster-board.json"
OUTPUT_MD = ROOT / "outputs/latest/traffic-cluster-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def quality_lookup(items: list[dict]) -> dict[str, dict]:
    return {item.get("keyword", ""): item for item in items if item.get("keyword")}


def capture_lookup(strategy: dict) -> dict[str, dict]:
    items = {}
    for item in strategy.get("items", []):
        keyword = item.get("keyword", "")
        if keyword:
            items[keyword] = item
    return items


def cluster_summary_name(keyword: str) -> str:
    mapping = {
        "fomc": "거시 이벤트 해설 클러스터",
        "bitcoin": "코인 해설 클러스터",
        "us_big_tech": "미국 빅테크 허브 클러스터",
        "cpi": "인플레이션 해설 클러스터",
    }
    return mapping.get(keyword, f"{keyword} 클러스터")


def build_report() -> dict:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    quality = quality_lookup(load_json(PRE_PUBLISH_QUALITY_GATE_JSON).get("items", []))
    capture = capture_lookup(load_json(KEYWORD_CAPTURE_STRATEGY_JSON))
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in inventory.get("items", []):
        grouped[item.get("source_keyword", item.get("keyword", ""))].append(item)

    clusters = []
    revenue_priority = {
        step.get("keyword", ""): idx for idx, step in enumerate(revenue_focus.get("today_path", []), start=1)
    }

    for source_keyword, items in grouped.items():
        main_post = next((item for item in items if item.get("inventory_type") == "main_post"), {})
        followups = [item for item in items if item.get("inventory_type") == "seo_followup"]
        q = quality.get(source_keyword, {})
        cluster_priority = (main_post.get("priority_score", 0) or 0) + sum(
            item.get("priority_score", 0) or 0 for item in followups[:3]
        )
        ready_followups = sum(1 for item in followups if item.get("ready_to_upload"))

        capture_item = capture.get(source_keyword, {})
        route = capture_item.get("capture_route", "")
        route_description = capture_item.get("capture_route_description", "")

        blockers = []
        if q.get("status") != "pass":
            blockers.append(f"main_quality={q.get('status', 'unknown')}")
        if q.get("status") == "review_before_publish":
            checks = [check.get("name") for check in q.get("checks", []) if not check.get("ok")]
            if checks:
                blockers.extend(checks[:3])

        next_action = "사용자 검토 후 승인 대기"
        if q.get("status") == "pass":
            next_action = "메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비"
        elif "hero_image_selected" in blockers:
            next_action = "대표 이미지 먼저 선택"

        clusters.append(
            {
                "source_keyword": source_keyword,
                "cluster_name": cluster_summary_name(source_keyword),
                "revenue_priority_rank": revenue_priority.get(source_keyword, 99),
                "cluster_priority_score": round(cluster_priority, 1),
                "main_title": main_post.get("title", ""),
                "main_keyword": main_post.get("keyword", ""),
                "main_priority_score": main_post.get("priority_score", 0),
                "main_quality_status": q.get("status", "unknown"),
                "main_ready_to_upload": q.get("status") == "pass",
                "followup_count": len(followups),
                "ready_followup_count": ready_followups,
                "revenue_objective": main_post.get("revenue_objective", ""),
                "cta_focus": main_post.get("cta_focus", ""),
                "capture_route": route,
                "route_description": route_description,
                "next_action": next_action,
                "blockers": blockers,
                "main_html_path": main_post.get("html_path", ""),
                "followups": [
                    {
                        "title": item.get("title", ""),
                        "keyword": item.get("keyword", ""),
                        "priority_score": item.get("priority_score", 0),
                        "post_type": item.get("post_type", ""),
                        "revenue_objective": item.get("revenue_objective", ""),
                        "html_path": item.get("html_path", ""),
                    }
                    for item in sorted(followups, key=lambda x: x.get("priority_score", 0), reverse=True)[:3]
                ],
            }
        )

    clusters.sort(key=lambda x: (x.get("revenue_priority_rank", 99), -x.get("cluster_priority_score", 0)))

    return {
        "board_goal": "메인 글 1개로 끝내지 않고 후속 글과 내부링크로 페이지뷰와 재방문을 늘리는 일일 트래픽 클러스터 우선순위 보드",
        "cluster_count": len(clusters),
        "clusters": clusters,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Traffic Cluster Board")
    lines.append("")
    lines.append("메인 글과 후속 글을 묶어 페이지뷰, 내부링크 순환, 재방문을 같이 키우기 위한 운영 보드입니다.")
    lines.append(f"- board_goal: {report.get('board_goal', '')}")
    lines.append(f"- cluster_count: `{report.get('cluster_count', 0)}`")
    lines.append("")
    for idx, cluster in enumerate(report.get("clusters", []), start=1):
        lines.append(f"## {idx}. {cluster.get('cluster_name', '')}")
        lines.append("")
        lines.append(f"- source_keyword: `{cluster.get('source_keyword', '')}`")
        lines.append(f"- revenue_priority_rank: `{cluster.get('revenue_priority_rank', 99)}`")
        lines.append(f"- cluster_priority_score: `{cluster.get('cluster_priority_score', 0)}`")
        lines.append(f"- main_title: `{cluster.get('main_title', '')}`")
        lines.append(f"- main_quality_status: `{cluster.get('main_quality_status', '')}`")
        lines.append(f"- main_ready_to_upload: `{cluster.get('main_ready_to_upload', False)}`")
        lines.append(f"- followup_count: `{cluster.get('followup_count', 0)}`")
        lines.append(f"- ready_followup_count: `{cluster.get('ready_followup_count', 0)}`")
        lines.append(f"- revenue_objective: {cluster.get('revenue_objective', '')}")
        lines.append(f"- cta_focus: {cluster.get('cta_focus', '')}")
        lines.append(f"- capture_route: `{cluster.get('capture_route', '')}`")
        lines.append(f"- route_description: {cluster.get('route_description', '')}")
        lines.append(f"- next_action: {cluster.get('next_action', '')}")
        for blocker in cluster.get("blockers", []):
            lines.append(f"- blocker: {blocker}")
        if cluster.get("main_html_path"):
            lines.append(f"- main_html_path: `{cluster.get('main_html_path', '')}`")
        for item in cluster.get("followups", []):
            lines.append(
                f"- followup: `{item.get('title', '')}` / `{item.get('keyword', '')}` / priority `{item.get('priority_score', 0)}` / {item.get('revenue_objective', '')}"
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
