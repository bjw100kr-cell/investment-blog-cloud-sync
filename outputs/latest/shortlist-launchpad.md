# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Fear is fading across markets, be it bitcoin, stocks, gold or bonds
  - Bitcoin slips as U.S. inflation fails to spark gains, ETFs see August's first two-day drawdown
  - Live updates: Bitcoin slips below $63,000 as oil, yields climb
- recent_evidence:
  - CoinDesk RSS | 2026-08-14T11:33:50+00:00 | Fear is fading across markets, be it bitcoin, stocks, gold or bonds
  - CoinDesk RSS | 2026-08-14T11:06:12+00:00 | Bitcoin slips as U.S. inflation fails to spark gains, ETFs see August's first two-day drawdown
  - Cointelegraph | 2026-08-14T10:43:57+00:00 | Bitcoin eyes new August lows as Binance longs face ‘cleanout’
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic's investor talks, Workday's stock surge, Apple's new facility and more in Morning Squawk
  - OpenAI and Anthropic in price war as Chinese AI rivals gain ground
  - Applied Materials shares are down on guidance and margin concerns. Analysts call it time to buy.
- recent_evidence:
  - Financial Times YouTube | 53K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-08-14T12:17:42+00:00 | Anthropic's investor talks, Workday's stock surge, Apple's new facility and more in Morning Squawk
  - Financial Times Home | 2026-08-14T04:00:14+00:00 | OpenAI and Anthropic in price war as Chinese AI rivals gain ground
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Uber partners with China's Pony.ai for 2,000 robotaxis in Europe
  - EXCLUSIVE: Apple trains its own AI model for China market with Alibaba's support, sources say - reuters.com
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-08-14T04:21:00+00:00 | EXCLUSIVE: Apple trains its own AI model for China market with Alibaba's support, sources say - reuters.com
  - CNBC Top News | 2026-08-14T01:02:39+00:00 | Uber partners with China's Pony.ai for 2,000 robotaxis in Europe
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
