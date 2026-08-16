# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-08-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Swiss mega-bank UBS ramps up its Bitcoin exposure with a massive 24-fold surge in ETF call options
  - Why the world’s second-largest Bitcoin mining power is shutting down rigs in its capital city
  - Paul Tudor Jones’ investment firm increases stake in BlackRock's bitcoin ETF after year of selling
- recent_evidence:
  - CoinDesk RSS | 2026-08-15T15:56:05+00:00 | Swiss mega-bank UBS ramps up its Bitcoin exposure with a massive 24-fold surge in ETF call options
  - CoinDesk RSS | 2026-08-15T15:21:15+00:00 | Why the world’s second-largest Bitcoin mining power is shutting down rigs in its capital city
  - CoinDesk RSS | 2026-08-15T15:12:29+00:00 | Paul Tudor Jones’ investment firm increases stake in BlackRock's bitcoin ETF after year of selling
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-08-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - I drove Tesla FSD, Rivian Autonomy+ ‘hands-free’ driving systems. Here’s how they compare
  - China poised to lift travel ban on Manus founders
  - EXCLUSIVE: Apple trains its own AI model for China market with Alibaba's support, sources say - Reuters
- recent_evidence:
  - CNBC Top News | 2026-08-15T12:00:01+00:00 | I drove Tesla FSD, Rivian Autonomy+ ‘hands-free’ driving systems. Here’s how they compare
  - Reuters Markets via Google News RSS | 2026-08-14T21:45:59+00:00 | EXCLUSIVE: Apple trains its own AI model for China market with Alibaba's support, sources say - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
