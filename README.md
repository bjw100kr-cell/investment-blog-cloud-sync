# Investment Blog Cloud Sync

컴퓨터가 꺼져 있어도 돌 수 있게 만든 무료 클라우드 자동화 뼈대입니다.

## 모델 효율 운영 규칙

이 프로젝트는 가능한 적은 크레딧으로 많은 작업을 처리하는 것을 목표로 합니다.

- 상위 모델(`GPT-5.5`, `GPT-5.4`급)은 설계, 아키텍처, 복잡한 디버깅, 중요한 의사결정, `Task Queue` 생성에 집중합니다.
- Spark(`GPT-5.3 Spark`)는 `TASK_QUEUE.md`에 정의된 TODO, 단순 구현, 문서 작성, 테스트, 반복 작업을 수행합니다.
- Spark 크레딧이 없으면 `GPT-5.4`가 Spark 역할을 대신 수행하되, 이때도 새 설계 결정 없이 `TASK_QUEUE.md`에 있는 작업만 처리합니다.
- 모든 세션은 종료 전에 다음 상위 모델 세션용 `HANDOFF.md`를 갱신합니다.

운영 기준 파일:

- `MODEL_EFFICIENCY_POLICY.md`
- `TASK_QUEUE.md`
- `HANDOFF.md`

## 무엇을 하나

- Google Trends KR/US 수집
- Google Trends 급상승 검색어를 별도 검색 수요 리포트로 정리
- Federal Reserve 통화정책 피드 수집
- CoinDesk RSS 수집
- CNBC / FT / Reuters 관련 RSS 수집
- 무역킹 / FT 유튜브 채널 신규 업로드 수집
- 가능하면 유튜브 transcript까지 가져와 핵심 설명 포인트 요약
- 상위 키워드와 오늘의 글감 후보 생성
- 주제 점수표 기준 오늘의 포스팅 브리프 생성
- 블로그 초안용 draft packet 생성
- 7일 편집 캘린더 자동 생성
- 선택적으로 OpenAI API 기반 Markdown 초안 생성
- 선택적으로 Blogger draft 업로드
- 선택적으로 WordPress draft 업로드
- 결과를 `outputs/latest/`에 저장
- GitHub Actions가 실행 후 결과를 자동 커밋
- GitHub Actions에서도 review approval이 비어 있으면 실제 업로드는 자동으로 보류

## 왜 GitHub Actions인가

- 컴퓨터가 꺼져 있어도 실행 가능
- GitHub Free에서도 가볍게 돌리기 좋음
- 하루 1~2회 수집 정도는 매우 가벼운 편
- 결과 파일이 리포지토리에 남아서 히스토리 추적 가능

## 완전 무료에 가깝게 운영하려면

- 가장 유리한 선택은 `public repository`
- GitHub 공식 문서 기준, public 저장소의 표준 GitHub-hosted runner는 무료
- private 저장소는 GitHub Free에서도 월 무료 Actions 분수 제한이 있음

실무 추천:

- 공개 가능한 수집기만 먼저 public repo로 운영
- 네이버 데이터랩 같은 비밀키를 붙이기 시작하면 private 전환 여부를 판단
- OpenAI API 초안 생성은 기본 비활성 상태로 두는 것이 비용 관리에 유리

## 현재 스케줄

- UTC 00:00
- UTC 12:00

한국 시간으로는 보통:

- 오전 9시
- 오후 9시

원하면 `매일 1회` 또는 `하루 2회 이상`으로 늘릴 수 있지만, 무료 가동을 기준으로는 현재 설정도 충분히 안정적입니다.

## 폴더 구조

