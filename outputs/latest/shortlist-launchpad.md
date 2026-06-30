# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 핵심 흐름 해설

- keyword `bitcoin` / publish `2026-07-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성
- sample_headlines:
  - Jefferies warns of crypto market volatility as Clarity Act faces Senate test
  - Bitcoin’s quiet $59,000-$60,000 range is starting to look dangerous
  - Here’s what happened in crypto today
- recent_evidence:
  - Cointelegraph | 2026-06-30T12:44:21+00:00 | Swan's Cory Klippsten sees record Bitcoin holder supply revealing early bottom
  - CoinDesk RSS | 2026-06-30T11:55:34+00:00 | Bitcoin’s quiet $59,000-$60,000 range is starting to look dangerous
  - Investing.com Crypto News | 2026-06-30 14:07:35 | Bitcoin weak below $60k as rate jitters, ETF outflows persist
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름 해설

- keyword `us_index_flow` / publish `2026-07-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Nasdaq expands distribution of its market data into blockchain infrastructure
  - AI spending, earnings hopes, Fed outlook set to sway US stocks in second half - Reuters
  - Tech selloff stirs bubble fears in US stock market - Reuters
- recent_evidence:
  - Financial Times World | 2026-06-30T14:53:33+00:00 | German leftwing terrorism on the rise, spy agency warns
  - CoinDesk RSS | 2026-06-30T13:00:00+00:00 | Nasdaq expands distribution of its market data into blockchain infrastructure
  - Reuters Markets via Google News RSS | 2026-06-30T10:25:32+00:00 | AI spending, earnings hopes, Fed outlook set to sway US stocks in second half - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향 해설

- keyword `china` / publish `2026-07-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - 1. The Grand Design to Pressure China
  - Starmer’s £15bn defence plan leaves short-term gaps, say former officers
- recent_evidence:
  - 무역킹 Trade King YouTube | 86K views | 1. The Grand Design to Pressure China
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
