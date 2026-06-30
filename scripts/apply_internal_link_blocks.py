#!/usr/bin/env python3
import html
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEXING_PRIORITY_PACK_JSON = ROOT / "outputs/latest/indexing-priority-pack.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
SEO_PUBLISH_READY_DIR = ROOT / "outputs/latest/seo-publish-ready"
OUTPUT_JSON = ROOT / "outputs/latest/internal-link-application-report.json"
OUTPUT_MD = ROOT / "outputs/latest/internal-link-application-report.md"
START_MARKER = "<!-- internal-link-block:start -->"
END_MARKER = "<!-- internal-link-block:end -->"


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


def manifest_lookup() -> dict[str, dict]:
    lookup = {}
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    for item in inventory.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword or not item.get("ready_to_upload"):
            continue
        html_path = resolve_workspace_path(item.get("html_path", ""))
        lookup[keyword] = {
            "manifest_path": str(resolve_workspace_path(item.get("manifest_path", ""))),
            "html_path": str(html_path),
            "title": item.get("title", ""),
            "ready": True,
            "source": "publish_inventory",
        }

    for path in list(PUBLISH_READY_DIR.glob("*.json")) + list(SEO_PUBLISH_READY_DIR.glob("*.json")):
        payload = load_json(path)
        keyword = payload.get("keyword", "")
        if not keyword or keyword in lookup:
            continue
        html_path = resolve_workspace_path(payload.get("html_path", ""))
        lookup[keyword] = {
            "manifest_path": str(path),
            "html_path": str(html_path),
            "title": payload.get("title", ""),
            "ready": bool(payload.get("ready")),
            "source": "manifest_glob",
        }
    return lookup


def remove_existing_block(body: str) -> str:
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return body
    return body[:start].rstrip() + body[end + len(END_MARKER) :].lstrip()


def render_block(actions: list[dict]) -> str:
    items = []
    for action in actions:
        target_url = html.escape(action.get("target_url", ""), quote=True)
        anchor = html.escape(action.get("anchor_hint", "") or action.get("target_keyword", "관련 글"))
        reason = html.escape(action.get("reason", ""))
        items.append(
            "<li>"
            f"<a href=\"{target_url}\" rel=\"noopener\">{anchor}</a>"
            f"<p class=\"internal-link-reason\">{reason}</p>"
            "</li>"
        )
    return (
        f"{START_MARKER}\n"
        "<section class=\"post-internal-link-boost\">"
        "<h2>함께 읽으면 흐름이 이어지는 글</h2>"
        "<p>이 글 하나로 끝내기보다 아래 글까지 이어서 보면 금리, 주식, 코인 흐름을 더 입체적으로 볼 수 있습니다.</p>"
        "<ul>"
        + "".join(items)
        + "</ul></section>\n"
        f"{END_MARKER}"
    )


def insertion_point(body: str) -> int:
    candidates = [
        "<section class='post-related-links'>",
        "<section class=\"post-related-links\">",
        "<section class='post-disclosure'>",
        "<section class=\"post-disclosure\">",
        "</article>",
    ]
    positions = [body.find(candidate) for candidate in candidates if body.find(candidate) != -1]
    return min(positions) if positions else len(body)


def apply_block(body: str, actions: list[dict]) -> str:
    cleaned = remove_existing_block(body)
    block = render_block(actions)
    index = insertion_point(cleaned)
    return cleaned[:index].rstrip() + "\n" + block + "\n" + cleaned[index:].lstrip()


def grouped_actions(actions: list[dict]) -> dict[str, list[dict]]:
    grouped = {}
    for action in actions:
        source = action.get("source_keyword", "")
        target_url = action.get("target_url", "")
        if not source or not target_url:
            continue
        grouped.setdefault(source, []).append(action)
    return grouped


def cleanup_unselected_blocks(selected_paths: set[Path]) -> list[dict]:
    cleanup_items = []
    for path in list(PUBLISH_READY_DIR.glob("*.html")) + list(SEO_PUBLISH_READY_DIR.glob("*.html")):
        if path.resolve() in selected_paths:
            continue
        before = path.read_text()
        if START_MARKER not in before:
            continue
        after = remove_existing_block(before)
        path.write_text(after)
        cleanup_items.append({"html_path": str(path), "removed_stale_block": True})
    return cleanup_items


def main() -> int:
    indexing_pack = load_json(INDEXING_PRIORITY_PACK_JSON)
    manifests = manifest_lookup()
    actions_by_source = grouped_actions(indexing_pack.get("internal_link_actions", []))
    items = []
    selected_paths = set()

    for keyword, actions in sorted(actions_by_source.items()):
        manifest = manifests.get(keyword, {})
        html_path = Path(manifest.get("html_path", ""))
        if not manifest:
            items.append({"keyword": keyword, "applied": False, "reason": "manifest_missing"})
            continue
        if not html_path.exists():
            items.append({"keyword": keyword, "applied": False, "reason": "html_missing", "html_path": str(html_path)})
            continue

        selected_paths.add(html_path.resolve())
        before = html_path.read_text()
        after = apply_block(before, actions)
        changed = before != after
        if changed:
            html_path.write_text(after)
        items.append(
            {
                "keyword": keyword,
                "title": manifest.get("title", ""),
                "html_path": str(html_path),
                "applied": True,
                "changed": changed,
                "link_count": len(actions),
                "source": manifest.get("source", ""),
                "target_keywords": [action.get("target_keyword", "") for action in actions],
            }
        )

    cleanup_items = cleanup_unselected_blocks(selected_paths)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(INDEXING_PRIORITY_PACK_JSON),
        "applied_count": sum(1 for item in items if item.get("applied")),
        "changed_count": sum(1 for item in items if item.get("changed")),
        "cleanup_count": len(cleanup_items),
        "items": items,
        "cleanup_items": cleanup_items,
    }
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = ["# Internal Link Application Report", ""]
    lines.append(f"- applied_count: `{report['applied_count']}`")
    lines.append(f"- changed_count: `{report['changed_count']}`")
    lines.append(f"- cleanup_count: `{report['cleanup_count']}`")
    lines.append("")
    for item in items:
        lines.append(
            f"- `{item.get('keyword', '')}` / applied `{item.get('applied', False)}` / changed `{item.get('changed', False)}` / links `{item.get('link_count', 0)}`"
        )
        if item.get("reason"):
            lines.append(f"  - reason: {item['reason']}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
