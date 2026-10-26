# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-27` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - UK banks face 10,000 complaints in 3 months over crypto restrictions
  - Strategy, Strive face balancing act between bitcoin buying and preferred stock dividends
  - Crypto under weekend pressure, bitcoin slides below $80,000 on U.S. Middle East evacuations
- recent_evidence:
  - Cointelegraph | 2026-10-25T22:48:40+00:00 | AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Investing.com Crypto News | 2026-10-25 14:32:13 | Bitcoin steadies near $80,400 after weekend selloff, Fed decision looms
  - Investing.com Crypto News | 2026-10-25 07:02:00 | Bitcoin tests $80K support in descending triangle: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China urges US to halt proposed expansion of outbound investment curbs - Reuters
  - Toyota takes on Tesla and China in humanoid robot race
- recent_evidence:
  - Financial Times World | 2026-10-25T21:00:06+00:00 | Toyota takes on Tesla and China in humanoid robot race
  - Reuters Markets via Google News RSS | 2026-10-24T13:51:55+00:00 | China urges US to halt proposed expansion of outbound investment curbs - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-28` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Elon Musk issues a warning for 'AI neoclouds' as SpaceX borrows $40 billion for chips
  - SpaceX closes $40 billion debt deal for AI chips, Elon Musk says
  - Musk says SpaceX landed a $40 billion debt deal — and forecasts doom for some AI rivals
- recent_evidence:
  - CoinDesk RSS | 2026-10-26T03:11:39+00:00 | Elon Musk issues a warning for 'AI neoclouds' as SpaceX borrows $40 billion for chips
  - CNBC Top News | 2026-10-26T00:37:51+00:00 | SpaceX closes $40 billion debt deal for AI chips, Elon Musk says
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
