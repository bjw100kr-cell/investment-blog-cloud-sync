#!/usr/bin/env python3
"""Backward-compatible entrypoint for older docs or manual commands.

Historically this script was referenced as build_github_launch_plan.py, while the
implementation now lives in prepare_github_launch_plan.py. Keeping this tiny
wrapper avoids command failures for operators following legacy instructions.
"""

import runpy
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    runpy.run_path(str(root / "prepare_github_launch_plan.py"), run_name="__main__")
