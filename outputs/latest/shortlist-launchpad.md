# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitcoin rebound already losing steam as AI trade returns with a bang
  - Cathie Wood's ARK Invest pulls the plug on two planned crypto ETFs
  - Eric Trump-backed American Bitcoin secures $150 million loan against its bitcoin
- recent_evidence:
  - CoinDesk RSS | 2026-11-23T17:31:27+00:00 | Bitcoin rebound already losing steam as AI trade returns with a bang
  - Cointelegraph | 2026-11-23T16:51:17+00:00 | Bitcoin rebounds 17% from $55K lows as Nvidia rally sparks $500M crypto liquidations
  - Cointelegraph | 2026-11-23T16:23:37+00:00 | Cross River Bank enters Bitcoin-backed lending with $250K loans
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (8개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia's Jensen Huang faces Senate scrutiny despite Trump-backed return as CEO
  - Bitcoin rebound already losing steam as AI trade returns with a bang
  - Nvidia soars as Jensen Huang returns to lead company
- recent_evidence:
  - CNBC Top News | 2026-11-23T23:42:17+00:00 | Trump sealed deal for Nvidia to rehire Jensen Huang as CEO
  - NYT Business | 2026-11-23T23:18:58+00:00 | Trump Administration Imposes Sanctions on Megaspeed, Singaporean Firm at Center of Nvidia Scandal
  - CNBC Top News | 2026-11-23T23:14:34+00:00 | Jim Cramer sees more upside for Nvidia stock with Jensen Huang back as CEO
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-11-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-10-28T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`
