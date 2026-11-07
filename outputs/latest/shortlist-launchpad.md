# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `2`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch
  - The crypto industry has found new ways to grow. Making money from them is another story
  - Thailand moves to block Bitget as crypto exchange's local acquisition faces uncertainty
- recent_evidence:
  - Cointelegraph | 2026-11-06T18:22:42+00:00 | Strive buys 15,124 Bitcoin in October, closes in on top treasury holders
  - Cointelegraph | 2026-11-06T17:49:33+00:00 | Bitcoin price dips under $75K as crypto markets miss tech-stock rebound
  - CoinDesk RSS | 2026-11-06T11:58:40+00:00 | Live updates: Bitcoin flatlines under $76,000 as stock bounce loses steam into the close
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `` / verdict `approve` / quality `needs_fix`
- ready_now: `False` / hero_image_selected: `True`
- intent: 
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Investors brace for lower Anthropic valuation, calling $1.5 trillion a 'stretch'
  - US believes Nvidia’s Huang had romantic relationship with alleged Chinese spy
  - Anthropic to press ahead with IPO targeting $1.5tn valuation
- recent_evidence:
  - Financial Times Home | 2026-11-07T02:33:26+00:00 | US believes Nvidia’s Huang had romantic relationship with alleged Chinese spy
  - MarketWatch Breaking News | 2026-11-06T21:24:00+00:00 | Nvidia, AMD and other chip stocks rebound — but is relief from the ‘violent’ selloff only temporary?
  - CNBC Top News | 2026-11-06T21:07:07+00:00 | Investors brace for lower Anthropic valuation, calling $1.5 trillion a 'stretch'
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
