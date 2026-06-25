#!/usr/bin/env python3
import json
import os
from pathlib import Path
from typing import Dict, Optional

import requests
from env_loader import load_env_file


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "outputs/latest/site-page-publish-plan.json"
REPORT_PATH = ROOT / "outputs/latest/blogger-site-pages-report.json"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
BLOGGER_PAGES_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages"
BLOGGER_PAGE_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages/{page_id}"
BLOGGER_PAGE_PUBLISH_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages/{page_id}/publish"


def env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name, "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "on"}


def ensure_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is not set")
    return value


def refresh_access_token() -> str:
    existing = os.getenv("GOOGLE_ACCESS_TOKEN", "").strip()
    if existing:
        return existing

    client_id = ensure_env("GOOGLE_CLIENT_ID")
    client_secret = ensure_env("GOOGLE_CLIENT_SECRET")
    refresh_token = ensure_env("GOOGLE_REFRESH_TOKEN")

    response = requests.post(
        GOOGLE_TOKEN_URL,
        timeout=30,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
    )
    response.raise_for_status()
    payload = response.json()
    token = payload.get("access_token", "")
    if not token:
        raise RuntimeError("Failed to obtain access_token from Google OAuth")
    return token


def auth_headers(access_token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


def load_plan() -> list[dict]:
    if not PLAN_PATH.exists():
        return []
    payload = json.loads(PLAN_PATH.read_text())
    return sorted(payload.get("items", []), key=lambda item: item.get("publish_sequence", 999))


def list_pages(blog_id: str, access_token: str, status: str) -> list[dict]:
    response = requests.get(
        BLOGGER_PAGES_URL.format(blog_id=blog_id),
        timeout=60,
        params={"status": status, "fetchBodies": "false"},
        headers=auth_headers(access_token),
    )
    response.raise_for_status()
    return response.json().get("items", [])


def existing_pages_lookup(blog_id: str, access_token: str) -> dict[str, dict]:
    items_by_id: dict[str, dict] = {}
    for status in ["live", "draft"]:
        for item in list_pages(blog_id, access_token, status):
            page_id = item.get("id")
            if page_id and page_id not in items_by_id:
                items_by_id[page_id] = item

    lookup: dict[str, dict] = {}
    for item in items_by_id.values():
        title = item.get("title", "").strip().lower()
        url = item.get("url", "").strip().lower()
        if title:
            lookup[f"title:{title}"] = item
        if url:
            lookup[f"url:{url}"] = item
    return lookup


def find_existing_page(page_plan: dict, lookup: Dict[str, dict]) -> Optional[dict]:
    title_key = f"title:{page_plan.get('title', '').strip().lower()}"
    if title_key in lookup:
        return lookup[title_key]

    html_path = Path(page_plan.get("html_path", ""))
    slug = html_path.stem.strip().lower()
    for key, item in lookup.items():
        if key.startswith("url:") and f"/p/{slug}.html" in key:
            return item
    return None


def insert_page(blog_id: str, access_token: str, title: str, content: str) -> dict:
    response = requests.post(
        BLOGGER_PAGES_URL.format(blog_id=blog_id),
        timeout=60,
        headers=auth_headers(access_token),
        json={
            "kind": "blogger#page",
            "title": title,
            "content": content,
        },
    )
    response.raise_for_status()
    return response.json()


def update_page(blog_id: str, access_token: str, page_id: str, title: str, content: str) -> dict:
    response = requests.put(
        BLOGGER_PAGE_URL.format(blog_id=blog_id, page_id=page_id),
        timeout=60,
        headers=auth_headers(access_token),
        json={
            "kind": "blogger#page",
            "id": page_id,
            "title": title,
            "content": content,
        },
    )
    response.raise_for_status()
    return response.json()


def publish_page(blog_id: str, access_token: str, page_id: str) -> dict:
    response = requests.post(
        BLOGGER_PAGE_PUBLISH_URL.format(blog_id=blog_id, page_id=page_id),
        timeout=60,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    response.raise_for_status()
    return response.json()


def write_report(payload: dict) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    load_env_file(ROOT)
    sync_enabled = env_flag("BLOGGER_SYNC_SITE_PAGES", default=False)
    publish_enabled = env_flag("BLOGGER_SITE_PAGES_PUBLISH", default=False)
    include_optional = env_flag("BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES", default=False)

    if not sync_enabled:
        write_report(
            {
                "synced": False,
                "reason": "BLOGGER_SYNC_SITE_PAGES not enabled",
                "items": [],
            }
        )
        return 0

    try:
        blog_id = ensure_env("BLOGGER_BLOG_ID")
        access_token = refresh_access_token()
    except Exception as exc:  # noqa: BLE001
        write_report(
            {
                "synced": False,
                "reason": str(exc),
                "items": [],
            }
        )
        return 0

    plan_items = load_plan()
    if not plan_items:
        write_report(
            {
                "synced": False,
                "reason": "site-page-publish-plan missing or empty",
                "items": [],
            }
        )
        return 0

    try:
        lookup = existing_pages_lookup(blog_id, access_token)
    except Exception as exc:  # noqa: BLE001
        write_report(
            {
                "synced": False,
                "reason": f"failed_to_list_existing_pages: {exc}",
                "items": [],
            }
        )
        return 0

    results = []
    for item in plan_items:
        if item.get("visibility") != "public_required" and not include_optional:
            results.append(
                {
                    "slug": item.get("slug"),
                    "title": item.get("title"),
                    "synced": False,
                    "reason": "optional_page_skipped",
                    "publish_sequence": item.get("publish_sequence"),
                }
            )
            continue

        html_path = Path(item.get("html_path", ""))
        if not html_path.exists():
            results.append(
                {
                    "slug": item.get("slug"),
                    "title": item.get("title"),
                    "synced": False,
                    "reason": "html_missing",
                    "html_path": str(html_path),
                    "publish_sequence": item.get("publish_sequence"),
                }
            )
            continue

        content = html_path.read_text()
        try:
            existing = find_existing_page(item, lookup)
            if existing:
                remote = update_page(blog_id, access_token, existing["id"], item["title"], content)
                action = "updated"
            else:
                remote = insert_page(blog_id, access_token, item["title"], content)
                action = "created"

            published = False
            published_resource = remote
            if publish_enabled and item.get("visibility") == "public_required":
                published_resource = publish_page(blog_id, access_token, remote["id"])
                published = True

            latest_url = published_resource.get("url") or remote.get("url", "")
            if remote.get("title"):
                lookup[f"title:{remote.get('title', '').strip().lower()}"] = remote
            if latest_url:
                lookup[f"url:{latest_url.strip().lower()}"] = published_resource

            results.append(
                {
                    "slug": item.get("slug"),
                    "title": item.get("title"),
                    "synced": True,
                    "action": action,
                    "published": published,
                    "page_id": remote.get("id"),
                    "url": latest_url,
                    "publish_sequence": item.get("publish_sequence"),
                }
            )
        except Exception as exc:  # noqa: BLE001
            results.append(
                {
                    "slug": item.get("slug"),
                    "title": item.get("title"),
                    "synced": False,
                    "reason": str(exc),
                    "publish_sequence": item.get("publish_sequence"),
                }
            )

    write_report(
        {
            "synced": any(item.get("synced") for item in results),
            "sync_enabled": sync_enabled,
            "publish_enabled": publish_enabled,
            "include_optional": include_optional,
            "items": results,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