- `.env.example`
- `data/performance_signals.example.csv`
- `data/search_console_queries.example.csv`
- `scripts/collect_investment_sources.py`
- `scripts/fetch_search_console_queries.py`
- `scripts/build_search_demand_report.py`
- `scripts/compile_performance_feedback.py`
- `scripts/search_console_to_feedback.py`
- `scripts/score_daily_topics.py`
- `scripts/build_draft_packets.py`
- `scripts/build_editorial_calendar.py`
- `scripts/generate_blog_drafts.py`
- `scripts/review_human_tone.py`
- `scripts/render_publish_ready_posts.py`
- `scripts/generate_growth_report.py`
- `scripts/build_publish_queue.py`
- `scripts/build_keyword_opportunity_board.py`
- `scripts/prepare_first_live_run_plan.py`
- `scripts/build_monetization_readiness_report.py`
- `scripts/analyze_seed_youtube_videos.py`
- `scripts/build_seo_backlog.py`
- `scripts/build_seo_draft_packets.py`
- `scripts/generate_seo_blog_drafts.py`
- `scripts/generate_seo_publishing_assets.py`
- `scripts/render_seo_publish_ready_posts.py`
- `scripts/build_publish_inventory.py`
- `scripts/build_distribution_pack.py`
- `scripts/upload_blogger_drafts.py`
- `scripts/run_pipeline.sh`
- `scripts/prepare_initial_commit.sh`
- `scripts/bootstrap_github_remote.sh`
- `scripts/prepare_github_launch_plan.py`
- `scripts/prepare_start_here_runbook.py`
- `scripts/resume_after_login.py`
- `scripts/build_success_gate.py`
- `scripts/check_setup.py`
- `scripts/generate_operator_handoff.py`
- `scripts/get_google_refresh_token.py`
- `scripts/bootstrap_google_oauth_credentials.py`
- `scripts/export_secrets_checklist.py`
- `scripts/generate_site_foundation.py`
- `scripts/render_site_foundation_pages.py`
- `scripts/build_site_page_publish_plan.py`
- `scripts/generate_publishing_assets.py`
- `scripts/sync_blogger_site_pages.py`
- `scripts/build_go_live_readiness_report.py`
- `config/investment_sources.json`
- `config/human_voice_rules.json`
- `config/human_voice_examples.json`
- `config/growth_rules.json`
- `config/blog_rendering.json`
- `config/seed_youtube_videos.json`
- `config/site_foundation.json`
- `config/publishing_rules.json`
- `templates/investment_blog_draft_prompt.md`
- `templates/sample_post_macro_explainer.md`
- `templates/sample_post_crypto_analysis.md`
- `templates/sample_post_sector_analysis.md`
- `.github/workflows/daily-investment-intake.yml`
- `outputs/latest/`
- `outputs/latest/site-pages/`
- `outputs/latest/site-page-publish-plan.json`

## 유튜브 transcript 수집

유튜브 소스는 제목만 보는 것보다, 실제로 어떤 설명을 했는지까지 반영하는 편이 글감 품질에 더 유리합니다.

현재 동작:

- YouTube RSS로 신규 업로드 감지
- 가능하면 transcript 자동 수집
- transcript에서 핵심 문장 digest 생성
- digest를 포스팅 브리프와 draft packet에 반영

주의:

- transcript는 참고 해설 포인트로만 사용
- 가격, 수치, 규제, 일정 등 핵심 사실은 본문 작성 전에 반드시 공식 자료나 신뢰 가능한 원문으로 다시 확인
- cloud 환경에서는 YouTube가 transcript 요청을 막을 수 있어, GitHub Actions에서는 일부 영상 transcript가 비어 있을 수 있음

## 시드 영상 학습

초기 참고 유튜브 영상 2개 같은 수동 시드 자료는 별도 분석 파일로 남길 수 있습니다.

실행:

```bash
python3 scripts/analyze_seed_youtube_videos.py
```

출력:

- `outputs/latest/seed-video-analysis.json`
- `outputs/latest/seed-video-analysis.md`

## 바로 실행하는 방법

### 0. 자동화 전용 시작 경로(권장)

1. `python3 scripts/check_setup.py`  
2. 값 보완 후 `bash scripts/run_pipeline.sh`  
3. `outputs/latest/operator-home.html` 또는 `outputs/latest/start-here-runbook.md`에서 blocker와 다음 단일 액션만 확인  

이 경로는 하루 자동 스케줄 동작과 같은 단계라, 컴퓨터를 켜 두지 않아도 운영 상태를 일관되게 유지하기 위해 우선순위를 맞춰둔 순서입니다.

### 1. 이 폴더를 별도 GitHub 리포지토리로 올리기

권장 리포지토리 이름 예시:

- `investment-blog-cloud-sync`

로컬에서 첫 커밋을 만들 때는:

- `bash scripts/prepare_initial_commit.sh`

원격 연결과 첫 푸시는:

- `bash scripts/bootstrap_github_repo.py <OWNER/REPO>`

이 명령은 `GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_PAT` 중 하나가 있으면
레포 생성 + 원격 연결 + 첫 푸시까지 한번에 시도합니다. 토큰이 없으면 
`https://github.com/new` 에서 레포만 먼저 만든 뒤 기존 방식으로 등록하세요.

기존 방식(토큰/브라우저 직접):

```bash
export GITHUB_TOKEN=ghp_...
bash scripts/bootstrap_github_remote.sh yourname/investment-blog-cloud-sync
```

`GITHUB_TOKEN` 대신 `GH_TOKEN` 또는 `GITHUB_PAT`도 사용 가능합니다.

배포 전 로컬 점검은:

- `python3 scripts/check_setup.py`

Google refresh token 발급 헬퍼:

- `python3 scripts/get_google_refresh_token.py`

다운로드한 Google OAuth client JSON 자동 탐지/반영:

