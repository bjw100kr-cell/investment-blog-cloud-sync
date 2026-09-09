# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-09-09T16:27:30.816192+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-09-09`
- priority_score: `139.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `5100`
- fallback_source: `source_snapshot_rank`
- source_count: `5`
- score_breakdown: search `28` / timeliness `25` / monetization `15`
- source_names: Federal Reserve Monetary Policy Press, Financial Times Home, Investing.com Crypto News, MarketWatch Breaking News, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Bitcoin recovers to $79.4k on Zcash ETF inflows; Fed, oil pressures limit rise
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-09-10`
- priority_score: `121.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `5100`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `28` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - U.S. Treasury sanctions another widespread cyber-scam hub, Xinbi Guarantee
  - Bitcoin and Ethereum race quantum clock as U.S. backs $300 million hardware push
  - Crypto Long & Short: Inside the 300-to-1 onchain gap between the dollar and euro
  - Trade groups seek to block Illinois crypto tax before January effective date
  - German finance ministry proposes 25% crypto tax starting 2028: Report
- recent_evidence:
  - CoinDesk RSS | 2026-09-09T15:30:00+00:00 | Bitcoin and Ethereum race quantum clock as U.S. backs $300 million hardware push | https://www.coindesk.com/tech/2026/09/09/bitcoin-and-ethereum-race-quantum-clock-as-u-s-backs-usd300-million-hardware-push
  - Investing.com Crypto News | 2026-09-09 13:48:40 | Bitcoin recovers to $79.4k on Zcash ETF inflows; Fed, oil pressures limit rise | https://www.investing.com/news/cryptocurrency-news/bitcoin-rebounds-above-79k-on-zcash-etf-inflows-fed-oil-pressures-limit-rise-4892730
  - Investing.com Crypto News | 2026-09-09 07:10:45 | Bitcoin coils near $79,300 in tight range: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-trapped-in-775k822k-range-live-levels-93CH-4890481
  - Investing.com Crypto News | 2026-09-08 20:54:31 | Bitcoin falls nearly 1% as Fed rate hike bets remain elevated, oil prices rise | https://www.investing.com/news/cryptocurrency-news/bitcoin-slips-toward-78k-as-as-fed-oil-pressures-mount-4890858
  - Investing.com Crypto News | 2026-09-07 13:47:35 | Bitcoin slips below $80k as Fed hike bets, oil surge weigh | https://www.investing.com/news/cryptocurrency-news/bitcoin-slips-below-80k-as-fed-hike-bets-oil-surge-weigh-4890363

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-09-11`
- priority_score: `105.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (apple)
- format: `sector_analysis`
- demand_signal_score: `700`
- fallback_source: `trend_match`
- source_count: `3`
- score_breakdown: search `22` / timeliness `15` / monetization `15`
- trend_queries: apple
- trend_regions: KR
- source_names: Financial Times World, Google Trends KR, Reuters Markets via Google News RSS
- sample_headlines:
  - apple
  - Amazon raises almost $6 billion in first sterling bond sale, lead manager says - Reuters
  - New Apple CEO to unveil $2,000 folding iPhone
- recent_evidence:
  - Google Trends KR | 2026-09-09T07:20:00-07:00 | apple | https://trends.google.com/trending/rss?geo=KR
  - Reuters Markets via Google News RSS | 2026-09-09T15:46:55+00:00 | Amazon raises almost $6 billion in first sterling bond sale, lead manager says - Reuters | https://news.google.com/rss/articles/CBMiswFBVV95cUxOdlZhMHZ0RkVhaWNCVWdOa3N1aXVYdXJ1LS1tUTFFWU5hMlJYYTJaQkQ3SWc5RGhMcklmZkxrQlNZV0ozd1lnWTdZbjFVT1hYYzFRTkJYZVZiTEFNRjBlNWkxVGprb29nRnVEeHBlZ3dkVl9HdkNhcUg1bjBpYlo0dFVDbTl4YXA2MEllSXo5bS16N3lzYUh0TThldUJhci1jYTJiWXFOdU1teDAxZmVhbTRBOA?oc=5
  - Financial Times World | 2026-09-09T15:43:32+00:00 | New Apple CEO to unveil $2,000 folding iPhone | https://www.ft.com/content/dea481e8-d30b-4cbb-b535-5ff219c4e546?syn-25a6b1a6=1
  - CoinDesk RSS | 2026-09-09T15:24:01+00:00 | Consensys to split MetaMask into its own firm while staying silent on IPO | https://www.coindesk.com/business/2026/09/09/consensys-to-split-metamask-into-its-own-firm-while-staying-silent-on-ipo
