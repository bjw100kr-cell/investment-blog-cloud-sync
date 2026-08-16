# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - The 'long bitcoin, short the bankers' era is officially over as TradFi giants embrace digital assets
  - Swiss mega-bank UBS ramps up its Bitcoin exposure with a massive 24-fold surge in ETF call options
  - Why the world’s second-largest Bitcoin mining power is shutting down rigs in its capital city
- recent_evidence:
  - CoinDesk RSS | 2026-08-16T12:00:00+00:00 | The 'long bitcoin, short the bankers' era is officially over as TradFi giants embrace digital assets
  - Investing.com Crypto News | 2026-08-16 09:22:42 | Bitcoin price trades above $63,000 as Saylor calls it ‘digital monetary energy’
  - Investing.com Crypto News | 2026-08-16 07:02:04 | Bitcoin trapped in $62,500-$64,000 chop zone: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. CPI 발표 후 금리와 나스닥, 비트코인이 같이 움직이는 이유

- keyword `cpi` / publish `2026-08-16` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Gold rises on weaker dollar as inflation data cements rate-hold bets - Reuters
  - Walmart and Target are about to reveal the health of the U.S. consumer
  - Worker Pay Isn’t Keeping Up With Inflation Once Again
- recent_evidence:
  - NYT Business | 2026-08-15T09:02:16+00:00 | Worker Pay Isn’t Keeping Up With Inflation Once Again
  - Reuters Markets via Google News RSS | 2026-08-14T18:09:39+00:00 | Gold rises on weaker dollar as inflation data cements rate-hold bets - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords cpi`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords cpi`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword cpi`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword cpi --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-08-18` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Secret outperformer: Dispelling the 'myths' about an unloved stock market
  - S&P 500 ends lower as investors weigh data, Middle East tensions - Reuters
  - An active fund holding a whopping 800 stocks is beating major indexes. Here’s how.
- recent_evidence:
  - CNBC Top News | 2026-08-16T09:45:45+00:00 | Secret outperformer: Dispelling the 'myths' about an unloved stock market
  - Reuters Markets via Google News RSS | 2026-08-14T22:57:49+00:00 | S&P 500 ends lower as investors weigh data, Middle East tensions - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
