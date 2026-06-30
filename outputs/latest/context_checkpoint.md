# Context Snapshot

생성 시각(UTC): `2026-06-30T21:09:11.316621+00:00`

- 목표: 주식/코인/세계경제 투자 블로그 자동화 운영 지속 및 수익화

## 핵심 상태
- published_count: `13`
- upload processed_count: `1`
- latest_synced_at: `2026-06-30T21:03:21.108351+00:00`
- all_core_checks_passed: `True`

## 이번 체크포인트 노트
- traffic amplification plan added

## 최근 병목 요약
- 최근 병목이 기록되지 않았습니다.

## 다음 액션
- Secret: `BLOGGER_BLOG_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`
- Variable: `OPENAI_MODEL`, `BLOGGER_SYNC_SITE_PAGES`, `BLOGGER_SITE_PAGES_PUBLISH`, `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES`, `BLOGGER_REQUIRE_REVIEW_APPROVAL`, `BLOGGER_AUTO_PUBLISH_POSTS`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS`, `BLOGGER_MAX_POSTS_PER_RUN`
- `python3 scripts/prepare_github_launch_plan.py`(repo_connected=true 재확인)
- `outputs/latest/blogger-upload-report.json`
- `outputs/latest/first-cloud-run-verification.json`

## 즉시 재개 커맨드
- `python3 scripts/run_pipeline.sh`
- `python3 scripts/emit_context_checkpoint.py`
- `jq '.summary.processed_count,.summary.review_required,.items[0:4]' outputs/latest/blogger-upload-report.json`
