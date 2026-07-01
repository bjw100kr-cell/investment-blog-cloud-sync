#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_TRAFFIC_GOAL_JSON = ROOT / "outputs/latest/daily-traffic-goal.json"
DISTRIBUTION_PACK_JSON = ROOT / "outputs/latest/distribution-pack.json"
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
TRAFFIC_CLUSTER_JSON = ROOT / "outputs/latest/traffic-cluster-board.json"
POPULAR_READS_JSON = ROOT / "outputs/latest/popular-reads-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/traffic-amplification-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/traffic-amplification-plan.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def public_url_lookup(state: dict) -> dict:
    items = state.get("items", {})
    if isinstance(items, dict):
        rows = items.values()
    else:
        rows = items if isinstance(items, list) else []
    lookup = {}
    for item in rows:
        keyword = item.get("keyword")
        if keyword and item.get("url"):
            lookup[keyword] = item.get("url")
    return lookup


def published_state_items(state: dict) -> list[dict]:
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    published = []
    for item in rows:
        keyword = item.get("keyword", "")
        url = item.get("url", "")
        if not keyword or not item.get("published") or not url.startswith("http"):
            continue
        published.append(item)
    published.sort(key=lambda item: item.get("last_synced_at", ""), reverse=True)
    return published


def distribution_lookup(pack: dict) -> dict:
    lookup = {}
    for item in pack.get("items", []):
        keyword = item.get("keyword")
        if keyword:
            lookup[keyword] = item
    return lookup


def cluster_lookup(report: dict) -> dict:
    return {item.get("source_keyword"): item for item in report.get("clusters", []) if item.get("source_keyword")}


def popular_lookup(report: dict) -> dict:
    return {item.get("source_keyword"): item for item in report.get("groups", []) if item.get("source_keyword")}


def compact_title(title: str) -> str:
    title = (title or "").strip()
    if len(title) <= 44:
        return title
    for sep in [":", ",", " | "]:
        if sep in title:
            head = title.split(sep, 1)[0].strip()
            if 8 <= len(head) <= 36:
                return head
    return title[:44].rstrip()


def platform_variants(title: str, url: str, keyword: str, channel: str, followups: list[dict]) -> list[dict]:
    short = compact_title(title)
    followup_title = next((item.get("title", "") for item in followups if item.get("title")), "")
    if not followup_title:
        followup_title = "관련 체크포인트 글"

    if channel == "x_threads_or_short_social":
        variants = [
            {
                "label": "question_hook",
                "copy": f"{short}\n\n오늘 시장이 왜 흔들리는지 3분 안에 볼 수 있게 정리했습니다.\n핵심은 가격보다 금리/달러/자금 흐름입니다.\n\n{url}",
            },
            {
                "label": "checklist_hook",
                "copy": f"{short}\n\n체크할 것 3개\n1. 금리/달러\n2. ETF·자금 흐름\n3. 다음 리스크 일정\n\n정리 글: {url}",
            },
            {
                "label": "beginner_hook",
                "copy": f"시장 뉴스는 많은데, 내 계좌에 어떤 의미인지 헷갈릴 때 보기 좋은 글입니다.\n\n{short}\n{url}",
            },
        ]
    elif channel == "telegram_kakao_or_personal_channel":
        variants = [
            {
                "label": "briefing",
                "copy": f"[오늘의 시장 메모]\n{title}\n\n짧게 보면: 가격보다 자금 흐름과 매크로 변수를 먼저 확인하는 구간입니다.\n\n{url}",
            },
            {
                "label": "friendly_note",
                "copy": f"오늘 시장 흐름 헷갈리면 이 글부터 보면 좋습니다.\n\n{short}\n- 왜 반응했는지\n- 무엇을 확인해야 하는지\n- 무리한 해석을 피하는 법\n\n{url}",
            },
            {
                "label": "followup_bridge",
                "copy": f"{short}\n\n읽고 나서 이어서 보면 좋은 흐름: {followup_title}\n먼저 메인 정리부터 확인해보세요.\n\n{url}",
            },
        ]
    else:
        variants = [
            {
                "label": "community_question",
                "copy": f"{title}\n\n요즘 시장 볼 때 저는 가격 자체보다 금리/달러/자금 흐름을 먼저 봐야 한다고 정리했습니다.\n다른 분들은 지금 어떤 지표를 먼저 보시나요?\n\n{url}",
            },
            {
                "label": "community_summary",
                "copy": f"오늘 시장 흐름을 초보자도 읽기 쉽게 정리했습니다.\n\n핵심 질문: 이 이슈가 주식/코인에 왜 같이 영향을 주는가?\n글: {url}",
            },
            {
                "label": "community_caution",
                "copy": f"{short}\n\n단순 전망보다 체크리스트 중심으로 정리했습니다. 매수/매도 추천이 아니라 시장을 읽는 기준을 정리한 글입니다.\n\n{url}",
            },
        ]

    return variants


