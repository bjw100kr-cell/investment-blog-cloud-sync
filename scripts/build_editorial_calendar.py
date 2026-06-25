#!/usr/bin/env python3
import json
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
PERFORMANCE_JSON = ROOT / "outputs/latest/performance-feedback.json"
TEMPLATE_JSON = ROOT / "config/editorial_calendar_templates.json"
OUTPUT_JSON = ROOT / "outputs/latest/editorial-calendar.json"
OUTPUT_MD = ROOT / "outputs/latest/editorial-calendar.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def load_optional_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def make_breaking_entry(day: date, slot: int, role: str, brief: dict, note: str) -> dict:
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": role,
        "post_type": "breaking_explainer",
        "target_keyword": brief["keyword"],
        "working_title": brief["title_candidates"][0],
        "angle": brief["reason"],
        "search_intent": "당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자",
        "monetization_path": "시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대",
        "internal_link_targets": brief["source_names"],
        "source_basis": brief["source_names"],
        "publish_note": note,
    }


def make_evergreen_entry(day: date, slot: int, cluster: dict, performance_lookup: dict) -> dict:
    bonus = 0.0
    for related in cluster["related_keywords"]:
        bonus = max(bonus, float(performance_lookup.get(related, {}).get("bonus", 0)))

    note = "성과 데이터가 있는 키워드와 연결된 설명형 글" if bonus > 0 else "검색 저변을 넓히는 설명형 글"
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": "evergreen_seo",
        "post_type": cluster["post_type"],
        "target_keyword": cluster["keyword"],
        "working_title": cluster["working_title"],
        "angle": cluster["angle"],
        "search_intent": cluster["search_intent"],
        "monetization_path": cluster["monetization_path"],
        "internal_link_targets": cluster["internal_link_targets"],
        "source_basis": cluster["related_keywords"],
        "publish_note": note,
    }


def make_follow_up_entry(day: date, slot: int, brief: dict) -> dict:
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": "follow_up",
        "post_type": "follow_up_analysis",
        "target_keyword": brief["keyword"],
        "working_title": f"{brief['title_candidates'][0]}: 다음으로 봐야 할 변수",
        "angle": "첫 해설에서 끝내지 않고 다음 이벤트와 체크포인트 중심으로 후속 글 구성",
        "search_intent": "어제/오늘 본 이슈가 앞으로 어떻게 이어질지 알고 싶은 재방문 독자",
        "monetization_path": "재방문 트래픽과 내부링크 순환 강화",
        "internal_link_targets": brief["title_candidates"][:2],
        "source_basis": brief["source_names"],
        "publish_note": "속보형 글 다음날 이어지는 후속 해설",
    }


def make_weekly_recap_entry(day: date, slot: int, briefs: list[dict]) -> dict:
    keywords = [brief["keyword"] for brief in briefs[:3]]
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": "weekly_recap",
        "post_type": "weekly_macro_recap",
        "target_keyword": ", ".join(keywords),
        "working_title": "이번 주 주식·코인·거시 흐름 한 번에 정리",
        "angle": "상위 이슈 3개를 한 글에서 연결해 재방문 독자와 체류 시간을 늘리는 회고형 글",
        "search_intent": "이번 주 시장 흐름을 짧게 복기하고 다음 주 포인트를 잡고 싶은 독자",
        "monetization_path": "주간 회고형 콘텐츠로 페이지뷰 누적과 내부 링크 허브 역할",
        "internal_link_targets": keywords,
        "source_basis": keywords,
        "publish_note": "주간 정리형 글로 카테고리 허브 역할 수행",
    }


def rank_clusters(clusters: list[dict], briefs: list[dict], performance_lookup: dict) -> list[dict]:
    brief_keywords = {brief["keyword"] for brief in briefs}
    ranked = []
    for cluster in clusters:
        overlap = len(brief_keywords.intersection(cluster["related_keywords"]))
        bonus = max(float(performance_lookup.get(keyword, {}).get("bonus", 0)) for keyword in cluster["related_keywords"])
        ranked.append((overlap, bonus, cluster["keyword"], cluster))
    ranked.sort(key=lambda item: (-item[0], -item[1], item[2]))
    return [item[3] for item in ranked]


def build_schedule(briefs: list[dict], clusters: list[dict], performance_lookup: dict) -> list[dict]:
    today = date.today()
    schedule = []
    primary = briefs[0] if briefs else None
    secondary = briefs[1] if len(briefs) > 1 else primary
    tertiary = briefs[2] if len(briefs) > 2 else secondary
    fourth = briefs[3] if len(briefs) > 3 else tertiary

    ranked_clusters = rank_clusters(clusters, briefs, performance_lookup)
    evergreen_one = ranked_clusters[0] if ranked_clusters else None
    evergreen_two = ranked_clusters[1] if len(ranked_clusters) > 1 else evergreen_one

    if primary:
        schedule.append(make_breaking_entry(today, 1, "breaking_primary", primary, "가장 강한 이슈는 당일 오전 포스팅 권장"))
    if secondary:
        schedule.append(make_breaking_entry(today + timedelta(days=1), 2, "breaking_secondary", secondary, "메인 이슈와 겹치지 않게 다른 독자층까지 확보"))
    if evergreen_one:
        schedule.append(make_evergreen_entry(today + timedelta(days=2), 3, evergreen_one, performance_lookup))
    if primary:
        schedule.append(make_follow_up_entry(today + timedelta(days=3), 4, primary))
    if evergreen_two:
        schedule.append(make_evergreen_entry(today + timedelta(days=4), 5, evergreen_two, performance_lookup))
    if fourth:
        schedule.append(make_breaking_entry(today + timedelta(days=5), 6, "sector_or_crypto", fourth, "섹터 또는 코인 글로 카테고리 다양화"))
    if briefs:
        schedule.append(make_weekly_recap_entry(today + timedelta(days=6), 7, briefs))

    return schedule


def main() -> int:
    brief_data = load_json(BRIEF_JSON)
    performance = load_optional_json(PERFORMANCE_JSON)
    templates = load_json(TEMPLATE_JSON)

    briefs = brief_data.get("top_briefs", [])
    performance_lookup = (performance or {}).get("keyword_feedback", {})
    schedule = build_schedule(briefs, templates.get("evergreen_clusters", []), performance_lookup)

    payload = {
        "generated_at": brief_data.get("generated_at"),
        "schedule": schedule,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 7일 편집 캘린더")
    lines.append("")
    lines.append(f"- 생성 시각: `{payload['generated_at']}`")
    lines.append("- 목적: 속보형 글만이 아니라 검색형 설명 글까지 섞어서 매일 포스팅 유지")
    lines.append("")
    for item in schedule:
        lines.append(f"## Day {item['slot']} · {item['date']} · {item['role']}")
        lines.append("")
        lines.append(f"- 포스트 유형: {item['post_type']}")
        lines.append(f"- 타깃 키워드: {item['target_keyword']}")
        lines.append(f"- 작업 제목: {item['working_title']}")
        lines.append(f"- 글 각도: {item['angle']}")
        lines.append(f"- 검색 의도: {item['search_intent']}")
        lines.append(f"- 수익화 경로: {item['monetization_path']}")
        lines.append(f"- 내부링크 대상: {', '.join(item['internal_link_targets'])}")
        lines.append(f"- 근거 소스/연결 키워드: {', '.join(item['source_basis'])}")
        lines.append(f"- 발행 메모: {item['publish_note']}")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
