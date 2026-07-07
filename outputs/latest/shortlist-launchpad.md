# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin stalls as open interest decline raises questions about rally's staying power
  - Binance taps into Bitcoin holders’ hunger for yield with new covered call yield play
  - Bitcoin's recent macro relief faces a challenge from Japanese interest rates
- recent_evidence:
  - CoinDesk RSS | 2026-07-07T10:44:09+00:00 | Bitcoin stalls as open interest decline raises questions about rally's staying power
  - Cointelegraph | 2026-07-07T10:14:40+00:00 | Bitcoin can fall below $58K if one of its 'cleanest' metrics copies history: Analysis
  - Cointelegraph | 2026-07-07T09:23:39+00:00 | Digital Chamber amicus brief urges dismissal of NY lawsuit over 39,069 Bitcoin wallets
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-10` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China breaks step with global markets, and investors buy in - Reuters
  - China's booming gig economy masks job market pain, strains welfare system - Reuters
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-07-07T01:10:00+00:00 | China breaks step with global markets, and investors buy in - Reuters
  - Reuters Markets via Google News RSS | 2026-07-06T23:03:00+00:00 | China's booming gig economy masks job market pain, strains welfare system - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담

- keyword `ai_growth_stocks` / publish `2026-07-09` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Palantir Is Moving the Japanese Military
- recent_evidence:
  - 무역킹 Trade King YouTube | 38K | Palantir Is Moving the Japanese Military
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks --apply`
