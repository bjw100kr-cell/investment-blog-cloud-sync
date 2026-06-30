#!/usr/bin/env python3
import html
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POPULAR_READS_BOARD_JSON = ROOT / "outputs/latest/popular-reads-board.json"
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
OUTPUT_JSON = ROOT / "outputs/latest/popular-reads-application-report.json"
OUTPUT_MD = ROOT / "outputs/latest/popular-reads-application-report.md"
START_MARKER = "<!-- popular-reads-live:start -->"
END_MARKER = "<!-- popular-reads-live:end -->"


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


def published_url_lookup() -> dict[str, dict]:
    state = load_json(BLOGGER_STATE_JSON)
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    lookup = {}
    for item in rows:
        keyword = item.get("keyword", "")
        url = item.get("url", "")
        if not keyword or not item.get("published") or not url.startswith("http"):
            continue
        lookup[keyword] = {
            "keyword": keyword,
            "title": item.get("title", ""),
            "url": url,
        }
    return lookup


def source_html_lookup() -> dict[str, dict]:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    lookup = {}
    for item in inventory.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword or not item.get("ready_to_upload"):
            continue
        lookup[keyword] = {
            "title": item.get("title", ""),
            "html_path": str(resolve_workspace_path(item.get("html_path", ""))),
            "source": "publish_inventory",
        }
    return lookup


def remove_existing_block(body: str) -> str:
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return body
    return body[:start].rstrip() + body[end + len(END_MARKER) :].lstrip()


def render_block(group: dict, live_picks: list[dict]) -> str:
    items = []
    for pick in live_picks:
        url = html.escape(pick.get("url", ""), quote=True)
        title = html.escape(pick.get("title", "") or pick.get("keyword", "관련 글"))
        reason = html.escape(pick.get("reason", ""))
        items.append(
            "<li>"
            f"<a href=\"{url}\" rel=\"noopener\">{title}</a>"
            f"<p class=\"popular-read-reason\">{reason}</p>"
            "</li>"
        )
    cta_focus = html.escape(group.get("cta_focus", "관련 글로 이어 보기"))
    return (
        f"{START_MARKER}\n"
        "<section class=\"post-popular-reads-live\">"
        "<h2>지금 같이 많이 볼 만한 글</h2>"
        f"<p>{cta_focus}. 한 글만 보고 나가지 않도록 핵심 흐름을 이어서 정리했습니다.</p>"
        "<ul>"
        + "".join(items)
        + "</ul></section>\n"
        f"{END_MARKER}"
    )


def insertion_point(body: str) -> int:
    candidates = [
        "<!-- internal-link-block:start -->",
        "<section class=\"post-internal-link-boost\">",
        "<section class='post-related-links'>",
        "<section class=\"post-related-links\">",
        "</article>",
    ]
    positions = [body.find(candidate) for candidate in candidates if body.find(candidate) != -1]
    return min(positions) if positions else len(body)


def apply_block(body: str, group: dict, live_picks: list[dict]) -> str:
    cleaned = remove_existing_block(body)
    block = render_block(group, live_picks)
    index = insertion_point(cleaned)
    return cleaned[:index].rstrip() + "\n" + block + "\n" + cleaned[index:].lstrip()


def live_picks_for_group(group: dict, url_lookup: dict[str, dict]) -> list[dict]:
    picks = []
    source_keyword = group.get("source_keyword", "")
    for pick in group.get("picks", []):
        keyword = pick.get("keyword", "")
        if keyword == source_keyword:
            continue
        live = url_lookup.get(keyword)
        if not live:
            continue
        picks.append(
            {
                **live,
                "reason": pick.get("reason", ""),
                "slot": pick.get("slot", ""),
            }
        )
    return picks[:3]


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
    board = load_json(POPULAR_READS_BOARD_JSON)
    url_lookup = published_url_lookup()
    html_lookup = source_html_lookup()
    selected_paths = set()
    items = []

    for group in board.get("groups", []):
        source_keyword = group.get("source_keyword", "")
        live_picks = live_picks_for_group(group, url_lookup)
        html_info = html_lookup.get(source_keyword, {})
        html_path = Path(html_info.get("html_path", ""))
        if not live_picks:
            items.append({"keyword": source_keyword, "applied": False, "reason": "no_live_followup_urls"})
            continue
        if not html_path.exists():
            items.append({"keyword": source_keyword, "applied": False, "reason": "html_missing", "html_path": str(html_path)})
            continue

        selected_paths.add(html_path.resolve())
        before = html_path.read_text()
        after = apply_block(before, group, live_picks)
        changed = before != after
        if changed:
            html_path.write_text(after)
        items.append(
            {
                "keyword": source_keyword,
                "title": html_info.get("title", group.get("cluster_name", "")),
                "html_path": str(html_path),
                "applied": True,
                "changed": changed,
                "live_pick_count": len(live_picks),
                "target_keywords": [pick.get("keyword", "") for pick in live_picks],
                "target_urls": [pick.get("url", "") for pick in live_picks],
            }
        )

    cleanup_items = cleanup_unselected_blocks(selected_paths)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(POPULAR_READS_BOARD_JSON),
        "applied_count": sum(1 for item in items if item.get("applied")),
        "changed_count": sum(1 for item in items if item.get("changed")),
        "cleanup_count": len(cleanup_items),
        "items": items,
        "cleanup_items": cleanup_items,
    }
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = ["# Popular Reads Application Report", ""]
    lines.append(f"- applied_count: `{report['applied_count']}`")
    lines.append(f"- changed_count: `{report['changed_count']}`")
    lines.append(f"- cleanup_count: `{report['cleanup_count']}`")
    lines.append("")
    for item in items:
        lines.append(
            f"- `{item.get('keyword', '')}` / applied `{item.get('applied', False)}` / changed `{item.get('changed', False)}` / live picks `{item.get('live_pick_count', 0)}`"
        )
        if item.get("reason"):
            lines.append(f"  - reason: {item['reason']}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
