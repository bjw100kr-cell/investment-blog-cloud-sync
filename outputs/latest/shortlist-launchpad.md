# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Copper CEO Amar Kuchinad departs as search for a buyer enters a fourth month
  - Bitcoin rally has more room as volatility shorts unwind, Two Prime CEO says
  - Bitmine purchased another $69 million of ETH, with Tom DeMark expecting price uptrend to soon resume
- recent_evidence:
  - Cointelegraph | 2026-09-08T15:41:11+00:00 | Bitcoin faces key support test at $78.3K as US crude oil hits three-month high
  - CoinDesk RSS | 2026-09-08T13:18:21+00:00 | Bitcoin rally has more room as volatility shorts unwind, Two Prime CEO says
  - CoinDesk RSS | 2026-09-08T12:09:26+00:00 | Bitcoin’s complexity paradox: How layer-2 scalers became AI's main target
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic withheld latest AI model from UK testing agency
  - Memory chips have come to rule the AI boom. Why Micron’s reign could be here to stay.
  - Qualcomm’s stock climbs as Amazon chip deal offers investors much-needed good news
- recent_evidence:
  - Financial Times YouTube | 59K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Financial Times Home | 2026-09-09T04:00:25+00:00 | Anthropic withheld latest AI model from UK testing agency
  - MarketWatch Breaking News | 2026-09-08T21:51:00+00:00 | Memory chips have come to rule the AI boom. Why Micron’s reign could be here to stay.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword `tariffs_trade` / publish `2026-09-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Canada's retaliatory tariffs worth CA$27.6 billion take effect as trade rift with U.S. deepens
  - 'Patients pay the tariff': Swiss pharma CEO warns of Trump's generic drug tariff threat
  - Bombardier’s stock drops as the U.S.-Canada trade war intensifies. Here’s what Trump is targeting next.
- recent_evidence:
  - NYT Business | 2026-09-09T02:33:37+00:00 | Carney Says Retaliation Against U.S. Tariffs Was Unavoidable
  - MarketWatch Breaking News | 2026-09-09T00:17:00+00:00 | Bombardier’s stock drops as the U.S.-Canada trade war intensifies. Here’s what Trump is targeting next.
  - CNBC Top News | 2026-09-08T17:11:11+00:00 | Canada's retaliatory tariffs worth CA$27.6 billion take effect as trade rift with U.S. deepens
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade --apply`
