# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Saylor's Strategy raises cash reserves to $3.2 billion, leaving bitcoin holdings unchanged
  - A bitcoin 'volmageddon' may be brewing, key indicator suggests
  - Bernstein raises Robinhood price target, cites tokenization and prediction markets
- recent_evidence:
  - Cointelegraph | 2026-07-20T15:47:00+00:00 | Bitcoin price hits $65K wall as stocks battle ‘record’ institutional tech sell-off
  - Cointelegraph | 2026-07-20T13:30:00+00:00 | Peter Brandt predicts the exact day Bitcoin’s bear market will be over
  - Cointelegraph | 2026-07-20T12:39:49+00:00 | Strategy raises $263.5M through MSTR sales, holds 843,775 Bitcoin
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-22` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - AMD launches Helios, its first rack AI system to rival Nvidia, adding Microsoft as newest buyer
  - Alphabet stock pops on report it's developing a more efficient AI chip
  - S&P 500, Nasdaq edge higher as chips recover; megacap earnings in focus - Reuters
- recent_evidence:
  - Financial Times YouTube | 39K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-07-20T17:05:00+00:00 | Forget Nvidia. These 5 S&P 500 stocks are quietly going all in on AI.
  - Reuters Markets via Google News RSS | 2026-07-20T16:23:20+00:00 | S&P 500, Nasdaq edge higher as chips recover; megacap earnings in focus - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's Moonshot pauses Kimi subscriptions amid hot demand, IPO push - Reuters
  - Soaring Egg Prices Are Hitting China Hard
- recent_evidence:
  - NYT Business | 2026-07-20T13:44:32+00:00 | Soaring Egg Prices Are Hitting China Hard
  - Reuters Markets via Google News RSS | 2026-07-20T08:07:34+00:00 | China's Moonshot pauses Kimi subscriptions amid hot demand, IPO push - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