def build_manual_checklist(public_url: str, share_slots: list[dict]) -> list[dict]:
    checklist = []
    for slot in share_slots:
        if slot.get("blocked_by") or slot.get("channel") in {"blogger_internal", "followup_post"}:
            continue
        variants = slot.get("copy_variants", [])
        checklist.append(
            {
                "done": False,
                "channel": slot.get("channel", ""),
                "time_window": slot.get("time_window", ""),
                "copy_variant_to_use": variants[0].get("label", "default") if variants else "default",
                "url": public_url,
                "expected_visitors": slot.get("potential_visitors_if_executed", 0),
                "note": "한 채널에 1회만 공유하고 반응이 좋은 문구를 다음 글에 재사용합니다.",
            }
        )
    return checklist


def build_share_slots(goal_item: dict, snippets: dict, public_url: str, cluster: dict, popular: dict) -> list[dict]:
    title = goal_item.get("title", "")
    keyword = goal_item.get("keyword", "")
    url_line = public_url or "<PUBLISHED_URL>"
    followups = cluster.get("followups", []) or cluster.get("followup_posts", [])
    popular_picks = popular.get("picks", [])

    base_hook = snippets.get("hook_line") or f"{title} | 오늘 시장 흐름 정리"
    community = snippets.get("community_post") or f"{title}\n\n오늘 시장 흐름을 투자자 관점에서 정리했습니다."
    telegram = snippets.get("telegram_post") or f"{title}\n핵심 체크포인트를 짧게 정리했습니다."
    x_post = snippets.get("x_post") or f"{title}\n\n오늘 시장 핵심만 정리했습니다."
    followup_text = ", ".join(item.get("title", "") for item in followups[:2] if item.get("title"))
    if not followup_text:
        followup_text = f"{keyword} 후속 글 1개를 먼저 생성하거나, 관련 메인 글 1개를 내부링크로 연결"
    popular_text = ", ".join(pick.get("title", "") for pick in popular_picks[:2] if pick.get("title"))
    if not popular_text:
        popular_text = "관련 허브 글과 최신 검색수요 글 2개"

    slots = [
        {
            "time_window": "publish_plus_0m",
            "channel": "blogger_internal",
            "potential_visitors_if_executed": 20,
            "task": "본문 상단과 하단에 같은 클러스터 후속 글 2개를 popular reads로 노출",
            "copy": f"{title} 읽은 뒤 바로 이어볼 글: {popular_text}",
        },
        {
            "time_window": "publish_plus_10m",
            "channel": "x_threads_or_short_social",
            "potential_visitors_if_executed": 10,
            "task": "짧은 훅과 공개 URL 공유",
            "copy": f"{x_post}\n\n{url_line}",
            "copy_variants": platform_variants(title, url_line, keyword, "x_threads_or_short_social", followups),
        },
        {
            "time_window": "publish_plus_30m",
            "channel": "telegram_kakao_or_personal_channel",
            "potential_visitors_if_executed": 10,
            "task": "짧은 브리핑형 공유",
            "copy": f"{telegram}\n\n{url_line}",
            "copy_variants": platform_variants(title, url_line, keyword, "telegram_kakao_or_personal_channel", followups),
        },
        {
            "time_window": "publish_plus_2h",
            "channel": "finance_community",
            "potential_visitors_if_executed": 15,
            "task": "투자 커뮤니티에 질문형 요약으로 공유",
            "copy": f"{community}\n\n질문: 지금은 가격보다 어떤 지표를 먼저 보는 게 맞을까요?\n{url_line}",
            "copy_variants": platform_variants(title, url_line, keyword, "finance_community", followups),
        },
        {
            "time_window": "publish_plus_24h",
            "channel": "followup_post",
            "potential_visitors_if_executed": 20,
            "task": "후속 글 1개를 발행하거나 기존 후속 글을 다시 내부링크",
            "copy": f"{keyword} 후속 글 후보: {followup_text}",
            "needs_followup_generation": not bool(followups),
        },
    ]
    if not public_url:
        for slot in slots:
            slot["blocked_by"] = "public_url_missing"
    return slots


