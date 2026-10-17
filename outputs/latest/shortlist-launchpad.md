# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-10-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - 'Dead money’ for a decade: Why this hedge fund approach may deliver an advantage over bonds
  - Bitcoin ticks up slightly above $82k as U.S. bond rally lifts risk sentiment
  - Anthropic offers Blackstone double-digit yield in latest chip financing
- recent_evidence:
  - CNBC Top News | 2026-10-17T15:00:01+00:00 | 'Dead money’ for a decade: Why this hedge fund approach may deliver an advantage over bonds
  - MarketWatch Breaking News | 2026-10-17T13:00:00+00:00 | Meet the home buyers totally unfazed by 7% mortgage rates
  - Financial Times Home | 2026-10-17T00:47:25+00:00 | Anthropic offers Blackstone double-digit yield in latest chip financing
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - ‘Wow, it’s a real discovery’: Claude cracks a 25-year NSA number mystery
  - Satoshi-era bitcoin faces a bigger quantum threat after Google’s new Willow breakthrough
  - Here’s what happened in crypto today
- recent_evidence:
  - CoinDesk RSS | 2026-10-17T02:30:00+00:00 | Satoshi-era bitcoin faces a bigger quantum threat after Google’s new Willow breakthrough
  - Investing.com Crypto News | 2026-10-17 14:14:28 | Bitcoin price holds near $81,000 as ETF outflows weigh on sentiment
  - Investing.com Crypto News | 2026-10-17 07:02:26 | Bitcoin stuck below 200 SMA at $81,621: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-19` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Satoshi-era bitcoin faces a bigger quantum threat after Google’s new Willow breakthrough
  - Anthropic offers Blackstone double-digit yield in latest chip financing
  - Chart of the Week: The chip stock split
- recent_evidence:
  - Financial Times World | 2026-10-17T09:30:02+00:00 | Chart of the Week: The chip stock split
  - Financial Times Home | 2026-10-17T00:47:25+00:00 | Anthropic offers Blackstone double-digit yield in latest chip financing
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
