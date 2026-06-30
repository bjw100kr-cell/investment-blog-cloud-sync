#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
DAILY_TRAFFIC_GOAL_JSON = ROOT / "outputs/latest/daily-traffic-goal.json"
TRAFFIC_CLUSTER_BOARD_JSON = ROOT / "outputs/latest/traffic-cluster-board.json"
POPULAR_READS_BOARD_JSON = ROOT / "outputs/latest/popular-reads-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/indexing-priority-pack.json"
OUTPUT_MD = ROOT / "outputs/latest/indexing-priority-pack.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def normalize_blog_url(url: str) -> str:
    url = (url or "").strip()
    if not url:
        return ""
    parts = url.split("/")
    if len(parts) < 3:
        return ""
    return "/".join(parts[:3]) + "/"


def published_posts(state: dict) -> list[dict]:
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    posts = []
    for item in rows:
        url = item.get("url", "")
        if not item.get("published") or not url.startswith("http"):
            continue
        posts.append(
            {
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "url": url,
                "last_synced_at": item.get("last_synced_at", ""),
            }
        )
    return posts


def score_lookup(goal: dict) -> dict:
    lookup = {}
    for item in goal.get("top_path", []):
        lookup[item.get("keyword", "")] = item.get("estimated_daily_visitors", 0)
    for item in goal.get("topic_items", []):
        keyword = item.get("keyword", "")
        lookup.setdefault(keyword, item.get("estimated_daily_visitors", item.get("traffic_estimate", 0)))
    return lookup


def build_priority_items(posts: list[dict], goal: dict) -> list[dict]:
    estimates = score_lookup(goal)
    rows = []
    for post in posts:
        keyword = post.get("keyword", "")
        estimate = int(estimates.get(keyword, 0) or 0)
        if keyword.startswith("seo_") and estimate == 0:
            estimate = 35
        rows.append(
            {
                **post,
                "estimated_daily_visitors": estimate,
                "priority": "high" if estimate >= 80 else "medium" if estimate >= 35 else "watch",
                "google_inspection_url": "https://search.google.com/search-console/inspect?" + urlencode({"resource_id": post.get("url", "")}),
                "google_site_search_url": "https://www.google.com/search?" + urlencode({"q": "site:" + post.get("url", "")}),
            }
        )
    rows.sort(key=lambda item: (item["estimated_daily_visitors"], item.get("last_synced_at", "")), reverse=True)
    return rows


def build_internal_link_actions(items: list[dict]) -> list[dict]:
    keyword_to_item = {item.get("keyword"): item for item in items}
    actions = []
    pairs = [
        ("fomc", "seo_fomc_1", "FOMC 메인 글에서 후속 검색형 글로 연결"),
        ("bitcoin", "fomc", "비트코인 글에서 금리/FOMC 영향 설명으로 연결"),
        ("us_index_flow", "fomc", "미국 지수 글에서 금리 이벤트 해설로 연결"),
        ("china", "us_index_flow", "중국 변수 글에서 미국 지수/세계 흐름 비교로 연결"),
    ]
    for source, target, reason in pairs:
        if source not in keyword_to_item or target not in keyword_to_item:
            continue
        actions.append(
            {
                "source_keyword": source,
                "source_url": keyword_to_item[source]["url"],
                "target_keyword": target,
                "target_url": keyword_to_item[target]["url"],
                "anchor_hint": keyword_to_item[target]["title"],
                "reason": reason,
            }
        )
    return actions


def build_report() -> dict:
    state = load_json(BLOGGER_STATE_JSON)
    goal = load_json(DAILY_TRAFFIC_GOAL_JSON)
    cluster = load_json(TRAFFIC_CLUSTER_BOARD_JSON)
    popular = load_json(POPULAR_READS_BOARD_JSON)
    posts = published_posts(state)
    blog_url = normalize_blog_url(posts[0]["url"]) if posts else ""
    priority_items = build_priority_items(posts, goal)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "blog_url": blog_url,
        "sitemap_urls": [f"{blog_url}sitemap.xml", f"{blog_url}feeds/posts/default?orderby=UPDATED"] if blog_url else [],
        "priority_items": priority_items,
        "internal_link_actions": build_internal_link_actions(priority_items),
        "cluster_count": len(cluster.get("clusters", [])),
        "popular_read_lanes": len(popular.get("lanes", [])),
        "daily_traffic_projection": goal.get("projected_daily_visitors", 0),
        "target_daily_visitors": goal.get("target_daily_visitors", 200),
        "search_console_required": True,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Indexing Priority Pack")
    lines.append("")
    lines.append("검색 유입을 빨리 만들기 위해 Search Console 검증 후 먼저 색인 확인할 URL과 내부링크 액션을 정리합니다.")
    lines.append("")
    lines.append(f"- target_daily_visitors: `{report.get('target_daily_visitors', 200)}`")
    lines.append(f"- daily_traffic_projection: `{report.get('daily_traffic_projection', 0)}`")
    lines.append(f"- search_console_required: `{report.get('search_console_required', True)}`")
    lines.append("")
    lines.append("## Sitemaps")
    lines.append("")
    for url in report.get("sitemap_urls", []):
        lines.append(f"- `{url}`")
    if not report.get("sitemap_urls"):
        lines.append("- none")
    lines.append("")
    lines.append("## Priority URLs")
    lines.append("")
    for item in report.get("priority_items", []):
        lines.append(f"- `{item.get('priority', '')}` / `{item.get('keyword', '')}` / 예상 `{item.get('estimated_daily_visitors', 0)}`명: {item.get('title', '')}")
        lines.append(f"  - url: {item.get('url', '')}")
        lines.append(f"  - inspect: {item.get('google_inspection_url', '')}")
        lines.append(f"  - site search: {item.get('google_site_search_url', '')}")
    if not report.get("priority_items"):
        lines.append("- none")
    lines.append("")
    lines.append("## Internal Link Actions")
    lines.append("")
    for action in report.get("internal_link_actions", []):
        lines.append(
            f"- `{action.get('source_keyword', '')}` -> `{action.get('target_keyword', '')}` / anchor `{action.get('anchor_hint', '')}` / {action.get('reason', '')}"
        )
    if not report.get("internal_link_actions"):
        lines.append("- none")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
