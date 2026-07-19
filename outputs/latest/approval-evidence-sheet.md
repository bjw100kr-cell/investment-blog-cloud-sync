# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-19T07:52:20.136130+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-19`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4500`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, Federal Reserve Monetary Policy Press, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Massive bitcoin call spreads target $72,000 by month end, right when the Fed meets
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-08T18:00:00+00:00 | Minutes of the Federal Open Market Committee, June 16-17, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260708a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-20`
- priority_score: `117.0`
- ready_now: `True` / quality_status `pass`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed), 실제 급상승 검색어 반영 (fidelity bitcoin)
- format: `crypto_analysis`
- demand_signal_score: `300`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `28` / timeliness `20` / monetization `15`
- trend_queries: fidelity bitcoin
- trend_regions: US
- source_names: CoinDesk RSS, Cointelegraph, Google Trends US, Investing.com Crypto News
- sample_headlines:
  - fidelity bitcoin
  - Crypto executives say digital native generations may never need a bank account
  - DOG Mode explains Bitcoin's next governance fight
  - Trump targets Brazil's payments system while dollar stablecoins are quietly overtaking country's payments
  - Here is why a massive $1.6 billion in crypto liquidity is sitting idle and wasting away
- recent_evidence:
  - Investing.com Crypto News | 2026-07-19 07:01:40 | Bitcoin stuck in tight range below $65,600: Hourly levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-trapped-at-supertrend-support-hourly-levels-93CH-4787508
  - Google Trends US | 2026-07-18T23:40:00-07:00 | fidelity bitcoin | https://trends.google.com/trending/rss?geo=US
  - CoinDesk RSS | 2026-07-18T17:00:00+00:00 | DOG Mode explains Bitcoin's next governance fight | https://www.coindesk.com/tech/2026/07/18/dog-mode-explains-bitcoin-s-next-governance-fight
  - CoinDesk RSS | 2026-07-18T14:15:15+00:00 | Massive bitcoin call spreads target $72,000 by month end, right when the Fed meets | https://www.coindesk.com/markets/2026/07/18/massive-bitcoin-call-spreads-target-usd72-000-by-month-end-right-when-the-fed-meets
  - Investing.com Crypto News | 2026-07-18 21:30:15 | Bitcoin recovers toward $65k after sliding on AI shock, crypto bill doubts | https://www.investing.com/news/cryptocurrency-news/bitcoin-rebounds-toward-64000-as-ai-shock-and-crypto-bill-doubts-weigh-4799577

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-07-21`
- priority_score: `106.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (stock market today)
- format: `sector_analysis`
- demand_signal_score: `2200`
- fallback_source: `trend_match`
- source_count: `1`
- score_breakdown: search `25` / timeliness `5` / monetization `15`
- trend_queries: stock market today
- trend_regions: US
- source_names: Google Trends US
- sample_headlines:
  - stock market today
- recent_evidence:
  - Google Trends US | 2026-07-18T23:30:00-07:00 | stock market today | https://trends.google.com/trending/rss?geo=US
