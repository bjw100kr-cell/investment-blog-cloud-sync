#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "outputs/latest/google-oauth-client-discovery.json"
OUTPUT_MD = ROOT / "outputs/latest/google-oauth-client-discovery.md"
SEARCH_ROOTS = [
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    ROOT,
]
MAX_DEPTH = 3
MAX_CANDIDATES = 20


def looks_like_google_oauth_client(path: Path) -> tuple[bool, dict]:
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return False, {}

    client_payload = payload.get("web") or payload.get("installed")
    if not isinstance(client_payload, dict):
        return False, {}
    client_id = (client_payload.get("client_id") or "").strip()
    client_secret = (client_payload.get("client_secret") or "").strip()
    if not client_id or not client_secret:
        return False, {}
    return True, {
        "client_type": "web" if "web" in payload else "installed",
        "client_id": client_id,
        "redirect_uris": client_payload.get("redirect_uris", []) or [],
    }


def iter_candidate_files(root: Path):
    if not root.exists():
        return
    for path in root.rglob("*.json"):
        try:
            depth = len(path.relative_to(root).parts)
        except Exception:
            continue
        if depth > MAX_DEPTH:
            continue
        lower_name = path.name.lower()
        if "client_secret" in lower_name or "google" in lower_name or "oauth" in lower_name:
            yield path


def discover() -> list[dict]:
    candidates = []
    seen = set()
    for root in SEARCH_ROOTS:
        for path in iter_candidate_files(root):
            resolved = str(path.resolve())
            if resolved in seen:
                continue
            seen.add(resolved)
            ok, meta = looks_like_google_oauth_client(path)
            if not ok:
                continue
            stat = path.stat()
            candidates.append(
                {
                    "path": resolved,
                    "name": path.name,
                    "parent": str(path.parent),
                    "mtime": stat.st_mtime,
                    "size": stat.st_size,
                    **meta,
                }
            )
            if len(candidates) >= MAX_CANDIDATES:
                return sorted(candidates, key=lambda item: (-item["mtime"], item["path"]))
    return sorted(candidates, key=lambda item: (-item["mtime"], item["path"]))


def write_outputs(candidates: list[dict]) -> None:
    payload = {
        "search_roots": [str(path) for path in SEARCH_ROOTS],
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Google OAuth Client Discovery")
    lines.append("")
    lines.append(f"- candidate_count: `{len(candidates)}`")
    lines.append("")
    if candidates:
        lines.append("## Candidates")
        lines.append("")
        for item in candidates:
            lines.append(f"- `{item['path']}`")
            lines.append(f"  - client_type: {item['client_type']}")
            lines.append(f"  - redirect_uris: {', '.join(item['redirect_uris']) if item['redirect_uris'] else '(none)'}")
    else:
        lines.append("- 자동 탐지된 OAuth client JSON이 없습니다.")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    candidates = discover()
    write_outputs(candidates)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
