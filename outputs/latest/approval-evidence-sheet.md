# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-10-10T05:21:48.776743+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-10-10`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4000`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Federal Reserve Monetary Policy Press, Investing.com Crypto News, NYT Business
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Trump created a committee to dig into the Fed's Lisa Cook. What is it and what comes next?
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-10-07T18:00:00+00:00 | Minutes of the Federal Open Market Committee, September 15-16, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-10-11`
- priority_score: `121.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `5000`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `28` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - New York AG secures up to $35 million and lifetime crypto ban from Celsius’ Alex Mashinsky
  - Ledger investigates potential wallet tampering after reports of $86 million in crypto stolen
  - US plans to seize $1B in crypto linked to Iran this week: Scott Bessent
  - New York permanently bars Celsius founder Mashinsky in $35M fraud settlement
  - Here’s what happened in crypto today
- recent_evidence:
  - Investing.com Crypto News | 2026-10-10 03:59:57 | Bitcoin trades above $82,000 as rising oil prices, Fed outlook weigh | https://www.investing.com/news/cryptocurrency-news/bitcoin-slips-toward-82000-as-rising-oil-prices-fed-outlook-weigh-4941955
  - Investing.com Crypto News | 2026-10-09 20:46:24 | Bitcoin holds ground above $82k, heads for weekly losses amid yield pressure | https://www.investing.com/news/cryptocurrency-news/bitcoin-falls-to-82k-heads-for-weekly-losses-amid-yield-pressure-4940276
  - Investing.com Crypto News | 2026-10-09 19:18:52 | Bitcoin clings to $81,121 macro support on 5h chart: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-tests-87363-resistance-with-fading-momentum-live-levels-93CH-4931135
  - Investing.com Crypto News | 2026-10-08 21:56:08 | Bitcoin slips under $82k amid surging oil prices, hit to Wall Street tech stocks | https://www.investing.com/news/cryptocurrency-news/bitcoin-falls-below-83k-as-meast-tensions-soaring-yields-dent-crypto-appetite-4937967
  - Cointelegraph | 2026-10-09T20:39:17+00:00 | US plans to seize $1B in crypto linked to Iran this week: Scott Bessent | https://cointelegraph.com/news/scott-bessent-us-seize-crypto-iran-sanctions?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-10-12`
- priority_score: `95.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `3`
- score_breakdown: search `12` / timeliness `15` / monetization `15`
- source_names: Financial Times Home, Financial Times World, MarketWatch Breaking News
- sample_headlines:
  - The hazy OpenAI growth metric driving Wall Street
  - How to provide guaranteed retirement income while paying no commissions
