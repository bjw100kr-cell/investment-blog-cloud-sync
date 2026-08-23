# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-08-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto's week in 5 stories
  - How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
  - Bitcoin rally sends crypto stocks soaring as miners, treasury companies jump
- recent_evidence:
  - MarketWatch Breaking News | 2026-08-23T12:00:00+00:00 | The Treasury’s bond-market intervention isn’t working. So what comes next?
  - CoinDesk RSS | 2026-08-22T05:05:13+00:00 | How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
  - Investing.com Crypto News | 2026-08-22 10:01:31 | Bitcoin holds above $77,000 after Treasury-fuelled short squeeze
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto exchange BitMart weighs partial restart and creditor payouts weeks after announcing shutdown
  - Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto's week in 5 stories
  - Zcash jumps 48% to over $800 as Grayscale spot ETF push adds to ‘next bitcoin’ buzz
- recent_evidence:
  - Investing.com Crypto News | 2026-08-23 09:58:05 | Bitcoin slips under $77,000 as rally boosts mining economics
  - Investing.com Crypto News | 2026-08-23 07:02:36 | Bitcoin surges past $76K with overbought RSI: Live levels
  - CoinDesk RSS | 2026-08-22T12:00:00+00:00 | Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto's week in 5 stories
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-08-25` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (apple tv)
- sample_headlines:
  - apple tv
  - Trump reshuffled his portfolio in June, selling names like Meta and buying Berkshire Hathaway
  - How Big Tech Captured American Schools
- recent_evidence:
  - Google Trends US | 2026-08-23T05:40:00-07:00 | apple tv
  - CNBC Top News | 2026-08-22T18:57:46+00:00 | Trump reshuffled his portfolio in June, selling names like Meta and buying Berkshire Hathaway
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
