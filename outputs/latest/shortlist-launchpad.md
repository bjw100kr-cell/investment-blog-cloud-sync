# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-27` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Over 1,000 Bitcoin miners were tricked into working for a thief by a fake internet route
  - Bill to lock up U.S. government bitcoin for 20 years advances to full House
  - French Senate blocks new crypto tax and wallet list critics called a kidnapping risk
- recent_evidence:
  - CoinDesk RSS | 2026-11-26T06:19:09+00:00 | Over 1,000 Bitcoin miners were tricked into working for a thief by a fake internet route
  - CoinDesk RSS | 2026-11-26T04:46:01+00:00 | Bill to lock up U.S. government bitcoin for 20 years advances to full House
  - Investing.com Crypto News | 2026-11-26 06:32:24 | Bitcoin recovers to $60.5k, but rates, regulatory fears persist
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - S&P warns Nvidia credit rating could be cut over 'rising' management and governance risk
  - Nvidia halts chip shipments to south-east Asia
  - ‘Jensanity’ erupts in Taiwan and China on Nvidia founder’s comeback
- recent_evidence:
  - Financial Times World | 2026-11-26T06:59:54+00:00 | Bank of Korea raises interest rates amid AI chip boom
  - Financial Times World | 2026-11-26T05:33:25+00:00 | FirstFT: Nvidia halts chip shipments to south-east Asia
  - Financial Times Home | 2026-11-26T05:00:19+00:00 | Nvidia halts chip shipments to south-east Asia
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - How Trump’s latest tariff moves hand India an edge over rival Asian exporters
  - U.S. proposes new tariffs on 14 trading partners, including China and the EU
  - ‘Jensanity’ erupts in Taiwan and China on Nvidia founder’s comeback
- recent_evidence:
  - NYT Business | 2026-11-26T05:00:17+00:00 | In China, the ‘Female Gaze’ Is Driving a New Entertainment Boom
  - Financial Times Home | 2026-11-26T00:45:54+00:00 | ‘Jensanity’ erupts in Taiwan and China on Nvidia founder’s comeback
  - CNBC Top News | 2026-11-25T16:02:52+00:00 | U.S. proposes new tariffs on 14 trading partners, including China and the EU
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
