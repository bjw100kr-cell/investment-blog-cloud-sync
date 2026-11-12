# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-13` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor
  - Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe
  - Crypto Long & Short: The GENIUS Act’s guarantees don’t cover DeFi lending
- recent_evidence:
  - CoinDesk RSS | 2026-11-12T05:22:31+00:00 | Bitcoin Core reveals bug that made thousands of nodes trust any stranger on Tor
  - Investing.com Crypto News | 2026-11-12 06:41:22 | Bitcoin slips to $73.6k; Strategy drops on MSCI index removal
  - CoinDesk RSS | 2026-11-11T12:21:24+00:00 | Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-14` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (8개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia perps crash 7% as CEO Jensen Huang reportedly faces the axe
  - Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound
  - Nvidia preparing to oust CEO Jensen Huang after affairs: WSJ
- recent_evidence:
  - CNBC Top News | 2026-11-12T06:11:16+00:00 | Nvidia board meeting to decide CEO Jensen Huang’s fate stretches into evening
  - Reuters Markets via Google News RSS | 2026-11-12T05:37:00+00:00 | Morning Bid: Jensen hangs on as Nvidia tumbles - Reuters
  - Financial Times World | 2026-11-12T05:31:16+00:00 | FirstFT: Nvidia board weighs Huang’s future as scandal deepens
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword `tariffs_trade` / publish `2026-11-15` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - EU and UK set to delay 10% tariff on electric cars
- recent_evidence:
  - Financial Times Home | 2026-11-12T05:00:21+00:00 | EU and UK set to delay 10% tariff on electric cars
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade --apply`
