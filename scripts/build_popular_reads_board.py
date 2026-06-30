#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRAFFIC_CLUSTER_BOARD_JSON = ROOT / "outputs/latest/traffic-cluster-board.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
OUTPUT_JSON = ROOT / "outputs/latest/popular-reads-board.json"
OUTPUT_MD = ROOT / "outputs/latest/popular-reads-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def quality_lookup(items: list[dict]) -> dict[str, dict]:
    return {item.get("keyword", ""): item for item in items if item.get("keyword")}


def cluster_label(cluster: dict) -> str:
    return cluster.get("cluster_name", cluster.get("source_keyword", ""))


def choose_reason(item: dict) -> str:
    objective = item.get("revenue_objective", "")
    if "검색" in objective:
        return "검색형 유입을 받기 좋은 주제"
    if "재방문" in objective or "내부링크" in objective:
        return "재방문과 내부링크 순환에 유리한 주제"
    if "체류시간" in objective:
        return "페이지 체류시간을 늘리기 좋은 주제"
    return "대표 읽을거리 묶음으로 쓰기 좋은 주제"


def build_report() -> dict:
    clusters = load_json(TRAFFIC_CLUSTER_BOARD_JSON).get("clusters", [])
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)
    quality = quality_lookup(load_json(PRE_PUBLISH_QUALITY_GATE_JSON).get("items", []))

    focus_keywords = {item.get("keyword", "") for item in revenue_focus.get("today_path", []) if item.get("keyword")}
    groups = []

    for cluster in clusters[:4]:
        picks = []
        source_keyword = cluster.get("source_keyword", "")
        main_ready = cluster.get("main_ready_to_upload", False)

        if cluster.get("main_title"):
            picks.append(
                {
                    "title": cluster.get("main_title", ""),
                    "keyword": cluster.get("main_keyword", ""),
                    "slot": "main_pick",
                    "reason": "지금 이 클러스터를 대표하는 메인 글",
                    "html_path": cluster.get("main_html_path", ""),
                    "ready_now": main_ready,
                }
            )

        for idx, item in enumerate(cluster.get("followups", [])[:2], start=1):
            q = quality.get(item.get("keyword", ""), {})
            picks.append(
                {
                    "title": item.get("title", ""),
                    "keyword": item.get("keyword", ""),
                    "slot": f"followup_pick_{idx}",
                    "reason": choose_reason(item),
                    "html_path": item.get("html_path", ""),
                    "ready_now": q.get("status") != "needs_fix",
                }
            )

        headline = "오늘 먼저 노출할 popular reads 묶음"
        if source_keyword in focus_keywords:
            headline = "오늘 메인 동선에 바로 붙일 popular reads 묶음"

        groups.append(
            {
                "cluster_name": cluster_label(cluster),
                "source_keyword": source_keyword,
                "headline": headline,
                "main_ready_to_upload": main_ready,
                "cta_focus": cluster.get("cta_focus", ""),
                "next_action": cluster.get("next_action", ""),
                "blockers": cluster.get("blockers", []),
                "picks": picks,
            }
        )

    return {
        "board_goal": "메인 글 아래나 허브 페이지에 붙일 popular reads 후보를 묶어 내부링크와 재방문 흐름을 강화",
        "group_count": len(groups),
        "groups": groups,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Popular Reads Board")
    lines.append("")
    lines.append("메인 글 아래나 허브 페이지에 붙일 `popular reads` 후보를 미리 묶어보는 운영 카드입니다.")
    lines.append(f"- board_goal: {report.get('board_goal', '')}")
    lines.append(f"- group_count: `{report.get('group_count', 0)}`")
    lines.append("")
    for idx, group in enumerate(report.get("groups", []), start=1):
        lines.append(f"## {idx}. {group.get('cluster_name', '')}")
        lines.append("")
        lines.append(f"- source_keyword: `{group.get('source_keyword', '')}`")
        lines.append(f"- headline: {group.get('headline', '')}")
        lines.append(f"- main_ready_to_upload: `{group.get('main_ready_to_upload', False)}`")
        lines.append(f"- cta_focus: {group.get('cta_focus', '')}")
        lines.append(f"- next_action: {group.get('next_action', '')}")
        for blocker in group.get("blockers", []):
            lines.append(f"- blocker: {blocker}")
        for pick in group.get("picks", []):
            lines.append(
                f"- pick: `{pick.get('title', '')}` / `{pick.get('keyword', '')}` / `{pick.get('slot', '')}` / ready `{pick.get('ready_now', False)}` / {pick.get('reason', '')}"
            )
            if pick.get("html_path"):
                lines.append(f"  - html_path: `{pick.get('html_path', '')}`")
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
