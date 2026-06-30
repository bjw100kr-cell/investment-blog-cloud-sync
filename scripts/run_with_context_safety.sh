#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ "$#" -lt 2 ]]; then
  echo "Usage: $0 <note> -- <command> [args...]"
  echo "Example: $0 \"github-bootstrap\" -- bash scripts/bootstrap_github_remote.sh jhyang1117/investment-blog-cloud-sync"
  exit 1
fi

NOTE="$1"
shift

if [[ "$1" == "--" ]]; then
  shift
fi

if [[ "$#" -eq 0 ]]; then
  echo "No command provided."
  exit 1
fi

echo "Context snapshot before: $NOTE (start)"
bash scripts/refresh_context_window.sh "${NOTE}-start"

"$@"

echo "Context snapshot after: $NOTE (complete)"
bash scripts/refresh_context_window.sh "${NOTE}-complete"