- `python3 scripts/bootstrap_google_oauth_credentials.py`

GitHub Secrets 체크리스트 생성:

- `python3 scripts/export_secrets_checklist.py`

`.env` 값을 GitHub Actions Secrets / Variables로 옮기는 `gh` CLI 스크립트 생성:

- `python3 scripts/export_github_actions_sync_commands.py`

`gh`가 설치돼 있지 않으면 `outputs/latest/github-web-launch-checklist.md`에 있는
GitHub UI 입력 가이드를 그대로 사용해 Secrets/Variables를 복붙으로 등록하세요.

GitHub 저장소 연결부터 Actions 첫 실행까지 실행계획서 생성:

- `python3 scripts/prepare_github_launch_plan.py`

로그인 이후 실제 순서만 짧게 정리한 시작 런북 생성:

- `python3 scripts/prepare_start_here_runbook.py`

로그인 뒤 자동으로 이어서 점검/반영/문서 갱신을 다시 돌리는 재개 헬퍼:

- `python3 scripts/resume_after_login.py`

현재 로그인/커밋/연결 상태를 초록불/대기 상태로 바로 판정하는 success gate:

- `python3 scripts/build_success_gate.py`

운영자 전달용 핸드오프 문서 생성:

- `python3 scripts/generate_operator_handoff.py`

런칭 전환용 체크리스트/대시보드/핸드오프를 한 번에 새로 생성:

- `python3 scripts/prepare_launch_bundle.py`

사이트 기반 페이지 생성:

- `python3 scripts/generate_site_foundation.py`

퍼블리싱 자산 생성:

- `python3 scripts/generate_publishing_assets.py`

메인 글에서 이어질 SEO/수익화 후속 글 백로그 생성:

- `python3 scripts/build_seo_backlog.py`

후속 글을 바로 초안 생성에 쓸 수 있는 packet으로 변환:

- `python3 scripts/build_seo_draft_packets.py`

SEO 후속 글 packet을 실제 Markdown 초안으로 생성:

- `python3 scripts/generate_seo_blog_drafts.py`

SEO 후속 글도 메타 정보와 발행 직전 HTML까지 미리 생성:

- `python3 scripts/generate_seo_publishing_assets.py`
- `python3 scripts/render_seo_publish_ready_posts.py`

메인 글과 SEO 후속 글을 합친 전체 발행 재고판 생성:

- `python3 scripts/build_publish_inventory.py`

발행 직후 X/텔레그램/커뮤니티/뉴스레터에 바로 쓸 배포 문구 팩 생성:

- `python3 scripts/build_distribution_pack.py`

첫 라이브 업로드를 안전모드 기준으로 어떻게 시작할지 실행계획서 생성:

- `python3 scripts/prepare_first_live_run_plan.py`

오늘 바로 쓸 글, 검색형 후속 글, 미매핑 급상승 쿼리를 한 번에 보는 기회판 생성:

- `python3 scripts/build_keyword_opportunity_board.py`

### 로컬 테스트 빠른 시작

1. `.env.example`을 복사해 `.env` 생성
2. 필요한 값만 채우기
3. 실행:

```bash
bash scripts/run_pipeline.sh
```

검토 후에만 업로드하려면:

```bash
python3 scripts/build_review_packet.py
python3 scripts/set_review_approvals.py --keywords fomc bitcoin
python3 scripts/upload_blogger_drafts.py
```

WordPress 초안 채널까지 같이 쓰려면:

```bash
python3 scripts/build_review_packet.py
python3 scripts/set_review_approvals.py --keywords us_big_tech seo_us_big_tech_7
python3 scripts/upload_wordpress_drafts.py
```

전체 승인으로 한 번에 올리려면:

```bash
python3 scripts/set_review_approvals.py --all
python3 scripts/upload_blogger_drafts.py
```

키가 없어도:

- 수집
- 무료 트렌드 수요 리포트 생성
- Search Console fetch/변환/성과 피드백 반영
- 점수화
- draft packet 생성
- 7일 편집 캘린더 생성
- 초안/업로드 skip 리포트
- 사람 느낌 문체 점검 리포트
- 사이트 기반 페이지 자동 생성
- 퍼블리싱 메타 자산 자동 생성
- 발행용 HTML 패키지 자동 생성
- 성장/수익화 전략 리포트 자동 생성
- 발행 우선순위 큐 자동 생성
- 수익화 준비도 리포트 자동 생성
- 라이브 오픈 준비도 리포트 자동 생성

까지는 확인할 수 있습니다.

## 로그인/연동 빠른 가이드 (1회만)

### 1) Blogger 업로드용 Google OAuth 클라이언트 생성

