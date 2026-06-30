#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from env_loader import load_env_file
from upload_blogger_drafts import (
    BLOGGER_POST_URL,
    ROOT,
    api_request_with_retry,
    ensure_env,
    env_float,
    env_int,
    refresh_access_token,
)


REPORT_PATH = ROOT / "outputs/latest/blogger-cleanup-report.json"
STATE_PATH = ROOT / "outputs/latest/blogger-upload-state.json"


def parse_post_ids(raw: str) -> list[str]:
    ids: list[str] = []
    for part in raw.replace("\n", ",").split(","):
        value = part.strip()
        if value and value not in ids:
            ids.append(value)
    return ids


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))


def delete_post(blog_id: str, access_token: str, post_id: str) -> tuple[bool, Optional[object], str]:
    return api_request_with_retry(
        "DELETE",
        BLOGGER_POST_URL.format(blog_id=blog_id, post_id=post_id),
        max_attempts=env_int("BLOGGER_API_MAX_ATTEMPTS", default=4),
        backoff_base=env_float("BLOGGER_API_BACKOFF_BASE_SECONDS", default=1.5),
        backoff_max=env_float("BLOGGER_API_BACKOFF_MAX_SECONDS", default=20.0),
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=60,
    )


def remove_deleted_from_state(post_ids: list[str]) -> int:
    state = load_json(STATE_PATH)
    items = state.get("items", {})
    if not isinstance(items, dict):
        return 0

    removed = 0
    for key, item in list(items.items()):
        if isinstance(item, dict) and str(item.get("post_id", "")) in post_ids:
            del items[key]
            removed += 1
    if removed:
        save_json(STATE_PATH, state)
    return removed


def main() -> int:
    load_env_file(ROOT)
    post_ids = parse_post_ids(os.getenv("BLOGGER_CLEANUP_POST_IDS", ""))
    if not post_ids:
        save_json(
            REPORT_PATH,
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "requested_post_ids": [],
                "deleted_count": 0,
                "items": [],
                "reason": "BLOGGER_CLEANUP_POST_IDS empty",
            },
        )
        return 0

    blog_id = ensure_env("BLOGGER_BLOG_ID")
    access_token = refresh_access_token()
    results = []
    deleted_ids: list[str] = []

    for post_id in post_ids:
        success, payload, error = delete_post(blog_id, access_token, post_id)
        if success:
            deleted_ids.append(post_id)
        results.append(
            {
                "post_id": post_id,
                "deleted": success,
                "error": error,
                "payload": payload,
            }
        )

    removed_from_state = remove_deleted_from_state(deleted_ids)
    save_json(
        REPORT_PATH,
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "requested_post_ids": post_ids,
            "deleted_count": len(deleted_ids),
            "removed_from_state_count": removed_from_state,
            "items": results,
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
