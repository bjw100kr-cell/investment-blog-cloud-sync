# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-07` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_on)
- sample_headlines:
  - Why crypto experts say buying and holding bitcoin easily beats trying to time the market
  - British investor thought he lost $2,000 in bitcoin in 2012. He just recovered $4.5 million
  - Southeast Asia’s crypto funding rebounds to $680 million as investors focus on mature firms
- recent_evidence:
  - CoinDesk RSS | 2026-09-05T18:05:11+00:00 | Why crypto experts say buying and holding bitcoin easily beats trying to time the market
  - CoinDesk RSS | 2026-09-05T12:00:00+00:00 | British investor thought he lost $2,000 in bitcoin in 2012. He just recovered $4.5 million
  - Cointelegraph | 2026-09-05T08:03:06+00:00 | Bitcoin ETF inflows hit $3.8B in strongest three-week stretch of 2026
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Silicon shadows: inside the black market for AI chips | FT Film
  - Authors Wrangle With Publishers Over $1.5 Billion Anthropic A.I. Settlement
- recent_evidence:
  - Financial Times YouTube | 58K views | Silicon shadows: inside the black market for AI chips | FT Film
  - NYT Business | 2026-09-05T09:03:10+00:00 | Authors Wrangle With Publishers Over $1.5 Billion Anthropic A.I. Settlement
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword `oil` / publish `2026-09-06` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Trump’s state capitalism comes to the oil industry with his unprecedented Venezuela deal
  - U.S. attacks 3 Iranian oil tankers after missiles target Navy warships
  - US strikes three Iranian oil tankers in response to attacks on warships
- recent_evidence:
  - Financial Times World | 2026-09-05T20:05:42+00:00 | US strikes three Iranian oil tankers in response to attacks on warships
  - CNBC Top News | 2026-09-05T15:43:08+00:00 | U.S. attacks 3 Iranian oil tankers after missiles target Navy warships
  - CNBC Top News | 2026-09-05T15:11:03+00:00 | Trump’s state capitalism comes to the oil industry with his unprecedented Venezuela deal
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil --apply`
