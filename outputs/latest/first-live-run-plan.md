# First Live Run Plan

- status: `ready_for_draft_test`
- missing_credentials_count: `0`
- manifest_candidate_count: `0`
- max_posts_per_run: `3`

## Missing Credentials

- 자동 채널 최소 1개 이상 준비되었습니다.

## Optional Credentials
- `OPENAI_API_KEY` (문구 품질 향상)

## Safe Mode Env

- `BLOGGER_SYNC_SITE_PAGES=false`
- `BLOGGER_SITE_PAGES_PUBLISH=false`
- `BLOGGER_AUTO_PUBLISH_POSTS=false`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`
- `BLOGGER_MAX_POSTS_PER_RUN=1`
- `WORDPRESS_AUTO_PUBLISH_POSTS=false`
- `WORDPRESS_PUBLISH_ONLY_DUE_POSTS=true`
- `WORDPRESS_MAX_POSTS_PER_RUN=1`

## First Upload Candidate

- title: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- inventory_type: `main_post`
- publish_date: ``
- priority_score: `124.0`
- cta_focus: ETF·규제·초보 가이드 글로 연결

## Next Candidates

- 다음 후보가 아직 없습니다.

## Dry Run Snapshot

- blogger_reason: ``
- blogger_first_item_reason: `pre_publish_quality_gate_review`
- wordpress_reason: `WORDPRESS_SITE_URL is not set`
- wordpress_first_item_reason: `credentials_missing_dry_run`

## Step Sequence

1. 자동 채널 1개 이상 연결 [done]
   - 자동 채널 준비 상태: blogger=True, wordpress=False
   - 참고: `OPENAI_API_KEY`는 없더라도 템플릿 fallback 초안으로 테스트 업로드가 가능합니다.
2. 안전모드 유지 [done]
   - BLOGGER_SYNC_SITE_PAGES=false
   - BLOGGER_SITE_PAGES_PUBLISH=false
   - BLOGGER_AUTO_PUBLISH_POSTS=false
   - BLOGGER_PUBLISH_ONLY_DUE_POSTS=true
   - BLOGGER_MAX_POSTS_PER_RUN=1
   - WORDPRESS_AUTO_PUBLISH_POSTS=false
   - WORDPRESS_PUBLISH_ONLY_DUE_POSTS=true
   - WORDPRESS_MAX_POSTS_PER_RUN=1
3. 첫 테스트 업로드 [pending]
   - 대상 글: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트
   - 업로드 유형: main_post
   - 권장 채널: blogger
   - 권장 액션: Blogger에서 초안 1개만 업로드 후 화면 검수
4. 발행 화면 검수 [pending]
   - 제목/본문/라벨/내부링크가 정상인지 확인
   - Blogger를 쓰는 경우 고정 페이지가 draft 상태로 잘 들어가는지 확인
   - 문제 없으면 다음날부터 max_posts_per_run을 2~3으로 점진 확대

## Recommended Command

- `python3 scripts/upload_blogger_drafts.py`
- 실행 전 Blogger/Google OAuth 값이 `.env`에 들어가 있어야 합니다.
