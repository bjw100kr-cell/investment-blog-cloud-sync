# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-09-29` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Aave leads DeFi higher as crypto shrugs off surging bond market
  - Bitcoin gives back gains as long-term holder supply keeps $85K out of reach
  - Trump Accounts will auto-enroll children, potentially adding 60 million accounts: Treasury
- recent_evidence:
  - CNBC Top News | 2026-09-29T17:55:39+00:00 | Trump Accounts will auto-enroll children, potentially adding 60 million accounts: Treasury
  - Financial Times Home | 2026-09-29T17:25:41+00:00 | US 30-year Treasury yield hits highest since 2002
  - MarketWatch Breaking News | 2026-09-29T16:44:00+00:00 | The hidden messages the bond market is sending about the AI boom and the stock market
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic warns of ‘existential risks to humanity’ in IPO prospectus
  - Nvidia turns to insurers to spread the risk of AI build-out
  - What’s In Anthropic’s I.P.O. Filing
- recent_evidence:
  - NYT Business | 2026-09-29T11:58:36+00:00 | What’s In Anthropic’s I.P.O. Filing
  - Financial Times Home | 2026-09-29T04:04:31+00:00 | Nvidia turns to insurers to spread the risk of AI build-out
  - Financial Times Home | 2026-09-29T02:28:18+00:00 | Anthropic warns of ‘existential risks to humanity’ in IPO prospectus
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-30` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성
- sample_headlines:
  - Bitcoin beats gold, surge to $100,000 in play
  - Aave leads DeFi higher as crypto shrugs off surging bond market
  - Live updates: Bitcoin turns lower as rates rise, consumer confidence plunges
- recent_evidence:
  - Cointelegraph | 2026-09-29T16:26:11+00:00 | Bitcoin gives back gains as long-term holder supply keeps $85K out of reach
  - Cointelegraph | 2026-09-29T13:30:00+00:00 | Peter Brandt says Bitcoin may hit $600K by 2029, calls XRP a ‘fool coin’
  - Cointelegraph | 2026-09-29T12:40:12+00:00 | Bitcoin ETF inflows leave institutional demand unclear: CoinShares
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`
