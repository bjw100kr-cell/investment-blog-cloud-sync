# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-31T03:32:23.889532+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-31`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4200`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: Federal Reserve Monetary Policy Press, Investing.com Crypto News, NYT Business
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Bitcoin seesaws as hit to risk sentiment and surging oil offsets Fed rate hold
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-08T18:00:00+00:00 | Minutes of the Federal Open Market Committee, June 16-17, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260708a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-08-01`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `6400`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Strategy books $8.2 billion Q2 loss on bitcoin price decline
  - Ondo Finance weighs acquisition worth up to $500 million
  - Crypto for Advisors: Is the Clarity Act dead?
  - JPMorgan says fading Clarity Act odds weigh on crypto outlook
  - Coldcard issues Mk3 warning as experts examine $38M Bitcoin wallet drain
- recent_evidence:
  - Cointelegraph | 2026-07-31T02:38:09+00:00 | Coldcard issues Mk3 warning as experts examine $38M Bitcoin wallet drain | https://cointelegraph.com/news/coldcard-mk3-warning-594-btc-sweep?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-07-31T00:31:21+00:00 | Bhutan’s Gelephu taps 3iQ to manage part of Bitcoin treasury | https://cointelegraph.com/news/bhutan-gelephu-3iq-bitcoin-treasury?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-07-30T21:36:39+00:00 | Strategy posts $8.2B Q2 loss as Bitcoin slump drives unrealized losses | https://cointelegraph.com/news/strategy-reports-q2-2026-loss?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-07-30T20:32:13+00:00 | Strategy books $8.2 billion Q2 loss on bitcoin price decline | https://www.coindesk.com/markets/2026/07/30/strategy-books-usd8-2-billion-second-quarter-loss-on-bitcoin-price-decline
  - Investing.com Crypto News | 2026-07-30 22:04:06 | Bitcoin caught up in broader risk asset rally; Strategy swings to quarterly loss | https://www.investing.com/news/cryptocurrency-news/bitcoin-falls-to-64k-amid-rates-iran-jitters-strategy-earnings-on-tap-4822491

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-08-02`
- priority_score: `123.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (cathie wood nvidia stock purchase)
- format: `sector_analysis`
- demand_signal_score: `5200`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `30` / timeliness `17` / monetization `15`
- trend_queries: cathie wood nvidia stock purchase
- trend_regions: US
- source_names: CNBC Top News, Financial Times Home, Financial Times YouTube, Google Trends US
- sample_headlines:
  - cathie wood nvidia stock purchase
  - SK Hynix shares surge 25%, while Samsung soars over 20% as AI rally roars back
  - Anthropic’s Claude AI models hack into 3 outside groups during testing
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 48K views | Silicon shadows: inside the black market for AI chips | FT Film | https://www.youtube.com/watch?v=kFcWmQevQo8
  - Financial Times Home | 2026-07-31T00:55:13+00:00 | Anthropic’s Claude AI models hack into 3 outside groups during testing | https://www.ft.com/content/1a841f08-8e59-49d9-9561-0ed20e9190df?syn-25a6b1a6=1
  - Google Trends US | 2026-07-30T20:00:00-07:00 | cathie wood nvidia stock purchase | https://trends.google.com/trending/rss?geo=US
