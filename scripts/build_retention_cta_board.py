#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POPULAR_READS_BOARD_JSON = ROOT / "outputs/latest/popular-reads-board.json"
DISTRIBUTION_PACK_JSON = ROOT / "outputs/latest/distribution-pack.json"
MONETIZATION_READINESS_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/retention-cta-board.json"
OUTPUT_MD = ROOT / "outputs/latest/retention-cta-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def snippet_lookup(pack: dict) -> dict[str, dict]:
    return {item.get("keyword", ""): item.get("snippets", {}) for item in pack.get("items", []) if item.get("keyword")}


def cluster_cta(cluster_keyword: str, cta_focus: str) -> dict:
    if cluster_keyword == "fomc":
        return {
            "inline_cta_now": "FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.",
            "telegram_cta_later": "거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.",
            "newsletter_cta_later": "거시 이벤트 해설을 한 번에 받고 싶다면 뉴스레터 구독 동선으로 이어 붙입니다.",
        }
    if cluster_keyword == "bitcoin":
        return {
            "inline_cta_now": "비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.",
            "telegram_cta_later": "코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.",
            "newsletter_cta_later": "비트코인과 주요 코인 흐름을 주간 브리핑으로 다시 받게 만드는 뉴스레터 CTA 후보입니다.",
        }
    if cluster_keyword == "us_big_tech":
        return {
            "inline_cta_now": "빅테크 흐름은 대표 종목과 공급망 글을 같이 봐야 실제 투자 연결이 됩니다. 아래 읽을거리까지 함께 보세요.",
            "telegram_cta_later": "섹터 흐름 요약을 짧게 계속 받고 싶다면 텔레그램/채널형 재방문 동선과 연결합니다.",
            "newsletter_cta_later": "실적 시즌과 섹터 흐름을 주간 정리로 다시 받아보게 만드는 뉴스레터 CTA 후보입니다.",
        }
    return {
        "inline_cta_now": f"이 글과 함께 아래 읽을거리까지 보면 `{cta_focus}` 흐름이 훨씬 더 잘 이어집니다.",
        "telegram_cta_later": "핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.",
        "newsletter_cta_later": "다음 중요한 이벤트를 놓치지 않도록 뉴스레터 구독 동선과 연결합니다.",
    }


def build_report() -> dict:
    popular = load_json(POPULAR_READS_BOARD_JSON)
    snippets = snippet_lookup(load_json(DISTRIBUTION_PACK_JSON))
    monetization = load_json(MONETIZATION_READINESS_JSON)

    retention_stage = next((stage for stage in monetization.get("stages", []) if stage.get("name") == "retention_stack"), {})
    groups = []

    for group in popular.get("groups", []):
        source_keyword = group.get("source_keyword", "")
        main_pick = next((pick for pick in group.get("picks", []) if pick.get("slot") == "main_pick"), {})
        followups = [pick for pick in group.get("picks", []) if pick.get("slot", "").startswith("followup_pick")]
        ctas = cluster_cta(source_keyword, group.get("cta_focus", ""))
        main_snippets = snippets.get(main_pick.get("keyword", ""), {})
        groups.append(
            {
                "cluster_name": group.get("cluster_name", ""),
                "source_keyword": source_keyword,
                "main_title": main_pick.get("title", ""),
                "main_ready_to_upload": group.get("main_ready_to_upload", False),
                "cta_focus": group.get("cta_focus", ""),
                "inline_cta_now": ctas.get("inline_cta_now", ""),
                "telegram_cta_later": ctas.get("telegram_cta_later", ""),
                "newsletter_cta_later": ctas.get("newsletter_cta_later", ""),
                "newsletter_subject_seed": main_snippets.get("newsletter_subject", ""),
                "newsletter_preview_seed": main_snippets.get("newsletter_preview", ""),
                "followup_titles": [item.get("title", "") for item in followups[:2]],
                "next_action": group.get("next_action", ""),
                "blockers": group.get("blockers", []),
            }
        )

    return {
        "board_goal": "글 하단 CTA를 재방문과 나중 구독 전환 흐름으로 바꾸기 위한 운영 보드",
        "retention_stack_ready": retention_stage.get("ready", False),
        "retention_next_step": retention_stage.get("next_step", ""),
        "group_count": len(groups),
        "groups": groups,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Retention CTA Board")
    lines.append("")
    lines.append("글 하단 CTA를 `다음 읽을거리`, `텔레그램/채널`, `뉴스레터` 흐름으로 정리한 운영 카드입니다.")
    lines.append(f"- board_goal: {report.get('board_goal', '')}")
    lines.append(f"- retention_stack_ready: `{report.get('retention_stack_ready', False)}`")
    lines.append(f"- retention_next_step: {report.get('retention_next_step', '')}")
    lines.append(f"- group_count: `{report.get('group_count', 0)}`")
    lines.append("")
    for idx, group in enumerate(report.get("groups", []), start=1):
        lines.append(f"## {idx}. {group.get('cluster_name', '')}")
        lines.append("")
        lines.append(f"- source_keyword: `{group.get('source_keyword', '')}`")
        lines.append(f"- main_title: `{group.get('main_title', '')}`")
        lines.append(f"- main_ready_to_upload: `{group.get('main_ready_to_upload', False)}`")
        lines.append(f"- cta_focus: {group.get('cta_focus', '')}")
        lines.append(f"- inline_cta_now: {group.get('inline_cta_now', '')}")
        lines.append(f"- telegram_cta_later: {group.get('telegram_cta_later', '')}")
        lines.append(f"- newsletter_cta_later: {group.get('newsletter_cta_later', '')}")
        lines.append(f"- newsletter_subject_seed: {group.get('newsletter_subject_seed', '')}")
        lines.append(f"- newsletter_preview_seed: {group.get('newsletter_preview_seed', '')}")
        for title in group.get("followup_titles", []):
            lines.append(f"- followup_title: {title}")
        lines.append(f"- next_action: {group.get('next_action', '')}")
        for blocker in group.get("blockers", []):
            lines.append(f"- blocker: {blocker}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
