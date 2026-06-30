# User Approval Reply Plan

- reply: `bitcoin 글 먼저 진행`
- clear_enough_to_apply: `True`
- approved_keywords: `bitcoin`
- held_keywords: `none`
- mentioned_but_ambiguous_keywords: `none`
- safety_note: 애매한 답변이면 apply 하지 않고 preview 로 멈춥니다.

## Item States

- `bitcoin` / 비트코인 핵심 흐름 해설 / ready_now `True` / state `approve` / effective `bitcoin` / mode `direct`
- `us_index_flow` / 미국 증시 지수 흐름 해설 / ready_now `True` / state `unmentioned` / effective `us_index_flow` / mode `direct`

## Next Command

- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin --notes "bitcoin 글 먼저 진행"`