def build_report() -> dict:
    goal = load_json(DAILY_TRAFFIC_GOAL_JSON)
    distribution = load_json(DISTRIBUTION_PACK_JSON)
    blogger_state = load_json(BLOGGER_STATE_JSON)
    clusters = load_json(TRAFFIC_CLUSTER_JSON)
    popular = load_json(POPULAR_READS_JSON)

    urls = public_url_lookup(blogger_state)
    snippets_by_keyword = distribution_lookup(distribution)
    clusters_by_keyword = cluster_lookup(clusters)
    popular_by_keyword = popular_lookup(popular)

    goal_items = list(goal.get("top_path", []))
    seen_keywords = {item.get("keyword", "") for item in goal_items}
    for item in published_state_items(blogger_state):
        keyword = item.get("keyword", "")
        if keyword in seen_keywords:
            continue
        goal_items.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "estimated_daily_visitors": 35 if keyword.startswith("seo_") else 20,
                "source": "published_blogger_state",
            }
        )
        seen_keywords.add(keyword)

    plans = []
    total_expected = 0
    total_potential = 0
    for goal_item in goal_items:
        keyword = goal_item.get("keyword", "")
        public_url = urls.get(keyword, "")
        distribution_item = snippets_by_keyword.get(keyword, {})
        snippets = distribution_item.get("snippets", {})
        share_slots = build_share_slots(
            goal_item,
            snippets,
            public_url,
            clusters_by_keyword.get(keyword, {}),
            popular_by_keyword.get(keyword, {}),
        )
        potential = sum(slot.get("potential_visitors_if_executed", 0) for slot in share_slots if not slot.get("blocked_by"))
        expected = 0
        total_expected += expected
        total_potential += potential
        plans.append(
            {
                "keyword": keyword,
                "title": goal_item.get("title", ""),
                "public_url": public_url,
                "base_estimated_search_visitors": goal_item.get("estimated_daily_visitors", 0),
                "amplification_expected_visitors": expected,
                "amplification_potential_visitors_if_executed": potential,
                "manual_execution_required": True,
                "manual_execution_checklist": build_manual_checklist(public_url, share_slots),
                "share_slots": share_slots,
            }
        )

    target = int(goal.get("target_daily_visitors", 200) or 200)
    projected_total = int(goal.get("projected_daily_visitors", 0) or 0) + total_expected
    potential_total = int(goal.get("projected_daily_visitors", 0) or 0) + total_potential
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_daily_visitors": target,
        "base_projected_visitors": goal.get("projected_daily_visitors", 0),
        "amplification_expected_visitors": total_expected,
        "amplification_potential_visitors_if_executed": total_potential,
        "projected_with_amplification": projected_total,
        "potential_with_manual_amplification": potential_total,
        "gap_after_amplification": max(target - projected_total, 0),
        "status": "amplification_plan_ready_manual_execution_required",
        "planned_public_url_count": len([plan for plan in plans if plan.get("public_url")]),
        "source_goal_item_count": len(goal.get("top_path", [])),
        "published_expansion_item_count": max(len(goal_items) - len(goal.get("top_path", [])), 0),
        "plans": plans,
        "rules": [
            "투자 조언처럼 보이는 매수/매도 문구는 쓰지 않습니다.",
            "커뮤니티 공유는 질문형 요약과 공개 URL 1개만 사용합니다.",
            "같은 글을 같은 채널에 반복 도배하지 않습니다.",
            "발행 후 24시간 안에 후속 글 또는 popular reads 내부링크를 최소 2개 붙입니다.",
        ],
        "manual_execution_summary": {
            "checklist_item_count": sum(len(plan.get("manual_execution_checklist", [])) for plan in plans),
            "first_action": "각 공개 URL마다 x_threads_or_short_social 문구 1개부터 공유",
            "do_not_do": "같은 채널에 같은 글을 반복 도배하지 않기",
        },
    }


