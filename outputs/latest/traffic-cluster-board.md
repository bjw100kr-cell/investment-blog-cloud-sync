# Traffic Cluster Board

메인 글과 후속 글을 묶어 페이지뷰, 내부링크 순환, 재방문을 같이 키우기 위한 운영 보드입니다.
- board_goal: 메인 글 1개로 끝내지 않고 후속 글과 내부링크로 페이지뷰와 재방문을 늘리는 일일 트래픽 클러스터 우선순위 보드
- cluster_count: `4`

## 1. 코인 해설 클러스터

- source_keyword: `bitcoin`
- revenue_priority_rank: `2`
- cluster_priority_score: `124.0`
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
- cluster_priority_score: `320.0`
- main_title: `AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지`
- main_quality_status: `review_before_publish`
- main_ready_to_upload: `False`
- followup_count: `2`
- ready_followup_count: `2`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: 실적·공급망·대표 종목 글로 연결
- capture_route: `sector_hub_to_followups`
- route_description: 섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=review_before_publish
- blocker: follow_up_posts_present
- blocker: canonical_url_present
- blocker: newsletter_ready
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`
- followup: `AI 반도체 주식 관련 대표 종목 한눈에 보기` / `seo_ai_semiconductors_8` / priority `108.5` / 섹터형 검색 유입 누적
- followup: `AI 반도체 주식 ETF·지수·대표 기업 정리` / `seo_ai_semiconductors_10` / priority `102.5` / 광고 노출과 장기 검색 유입 확보

## 3. tariffs_trade 클러스터

- source_keyword: `tariffs_trade`
- revenue_priority_rank: `99`
- cluster_priority_score: `273.5`
- main_title: `관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기`
- main_quality_status: `review_before_publish`
- main_ready_to_upload: `False`
- followup_count: `3`
- ready_followup_count: `3`
- revenue_objective: 페이지뷰와 체류시간 균형 확보
- cta_focus: 실적·공급망·대표 종목 글로 연결
- capture_route: `search_entry_to_internal_links`
- route_description: 검색형 진입 글에서 정의와 기준점을 설명한 뒤 관련 허브 글로 내부링크를 넘깁니다.
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=review_before_publish
- blocker: source_strength
- blocker: follow_up_posts_present
- blocker: canonical_url_present
- main_html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-관세와-무역-갈등이-증시에-미치는-영향-환율과-공급망까지-보기.html`
- followup: `관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기 관련 대표 종목 한눈에 보기` / `seo_tariffs_trade_11` / priority `70.5` / 섹터형 검색 유입 누적
- followup: `관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기 공급망 정리: 누가 수혜를 보나` / `seo_tariffs_trade_12` / priority `67.5` / 체류시간과 페이지뷰 확대
- followup: `관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기 ETF·지수·대표 기업 정리` / `seo_tariffs_trade_13` / priority `64.5` / 광고 노출과 장기 검색 유입 확보

## 4. 거시 이벤트 해설 클러스터

- source_keyword: `fomc`
- revenue_priority_rank: `99`
- cluster_priority_score: `117.0`
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
