# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin is flashing 8 of 12 capitulation signals, but bottom's not yet in, says VanEck
  - A year after losing $1.46 billion, Bybit says AI helped it save $700 million
  - Fed decision making comes into focus as bitcoin holds steady, bond yields surge
- recent_evidence:
  - CoinDesk RSS | 2026-08-19T12:45:35+00:00 | Bitcoin is flashing 8 of 12 capitulation signals, but bottom's not yet in, says VanEck
  - Cointelegraph | 2026-08-19T11:59:30+00:00 | Sweden’s H100 reports $26M H1 loss driven by falling Bitcoin value
  - CoinDesk RSS | 2026-08-19T11:14:50+00:00 | Fed decision making comes into focus as bitcoin holds steady, bond yields surge
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OpenAI trails Anthropic as losses deepen and Altman pauses frontier AI training
  - SK Hynix suggests its stock is too cheap as it embarks on $29 billion buyback
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 54K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CoinDesk RSS | 2026-08-19T09:10:22+00:00 | OpenAI trails Anthropic as losses deepen and Altman pauses frontier AI training
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-22` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China triples its e-CNY network in 2026 as 8 more banks join the CBDC push this week
  - Chinese robotic company’s stock soars over 600% in trading debut
  - Europe Hurries to Fund More Cutting-Edge Businesses to Compete With China and U.S.
- recent_evidence:
  - CoinDesk RSS | 2026-08-19T11:55:45+00:00 | China triples its e-CNY network in 2026 as 8 more banks join the CBDC push this week
  - NYT Business | 2026-08-19T09:02:53+00:00 | Europe Hurries to Fund More Cutting-Edge Businesses to Compete With China and U.S.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
