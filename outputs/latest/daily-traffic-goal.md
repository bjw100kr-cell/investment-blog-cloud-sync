# Daily Traffic Goal

- 목표: 하루 최소 `200`명 방문
- 현재 예상 합계: `337`명
- 목표까지 부족분: `0`명
- 상태: `estimated_on_track_measurement_missing`

## 200명 목표를 위한 오늘의 글 경로

1. `fomc` FOMC 이후 시장 해설 / 예상 `95`명 / 수요 `5700` / 품질 `pass`
   - action: 금리·달러·주식·코인 영향까지 한 번에 설명하는 evergreen 허브로 연결
2. `bitcoin` 비트코인 핵심 흐름 해설 / 예상 `95`명 / 수요 `6000` / 품질 `pass`
   - action: 코인 시장 신호와 ETF/규제 후속 글을 내부링크로 묶어 발행
3. `us_index_flow` 미국 증시 지수 흐름 해설 / 예상 `92`명 / 수요 `3400` / 품질 `pass`
   - action: 대표 종목/실적/지수 흐름 후속 글로 페이지뷰 확장
4. `china` 중국 변수와 시장 영향 해설 / 예상 `55`명 / 수요 `0` / 품질 `pass`
   - action: 세계 흐름 해설 뒤 관련 섹터/환율 글로 연결

## 병목

- GA4/Search Console 연결 전이라 실제 200명 달성 여부를 자동 측정하기 어렵습니다.
- 뉴스레터/텔레그램 재방문 동선이 없어 첫 방문자를 반복 방문으로 쌓기 어렵습니다.

## 다음 액션

- 오늘은 예상 방문자 기여도가 가장 큰 1개 글을 먼저 발행하고, 같은 클러스터 후속 글 2개를 내부링크로 묶습니다.
- 검색 수요 점수 3,000 이상 키워드는 메인 해설 1개 + 초보자/FAQ/ETF·규제 후속 글로 묶어 체류시간을 늘립니다.
- GA4_MEASUREMENT_ID와 SEARCH_CONSOLE_SITE_URL을 연결하면 200명/일 달성 여부를 추정이 아니라 실제 지표로 전환합니다.

## 후보 전체

- `fomc` lane `macro` / 예상 `95`명 / ready `True` / quality `pass`
- `bitcoin` lane `crypto` / 예상 `95`명 / ready `True` / quality `pass`
- `us_index_flow` lane `us-stocks` / 예상 `92`명 / ready `True` / quality `pass`
- `china` lane `world-flow` / 예상 `55`명 / ready `True` / quality `pass`
- `ai_semiconductors` lane `us-stocks` / 예상 `0`명 / ready `False` / quality `unknown`
