# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-28T14:27:56.527061+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-29`
- priority_score: `126.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- format: `crypto_analysis`
- demand_signal_score: `6800`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, NYT Business
- sample_headlines:
  - Core Scientific lands AMD AI deal as bitcoin mining operation winds down
  - Binance makes fighting crypto crime more difficult, says new report
  - Apple kept fake bitcoin wallet on App Store after $875,000 theft report, lawsuit alleges
  - Bitcoin’s recent stability hasn't been enough to spark a broader altcoin rally
  - Bitcoin drops as South Korean stocks tumble, Senate shelves crypto Clarity Act
- recent_evidence:
  - CoinDesk RSS | 2026-07-28T12:46:05+00:00 | Core Scientific lands AMD AI deal as bitcoin mining operation winds down | https://www.coindesk.com/business/2026/07/28/core-scientific-lands-amd-ai-deal-as-bitcoin-mining-operation-winds-down
  - CoinDesk RSS | 2026-07-28T11:59:17+00:00 | Apple kept fake bitcoin wallet on App Store after $875,000 theft report, lawsuit alleges | https://www.coindesk.com/business/2026/07/28/apple-kept-fake-bitcoin-wallet-on-app-store-after-usd875-000-theft-report-lawsuit-alleges
  - CoinDesk RSS | 2026-07-28T11:37:31+00:00 | Bitcoin’s recent stability hasn't been enough to spark a broader altcoin rally | https://www.coindesk.com/daybook-us/2026/07/28/bitcoin-s-recent-stability-hasn-t-been-enough-to-spark-a-broader-altcoin-rally
  - CoinDesk RSS | 2026-07-28T11:09:16+00:00 | Bitcoin drops as South Korean stocks tumble, Senate shelves crypto Clarity Act | https://www.coindesk.com/markets/2026/07/28/bitcoin-drops-as-south-korean-stocks-tumble-senate-shelves-crypto-clarity-act
  - Investing.com Crypto News | 2026-07-28 13:25:47 | Is the Bitcoin bottom in? Key levels to watch after summer drop | https://www.investing.com/news/cryptocurrency-news/is-the-bitcoin-bottom-in-key-levels-to-watch-after-summer-drop-93CH-4816979

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-07-31`
- priority_score: `83.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `8` / timeliness `13` / monetization `13`
- source_names: MarketWatch Breaking News, NYT Business
- sample_headlines:
  - Micron’s stock sinks toward worst monthly drop in 11 years as China fears escalate
  - Tech Stocks Tumble on Worries About A.I. Spending and China’s Chip Competition
  - He Served China’s Police State of Xinjiang. He Says It Imprisoned Him, Too.
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-28T14:25:00+00:00 | Micron’s stock sinks toward worst monthly drop in 11 years as China fears escalate | https://www.marketwatch.com/story/microns-stock-sinks-toward-worst-monthly-drop-in-11-years-as-china-fears-escalate-3c956a67?mod=mw_rss_topstories
  - NYT Business | 2026-07-28T14:21:14+00:00 | Tech Stocks Tumble on Worries About A.I. Spending and China’s Chip Competition | https://www.nytimes.com/2026/07/28/business/stocks-ai-chips.html
  - NYT Business | 2026-07-28T04:01:20+00:00 | He Served China’s Police State of Xinjiang. He Says It Imprisoned Him, Too. | https://www.nytimes.com/2026/07/28/business/china-uyghurs.html

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-07-30`
- priority_score: `127.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (stock market)
- format: `sector_analysis`
- demand_signal_score: `5200`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `30` / timeliness `20` / monetization `15`
- trend_queries: stock market
- trend_regions: US
- source_names: Financial Times Home, Financial Times World, Google Trends US, Reuters Markets via Google News RSS
- sample_headlines:
  - stock market
  - US tech stocks enter correction as AI sell-off deepens
  - Nasdaq opens lower as AI worries mount ahead of pivotal earnings - Reuters
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-07-28T13:33:44+00:00 | Nasdaq opens lower as AI worries mount ahead of pivotal earnings - Reuters | https://news.google.com/rss/articles/CBMipgFBVV95cUxPNkhJQS14Y3d3QkMxeG5XZmR3cldUel9CSk9pdDZrSDFkc0gydEgxSXQ1d0xzTi1OR29xVWEwUjJtV1k4V1p3WlZJeUZCbnB2MzJOYjBHRExWTmVobWlibGFqajlUcWx5emx2M01vYmNwcHlDM2FvYjRwU3o2M0szNVpyM3JwakJyRkZReUMyVk5GUklTWWczOXdFSUcwNkh1clFNVWJn?oc=5
  - Google Trends US | 2026-07-28T07:10:00-07:00 | stock market | https://trends.google.com/trending/rss?geo=US
