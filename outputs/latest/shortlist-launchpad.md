# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - XRP, HYPE funds are the bright spots as investors flee bitcoin, ether ETFs
  - Bitcoin options traders load up on $50,000 puts and gold futures flash a death cross
  - Bitcoin’s 20% June crash looks even deadlier on the charts. Here’s why
- recent_evidence:
  - CoinDesk RSS | 2026-07-01T11:15:00+00:00 | XRP, HYPE funds are the bright spots as investors flee bitcoin, ether ETFs
  - CoinDesk RSS | 2026-07-01T10:47:34+00:00 | Bitcoin options traders load up on $50,000 puts and gold futures flash a death cross
  - Cointelegraph | 2026-07-01T09:22:09+00:00 | Bitcoin ETFs lose record $4.5B in June, eclipsing Strategy's $1.25B raise
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic restores AI models Fable, Mythos after the U.S. lifts export controls
  - Anthropic to bring back Fable 5 as US lifts export controls
  - Anthropic says Trump admin has lifted export controls on Claude Fable 5 and Mythos 5
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-01T11:08:00+00:00 | Why it’s too early to call a top on semiconductor stocks, according to these highly regarded analysts
  - CNBC Top News | 2026-07-01T10:19:57+00:00 | Anthropic says Trump admin has lifted export controls on Claude Fable 5 and Mythos 5
  - MarketWatch Breaking News | 2026-07-01T09:44:00+00:00 | Anthropic gets all-clear to let foreigners use latest model ahead of crucial IPO
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bulls are betting big on this global ETF that's deep in a bear market
  - Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund
  - 1. The Grand Design to Pressure China
- recent_evidence:
  - 무역킹 Trade King YouTube | 90K views | 1. The Grand Design to Pressure China
  - Financial Times World | 2026-07-01T11:00:06+00:00 | How China’s green tech could boost its global finance ambitions
  - CNBC Top News | 2026-06-30T22:07:27+00:00 | Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
