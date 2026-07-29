# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - The inside story of how a hike in Hong Kong changed crypto trading forever
  - 3 reasons Wednesday's Fed meeting is pivotal for BTC
  - Bitcoin steadies above $64,000 as crypto looks to Fed interest-rate decision
- recent_evidence:
  - CoinDesk RSS | 2026-07-29T10:34:18+00:00 | Bitcoin steadies above $64,000 as crypto looks to Fed interest-rate decision
  - Investing.com Crypto News | 2026-07-29 13:26:38 | Bitcoin hovers above $64k ahead of Fed decision, shrugs off AI-led tech weakness
  - Investing.com Crypto News | 2026-07-29 07:04:01 | Bitcoin coiled between SMAs at $64,408: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-31` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Tech rout roils markets after SK Hynix profits disappoint
  - ‘Anti-tech’ index shines in global chip rout
  - Wall St opens lower ahead of Fed decision; chip stocks wobble - reuters.com
- recent_evidence:
  - Financial Times YouTube | 47K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Reuters Markets via Google News RSS | 2026-07-29T13:35:43+00:00 | Wall St opens lower ahead of Fed decision; chip stocks wobble - reuters.com
  - NYT Business | 2026-07-29T10:45:53+00:00 | The Chips That Will Decide A.I.’s Future
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nike was once China's sneaker king. Here's why its sales have fallen 30%
  - Ferrari EV designed by Jony Ive has already hit 2026 sales target
  - 3. The Final Chapter on the Northern Sea Route: The Complex Motives of South Korea, China, and Japan
- recent_evidence:
  - CNBC Top News | 2026-07-29T11:46:44+00:00 | Nike was once China's sneaker king. Here's why its sales have fallen 30%
  - NYT Business | 2026-07-29T09:02:02+00:00 | Trump’s Tariffs Are Sending Some Companies Back to China
  - 무역킹 Trade King YouTube | 10K views | 3. The Final Chapter on the Northern Sea Route: The Complex Motives of South Korea, China, and Japan
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
