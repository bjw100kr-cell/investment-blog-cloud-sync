#!/usr/bin/env python3
import hashlib
import json
import os
import random
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

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
REVIEW_APPROVALS_PATH = ROOT / "outputs/latest/review-approvals.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
SOURCE_FRESHNESS_BOARD_JSON = ROOT / "outputs/latest/source-freshness-board.json"
PUBLISH_READY_REPORT_JSON = ROOT / "outputs/latest/publish-ready-report.json"
SEO_PUBLISH_READY_REPORT_JSON = ROOT / "outputs/latest/seo-publish-ready-report.json"
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


def env_float(name: str, default: float) -> float:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return max(0.0, float(raw))
    except ValueError:
        return default


def env_csv_set(name: str) -> set[str]:
    raw = os.getenv(name, "").strip()
    if not raw:
        return set()
    return {item.strip() for item in raw.split(",") if item.strip()}


def parse_retry_after(value: str) -> float:
    if not value:
        return 0.0
    try:
        return float(value)
    except ValueError:
        pass

    # Retry-After can be an HTTP date.
    from email.utils import parsedate_to_datetime
    import datetime as _dt

    try:
        target = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        return 0.0
    if target.tzinfo is None:
        target = target.replace(tzinfo=_dt.timezone.utc)
    delta = (target - datetime.now(timezone.utc)).total_seconds()
    return max(0.0, delta)


