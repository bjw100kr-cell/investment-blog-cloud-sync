# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-08-28T22:11:08.592281+00:00`
- snapshot_generated_at: `2026-08-28T22:11:03.752602+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `9.2`
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

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-08-28T21:37:51+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin dips to $78.4K as Fed’s Warsh downplays softer inflation prints
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-08-28T15:31:25+00:00 / Bitcoin dips to $78.4K as Fed’s Warsh downplays softer inflation prints
- evidence: Cointelegraph / 2026-08-28T14:53:40+00:00 / Crypto Biz: Bitcoin pumps, Wall Street does the paperwork
- evidence: CoinDesk RSS / 2026-08-28T11:43:19+00:00 / Bitcoin is outperforming stocks and correlating with gold just when it matters most

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-08-28T21:34:00+00:00`
- quality_status: `review_before_publish` / ready_now `False`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Microsoft’s stock seals its longest winning streak of the year as AI software fears fade
- recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: MarketWatch Breaking News / 2026-08-28T21:34:00+00:00 / Microsoft’s stock seals its longest winning streak of the year as AI software fears fade
- evidence: CNBC Top News / 2026-08-28T19:09:34+00:00 / Apple hikes subscription prices for Apple TV and Apple One in the U.S.
- evidence: Google Trends US / 2026-08-28T14:30:00-07:00 / apple watch ultra 4