1. Google Cloud Console에서 프로젝트를 열고, `APIs 및 서비스 → OAuth 동의 화면`에서 앱 이름/이메일을 설정합니다.
2. `API 라이브러리`에서 `Blogger API`를 활성화합니다.
3. 같은 프로젝트에서 `사용자 인증 정보`로 이동해 `OAuth 클라이언트 ID`를 생성합니다.
   - 애플리케이션 유형: 웹 애플리케이션
   - 승인된 리디렉션 URI: `http://127.0.0.1:8765/oauth2callback`
4. 생성된 Client ID/Secret을 `.env`에 입력합니다.

클라이언트 JSON 파일을 내려받았다면 수동 입력 대신 바로 가져올 수 있습니다.

```bash
python3 scripts/find_google_oauth_client.py
python3 scripts/import_google_oauth_client.py /path/to/client_secret_<id>.json
```

자동 탐지된 경로를 먼저 보고 싶지 않고, 바로 찾은 첫 후보로 가져오려면 아래 리포트에서 경로를 확인하면 됩니다.

```bash
open outputs/latest/google-oauth-client-discovery.md
```

직접 파일 경로를 안다면:

```bash
python3 scripts/import_google_oauth_client.py /path/to/client_secret_<id>.json
```

### 2) Refresh token 발급

1. `.env`에 아래 값을 둡니다.
   - `GOOGLE_REDIRECT_URI=http://127.0.0.1:8765/oauth2callback`
   - `GOOGLE_OAUTH_OPEN_BROWSER=true` (원하면 브라우저 자동 열기)
2. `python3 scripts/get_google_refresh_token.py` 실행
3. 표시되는 URL로 로그인/동의 후, 터미널에 출력된 `GOOGLE_REFRESH_TOKEN` 값을 복사해 `.env`에 넣습니다.

브라우저를 바로 띄우고 싶다면 아래처럼 실행하세요.

```bash
GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py
```

리프레시 토큰까지 자동 반영하려면:

```bash
python3 scripts/apply_google_oauth_result.py
```

반대로, URL만 보고 수동으로 열고 싶다면 `GOOGLE_OAUTH_OPEN_BROWSER=false`로 두고 터미널에 뜨는 인증 URL을 그대로 접속하면 됩니다.

### 3) 안전 모드 업로드 설정

컴퓨터가 꺼져도 매일 스케줄러가 실행되도록 `workflow`는 이미 구성되어 있습니다.
초기에는 Draft 동기화만 하도록 아래 값으로 두세요.

- `BLOGGER_AUTO_PUBLISH_POSTS=false`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`
- `BLOGGER_MAX_POSTS_PER_RUN=1`
- `BLOGGER_SYNC_SITE_PAGES=false`
- `BLOGGER_SITE_PAGES_PUBLISH=false`

### 4) GitHub Actions 시크릿/변수 입력

`GitHub → Settings → Secrets and variables → Actions`에서 다음을 최소 한 번 입력합니다.

- 필수: `BLOGGER_BLOG_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`
- 추천: `OPENAI_API_KEY`, `SEARCH_CONSOLE_*`, `NAVER_CLIENT_ID/SECRET`, `GA4_MEASUREMENT_ID`, AdSense 값

## 사람처럼 쓰는 톤 규칙

이 프로젝트는 단순히 키워드만 넣는 초안 생성기가 아니라,
사람이 실제로 시장을 설명해 주는 듯한 해설형 글을 목표로 합니다.

현재 자동 점검 포인트:

- 도입부 초반에 독자 관점 문장이 들어가는지
- 숫자 뒤에 해석 문장이 붙는지
- 독자에게 직접 말 거는 표현이 충분한지
- 같은 문장 어미가 과하게 반복되지 않는지
- AI스러운 관용 문구가 들어갔는지

관련 파일:

- `config/human_voice_rules.json`
- `config/human_voice_examples.json`
- `templates/investment_blog_draft_prompt.md`
- `scripts/review_human_tone.py`

## 성장 리포트

매일 수집 결과를 바탕으로 어떤 카테고리를 더 밀지, 어떤 검색 키워드를 evergreen 글로 확장할지,
문체 품질은 어느 정도인지까지 자동 요약합니다.

출력 파일:

- `outputs/latest/growth-report.json`
- `outputs/latest/growth-report.md`

## 검색 수요 신호

Search Console 데이터가 아직 없더라도, Google Trends KR/US 급상승 검색어를 따로 모아서
"오늘 실제로 검색이 튀는 쿼리"를 볼 수 있게 해둡니다.

출력 파일:

- `outputs/latest/search-demand-report.json`

## 오픈AI 없이도 첫 발행 준비

초안 생성은 OpenAI 키가 없어도 동작합니다. `generate_blog_drafts.py`는
`OPENAI_API_KEY`가 없으면 템플릿 기반 글을 생성하고, 그래도 다음 단계(`review_human_tone`, `render_publish_ready_posts`)는 정상적으로 진행됩니다.

`outputs/latest/publish-ready-report.json`에 `ready`가 true인 항목이 1개 이상이면
Blogger 업로드/작성용 HTML 패킷은 바로 준비됩니다.

## 로그인(필수 연동) 가이드

로그인이 필요한 항목은 Google OAuth입니다. 로그인 창은 아래 흐름에서 `Google 계정 로그인` 화면으로 열립니다.

1) Google Cloud OAuth 동의 화면 + Blogger API 승인 화면
2) 로그인 동의 완료 후 로컬 콜백(`http://127.0.0.1:8765/oauth2callback`)
3) 리프레시 토큰 발급 완료