def request_error_message(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if response is None:
        return str(exc)
    body = getattr(response, "text", "") or ""
    return f"{exc} :: {body[:500]}"


def api_request_with_retry(
    method: str,
    url: str,
    *,
    max_attempts: int,
    backoff_base: float,
    backoff_max: float,
    params: Optional[dict[str, str]] = None,
    headers: Optional[dict[str, str]] = None,
    json_payload: Optional[dict[str, Any]] = None,
    timeout: int = 60,
) -> tuple[bool, Optional[object], str]:
    import requests

    delay = backoff_base
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.request(
                method,
                url,
                params=params,
                headers=headers,
                json=json_payload,
                timeout=timeout,
            )
            if response.status_code == 429:
                if attempt >= max_attempts:
                    return (
                        False,
                        None,
                        f"Blogger API 429 after {attempt} attempts: {response.text[:200]}",
                    )
                retry_after = parse_retry_after(response.headers.get("Retry-After", ""))
                wait_seconds = retry_after if retry_after > 0 else delay
                jitter = random.uniform(0, 0.2 * max(wait_seconds, 1.0))
                time.sleep(wait_seconds + jitter)
                delay = min(backoff_max, delay * 2)
                continue

            response.raise_for_status()
            payload_data = response.json()
            return True, payload_data, ""
        except (requests.RequestException, ValueError) as exc:  # noqa: BLE001
            if attempt >= max_attempts:
                return False, None, request_error_message(exc)
            jitter = random.uniform(0, min(1.0, delay))
            time.sleep(delay + jitter)
            delay = min(backoff_max, delay * 2)
    return False, None, "unknown retry failure"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def find_state_item(state_items: dict, slug: str, keyword: str) -> dict:
    if slug in state_items:
        return state_items.get(slug, {})
    matches = [
        item
        for item in state_items.values()
        if isinstance(item, dict) and keyword and item.get("keyword") == keyword
    ]
    if not matches:
        return {}
    matches.sort(key=lambda item: parse_timestamp(item.get("last_synced_at", "")))
    return matches[0]


def parse_timestamp(value: str) -> datetime:
    if not value:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def is_inventory_stale() -> bool:
    inventory = load_json(PUBLISH_INVENTORY_PATH)
    if not inventory.get("items"):
        return True

    inventory_generated = parse_timestamp(inventory.get("generated_at", ""))
    source_timestamps = [
        parse_timestamp(load_json(PUBLISH_READY_REPORT_JSON).get("generated_at", "")),
        parse_timestamp(load_json(SEO_PUBLISH_READY_REPORT_JSON).get("generated_at", "")),
    ]

    if not any(t != parse_timestamp("") for t in source_timestamps):
        return False

    newest_source = max(source_timestamps)
    return newest_source > inventory_generated


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
    success, payload, error = api_request_with_retry(
        "POST",
        BLOGGER_POSTS_URL.format(blog_id=blog_id),
        max_attempts=env_int("BLOGGER_API_MAX_ATTEMPTS", default=4),
        backoff_base=env_float("BLOGGER_API_BACKOFF_BASE_SECONDS", default=1.5),
        backoff_max=env_float("BLOGGER_API_BACKOFF_MAX_SECONDS", default=20.0),
        params={"isDraft": "true"},
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json_payload={
            "kind": "blogger#post",
            "title": title,
            "content": html_body,
            "labels": labels,
        },
    )
    if not success:
        raise RuntimeError(error)
    return payload


def update_post(blog_id: str, post_id: str, access_token: str, title: str, html_body: str, labels: list[str]) -> dict:
    success, payload, error = api_request_with_retry(
        "PUT",
        BLOGGER_POST_URL.format(blog_id=blog_id, post_id=post_id),
        max_attempts=env_int("BLOGGER_API_MAX_ATTEMPTS", default=4),
        backoff_base=env_float("BLOGGER_API_BACKOFF_BASE_SECONDS", default=1.5),
        backoff_max=env_float("BLOGGER_API_BACKOFF_MAX_SECONDS", default=20.0),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json_payload={
            "kind": "blogger#post",
            "id": post_id,
            "title": title,
            "content": html_body,
            "labels": labels,
        },
    )
    if not success:
        raise RuntimeError(error)
    return payload


def publish_post(blog_id: str, post_id: str, access_token: str) -> dict:
    success, payload, error = api_request_with_retry(
        "POST",
        BLOGGER_POST_PUBLISH_URL.format(blog_id=blog_id, post_id=post_id),
        max_attempts=env_int("BLOGGER_API_MAX_ATTEMPTS", default=4),
        backoff_base=env_float("BLOGGER_API_BACKOFF_BASE_SECONDS", default=1.5),
        backoff_max=env_float("BLOGGER_API_BACKOFF_MAX_SECONDS", default=20.0),
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    if not success:
        raise RuntimeError(error)
    return payload


def load_sequence_lookup() -> dict[str, int]:
    if PUBLISH_INVENTORY_PATH.exists():
        inventory = load_json(PUBLISH_INVENTORY_PATH)
        return {
            item.get("keyword"): item.get("inventory_sequence", 999)
            for item in inventory.get("items", [])
        }
    if PUBLISH_QUEUE_PATH.exists():
        queue = load_json(PUBLISH_QUEUE_PATH)
        return {
            item.get("keyword"): item.get("upload_sequence", 999)
            for item in queue.get("items", [])
        }
    return {}


def _manifest_inventory_key(manifest: dict, path: Path) -> str:
    slug = manifest.get("slug") or ""
    keyword = manifest.get("keyword") or ""
    return (slug + "::" + keyword + "::" + path.stem).strip(":")


def _parse_manifest(path: Path) -> tuple[dict, bool]:
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}, False
    return payload, True


def _manifest_sort_key(path: Path, sequence_lookup: dict[str, int], stale_orphan: bool) -> tuple:
    if not stale_orphan:
        manifest, ok = _parse_manifest(path)
        if not ok:
            return (9999, path.name)
        key = manifest.get("keyword", "")
        return (
            sequence_lookup.get(key, 999),
            sequence_lookup.get(path.stem, 999),
            path.name,
        )
    manifest, ok = _parse_manifest(path)
    if not ok:
        return (9999, 999, path.name)
    upload_sequence = sequence_lookup.get(manifest.get("keyword", ""), 999)
    manifest_date = manifest.get("recommended_publish_date", "9999-12-31")
    return (upload_sequence, manifest_date, path.name)


def manifest_matches_keyword_filter(manifest: dict, keyword_filter: set[str]) -> bool:
    if not keyword_filter:
        return True
    candidates = {
        manifest.get("keyword", ""),
        manifest.get("slug", ""),
        Path(manifest.get("html_path", "")).stem,
    }
    return any(candidate in keyword_filter for candidate in candidates if candidate)


def collect_manifest_files(keyword_filter: Optional[set[str]] = None) -> list[Path]:
    keyword_filter = keyword_filter or set()
    sequence_lookup = load_sequence_lookup()
    stale = is_inventory_stale()
    include_orphans = env_flag("BLOGGER_INCLUDE_ORPHAN_MANIFESTS", False)
    seen = set()
    selected: list[Path] = []

    if PUBLISH_INVENTORY_PATH.exists():
        inventory = load_json(PUBLISH_INVENTORY_PATH)
        for item in inventory.get("items", []):
            manifest_path = item.get("manifest_path", "")
            if not manifest_path:
                continue
            path = Path(manifest_path)
            manifest, ok = _parse_manifest(path)
            if not ok:
                continue
            if not manifest_matches_keyword_filter(manifest, keyword_filter):
                continue
            key = _manifest_inventory_key(manifest, path)
            if key not in seen:
                selected.append(path)
                seen.add(key)

    if include_orphans and (not selected or stale):
        all_manifests = list(PUBLISH_READY_DIR.glob("*.json")) + list(SEO_PUBLISH_READY_DIR.glob("*.json"))
        for path in all_manifests:
            manifest, ok = _parse_manifest(path)
            if not ok:
                continue
            if not manifest_matches_keyword_filter(manifest, keyword_filter):
                continue
            key = _manifest_inventory_key(manifest, path)
            if key in seen:
                continue
            selected.append(path)
            seen.add(key)

    if not selected:
        return []

    return sorted(selected, key=lambda path: _manifest_sort_key(path, sequence_lookup, stale))


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


def load_quality_gate_statuses() -> dict[str, str]:
    if not PRE_PUBLISH_QUALITY_GATE_JSON.exists():
        return {}
    payload = json.loads(PRE_PUBLISH_QUALITY_GATE_JSON.read_text())
    statuses: dict[str, str] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        html_path = item.get("html_path", "")
        status = item.get("status", "")
        source_group = item.get("source_group", "")
        if keyword and status:
            statuses[keyword] = status
            statuses[f"{keyword}:{source_group}"] = status
        if html_path:
            statuses[Path(html_path).stem] = status
    return statuses


def append_failure(result_items: list[dict], manifest: dict, reason: str, upload_sequence: int) -> None:
    result_items.append(
        {
            "file": manifest.get("html_path", ""),
            "uploaded": False,
            "reason": reason,
            "keyword": manifest.get("keyword", ""),
            "title": manifest.get("title", ""),
            "upload_sequence": upload_sequence,
        }
    )


def load_freshness_statuses() -> dict[str, str]:
    if not SOURCE_FRESHNESS_BOARD_JSON.exists():
        return {}
    payload = json.loads(SOURCE_FRESHNESS_BOARD_JSON.read_text())
    statuses: dict[str, str] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        status = item.get("freshness_status", "")
        if keyword and status:
            statuses[keyword] = status
    return statuses


def quality_gate_check(manifest: dict, quality_statuses: dict[str, str]) -> tuple[bool, str]:
    if not quality_statuses:
        return True, ""
    keyword = manifest.get("keyword", "")
    html_path = manifest.get("html_path", "")
    source_group = "seo_followup" if "seo-publish-ready" in html_path else "main"
    status = quality_statuses.get(keyword) or quality_statuses.get(f"{keyword}:{source_group}") or quality_statuses.get(
        Path(html_path).stem if html_path else ""
    )
    if not status:
        return True, ""
    if status == "needs_fix":
        return False, "pre_publish_quality_gate_needs_fix"
    if status == "review_before_publish":
        return False, "pre_publish_quality_gate_review"
    return True, ""


def freshness_check(manifest: dict, freshness_statuses: dict[str, str]) -> tuple[bool, str]:
    if not freshness_statuses:
        return True, ""
    status = freshness_statuses.get(manifest.get("keyword", ""))
    if status == "stale":
        return False, "source_freshness_stale"
    return True, ""


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"items": {}}
    return json.loads(STATE_PATH.read_text())


