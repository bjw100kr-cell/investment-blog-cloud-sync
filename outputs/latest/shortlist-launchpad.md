# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto Long & Short: The crypto question isn't what to own — it's what you can survive holding
  - U.S. seeks forfeiture of $25 million in crypto tied to romance and investment scams
  - Forget Nvidia: The next big AI trade could be crypto and blockchain
- recent_evidence:
  - Cointelegraph | 2026-07-22T15:55:20+00:00 | Bitcoin price avoids major Iran jitters as S&P 500 ‘short squeeze’ on horizon
  - Cointelegraph | 2026-07-22T11:55:21+00:00 | Bitcoin analysis eyes ‘serious volume’ after Binance sees 9K BTC daily outflow
  - Investing.com Crypto News | 2026-07-22 13:53:24 | Bitcoin subdued near $66k with focus on CLARITY Act, Iran tensions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Forget Nvidia: The next big AI trade could be crypto and blockchain
  - Morning Bid: The new ad for chips? An AI model Breaking Bad - Reuters
  - AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s dominance
- recent_evidence:
  - Financial Times YouTube | 42K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-07-22T16:58:00+00:00 | AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s dominance
  - CoinDesk RSS | 2026-07-22T13:32:40+00:00 | Forget Nvidia: The next big AI trade could be crypto and blockchain
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-25` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Mercedes risks US sales ban under Senate China bill
- recent_evidence:
  - Financial Times Home | 2026-07-22T14:00:30+00:00 | Mercedes risks US sales ban under Senate China bill
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
