# Context Snapshot

생성 시각(UTC): `2026-06-30T21:50:16.805843+00:00`

- 목표: 주식/코인/세계경제 투자 블로그 자동화 운영 지속 및 수익화

## 핵심 상태
- published_count: `13`
- upload processed_count: `1`
- latest_synced_at: `2026-06-30T21:44:35.163395+00:00`
- all_core_checks_passed: `True`

## 이번 체크포인트 노트
- click title sync added

## 최근 병목 요약
- 최근 병목이 기록되지 않았습니다.

## 다음 액션
- `scripts/sync_click_titles_from_html.py`가 추가되어 `publish-inventory.json`의 메인 글 manifest만 대상으로 HTML H1을 `title`/`meta_title`에 동기화.
- 로컬/클라우드 파이프라인 모두 `Build publish inventory` 직후 해당 단계를 실행.
- 최신 검증에서 메인 글 4개가 모두 개선됨: `manifest_changed_count=4`, `inventory_changed_count=4`.
- 현재 Blogger 1순위 후보 `bitcoin` 제목은 `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`.
- Secret: `BLOGGER_BLOG_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`
- Variable: `OPENAI_MODEL`, `BLOGGER_SYNC_SITE_PAGES`, `BLOGGER_SITE_PAGES_PUBLISH`, `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES`, `BLOGGER_REQUIRE_REVIEW_APPROVAL`, `BLOGGER_AUTO_PUBLISH_POSTS`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS`, `BLOGGER_MAX_POSTS_PER_RUN`

## 즉시 재개 커맨드
- `python3 scripts/run_pipeline.sh`
- `python3 scripts/emit_context_checkpoint.py`
- `jq '.summary.processed_count,.summary.review_required,.items[0:4]' outputs/latest/blogger-upload-report.json`
