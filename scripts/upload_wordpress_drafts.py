#!/usr/bin/env python3
import base64
import hashlib
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import markdown
from env_loader import load_env_file


ROOT = Path(__file__).resolve().parents[1]
DRAFTS_DIR = ROOT / "outputs/latest/drafts"
PUBLISH_READY_DIR = ROOT / "outputs/latest/publish-ready"
SEO_PUBLISH_READY_DIR = ROOT / "outputs/latest/seo-publish-ready"
PUBLISH_QUEUE_PATH = ROOT / "outputs/latest/publish-queue.json"
PUBLISH_INVENTORY_PATH = ROOT / "outputs/latest/publish-inventory.json"
REPORT_PATH = ROOT / "outputs/latest/wordpress-upload-report.json"
STATE_PATH = ROOT / "outputs/latest/wordpress-upload-state.json"
REVIEW_APPROVALS_PATH = ROOT / "outputs/latest/review-approvals.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
SOURCE_FRESHNESS_BOARD_JSON = ROOT / "outputs/latest/source-freshness-board.json"
KST = timezone(timedelta(hours=9))

CATEGORY_NAME_MAP = {
    "macro": "거시경제",
    "crypto": "코인",
    "global-sector": "글로벌섹터",
}


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


def wordpress_base_url(site_url: str) -> str:
    return f"{site_url.rstrip('/')}/wp-json/wp/v2"


def wordpress_auth_header(username: str, application_password: str) -> str:
    token = base64.b64encode(f"{username}:{application_password}".encode("utf-8")).decode("ascii")
    return f"Basic {token}"


def request_json(
    method: str,
    url: str,
    auth_header: str,
    params: Optional[dict] = None,
    json_body: Optional[dict] = None,
) -> dict:
    import requests

    response = requests.request(
        method,
        url,
        timeout=60,
        headers={
            "Authorization": auth_header,
            "Content-Type": "application/json",
        },
        params=params,
        json=json_body,
    )
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, dict):
        return payload
    raise RuntimeError(f"Unexpected response type from WordPress endpoint: {url}")


def request_json_list(method: str, url: str, auth_header: str, params: Optional[dict] = None) -> list[dict]:
    import requests

    response = requests.request(
        method,
        url,
        timeout=60,
        headers={
            "Authorization": auth_header,
        },
        params=params,
    )
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, list):
        return payload
    raise RuntimeError(f"Unexpected list response type from WordPress endpoint: {url}")


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
            reason = "WORDPRESS_MAX_POSTS_PER_RUN reached"
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


