# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Fanatics buys regulated exchange in bid to grow prediction markets business
  - Cantor is advising crypto bank AMINA on path to potential public listing
  - Crypto is rewriting how Wall Street traders spend their weekends
- recent_evidence:
  - Cointelegraph | 2026-07-27T13:31:07+00:00 | Rate path still divides investors: Five things to know in Bitcoin this week
  - Investing.com Crypto News | 2026-07-27 13:54:05 | Bitcoin climbs above $65k as easing Middle East tensions lift risk appetite
  - Investing.com Crypto News | 2026-07-27 12:03:05 | Strategy sells MSTR shares, doesn’t buy bitcoin
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia forms 37-member AI security alliance without OpenAI, Anthropic or Google
  - Nvidia, SpaceX, Microsoft launch AI safety initiative as OpenAI cyberattack fallout continues
  - Chinese chip champion CXMT soars 466% in market debut
- recent_evidence:
  - Financial Times YouTube | 46K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-07-27T14:19:43+00:00 | Chipmaker CXMT’s 466% market debut surge makes it the most valuable China-listed company
  - CoinDesk RSS | 2026-07-27T13:25:58+00:00 | Nvidia forms 37-member AI security alliance without OpenAI, Anthropic or Google
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Why Trump's new tariff blitz is very different this time around
  - Chipmaker CXMT’s 466% market debut surge makes it the most valuable China-listed company
  - Chinese chip champion CXMT soars 466% in market debut
- recent_evidence:
  - NYT Business | 2026-07-27T14:23:30+00:00 | Even China’s A.I. Powerhouses Can’t Figure Out How to Profit Off A.I.
  - CNBC Top News | 2026-07-27T14:19:43+00:00 | Chipmaker CXMT’s 466% market debut surge makes it the most valuable China-listed company
  - Reuters Markets via Google News RSS | 2026-07-27T10:54:19+00:00 | Morning Bid: China chip champ - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