필요한 로그인/설정 페이지를 먼저 정리만 하려면:

```bash
python3 scripts/open_login_setup_pages.py
```

브라우저 탭까지 한 번에 열고 싶다면:

```bash
python3 scripts/open_login_setup_pages.py --open
```

`--open`은 최소 경로만 열고, 한 번에 여러 탭이 필요하면 `--open-all`을 사용하세요.

```bash
python3 scripts/open_login_setup_pages.py --open-all
```

한 개씩 순차적으로 열고 싶다면:

```bash
python3 scripts/open_login_setup_pages.py --open-next
```

로그인 화면을 바로 띄우려면:

```bash
GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py
```

토큰 발급 후 `outputs/latest/google-oauth-token-result.json` 값을 `.env`에 자동 반영하려면:

```bash
python3 scripts/apply_google_oauth_result.py
```

브라우저를 직접 열어야 한다면 같은 명령을 실행했을 때 출력되는 URL을 그대로 복사해 접속하면 됩니다.

출력되는 `GOOGLE_REFRESH_TOKEN=...` 값은 `.env`와 GitHub Actions Secret에 각각 저장합니다.

 - `.env`에 추가: `GOOGLE_REFRESH_TOKEN=<토큰>`
 - GitHub Secret에 추가: `GOOGLE_REFRESH_TOKEN=<토큰>`

활용 방식:

- 우리 핵심 키워드에 직접 매핑된 급상승 검색어는 점수에 보너스를 줌
- 매칭되지 않은 시장성 트렌드는 `unmatched_market_trends`로 잡혀도 바로 브리프/큐 보강에 사용
- Search Console이 쌓이기 전에도 급상승 트렌드로 매일 포스팅 후보를 유지

## 발행 우선순위 큐

실제 운영에서는 글을 모두 한 번에 쓰는 것보다,
어떤 글을 먼저 draft로 올리고 어떤 글을 evergreen 후속으로 묶을지가 더 중요합니다.

이 프로젝트는 `build_publish_queue.py`로 다음을 자동 정리합니다.

- 업로드 순서
- 오늘/내일/이번 주 발행 버킷
- 글 역할: 속보, evergreen, 후속, 주간회고
- 수익화 목표: 검색 유입, 재방문, 체류시간 등
- 추천 광고 슬롯
- CTA 초점

출력 파일:

- `outputs/latest/publish-queue.json`
- `outputs/latest/publish-queue.md`

추가로 Blogger 업로드 스크립트는 이 큐 순서를 읽어서 draft 업로드 순서를 맞춥니다.

## 신뢰 페이지 HTML export

`About`, `Disclosure`, `Privacy`, `Editorial`, `Contact` 같은 기반 페이지는
광고 승인과 운영 신뢰도에 중요합니다.

`render_site_foundation_pages.py`는 `outputs/latest/site-foundation/*.md`를
실제 블로그에 붙이기 쉬운 HTML 자산으로 변환합니다.

출력 파일:

- `outputs/latest/site-pages/*.html`
- `outputs/latest/site-pages-report.json`
- `outputs/latest/site-pages-report.md`

## 사이트 페이지 배포 플랜

신뢰 페이지와 허브 페이지를 다 만들었다고 끝이 아니라,
실제 블로그 정적 페이지로 어떤 순서로 먼저 올릴지도 중요합니다.

`build_site_page_publish_plan.py`는 다음을 정리합니다.

- 페이지별 업로드 순서
- trust page / hub page 구분
- 필수 공개 여부
- 각 페이지의 목적

출력 파일:

- `outputs/latest/site-page-publish-plan.json`
- `outputs/latest/site-page-publish-plan.md`

## 수익화 준비도 리포트

수익형 블로그는 글만 쌓는다고 끝나지 않고,
발행, 검색 수요, 분석, 광고, 재방문 수단이 어느 정도 준비됐는지 같이 봐야 합니다.

