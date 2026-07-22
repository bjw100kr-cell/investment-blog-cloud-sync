# Popular Reads Board

메인 글 아래나 허브 페이지에 붙일 `popular reads` 후보를 미리 묶어보는 운영 카드입니다.
- board_goal: 메인 글 아래나 허브 페이지에 붙일 popular reads 후보를 묶어 내부링크와 재방문 흐름을 강화
- group_count: `4`

## 1. 코인 해설 클러스터

- source_keyword: `bitcoin`
- headline: 오늘 메인 동선에 바로 붙일 popular reads 묶음
- main_ready_to_upload: `True`
- cta_focus: ETF·규제·초보 가이드 글로 연결
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- pick: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트` / `bitcoin` / `main_pick` / ready `True` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`

## 2. ai_semiconductors 클러스터

- source_keyword: `ai_semiconductors`
- headline: 오늘 메인 동선에 바로 붙일 popular reads 묶음
- main_ready_to_upload: `True`
- cta_focus: 실적·공급망·대표 종목 글로 연결
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- pick: `AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지` / `ai_semiconductors` / `main_pick` / ready `True` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`
- pick: `AI 반도체 주식 관련 대표 종목 한눈에 보기` / `seo_ai_semiconductors_9` / `followup_pick_1` / ready `True` / 검색형 유입을 받기 좋은 주제
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/01-ai-반도체-주식-관련-대표-종목-한눈에-보기.html`

## 3. china 클러스터

- source_keyword: `china`
- headline: 오늘 먼저 노출할 popular reads 묶음
- main_ready_to_upload: `False`
- cta_focus: 실적·공급망·대표 종목 글로 연결
- next_action: 사용자 검토 후 승인 대기
- blocker: main_quality=review_before_publish
- blocker: follow_up_posts_present
- blocker: canonical_url_present
- blocker: newsletter_ready
- pick: `중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유` / `china` / `main_pick` / ready `False` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-중국-변수와-시장-영향-해설.html`
- pick: `중국 변수와 시장 영향 관련 대표 종목 한눈에 보기` / `seo_china_12` / `followup_pick_1` / ready `True` / 검색형 유입을 받기 좋은 주제
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/02-중국-변수와-시장-영향-관련-대표-종목-한눈에-보기.html`
- pick: `중국 변수와 시장 영향 공급망 정리: 누가 수혜를 보나` / `seo_china_13` / `followup_pick_2` / ready `True` / 페이지 체류시간을 늘리기 좋은 주제
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/03-중국-변수와-시장-영향-공급망-정리-누가-수혜를-보나.html`

## 4. 거시 이벤트 해설 클러스터

- source_keyword: `fomc`
- headline: 오늘 먼저 노출할 popular reads 묶음
- main_ready_to_upload: `True`
- cta_focus: 환율·금리·미국증시 evergreen 글로 연결
- next_action: 메인 글 승인 후 후속 SEO 글 내부링크 흐름 준비
- pick: `FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지` / `fomc` / `main_pick` / ready `True` / 지금 이 클러스터를 대표하는 메인 글
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`
