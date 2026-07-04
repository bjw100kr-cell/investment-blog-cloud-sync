# Popular Reads Board

메인 글 아래나 허브 페이지에 붙일 `popular reads` 후보를 미리 묶어보는 운영 카드입니다.
- board_goal: 메인 글 아래나 허브 페이지에 붙일 popular reads 후보를 묶어 내부링크와 재방문 흐름을 강화
- group_count: `4`

## 1. 거시 이벤트 해설 클러스터

- source_keyword: `fomc`
- headline: 오늘 메인 동선에 바로 붙일 popular reads 묶음
- main_ready_to_upload: `True`
- cta_focus: 환율·금리·미국증시 evergreen 글로 연결
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- pick: `FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지` / `fomc` / `main_pick` / ready `True` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`

## 2. 코인 해설 클러스터

- source_keyword: `bitcoin`
- headline: 오늘 메인 동선에 바로 붙일 popular reads 묶음
- main_ready_to_upload: `True`
- cta_focus: ETF·규제·초보 가이드 글로 연결
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- pick: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트` / `bitcoin` / `main_pick` / ready `True` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`

## 3. 미국 빅테크 허브 클러스터

- source_keyword: `us_big_tech`
- headline: 오늘 먼저 노출할 popular reads 묶음
- main_ready_to_upload: `False`
- cta_focus: 실적·공급망·대표 종목 글로 연결
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=review_before_publish
- blocker: follow_up_posts_present
- blocker: canonical_url_present
- blocker: newsletter_ready
- pick: `미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자` / `us_big_tech` / `main_pick` / ready `False` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-미국-빅테크-주가가-흔들릴-때-확인할-것-실적-금리-ai-투자.html`
- pick: `미국 빅테크 주식 관련 대표 종목 한눈에 보기` / `seo_us_big_tech_7` / `followup_pick_1` / ready `True` / 검색형 유입을 받기 좋은 주제
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/01-미국-빅테크-주식-관련-대표-종목-한눈에-보기.html`
- pick: `미국 빅테크 주식 공급망 정리: 누가 수혜를 보나` / `seo_us_big_tech_8` / `followup_pick_2` / ready `True` / 페이지 체류시간을 늘리기 좋은 주제
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/02-미국-빅테크-주식-공급망-정리-누가-수혜를-보나.html`

## 4. us_index_flow 클러스터

- source_keyword: `us_index_flow`
- headline: 오늘 먼저 노출할 popular reads 묶음
- main_ready_to_upload: `False`
- cta_focus: 실적·공급망·대표 종목 글로 연결
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=needs_fix
- pick: `미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유` / `us_index_flow` / `main_pick` / ready `False` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-미국-증시-지수-흐름-해설.html`
