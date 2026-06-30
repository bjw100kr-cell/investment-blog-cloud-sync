# User Approval Rehearsal

자연어 승인 답변이 실제 업로드 전에 어떤 후보 상태를 만들지 안전하게 미리 보는 리허설입니다.

- reply: `FOMC 메인 말고 SEO 후속 글로 전환`
- clear_enough_to_apply: `True`
- approved_keywords: `seo_fomc_1`
- held_keywords: `none`
- ambiguous_keywords: `none`
- safety_note: 이 리허설은 approval plan만 해석하고, 실제 review-approvals.json이나 Blogger 업로드 상태는 바꾸지 않습니다.

## Preview Command

- command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply FOMC 메인 말고 SEO 후속 글로 전환`
- returncode: `0`
- stdout: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/user-approval-reply-plan.md`

## Candidate Outcomes

- `seo_fomc_1` / FOMC 이후 시장이 주식과 코인에 미치는 영향 / seo_followup / quality `review_before_publish` / freshness `` / predicted `blocked` / reason `pre_publish_quality_gate_review`
