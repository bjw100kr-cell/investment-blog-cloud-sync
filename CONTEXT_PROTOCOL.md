# Context Protocol

Purpose: prevent long sessions from losing usable project state when the model context window gets full.

## Operating Rule

Do not rely on the chat history as the source of truth. Keep the project state compressed in files and continue from those files.

## Files To Keep Current

- `CONVERSATION_SUMMARY.md`: compact user preference, project status, and current bottleneck summary.
- `HANDOFF.md`: exact next action for the next high-performance model session.
- `TASK_QUEUE.md`: work that can be delegated to Spark or lower-cost model sessions.
- `outputs/latest/*`: generated reports, publish states, review boards, upload reports, and proof files.

## Save Rhythm

Update `CONVERSATION_SUMMARY.md` and `HANDOFF.md` whenever one of these happens:

- A login, token, blog connection, or upload state changes.
- A post is published, skipped, blocked, or moved in priority.
- A new root cause is found.
- The user changes publishing policy, platform priority, cost policy, or review policy.
- The session has been doing substantial work for a while and the next step would be hard to reconstruct from memory.

Also treat checkpoint generation as mandatory after any successful run and also during long running runs:

- After major runs, run `python3 scripts/emit_context_checkpoint.py`.
- 권장 패턴(요약): `bash scripts/refresh_context_window.sh "<phase>"`를 실행해 checkpoint + 세션 메모를 같이 남기면 됩니다.
- `scripts/run_pipeline.sh` now emits compressed checkpoints at every stage start/completion and on failure.
- Failure checkpoints include step/line/command context for faster resume.
- Keep only these additional checkpoint artifacts: `outputs/latest/context_checkpoint.md`, `outputs/latest/context_checkpoint.json`.
- 긴 구간 작업 전환 전에 아래로 즉시 압축 저장하세요.
  - `bash scripts/refresh_context_window.sh "<short-note>"`
  - 로그인/워크플로우 실행/브라우저 전환처럼 오버플로우 위험 구간은 다음 래퍼로 압축+실행을 묶어 쓰세요.
    - `bash scripts/run_with_context_safety.sh "<short-note>" -- <command>`

- Chat window overflow 예방 루틴(권장):
- 새 정책 결정/리스크 변경/사용자 지시 변경마다 즉시 1회
- 실행 전후 큰 단계(예: 업로드, 승인, 배포)마다 1회
- 메시지가 길어지거나 분기 판단이 많아질 때 1회
- 한 번에 3개 이상 판단을 내렸으면 즉시 `bash scripts/refresh_context_window.sh "decision-burst"` 실행.


- 즉시 복원용 순서는 고정입니다.
  - `outputs/latest/context_checkpoint.md`
- `outputs/latest/session_memos/session_memories.md`
- `HANDOFF.md`
- `CONVERSATION_SUMMARY.md`
- 장기 작업은 이 4개만 열면 되고, 원본 긴 대화 로그는 참조하지 않습니다.

For stricter chat-window safety, run `python3 scripts/persist_session_context.py -n "<phase>"` as often as needed during long sessions.

`scripts/run_pipeline.sh` automatically runs `persist_session_context.py` every 5 `run_step` calls by default.
You can tune cadence with `PIPELINE_CONTEXT_FLUSH_INTERVAL` environment variable.
Examples:
- Default (no env set): every 5 steps
- `PIPELINE_CONTEXT_FLUSH_INTERVAL=3`: every 3 steps
- `PIPELINE_CONTEXT_FLUSH_INTERVAL=8`: every 8 steps

추가로, 긴 세션에서는 수동으로도 다음 노트를 남겨 주세요:
- `python3 scripts/persist_session_context.py -n "handoff"`
- `python3 scripts/persist_session_context.py -n "before-model-switch"`
This compresses durable facts into `CONVERSATION_SUMMARY.md` and appends a chronological `outputs/latest/session_memos/session_memories.md/jsonl`.

권장 복원 체크리스트(오버플로우 방지용):
- `bash scripts/refresh_context_window.sh "handoff"`
- 새 창/새 세션 진입 직후 `outputs/latest/context_checkpoint.md`, `CONVERSATION_SUMMARY.md`, `HANDOFF.md` 순서로 읽기.
- 즉시 `python3 scripts/persist_session_context.py -n "resume-start"`로 마지막 상태를 다시 봉인.

Additional compression controls for long-running sessions:

- If messages are becoming long, run `python3 scripts/emit_context_checkpoint.py` immediately, then continue only with the compact artifacts below.
- Recommended recurrent command during heavy automation work:
  - `python3 scripts/emit_context_checkpoint.py --note "phase-name"`
- `run_pipeline.sh` notes:
  - `--note starting-<step>`
  - `--note completed-<step>`
  - `--note failed step=<step> line=<line> cmd=<command>`
  - `--note pipeline-finished`
- Before switching model sessions, read only: `outputs/latest/context_checkpoint.md` + `HANDOFF.md` + `CONVERSATION_SUMMARY.md`.
- Do not carry raw turn-by-turn chat into the next context. Convert any new findings into one of those documents first.

## Compression Rule

When saving, keep only durable facts:

- Current goal and active constraints.
- What is already built.
- What was verified.
- What is blocked and why.
- The next 1-5 concrete actions.
- Exact files/commands needed to resume.

For long sessions, open `outputs/latest/context_checkpoint.md` first.
For full session continuity, open `CONVERSATION_SUMMARY.md` after compression as the short memory handoff file.

Avoid saving long chat transcripts, repeated status messages, or outdated branches of thought.

## Cleanup Rule

Delete only clearly disposable local files:

- `.pycache`
- `.tmp_pycache`
- `.tmp_test`
- `.pytest_cache`

Do not delete:

- `.env`
- `.github`
- `outputs/latest/blogger-upload-state.json`
- `outputs/latest/blogger-upload-report.json`
- `outputs/latest/publish-inventory.json`
- `outputs/latest/publish-ready`
- `outputs/latest/seo-publish-ready`

## Current Resume Point

As of 2026-07-01 10:00 KST, the next engineering task is to keep the GitHub unblock path compact and deterministic (no extra browser tabs), then continue local/Cloud publish verification from the saved checkpoints. `run_pipeline.sh` checkpoints at each stage and on error, so context windows can be resumed from `outputs/latest/context_checkpoint.md`.
