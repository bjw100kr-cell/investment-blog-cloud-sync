# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Europe’s top regulator questions Polymarket and Kalshi’s EU access, warns of authorization gaps
  - Bitcoin Bancorp snaps up thousands of defunct Bitcoin Depot ATMs for $620,000
  - Crypto for Advisors: Hyperliquid and the future of finance
- recent_evidence:
  - CoinDesk RSS | 2026-09-10T15:14:49+00:00 | Bitcoin Bancorp snaps up thousands of defunct Bitcoin Depot ATMs for $620,000
  - Cointelegraph | 2026-09-10T14:52:15+00:00 | Bitcoin falls on US PPI overshoot as 30-year bond yield hits new 19-year high
  - Investing.com Crypto News | 2026-09-10 21:43:48 | Bitcoin dips to $77.1k as PPI data boosts Fed rate hike bets, oil prices jump
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-13` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OKX brings OpenAI and Anthropic bets to Europe as pre-IPO trading grows
  - Chinese AI labs secretly used millions of Claude exchanges to train their models, Anthropic says
  - Chinese Nvidia rival Enflame soars 206% on stock market debut as AI demand stays hot
- recent_evidence:
  - Financial Times YouTube | 60K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-09-11T01:53:08+00:00 | Chinese Nvidia rival Enflame soars 206% on stock market debut as AI demand stays hot
  - CNBC Top News | 2026-09-11T00:59:45+00:00 | Chinese AI labs secretly used millions of Claude exchanges to train their models, Anthropic says
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-14` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Chinese AI labs secretly used millions of Claude exchanges to train their models, Anthropic says
  - Chinese Nvidia rival Enflame soars 206% on stock market debut as AI demand stays hot
  - China-Philippines tensions simmer after Beijing rebukes Manila over Seoul clash
- recent_evidence:
  - 무역킹 Trade King YouTube | 63K views | Has China Finally Responded to the U.S. Lawsuit???
  - CNBC Top News | 2026-09-11T03:44:43+00:00 | China-Philippines tensions simmer after Beijing rebukes Manila over Seoul clash
  - Financial Times World | 2026-09-11T03:17:24+00:00 | How China is extending its long arm abroad
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
