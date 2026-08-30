# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-08-30T04:53:11.374943+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-08-31`
- priority_score: `122.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `5400`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - A $1.1 million crypto card hack crashed a neobank's token 49%
  - Ditching 'digital gold': BPI study suggests everyday Americans prefer control and micro-investing
  - Inside the high-stakes battle between digital dollars and Swift's massive money engine
  - The next trillion-dollar currency may not be a stablecoin — it might not even have a name yet
  - Bitcoin wallets untouched for 10 years moved $40 million worth of coins
- recent_evidence:
  - Cointelegraph | 2026-08-29T06:47:12+00:00 | Bitcoin ETFs end 9-day inflow streak as BTC dips below $78K | https://cointelegraph.com/markets/bitcoin-etf-end-9-day-inflow-streak-btc-below-78k?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-08-29T04:30:00+00:00 | Bitcoin wallets untouched for 10 years moved $40 million worth of coins | https://www.coindesk.com/markets/2026/08/28/bitcoin-wallets-untouched-for-10-years-moved-usd40-million-most-avoided-exchanges
  - Investing.com Crypto News | 2026-08-29 21:13:26 | Bitcoin price holds at $78,000 as ‘digital gold’ narrative faces fresh test | https://www.investing.com/news/cryptocurrency-news/bitcoin-price-slips-below-78000-as-digital-gold-narrative-faces-fresh-test-4881960
  - Investing.com Crypto News | 2026-08-29 19:02:26 | Bitcoin consolidates between $77.2K-$78.7K: Hourly levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-stalls-below-78500-resistance-live-hourly-levels-93CH-4872743
  - Investing.com Crypto News | 2026-08-28 21:37:51 | Bitcoin sheds more than 3% on hawkish Warsh, loses steam after debasement rally | https://www.investing.com/news/cryptocurrency-news/bitcoin-steadies-near-80k-with-warsh-speech-in-focus-4880563

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-09-01`
- priority_score: `88.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `10` / timeliness `13` / monetization `15`
- source_names: CNBC Top News, MarketWatch Breaking News
- sample_headlines:
  - Tech backlash reaches fever pitch as AI angst collides with social media fears
  - Meta’s $18 billion settlement puts TikTok and YouTube on notice. Who's next on the firing line?
  - Tim Cook wasn’t a ‘product guy’ — so he re-engineered Apple instead
- recent_evidence:
  - NYT Business | 2026-08-29T17:02:38+00:00 | Thievery or Innovation? The Music Industry Grapples With A.I. | https://www.nytimes.com/2026/08/29/business/dealbook/ai-generated-music.html
  - MarketWatch Breaking News | 2026-08-29T12:30:00+00:00 | Tim Cook wasn’t a ‘product guy’ — so he re-engineered Apple instead | https://www.marketwatch.com/story/tim-cook-wasnt-a-product-guy-so-he-re-engineered-apple-instead-03ca53f4?mod=mw_rss_topstories
  - CNBC Top News | 2026-08-29T05:00:01+00:00 | Meta’s $18 billion settlement puts TikTok and YouTube on notice. Who's next on the firing line? | https://www.cnbc.com/2026/08/29/meta-settlement-tiktok-youtube-snap-teen-safety.html

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword: `treasury_yields`
- publish_date: `2026-08-30`
- priority_score: `123.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `2600`
- fallback_source: `source_snapshot_rank`
- source_count: `5`
- score_breakdown: search `18` / timeliness `21` / monetization `15`
- source_names: Financial Times Home, Financial Times World, Investing.com Crypto News, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - altFINS Partners with BitPath Holdings to Launch Gen 2 Digital Asset Treasury Strategy Powered by AI Analytics
  - Rising bond yields add tens of billions to G7 countries’ debt costs
  - Stocks fall while dollar, bond yields rise as Warsh prompts rate hike bets - Reuters
  - Treasury Bars Some Reporters From G20 Finance Meeting
- recent_evidence:
  - Financial Times Home | 2026-08-30T04:12:14+00:00 | What’s the fiscal hit from higher yields? | https://www.ft.com/content/63311687-676b-4548-9bd8-3d7ad96d7ce5
  - Financial Times Home | 2026-08-30T04:00:19+00:00 | Rising bond yields add tens of billions to G7 countries’ debt costs | https://www.ft.com/content/bbe90db5-64ac-441d-87e4-e984c5ef8629?syn-25a6b1a6=1
  - NYT Business | 2026-08-29T23:20:50+00:00 | Treasury Bars Some Reporters From G20 Finance Meeting | https://www.nytimes.com/2026/08/29/business/reporters-denied-g20-meeting.html
  - Reuters Markets via Google News RSS | 2026-08-28T01:56:00+00:00 | Stocks fall while dollar, bond yields rise as Warsh prompts rate hike bets - Reuters | https://news.google.com/rss/articles/CBMigwFBVV95cUxPd1RUYUM0TDhTNURUOVdtU1ZYc0p2YTZQZGhTREUtRkRNWms5UVN5LUVxelJjWVluQVJkQ0UteTAtMng0V2h1Z014d2xQZXBZUDZfSHdSM2ZXdWljRFBJT0lXR1VHVUo3N0djMVJmaHkzaVh4YWJpWlZtSFM3RjJLYUc0Zw?oc=5
  - Investing.com Crypto News | 2026-08-28 18:00:39 | altFINS Partners with BitPath Holdings to Launch Gen 2 Digital Asset Treasury Strategy Powered by AI Analytics | https://www.investing.com/news/cryptocurrency-news/altfins-partners-with-bitpath-holdings-to-launch-gen-2-digital-asset-treasury-strategy-powered-by-ai-analytics-4881727
