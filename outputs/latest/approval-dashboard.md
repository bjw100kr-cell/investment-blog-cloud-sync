# Approval Dashboard

사용자가 긴 리뷰 패킷을 다 읽지 않아도, 먼저 최종 확인할 묶음을 고르기 쉽게 만든 운영 대시보드입니다.

- 전체 검토 대상: `13`
- 메인 글 수: `4`
- 곧 발행할 메인 글 수: `2`
- 미국 빅테크 라인 글 수: `0`
- 지금 바로 발행 가까운 글 수: `13`
- 원칙: 사용자 최종 확인 전에는 실제 업로드를 실행하지 않습니다.

## 가장 먼저 볼 메인 글

- reason: 발행일이 오늘 또는 내일인 메인 글이며, 품질/이미지 준비가 된 글을 위로 올렸습니다.
- ready_now_count: `2`
- user confirmation command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc bitcoin`
- `bitcoin` / 비트코인 핵심 흐름 해설 / main_post / lane_focus_crypto / publish 2026-07-02 / priority 121.0 / freshness `fresh` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `fomc` / FOMC 이후 시장 해설 / main_post / lane_focus_macro / publish 2026-07-01 / priority 140.0 / freshness `stale` / quality `pass` / hero_image_selected `True` / ready_now `True`

## 미국 빅테크 수익 라인

- reason: 메인 글 1개와 후속 SEO 글 3개를 묶어 미국 주식 검색 유입을 노립니다.
- ready_now_count: `0`
- user confirmation command: ``

## 거시 해설 라인

- reason: FOMC 메인 글과 후속 설명형 글 묶음입니다.
- ready_now_count: `4`
- user confirmation command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc seo_fomc_1 seo_fomc_2 seo_fomc_3`
- `seo_fomc_1` / FOMC 이후 시장이 주식과 코인에 미치는 영향 / seo_followup / evergreen_seo / publish 2026-07-01 / priority 139.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `seo_fomc_2` / FOMC 이후 시장에서 다음으로 봐야 할 체크포인트 5가지 / seo_followup / follow_up / publish 2026-07-01 / priority 136.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `seo_fomc_3` / FOMC 이후 시장 초보자 가이드: 용어부터 시장 반응까지 / seo_followup / evergreen_seo / publish 2026-07-01 / priority 133.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `fomc` / FOMC 이후 시장 해설 / main_post / lane_focus_macro / publish 2026-07-01 / priority 140.0 / freshness `stale` / quality `pass` / hero_image_selected `True` / ready_now `True`

## 코인 해설 라인

- reason: 비트코인 메인 글과 후속 검색형 글 묶음입니다.
- ready_now_count: `4`
- user confirmation command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin seo_bitcoin_4 seo_bitcoin_5 seo_bitcoin_6`
- `bitcoin` / 비트코인 핵심 흐름 해설 / main_post / lane_focus_crypto / publish 2026-07-02 / priority 121.0 / freshness `fresh` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `seo_bitcoin_4` / 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조 / seo_followup / evergreen_seo / publish 2026-07-02 / priority 120.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `seo_bitcoin_5` / 비트코인 핵심 흐름 ETF·규제 이슈 정리 / seo_followup / follow_up / publish 2026-07-02 / priority 117.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `seo_bitcoin_6` / 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리 / seo_followup / evergreen_seo / publish 2026-07-02 / priority 114.5 / freshness `unknown` / quality `pass` / hero_image_selected `True` / ready_now `True`
