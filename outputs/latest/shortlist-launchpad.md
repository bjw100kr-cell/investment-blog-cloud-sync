# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin, gold trim early losses as yen gives up gains. Oil stays near $100
  - Senate's top Democratic investigator looking into Tether payments to Bo Hines' firm
  - A16z is the latest VC giant to widen bets beyond crypto and into AI and emerging tech
- recent_evidence:
  - CoinDesk RSS | 2026-10-23T03:13:01+00:00 | Bitcoin, gold trim early losses as yen gives up gains. Oil stays near $100
  - Cointelegraph | 2026-10-23T00:59:35+00:00 | Switzerland approves first spot Bitcoin ETF for retail investors
  - Investing.com Crypto News | 2026-10-22 21:41:46 | Bitcoin dives 4%, slides below $82k as AI rout, oil surge slams risk sentiment
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Meta stock sinks nearly 7% as AI spend pushes free cash flow negative
  - Steep bill for AI buildout punishes Meta, other tech favorites - Reuters
  - 3 big reasons Micron and other chip stocks fell hard on Thursday
- recent_evidence:
  - CNBC Top News | 2026-10-22T20:03:03+00:00 | Meta stock sinks nearly 7% as AI spend pushes free cash flow negative
  - Reuters Markets via Google News RSS | 2026-10-22T18:33:00+00:00 | Steep bill for AI buildout punishes Meta, other tech favorites - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-10-23` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - 10-year Treasury yield tumbles below 5% to lowest level in nearly a month
  - Europe’s bracing reality on US bond yields
  - Beware Bessent’s tilt towards short-term debt
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-23T01:50:00+00:00 | Asian shares wobble as tech rout boosts bonds, dents rate hike bets - Reuters
  - Financial Times Home | 2026-10-22T23:13:15+00:00 | US Treasury proposes tighter rules on investing in sensitive Chinese tech
  - MarketWatch Breaking News | 2026-10-22T22:07:00+00:00 | Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
