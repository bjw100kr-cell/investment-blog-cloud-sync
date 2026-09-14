# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Is Clarity dead? A vibes-based analysis: State of Crypto
  - Crypto's Clarity Act is a Schrödinger's cat in life-death limbo as U.S. Senate returns
  - Bitcoin Suisse plans to cut up to half its Swiss jobs as it shifts work abroad
- recent_evidence:
  - Investing.com Crypto News | 2026-09-13 21:59:53 | Bitcoin little changed at $77k as rate pressure clashes with diversification case
  - Investing.com Crypto News | 2026-09-13 19:02:21 | Bitcoin stalls at $77,338 between key support and resistance: Live
  - CoinDesk RSS | 2026-09-12T21:09:06+00:00 | Bitcoin Suisse plans to cut up to half its Swiss jobs as it shifts work abroad
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic chief urges slowdown in AI development to safer pace
  - Anthropic walks tightrope to Nasdaq, pushing for a slowdown while pursuing $2 trillion valuation
  - Anthropic's Amodei says China presents 'toughest dilemma' for his proposed AI slowdown
- recent_evidence:
  - Financial Times YouTube | 61K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-09-14T04:01:01+00:00 | Anthropic walks tightrope to Nasdaq, pushing for a slowdown while pursuing $2 trillion valuation
  - Financial Times Home | 2026-09-13T22:29:46+00:00 | Anthropic tells investors it will be profitable for second straight quarter
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic's Amodei says China presents 'toughest dilemma' for his proposed AI slowdown
  - German firms lift China investment as US outlays fall, IW study shows - Reuters
  - China Sent a Note and Got Absolutely Roasted
- recent_evidence:
  - 무역킹 Trade King YouTube | 74K views | China Sent a Note and Got Absolutely Roasted
  - CNBC Top News | 2026-09-13T16:39:24+00:00 | Anthropic's Amodei says China presents 'toughest dilemma' for his proposed AI slowdown
  - Reuters Markets via Google News RSS | 2026-09-13T06:32:00+00:00 | German firms lift China investment as US outlays fall, IW study shows - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
