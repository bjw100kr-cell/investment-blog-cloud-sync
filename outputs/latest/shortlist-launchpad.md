# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - A tiny payment can expose the IP address behind a bitcoin wallet, developer finds
  - Bitcoin’s dormant supply rises, a behavior seen during previous bear-market bottoming phases
  - Crypto for Advisors: Four questions to ask before trusting a crypto exchange
- recent_evidence:
  - Investing.com Crypto News | 2026-11-27 05:52:57 | Bitcoin recovers to $61.5k; set for first positive week in 8
  - CoinDesk RSS | 2026-11-26T17:30:00+00:00 | A tiny payment can expose the IP address behind a bitcoin wallet, developer finds
  - CoinDesk RSS | 2026-11-26T16:50:23+00:00 | Bitcoin’s dormant supply rises, a behavior seen during previous bear-market bottoming phases
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia chip buyers told to rule out Chinese renters to purchase GPUs, sources say
  - I hate that Jensen Huang is back at Nvidia, but I love what it’s done for my 401(k). Am I a hypocrite?
  - We are living in perilous times if Nvidia CEO Jensen Huang dictates your 401(k) balance
- recent_evidence:
  - NYT Business | 2026-11-27T02:45:41+00:00 | Nvidia Halts Sales to Southeast Asia as U.S. Tightens China Restrictions
  - MarketWatch Breaking News | 2026-11-27T01:15:00+00:00 | I hate that Jensen Huang is back at Nvidia, but I love what it’s done for my 401(k). Am I a hypocrite?
  - MarketWatch Breaking News | 2026-11-27T00:31:00+00:00 | We are living in perilous times if Nvidia CEO Jensen Huang dictates your 401(k) balance
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-30` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China’s factories are growing profits again, but the AI boom is picking the winners
  - Chinese households shed billions in consumer debt
  - Taiwan Election Interference: Is China Aiming for Division?
- recent_evidence:
  - 무역킹 Trade King YouTube | 33K | Taiwan Election Interference: Is China Aiming for Division?
  - CNBC Top News | 2026-11-27T06:09:51+00:00 | China’s factories are growing profits again, but the AI boom is picking the winners
  - NYT Business | 2026-11-27T02:45:41+00:00 | Nvidia Halts Sales to Southeast Asia as U.S. Tightens China Restrictions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