`build_monetization_readiness_report.py`는 다음을 자동 점검합니다.

- 콘텐츠 엔진 준비 상태
- Blogger 발행 엔진 준비 상태
- 검색 수요 엔진 준비 상태
- GA4 분석 준비 상태
- AdSense 준비 상태
- 뉴스레터/재방문 수단 준비 상태

출력 파일:

- `outputs/latest/monetization-readiness-report.json`
- `outputs/latest/monetization-readiness-report.md`

## 발행용 패키지

Markdown 초안이 실제로 생성되면, 업로드 직전에 발행용 HTML 패키지로 한 번 더 정리합니다.

현재 포함 요소:

- 메타 제목
- 메타 설명
- 작성자/발행일 박스
- 안내 문구
- 내부 링크 목록
- Blogger 업로드용 HTML 본문

출력 파일:

- `outputs/latest/publish-ready/*.html`
- `outputs/latest/publish-ready/*.json`
- `outputs/latest/publish-ready-report.json`
- `outputs/latest/publish-ready-report.md`

### 2. GitHub Actions 활성화

- 리포지토리의 `Actions` 탭에서 워크플로 허용

### 2-1. 꼭 기억할 점

- 로컬 `.env` 값은 GitHub Secrets로 자동 복사되지 않음
- GitHub에서 직접 `Settings -> Secrets and variables -> Actions` 로 넣어야 함
- 무료 운영을 우선하면 public repo가 가장 단순함

### 3. 선택: 네이버 데이터랩 비밀값 추가

없어도 기본 수집은 돌아갑니다.

있으면 한국 검색 보정이 더 좋아집니다.

필요한 Secrets:

- `NAVER_CLIENT_ID`
- `NAVER_CLIENT_SECRET`

### 3-1. 선택: 성과 피드백 CSV 추가

Search Console이나 수동 성과 기록을 아래 형식으로 넣으면,
다음 글감 점수에 `performance bonus`가 붙습니다.

기본 예시:

- `data/performance_signals.example.csv`
- `data/search_console_queries.example.csv`

실제 사용 파일 이름:

- `data/performance_signals.csv`

Search Console export에서 바로 변환하려면:

1. `data/search_console_queries.example.csv` 형식을 참고해
2. 실제 export를 `data/search_console_queries.csv`로 저장
3. 변환:

```bash
python3 scripts/search_console_to_feedback.py
```

### 3-2. 선택: Search Console API 직접 연결

Search Console API를 직접 연결하면 `search_console_queries.csv`를 자동으로 가져올 수 있습니다.

필요한 Secrets / Variables:

- `SEARCH_CONSOLE_SITE_URL`
- `SEARCH_CONSOLE_CLIENT_ID`
- `SEARCH_CONSOLE_CLIENT_SECRET`
- `SEARCH_CONSOLE_REFRESH_TOKEN`
- `SEARCH_CONSOLE_LAG_DAYS` (기본 3)
- `SEARCH_CONSOLE_WINDOW_DAYS` (기본 7)

로컬 테스트:

```bash
python3 scripts/fetch_search_console_queries.py
```

### 4. 선택: OpenAI 초안 생성 비밀값 추가

없어도 기본 루프는 모두 동작합니다.

있으면 `draft packet -> 실제 Markdown 초안`까지 자동 생성할 수 있습니다.

필요한 Secrets / Variables:

- `OPENAI_API_KEY` (Secret)
- `OPENAI_MODEL` (Variable, 선택. 기본값 `gpt-5.4-mini`)

### 5. 선택: Blogger draft 업로드 비밀값 추가

없어도 기본 루프는 모두 동작합니다.

있으면 생성된 초안을 Blogger에 `draft` 상태로 올릴 수 있습니다.

필요한 Secrets / Variables:

- `BLOGGER_BLOG_ID`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`
- `BLOGGER_SYNC_SITE_PAGES` (Variable, 선택. `true`면 trust/hub 페이지도 동기화)
- `BLOGGER_SITE_PAGES_PUBLISH` (Variable, 선택. `true`면 정적 페이지 publish까지 진행)
- `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES` (Variable, 선택. 기본은 optional 페이지 skip)
- `BLOGGER_AUTO_PUBLISH_POSTS` (Variable, 선택. `true`면 draft 업로드 후 실제 공개까지 진행)
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS` (Variable, 선택. 기본 `true`, 추천 발행일이 지난 글만 공개)
- `BLOGGER_MAX_POSTS_PER_RUN` (Variable, 선택. 기본 `1`, 한 번 실행당 최대 공개/업데이트 개수 제한)

또는 이미 발급한 액세스 토큰을 잠깐 테스트할 때:

- `GOOGLE_ACCESS_TOKEN`

