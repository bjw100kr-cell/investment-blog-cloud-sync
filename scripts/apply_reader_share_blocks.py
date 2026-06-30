#!/usr/bin/env python3
import html
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote_plus, urlencode


ROOT = Path(__file__).resolve().parents[1]
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
OUTPUT_JSON = ROOT / "outputs/latest/reader-share-application-report.json"
OUTPUT_MD = ROOT / "outputs/latest/reader-share-application-report.md"
START_MARKER = "<!-- reader-share-block:start -->"
END_MARKER = "<!-- reader-share-block:end -->"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def resolve_workspace_path(value: str) -> Path:
    path = Path(value)
    if path.exists():
        return path
    parts = path.parts
    if "outputs" in parts:
        index = parts.index("outputs")
        candidate = ROOT / Path(*parts[index:])
        if candidate.exists():
            return candidate
    return path


def published_lookup() -> dict[str, dict]:
    state = load_json(BLOGGER_STATE_JSON)
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    lookup = {}
    for item in rows:
        keyword = item.get("keyword", "")
        url = item.get("url", "")
        if keyword and item.get("published") and url.startswith("http"):
            lookup[keyword] = {"url": url, "title": item.get("title", "")}
    return lookup


def target_posts() -> list[dict]:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    published = published_lookup()
    posts = []
    for item in inventory.get("items", []):
        keyword = item.get("keyword", "")
        live = published.get(keyword)
        if not live or item.get("inventory_type") != "main_post":
            continue
        html_path = resolve_workspace_path(item.get("html_path", ""))
        posts.append(
            {
                "keyword": keyword,
                "title": item.get("title", live.get("title", "")),
                "url": live.get("url", ""),
                "html_path": str(html_path),
            }
        )
    return posts


def remove_existing_block(body: str) -> str:
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return body
    return body[:start].rstrip() + body[end + len(END_MARKER) :].lstrip()


def share_links(title: str, url: str) -> dict[str, str]:
    text = f"{title} - 경제·코인·주식 흐름을 쉽게 정리한 글"
    return {
        "x": "https://twitter.com/intent/tweet?" + urlencode({"text": text, "url": url}),
        "telegram": "https://t.me/share/url?" + urlencode({"url": url, "text": text}),
        "facebook": "https://www.facebook.com/sharer/sharer.php?" + urlencode({"u": url}),
        "copy_url": url,
    }


def render_block(title: str, url: str) -> str:
    links = share_links(title, url)
    safe_title = html.escape(title)
    return (
        f"{START_MARKER}\n"
        "<section class=\"post-reader-share\">"
        "<h2>이 글이 도움 됐다면 공유하기</h2>"
        f"<p>{safe_title}을 나중에 다시 보거나, 투자 흐름을 같이 보는 사람에게 공유해 보세요.</p>"
        "<p class=\"reader-share-links\">"
        f"<a href=\"{html.escape(links['x'], quote=True)}\" rel=\"noopener\" target=\"_blank\">X에 공유</a> "
        f"<a href=\"{html.escape(links['telegram'], quote=True)}\" rel=\"noopener\" target=\"_blank\">텔레그램 공유</a> "
        f"<a href=\"{html.escape(links['facebook'], quote=True)}\" rel=\"noopener\" target=\"_blank\">페이스북 공유</a> "
        f"<a href=\"{html.escape(links['copy_url'], quote=True)}\" rel=\"noopener\" target=\"_blank\">원문 열기</a>"
        "</p>"
        "</section>\n"
        f"{END_MARKER}"
    )


def insertion_point(body: str) -> int:
    candidates = [
        "<section class='post-retention-cta'>",
        "<section class=\"post-retention-cta\">",
        "<!-- popular-reads-live:start -->",
        "<!-- internal-link-block:start -->",
        "<section class='post-related-links'>",
        "</article>",
    ]
    positions = [body.find(candidate) for candidate in candidates if body.find(candidate) != -1]
    return min(positions) if positions else len(body)


def apply_block(body: str, title: str, url: str) -> str:
    cleaned = remove_existing_block(body)
    block = render_block(title, url)
    index = insertion_point(cleaned)
    return cleaned[:index].rstrip() + "\n" + block + "\n" + cleaned[index:].lstrip()


def cleanup_unselected_blocks(selected_paths: set[Path]) -> list[dict]:
    cleanup_items = []
    for path in PUBLISH_READY_DIR.glob("*.html"):
        if path.resolve() in selected_paths:
            continue
        before = path.read_text()
        if START_MARKER not in before:
            continue
        path.write_text(remove_existing_block(before))
        cleanup_items.append({"html_path": str(path), "removed_stale_block": True})
    return cleanup_items


def main() -> int:
    items = []
    selected_paths = set()
    for post in target_posts():
        html_path = Path(post["html_path"])
        if not html_path.exists():
            items.append({"keyword": post["keyword"], "applied": False, "reason": "html_missing", "html_path": str(html_path)})
            continue
        selected_paths.add(html_path.resolve())
        before = html_path.read_text()
        after = apply_block(before, post["title"], post["url"])
        changed = before != after
        if changed:
            html_path.write_text(after)
        items.append(
            {
                "keyword": post["keyword"],
                "title": post["title"],
                "url": post["url"],
                "html_path": str(html_path),
                "applied": True,
                "changed": changed,
                "share_channels": ["x", "telegram", "facebook", "copy_url"],
            }
        )

    cleanup_items = cleanup_unselected_blocks(selected_paths)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "applied_count": sum(1 for item in items if item.get("applied")),
        "changed_count": sum(1 for item in items if item.get("changed")),
        "cleanup_count": len(cleanup_items),
        "items": items,
        "cleanup_items": cleanup_items,
    }
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = ["# Reader Share Application Report", ""]
    lines.append(f"- applied_count: `{report['applied_count']}`")
    lines.append(f"- changed_count: `{report['changed_count']}`")
    lines.append(f"- cleanup_count: `{report['cleanup_count']}`")
    lines.append("")
    for item in items:
        lines.append(f"- `{item.get('keyword', '')}` / applied `{item.get('applied', False)}` / changed `{item.get('changed', False)}` / url {item.get('url', '')}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
