# Approval Dashboard

사용자가 긴 리뷰 패킷을 다 읽지 않아도, 먼저 최종 확인할 묶음을 고르기 쉽게 만든 운영 대시보드입니다.

- 전체 검토 대상: `7`
- 메인 글 수: `4`
- 곧 발행할 메인 글 수: `2`
- 미국 빅테크 라인 글 수: `0`
- 지금 바로 발행 가까운 글 수: `6`
- 원칙: 사용자 최종 확인 전에는 실제 업로드를 실행하지 않습니다.

## 가장 먼저 볼 메인 글

- reason: 발행일이 오늘 또는 내일인 메인 글이며, 품질/이미지 준비가 된 글을 위로 올렸습니다.
- ready_now_count: `2`
- user confirmation command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc bitcoin`
- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / lane_focus_crypto / publish 2026-07-15 / priority 125.0 / freshness `fresh` / quality `pass` / hero_image_selected `True` / ready_now `True`
- `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지 / main_post / lane_focus_macro / publish 2026-07-14 / priority 137.0 / freshness `aging` / quality `pass` / hero_image_selected `True` / ready_now `True`

## 미국 빅테크 수익 라인

- reason: 메인 글 1개와 후속 SEO 글 3개를 묶어 미국 주식 검색 유입을 노립니다.
- ready_now_count: `0`
- user confirmation command: ``

## 거시 해설 라인

- reason: FOMC 메인 글과 후속 설명형 글 묶음입니다.
- ready_now_count: `1`
- user confirmation command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지 / main_post / lane_focus_macro / publish 2026-07-14 / priority 137.0 / freshness `aging` / quality `pass` / hero_image_selected `True` / ready_now `True`

## 코인 해설 라인

- reason: 비트코인 메인 글과 후속 검색형 글 묶음입니다.
- ready_now_count: `1`
- user confirmation command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / lane_focus_crypto / publish 2026-07-15 / priority 125.0 / freshness `fresh` / quality `pass` / hero_image_selected `True` / ready_now `True`
