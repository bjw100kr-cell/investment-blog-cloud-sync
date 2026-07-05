# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-05T15:56:40.897941+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-05`
- priority_score: `135.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3800`
- fallback_source: `source_snapshot_rank`
- source_count: `2`
- score_breakdown: search `24` / timeliness `25` / monetization `15`
- source_names: Federal Reserve Monetary Policy Press, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Wall St Week Ahead Investors look for Fed clues, earnings signs as tech wobbles - Reuters
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-03-18T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318a.htm
  - Federal Reserve Monetary Policy Press | 2026-05-20T18:00:00+00:00 | Minutes of the Federal Open Market Committee, April 28-29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-06`
- priority_score: `123.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `4400`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `26` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, NYT Business
- sample_headlines:
  - Barstool's Portnoy plans to hold bitcoin down to zero after timing it wrong every time
  - Bitcoin jumps above $63,000, reversing end-June losses
  - Bitcoin experts split over plan to freeze Satoshi's 1.1 million bitcoin as quantum threat grows
  - South Africa proposes crypto tax guidance under existing framework
  - Here’s what happened in crypto today
- recent_evidence:
  - CoinDesk RSS | 2026-07-05T06:00:22+00:00 | Barstool's Portnoy plans to hold bitcoin down to zero after timing it wrong every time | https://www.coindesk.com/markets/2026/07/05/barstool-s-portnoy-plans-to-hold-bitcoin-down-to-zero-after-timing-it-wrong-every-time
  - Investing.com Crypto News | 2026-07-05 09:51:59 | Bitcoin trades above $62K as U.S. crypto bill gains fresh traction | https://www.investing.com/news/cryptocurrency-news/bitcoin-trades-above-62k-as-us-crypto-bill-gains-fresh-traction-4775415
  - Investing.com Crypto News | 2026-07-05 07:02:21 | Bitcoin tests $63,100-$63,600 resistance: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-in-bear-flag-near-annual-low-live-levels-93CH-4764319
  - CoinDesk RSS | 2026-07-04T18:07:17+00:00 | Bitcoin jumps above $63,000, reversing end-June losses | https://www.coindesk.com/markets/2026/07/04/bitcoin-jumps-above-usd63-000-reversing-end-june-losses
  - CoinDesk RSS | 2026-07-04T18:00:00+00:00 | Bitcoin experts split over plan to freeze Satoshi's 1.1 million bitcoin as quantum threat grows | https://www.coindesk.com/business/2026/07/04/bitcoin-experts-split-over-plan-to-freeze-satoshi-s-1-1-million-bitcoin-as-quantum-threat-grows

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: ``
- priority_score: `83.0`
- ready_now: `False` / quality_status `needs_fix`
- reason: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `8` / timeliness `10` / monetization `15`
- source_names: Financial Times Home, MarketWatch Breaking News
- sample_headlines:
  - How Bending Spoons built a $23bn tech empire from struggling brands
  - Why the stock market’s red-hot momentum trade might be headed for a violent unwind this month
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-05T13:00:00+00:00 | Why the stock market’s red-hot momentum trade might be headed for a violent unwind this month | https://www.marketwatch.com/story/why-the-stock-markets-red-hot-momentum-trade-might-be-headed-for-a-violent-unwind-this-month-78a45397?mod=mw_rss_topstories
