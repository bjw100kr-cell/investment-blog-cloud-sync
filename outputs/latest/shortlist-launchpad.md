# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Goldman Sachs brings $100 billion Treasury fund into crypto’s institutional plumbing
  - The restaking gold rush is over, and top protocols are barely making a profit
  - Chainlink launches new version of its crypto bridge tech 'CCIP' to give apps more control over their security
- recent_evidence:
  - MarketWatch Breaking News | 2026-09-28T17:30:00+00:00 | ‘I’m never selling’: I’m 47 and buy bitcoin with every dollar I earn. Am I crazy?
  - Cointelegraph | 2026-09-28T12:38:01+00:00 | Strategy buys 1,665 Bitcoin for $143M as BTC stack hits 847,666
  - CoinDesk RSS | 2026-09-28T12:13:09+00:00 | THORChain rejects Bitget request to block hacker as $6 million moves to bitcoin
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OpenAI sparked Hugging Face bids with early investment offer ahead of Nvidia's $13 billion deal
  - Nvidia share buyback plan gets $150 billion boost
  - Anthropic launches cheaper AI model, its second release since CEO's call for a slowdown
- recent_evidence:
  - CNBC Top News | 2026-09-28T18:47:21+00:00 | OpenAI sparked Hugging Face bids with early investment offer ahead of Nvidia's $13 billion deal
  - NYT Business | 2026-09-28T18:01:42+00:00 | Nvidia Adds $150 Billion to Massive Stock Buyback, the Largest Ever
  - CNBC Top News | 2026-09-28T18:00:06+00:00 | Anthropic launches cheaper AI model, its second release since CEO's call for a slowdown
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - The U.S. and China agree to $60 billion in tariff cuts on products like dolls and fireworks. Rare earths remain a sticking point.
  - Two of China’s EV Makers Announce a Deal as Auto Industry Moves Toward Consolidation
  - China and the U.S. Pledge to Cut Tariffs on $60 Billion in Goods
- recent_evidence:
  - MarketWatch Breaking News | 2026-09-28T18:15:00+00:00 | The U.S. and China agree to $60 billion in tariff cuts on products like dolls and fireworks. Rare earths remain a sticking point.
  - NYT Business | 2026-09-28T18:05:11+00:00 | China and the U.S. Pledge to Cut Tariffs on $60 Billion in Goods
  - NYT Business | 2026-09-28T16:46:59+00:00 | Two of China’s EV Makers Announce a Deal as Auto Industry Moves Toward Consolidation
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
