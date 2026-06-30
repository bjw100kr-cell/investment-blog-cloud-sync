#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
OUTPUT_JSON = ROOT / "outputs/latest/click-title-sync-report.json"
OUTPUT_MD = ROOT / "outputs/latest/click-title-sync-report.md"
MAIN_KEYWORDS = {"fomc", "bitcoin", "us_index_flow", "china"}


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


def extract_h1(html_body: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", html_body, flags=re.DOTALL)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def sync_manifest(path: Path) -> dict:
    manifest = load_json(path)
    keyword = manifest.get("keyword", "")
    if keyword not in MAIN_KEYWORDS:
        return {"path": str(path), "changed": False, "skipped": True, "reason": "not_main_keyword"}

    html_path = resolve_workspace_path(manifest.get("html_path", ""))
    if not html_path.exists():
        return {"path": str(path), "keyword": keyword, "changed": False, "reason": "html_missing"}

    h1 = extract_h1(html_path.read_text())
    if not h1:
        return {"path": str(path), "keyword": keyword, "changed": False, "reason": "h1_missing"}

    old_title = manifest.get("title", "")
    old_meta_title = manifest.get("meta_title", "")
    changed = old_title != h1 or old_meta_title != h1
    manifest["title"] = h1
    manifest["meta_title"] = h1
    if changed:
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    return {
        "path": str(path),
        "keyword": keyword,
        "changed": changed,
        "old_title": old_title,
        "old_meta_title": old_meta_title,
        "new_title": h1,
        "html_path": str(html_path),
    }


def sync_inventory(items: list[dict], title_by_keyword: dict[str, str]) -> tuple[list[dict], int]:
    changed_count = 0
    for item in items:
        keyword = item.get("keyword", "")
        title = title_by_keyword.get(keyword)
        if not title:
            continue
        if item.get("title") != title:
            item["title"] = title
            changed_count += 1
    return items, changed_count


def inventory_manifest_paths(inventory: dict) -> list[Path]:
    paths = []
    seen = set()
    for item in inventory.get("items", []):
        keyword = item.get("keyword", "")
        if keyword not in MAIN_KEYWORDS:
            continue
        manifest_path = item.get("manifest_path", "")
        if not manifest_path:
            continue
        path = resolve_workspace_path(manifest_path)
        if path in seen:
            continue
        seen.add(path)
        paths.append(path)
    return paths


def main() -> int:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    manifest_paths = inventory_manifest_paths(inventory)
    if not manifest_paths:
        manifest_paths = sorted(PUBLISH_READY_DIR.glob("*.json"))

    manifest_items = []
    for path in manifest_paths:
        result = sync_manifest(path)
        if not result.get("skipped"):
            manifest_items.append(result)

    title_by_keyword = {
        item["keyword"]: item["new_title"]
        for item in manifest_items
        if item.get("keyword") and item.get("new_title")
    }
    inventory_changed_count = 0
    if inventory.get("items"):
        inventory["items"], inventory_changed_count = sync_inventory(inventory["items"], title_by_keyword)
        if inventory_changed_count:
            PUBLISH_INVENTORY_JSON.write_text(json.dumps(inventory, ensure_ascii=False, indent=2))

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_changed_count": sum(1 for item in manifest_items if item.get("changed")),
        "inventory_changed_count": inventory_changed_count,
        "items": manifest_items,
    }
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = ["# Click Title Sync Report", ""]
    lines.append(f"- manifest_changed_count: `{report['manifest_changed_count']}`")
    lines.append(f"- inventory_changed_count: `{report['inventory_changed_count']}`")
    lines.append("")
    for item in manifest_items:
        lines.append(f"- `{item.get('keyword', '')}` / changed `{item.get('changed', False)}`")
        lines.append(f"  - old: {item.get('old_meta_title', item.get('old_title', ''))}")
        lines.append(f"  - new: {item.get('new_title', '')}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
