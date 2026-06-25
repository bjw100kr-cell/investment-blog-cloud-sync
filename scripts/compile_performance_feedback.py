#!/usr/bin/env python3
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "data/performance_signals.csv"
OUTPUT_JSON = ROOT / "outputs/latest/performance-feedback.json"
OUTPUT_MD = ROOT / "outputs/latest/performance-feedback.md"


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def main() -> int:
    if not INPUT_CSV.exists():
        payload = {
            "available": False,
            "reason": "performance_signals.csv not found",
            "keyword_feedback": {},
        }
        OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        OUTPUT_MD.write_text(
            "# 성과 피드백\n\n- 상태: `없음`\n- 이유: `data/performance_signals.csv` 파일이 아직 없습니다.\n"
        )
        return 0

    rows = []
    with INPUT_CSV.open() as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            rows.append(row)

    keyword_feedback = {}
    for row in rows:
        keyword = (row.get("keyword") or "").strip()
        if not keyword:
            continue
        clicks = float(row.get("clicks") or 0)
        impressions = float(row.get("impressions") or 0)
        ctr = float(row.get("ctr_percent") or 0)
        avg_position = float(row.get("avg_position") or 100)

        bonus = 0.0
        bonus += clamp(clicks / 10.0, 0, 5)
        bonus += clamp(impressions / 200.0, 0, 4)
        bonus += clamp(ctr / 2.0, 0, 4)
        bonus += clamp((20 - avg_position) / 4.0, 0, 3)
        bonus = round(clamp(bonus, 0, 12), 2)

        keyword_feedback[keyword] = {
            "bonus": bonus,
            "clicks": clicks,
            "impressions": impressions,
            "ctr_percent": ctr,
            "avg_position": avg_position,
            "notes": row.get("notes", "").strip(),
        }

    payload = {
        "available": True,
        "keyword_feedback": keyword_feedback,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 성과 피드백")
    lines.append("")
    lines.append("- 상태: `사용 가능`")
    lines.append("")
    for keyword, data in sorted(keyword_feedback.items(), key=lambda kv: (-kv[1]["bonus"], kv[0])):
        lines.append(
            f"- `{keyword}`: bonus {data['bonus']}, clicks {int(data['clicks'])}, impressions {int(data['impressions'])}, ctr {data['ctr_percent']}, avg_position {data['avg_position']}"
        )
        if data["notes"]:
            lines.append(f"  - note: {data['notes']}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
