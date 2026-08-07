# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - After a Clarity Act funeral, the crypto world would keep turning
  - Why Bitcoin's BIP-110 refuses to die despite near-zero miner support
  - Bitcoin’s volatility has nearly disappeared. The risk hasn’t.
- recent_evidence:
  - Cointelegraph | 2026-08-07T13:00:01+00:00 | Bitcoiners turn to dice throws as self-custody setups are re-evaluated
  - CoinDesk RSS | 2026-08-07T11:45:49+00:00 | Why Bitcoin's BIP-110 refuses to die despite near-zero miner support
  - CoinDesk RSS | 2026-08-07T11:42:20+00:00 | Bitcoin’s volatility has nearly disappeared. The risk hasn’t.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Solar stocks shine after Trump extends China tariffs to polysilicon products
  - Optical stocks have a China problem that most investors are missing
  - China’s Export Boom Rolls On Despite Trade Backlash
- recent_evidence:
  - CNBC Top News | 2026-08-07T12:13:07+00:00 | Solar stocks shine after Trump extends China tariffs to polysilicon products
  - MarketWatch Breaking News | 2026-08-07T11:00:00+00:00 | Optical stocks have a China problem that most investors are missing
  - NYT Business | 2026-08-07T07:20:24+00:00 | China’s Export Boom Rolls On Despite Trade Backlash
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-09` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (amd)
- sample_headlines:
  - amd
  - SK Hynix to invest $38 billion building new memory chip plants as demand soars
  - Micron’s stock falls but is spared the worst of the memory-chip selloff
- recent_evidence:
  - Google Trends KR | 2026-08-07T04:30:00-07:00 | amd
  - Financial Times YouTube | 50K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-08-07T09:02:59+00:00 | SK Hynix to invest $38 billion building new memory chip plants as demand soars
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
