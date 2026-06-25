#!/usr/bin/env python3
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    command = [
        "python3",
        str(ROOT / "scripts/generate_publishing_assets.py"),
        "--packets-json",
        str(ROOT / "outputs/latest/seo-draft-packets.json"),
        "--output-json",
        str(ROOT / "outputs/latest/seo-publishing-assets.json"),
        "--output-md",
        str(ROOT / "outputs/latest/seo-publishing-assets.md"),
    ]
    completed = subprocess.run(command, cwd=ROOT)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
