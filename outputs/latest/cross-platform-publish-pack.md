# Cross-Platform Publish Pack

- generated_at: `2026-06-30T20:45:28.955315+00:00`
- selected_count: `4`
- manual_selected_count: `4`
- automation_policy: `automation-first`
- primary_channel: `blogger`
- secondary_channel: `wordpress`

## 자동 채널

### Blogger (자동)
- mode: `auto`
- ready: `True`
- ready_item_count: `4`
- command: `python3 scripts/upload_blogger_drafts.py`
- status: `ready_to_publish_candidates`

#### 후보 글
- [1] 비트코인 핵심 흐름 해설 | keyword=bitcoin | score=120.0 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- [8] 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조 | keyword=seo_bitcoin_4 | score=119.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-비트코인-핵심-흐름-초보자-가이드-지금-꼭-알아야-할-핵심-구조.html`
- [10] 비트코인 핵심 흐름 ETF·규제 이슈 정리 | keyword=seo_bitcoin_6 | score=116.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-비트코인-핵심-흐름-etf-규제-이슈-정리.html`
- [12] 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리 | keyword=seo_bitcoin_8 | score=113.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/06-비트코인-핵심-흐름-faq-10개-많이-헷갈리는-질문-정리.html`

### WordPress (자동)
- mode: `auto`
- ready: `False`
- ready_item_count: `4`
- command: `python3 scripts/upload_wordpress_drafts.py`
- status: `waiting_for_credentials`

#### 후보 글
- [1] 비트코인 핵심 흐름 해설 | keyword=bitcoin | score=120.0 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- [8] 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조 | keyword=seo_bitcoin_4 | score=119.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-비트코인-핵심-흐름-초보자-가이드-지금-꼭-알아야-할-핵심-구조.html`
- [10] 비트코인 핵심 흐름 ETF·규제 이슈 정리 | keyword=seo_bitcoin_6 | score=116.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-비트코인-핵심-흐름-etf-규제-이슈-정리.html`
- [12] 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리 | keyword=seo_bitcoin_8 | score=113.5 | quality=unknown | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/06-비트코인-핵심-흐름-faq-10개-많이-헷갈리는-질문-정리.html`

## 수동 채널

### 네이버 블로그 (수동)
- reason: 운영 정책상 수동 운영 채널로 분리
- editor_url: `https://blog.naver.com`
- ready: `True`
- mode: `manual`
- ready_item_count: `4`
- ready_command: `open https://blog.naver.com and paste html_path content`
- quality_note: `수동 채널은 품질 게이트 상태와 상관없이 수동 발행 후보로 노출됩니다.`
- publishing_steps:
  - 1) `html_path`에 적힌 파일을 열어 전체 본문을 복사
  - 2) 네이버 블로그 글쓰기 에디터에서 새 글 작성으로 붙여넣기
  - 3) 카테고리/태그: `경제`, `투자`, `주식`, `코인` 중심으로 정리
  - 공개 범위를 확인하고 발행
  - 발행한 뒤 링크에 `출처`를 한 줄 넣고, 수익화 성과 트래킹 시트에 URL 기록
  - 발행 URL을 추후 수동 성과 추적용으로 기록
  - 중복/오타 검수 후 바로 다음 글로 이동
- execution_notes:
  - 네이버는 현재 수동 채널입니다. 동일 후보 글이 여러 개면 한 번에 하나씩 발행하세요.
  - 업로드 대상이 여러 개면 `1번 후보 -> 발행 -> 다음 후보`로 순서 유지가 효율적입니다.

#### 후보 글 (복사 대상)
- [1] 비트코인 핵심 흐름 해설 | keyword=bitcoin | score=120.0 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- [8] 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조 | keyword=seo_bitcoin_4 | score=119.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-비트코인-핵심-흐름-초보자-가이드-지금-꼭-알아야-할-핵심-구조.html`
- [10] 비트코인 핵심 흐름 ETF·규제 이슈 정리 | keyword=seo_bitcoin_6 | score=116.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-비트코인-핵심-흐름-etf-규제-이슈-정리.html`
- [12] 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리 | keyword=seo_bitcoin_8 | score=113.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/06-비트코인-핵심-흐름-faq-10개-많이-헷갈리는-질문-정리.html`

### 티스토리 (수동)
- reason: 운영 정책상 수동 운영 채널로 분리
- editor_url: `https://www.tistory.com/manage`
- ready: `True`
- mode: `manual`
- ready_item_count: `4`
- ready_command: `open https://www.tistory.com/manage and create a new post with copied html_path content`
- publishing_steps:
  - 1) `html_path`에 적힌 파일을 열어 본문을 복사
  - 2) 티스토리 새 글 작성으로 붙여넣기
  - 3) 썸네일/태그/카테고리를 시장 흐름 중심으로 정렬
  - 발행 후 상단 고정 링크와 관련 글 이동 경로를 점검
  - 문단 구분이 깨지면 HTML 보기에서 한 번 더 줄 바꿈 정리
  - 발행 URL과 대표 키워드를 수기 스프레드시트나 텍스트로 저장
- execution_notes:
  - 티스토리는 수동 채널이라 자동 업로드가 없고, 발행은 사용자가 직접 확인해야 합니다.
  - SEO 글이면 `해시태그`에 핵심 키워드 2~3개만 짧게 넣어 검색 유입을 확보하세요.

#### 후보 글 (복사 대상)
- [1] 비트코인 핵심 흐름 해설 | keyword=bitcoin | score=120.0 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- [8] 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조 | keyword=seo_bitcoin_4 | score=119.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-비트코인-핵심-흐름-초보자-가이드-지금-꼭-알아야-할-핵심-구조.html`
- [10] 비트코인 핵심 흐름 ETF·규제 이슈 정리 | keyword=seo_bitcoin_6 | score=116.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-비트코인-핵심-흐름-etf-규제-이슈-정리.html`
- [12] 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리 | keyword=seo_bitcoin_8 | score=113.5 | quality=pass | date=2026-07-01
  - html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/06-비트코인-핵심-흐름-faq-10개-많이-헷갈리는-질문-정리.html`
