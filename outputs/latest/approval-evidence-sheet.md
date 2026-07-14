# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-14T07:25:45.012734+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-15`
- priority_score: `125.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `7600`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `30` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Live updates: Bitcoin holds $62,600 as the Iran conflict reignites and CPI looms
  - U.S. government moves $288 million in seized bitcoin, ether to Coinbase Prime
  - Solo bitcoin miner makes $200,000 using $150 equipment
  - Bitcoin slips as traders lift July Fed rate hike bets ahead of Inflation report
  - Franklin Crypto CIO says crypto prices are disconnected from fundamentals
- recent_evidence:
  - CoinDesk RSS | 2026-07-14T06:55:24+00:00 | Live updates: Bitcoin holds $62,600 as the Iran conflict reignites and CPI looms | https://www.coindesk.com/business/2026/07/14/live-updates-bitcoin-holds-usd62-600-as-the-iran-conflict-reignites-and-cpi-looms
  - CoinDesk RSS | 2026-07-14T06:28:43+00:00 | U.S. government moves $288 million in seized bitcoin, ether to Coinbase Prime | https://www.coindesk.com/markets/2026/07/14/u-s-government-moves-usd288-million-in-seized-bitcoin-ether-to-coinbase-prime
  - CoinDesk RSS | 2026-07-14T04:43:56+00:00 | Solo bitcoin miner makes $200,000 using $150 equipment | https://www.coindesk.com/markets/2026/07/14/solo-btc-miner-makes-usd200-000-using-usd150-equipment
  - Cointelegraph | 2026-07-14T03:35:51+00:00 | US government moves $297M in seized Bitcoin, Ether to Coinbase Prime | https://cointelegraph.com/news/us-government-moves-297m-in-seized-bitcoin-ether-to-coinbase-prime?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-07-14T02:58:36+00:00 | Bitcoin slips as traders lift July Fed rate hike bets ahead of Inflation report | https://www.coindesk.com/markets/2026/07/14/bitcoin-slips-as-traders-lift-july-fed-rate-hike-bets-ahead-of-inflation-report

## 2. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-14`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4100`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: CoinDesk RSS, Federal Reserve Monetary Policy Press, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Bitcoin slips as traders lift July Fed rate hike bets ahead of Inflation report
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-08T18:00:00+00:00 | Minutes of the Federal Open Market Committee, June 16-17, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260708a.htm

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-07-16`
- priority_score: `114.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (stock market news today)
- format: `sector_analysis`
- demand_signal_score: `2200`
- fallback_source: `trend_match`
- source_count: `2`
- score_breakdown: search `27` / timeliness `10` / monetization `15`
- trend_queries: stock market news today
- trend_regions: US
- source_names: Google Trends US, MarketWatch Breaking News
- sample_headlines:
  - stock market news today
  - Why a borrowing binge by investors is a warning sign for the stock market
- recent_evidence:
  - Google Trends US | 2026-07-13T22:50:00-07:00 | stock market news today | https://trends.google.com/trending/rss?geo=US
  - MarketWatch Breaking News | 2026-07-13T22:19:00+00:00 | Why a borrowing binge by investors is a warning sign for the stock market | https://www.marketwatch.com/story/why-a-borrowing-binge-by-investors-is-a-warning-sign-for-the-stock-market-996ee446?mod=mw_rss_topstories
