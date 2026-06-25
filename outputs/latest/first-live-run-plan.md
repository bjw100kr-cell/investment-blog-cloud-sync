# First Live Run Plan

- status: `awaiting_credentials`
- missing_credentials_count: `3`
- manifest_candidate_count: `9`
- max_posts_per_run: `1`

## Missing Credentials

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`

## Optional Credentials
- `OPENAI_API_KEY` (문구 품질 향상)

## Safe Mode Env

- `BLOGGER_SYNC_SITE_PAGES=true`
- `BLOGGER_SITE_PAGES_PUBLISH=false`
- `BLOGGER_AUTO_PUBLISH_POSTS=false`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`
- `BLOGGER_MAX_POSTS_PER_RUN=1`

## First Upload Candidate

- title: `FOMC 이후 시장 해설`
- inventory_type: `main_post`
- publish_date: ``
- priority_score: `136.0`
- cta_focus: 환율·금리·미국증시 evergreen 글로 연결

## Next Candidates

- `비트코인 핵심 흐름 해설` / main_post / score 131.0
- `CPI 발표 이후 시장 해설` / main_post / score 104.0
- `FOMC 이후 시장이 주식과 코인에 미치는 영향` / seo_followup / score 134.66

## Dry Run Snapshot

- reason: `GOOGLE_CLIENT_ID is not set`
- first_item_reason: `credentials_missing_dry_run`

## Step Sequence

1. 필수 계정 연결 [pending]
   - GOOGLE_CLIENT_ID
   - GOOGLE_CLIENT_SECRET
   - GOOGLE_REFRESH_TOKEN
2. 안전모드 유지 [done]
   - BLOGGER_SYNC_SITE_PAGES=true
   - BLOGGER_SITE_PAGES_PUBLISH=false
   - BLOGGER_AUTO_PUBLISH_POSTS=false
   - BLOGGER_PUBLISH_ONLY_DUE_POSTS=true
   - BLOGGER_MAX_POSTS_PER_RUN=1
3. 첫 테스트 업로드 [pending]
   - 대상 글: FOMC 이후 시장 해설
   - 업로드 유형: main_post
   - 권장 액션: Blogger 초안으로 1개만 업로드 후 화면 검수
4. Blogger 화면 검수 [pending]
   - 제목/본문/라벨/내부링크가 정상인지 확인
   - 고정 페이지가 draft 상태로 잘 들어가는지 확인
   - 문제 없으면 다음날부터 max_posts_per_run을 2~3으로 점진 확대

## Recommended Command

- `python3 scripts/upload_blogger_drafts.py`
- 실행 전 Blogger/Google OAuth 값이 `.env`에 들어가 있어야 합니다.
