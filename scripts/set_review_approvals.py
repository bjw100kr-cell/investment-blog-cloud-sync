#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create or update the user final confirmation file for blog uploads.")
    parser.add_argument("--all", action="store_true", help="Approve all review packet items.")
    parser.add_argument("--keywords", nargs="*", default=[], help="Approve specific keywords from the review packet.")
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear prior approvals and reset to 안전한 대기 상태.",
    )
    parser.add_argument("--notes", default="", help="Optional note to save in the approval file.")
    return parser.parse_args()


def load_packet_keywords() -> list[str]:
    if not REVIEW_PACKET_JSON.exists():
        return []
    payload = json.loads(REVIEW_PACKET_JSON.read_text())
    return [item.get("keyword", "") for item in payload.get("items", []) if item.get("keyword")]


def main() -> int:
    args = parse_args()
    if args.clear:
        approved_all = False
    else:
        approved_all = bool(args.all)

    packet_keywords = load_packet_keywords()
    if args.clear:
        approved_keywords = []
    else:
        approved_keywords = packet_keywords if args.all else [keyword for keyword in args.keywords if keyword]

    payload = {
        "user_final_confirmation_required": True,
        "user_confirmed_all": approved_all,
        "user_confirmed_keywords": approved_keywords,
        "approved_all": approved_all,
        "approved_keywords": approved_keywords,
        "notes": args.notes,
    }
    APPROVALS_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(str(APPROVALS_JSON))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
