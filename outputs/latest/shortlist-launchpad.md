# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-31` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - A $1.1 million crypto card hack crashed a neobank's token 49%
  - Ditching 'digital gold': BPI study suggests everyday Americans prefer control and micro-investing
  - Inside the high-stakes battle between digital dollars and Swift's massive money engine
- recent_evidence:
  - Cointelegraph | 2026-08-29T06:47:12+00:00 | Bitcoin ETFs end 9-day inflow streak as BTC dips below $78K
  - CoinDesk RSS | 2026-08-29T04:30:00+00:00 | Bitcoin wallets untouched for 10 years moved $40 million worth of coins
  - Investing.com Crypto News | 2026-08-29 21:13:26 | Bitcoin price holds at $78,000 as ‘digital gold’ narrative faces fresh test
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-09-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Tech backlash reaches fever pitch as AI angst collides with social media fears
  - Meta’s $18 billion settlement puts TikTok and YouTube on notice. Who's next on the firing line?
  - Tim Cook wasn’t a ‘product guy’ — so he re-engineered Apple instead
- recent_evidence:
  - NYT Business | 2026-08-29T17:02:38+00:00 | Thievery or Innovation? The Music Industry Grapples With A.I.
  - MarketWatch Breaking News | 2026-08-29T12:30:00+00:00 | Tim Cook wasn’t a ‘product guy’ — so he re-engineered Apple instead
  - CNBC Top News | 2026-08-29T05:00:01+00:00 | Meta’s $18 billion settlement puts TikTok and YouTube on notice. Who's next on the firing line?
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-08-30` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - altFINS Partners with BitPath Holdings to Launch Gen 2 Digital Asset Treasury Strategy Powered by AI Analytics
  - Rising bond yields add tens of billions to G7 countries’ debt costs
  - Stocks fall while dollar, bond yields rise as Warsh prompts rate hike bets - Reuters
- recent_evidence:
  - Financial Times Home | 2026-08-30T04:12:14+00:00 | What’s the fiscal hit from higher yields?
  - Financial Times Home | 2026-08-30T04:00:19+00:00 | Rising bond yields add tens of billions to G7 countries’ debt costs
  - NYT Business | 2026-08-29T23:20:50+00:00 | Treasury Bars Some Reporters From G20 Finance Meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
