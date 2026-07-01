#!/usr/bin/env python3
import csv
import json
import os
from datetime import date, timedelta
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import requests
from requests import HTTPError


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "data/search_console_queries.csv"
OUTPUT_JSON = ROOT / "outputs/latest/search-console-fetch-report.json"
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
ENV_PATH = ROOT / ".env"
SEARCH_CONSOLE_URL = "https://www.googleapis.com/webmasters/v3/sites/{site_url}/searchAnalytics/query"
SEARCH_CONSOLE_SITES_URL = "https://www.googleapis.com/webmasters/v3/sites"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"


def load_env_file() -> None:
    if not ENV_PATH.exists():
        return
    for raw_line in ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key and key not in os.environ:
            os.environ[key] = value.strip().strip("'").strip('"')


def getenv_any(*names: str) -> str:
    for name in names:
        value = os.getenv(name, "").strip()
        if value:
            return value
    return ""


def write_report(payload: dict) -> None:
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def normalize_site_url(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    if not value.endswith("/"):
        value += "/"
    return value


def infer_site_url() -> tuple[str, str]:
    explicit = getenv_any("SEARCH_CONSOLE_SITE_URL")
    if explicit:
        return normalize_site_url(explicit), "SEARCH_CONSOLE_SITE_URL"

    blog_base_url = getenv_any("BLOG_BASE_URL", "BLOGGER_PUBLIC_URL")
    if blog_base_url:
        return normalize_site_url(blog_base_url), "BLOG_BASE_URL"

    state = load_json(BLOGGER_STATE_JSON)
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    for item in rows:
        url = item.get("url", "")
        if not url.startswith("http"):
            continue
        parts = url.split("/")
        if len(parts) >= 3:
            return normalize_site_url("/".join(parts[:3])), "blogger_upload_state"
    return "", ""


def origin_without_trailing_slash(value: str) -> str:
    return normalize_site_url(value).rstrip("/")


def site_url_matches(candidate: str, inferred: str) -> bool:
    candidate_norm = origin_without_trailing_slash(candidate)
    inferred_norm = origin_without_trailing_slash(inferred)
    if not candidate_norm or not inferred_norm:
        return False
    if candidate_norm == inferred_norm:
        return True
    return candidate_norm.startswith("sc-domain:") and inferred_norm.endswith(candidate_norm.removeprefix("sc-domain:"))


def refresh_access_token() -> str:
    existing = getenv_any("SEARCH_CONSOLE_ACCESS_TOKEN", "GOOGLE_ACCESS_TOKEN")
    if existing:
        return existing

    client_id = getenv_any("SEARCH_CONSOLE_CLIENT_ID", "GOOGLE_CLIENT_ID")
    client_secret = getenv_any("SEARCH_CONSOLE_CLIENT_SECRET", "GOOGLE_CLIENT_SECRET")
    refresh_token = getenv_any("SEARCH_CONSOLE_REFRESH_TOKEN", "GOOGLE_REFRESH_TOKEN")

    if not client_id or not client_secret or not refresh_token:
        raise RuntimeError("Search Console OAuth credentials are not set")

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
        raise RuntimeError("Failed to obtain Search Console access token")
    return token


def list_accessible_sites(access_token: str) -> list[dict]:
    response = requests.get(
        SEARCH_CONSOLE_SITES_URL,
        timeout=30,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    response.raise_for_status()
    return response.json().get("siteEntry", [])


def choose_accessible_site_url(inferred_site_url: str, accessible_sites: list[dict]) -> tuple[str, str]:
    for site in accessible_sites:
        candidate = site.get("siteUrl", "")
        if site_url_matches(candidate, inferred_site_url):
            return candidate, "search_console_sites_match"
    return inferred_site_url, ""


def http_status_code(exc: Exception) -> Optional[int]:
    if isinstance(exc, HTTPError) and exc.response is not None:
        return exc.response.status_code
    response = getattr(exc, "response", None)
    if response is not None:
        return getattr(response, "status_code", None)
    return None


def query_rows(site_url: str, access_token: str, start_date: str, end_date: str) -> list:
    all_rows = []
    start_row = 0

    while True:
        response = requests.post(
            SEARCH_CONSOLE_URL.format(site_url=quote(site_url, safe="")),
            timeout=60,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json={
                "startDate": start_date,
                "endDate": end_date,
                "dimensions": ["query"],
                "rowLimit": 250,
                "startRow": start_row,
            },
        )
        response.raise_for_status()
        payload = response.json()
        rows = payload.get("rows", [])
        if not rows:
            break
        all_rows.extend(rows)
        start_row += len(rows)
        if len(rows) < 250:
            break

    return all_rows


def main() -> int:
    load_env_file()
    site_url, site_url_source = infer_site_url()
    if not site_url:
        write_report(
            {
                "available": False,
                "reason": "Search Console site URL is not set and could not be inferred",
                "rows_written": 0,
                "site_url_source": "",
            }
        )
        return 0

    try:
        access_token = refresh_access_token()
    except Exception as exc:  # noqa: BLE001
        write_report({"available": False, "reason": str(exc), "rows_written": 0, "site_url": site_url, "site_url_source": site_url_source})
        return 0

    accessible_sites = []
    accessible_sites_error = ""
    try:
        accessible_sites = list_accessible_sites(access_token)
    except Exception as exc:  # noqa: BLE001
        accessible_sites_error = str(exc)
    else:
        if not accessible_sites:
            write_report(
                {
                    "available": False,
                    "reason": "no_accessible_search_console_sites",
                    "action_required": "Search Console에서 블로그 URL-prefix 속성을 같은 Google 계정으로 등록/검증하세요.",
                    "rows_written": 0,
                    "site_url": site_url,
                    "site_url_source": site_url_source,
                    "start_date": "",
                    "end_date": "",
                    "accessible_sites": [],
                    "accessible_sites_error": "",
                }
            )
            return 0
        selected_site_url, selected_source = choose_accessible_site_url(site_url, accessible_sites)
        if selected_source:
            site_url = selected_site_url
            site_url_source = selected_source

    lag_days = int(os.getenv("SEARCH_CONSOLE_LAG_DAYS", "3"))
    window_days = int(os.getenv("SEARCH_CONSOLE_WINDOW_DAYS", "7"))
    end = date.today() - timedelta(days=lag_days)
    start = end - timedelta(days=window_days - 1)

    try:
        rows = query_rows(site_url, access_token, start.isoformat(), end.isoformat())
    except Exception as exc:  # noqa: BLE001
        write_report(
            {
                "available": False,
                "reason": str(exc),
                "status_code": http_status_code(exc),
                "rows_written": 0,
                "site_url": site_url,
                "site_url_source": site_url_source,
                "start_date": start.isoformat(),
                "end_date": end.isoformat(),
                "accessible_sites": accessible_sites,
                "accessible_sites_error": accessible_sites_error,
            }
        )
        return 0

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=["query", "clicks", "impressions", "ctr", "position"])
        writer.writeheader()
        for row in rows:
            keys = row.get("keys", [])
            writer.writerow(
                {
                    "query": keys[0] if keys else "",
                    "clicks": row.get("clicks", 0),
                    "impressions": row.get("impressions", 0),
                    "ctr": row.get("ctr", 0),
                    "position": row.get("position", 0),
                }
            )

    write_report(
        {
            "available": True,
            "rows_written": len(rows),
            "site_url": site_url,
            "site_url_source": site_url_source,
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "accessible_sites": accessible_sites,
            "accessible_sites_error": accessible_sites_error,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
