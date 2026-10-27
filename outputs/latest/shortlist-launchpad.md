# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Tom Lee's Bitmine favors share buybacks to ether purchases as crypto declines
  - South Korea weighs fourth delay on its crypto gains tax, pushing it to 2029
  - A $68 million bitcoin bet is targeting a post-midterm election breakout to $90,000
- recent_evidence:
  - CoinDesk RSS | 2026-10-26T11:53:07+00:00 | A $68 million bitcoin bet is targeting a post-midterm election breakout to $90,000
  - Investing.com Crypto News | 2026-10-26 21:38:41 | Bitcoin little-changed at $80.4k as oil, rate jitters dent crypto appetite
  - Investing.com Crypto News | 2026-10-26 19:18:44 | Bitcoin nears oversold as descending triangle forms: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - AI giant Anthropic files for blockbuster IPO
  - Injective launches onchain futures market tracking Nvidia GPU rental costs
  - AI company Anthropic announces IPO, expected as early as November
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-27T01:46:00+00:00 | Asian stocks surge as Anthropic IPO lifts sentiment ahead of earnings, central banks - Reuters
  - Reuters Markets via Google News RSS | 2026-10-26T23:28:41+00:00 | Equities end higher as Anthropic's IPO filing buoys AI stocks - Reuters
  - CNBC Top News | 2026-10-26T22:50:07+00:00 | From Wall Street to Silicon Valley, Anthropic IPO poised to have massive 'trickle-down effect'
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China industrial profits post strongest growth in three months as tech boom widens economic divide
  - In China, the AI bubble has already burst - Reuters
  - TikTok parent ByteDance’s chatbot is now giving travel-booking sites a run for their money. And yours.
- recent_evidence:
  - CNBC Top News | 2026-10-27T03:34:08+00:00 | China industrial profits post strongest growth in three months as tech boom widens economic divide
  - Reuters Markets via Google News RSS | 2026-10-26T12:02:00+00:00 | In China, the AI bubble has already burst - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
