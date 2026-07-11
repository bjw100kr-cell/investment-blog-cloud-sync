# Search Console Setup Card

실제 하루 200명 달성을 증명하려면 Search Console에서 블로그 속성 검증이 먼저 필요합니다.

## Current State

- blog_url: `https://gimu-economy-insight.blogspot.com/`
- proof_status: `measurement_missing`
- search_console_available: `False`
- accessible_site_count: `0`

## One-Time Setup

### 지금 할 일 1개

- action: `Search Console에 URL-prefix 속성 추가/검증`
- property_value: `https://gimu-economy-insight.blogspot.com/`
- open: https://search.google.com/search-console/welcome
- why: 이 작업이 끝나야 실제 검색 클릭/노출을 가져와 하루 200명 달성 여부를 증명할 수 있습니다.

- recommended_property_type: `URL-prefix`
- property_value: `https://gimu-economy-insight.blogspot.com/`
- why: Blogger 하위 도메인은 URL-prefix 속성으로 먼저 검증하는 것이 가장 단순합니다.
- add property: https://search.google.com/search-console/welcome
- sitemap page: https://search.google.com/search-console/sitemaps
- latest post inspection: https://search.google.com/search-console/inspect?resource_id=https%3A%2F%2Fgimu-economy-insight.blogspot.com%2F2026%2F06%2Fblog-post.html

## Step By Step

1. Search Console을 같은 Google 계정으로 엽니다.
2. 속성 추가에서 `URL-prefix`를 선택합니다.
3. `https://gimu-economy-insight.blogspot.com/`를 그대로 붙여넣고 계속을 누릅니다.
4. Blogger를 관리하는 같은 Google 계정이면 Google-hosted property로 자동 검증될 수 있습니다.
5. 검증 후 Sitemaps 메뉴에서 `sitemap.xml`과 `feeds/posts/default?orderby=UPDATED`를 제출합니다.
6. URL 검사에서 상위 공개 글 3~5개를 검사하고 색인 요청합니다.
7. 아래 재검증 명령을 실행해 accessible_sites와 clicks/impressions가 들어오는지 확인합니다.

## Submit These Sitemaps

- `https://gimu-economy-insight.blogspot.com/sitemap.xml`
- `https://gimu-economy-insight.blogspot.com/feeds/posts/default?orderby=UPDATED`

## First URLs To Inspect

- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트: https://gimu-economy-insight.blogspot.com/2026/06/blog-post.html
- `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지: https://gimu-economy-insight.blogspot.com/2026/06/fomc.html
- `china` / 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_510.html
- `seo_us_big_tech_10` / 미국 빅테크 주식 ETF·지수·대표 기업 정리: https://gimu-economy-insight.blogspot.com/2026/07/5.html
- `us_index_flow` / 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_30.html
- `seo_oil_12` / 국제유가 전망 초보자 가이드: 용어부터 시장 반응까지: https://gimu-economy-insight.blogspot.com/2026/07/5_097860030.html
- `seo_ai_semiconductors_11` / AI 반도체 주식 공급망 정리: 누가 수혜를 보나: https://gimu-economy-insight.blogspot.com/2026/07/ai-5.html
- `seo_us_index_flow_8` / 미국 증시 오늘: 지금 투자자가 확인할 체크포인트 5가지: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_251.html
- `seo_oil_12` / 국제유가 전망: 지금 투자자가 확인할 체크포인트 5가지: https://gimu-economy-insight.blogspot.com/2026/07/5_097860030.html
- `seo_ai_semiconductors_11` / AI 반도체 주식: 지금 투자자가 확인할 체크포인트 5가지: https://gimu-economy-insight.blogspot.com/2026/07/ai-5.html

## Blockers

- Search Console 실측 데이터 없음: no_accessible_search_console_sites
- Search Console 접근 가능 사이트가 0개입니다. 블로그 속성 등록/검증 또는 계정 권한 연결이 필요합니다.

## After Setup

- run: `python3 scripts/fetch_search_console_queries.py && python3 scripts/build_visitor_proof_board.py`
- full refresh: `python3 scripts/fetch_search_console_queries.py && python3 scripts/search_console_to_feedback.py && python3 scripts/compile_performance_feedback.py && python3 scripts/build_visitor_proof_board.py`
- success: Search Console API에서 accessible_sites가 1개 이상이고 visitor-proof-board가 실제 clicks/impressions를 표시

## Official References

- [Google Search Console: Add a website property](https://support.google.com/webmasters/answer/34592): Blogger 같은 Google-hosted site는 같은 계정이면 URL-prefix 또는 Domain property 검증이 자동 처리될 수 있습니다.
- [Google Search Central: Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap): Blogger 같은 CMS는 sitemap/feed를 제공할 수 있고, Search Console Sitemaps report로 제출합니다.
- [Google Search Console: Sitemaps report](https://support.google.com/webmasters/answer/7451001): Sitemaps report에서 제출 이력과 처리 오류를 확인합니다.
