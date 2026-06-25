#!/usr/bin/env python3
import hashlib
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import markdown
from env_loader import load_env_file


ROOT = Path(__file__).resolve().parents[1]
DRAFTS_DIR = ROOT / "outputs/latest/drafts"
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
SEO_PUBLISH_READY_DIR = ROOT / "outputs/latest/seo-publish-ready"
PUBLISH_QUEUE_PATH = ROOT / "outputs/latest/publish-queue.json"
PUBLISH_INVENTORY_PATH = ROOT / "outputs/latest/publish-inventory.json"
REPORT_PATH = ROOT / "outputs/latest/blogger-upload-report.json"
STATE_PATH = ROOT / "outputs/latest/blogger-upload-state.json"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
BLOGGER_POSTS_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"
BLOGGER_POST_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/{post_id}"
BLOGGER_POST_PUBLISH_URL = "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/{post_id}/publish"
KST = timezone(timedelta(hours=9))


def ensure_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is not set")
    return value


def env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name, "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "y", "on"}


def env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return max(0, int(raw))
    except ValueError:
        return default


def refresh_access_token() -> str:
    import requests

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


def markdown_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["extra", "nl2br"])


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
        return stripped[:120]
    return fallback


def upload_post(blog_id: str, access_token: str, title: str, html_body: str, labels: list[str]) -> dict:
    import requests

    response = requests.post(
        BLOGGER_POSTS_URL.format(blog_id=blog_id),
        timeout=60,
        params={"isDraft": "true"},
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json={
            "kind": "blogger#post",
            "title": title,
            "content": html_body,
            "labels": labels,
        },
    )
    response.raise_for_status()
    return response.json()


def update_post(blog_id: str, post_id: str, access_token: str, title: str, html_body: str, labels: list[str]) -> dict:
    import requests

    response = requests.put(
        BLOGGER_POST_URL.format(blog_id=blog_id, post_id=post_id),
        timeout=60,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json={
            "kind": "blogger#post",
            "id": post_id,
            "title": title,
            "content": html_body,
            "labels": labels,
        },
    )
    response.raise_for_status()
    return response.json()


