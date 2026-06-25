#!/usr/bin/env python3
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    command = [
        "python3",
        str(ROOT / "scripts/generate_blog_drafts.py"),
        "--packets-json",
        str(ROOT / "outputs/latest/seo-draft-packets.json"),
        "--prompts-dir",
        str(ROOT / "outputs/latest/seo-prompts"),
        "--drafts-dir",
        str(ROOT / "outputs/latest/seo-drafts"),
        "--report-json",
        str(ROOT / "outputs/latest/seo-draft-generation-report.json"),
    ]
    completed = subprocess.run(command, cwd=ROOT)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
