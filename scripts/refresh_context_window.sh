#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

NOTE="${1:-manual-window-refresh}"

printf 'Context refresh start: %s\n' "$NOTE"
python3 scripts/emit_context_checkpoint.py --note "$NOTE"
python3 scripts/persist_session_context.py -n "$NOTE"

echo "Context refresh done."
echo "- CONVERSATION_SUMMARY: $(pwd)/CONVERSATION_SUMMARY.md"
echo "- CHECKPOINT_MD: $(pwd)/outputs/latest/context_checkpoint.md"
echo "- CHECKPOINT_JSON: $(pwd)/outputs/latest/context_checkpoint.json"
echo "- MEMO_LOG: $(pwd)/outputs/latest/session_memos/session_memories.md"
