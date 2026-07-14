# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-07-14T07:25:49.583177+00:00`
- snapshot_generated_at: `2026-07-14T07:25:45.012734+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `1` / stale `0` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `aging`
- newest_evidence_age_days: `4.5`
- newest_evidence_iso: `2026-07-09T19:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 아직 쓸 수는 있지만 뉴스 속도는 조금 늦었습니다. 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 초안은 유지하되 발행 직전에 가격, 수치, headline을 한 번 더 갱신하는 편이 안전합니다.
- recovery_mode: `refresh_before_publish`
- recovery_summary: 발행 직전 전체 파이프라인을 다시 돌려 headline과 숫자를 최신 상태로 갱신하는 편이 안전합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-04-29T18:00:00+00:00 / Federal Reserve issues FOMC statement

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-07-14T05:50:00+00:00`
- quality_status: `review_before_publish` / ready_now `False`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: stock market news today
- recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Google Trends US / 2026-07-13T22:50:00-07:00 / stock market news today
- evidence: MarketWatch Breaking News / 2026-07-13T22:19:00+00:00 / Why a borrowing binge by investors is a warning sign for the stock market

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-07-14T06:55:24+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Live updates: Bitcoin holds $62,600 as the Iran conflict reignites and CPI looms
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CoinDesk RSS / 2026-07-14T06:55:24+00:00 / Live updates: Bitcoin holds $62,600 as the Iran conflict reignites and CPI looms
- evidence: CoinDesk RSS / 2026-07-14T06:28:43+00:00 / U.S. government moves $288 million in seized bitcoin, ether to Coinbase Prime
- evidence: CoinDesk RSS / 2026-07-14T04:43:56+00:00 / Solo bitcoin miner makes $200,000 using $150 equipment
