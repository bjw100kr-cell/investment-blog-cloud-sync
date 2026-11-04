# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-05` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - U.S.-sanctioned Moscow Exchange to list bitcoin and Tether’s USDT in December
  - South Korea's ruling party wants to delay its crypto tax again
  - Democrats surge toward Senate, House majorities, with crypto braced for new direction
- recent_evidence:
  - CoinDesk RSS | 2026-11-04T05:14:12+00:00 | U.S.-sanctioned Moscow Exchange to list bitcoin and Tether’s USDT in December
  - CoinDesk RSS | 2026-11-04T04:48:16+00:00 | Bitcoin briefly sinks to $75,700 as bets on a Democratic sweep rattle markets
  - Investing.com Crypto News | 2026-11-03 23:10:20 | Bitcoin rises as risk sentiment prevails on Wall Street; midterm elections eyed
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-11-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Stock market after midterm elections: What S&P 500 history shows
  - Nasdaq ends higher as AI heavyweights rebound ahead of midterm results - Reuters
  - S&P 500 is looking over the edge of a technical cliff — what happens if it falls off?
- recent_evidence:
  - NYT Business | 2026-11-04T05:41:50+00:00 | How the Stock Market Is Reacting to the Midterm Elections
  - MarketWatch Breaking News | 2026-11-03T21:30:00+00:00 | S&P 500 is looking over the edge of a technical cliff — what happens if it falls off?
  - CNBC Top News | 2026-11-03T18:21:05+00:00 | Stock market after midterm elections: What S&P 500 history shows
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `` / verdict `approve` / quality `needs_fix`
- ready_now: `False` / hero_image_selected: `True`
- intent: 
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - AMD stock jumps 8% on earnings as data center revenue nearly doubles
  - AI Revenue Up 78% But Stock Crashes: Understanding the Semiconductor Cycle Through the Intel Cris...
  - Here’s why AMD’s stock is rising — and sending a confident message about the AI trade
- recent_evidence:
  - 무역킹 Trade King YouTube | 무역킹 Trade King | AI Revenue Up 78% But Stock Crashes: Understanding the Semiconductor Cycle Through the Intel Cris...
  - MarketWatch Breaking News | 2026-11-04T01:16:00+00:00 | Here’s why AMD’s stock is rising — and sending a confident message about the AI trade
  - NYT Business | 2026-11-03T23:39:55+00:00 | OpenAI and Anthropic Set Up ‘War Rooms’ to Fight Disinfo About Midterm Elections
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
