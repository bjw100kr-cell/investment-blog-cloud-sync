# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-07-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Fed meeting minutes to show 'family fight' over rates. The squabble could drag on for a while
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-09` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Crypto Long & Short: With MSTR concerns assuaged, look to traditional signals around BTC
  - Crypto VC Paradigm launches $1.2 billion AI fund as it broadens beyond digital assets
  - Citadel abandons multi-year crypto lawsuit to focus on bankruptcy order against an ex-employee
- recent_evidence:
  - Cointelegraph | 2026-07-08T15:35:31+00:00 | Bitcoin slides as Iran ceasefire collapse sees $75 oil on Hormuz blockade threats
  - Cointelegraph | 2026-07-08T13:36:44+00:00 | Bull Bitcoin asks French court to strike down DAC8 implementing decree
  - Cointelegraph | 2026-07-08T12:59:06+00:00 | BTC speculators in focus as analysis says 'textbook Bitcoin bottom' is underway
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담

- keyword `ai_growth_stocks` / publish `2026-07-10` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Palantir’s real weak spot
  - Palantir Is Moving the Japanese Military
  - Palantir: profits, procurement and power | FT Film
- recent_evidence:
  - 무역킹 Trade King YouTube | 38K views | Palantir Is Moving the Japanese Military
  - Financial Times YouTube | 26K views | Palantir: profits, procurement and power | FT Film
  - Financial Times Home | 2026-07-08T04:00:09+00:00 | Palantir’s real weak spot
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks --apply`
