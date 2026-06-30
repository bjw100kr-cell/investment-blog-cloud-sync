# Search Console Setup Card

실제 하루 200명 달성을 증명하려면 Search Console에서 블로그 속성 검증이 먼저 필요합니다.

## Current State

- blog_url: `https://gimu-economy-insight.blogspot.com/`
- proof_status: `measurement_missing`
- search_console_available: `False`
- accessible_site_count: `0`

## One-Time Setup

- recommended_property_type: `URL-prefix`
- property_value: `https://gimu-economy-insight.blogspot.com/`
- why: Blogger 하위 도메인은 URL-prefix 속성으로 먼저 검증하는 것이 가장 단순합니다.
- add property: https://search.google.com/search-console/welcome
- sitemap page: https://search.google.com/search-console/sitemaps
- latest post inspection: https://search.google.com/search-console/inspect?resource_id=https%3A%2F%2Fgimu-economy-insight.blogspot.com%2F2026%2F06%2Fblog-post.html

## Submit These Sitemaps

- `https://gimu-economy-insight.blogspot.com/sitemap.xml`
- `https://gimu-economy-insight.blogspot.com/feeds/posts/default?orderby=UPDATED`

## First URLs To Inspect

- `bitcoin` / 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트: https://gimu-economy-insight.blogspot.com/2026/06/blog-post.html
- `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지: https://gimu-economy-insight.blogspot.com/2026/06/fomc.html
- `seo_fomc_2` / FOMC 이후 시장에서 다음으로 봐야 할 체크포인트 5가지: https://gimu-economy-insight.blogspot.com/2026/06/fomc-5.html
- `seo_fomc_1` / FOMC 이후 시장이 주식과 코인에 미치는 영향: https://gimu-economy-insight.blogspot.com/2026/06/fomc_074069453.html
- `china` / 중국 변수와 시장 영향 해설: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_510.html
- `us_index_flow` / 미국 증시 지수 흐름 해설: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_30.html
- `seo_fomc_3` / FOMC 이후 시장 초보자 가이드: 용어부터 시장 반응까지: https://gimu-economy-insight.blogspot.com/2026/06/fomc_01787353078.html
- `seo_us_index_flow_9` / 미국 증시 지수 흐름 ETF·지수·대표 기업 정리: https://gimu-economy-insight.blogspot.com/2026/06/etf_01918375183.html
- `seo_us_index_flow_8` / 미국 증시 지수 흐름 공급망 정리: 누가 수혜를 보나: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_251.html
- `seo_us_index_flow_7` / 미국 증시 지수 흐름 관련 대표 종목 한눈에 보기: https://gimu-economy-insight.blogspot.com/2026/06/blog-post_154.html

## Blockers

- Search Console 실측 데이터 없음: 403 Client Error: Forbidden for url: https://www.googleapis.com/webmasters/v3/sites/https%3A%2F%2Fgimu-economy-insight.blogspot.com%2F/searchAnalytics/query
- Search Console 접근 가능 사이트가 0개입니다. 블로그 속성 등록/검증 또는 계정 권한 연결이 필요합니다.

## After Setup

- run: `python3 scripts/fetch_search_console_queries.py && python3 scripts/build_visitor_proof_board.py`
- success: Search Console API에서 accessible_sites가 1개 이상이고 visitor-proof-board가 실제 clicks/impressions를 표시
