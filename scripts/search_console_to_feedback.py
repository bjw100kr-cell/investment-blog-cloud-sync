#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/investment_sources.json"
INPUT_CSV = ROOT / "data/search_console_queries.csv"
OUTPUT_CSV = ROOT / "data/performance_signals.csv"
OUTPUT_JSON = ROOT / "outputs/latest/search-console-conversion-report.json"
OUTPUT_MD = ROOT / "outputs/latest/search-console-conversion-report.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def normalize_header(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def parse_percent(value: str) -> float:
    value = (value or "").strip().replace("%", "")
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_float(value: str) -> float:
    value = (value or "").replace(",", "").strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


def find_keywords(text: str, aliases: dict) -> list:
    haystack = (text or "").lower()
    hits = []
    for canonical, variations in aliases.items():
        for variant in variations:
            if variant.lower() in haystack:
                hits.append(canonical)
                break
    return hits


def detect_columns(fieldnames: list) -> dict:
    mapping = {}
    normalized = {normalize_header(name): name for name in fieldnames}

    candidates = {
        "query": ["query", "queries", "searchquery", "topqueries"],
        "clicks": ["clicks"],
        "impressions": ["impressions"],
        "ctr": ["ctr", "clickthroughrate"],
        "position": ["position", "avgposition", "averageposition"],
    }

    for target, options in candidates.items():
        for option in options:
            if option in normalized:
                mapping[target] = normalized[option]
                break
    return mapping


def main() -> int:
    if not INPUT_CSV.exists():
        payload = {"available": False, "reason": "search_console_queries.csv not found", "rows_written": 0}
        OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        OUTPUT_MD.write_text(
            "# Search Console 변환 리포트\n\n- 상태: `없음`\n- 이유: `data/search_console_queries.csv` 파일이 아직 없습니다.\n"
        )
        return 0

    config = load_json(CONFIG_PATH)
    aliases = config["keyword_aliases"]

    with INPUT_CSV.open() as fp:
        reader = csv.DictReader(fp)
        fieldnames = reader.fieldnames or []
        mapping = detect_columns(fieldnames)
        rows = list(reader)

    required = ["query", "clicks", "impressions", "ctr", "position"]
    missing = [name for name in required if name not in mapping]
    if missing:
        payload = {"available": False, "reason": f"missing columns: {', '.join(missing)}", "rows_written": 0}
        OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        OUTPUT_MD.write_text(
            "# Search Console 변환 리포트\n\n"
            f"- 상태: `실패`\n- 이유: `필수 컬럼 누락: {', '.join(missing)}`\n"
        )
        return 0

    keyword_rollup = {}
    for row in rows:
        query = row.get(mapping["query"], "")
        hits = find_keywords(query, aliases)
        if not hits:
            continue
        keyword = hits[0]

        clicks = parse_float(row.get(mapping["clicks"], "0"))
        impressions = parse_float(row.get(mapping["impressions"], "0"))
        ctr = parse_percent(row.get(mapping["ctr"], "0"))
        position = parse_float(row.get(mapping["position"], "100"))

        item = keyword_rollup.setdefault(
            keyword,
            {"clicks": 0.0, "impressions": 0.0, "weighted_ctr_sum": 0.0, "weighted_position_sum": 0.0, "queries": []},
        )
        item["clicks"] += clicks
        item["impressions"] += impressions
        item["weighted_ctr_sum"] += ctr * max(impressions, 1)
        item["weighted_position_sum"] += position * max(impressions, 1)
        item["queries"].append(query)

    with OUTPUT_CSV.open("w", newline="") as fp:
        writer = csv.DictWriter(
            fp,
            fieldnames=["date", "keyword", "clicks", "impressions", "ctr_percent", "avg_position", "notes"],
        )
        writer.writeheader()
        for keyword, data in sorted(keyword_rollup.items()):
            impressions = max(data["impressions"], 1.0)
            ctr_percent = round(data["weighted_ctr_sum"] / impressions, 2)
            avg_position = round(data["weighted_position_sum"] / impressions, 2)
            writer.writerow(
                {
                    "date": "",
                    "keyword": keyword,
                    "clicks": round(data["clicks"], 2),
                    "impressions": round(data["impressions"], 2),
                    "ctr_percent": ctr_percent,
                    "avg_position": avg_position,
                    "notes": "Derived from search_console_queries.csv",
                }
            )

    report_items = []
    for keyword, data in sorted(keyword_rollup.items(), key=lambda kv: (-kv[1]["clicks"], kv[0])):
        report_items.append(
            {
                "keyword": keyword,
                "clicks": round(data["clicks"], 2),
                "impressions": round(data["impressions"], 2),
                "queries": data["queries"][:5],
            }
        )

    payload = {"available": True, "rows_written": len(keyword_rollup), "items": report_items}
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Search Console 변환 리포트")
    lines.append("")
    lines.append("- 상태: `성공`")
    lines.append(f"- rows_written: `{len(keyword_rollup)}`")
    lines.append("")
    for item in report_items:
        lines.append(f"- `{item['keyword']}`: clicks {item['clicks']}, impressions {item['impressions']}")
        for query in item["queries"]:
            lines.append(f"  - query: {query}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
