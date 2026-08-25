# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `2`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin nears $80,000, but analysts say the next pullback will be key
  - Crypto political group details list of U.S. congressional allies its backing this year
  - Coinbase debuts tokenized stocks on Base network, joining race to bring equities on blockchain
- recent_evidence:
  - MarketWatch Breaking News | 2026-08-24T20:53:00+00:00 | Bitcoin has beaten stocks and gold over six months. Now it’s closing in on $80,000.
  - CoinDesk RSS | 2026-08-24T19:36:36+00:00 | Bitcoin nears $80,000, but analysts say the next pullback will be key
  - Cointelegraph | 2026-08-24T17:48:44+00:00 | Bitcoin price hits $80K as 24-hour crypto short liquidations pass $220M
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-08-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: FOMC가 무엇인지와 금리·주식·코인에 왜 중요한지 알고 싶어 하는 초중급 투자자
- why_now: 복수 소스 교차 확인 가능 (7개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Tom Lee's Bitmine buys $81 million of ETH in largest weekly haul since early July
  - Strive buys 1,110 Bitcoin for $81.5M, holdings top 21K BTC; ASST shares surge 11%
  - Bessent could tap near $1 trillion Treasury General Account to fund bond buybacks, sources said
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-08-24T21:07:43+00:00 | Bond market anxiety raises stakes for Warsh's debut Jackson Hole speech - Reuters
  - NYT Business | 2026-08-24T20:03:52+00:00 | What’s Behind the U.S. Treasury’s Latest Attempt to Lower Interest Rates
  - Financial Times Home | 2026-08-24T17:16:47+00:00 | Treasury market interventions are only a band-aid
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
