# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-05` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto poured years into new products. The next challenge is keeping users
  - The Clarity Act stalled. Bankers aren’t hitting the brakes yet on crypto dealmaking
  - Crypto job postings triple to over 1,200 in September, but applications fall
- recent_evidence:
  - Cointelegraph | 2026-10-04T09:40:00+00:00 | El Salvador receives $138 million from IMF after Bitcoin waivers granted
  - Investing.com Crypto News | 2026-10-04 07:02:26 | Bitcoin MFI hits 100 inside Ichimoku cloud: Live levels
  - Investing.com Crypto News | 2026-10-04 05:38:13 | Bitcoin holds near $85,000 as SEC clears first 3x leveraged crypto ETPs
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-10-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Payments firm OpenPayd targets year-end Nasdaq listing to fund U.S. expansion and acquisitions
- recent_evidence:
  - CoinDesk RSS | 2026-10-03T16:00:00+00:00 | Payments firm OpenPayd targets year-end Nasdaq listing to fund U.S. expansion and acquisitions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-07` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
  - 2. Trump actually lost? Who says so? (US-China Summit)
  - 1. The main topic of the US-China summit was SI (US-China summit)
- recent_evidence:
  - 무역킹 Trade King YouTube | 43K | 2. Trump actually lost? Who says so? (US-China Summit)
  - 무역킹 Trade King YouTube | 18K | 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
  - 무역킹 Trade King YouTube | 17K | 1. The main topic of the US-China summit was SI (US-China summit)
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
