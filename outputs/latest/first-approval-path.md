# First Confirmation Path

오늘 처음 사용자 최종 확인할 글을 고르는 가장 짧은 운영 경로입니다.

- blogger_ready: `True`
- platform_primary_channel: `blogger`
- 원칙: 아래 글을 먼저 읽고 확인한 뒤에만 업로드 명령으로 넘어갑니다.

## 추천 1순위 묶음

- label: `가장 먼저 볼 메인 글`
- reason: 발행일이 오늘 또는 내일인 메인 글이며, 품질/이미지 준비가 된 글을 위로 올렸습니다.
- item_count: `2`
- ready_now_count: `2`
- user_confirmation_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc bitcoin`
- `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지 / lane `macro` / publish 2026-07-05 / priority 135.0 / freshness `` / quality `pass` / hero_image_selected `True`
- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / lane `crypto` / publish 2026-07-06 / priority 123.0 / freshness `fresh` / quality `pass` / hero_image_selected `True`

## 가장 먼저 단건 확인할 글

- keyword: `fomc`
- title: `FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지`
- brand_lane: `macro` (거시경제)
- publish_date: `2026-07-05`
- review_verdict: `approve`
- priority_score: `135.0`
- freshness_status: ``
- quality_status: `pass`
- hero_image_selected: `True`
- selection_summary: `fomc`이 오늘 직접 발행 가능한 후보 중 가장 안전한 1순위입니다. 현재 브랜드 레인은 `macro` (거시경제)이고 freshness는 `unknown`입니다. 품질 게이트가 통과 상태라 승인 후 업로드 경로가 가장 짧습니다. 대표 이미지도 이미 선택되어 있어 추가 준비가 거의 없습니다. 오늘 1순위 후보는 레인 우선순위 `macro > crypto > us-stocks > world-flow` 기준에서 freshness와 검수 상태를 함께 반영해 고릅니다.
- why_not_other_topics:
  - `seo_china_10`도 같은 `macro` 레인이지만 현재 점수와 발행 준비도 기준에서는 `fomc`가 앞섭니다.
- user_confirmation_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`

## 사용자 확인 후 바로 실행

- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## 운영 메모

- 첫 실전 검증은 `Blogger`만 봅니다.
- WordPress는 이 승인 경로가 안정화된 뒤 두 번째 자동 채널로 붙입니다.