### 5-1. Google refresh token 발급 방법

이 프로젝트는 Blogger와 Search Console 모두 Google OAuth 2.0 refresh token 기반으로 연결할 수 있습니다.

사전 준비:

1. Google Cloud 프로젝트 생성
2. `Blogger API v3`
3. `Search Console API`
4. OAuth 동의 화면 설정
5. OAuth Client ID 생성

권장 클라이언트 유형:

- `Web application`

권장 Redirect URI:

- `http://127.0.0.1:8765/oauth2callback`

그 다음 `.env` 또는 환경변수에 아래를 넣습니다.

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REDIRECT_URI=http://127.0.0.1:8765/oauth2callback`
- `GOOGLE_OAUTH_PRESET=combined`

실행:

```bash
python3 scripts/get_google_refresh_token.py
```

이 스크립트는:

- 로컬 loopback 주소에서 OAuth callback 대기
- 승인 URL 출력
- 승인 후 authorization code를 access token / refresh token으로 교환
- 결과를 `outputs/latest/google-oauth-token-result.json` 에 저장

성공 시 넣을 값:

- `GOOGLE_REFRESH_TOKEN`
- `SEARCH_CONSOLE_REFRESH_TOKEN` (같은 토큰 재사용 가능)

참고:

- refresh token이 안 나오면 같은 OAuth client로 이미 동의했던 계정일 수 있음
- 그 경우 앱 권한을 철회한 뒤 다시 실행하거나, 다른 OAuth client를 써서 다시 동의해야 할 수 있음

### 5-2. GitHub Secrets 입력 체크리스트 생성

```bash
python3 scripts/export_secrets_checklist.py
```

생성 파일:

- `outputs/latest/github-secrets-checklist.md`

### 5-3. Blogger 신뢰 페이지 동기화

글 draft만 올라가면 아직 블로그 운영 기본 뼈대가 비어 보일 수 있어서,
`About`, `Disclosure`, `Privacy`, `Editorial`, `Contact` 같은 정적 페이지도 별도로 올릴 수 있게 해두었습니다.

기본 원칙:

- 기본값은 비활성
- `BLOGGER_SYNC_SITE_PAGES=true`일 때만 실행
- 첫 연결은 `BLOGGER_SITE_PAGES_PUBLISH=false`로 draft/update 검증부터 권장
- 확인 후 `BLOGGER_SITE_PAGES_PUBLISH=true`로 공개 전환

실행:

```bash
python3 scripts/sync_blogger_site_pages.py
```

결과:

- `outputs/latest/blogger-site-pages-report.json`

### 5-4. 라이브 오픈 준비도 리포트

실제 로그인 직전에 "지금 바로 첫 업로드 가능한 상태인지"를 한눈에 보기 위한 리포트입니다.

실행:

```bash
python3 scripts/build_go_live_readiness_report.py
```

결과:

- `outputs/latest/go-live-readiness-report.json`
- `outputs/latest/go-live-readiness-report.md`

### 5-5. Blogger 자동 발행 안전장치

매일 글이 올라가게 하려면 `draft 업로드`만으로는 부족해서,
실제 공개용 스위치를 별도로 두는 편이 안전합니다.

권장 초기값:

- `BLOGGER_AUTO_PUBLISH_POSTS=false`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`
- `BLOGGER_MAX_POSTS_PER_RUN=1`

이 설정이면:

- 같은 글을 스케줄이 돌 때마다 중복 draft로 올리지 않음
- 이미 올린 동일 콘텐츠는 state 파일 기준으로 skip
- 하루에 한 번 최대 1개 글만 공개되도록 제한 가능
- 추천 발행일이 아직 안 된 글은 draft 상태로만 유지 가능

### 5-6. 운영 자동 모드 (확인 자동화)

원할 때는 초기 안전 장치를 끄고 매일 자동 업로드/공개가 되게 운영 모드로 바꿀 수 있습니다.

- `BLOGGER_REQUIRE_REVIEW_APPROVAL=false`
- `BLOGGER_AUTO_PUBLISH_POSTS=true`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=false`
- `BLOGGER_MAX_POSTS_PER_RUN=3` (원하면 5/10으로 조정)
- `BLOGGER_ALLOW_REUPLOAD_SAME_CONTENT=false` (안정 운영은 `false`, 동일 본문까지 강제 재동기화가 필요하면 `true`)

운영 모드에서는 GitHub Actions가 실행될 때마다 리뷰 승인 대기 없이 바로 게시되고,
같은 글은 `outputs/latest/blogger-upload-state.json`의 `content_hash` 기준으로 중복 업로드를 방지합니다.

