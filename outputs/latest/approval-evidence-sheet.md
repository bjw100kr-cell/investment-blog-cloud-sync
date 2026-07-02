# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-02T18:18:35.736575+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-02`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4600`
- fallback_source: `source_snapshot_rank`
- source_count: `5`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Federal Reserve Monetary Policy Press, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - U.S. payroll growth slowed sharply in June, with only 57,000 jobs added
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-03-18T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318a.htm
  - Federal Reserve Monetary Policy Press | 2026-05-20T18:00:00+00:00 | Minutes of the Federal Open Market Committee, April 28-29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-03`
- priority_score: `127.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `5200`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `28` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, MarketWatch Breaking News
- sample_headlines:
  - Bitwise says STRC selloff signals crypto cycle nearing a bottom, not Strategy’s breaking point
  - US Treasury sanctions over 100 ISIS-K crypto addresses that moved over $1.4 million
  - SBI Crypto to shut down mining pool that holds roughly 2% of Bitcoin's hashrate
  - JPMorgan says Strategy's bitcoin sales policy adds 'two-way risk' to crypto markets
  - A struggling Nasdaq-listed company that tried to copy Saylor's Bitcoin playbook is completely dumping crypto for AI
- recent_evidence:
  - Cointelegraph | 2026-07-02T17:41:26+00:00 | Bitcoin price taps new July high above $62K on weak US jobs data | https://cointelegraph.com/markets/bitcoin-returns-to-62k?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-07-02T14:44:55+00:00 | SBI Crypto to shut down mining pool that holds roughly 2% of Bitcoin's hashrate | https://www.coindesk.com/business/2026/07/02/sbi-crypto-to-shut-down-mining-pool-that-holds-roughly-2-of-bitcoin-s-hashrate
  - CoinDesk RSS | 2026-07-02T13:11:22+00:00 | JPMorgan says Strategy's bitcoin sales policy adds 'two-way risk' to crypto markets | https://www.coindesk.com/markets/2026/07/02/jpmorgan-says-strategy-s-bitcoin-sales-policy-adds-two-way-risk-to-crypto-markets
  - CoinDesk RSS | 2026-07-02T12:10:15+00:00 | A struggling Nasdaq-listed company that tried to copy Saylor's Bitcoin playbook is completely dumping crypto for AI | https://www.coindesk.com/markets/2026/07/02/a-struggling-nasdaq-listed-company-that-tried-to-copy-saylor-s-bitcoin-playbook-is-completely-dumping-crypto-for-ai
  - Investing.com Crypto News | 2026-07-02 18:02:24 | Strategy’s bitcoin trading policy creates risks for broader markets, says JPMorgan | https://www.investing.com/news/cryptocurrency-news/strategys-bitcoin-trading-policy-creates-risks-for-broader-markets-says-jpmorgan-4773820

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: ``
- priority_score: `103.0`
- ready_now: `False` / quality_status `needs_fix`
- reason: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `2200`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `15` / timeliness `18` / monetization `15`
- source_names: CNBC Top News, MarketWatch Breaking News, NYT Business
- sample_headlines:
  - Tesla stock sinks 7% despite strong deliveries report
  - Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit
  - Why Tesla’s stock is sinking toward its worst day in a year despite blowout delivery numbers
  - Tesla Sales Surge 25% on Recovery in Europe
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-02T17:44:00+00:00 | Why Tesla’s stock is sinking toward its worst day in a year despite blowout delivery numbers | https://www.marketwatch.com/story/tesla-crushes-delivery-estimates-giving-its-stock-a-boost-16c198da?mod=mw_rss_topstories
  - CNBC Top News | 2026-07-02T15:40:29+00:00 | Tesla stock sinks 7% despite strong deliveries report | https://www.cnbc.com/2026/07/02/tesla-tsla-q2-2026-vehicle-delivery-production.html
  - NYT Business | 2026-07-02T15:07:48+00:00 | Tesla Sales Surge 25% on Recovery in Europe | https://www.nytimes.com/2026/07/02/business/tesla-electric-vehicle-auto-sales.html
  - CNBC Top News | 2026-07-02T13:00:02+00:00 | Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit | https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html
