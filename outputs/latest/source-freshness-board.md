# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-07-04T15:47:29.998497+00:00`
- snapshot_generated_at: `2026-07-04T15:47:25.616352+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `1` / aging `0` / stale `1` / unknown `1`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `16.9`
- newest_evidence_iso: `2026-06-17T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `full_refresh_needed`
- recovery_summary: 현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-04-29T18:00:00+00:00 / Federal Reserve issues FOMC statement

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- freshness_status: `unknown`
- newest_evidence_age_days: `None`
- newest_evidence_iso: ``
- quality_status: `review_before_publish` / ready_now `False`
- summary: 대표 근거 시각을 읽지 못해 판단이 보류되었습니다.
- recommendation: 최근 근거 시각을 다시 수집해 신선도를 먼저 확인하세요.
- recovery_mode: `manual_check`
- recovery_summary: 최근 근거 시각을 먼저 다시 확인한 뒤 다음 액션을 결정하세요.

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-07-04T13:09:16+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bollinger Bands creator eyes Bitcoin bear-market end, 'W'-shaped reversal
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-07-04T13:09:16+00:00 / Bollinger Bands creator eyes Bitcoin bear-market end, 'W'-shaped reversal
- evidence: Cointelegraph / 2026-07-04T08:31:02+00:00 / Tim Draper denies moving Bitcoin, reiterates $250,000 BTC prediction
- evidence: CoinDesk RSS / 2026-07-04T06:48:42+00:00 / Bitcoin’s next parabolic run may need $1 trillion in fresh capital