def write_markdown(report: dict) -> None:
    lines = [
        "# Traffic Amplification Plan",
        "",
        f"- 목표 방문자: `{report['target_daily_visitors']}`",
        f"- 기본 예상 방문자: `{report['base_projected_visitors']}`",
        f"- 실행 전 배포 추가 예상 방문자: `{report['amplification_expected_visitors']}`",
        f"- 수동 실행 시 추가 잠재 방문자: `{report['amplification_potential_visitors_if_executed']}`",
        f"- 실행 전 배포 포함 예상 방문자: `{report['projected_with_amplification']}`",
        f"- 수동 실행 시 잠재 방문자: `{report['potential_with_manual_amplification']}`",
        f"- 남은 부족분: `{report['gap_after_amplification']}`",
        f"- 상태: `{report['status']}`",
        "",
        "## 운영 규칙",
        "",
    ]
    for rule in report.get("rules", []):
        lines.append(f"- {rule}")
    lines.append("")
    for idx, plan in enumerate(report.get("plans", []), start=1):
        lines.append(f"## {idx}. {plan.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{plan.get('keyword', '')}`")
        lines.append(f"- public_url: {plan.get('public_url') or '`missing`'}")
        lines.append(f"- base_search_estimate: `{plan.get('base_estimated_search_visitors', 0)}`")
        lines.append(f"- amplification_expected_before_execution: `{plan.get('amplification_expected_visitors', 0)}`")
        lines.append(f"- amplification_potential_if_executed: `{plan.get('amplification_potential_visitors_if_executed', 0)}`")
        lines.append(f"- manual_execution_required: `{plan.get('manual_execution_required', True)}`")
        lines.append("")
        lines.append("### Manual Execution Checklist")
        lines.append("")
        for check in plan.get("manual_execution_checklist", []):
            lines.append(
                f"- [ ] `{check.get('channel', '')}` / `{check.get('time_window', '')}` / variant `{check.get('copy_variant_to_use', '')}` / expected `{check.get('expected_visitors', 0)}`"
            )
        if not plan.get("manual_execution_checklist"):
            lines.append("- 실행할 외부 배포 체크리스트가 없습니다.")
        lines.append("")
        for slot in plan.get("share_slots", []):
            blocked = f" / blocked `{slot.get('blocked_by')}`" if slot.get("blocked_by") else ""
            lines.append(
                f"### {slot.get('time_window')} / {slot.get('channel')} / potential `{slot.get('potential_visitors_if_executed', 0)}`{blocked}"
            )
            lines.append("")
            lines.append(f"- task: {slot.get('task', '')}")
            lines.append("")
            lines.append("```text")
            lines.append(slot.get("copy", ""))
            lines.append("```")
            lines.append("")
            if slot.get("copy_variants"):
                lines.append("#### Copy Variants")
                lines.append("")
                for variant in slot.get("copy_variants", []):
                    lines.append(f"- `{variant.get('label', '')}`")
                    lines.append("")
                    lines.append("```text")
                    lines.append(variant.get("copy", ""))
                    lines.append("```")
                    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
