# 수익화 준비도 리포트

- 생성 시각: `2026-07-19T07:52:20.136130+00:00`
- 준비도 점수: `50.0`

## 단계별 상태

- `content_engine`: ready
  - evidence: publish queue ready items 4개
  - evidence: human tone average 92.0
  - next: 발행 가능한 글을 최소 1개 이상 유지하고, 매일 속보 1개 + evergreen 1개 조합을 계속 굴립니다.
- `publishing_engine`: ready
  - evidence: publish-ready html items 4개
  - evidence: blogger integration ready=True
  - evidence: wordpress integration ready=False
  - evidence: automated channel count=1
  - next: Blogger draft 업로드를 먼저 자동 검증하고, 안정화 뒤 WordPress를 두 번째 자동 채널로 확장합니다.
- `search_demand_engine`: ready
  - evidence: trend watchlist 5개
  - evidence: search console watchlist 0개
  - evidence: daily opportunity breaking candidates 5개
  - evidence: daily opportunity query watchlist 3개
  - evidence: seo follow-up backlog 12개
  - next: 기회판과 SEO 백로그를 기준으로 당일 글 1개, 후속 검색형 글 1개씩 이어 붙이면서 Search Console 데이터가 쌓일 때까지 운영합니다.
- `analytics_stack`: not_ready
  - evidence: GA4 measurement id missing
  - missing: GA4_MEASUREMENT_ID
  - next: GA4 측정 ID를 연결해 어떤 글이 실제 체류시간과 재방문을 만드는지 확인합니다.
- `adsense_stack`: not_ready
  - evidence: AdSense publisher id missing
  - missing: ADSENSE_PUBLISHER_ID
  - missing: ADSENSE_SITE_VERIFICATION
  - next: AdSense 승인 이후 publisher id와 사이트 검증값을 붙여 수익화 스택을 완성합니다.
- `retention_stack`: not_ready
  - evidence: newsletter url missing
  - missing: NEWSLETTER_SUBSCRIBE_URL
  - next: 뉴스레터나 텔레그램 같은 재방문 수단 URL을 연결해 한 번 들어온 독자를 쌓습니다.

## 지금 바로 올릴 우선 글

- `1` `fomc`: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지 / 목표 페이지뷰와 체류시간 균형 확보 / CTA 환율·금리·미국증시 evergreen 글로 연결
- `2` `bitcoin`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / 목표 페이지뷰와 체류시간 균형 확보 / CTA ETF·규제·초보 가이드 글로 연결
- `3` `us_index_flow`: 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유 / 목표 페이지뷰와 체류시간 균형 확보 / CTA 실적·공급망·대표 종목 글로 연결

## 다음 액션

- analytics_stack: GA4 측정 ID를 연결해 어떤 글이 실제 체류시간과 재방문을 만드는지 확인합니다.
- adsense_stack: AdSense 승인 이후 publisher id와 사이트 검증값을 붙여 수익화 스택을 완성합니다.
- retention_stack: 뉴스레터나 텔레그램 같은 재방문 수단 URL을 연결해 한 번 들어온 독자를 쌓습니다.
