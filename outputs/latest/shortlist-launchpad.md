# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Keyrock acquires BlockFills trading assets to expand institutional crypto business
  - Crypto for Advisors: Strengthening defenses against AI fraud
  - Crypto brokerage firm Alpaca raises $135 million for tokenized stock infrastructure
- recent_evidence:
  - Investing.com Crypto News | 2026-07-16 13:45:54 | Bitcoin slips to $64.2k as markets parse cooling rate jitters, Iran tensions
  - Investing.com Crypto News | 2026-07-16 07:04:55 | Bitcoin tests $65,500 resistance as volume fades: Live levels
  - Investing.com Crypto News | 2026-07-15 22:17:08 | Bitcoin turns marginally lower as soft U.S. Inflation data offset by Iran tensions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - S&P 500, Nasdaq fall as chip stocks weaken; earnings and data in focus - Reuters
  - Chipmakers chip away at stocks, oil hovers at $85 - Reuters
  - TSMC Q2 profit jumps 77% to record, far surpasses expectations - Reuters
- recent_evidence:
  - Financial Times YouTube | 32K views | Silicon shadows: inside the black market for AI chips | FT Film
  - NYT Business | 2026-07-16T15:59:46+00:00 | Anthropic Inches Toward a Mega-I.P.O.
  - Reuters Markets via Google News RSS | 2026-07-16T14:15:07+00:00 | S&P 500, Nasdaq fall as chip stocks weaken; earnings and data in focus - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword `oil` / publish `2026-07-16` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - US hits tanker heading for Kharg Island under renewed Iran blockade
  - Chipmakers chip away at stocks, oil hovers at $85 - Reuters
  - Can Kazakhstan’s oil boom survive Putin’s War? | FT Film
- recent_evidence:
  - Financial Times Home | 2026-07-16T15:57:54+00:00 | Zelenskyy’s government plunged into turmoil by defence minister’s firing
  - NYT Business | 2026-07-16T13:45:14+00:00 | Strait of Hormuz Tanker Traffic Erodes Further as Oil Prices Rise
  - Reuters Markets via Google News RSS | 2026-07-16T02:09:00+00:00 | Chipmakers chip away at stocks, oil hovers at $85 - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil --apply`
