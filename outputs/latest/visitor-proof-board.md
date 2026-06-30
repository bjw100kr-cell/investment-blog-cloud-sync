# Visitor Proof Board

하루 200명 목표를 `예상`이 아니라 `실측 증거`로 확인하기 위한 보드입니다.

## Verdict

- proof_status: `measurement_missing`
- target_daily_visitors: `200`
- actual_verified_visitors: `0`
- actual_verified_impressions: `0`
- gap_to_verified_target: `200`

## Evidence Window

- source: `Google Search Console query clicks`
- site_url: `https://gimu-economy-insight.blogspot.com/`
- site_url_source: `blogger_upload_state`
- start_date: ``
- end_date: ``

## Projection Is Not Proof

- projected_daily_visitors: `335`
- projected_with_amplification: `335`
- potential_with_manual_amplification: `635`
- projection_is_proof: `False`

## Measurement Blockers

- Search Console 실측 데이터 없음: Search Console OAuth credentials are not set
- Search Console 설정 미완료: SEARCH_CONSOLE_SITE_URL

## Top Verified Queries

- 아직 실측 쿼리 데이터가 없습니다.

## Next Actions

- GitHub Actions secrets에 Search Console OAuth 값과 사이트 속성 URL을 연결해 실측 클릭을 가져옵니다.
- GA4 측정 ID를 연결해 검색 외 직접/재방문 트래픽까지 확인합니다.
- 그 전까지는 projected 값과 Blogger 공개 URL 기준 확산 계획을 참고하되, 목표 달성 증거로 보지는 않습니다.
- 측정 연결 후 이 보드에서 `proof_status=verified_achieved`가 나와야 목표 달성으로 판단합니다.
