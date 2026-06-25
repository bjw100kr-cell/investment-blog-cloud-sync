#!/usr/bin/env python3
import csv
import json
import os
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import quote

import requests


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "data/search_console_queries.csv"
OUTPUT_JSON = ROOT / "outputs/latest/search-console-fetch-report.json"
SEARCH_CONSOLE_URL = "https://www.googleapis.com/webmasters/v3/sites/{site_url}/searchAnalytics/query"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"


def getenv_any(*names: str) -> str:
    for name in names:
        value = os.getenv(name, "").strip()
        if value:
            return value
    return ""


def write_report(payload: dict) -> None:
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))


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
    site_url = getenv_any("SEARCH_CONSOLE_SITE_URL")
    if not site_url:
        write_report({"available": False, "reason": "SEARCH_CONSOLE_SITE_URL is not set", "rows_written": 0})
        return 0

    try:
        access_token = refresh_access_token()
    except Exception as exc:  # noqa: BLE001
        write_report({"available": False, "reason": str(exc), "rows_written": 0})
        return 0

    lag_days = int(os.getenv("SEARCH_CONSOLE_LAG_DAYS", "3"))
    window_days = int(os.getenv("SEARCH_CONSOLE_WINDOW_DAYS", "7"))
    end = date.today() - timedelta(days=lag_days)
    start = end - timedelta(days=window_days - 1)

    try:
        rows = query_rows(site_url, access_token, start.isoformat(), end.isoformat())
    except Exception as exc:  # noqa: BLE001
        write_report({"available": False, "reason": str(exc), "rows_written": 0})
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
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
