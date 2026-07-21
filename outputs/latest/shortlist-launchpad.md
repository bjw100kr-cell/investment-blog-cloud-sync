# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-22` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Claude's Fable 5 just solved an 87-year-old math problem, and it matters for bitcoin
  - Galaxy sets up $5 million fund to help shield Bitcoin against quantum computing threats
  - Russia’s parliament passes crypto market law with $3,800 annual cap for retail investors
- recent_evidence:
  - CoinDesk RSS | 2026-07-21T16:19:24+00:00 | Claude's Fable 5 just solved an 87-year-old math problem, and it matters for bitcoin
  - CoinDesk RSS | 2026-07-21T16:16:14+00:00 | Galaxy sets up $5 million fund to help shield Bitcoin against quantum computing threats
  - Cointelegraph | 2026-07-21T15:14:37+00:00 | Bitcoin nears seven-week high as stocks ignore Iran strikes, Trump 10% tariff plans
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OpenAI, Anthropic boost lobbying as legacy tech and defense spending slips
  - Nvidia details its next-generation Vera CPU for AI, setting up challenge to AMD and Intel
  - Bessent says U.S. could sanction China over AI model 'theft'
- recent_evidence:
  - Financial Times YouTube | 41K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-07-21T16:30:11+00:00 | OpenAI, Anthropic boost lobbying as legacy tech and defense spending slips
  - Reuters Markets via Google News RSS | 2026-07-21T16:21:43+00:00 | Wall St gains on chip stocks recovery; earnings draw focus - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword `tariffs_trade` / publish `2026-07-24` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin nears seven-week high as stocks ignore Iran strikes, Trump 10% tariff plans
  - Trump prepares fresh tariff barrage with 10% levies set to expire
  - US to hit Canada with 50% tariffs on wide range of goods
- recent_evidence:
  - NYT Business | 2026-07-21T16:26:15+00:00 | Trump Escalates Canada Tariffs as Mark Carney Holds Firm
  - Cointelegraph | 2026-07-21T15:14:37+00:00 | Bitcoin nears seven-week high as stocks ignore Iran strikes, Trump 10% tariff plans
  - CNBC Top News | 2026-07-21T13:38:59+00:00 | Greer hints new Trump tariffs coming on dozens of countries: 'Expect action soon'
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade --apply`
