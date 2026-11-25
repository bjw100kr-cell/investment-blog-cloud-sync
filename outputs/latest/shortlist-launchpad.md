# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Crypto traders can now hedge Nvidia, Anthropic and oil bets on Derive
  - A year after buying bitcoin, Czech central bank won't say what it's worth
  - 'AI trade never died': Traders see room for market recovery, but bitcoin's participation is another story
- recent_evidence:
  - CoinDesk RSS | 2026-11-25T04:50:08+00:00 | A year after buying bitcoin, Czech central bank won't say what it's worth
  - Cointelegraph | 2026-11-25T01:40:59+00:00 | CleanSpark weighs selling more Bitcoin than it mines to de-risk books
  - Investing.com Crypto News | 2026-11-25 06:19:34 | Bitcoin extends losses below $59,000 as ETF outflows weigh
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-27` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (8개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (엔비디아 ceo 미국 의회 조사 최신 뉴스 알려줘)
- sample_headlines:
  - 엔비디아 ceo 미국 의회 조사 최신 뉴스 알려줘
  - Crypto traders can now hedge Nvidia, Anthropic and oil bets on Derive
  - Trump says he's willing to give Nvidia's Huang a pardon, doesn't think he needs one
- recent_evidence:
  - Google Trends KR | 2026-11-24T21:50:00-08:00 | 엔비디아 ceo 미국 의회 조사 최신 뉴스 알려줘
  - CNBC Top News | 2026-11-25T06:29:46+00:00 | AI debt worries grow as Nvidia rebound masks Big Tech spending squeeze
  - Financial Times Home | 2026-11-25T06:00:02+00:00 | Anthropic has pulled up the ladder
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Trump readies raft of new tariffs on major economies
  - China issues list of demands to Brussels over EU trade talks
- recent_evidence:
  - Financial Times World | 2026-11-25T06:00:02+00:00 | China issues list of demands to Brussels over EU trade talks
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
