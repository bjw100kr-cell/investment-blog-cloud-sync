# Start Here Runbook

이 문서만 따라가면 첫 로그인부터 첫 자동 채널 테스트 업로드와 GitHub 자동화 연결까지 진행할 수 있습니다.

## 현재 상태

- first_live_status: `ready_for_draft_test`
- github_status: `needs_gh_cli`
- repo_connected: `True`
- missing_credentials_count: `0`

## 자동화 범위

- 지금 당장 자동 운영하는 채널: `blogger`
- 나중에 붙일 두 번째 자동 채널: `wordpress`
- 네이버/티스토리는 현재 자동 발행 범위에서 제외하고 수동 운영 채널로 둡니다.
- 수동 채널 발행은 `cross-platform-publish-pack.md`의 채널별 단계에 따라 순차 진행하세요.
  - 네이버: 복사 -> 붙여넣기 -> 카테고리/태그 설정 -> 발행 -> URL 기록
  - 티스토리: 복사 -> 새 글 작성 -> 썸네일/태그 정리 -> 발행 -> URL 기록

## 지금 바로 할 일

로그인을 마치고 다시 돌아오면 먼저 이 명령을 실행해도 됩니다:
- `python3 scripts/resume_after_login.py`

1. `python3 scripts/check_setup.py`
2. `bash scripts/run_pipeline.sh`
3. 승인된 글이 있다면 자동 채널 draft가 정상 생성됐는지 확인합니다.

## WordPress는 나중에 붙여도 됩니다

- 지금 최소 실행 경로에는 WordPress가 필수가 아닙니다.
- Blogger 실전 검증이 끝난 뒤 두 번째 자동 채널로 확장하면 됩니다.

## OpenAI 키 미입력 모드

- OpenAI 키 없이도 템플릿 fallback 초안으로 일일 업로드를 시작할 수 있습니다.
- 수익성/톤을 더 다듬으려면 `OPENAI_API_KEY`를 나중에 추가하고 같은 파이프라인을 재실행하세요.

## 첫 업로드 목표

- 1차 테스트 글: `비트코인 핵심 흐름 해설`
- 유형: `main_post`
- CTA 포커스: ETF·규제·초보 가이드 글로 연결

## 자동 채널 우선순위

- `blogger`: ready=True / command `python3 scripts/upload_blogger_drafts.py` / approved_ready_items=1
- `wordpress`: ready=False / command `python3 scripts/upload_wordpress_drafts.py` / approved_ready_items=1

## 안전모드 확인

- `BLOGGER_SYNC_SITE_PAGES=false`
- `BLOGGER_SITE_PAGES_PUBLISH=false`
- `BLOGGER_AUTO_PUBLISH_POSTS=true`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=false`
- `BLOGGER_MAX_POSTS_PER_RUN=3`
- `WORDPRESS_AUTO_PUBLISH_POSTS=false`
- `WORDPRESS_PUBLISH_ONLY_DUE_POSTS=true`
- `WORDPRESS_MAX_POSTS_PER_RUN=1`

## 참고 문서

- [first-live-run-plan.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-live-run-plan.md)
- [github-launch-plan.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-launch-plan.md)
- [go-live-dashboard.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/go-live-dashboard.md)
- [platform-publish-plan.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/platform-publish-plan.md)
- [automation-scope.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/automation-scope.md)
- [cross-platform-publish-pack.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/cross-platform-publish-pack.md)
- [current-reference-strategy.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/current-reference-strategy.md)
- [reference-strength-benchmark.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/reference-strength-benchmark.md)
- [keyword-capture-strategy.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/keyword-capture-strategy.md)
- [first-approval-path.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-approval-path.md)
- [daily-revenue-focus.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/daily-revenue-focus.md)
- [traffic-cluster-board.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/traffic-cluster-board.md)
- [popular-reads-board.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/popular-reads-board.md)
- [retention-cta-board.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/retention-cta-board.md)
- [monetization-roadmap.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/monetization-roadmap.md)
- [first-publish-operator-run.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-publish-operator-run.md)
- [user-review-shortlist.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/user-review-shortlist.md)
- [review-preview-board.html](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/review-preview-board.html)
- [operator-home.html](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/operator-home.html)
- [draft-polish-board.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/draft-polish-board.md)
- [pre-publish-quality-gate.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/pre-publish-quality-gate.md)
- [today-operator-console.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/today-operator-console.md)
- [github-web-launch-checklist.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-web-launch-checklist.md)
- [github-minimum-launch-card.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md)
- [cloud-launch-preflight.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/cloud-launch-preflight.md)
- [first-run-values-card.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-run-values-card.md)
- [pipeline-workflow-parity.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/pipeline-workflow-parity.md)
- [first-cloud-run-verification.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-cloud-run-verification.md)
- [operator-handoff.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/operator-handoff.md)
- [success-gate.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/success-gate.md)
