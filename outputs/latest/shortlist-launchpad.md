# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-14` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin Suisse plans to cut up to half its Swiss jobs as it shifts work abroad
  - Nigel Farage’s Reform UK lands $97 million donations from two crypto billionaires in 24 hours
  - Ditching bonds for bitcoin: How crypto can tackle the AI-heavy portfolio dilemma
- recent_evidence:
  - CoinDesk RSS | 2026-09-12T21:09:06+00:00 | Bitcoin Suisse plans to cut up to half its Swiss jobs as it shifts work abroad
  - CoinDesk RSS | 2026-09-12T16:00:00+00:00 | Ditching bonds for bitcoin: How crypto can tackle the AI-heavy portfolio dilemma
  - CoinDesk RSS | 2026-09-12T10:11:01+00:00 | Bitcoin activity, passports exposed after Revolut falls for fake government request
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic CEO calls for AI race to slow down citing safety. Musk and OpenAI's Altman agrees
  - Nvidia considers $10B investment in potential record Anthropic IPO: Reuters
  - Elon Musk backs Anthropic’s call to slow down AI progress before rogue bots take over the entire internet
- recent_evidence:
  - Financial Times YouTube | 60K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CoinDesk RSS | 2026-09-12T18:43:33+00:00 | Anthropic CEO calls for AI race to slow down citing safety. Musk and OpenAI's Altman agrees
  - MarketWatch Breaking News | 2026-09-12T17:20:00+00:00 | Elon Musk backs Anthropic’s call to slow down AI progress before rogue bots take over the entire internet
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Oil's roundtrip back to $100. Why China could determine what happens next
  - GM plans U.S. battery development as Trump's DOT attacks Ford for China ties
  - China Sent a Note and Got Absolutely Roasted
- recent_evidence:
  - 무역킹 Trade King YouTube | 62K views | China Sent a Note and Got Absolutely Roasted
  - CNBC Top News | 2026-09-12T12:40:05+00:00 | Oil's roundtrip back to $100. Why China could determine what happens next
  - CNBC Top News | 2026-09-12T12:00:01+00:00 | GM plans U.S. battery development as Trump's DOT attacks Ford for China ties
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
