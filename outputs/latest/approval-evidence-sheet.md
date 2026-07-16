# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-16T07:38:10.147439+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-16`
- priority_score: `135.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3800`
- fallback_source: `source_snapshot_rank`
- source_count: `2`
- score_breakdown: search `24` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Federal Reserve Monetary Policy Press
- sample_headlines:
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Fed Chairman Warsh says he meets 'often' with Trump administration, defends independence
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-08T18:00:00+00:00 | Minutes of the Federal Open Market Committee, June 16-17, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260708a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-17`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `6600`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Live updates: ZachXBT calls hardware wallets complete garbage; BTC steady after Korea rate hike
  - U.S. Senate unanimously opposes clemency for FTX founder Sam Bankman-Fried
  - A bitcoin wallet dormant since the 2017 peak just moved $383 million
  - Ether outruns bitcoin as ETF money returns, almost all of from BlackRock's fund
  - Two groups of bitcoin investors sell on the rise as U.S. inflation lifts prices to nearly $65,000
- recent_evidence:
  - CoinDesk RSS | 2026-07-16T05:12:26+00:00 | A bitcoin wallet dormant since the 2017 peak just moved $383 million | https://www.coindesk.com/markets/2026/07/16/a-bitcoin-wallet-dormant-since-the-2017-peak-just-moved-usd383-million
  - CoinDesk RSS | 2026-07-16T04:56:15+00:00 | Ether outruns bitcoin as ETF money returns, almost all of from BlackRock's fund | https://www.coindesk.com/markets/2026/07/16/ether-outruns-bitcoin-as-etf-money-returns-almost-all-of-from-blackrock-s-fund
  - CoinDesk RSS | 2026-07-16T04:09:10+00:00 | Two groups of bitcoin investors sell on the rise as U.S. inflation lifts prices to nearly $65,000 | https://www.coindesk.com/markets/2026/07/16/two-groups-of-bitcoin-investors-sell-on-the-rise-as-inflation-lifts-prices-to-nearly-usd65-000
  - Investing.com Crypto News | 2026-07-16 07:04:55 | Bitcoin tests $65,500 resistance as volume fades: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-trapped-at-supertrend-support-hourly-levels-93CH-4787508
  - Investing.com Crypto News | 2026-07-16 05:48:10 | Bitcoin steady at $64.5k as markets parse cooling rate jitters, Iran tensions | https://www.investing.com/news/cryptocurrency-news/bitcoin-steady-at-645k-as-markets-parse-cooling-rate-jitters-iran-tensions-4794658

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-07-18`
- priority_score: `120.0`
- ready_now: `True` / quality_status `pass`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (tsmc stock)
- format: `sector_analysis`
- demand_signal_score: `1200`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `28` / timeliness `20` / monetization `15`
- trend_queries: tsmc stock
- trend_regions: US
- source_names: CNBC Top News, Financial Times YouTube, Google Trends US, Reuters Markets via Google News RSS
- sample_headlines:
  - tsmc stock
  - TSMC second-quarter profit jumps over 77%, beating estimates, on high-end chip boom
  - SK Hynix shares plunge over 11% as Asia sees tech rout, tracking U.S. chip losses
  - TSMC posts 77% profit jump for Q2, surging past market expectations - Reuters
  - ASML capacity upgrade soothes AI chip bottleneck fears - Reuters
- recent_evidence:
  - Financial Times YouTube | 30K views | Silicon shadows: inside the black market for AI chips | FT Film | https://www.youtube.com/watch?v=kFcWmQevQo8
  - CNBC Top News | 2026-07-16T07:02:36+00:00 | SK Hynix shares plunge over 11% as Asia sees tech rout, tracking U.S. chip losses | https://www.cnbc.com/2026/07/16/sk-hynix-falls-amid-asia-tech-rout-tracking-us-semiconductor-losses.html
  - CNBC Top News | 2026-07-16T05:52:58+00:00 | TSMC second-quarter profit jumps over 77%, beating estimates, on high-end chip boom | https://www.cnbc.com/2026/07/16/tsmc-second-quarter-profit-.html
  - Reuters Markets via Google News RSS | 2026-07-16T02:09:00+00:00 | Asian shares fall on chipmaker drag, bonds cheer cooler inflation - Reuters | https://news.google.com/rss/articles/CBMigwFBVV95cUxONzEtUE5IX0ZhajhxclVEalRCODR4QWpsVTNmWHFYZkpvXy1jTy10ZGJmVEZ4SVFKT1BkSkF2OTdzTXd6WE1tWk5OMEV2ajVLOGhnaUlER3pKbnZ5SHhSdGcxSG83RTVIckFaOUp6Z0x2T1FKUGo2M0V6YzhQRnFOLTlRcw?oc=5
  - Google Trends US | 2026-07-15T23:10:00-07:00 | tsmc stock | https://trends.google.com/trending/rss?geo=US
