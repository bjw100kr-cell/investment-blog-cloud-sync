# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Gate bets all-in-one money app is crypto’s biggest consumer trend this year and next
  - Crypto Long & Short: Zcash and the case for privacy in the age of AI
  - Crypto trading giant GSR's new vault business is a $100M bet on onchain credit
- recent_evidence:
  - Cointelegraph | 2026-10-07T15:06:14+00:00 | Bitcoin price drops to $82.7K October low as bond sell-off resumes on Iran nerves
  - Investing.com Crypto News | 2026-10-07 13:52:32 | Bitcoin drops to $83k amid pressure from rising oil prices, yields
  - Investing.com Crypto News | 2026-10-07 10:52:38 | Bitcoin falls as Iran attacks, oil surge fuel rate fears; crypto stocks slip
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Supertanker chartered from Gulf Coast to China for $76 million, 10 times higher than pre-war level
  - China slaps down EU request for voluntary curbs on hybrid car exports
  - 4. Why the Outcome of the Talks Differs (U.S.-China Summit)
- recent_evidence:
  - 무역킹 Trade King YouTube | 46K | 3. They may have smiled to each other, but China’s true intentions... (US-China Summit)
  - 무역킹 Trade King YouTube | 23K | 4. Why the Outcome of the Talks Differs (U.S.-China Summit)
  - CNBC Top News | 2026-10-07T18:32:55+00:00 | Supertanker chartered from Gulf Coast to China for $76 million, 10 times higher than pre-war level
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-09` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Microsoft to sell $2,599 Surface Laptop Ultra containing Nvidia AI chip
  - SpaceX credit risk jumps on worries over its borrowing spree
  - SpaceX may chase ‘stunning’ AI returns by taking on a lot of debt to buy Nvidia chips
- recent_evidence:
  - CNBC Top News | 2026-10-07T18:34:31+00:00 | Microsoft to sell $2,599 Surface Laptop Ultra containing Nvidia AI chip
  - MarketWatch Breaking News | 2026-10-07T18:22:00+00:00 | SpaceX may chase ‘stunning’ AI returns by taking on a lot of debt to buy Nvidia chips
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