def load_review_approvals() -> dict:
    if not REVIEW_APPROVALS_PATH.exists():
        return {
            "user_final_confirmation_required": True,
            "user_confirmed_all": False,
            "user_confirmed_keywords": [],
            "approved_all": False,
            "approved_keywords": [],
        }
    payload = json.loads(REVIEW_APPROVALS_PATH.read_text())
    payload.setdefault("user_final_confirmation_required", True)
    payload.setdefault("user_confirmed_all", payload.get("approved_all", False))
    payload.setdefault("user_confirmed_keywords", payload.get("approved_keywords", []))
    payload.setdefault("approved_all", False)
    payload.setdefault("approved_keywords", [])
    return payload


def is_approved_for_upload(manifest: dict, approvals: dict) -> bool:
    if approvals.get("user_confirmed_all", approvals.get("approved_all", False)):
        return True
    approved_keywords = set(approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", [])))
    candidates = {
        manifest.get("keyword", ""),
        manifest.get("slug", ""),
        Path(manifest.get("html_path", "")).stem,
    }
    return any(candidate in approved_keywords for candidate in candidates if candidate)


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
    only_keywords = env_csv_set("BLOGGER_ONLY_KEYWORDS")
    manifest_files = collect_manifest_files(only_keywords)
    sequence_lookup = load_sequence_lookup()
    quality_statuses = load_quality_gate_statuses()
    freshness_statuses = load_freshness_statuses()
    allow_reupload_same_content = env_flag("BLOGGER_ALLOW_REUPLOAD_SAME_CONTENT", default=False)
    review_required = env_flag("BLOGGER_REQUIRE_REVIEW_APPROVAL", default=True)
    approvals = load_review_approvals()
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
                        "review_required": review_required,
                        "only_keywords": sorted(only_keywords),
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
            upload_sequence = 999
            manifest = {}
            try:
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

                quality_ok, reason = quality_gate_check(manifest, quality_statuses)
                if not quality_ok:
                    results.append(
                        {
                            "file": manifest.get("html_path", ""),
                            "uploaded": False,
                            "reason": reason,
                            "keyword": manifest.get("keyword", ""),
                            "title": manifest.get("title", ""),
                            "upload_sequence": upload_sequence,
                        }
                    )
                    continue

                freshness_ok, reason = freshness_check(manifest, freshness_statuses)
                if not freshness_ok:
                    results.append(
                        {
                            "file": manifest.get("html_path", ""),
                            "uploaded": False,
                            "reason": reason,
                            "keyword": manifest.get("keyword", ""),
                            "title": manifest.get("title", ""),
                            "upload_sequence": upload_sequence,
                        }
                    )
                    continue

                if review_required and not is_approved_for_upload(manifest, approvals):
                    results.append(
                        {
                            "file": manifest.get("html_path", ""),
                            "uploaded": False,
                            "reason": "awaiting_user_review_approval",
                            "keyword": manifest.get("keyword", ""),
                            "title": manifest.get("title", ""),
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
                state_item = find_state_item(state_items, slug, manifest.get("keyword", ""))
                due_for_publish = is_due_for_publish(manifest.get("recommended_publish_date", ""))
                should_publish = auto_publish and (due_for_publish or not publish_due_only)
                same_content = state_item.get("content_hash") == digest
                same_publish_state = state_item.get("published") == should_publish

                if (
                    not allow_reupload_same_content
                    and same_content
                    and same_publish_state
                    and state_item.get("post_id")
                ):
                    results.append(
                        {
                            "file": manifest.get("html_path", ""),
                            "uploaded": False,
                            "reason": (
                                "already_synced_same_content"
                                if not allow_reupload_same_content
                                else "ready_to_update_same_content"
                            ),
                            "post_id": state_item.get("post_id", ""),
                            "url": state_item.get("url", ""),
                            "post_url": state_item.get("url", ""),
                            "title": title,
                            "upload_sequence": upload_sequence,
                            "slug": slug,
                            "keyword": manifest.get("keyword", ""),
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
                        "post_url": final_resource.get("url", ""),
                        "title": final_resource.get("title", manifest.get("title", "")),
                        "upload_sequence": upload_sequence,
                        "action": action,
                        "published": published,
                        "slug": slug,
                        "keyword": manifest.get("keyword", ""),
                    }
                )
            except (KeyError, TypeError, RuntimeError) as exc:
                append_failure(
                    results,
                    manifest,
                    f"upload_error::{type(exc).__name__}: {str(exc)}",
                    upload_sequence,
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
            if (
                not allow_reupload_same_content
                and state_item.get("content_hash") == digest
                and state_item.get("post_id")
            ):
                results.append(
                    {
                        "file": str(draft_file),
                        "uploaded": False,
                        "reason": "already_synced_same_content",
                        "post_id": state_item.get("post_id", ""),
                        "url": state_item.get("url", ""),
                        "post_url": state_item.get("url", ""),
                        "title": title,
                        "slug": slug,
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
                    "post_url": uploaded.get("url", ""),
                    "title": uploaded.get("title", title),
                    "action": action,
                    "slug": slug,
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
                        "allow_reupload_same_content": allow_reupload_same_content,
                        "review_required": review_required,
                        "only_keywords": sorted(only_keywords),
                        "approval_file_present": REVIEW_APPROVALS_PATH.exists(),
                        "user_final_confirmation_required": review_required
                        and approvals.get("user_final_confirmation_required", True),
                        "user_confirmed_all": approvals.get("user_confirmed_all", approvals.get("approved_all", False)),
                    "user_confirmed_keywords": approvals.get(
                        "user_confirmed_keywords", approvals.get("approved_keywords", [])
                    ),
                    "approved_all": approvals.get("approved_all", False),
                    "approved_keywords": approvals.get("approved_keywords", []),
                    "quality_gate_blocked": [
                        item.get("reason", "")
                        for item in results
                        if item.get("reason", "").startswith("pre_publish_quality_gate")
                    ],
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
