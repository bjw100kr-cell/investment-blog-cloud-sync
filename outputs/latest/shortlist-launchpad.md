# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - U.S. Treasury sanctions another widespread cyber-scam hub, Xinbi Guarantee
  - Bitcoin and Ethereum race quantum clock as U.S. backs $300 million hardware push
  - Crypto Long & Short: Inside the 300-to-1 onchain gap between the dollar and euro
- recent_evidence:
  - Cointelegraph | 2026-09-09T16:28:19+00:00 | Bitcoin fails to reclaim $80K as Bessent fuels yen strength around 153 per dollar
  - CoinDesk RSS | 2026-09-09T15:30:00+00:00 | Bitcoin and Ethereum race quantum clock as U.S. backs $300 million hardware push
  - Investing.com Crypto News | 2026-09-09 20:47:59 | Bitcoin marginally lower to $78.3k as Brent tops $100 and U.S. bonds slide
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-09-12` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Bitcoin fails to reclaim $80K as Bessent fuels yen strength around 153 per dollar
  - Fearless US stock market vulnerable to shocks as midterms loom - Reuters
  - S&P 500 ends down as oil tops $100 per barrel - Reuters
- recent_evidence:
  - 무역킹 Trade King YouTube | 24K views | Stop looking for stock market secrets and do this instead
  - Reuters Markets via Google News RSS | 2026-09-09T23:06:18+00:00 | S&P 500 ends down as oil tops $100 per barrel - Reuters
  - Reuters Markets via Google News RSS | 2026-09-09T13:20:23+00:00 | Fearless US stock market vulnerable to shocks as midterms loom - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword `tariffs_trade` / publish `2026-09-13` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Trump promises $5,000 checks if Republicans win the midterms. He also teased tariff and ‘DOGE’ dividends last year that never came.
  - IMF ditched top candidate for chief economist job over Trump tariff remarks
  - Trump’s Midterm Pitch Clouded by Iran War and Canada Tariffs
- recent_evidence:
  - Financial Times World | 2026-09-10T04:00:28+00:00 | IMF ditched top candidate for chief economist job over Trump tariff remarks
  - MarketWatch Breaking News | 2026-09-10T03:00:00+00:00 | Trump promises $5,000 checks if Republicans win the midterms. He also teased tariff and ‘DOGE’ dividends last year that never came.
  - NYT Business | 2026-09-09T20:29:50+00:00 | Trump’s Midterm Pitch Clouded by Iran War and Canada Tariffs
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade --apply`