def content_hash(title: str, html_body: str, labels: list[str], excerpt: str, status: str) -> str:
    payload = json.dumps(
        {
            "title": title,
            "html_body": html_body,
            "labels": labels,
            "excerpt": excerpt,
            "status": status,
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


def normalize_term_name(name: str) -> str:
    return " ".join(name.strip().split()).casefold()


def ensure_term_ids(site_url: str, auth_header: str, taxonomy: str, names: list[str]) -> list[int]:
    endpoint = f"{wordpress_base_url(site_url)}/{taxonomy}"
    term_ids: list[int] = []
    seen: set[int] = set()

    for name in names:
        cleaned = name.strip()
        if not cleaned:
            continue
        normalized = normalize_term_name(cleaned)
        matches = request_json_list("GET", endpoint, auth_header, params={"search": cleaned, "per_page": 100})
        matched = next(
            (
                item
                for item in matches
                if normalize_term_name(str(item.get("name", ""))) == normalized
            ),
            None,
        )
        if matched is None:
            matched = request_json("POST", endpoint, auth_header, json_body={"name": cleaned})
        term_id = int(matched.get("id", 0))
        if term_id and term_id not in seen:
            seen.add(term_id)
            term_ids.append(term_id)
    return term_ids


def build_category_names(manifest: dict) -> list[str]:
    category_key = manifest.get("category", "").strip()
    if not category_key:
        return []
    return [CATEGORY_NAME_MAP.get(category_key, category_key)]


def create_post(site_url: str, auth_header: str, payload: dict) -> dict:
    return request_json("POST", f"{wordpress_base_url(site_url)}/posts", auth_header, json_body=payload)


def update_post(site_url: str, post_id: int, auth_header: str, payload: dict) -> dict:
    return request_json("POST", f"{wordpress_base_url(site_url)}/posts/{post_id}", auth_header, json_body=payload)


def main() -> int:
    load_env_file(ROOT)
    manifest_files = collect_manifest_files()
    sequence_lookup = load_sequence_lookup()
    quality_statuses = load_quality_gate_statuses()
    freshness_statuses = load_freshness_statuses()
    review_required = env_flag("WORDPRESS_REQUIRE_REVIEW_APPROVAL", default=True)
    approvals = load_review_approvals()
    auto_publish = env_flag("WORDPRESS_AUTO_PUBLISH_POSTS", default=False)
    publish_due_only = env_flag("WORDPRESS_PUBLISH_ONLY_DUE_POSTS", default=True)
    max_posts_per_run = env_int("WORDPRESS_MAX_POSTS_PER_RUN", default=1)

    try:
        site_url = ensure_env("WORDPRESS_SITE_URL")
        username = ensure_env("WORDPRESS_USERNAME")
        application_password = ensure_env("WORDPRESS_APPLICATION_PASSWORD")
        auth_header = wordpress_auth_header(username, application_password)
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
                        "reason": "WORDPRESS_MAX_POSTS_PER_RUN reached",
                        "upload_sequence": upload_sequence,
                    }
                )
                continue

            title = manifest.get("meta_title") or manifest.get("title", html_path.stem)
            labels = manifest.get("labels", [])
            category_names = build_category_names(manifest)
            html_body = html_path.read_text()
            slug = manifest.get("slug") or manifest.get("keyword") or html_path.stem
            excerpt = manifest.get("meta_description") or manifest.get("summary_angle") or ""
            due_for_publish = is_due_for_publish(manifest.get("recommended_publish_date", ""))
            status = "publish" if auto_publish and (due_for_publish or not publish_due_only) else "draft"
            digest = content_hash(title, html_body, labels, excerpt, status)
            state_item = state_items.get(slug, {})

            if (
                state_item.get("content_hash") == digest
                and state_item.get("status") == status
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

            tag_ids = ensure_term_ids(site_url, auth_header, "tags", labels)
            category_ids = ensure_term_ids(site_url, auth_header, "categories", category_names)
            payload = {
                "title": title,
                "content": html_body,
                "slug": slug,
                "status": status,
                "excerpt": excerpt,
                "tags": tag_ids,
                "categories": category_ids,
            }

            if state_item.get("post_id"):
                synced = update_post(site_url, int(state_item["post_id"]), auth_header, payload)
                action = "updated_post"
            else:
                synced = create_post(site_url, auth_header, payload)
                action = "created_post"

            processed_count += 1
            link = synced.get("link", "")
            post_id = synced.get("id", "")
            state_items[slug] = {
                "slug": slug,
                "keyword": manifest.get("keyword", ""),
                "post_id": post_id,
                "content_hash": digest,
                "status": status,
                "recommended_publish_date": manifest.get("recommended_publish_date", ""),
                "title": synced.get("title", {}).get("rendered", title) if isinstance(synced.get("title"), dict) else title,
                "url": link,
                "last_action": action,
                "last_synced_at": datetime.now(timezone.utc).isoformat(),
            }
            results.append(
                {
                    "file": manifest.get("html_path", ""),
                    "uploaded": True,
                    "post_id": post_id,
                    "url": link,
                    "title": title,
                    "upload_sequence": upload_sequence,
                    "action": action,
                    "published": status == "publish",
                    "status": status,
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
                        "reason": "WORDPRESS_MAX_POSTS_PER_RUN reached",
                    }
                )
                continue

            title = extract_title(text, draft_file.stem)
            html_body = markdown_to_html(text)
            slug = draft_file.stem
            status = "draft"
            digest = content_hash(title, html_body, [], "", status)
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

            payload = {
                "title": title,
                "content": html_body,
                "slug": slug,
                "status": status,
            }
            if state_item.get("post_id"):
                uploaded = update_post(site_url, int(state_item["post_id"]), auth_header, payload)
                action = "updated_post"
            else:
                uploaded = create_post(site_url, auth_header, payload)
                action = "created_post"

            processed_count += 1
            state_items[slug] = {
                "slug": slug,
                "post_id": uploaded.get("id", ""),
                "content_hash": digest,
                "status": status,
                "title": title,
                "url": uploaded.get("link", ""),
                "last_action": action,
                "last_synced_at": datetime.now(timezone.utc).isoformat(),
            }
            results.append(
                {
                    "file": str(draft_file),
                    "uploaded": True,
                    "post_id": uploaded.get("id"),
                    "url": uploaded.get("link", ""),
                    "title": title,
                    "action": action,
                    "status": status,
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
                    "review_required": review_required,
                    "approval_file_present": REVIEW_APPROVALS_PATH.exists(),
                    "user_final_confirmation_required": approvals.get("user_final_confirmation_required", True),
                    "user_confirmed_all": approvals.get("user_confirmed_all", approvals.get("approved_all", False)),
                    "user_confirmed_keywords": approvals.get(
                        "user_confirmed_keywords", approvals.get("approved_keywords", [])
                    ),
                    "approved_all": approvals.get("approved_all", False),
                    "approved_keywords": approvals.get("approved_keywords", []),
                    "site_url": site_url,
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
