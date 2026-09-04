# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-09-04T16:13:36.923385+00:00`
- snapshot_generated_at: `2026-09-04T16:13:31.683233+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `15.9`
- newest_evidence_iso: `2026-08-19T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `full_refresh_needed`
- recovery_summary: 현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-07-29T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.5`
- newest_evidence_iso: `2026-09-04T04:00:19+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Silicon shadows: inside the black market for AI chips | FT Film
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Financial Times YouTube / 58K views / Silicon shadows: inside the black market for AI chips | FT Film
- evidence: Financial Times Home / 2026-09-04T04:00:19+00:00 / Anthropic’s $2tn IPO puts powerful external trustees in spotlight
- evidence: Financial Times Home / 2026-09-03T18:00:11+00:00 / OpenAI says it has overtaken Anthropic with its latest AI model

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-09-04T14:04:03+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: We checked 6 years of bitcoin data. The NFP report isn't big price mover
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CoinDesk RSS / 2026-09-04T11:29:05+00:00 / We checked 6 years of bitcoin data. The NFP report isn't big price mover
- evidence: CoinDesk RSS / 2026-09-04T09:57:01+00:00 / Bitcoin clears $81,000 as privacy coins lead a broad crypto rally
- evidence: CoinDesk RSS / 2026-09-04T09:47:15+00:00 / IMF confirms El Salvador’s bitcoin growth was funded by private donations, not public money
