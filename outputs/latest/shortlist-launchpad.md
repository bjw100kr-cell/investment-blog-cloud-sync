# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-09-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Firelight raises $8 million, expands beyond XRP as it aims to make DeFi less scary for fintechs
  - Ethena pushes stablecoins into everyday banking with high-yield savings, cards and payments
  - US launches further strikes on Iran as conflict flares up
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-09-02T01:16:51+00:00 | Asian markets tumble as US-Iran fighting lifts oil and bond yields - Reuters
  - NYT Business | 2026-09-02T00:25:48+00:00 | Bond Sell-Off Threatens to Squeeze Borrowers Around the World
  - Reuters Markets via Google News RSS | 2026-09-01T22:26:55+00:00 | Wall Street ends lower as higher yields, rising oil prices mark shaky start to September - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Robinhood's new crypto network is printing cash, and it's sending Arbitrum's token soaring
  - Musk’s X hit by wave of unsolicited password reset emails
  - Firelight raises $8 million, expands beyond XRP as it aims to make DeFi less scary for fintechs
- recent_evidence:
  - CoinDesk RSS | 2026-09-01T13:55:26+00:00 | Bitcoin enters ‘Rektember’ as rate-hike risk combines with seasonality to threaten rally
  - Investing.com Crypto News | 2026-09-01 22:03:01 | Bitcoin slips a day after posting its best monthly performance since November 2024
  - Investing.com Crypto News | 2026-09-01 19:19:22 | Bitcoin bearish Marubozu near $77,248: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-09-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Dell surges 9% after lifting fiscal 2027 forecast on AI server strength
  - Apple enters John Ternus era as AI challenges and memory crunch intensify
  - Tim Cook handed $47mn pay deal as Apple’s executive chair
- recent_evidence:
  - MarketWatch Breaking News | 2026-09-02T00:19:00+00:00 | Dell’s AI servers drive a stellar earnings performance, and a raised outlook
  - Financial Times Home | 2026-09-01T23:38:26+00:00 | Tim Cook handed $47mn pay deal as Apple’s executive chair
  - CNBC Top News | 2026-09-01T21:40:18+00:00 | Dell surges 9% after lifting fiscal 2027 forecast on AI server strength
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
