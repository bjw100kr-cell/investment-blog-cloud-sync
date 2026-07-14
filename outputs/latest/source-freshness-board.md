# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-07-14T16:45:06.286582+00:00`
- snapshot_generated_at: `2026-07-14T16:45:01.367543+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `1` / aging `1` / stale `0` / unknown `1`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `aging`
- newest_evidence_age_days: `4.9`
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

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- freshness_status: `unknown`
- newest_evidence_age_days: `None`
- newest_evidence_iso: ``
- quality_status: `review_before_publish` / ready_now `False`
- summary: 대표 근거 시각을 읽지 못해 판단이 보류되었습니다.
- recommendation: 최근 근거 시각을 다시 수집해 신선도를 먼저 확인하세요.
- recovery_mode: `manual_check`
- recovery_summary: 최근 근거 시각을 먼저 다시 확인한 뒤 다음 액션을 결정하세요.
- evidence: Financial Times YouTube / 17K views / Silicon shadows: inside the black market for AI chips | FT Film

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-07-14T16:39:26+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin jumps on lowest US CPI since 2020 as traders stay wary of $64K failure
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-07-14T14:53:13+00:00 / Bitcoin jumps on lowest US CPI since 2020 as traders stay wary of $64K failure
- evidence: Investing.com Crypto News / 2026-07-14 14:03:57 / Bitcoin climbs to $63.8k on cool CPI data, but gains limited amid Iran, rate fears
- evidence: Investing.com Crypto News / 2026-07-14 07:04:32 / Bitcoin teeters above support after 48% drop: Live levels
