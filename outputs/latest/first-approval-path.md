# First Confirmation Path

오늘 처음 사용자 최종 확인할 글을 고르는 가장 짧은 운영 경로입니다.

- blogger_ready: `True`
- platform_primary_channel: `blogger`
- 원칙: 아래 글을 먼저 읽고 확인한 뒤에만 업로드 명령으로 넘어갑니다.

## 추천 1순위 묶음

- label: `가장 먼저 볼 메인 글`
- reason: 발행일이 오늘 또는 내일인 메인 글이며, 품질/이미지 준비가 된 글을 위로 올렸습니다.
- item_count: `1`
- ready_now_count: `1`
- user_confirmation_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / lane `crypto` / publish 2026-07-19 / priority 123.0 / freshness `fresh` / quality `pass` / hero_image_selected `True`

## 가장 먼저 단건 확인할 글

- keyword: `bitcoin`
- title: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- brand_lane: `crypto` (코인)
- publish_date: `2026-07-19`
- review_verdict: `approve`
- priority_score: `123.0`
- freshness_status: `fresh`
- quality_status: `pass`
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- hero_image_selected: `True`
- selection_summary: `bitcoin`이 오늘 직접 발행 가능한 후보 중 가장 안전한 1순위입니다. 현재 브랜드 레인은 `crypto` (코인)이고 freshness는 `fresh`입니다. 품질 게이트가 통과 상태라 승인 후 업로드 경로가 가장 짧습니다. 대표 이미지도 이미 선택되어 있어 추가 준비가 거의 없습니다. 오늘 1순위 후보는 레인 우선순위 `macro > crypto > us-stocks > world-flow` 기준에서 freshness와 검수 상태를 함께 반영해 고릅니다.
- why_not_other_topics:
  - `fomc`는 priority `126.0`로 높지만 freshness가 `stale`라서 오늘 메인 직접 발행 후보에서 보류됐습니다.
- user_confirmation_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`

## 사용자 확인 후 바로 실행

- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## 운영 메모

- 첫 실전 검증은 `Blogger`만 봅니다.
- WordPress는 이 승인 경로가 안정화된 뒤 두 번째 자동 채널로 붙입니다.
