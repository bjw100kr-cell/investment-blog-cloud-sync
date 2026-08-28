# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin hits highest level in 3 months before pulling back as altcoins consolidate
  - Visa doubles down on South Korea with Upbit operator Dunamu on stablecoin payments
  - Kraken users briefly locked out after a flood of sanctioned crypto transactions
- recent_evidence:
  - CoinDesk RSS | 2026-08-28T10:37:35+00:00 | Bitcoin hits highest level in 3 months before pulling back as altcoins consolidate
  - CoinDesk RSS | 2026-08-28T09:09:07+00:00 | Live updates: Markets turn cautious before Warsh speech as bitcoin loses overnight gains
  - CoinDesk RSS | 2026-08-28T06:30:10+00:00 | Here’s why Warsh’s Jackson Hole speech is a major event for bitcoin and gold
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (anthropic)
- sample_headlines:
  - anthropic
  - Nasdaq, S&P 500 lifted by Nvidia's forecast; investors eye speech by Fed's Warsh - Reuters
  - Is Anthropic worth $2 trillion? Here’s how the company is trading in a new tokenized market.
- recent_evidence:
  - Financial Times YouTube | 55K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-08-28T10:29:00+00:00 | Is Anthropic worth $2 trillion? Here’s how the company is trading in a new tokenized market.
  - Google Trends US | 2026-08-28T03:30:00-07:00 | anthropic
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-31` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Trump ratchets up rhetoric against Beijing as U.S.-China officials meet for Xi's Washington visit
  - The devastating forces behind the deadly Himalayan flood
  - Is China’s ‘wise camel’ the winner from the US-Iran war?
- recent_evidence:
  - Financial Times Home | 2026-08-28T09:10:55+00:00 | China suspends Himalaya flood rescue efforts as lake overflows
  - Financial Times Home | 2026-08-28T04:00:16+00:00 | Is China’s ‘wise camel’ the winner from the US-Iran war?
  - Financial Times Home | 2026-08-28T01:37:21+00:00 | China bets on exports of cheap 3D-printed drone killers
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
