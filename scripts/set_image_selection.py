#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "outputs/latest/image-selections.json"
EXAMPLE_JSON = ROOT / "outputs/latest/image-selections.example.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create or update selected blog image metadata by keyword and slot.")
    parser.add_argument("--keyword", required=True, help="Target post keyword.")
    parser.add_argument("--slot", required=True, choices=["hero", "inline"], help="Image slot to update.")
    parser.add_argument("--selected-url", required=True, help="Approved image URL.")
    parser.add_argument("--selected-credit", default="", help="Caption or credit line.")
    parser.add_argument("--selected-photographer", default="", help="Photographer name if separated from credit.")
    parser.add_argument("--notes", default="", help="Optional notes about why this image was chosen.")
    parser.add_argument("--approve", action="store_true", help="Mark the image selection as approved.")
    return parser.parse_args()


def load_payload() -> dict:
    if not OUTPUT_JSON.exists():
        return {"items": []}
    return json.loads(OUTPUT_JSON.read_text())


def write_example_if_missing() -> None:
    if EXAMPLE_JSON.exists():
        return
    EXAMPLE_JSON.write_text(
        json.dumps(
            {
                "items": [
                    {
                        "keyword": "fomc",
                        "slot": "hero",
                        "selected_url": "https://images.unsplash.com/example",
                        "selected_credit": "Photo by Name on Unsplash",
                        "selected_photographer": "Name",
                        "approved": True,
                        "notes": "대표 이미지로 사용"
                    }
                ]
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def main() -> int:
    args = parse_args()
    payload = load_payload()
    items = payload.get("items", [])

    updated = False
    for item in items:
        if item.get("keyword") == args.keyword and item.get("slot") == args.slot:
            item["selected_url"] = args.selected_url
            item["selected_credit"] = args.selected_credit
            item["selected_photographer"] = args.selected_photographer
            item["approved"] = bool(args.approve)
            item["notes"] = args.notes
            updated = True
            break

    if not updated:
        items.append(
            {
                "keyword": args.keyword,
                "slot": args.slot,
                "selected_url": args.selected_url,
                "selected_credit": args.selected_credit,
                "selected_photographer": args.selected_photographer,
                "approved": bool(args.approve),
                "notes": args.notes,
            }
        )

    payload["items"] = items
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    write_example_if_missing()
    print(str(OUTPUT_JSON))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
