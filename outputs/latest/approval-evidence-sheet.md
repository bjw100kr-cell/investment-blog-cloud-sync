# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-05T09:48:26.749192+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-06`
- priority_score: `126.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `5700`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, NYT Business
- sample_headlines:
  - Barstool's Portnoy plans to hold bitcoin down to zero after timing it wrong every time
  - Bitcoin jumps above $63,000, reversing end-June losses
  - Bitcoin experts split over plan to freeze Satoshi's 1.1 million bitcoin as quantum threat grows
  - How ethical hackers with just a $3,000 server found a flaw that could've put $70 billion in crypto at risk
  - Why bitcoin's disconnect from record-high stocks won't last
- recent_evidence:
  - CoinDesk RSS | 2026-07-05T06:00:22+00:00 | Barstool's Portnoy plans to hold bitcoin down to zero after timing it wrong every time | https://www.coindesk.com/markets/2026/07/05/barstool-s-portnoy-plans-to-hold-bitcoin-down-to-zero-after-timing-it-wrong-every-time
  - Investing.com Crypto News | 2026-07-05 07:02:21 | Bitcoin tests $63,100-$63,600 resistance: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-in-bear-flag-near-annual-low-live-levels-93CH-4764319
  - CoinDesk RSS | 2026-07-04T18:07:17+00:00 | Bitcoin jumps above $63,000, reversing end-June losses | https://www.coindesk.com/markets/2026/07/04/bitcoin-jumps-above-usd63-000-reversing-end-june-losses
  - CoinDesk RSS | 2026-07-04T18:00:00+00:00 | Bitcoin experts split over plan to freeze Satoshi's 1.1 million bitcoin as quantum threat grows | https://www.coindesk.com/business/2026/07/04/bitcoin-experts-split-over-plan-to-freeze-satoshi-s-1-1-million-bitcoin-as-quantum-threat-grows
  - CoinDesk RSS | 2026-07-04T16:00:00+00:00 | Why bitcoin's disconnect from record-high stocks won't last | https://www.coindesk.com/markets/2026/07/03/why-bitcoin-s-disconnect-from-record-high-stocks-won-t-last

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-07-07`
- priority_score: `120.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (반도체)
- format: `sector_analysis`
- demand_signal_score: `20200`
- fallback_source: `trend_match`
- source_count: `3`
- score_breakdown: search `30` / timeliness `15` / monetization `15`
- trend_queries: 반도체
- trend_regions: KR
- source_names: Google Trends KR, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - 반도체
  - Trading Day: Chips are down, and so are payrolls - Reuters
  - Are the ‘MANGOS’ Stocks Already Turning Soft?
- recent_evidence:
  - Google Trends KR | 2026-07-04T23:50:00-07:00 | 반도체 | https://trends.google.com/trending/rss?geo=KR
  - Reuters Markets via Google News RSS | 2026-07-02T21:11:28+00:00 | Trading Day: Chips are down, and so are payrolls - Reuters | https://news.google.com/rss/articles/CBMimwFBVV95cUxQLXd6N2hYVEtXSklabi1QdDBWMEU0ZW1OUExWR1hhSDNJNGFrMkNKalRHcXlOdnFVLVVYTldrVlBOTXNzWml6MEY2RHVxcGI4Wl9NRlM3R2U1ZkJFbGQ4RVJFQkU4MXQzbG5UVDlVSTBleEpYQUdvaWFJSG9ydHFtRlBhM0ZwT3kxOGEteGxlQVJ4Q0p6RmdGYVBIUQ?oc=5

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-07-08`
- priority_score: `80.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `8` / timeliness `10` / monetization `13`
- source_names: Financial Times Home, Financial Times World
- sample_headlines:
  - Wall Street banks recover in China amid trading boom
  - China cools on overseas publication of scientific research
- recent_evidence:
  - Financial Times Home | 2026-07-05T04:00:02+00:00 | Wall Street banks recover in China amid trading boom | https://www.ft.com/content/90c1934a-505f-4c9d-9bdf-a28db14eb9f2
  - Financial Times World | 2026-07-05T04:00:02+00:00 | China cools on overseas publication of scientific research | https://www.ft.com/content/64a811f1-b132-4211-8a8c-2252cf964039
