# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-09-25T04:26:26.885139+00:00`
- snapshot_generated_at: `2026-09-25T04:26:21.787384+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `8.4`
- newest_evidence_iso: `2026-09-16T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `full_refresh_needed`
- recovery_summary: 현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-07-29T18:00:00+00:00 / Federal Reserve issues FOMC statement

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.2`
- newest_evidence_iso: `2026-09-24T23:30:37+00:00`
- quality_status: `review_before_publish` / ready_now `False`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: S&P 500 ends marginally lower as investors focus on US-Iran war - Reuters
- recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Reuters Markets via Google News RSS / 2026-09-24T23:30:37+00:00 / S&P 500 ends marginally lower as investors focus on US-Iran war - Reuters
- evidence: MarketWatch Breaking News / 2026-09-24T23:26:00+00:00 / The S&P 500’s newest tech stock is now its best performer

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-09-25T02:00:54+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Block brings Bitcoin Lightning payments to x402 for AI agents
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-09-25T02:00:54+00:00 / Block brings Bitcoin Lightning payments to x402 for AI agents
- evidence: Cointelegraph / 2026-09-24T20:32:16+00:00 / Bitcoin price steadies, ONDO rallies as US Treasury yields hit 2007 highs
- evidence: CoinDesk RSS / 2026-09-24T18:46:58+00:00 / Bitcoin just topped a key long-term moving average. Here's what it might mean
