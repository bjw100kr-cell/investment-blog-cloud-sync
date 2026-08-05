# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `2`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto may have institutionalized, but it still trades like a rumor mill
  - SpaceX extends decline to 11% on lockup expiration and capex spending fears
  - The $120 million Coldcard hack lights up Bitcoin's memory pool
- recent_evidence:
  - CoinDesk RSS | 2026-08-05T11:20:58+00:00 | The $120 million Coldcard hack lights up Bitcoin's memory pool
  - Cointelegraph | 2026-08-05T10:43:05+00:00 | Bitcoin ETFs log inflows as cold wallet hack reignites custody debate
  - Investing.com Crypto News | 2026-08-05 13:07:25 | Bitcoin rangebound above $64k with Hormuz deal in focus
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `` / verdict `approve` / quality `needs_fix`
- ready_now: `False` / hero_image_selected: `True`
- intent: 
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic's Mythos created fake identities to fool humans in new cyber incident
  - 3 reasons AMD’s stock is falling in the face of its latest earnings report
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 50K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-08-05T13:48:00+00:00 | 3 reasons AMD’s stock is falling in the face of its latest earnings report
  - CNBC Top News | 2026-08-05T10:18:07+00:00 | Anthropic's Mythos created fake identities to fool humans in new cyber incident
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
