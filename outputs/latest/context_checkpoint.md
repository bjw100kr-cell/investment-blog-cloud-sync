# Context Snapshot

생성 시각(UTC): `2026-06-30T22:19:28.375960+00:00`

- 목표: 주식/코인/세계경제 투자 블로그 자동화 운영 지속 및 수익화

## 핵심 상태
- published_count: `14`
- upload processed_count: `1`
- latest_synced_at: `2026-06-30T22:16:29.385587+00:00`
- all_core_checks_passed: `True`

## 이번 체크포인트 노트
- blogger duplicate cleanup workflow added

## 최근 병목 요약
- 최근 병목이 기록되지 않았습니다.

## 다음 액션
- `scripts/sync_click_titles_from_html.py`가 추가되어 `publish-inventory.json`의 메인 글 manifest만 대상으로 HTML H1을 `title`/`meta_title`에 동기화.
- 로컬/클라우드 파이프라인 모두 `Build publish inventory` 직후 해당 단계를 실행.
- 최신 검증에서 메인 글 4개가 모두 개선됨: `manifest_changed_count=4`, `inventory_changed_count=4`.
- 현재 Blogger 1순위 후보 `bitcoin` 제목은 `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`.
- 신규 개선: `score_daily_topics.py` 기본 제목도 클릭형으로 교체했고, `generate_blog_drafts.py`의 미국 증시 제목 부제 중복 버그를 제거.
- `daily-traffic-goal.json`은 이제 실제 발행 인벤토리 제목과 코인 시장 신호(`extreme_fear`, BTC 변동, Fear/Greed)를 같이 보여줌.

## 즉시 재개 커맨드
- `python3 scripts/run_pipeline.sh`
- `python3 scripts/emit_context_checkpoint.py`
- `jq '.summary.processed_count,.summary.review_required,.items[0:4]' outputs/latest/blogger-upload-report.json`
