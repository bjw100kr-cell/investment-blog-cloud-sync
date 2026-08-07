# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-08-07T13:20:22.456738+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-08-08`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `6800`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, MarketWatch Breaking News
- sample_headlines:
  - After a Clarity Act funeral, the crypto world would keep turning
  - Why Bitcoin's BIP-110 refuses to die despite near-zero miner support
  - Bitcoin’s volatility has nearly disappeared. The risk hasn’t.
  - Bitcoin hovers below $65,000 as Middle East tensions escalate further
  - Coldcard fallout shows up onchain as 210,000 bitcoin leaves old wallets
- recent_evidence:
  - Cointelegraph | 2026-08-07T13:00:01+00:00 | Bitcoiners turn to dice throws as self-custody setups are re-evaluated | https://cointelegraph.com/features/bitcoiners-turn-to-dice-throws-as-self-custody-setups-are-re-evaluated?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-08-07T11:45:49+00:00 | Why Bitcoin's BIP-110 refuses to die despite near-zero miner support | https://www.coindesk.com/tech/2026/08/06/why-bitcoin-s-bip-110-refuses-to-die-despite-near-zero-miner-support
  - CoinDesk RSS | 2026-08-07T11:42:20+00:00 | Bitcoin’s volatility has nearly disappeared. The risk hasn’t. | https://www.coindesk.com/daybook-us/2026/08/07/bitcoin-s-volatility-has-nearly-disappeared-the-risk-hasn-t
  - Cointelegraph | 2026-08-07T11:05:01+00:00 | Binance Bitcoin volume ratio hits record as futures outweigh spot eight times over | https://cointelegraph.com/markets/binance-bitcoin-volume-ratio-hits-record-as-futures-outweigh-spot-eight-times-over?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-08-07T10:36:14+00:00 | Bitcoin hovers below $65,000 as Middle East tensions escalate further | https://www.coindesk.com/markets/2026/08/07/cmt

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-08-10`
- priority_score: `90.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `3`
- score_breakdown: search `11` / timeliness `15` / monetization `14`
- source_names: CNBC Top News, MarketWatch Breaking News, NYT Business
- sample_headlines:
  - Solar stocks shine after Trump extends China tariffs to polysilicon products
  - Optical stocks have a China problem that most investors are missing
  - China’s Export Boom Rolls On Despite Trade Backlash
- recent_evidence:
  - CNBC Top News | 2026-08-07T12:13:07+00:00 | Solar stocks shine after Trump extends China tariffs to polysilicon products | https://www.cnbc.com/2026/08/07/polysilicon-solar-tariffs-donald-trump-us-china-trade-war-energy-semiconductors.html
  - MarketWatch Breaking News | 2026-08-07T11:00:00+00:00 | Optical stocks have a China problem that most investors are missing | https://www.marketwatch.com/story/optical-stocks-have-a-china-problem-that-most-investors-are-missing-45523981?mod=mw_rss_topstories
  - NYT Business | 2026-08-07T07:20:24+00:00 | China’s Export Boom Rolls On Despite Trade Backlash | https://www.nytimes.com/2026/08/07/business/china-trade-exports.html

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-08-09`
- priority_score: `107.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (amd)
- format: `sector_analysis`
- demand_signal_score: `400`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `21` / timeliness `17` / monetization `15`
- trend_queries: amd
- trend_regions: KR
- source_names: CNBC Top News, Financial Times YouTube, Google Trends KR, MarketWatch Breaking News
- sample_headlines:
  - amd
  - SK Hynix to invest $38 billion building new memory chip plants as demand soars
  - Micron’s stock falls but is spared the worst of the memory-chip selloff
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Google Trends KR | 2026-08-07T04:30:00-07:00 | amd | https://trends.google.com/trending/rss?geo=KR
  - Financial Times YouTube | 50K views | Silicon shadows: inside the black market for AI chips | FT Film | https://www.youtube.com/watch?v=kFcWmQevQo8
  - CNBC Top News | 2026-08-07T09:02:59+00:00 | SK Hynix to invest $38 billion building new memory chip plants as demand soars | https://www.cnbc.com/2026/08/07/sk-hynix-memory-chips-ai-prices.html
  - MarketWatch Breaking News | 2026-08-07T02:35:00+00:00 | Micron’s stock falls but is spared the worst of the memory-chip selloff | https://www.marketwatch.com/story/microns-stock-claws-back-to-buck-the-memory-chip-selloff-58af0155?mod=mw_rss_topstories
