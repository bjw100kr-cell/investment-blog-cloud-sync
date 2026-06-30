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
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "blog_url": blog_url,
        "proof_status": proof.get("proof_status", ""),
        "search_console_available": fetch_report.get("available", False),
        "accessible_site_count": len(fetch_report.get("accessible_sites", []) or []),
        "blockers": blockers,
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
        "sitemap_urls": sitemap_urls,
        "submit_first_urls": posts[:10],
        "verification_check_command": "python3 scripts/fetch_search_console_queries.py && python3 scripts/build_visitor_proof_board.py",
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
    property_info = report.get("recommended_property", {})
    lines.append(f"- recommended_property_type: `{property_info.get('type', '')}`")
    lines.append(f"- property_value: `{property_info.get('value', '')}`")
    lines.append(f"- why: {property_info.get('why', '')}")
    lines.append(f"- add property: {report.get('open_links', {}).get('add_property', '')}")
    lines.append(f"- sitemap page: {report.get('open_links', {}).get('sitemaps', '')}")
    if report.get("open_links", {}).get("url_inspection_latest_post"):
        lines.append(f"- latest post inspection: {report['open_links']['url_inspection_latest_post']}")
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
    lines.append(f"- success: {report.get('success_condition', '')}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
