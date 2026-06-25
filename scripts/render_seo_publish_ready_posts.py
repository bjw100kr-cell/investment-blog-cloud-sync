#!/usr/bin/env python3
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    command = [
        "python3",
        str(ROOT / "scripts/render_publish_ready_posts.py"),
        "--packets-json",
        str(ROOT / "outputs/latest/seo-draft-packets.json"),
        "--publishing-json",
        str(ROOT / "outputs/latest/seo-publishing-assets.json"),
        "--drafts-dir",
        str(ROOT / "outputs/latest/seo-drafts"),
        "--output-dir",
        str(ROOT / "outputs/latest/seo-publish-ready"),
        "--output-json",
        str(ROOT / "outputs/latest/seo-publish-ready-report.json"),
        "--output-md",
        str(ROOT / "outputs/latest/seo-publish-ready-report.md"),
    ]
    completed = subprocess.run(command, cwd=ROOT)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
