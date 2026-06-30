#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "=== STEP 1: GitHub repo next URL check ==="
python3 scripts/open_login_setup_pages.py --print-next
echo

echo "=== STEP 2: Local launch plan refresh ==="
python3 scripts/prepare_github_launch_plan.py
echo

echo "=== STEP 3: Web launch checklist refresh ==="
python3 scripts/prepare_github_web_launch_checklist.py
echo

echo "=== STEP 4: Export sync command ==="
python3 scripts/export_github_actions_sync_commands.py
echo

echo "=== STEP 5: Print Actions minimum inputs ==="
python3 scripts/print_github_actions_minimum_inputs.py
echo
