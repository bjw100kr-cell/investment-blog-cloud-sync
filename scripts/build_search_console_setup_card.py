#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote_plus, urlencode


ROOT = Path(__file__).resolve().parents[1]
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
SEARCH_CONSOLE_FETCH_JSON = ROOT / "outputs/latest/search-console-fetch-report.json"
VISITOR_PROOF_BOARD_JSON = ROOT / "outputs/latest/visitor-proof-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/search-console-setup-card.json"
OUTPUT_MD = ROOT / "outputs/latest/search-console-setup-card.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def normalize_site_url(value: str) -> str:
    value = (value or "").strip()
    if value and not value.endswith("/"):
        value += "/"
    return value


def infer_blog_url(state: dict, fetch_report: dict) -> str:
    if fetch_report.get("site_url"):
        return normalize_site_url(fetch_report["site_url"])
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    for item in rows:
        url = item.get("url", "")
        if url.startswith("http"):
            parts = url.split("/")
            if len(parts) >= 3:
                return normalize_site_url("/".join(parts[:3]))
    return ""


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
    posts.sort(key=lambda item: item.get("last_synced_at", ""), reverse=True)
    return posts


def build_report() -> dict:
    state = load_json(BLOGGER_STATE_JSON)
    fetch_report = load_json(SEARCH_CONSOLE_FETCH_JSON)
    proof = load_json(VISITOR_PROOF_BOARD_JSON)
    blog_url = infer_blog_url(state, fetch_report)
    posts = published_posts(state)
    sitemap_urls = []
    if blog_url:
        sitemap_urls = [
            f"{blog_url}sitemap.xml",
            f"{blog_url}feeds/posts/default?orderby=UPDATED",
        ]
    add_property_url = "https://search.google.com/search-console/welcome"
    property_settings_url = "https://search.google.com/search-console/settings"
    sitemaps_url = "https://search.google.com/search-console/sitemaps"
    inspection_url = ""
    if posts:
        inspection_url = "https://search.google.com/search-console/inspect?" + urlencode({"resource_id": posts[0]["url"]})

    blockers = proof.get("measurement", {}).get("blockers", [])
    minimum_action = {
        "label": "Search Console에 URL-prefix 속성 추가/검증",
        "property_value": blog_url,
        "open_url": add_property_url,
        "why_now": "이 작업이 끝나야 실제 검색 클릭/노출을 가져와 하루 200명 달성 여부를 증명할 수 있습니다.",
    }
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "blog_url": blog_url,
        "proof_status": proof.get("proof_status", ""),
        "search_console_available": fetch_report.get("available", False),
        "accessible_site_count": len(fetch_report.get("accessible_sites", []) or []),
        "blockers": blockers,
        "minimum_next_action": minimum_action,
        "recommended_property": {
            "type": "URL-prefix",
            "value": blog_url,
            "why": "Blogger 하위 도메인은 URL-prefix 속성으로 먼저 검증하는 것이 가장 단순합니다.",
        },
        "open_links": {
            "add_property": add_property_url,
            "settings": property_settings_url,
            "sitemaps": sitemaps_url,
            "url_inspection_latest_post": inspection_url,
            "search_preview": f"https://www.google.com/search?{urlencode({'q': 'site:' + blog_url})}" if blog_url else "",
        },
        "step_by_step": [
            "Search Console을 같은 Google 계정으로 엽니다.",
            "속성 추가에서 `URL-prefix`를 선택합니다.",
            f"`{blog_url}`를 그대로 붙여넣고 계속을 누릅니다.",
            "Blogger를 관리하는 같은 Google 계정이면 Google-hosted property로 자동 검증될 수 있습니다.",
            "검증 후 Sitemaps 메뉴에서 `sitemap.xml`과 `feeds/posts/default?orderby=UPDATED`를 제출합니다.",
            "URL 검사에서 상위 공개 글 3~5개를 검사하고 색인 요청합니다.",
            "아래 재검증 명령을 실행해 accessible_sites와 clicks/impressions가 들어오는지 확인합니다.",
        ],
        "official_references": [
            {
                "label": "Google Search Console: Add a website property",
                "url": "https://support.google.com/webmasters/answer/34592",
                "note": "Blogger 같은 Google-hosted site는 같은 계정이면 URL-prefix 또는 Domain property 검증이 자동 처리될 수 있습니다.",
            },
            {
                "label": "Google Search Central: Build and submit a sitemap",
                "url": "https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap",
                "note": "Blogger 같은 CMS는 sitemap/feed를 제공할 수 있고, Search Console Sitemaps report로 제출합니다.",
            },
            {
                "label": "Google Search Console: Sitemaps report",
                "url": "https://support.google.com/webmasters/answer/7451001",
                "note": "Sitemaps report에서 제출 이력과 처리 오류를 확인합니다.",
            },
        ],
        "sitemap_urls": sitemap_urls,
        "submit_first_urls": posts[:10],
        "verification_check_command": "python3 scripts/fetch_search_console_queries.py && python3 scripts/build_visitor_proof_board.py",
        "verification_full_command": "python3 scripts/fetch_search_console_queries.py && python3 scripts/search_console_to_feedback.py && python3 scripts/compile_performance_feedback.py && python3 scripts/build_visitor_proof_board.py",
        "success_condition": "Search Console API에서 accessible_sites가 1개 이상이고 visitor-proof-board가 실제 clicks/impressions를 표시",
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Search Console Setup Card")
    lines.append("")
    lines.append("실제 하루 200명 달성을 증명하려면 Search Console에서 블로그 속성 검증이 먼저 필요합니다.")
    lines.append("")
    lines.append("## Current State")
    lines.append("")
    lines.append(f"- blog_url: `{report.get('blog_url', '')}`")
    lines.append(f"- proof_status: `{report.get('proof_status', '')}`")
    lines.append(f"- search_console_available: `{report.get('search_console_available', False)}`")
    lines.append(f"- accessible_site_count: `{report.get('accessible_site_count', 0)}`")
    lines.append("")
    lines.append("## One-Time Setup")
    lines.append("")
    action = report.get("minimum_next_action", {})
    lines.append("### 지금 할 일 1개")
    lines.append("")
    lines.append(f"- action: `{action.get('label', '')}`")
    lines.append(f"- property_value: `{action.get('property_value', '')}`")
    lines.append(f"- open: {action.get('open_url', '')}")
    lines.append(f"- why: {action.get('why_now', '')}")
    lines.append("")
    property_info = report.get("recommended_property", {})
    lines.append(f"- recommended_property_type: `{property_info.get('type', '')}`")
    lines.append(f"- property_value: `{property_info.get('value', '')}`")
    lines.append(f"- why: {property_info.get('why', '')}")
    lines.append(f"- add property: {report.get('open_links', {}).get('add_property', '')}")
    lines.append(f"- sitemap page: {report.get('open_links', {}).get('sitemaps', '')}")
    if report.get("open_links", {}).get("url_inspection_latest_post"):
        lines.append(f"- latest post inspection: {report['open_links']['url_inspection_latest_post']}")
    lines.append("")
    lines.append("## Step By Step")
    lines.append("")
    for idx, step in enumerate(report.get("step_by_step", []), start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    lines.append("## Submit These Sitemaps")
    lines.append("")
    for url in report.get("sitemap_urls", []):
        lines.append(f"- `{url}`")
    if not report.get("sitemap_urls"):
        lines.append("- 블로그 URL을 아직 찾지 못했습니다.")
    lines.append("")
    lines.append("## First URLs To Inspect")
    lines.append("")
    for item in report.get("submit_first_urls", []):
        lines.append(f"- `{item.get('keyword', '')}` / {item.get('title', '')}: {item.get('url', '')}")
    if not report.get("submit_first_urls"):
        lines.append("- 아직 공개 URL이 없습니다.")
    lines.append("")
    lines.append("## Blockers")
    lines.append("")
    for blocker in report.get("blockers", []):
        lines.append(f"- {blocker}")
    if not report.get("blockers"):
        lines.append("- none")
    lines.append("")
    lines.append("## After Setup")
    lines.append("")
    lines.append(f"- run: `{report.get('verification_check_command', '')}`")
    lines.append(f"- full refresh: `{report.get('verification_full_command', '')}`")
    lines.append(f"- success: {report.get('success_condition', '')}")
    lines.append("")
    lines.append("## Official References")
    lines.append("")
    for item in report.get("official_references", []):
        lines.append(f"- [{item.get('label', '')}]({item.get('url', '')}): {item.get('note', '')}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
