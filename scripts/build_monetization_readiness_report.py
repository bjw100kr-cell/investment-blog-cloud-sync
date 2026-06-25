#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
ENV_PATH = ROOT / ".env"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
GROWTH_JSON = ROOT / "outputs/latest/growth-report.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
OUTPUT_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
OUTPUT_MD = ROOT / "outputs/latest/monetization-readiness-report.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def parse_env(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def build_stage(name: str, ready: bool, evidence: list[str], missing: list[str], next_step: str) -> dict:
    return {
        "name": name,
        "ready": ready,
        "evidence": evidence,
        "missing": missing,
        "next_step": next_step,
    }


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    growth = load_json(GROWTH_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    seo_backlog = load_json(SEO_BACKLOG_JSON)

    integrations = integration_lookup(setup)
    env_values = parse_env(ENV_PATH)
    queue_items = queue.get("items", [])
    ready_queue_items = [item for item in queue_items if item.get("ready_to_upload")]
    trend_watchlist = growth.get("trend_watchlist", [])
    query_watchlist = growth.get("query_watchlist", [])
    board_breaking = keyword_board.get("breaking_candidates", [])
    board_watchlist = keyword_board.get("query_watchlist", [])
    seo_followups = seo_backlog.get("items", [])

    content_engine_ready = bool(ready_queue_items)
    publishing_engine_ready = bool(ready_queue_items) and integrations.get("blogger_upload", {}).get("ready", False)
    search_engine_ready = bool(trend_watchlist or query_watchlist or board_breaking or board_watchlist or seo_followups)
    analytics_ready = bool(env_values.get("GA4_MEASUREMENT_ID"))
    adsense_ready = bool(env_values.get("ADSENSE_PUBLISHER_ID"))
    newsletter_ready = bool(env_values.get("NEWSLETTER_SUBSCRIBE_URL"))

    stages = [
        build_stage(
            "content_engine",
            content_engine_ready,
            [
                f"publish queue ready items {len(ready_queue_items)}개",
                f"human tone average {growth.get('tone_review', {}).get('average_score', 0)}",
            ],
            [] if content_engine_ready else ["publish-ready posts not generated"],
            "발행 가능한 글을 최소 1개 이상 유지하고, 매일 속보 1개 + evergreen 1개 조합을 계속 굴립니다.",
        ),
        build_stage(
            "publishing_engine",
            publishing_engine_ready,
            [
                f"publish-ready html items {setup.get('publish_ready', {}).get('ready_count', 0)}개",
                f"blogger integration ready={integrations.get('blogger_upload', {}).get('ready', False)}",
            ],
            integrations.get("blogger_upload", {}).get("missing", []) if not publishing_engine_ready else [],
            "Blogger 업로드 자격값을 연결해서 draft 업로드를 자동 검증합니다.",
        ),
        build_stage(
            "search_demand_engine",
            search_engine_ready,
            [
                f"trend watchlist {len(trend_watchlist)}개",
                f"search console watchlist {len(query_watchlist)}개",
                f"daily opportunity breaking candidates {len(board_breaking)}개",
                f"daily opportunity query watchlist {len(board_watchlist)}개",
                f"seo follow-up backlog {len(seo_followups)}개",
            ],
            [] if search_engine_ready else ["search demand signals unavailable"],
            "기회판과 SEO 백로그를 기준으로 당일 글 1개, 후속 검색형 글 1개씩 이어 붙이면서 Search Console 데이터가 쌓일 때까지 운영합니다.",
        ),
        build_stage(
            "analytics_stack",
            analytics_ready,
            ["GA4 measurement id present" if analytics_ready else "GA4 measurement id missing"],
            [] if analytics_ready else ["GA4_MEASUREMENT_ID"],
            "GA4 측정 ID를 연결해 어떤 글이 실제 체류시간과 재방문을 만드는지 확인합니다.",
        ),
        build_stage(
            "adsense_stack",
            adsense_ready,
            ["AdSense publisher id present" if adsense_ready else "AdSense publisher id missing"],
            [] if adsense_ready else ["ADSENSE_PUBLISHER_ID", "ADSENSE_SITE_VERIFICATION"],
            "AdSense 승인 이후 publisher id와 사이트 검증값을 붙여 수익화 스택을 완성합니다.",
        ),
        build_stage(
            "retention_stack",
            newsletter_ready,
            ["newsletter url present" if newsletter_ready else "newsletter url missing"],
            [] if newsletter_ready else ["NEWSLETTER_SUBSCRIBE_URL"],
            "뉴스레터나 텔레그램 같은 재방문 수단 URL을 연결해 한 번 들어온 독자를 쌓습니다.",
        ),
    ]

    readiness_score = round((sum(1 for stage in stages if stage["ready"]) / max(len(stages), 1)) * 100, 1)
    next_actions = []
    for stage in stages:
        if not stage["ready"]:
            next_actions.append(f"{stage['name']}: {stage['next_step']}")

    return {
        "generated_at": queue.get("generated_at", ""),
        "readiness_score": readiness_score,
        "stages": stages,
        "queue_summary": {
            "queue_count": queue.get("summary", {}).get("queue_count", 0),
            "ready_count": queue.get("summary", {}).get("ready_count", 0),
        },
        "top_publish_targets": [
            {
                "keyword": item.get("keyword"),
                "title": item.get("title"),
                "upload_sequence": item.get("upload_sequence"),
                "revenue_objective": item.get("revenue_objective"),
                "cta_focus": item.get("cta_focus"),
            }
            for item in ready_queue_items[:3]
        ],
        "next_actions": next_actions,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# 수익화 준비도 리포트")
    lines.append("")
    lines.append(f"- 생성 시각: `{report.get('generated_at', '')}`")
    lines.append(f"- 준비도 점수: `{report.get('readiness_score', 0)}`")
    lines.append("")
    lines.append("## 단계별 상태")
    lines.append("")
    for stage in report.get("stages", []):
        lines.append(f"- `{stage['name']}`: {'ready' if stage['ready'] else 'not_ready'}")
        for evidence in stage.get("evidence", []):
            lines.append(f"  - evidence: {evidence}")
        for missing in stage.get("missing", []):
            lines.append(f"  - missing: {missing}")
        lines.append(f"  - next: {stage['next_step']}")
    lines.append("")
    lines.append("## 지금 바로 올릴 우선 글")
    lines.append("")
    for item in report.get("top_publish_targets", []):
        lines.append(
            f"- `{item['upload_sequence']}` `{item['keyword']}`: {item['title']} / 목표 {item['revenue_objective']} / CTA {item['cta_focus']}"
        )
    lines.append("")
    lines.append("## 다음 액션")
    lines.append("")
    for action in report.get("next_actions", []):
        lines.append(f"- {action}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