def publish_post(blog_id: str, post_id: str, access_token: str) -> dict:
    import requests

    response = requests.post(
        BLOGGER_POST_PUBLISH_URL.format(blog_id=blog_id, post_id=post_id),
        timeout=60,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    response.raise_for_status()
    return response.json()


def load_sequence_lookup() -> dict[str, int]:
    if PUBLISH_INVENTORY_PATH.exists():
        inventory = json.loads(PUBLISH_INVENTORY_PATH.read_text())
        return {
            item.get("keyword"): item.get("inventory_sequence", 999)
            for item in inventory.get("items", [])
        }
    if PUBLISH_QUEUE_PATH.exists():
        queue = json.loads(PUBLISH_QUEUE_PATH.read_text())
        return {
            item.get("keyword"): item.get("upload_sequence", 999)
            for item in queue.get("items", [])
        }
    return {}


def collect_manifest_files() -> list[Path]:
    if PUBLISH_INVENTORY_PATH.exists():
        inventory = json.loads(PUBLISH_INVENTORY_PATH.read_text())
        manifests = []
        for item in inventory.get("items", []):
            manifest_path = item.get("manifest_path", "")
            if not manifest_path:
                continue
            path = Path(manifest_path)
            if path.exists():
                manifests.append(path)
        if manifests:
            return manifests

    manifests = list(PUBLISH_READY_DIR.glob("*.json")) + list(SEO_PUBLISH_READY_DIR.glob("*.json"))
    if not manifests:
        return []

    sequence_lookup = load_sequence_lookup()
    return sorted(
        manifests,
        key=lambda path: (
            sequence_lookup.get(json.loads(path.read_text()).get("keyword"), 999),
            path.name,
        ),
    )


def build_dry_run_items(manifest_files: list[Path], max_posts_per_run: int) -> list[dict]:
    sequence_lookup = load_sequence_lookup()
    items = []
    for index, manifest_file in enumerate(manifest_files, start=1):
        manifest = json.loads(manifest_file.read_text())
        upload_sequence = sequence_lookup.get(manifest.get("keyword", ""), 999)
        html_path = manifest.get("html_path", "")
        if not manifest.get("ready"):
            reason = manifest.get("reason", "publish_not_ready")
        elif max_posts_per_run and index > max_posts_per_run:
            reason = "BLOGGER_MAX_POSTS_PER_RUN reached"
        else:
            reason = "credentials_missing_dry_run"
        items.append(
            {
                "file": html_path or str(manifest_file),
                "uploaded": False,
                "reason": reason,
                "title": manifest.get("title", ""),
                "keyword": manifest.get("keyword", ""),
                "inventory_type": "seo_followup" if "seo-publish-ready" in str(manifest_file) else "main_post",
                "upload_sequence": upload_sequence,
            }
        )
    return items


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"items": {}}
    return json.loads(STATE_PATH.read_text())


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def content_hash(title: str, html_body: str, labels: list[str]) -> str:
    payload = json.dumps(
        {
            "title": title,
            "html_body": html_body,
            "labels": labels,
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def is_due_for_publish(recommended_publish_date: str) -> bool:
    if not recommended_publish_date:
        return True
    try:
        target = date.fromisoformat(recommended_publish_date)
    except ValueError:
        return True
    return datetime.now(KST).date() >= target


def main() -> int:
    load_env_file(ROOT)
    manifest_files = collect_manifest_files()
    sequence_lookup = load_sequence_lookup()
    auto_publish = env_flag("BLOGGER_AUTO_PUBLISH_POSTS", default=False)
    publish_due_only = env_flag("BLOGGER_PUBLISH_ONLY_DUE_POSTS", default=True)
    max_posts_per_run = env_int("BLOGGER_MAX_POSTS_PER_RUN", default=1)

    try:
        blog_id = ensure_env("BLOGGER_BLOG_ID")
        access_token = refresh_access_token()
    except Exception as exc:  # noqa: BLE001
        REPORT_PATH.write_text(
            json.dumps(
                {
                    "uploaded": False,
                    "reason": str(exc),
                    "items": build_dry_run_items(manifest_files, max_posts_per_run),
                    "summary": {
                        "processed_count": 0,
                        "auto_publish": auto_publish,
                        "publish_due_only": publish_due_only,
                        "max_posts_per_run": max_posts_per_run,
                        "manifest_candidate_count": len(manifest_files),
                    },
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    state = load_state()
    state_items = state.setdefault("items", {})
    results = []
    processed_count = 0

    if manifest_files:
        for manifest_file in manifest_files:
            manifest = json.loads(manifest_file.read_text())
            upload_sequence = sequence_lookup.get(manifest.get("keyword", ""), 999)
            if not manifest.get("ready"):
                results.append(
                    {
                        "file": manifest.get("draft_path", ""),
                        "uploaded": False,
                        "reason": manifest.get("reason", "publish_not_ready"),
                        "upload_sequence": upload_sequence,
                    }
                )
                continue

            html_path = Path(manifest["html_path"])
            if not html_path.exists():
                results.append(
                    {
                        "file": manifest.get("html_path", ""),
                        "uploaded": False,
                        "reason": "rendered_html_missing",
                        "upload_sequence": upload_sequence,
                    }
                )
                continue

            if max_posts_per_run and processed_count >= max_posts_per_run:
                results.append(
                    {
                        "file": manifest.get("html_path", ""),
                        "uploaded": False,
                        "reason": "BLOGGER_MAX_POSTS_PER_RUN reached",
                        "upload_sequence": upload_sequence,
                    }
                )
                continue

            title = manifest.get("meta_title") or manifest.get("title", html_path.stem)
            labels = manifest.get("labels", [])
            html_body = html_path.read_text()
            slug = manifest.get("slug") or manifest.get("keyword") or html_path.stem
            digest = content_hash(title, html_body, labels)
            state_item = state_items.get(slug, {})
            due_for_publish = is_due_for_publish(manifest.get("recommended_publish_date", ""))
            should_publish = auto_publish and (due_for_publish or not publish_due_only)

            if (
                state_item.get("content_hash") == digest
                and state_item.get("published") == should_publish
                and state_item.get("post_id")
            ):
                results.append(
                    {
                        "file": manifest.get("html_path", ""),
                        "uploaded": False,
                        "reason": "already_synced_same_content",
                        "post_id": state_item.get("post_id", ""),
                        "url": state_item.get("url", ""),
                        "title": title,
                        "upload_sequence": upload_sequence,
                    }
                )
                continue

            if state_item.get("post_id"):
                synced = update_post(
                    blog_id,
                    state_item["post_id"],
                    access_token,
                    title,
                    html_body,
                    labels,
                )
                action = "updated_draft"
            else:
                synced = upload_post(
                    blog_id,
                    access_token,
                    title,
                    html_body,
                    labels,
                )
                action = "created_draft"

            published = False
            final_resource = synced
            if should_publish and synced.get("id"):
                final_resource = publish_post(blog_id, synced["id"], access_token)
                published = True
                action = "published"

            processed_count += 1
            state_items[slug] = {
                "slug": slug,
                "keyword": manifest.get("keyword", ""),
                "post_id": final_resource.get("id") or synced.get("id", ""),
                "content_hash": digest,
                "published": published,
                "recommended_publish_date": manifest.get("recommended_publish_date", ""),
                "title": final_resource.get("title") or title,
                "url": final_resource.get("url") or synced.get("url", ""),
                "last_action": action,
                "last_synced_at": datetime.now(timezone.utc).isoformat(),
            }
            results.append(
                {
                    "file": manifest.get("html_path", ""),
                    "uploaded": True,
                    "post_id": final_resource.get("id") or synced.get("id", ""),
                    "url": final_resource.get("url", ""),
                    "title": final_resource.get("title", manifest.get("title", "")),
                    "upload_sequence": upload_sequence,
                    "action": action,
                    "published": published,
                }
            )
    else:
        draft_files = sorted(DRAFTS_DIR.glob("*.md"))
        for draft_file in draft_files:
            text = draft_file.read_text()
            if text.startswith("# Draft not generated"):
                results.append(
                    {
                        "file": str(draft_file),
                        "uploaded": False,
                        "reason": "draft_not_generated",
                    }
                )
                continue

            if max_posts_per_run and processed_count >= max_posts_per_run:
                results.append(
                    {
                        "file": str(draft_file),
                        "uploaded": False,
                        "reason": "BLOGGER_MAX_POSTS_PER_RUN reached",
                    }
                )
                continue

            title = extract_title(text, draft_file.stem)
            html_body = markdown_to_html(text)
            slug = draft_file.stem
            digest = content_hash(title, html_body, [])
            state_item = state_items.get(slug, {})
            if state_item.get("content_hash") == digest and state_item.get("post_id"):
                results.append(
                    {
                        "file": str(draft_file),
                        "uploaded": False,
                        "reason": "already_synced_same_content",
                        "post_id": state_item.get("post_id", ""),
                        "url": state_item.get("url", ""),
                        "title": title,
                    }
                )
                continue

            if state_item.get("post_id"):
                uploaded = update_post(blog_id, state_item["post_id"], access_token, title, html_body, [])
                action = "updated_draft"
            else:
                uploaded = upload_post(blog_id, access_token, title, html_body, [])
                action = "created_draft"
            processed_count += 1
            state_items[slug] = {
                "slug": slug,
                "post_id": uploaded.get("id", ""),
                "content_hash": digest,
                "published": False,
                "title": uploaded.get("title", title),
                "url": uploaded.get("url", ""),
                "last_action": action,
                "last_synced_at": datetime.now(timezone.utc).isoformat(),
            }
            results.append(
                {
                    "file": str(draft_file),
                    "uploaded": True,
                    "post_id": uploaded.get("id"),
                    "url": uploaded.get("url", ""),
                    "title": uploaded.get("title", title),
                    "action": action,
                }
            )

    save_state(state)
    REPORT_PATH.write_text(
        json.dumps(
            {
                "items": results,
                "summary": {
                    "processed_count": processed_count,
                    "auto_publish": auto_publish,
                    "publish_due_only": publish_due_only,
                    "max_posts_per_run": max_posts_per_run,
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
