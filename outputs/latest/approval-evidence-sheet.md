# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-10-23T04:16:19.640745+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-10-24`
- priority_score: `122.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `6700`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Bitcoin, gold trim early losses as yen gives up gains. Oil stays near $100
  - Senate's top Democratic investigator looking into Tether payments to Bo Hines' firm
  - A16z is the latest VC giant to widen bets beyond crypto and into AI and emerging tech
  - Crypto for Advisors: Stablecoins are ready for prime time
  - Crypto custody specialist Fireblocks denies it's in talks to be acquired by Visa
- recent_evidence:
  - CoinDesk RSS | 2026-10-23T03:13:01+00:00 | Bitcoin, gold trim early losses as yen gives up gains. Oil stays near $100 | https://www.coindesk.com/markets/2026/10/23/bitcoin-gold-trim-early-losses-as-yen-gives-up-gains-oil-stays-near-usd100
  - Cointelegraph | 2026-10-23T00:59:35+00:00 | Switzerland approves first spot Bitcoin ETF for retail investors | https://cointelegraph.com/news/switzerland-approves-first-spot-bitcoin-etf-for-retail-investors?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Investing.com Crypto News | 2026-10-22 21:41:46 | Bitcoin dives 4%, slides below $82k as AI rout, oil surge slams risk sentiment | https://www.investing.com/news/cryptocurrency-news/bitcoin-falls-back-to-82k-as-ai-selldown-rising-oil-batter-risk-4964695
  - Investing.com Crypto News | 2026-10-22 19:17:58 | Bitcoin breaks below 200 SMA and cloud: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-bull-flag-coils-at-81908-live-levels-93CH-4958174
  - Investing.com Crypto News | 2026-10-21 21:46:19 | Bitcoin gains more than 2% to $84.8k as risk sentiment prevails | https://www.investing.com/news/cryptocurrency-news/bitcoin-firms-to-82k-but-oil-ai-jitters-limit-upside-4961711

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-10-25`
- priority_score: `99.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `4`
- score_breakdown: search `14` / timeliness `20` / monetization `15`
- source_names: CNBC Top News, MarketWatch Breaking News, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Meta stock sinks nearly 7% as AI spend pushes free cash flow negative
  - Steep bill for AI buildout punishes Meta, other tech favorites - Reuters
  - 3 big reasons Micron and other chip stocks fell hard on Thursday
  - Zuckerberg’s Big Deal to Stay in California
- recent_evidence:
  - CNBC Top News | 2026-10-22T20:03:03+00:00 | Meta stock sinks nearly 7% as AI spend pushes free cash flow negative | https://www.cnbc.com/2026/10/22/meta-stock-q3-earnings-free-cash-flow.html
  - Reuters Markets via Google News RSS | 2026-10-22T18:33:00+00:00 | Steep bill for AI buildout punishes Meta, other tech favorites - Reuters | https://news.google.com/rss/articles/CBMipAFBVV95cUxOaG4yYUM1ZzJnZmtpWnhIUVEzU01PRmxZM1BDRDJLazA1dkdaX3k0Z2pPMHJJUi1HUEM2OF9oV1JzSFh3d1dEU0dzc3JMQWRCeDhRa2JvNGVBbVluUlY4UGY3REoyWVZkTFBZT3BGa0swX2s1RzY3MDM5ZWlBTm1wYVBYNEt5M2VlTFoyRVNTTXJUaUVVYzVNcUtQQ2hfUW9nalZGbQ?oc=5

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword: `treasury_yields`
- publish_date: `2026-10-23`
- priority_score: `125.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3000`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `21` / timeliness `20` / monetization `15`
- source_names: CNBC Top News, Financial Times Home, MarketWatch Breaking News, NYT Business
- sample_headlines:
  - 10-year Treasury yield tumbles below 5% to lowest level in nearly a month
  - Europe’s bracing reality on US bond yields
  - Beware Bessent’s tilt towards short-term debt
  - US Treasury proposes tighter rules on investing in sensitive Chinese tech
  - The U.S. stock market is fracturing into two camps, and it’s leaving investors with a brutal case of whiplash
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-23T01:50:00+00:00 | Asian shares wobble as tech rout boosts bonds, dents rate hike bets - Reuters | https://news.google.com/rss/articles/CBMigwFBVV95cUxQMG5uTk9BQ2lzbUtHT1k4Nlp4RlRCcXFvVXR5YUhCamhubGQ1SlB0c2FYczVLdl9ESzJBRzdkNmVuYU1ISVc2MndXWnBZTzBDNFdzeHBEQTNPTGU2SGhBTmtKM3Z1SWUxR2szN20yYWIySGIzUXlZcXVhdGNtTlJNMGN1WQ?oc=5
  - Financial Times Home | 2026-10-22T23:13:15+00:00 | US Treasury proposes tighter rules on investing in sensitive Chinese tech | https://www.ft.com/content/f57a1f1c-60ce-432d-a901-673ae7d1241e?syn-25a6b1a6=1
  - MarketWatch Breaking News | 2026-10-22T22:07:00+00:00 | Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on. | https://www.marketwatch.com/story/treasury-yields-see-extreme-plunge-why-investors-are-ducking-for-cover-60044c66?mod=mw_rss_topstories
  - CNBC Top News | 2026-10-22T20:05:13+00:00 | 10-year Treasury yield tumbles below 5% to lowest level in nearly a month | https://www.cnbc.com/2026/10/22/treasurys-bonds-ai-yields.html
  - NYT Business | 2026-10-22T19:18:58+00:00 | Mortgage Rates Remain Above 7%, Pushing Home Prices Lower in Some Areas | https://www.nytimes.com/2026/10/22/business/mortgage-rates-housing-costs.html
