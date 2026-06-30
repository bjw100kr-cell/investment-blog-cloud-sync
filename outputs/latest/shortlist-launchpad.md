# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. FOMC 이후 시장 해설

- keyword `fomc` / publish `2026-07-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Minutes of the Federal Open Market Committee, April 28-29, 2026
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
- confirm_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`

## 2. 비트코인 핵심 흐름 해설

- keyword `bitcoin` / publish `2026-07-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성
- sample_headlines:
  - Jefferies warns of crypto market volatility as Clarity Act faces Senate test
  - Bitcoin’s quiet $59,000-$60,000 range is starting to look dangerous
  - Bitcoin $4.4 billion supply overhang emerges as institutional demand wilts
- recent_evidence:
  - Cointelegraph | 2026-06-30T12:44:21+00:00 | Swan's Cory Klippsten sees record Bitcoin holder supply revealing early bottom
  - CoinDesk RSS | 2026-06-30T11:55:34+00:00 | Bitcoin’s quiet $59,000-$60,000 range is starting to look dangerous
  - CoinDesk RSS | 2026-06-30T11:18:34+00:00 | Bitcoin $4.4 billion supply overhang emerges as institutional demand wilts
- confirm_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 증시 지수 흐름 해설

- keyword `us_index_flow` / publish `2026-07-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Nasdaq expands distribution of its market data into blockchain infrastructure
  - Tech selloff stirs bubble fears in US stock market - Reuters
  - AI spending, earnings hopes, Fed outlook set to sway US stocks in second half - Reuters
- recent_evidence:
  - CoinDesk RSS | 2026-06-30T13:00:00+00:00 | Nasdaq expands distribution of its market data into blockchain infrastructure
  - Reuters Markets via Google News RSS | 2026-06-30T10:25:32+00:00 | AI spending, earnings hopes, Fed outlook set to sway US stocks in second half - Reuters
  - Reuters Markets via Google News RSS | 2026-06-30T09:04:09+00:00 | Tech selloff stirs bubble fears in US stock market - Reuters
- confirm_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
