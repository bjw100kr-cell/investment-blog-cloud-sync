# Traffic Cluster Board

메인 글과 후속 글을 묶어 페이지뷰, 내부링크 순환, 재방문을 같이 키우기 위한 운영 보드입니다.
- board_goal: 메인 글 1개로 끝내지 않고 후속 글과 내부링크로 페이지뷰와 재방문을 늘리는 일일 트래픽 클러스터 우선순위 보드
- cluster_count: `5`

## 1. 코인 해설 클러스터

- source_keyword: `bitcoin`
- revenue_priority_rank: `2`
- cluster_priority_score: `122.0`
- main_title: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- main_quality_status: `pass`
- main_ready_to_upload: `True`
- followup_count: `0`
- ready_followup_count: `0`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: ETF·규제·초보 가이드 글로 연결
- capture_route: `breaking_to_evergreen`
- route_description: 당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`

## 2. ai_semiconductors 클러스터

- source_keyword: `ai_semiconductors`
- revenue_priority_rank: `3`
- cluster_priority_score: `112.0`
- main_title: `AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지`
- main_quality_status: `needs_fix`
- main_ready_to_upload: `False`
- followup_count: `0`
- ready_followup_count: `0`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: 실적·공급망·대표 종목 글로 연결
- capture_route: `sector_hub_to_followups`
- route_description: 섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=needs_fix
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`

## 3. 거시 이벤트 해설 클러스터

- source_keyword: `fomc`
- revenue_priority_rank: `99`
- cluster_priority_score: `122.0`
- main_title: `FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지`
- main_quality_status: `pass`
- main_ready_to_upload: `True`
- followup_count: `0`
- ready_followup_count: `0`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: 환율·금리·미국증시 evergreen 글로 연결
- capture_route: `breaking_to_evergreen`
- route_description: 당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`

## 4. 미국 빅테크 허브 클러스터

- source_keyword: `us_big_tech`
- revenue_priority_rank: `99`
- cluster_priority_score: `110.0`
- main_title: `미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자`
- main_quality_status: `review_before_publish`
- main_ready_to_upload: `False`
- followup_count: `0`
- ready_followup_count: `0`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: 실적·공급망·대표 종목 글로 연결
- capture_route: `sector_hub_to_followups`
- route_description: 섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=review_before_publish
- blocker: follow_up_posts_present
- blocker: canonical_url_present
- blocker: newsletter_ready
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-미국-빅테크-주가가-흔들릴-때-확인할-것-실적-금리-ai-투자.html`

## 5. 인플레이션 해설 클러스터

- source_keyword: `cpi`
- revenue_priority_rank: `99`
- cluster_priority_score: `106.4`
- main_title: ``
- main_quality_status: `unknown`
- main_ready_to_upload: `False`
- followup_count: `1`
- ready_followup_count: `1`
- revenue_objective: 
- cta_focus: 
- capture_route: `breaking_to_evergreen`
- route_description: 당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=unknown
- followup: `cpi: 지금 투자자가 확인할 체크포인트 5가지` / `seo_cpi_11` / priority `106.37` / 새 검색 수요를 빠르게 받아내고 내부링크로 기존 핵심 글과 연결