동일 본문으로 인해 모든 글이 `already_synced_same_content`로 스킵될 때는 새 원고 반영이 없는 상태입니다.
그래도 강제로 최신 상태를 다시 반영하고 싶다면 위 플래그를 `true`로 두고 실행하면
기존 게시글을 content_hash 변경 여부와 무관하게 `update_post`로 재동기화합니다.

관련 산출물:

- `outputs/latest/blogger-upload-report.json`
- `outputs/latest/blogger-upload-state.json`

### 6. 수동 1회 실행

- `Actions`
- `Daily Investment Intake`
- `Run workflow`

### 6-1. 런칭 직전 점검

로컬에서:

```bash
python3 scripts/check_setup.py
```

이 스크립트는 아래를 점검합니다.

- `.env` 존재 여부
- 필수/선택 키 누락 여부
- 현재 git branch / origin 상태
- `outputs/latest/` 생성 여부
- 각 통합 기능의 준비 상태

### 7. 결과 확인

- `outputs/latest/source-snapshot.md`
- `outputs/latest/source-snapshot.json`
- `outputs/latest/search-console-fetch-report.json`
- `outputs/latest/search-console-conversion-report.md`
- `outputs/latest/search-console-conversion-report.json`
- `outputs/latest/performance-feedback.md`
- `outputs/latest/performance-feedback.json`
- `outputs/latest/daily-post-brief.md`
- `outputs/latest/daily-post-brief.json`
- `outputs/latest/draft-packets.md`
- `outputs/latest/draft-packets.json`
- `outputs/latest/editorial-calendar.md`
- `outputs/latest/editorial-calendar.json`
- `outputs/latest/google-oauth-token-result.json`
- `outputs/latest/github-secrets-checklist.md`
- `outputs/latest/human-tone-review.json`
- `outputs/latest/human-tone-review.md`
- `outputs/latest/site-foundation/`
- `outputs/latest/publishing-assets.json`
- `outputs/latest/publishing-assets.md`
- `outputs/latest/prompts/`
- `outputs/latest/drafts/`
- `outputs/latest/draft-generation-report.json`
- `outputs/latest/blogger-upload-report.json`
- `outputs/latest/blogger-upload-state.json`

## 무료 운영 원칙

- 무거운 크롤링 대신 RSS/피드 중심
- 하루 1~2회만 실행
- 결과를 아티팩트가 아니라 git 커밋으로 남겨 추가 저장비용 최소화
- API 키가 꼭 필요하지 않은 공개 소스를 우선 사용

## 매일 포스팅 운영 방식

- `daily-post-brief`는 오늘 강한 뉴스형 글감을 뽑습니다.
- `draft-packets`는 실제 글 쓰기용 구조를 만듭니다.
- `editorial-calendar`는 7일치 속보형 + SEO형 큐를 섞어 줍니다.
- `get_google_refresh_token.py`는 Blogger/Search Console용 refresh token 발급을 돕습니다.
- `github-secrets-checklist.md`는 클라우드 실행용 입력값 누락을 줄여 줍니다.
- `review_human_tone.py`는 초안이 너무 기계적으로 보이지 않는지 점검합니다.
- `human_voice_examples.json`은 실제로 참고할 사람 느낌 문단 예시를 제공합니다.
- `sample_post_*.md` 파일들은 발행 가능한 샘플 글 자산으로, 전체 톤의 기준점 역할을 합니다.
- `generate_site_foundation.py`는 About, 허브 글, 운영 원칙 같은 블로그 기반 페이지를 자동 생성합니다.
- `generate_publishing_assets.py`는 slug, meta description, labels, 내부링크 같은 발행용 자산을 자동 생성합니다.

즉 뉴스가 약한 날에도:

- 설명형 검색 글
- 이전 이슈 후속 글
- 주간 회고형 글

로 일일 발행을 이어갈 수 있습니다.

## 추천 런칭 순서

1. `bash scripts/prepare_initial_commit.sh`
2. `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>`
3. `python3 scripts/check_setup.py`
4. GitHub Secrets 입력
5. GitHub Actions 수동 1회 실행
6. `outputs/latest/` 결과와 커밋 생성 여부 확인

## 한계

- CoinNess는 현재 서버사이드 피드가 확인되지 않아 자동 수집 기본값에 넣지 않았습니다.
- 네이버 데이터랩은 후보 키워드 비교용이라, 완전한 "전체 검색량 순위" 제공 도구는 아닙니다.
- 실제 블로그 유입 최적화는 나중에 Search Console 데이터까지 붙여야 더 정밀해집니다.

## 다음 추천 확장

1. 네이버 데이터랩 API 연결
2. Google Search Console 연결
3. WordPress 초안 업로드와 연결
4. Search Console 실제 유입 키워드와 자동 결합
5. 성과 데이터를 기준으로 주제 점수표 자동 보정 고도화
