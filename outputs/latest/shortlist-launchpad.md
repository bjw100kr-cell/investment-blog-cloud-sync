# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - AI agents make 138 million crypto payments as U.S. dominates spending on AI models
  - Crypto Long & Short: Why gold and bitcoin belong in the same portfolio
  - BlackRock's crypto ETF assets surge 63% but remain far below 2025 peak
- recent_evidence:
  - CoinDesk RSS | 2026-10-14T15:05:15+00:00 | Crypto Long & Short: Why gold and bitcoin belong in the same portfolio
  - Cointelegraph | 2026-10-14T14:21:15+00:00 | Bitcoin price dips below $82K as high oil prices spike US CPI inflation
  - Investing.com Crypto News | 2026-10-14 14:01:39 | Bitcoin dips below $83k after hot U.S. inflation data
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - AI agents make 138 million crypto payments as U.S. dominates spending on AI models
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. CPI 발표 후 금리와 나스닥, 비트코인이 같이 움직이는 이유

- keyword `cpi` / publish `2026-10-14` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (7개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Bitcoin price dips below $82K as high oil prices spike US CPI inflation
  - Here's the inflation breakdown for September 2026 — in one chart
  - Bitcoin dips below $83k after hot U.S. inflation data
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-14T15:58:13+00:00 | Wall St slides as hot CPI data fuels rate-hike bets; chips, banks weigh - Reuters
  - NYT Business | 2026-10-14T15:25:31+00:00 | Democrats Blame Trump After CPI Report Shows Energy Prices Drove Up Inflation
  - Cointelegraph | 2026-10-14T14:21:15+00:00 | Bitcoin price dips below $82K as high oil prices spike US CPI inflation
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords cpi`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords cpi`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword cpi`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword cpi --apply`
