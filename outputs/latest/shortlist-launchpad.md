# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin nears $81,000 ahead of Fed decision as ZEC jumps 8%
  - Coinbase says user funds are safe after third-party vendor exposes customer contact info
  - Treasury's Bessent sees crypto as America's next tool for keeping the U.S. dollar on top
- recent_evidence:
  - CoinDesk RSS | 2026-10-28T04:15:20+00:00 | Bitcoin nears $81,000 ahead of Fed decision as ZEC jumps 8%
  - Cointelegraph | 2026-10-27T21:28:22+00:00 | VanEck launches diversified ETF combining stocks, bonds and Bitcoin exposure
  - Cointelegraph | 2026-10-27T20:33:19+00:00 | Quantum fears already limiting Bitcoin’s growth, Stacks founder says
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Indian investors rush to Nvidia, SpaceX, Apple as local trading apps roll out access to U.S. stocks
  - Anthropic's IPO could be 'speculative fiction' or a 'generational moment' — investors are split
  - PrimeXBT Brings Tesla, SpaceX, NVIDIA and More to Crypto Futures with New Tokenised Stocks
- recent_evidence:
  - CNBC Top News | 2026-10-28T01:56:59+00:00 | SK Hynix shares soar over 8% as profit beats, chipmaker to return $25 billion to investors
  - CNBC Top News | 2026-10-28T00:14:24+00:00 | Indian investors rush to Nvidia, SpaceX, Apple as local trading apps roll out access to U.S. stocks
  - MarketWatch Breaking News | 2026-10-27T22:51:00+00:00 | Retail traders buy the dip on chip stocks — but Robinhood gets burned by the crypto market
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-31` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China rushes to shore up struggling markets
  - China Steps In to Rescue Stocks, But the Market Continues to Fall
- recent_evidence:
  - Financial Times Home | 2026-10-28T03:54:50+00:00 | China rushes to shore up struggling markets
  - NYT Business | 2026-10-27T14:15:17+00:00 | China Steps In to Rescue Stocks, But the Market Continues to Fall
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
