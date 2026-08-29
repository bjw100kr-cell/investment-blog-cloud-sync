# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Bitcoin wallets untouched for 10 years moved $40 million. Most avoided exchanges
  - Ripple is preparing XRP Ledger for quantum computers before ‘Q-Day’ arrives
  - Ethena looks beyond crypto to squeeze yield from booming equity perpetuals
- recent_evidence:
  - CoinDesk RSS | 2026-08-29T04:30:00+00:00 | Bitcoin wallets untouched for 10 years moved $40 million. Most avoided exchanges
  - Cointelegraph | 2026-08-28T15:31:25+00:00 | Bitcoin dips to $78.4K as Fed’s Warsh downplays softer inflation prints
  - Cointelegraph | 2026-08-28T14:53:40+00:00 | Crypto Biz: Bitcoin pumps, Wall Street does the paperwork
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - ‘In a flash, everything was gone’: Nepal rushes to rescue flood survivors
  - China Sees Opportunity in America’s Recent A.I. Security Scares
- recent_evidence:
  - NYT Business | 2026-08-28T18:05:44+00:00 | China Sees Opportunity in America’s Recent A.I. Security Scares
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-31` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Ripple is preparing XRP Ledger for quantum computers before ‘Q-Day’ arrives
  - Nvidia’s revenue forecast is so huge that Wall Street wonders if SpaceX is the reason
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 56K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-08-28T20:58:00+00:00 | Nvidia’s revenue forecast is so huge that Wall Street wonders if SpaceX is the reason
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
