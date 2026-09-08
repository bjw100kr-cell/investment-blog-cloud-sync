# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-09` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Polish prosecutors charge fifth suspect in a massive crypto probe
  - Bitcoin blinks less than gold when Treasury yields move
  - Liquid ‘white hats’ return $270M in Bitcoin as network prepares restart
- recent_evidence:
  - Cointelegraph | 2026-09-08T03:46:17+00:00 | Liquid ‘white hats’ return $270M in Bitcoin as network prepares restart
  - Cointelegraph | 2026-09-07T17:29:27+00:00 | Bitcoin fund flows show investors trading Fed rate path, not exiting market: CoinShares
  - Cointelegraph | 2026-09-07T16:42:49+00:00 | Capital B adds 376 Bitcoin in $29M purchase, boosting holdings to 3,521 BTC
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia supplier Wistron's shares drop after it announces $1.5 billion global stock sale
  - Huawei drives China’s push to make its own advanced chips
  - Chip stock investors beware — these charts could warn of further weakness ahead
- recent_evidence:
  - Financial Times YouTube | 59K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-09-08T03:54:54+00:00 | Nvidia supplier Wistron's shares drop after it announces $1.5 billion global stock sale
  - Financial Times Home | 2026-09-08T02:57:46+00:00 | Huawei drives China’s push to make its own advanced chips
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's imports in August miss estimates as exports pick up pace amid calls for rebalancing trade
  - CNBC's The China Connection newsletter: China's weak consumer becomes the world's problem
  - Huawei drives China’s push to make its own advanced chips
- recent_evidence:
  - CNBC Top News | 2026-09-08T03:10:42+00:00 | China's imports in August miss estimates as exports pick up pace amid calls for rebalancing trade
  - Financial Times Home | 2026-09-08T03:00:21+00:00 | China’s exports jump 25% in August in boost from AI build-out
  - Financial Times Home | 2026-09-08T02:57:46+00:00 | Huawei drives China’s push to make its own advanced chips
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
