#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
PUBLISHING_JSON = ROOT / "outputs/latest/publishing-assets.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/seo-backlog.json"
OUTPUT_MD = ROOT / "outputs/latest/seo-backlog.md"


SEO_TEMPLATES = {
    "macro": [
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_explainer",
            "title_template": "{topic}{subject_particle} 주식과 코인에 미치는 영향",
            "search_intent": "뉴스를 봤지만 내 투자에 어떻게 연결되는지 쉽게 이해하고 싶은 독자",
            "monetization_goal": "검색 유입 누적과 첫 방문 독자 확보",
            "cta_focus": "거시 허브와 당일 해설 글로 연결",
        },
        {
            "role": "follow_up",
            "post_type": "follow_up_analysis",
            "title_template": "{topic}에서 다음으로 봐야 할 체크포인트 5가지",
            "search_intent": "발표 이후 다음 일정과 후속 확인 포인트를 빠르게 정리하고 싶은 독자",
            "monetization_goal": "재방문과 내부링크 순환 강화",
            "cta_focus": "다음 이벤트 캘린더와 관련 거시 글로 연결",
        },
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_explainer",
            "title_template": "{topic} 초보자 가이드: 용어부터 시장 반응까지",
            "search_intent": "기초 개념을 처음부터 이해하고 싶은 초보 독자",
            "monetization_goal": "광범위한 초보 검색 수요 흡수",
            "cta_focus": "About, 허브 글, 후속 해설 글로 연결",
        },
    ],
    "global-sector": [
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_sector_guide",
            "title_template": "{topic} 관련 대표 종목 한눈에 보기",
            "search_intent": "섹터 뉴스는 봤지만 실제 어떤 기업을 같이 봐야 하는지 알고 싶은 독자",
            "monetization_goal": "섹터형 검색 유입 누적",
            "cta_focus": "대표 종목 글과 허브 글 연결",
        },
        {
            "role": "follow_up",
            "post_type": "follow_up_analysis",
            "title_template": "{topic} 공급망 정리: 누가 수혜를 보나",
            "search_intent": "테마가 실제 공급망과 실적에 어떻게 연결되는지 알고 싶은 독자",
            "monetization_goal": "체류시간과 페이지뷰 확대",
            "cta_focus": "실적 해설과 글로벌 섹터 허브 연결",
        },
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_sector_guide",
            "title_template": "{topic} ETF·지수·대표 기업 정리",
            "search_intent": "개별 종목보다 묶음으로 섹터를 이해하고 싶은 독자",
            "monetization_goal": "광고 노출과 장기 검색 유입 확보",
            "cta_focus": "섹터 허브와 후속 비교 글 연결",
        },
    ],
    "crypto": [
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_explainer",
            "title_template": "{topic} 초보자 가이드: 지금 꼭 알아야 할 핵심 구조",
            "search_intent": "가격 기사보다 구조와 기본 개념을 먼저 이해하고 싶은 초보 독자",
            "monetization_goal": "초보 검색 유입과 긴 체류시간 확보",
            "cta_focus": "코인 허브와 규제/ETF 글 연결",
        },
        {
            "role": "follow_up",
            "post_type": "follow_up_analysis",
            "title_template": "{topic} ETF·규제 이슈 정리",
            "search_intent": "뉴스가 복잡해서 규제와 ETF 이슈만 따로 정리해 보고 싶은 독자",
            "monetization_goal": "반복 방문과 뉴스형 검색 유입",
            "cta_focus": "당일 코인 해설 글과 초보 가이드 연결",
        },
        {
            "role": "evergreen_seo",
            "post_type": "evergreen_explainer",
            "title_template": "{topic} FAQ 10개: 많이 헷갈리는 질문 정리",
            "search_intent": "짧은 질문 단위로 빠르게 답을 찾고 싶은 독자",
            "monetization_goal": "롱테일 검색 키워드 확보",
            "cta_focus": "기초 글과 주간 정리 글 연결",
        },
    ],
}

STABLE_SEO_TOPIC_BY_SOURCE_KEYWORD = {
    "fomc": "FOMC 이후 시장",
    "bitcoin": "비트코인 핵심 흐름",
    "us_index_flow": "미국 증시 지수 흐름",
    "china": "중국 변수와 시장 영향",
}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def ends_with_final_consonant(text: str) -> bool:
    cleaned = (text or "").strip()
    if not cleaned:
        return False
    code = ord(cleaned[-1])
    if 0xAC00 <= code <= 0xD7A3:
        return ((code - 0xAC00) % 28) != 0
    return False


def choose_particle(text: str, consonant_form: str, vowel_form: str) -> str:
    return consonant_form if ends_with_final_consonant(text) else vowel_form


def render_title(template: str, topic: str) -> str:
    return (
        template
        .replace("{topic}", topic)
        .replace("{subject_particle}", choose_particle(topic, "이", "가"))
        .replace("{and_particle}", choose_particle(topic, "과", "와"))
    )


def slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "_", "·"}:
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "seo-backlog"


def stable_seo_topic(source_keyword: str, fallback_topic: str) -> str:
    return STABLE_SEO_TOPIC_BY_SOURCE_KEYWORD.get(source_keyword, fallback_topic)


def build_asset_lookup(publishing_data: dict) -> dict:
    return {item.get("keyword"): item for item in publishing_data.get("items", [])}


def backlog_items() -> list[dict]:
    queue = load_json(PUBLISH_QUEUE_JSON)
    publishing = load_json(PUBLISHING_JSON)
    monetization = load_json(MONETIZATION_JSON)
    assets = build_asset_lookup(publishing)
    readiness_score = monetization.get("readiness_score", 0)

    items = []
    for queue_item in queue.get("items", []):
        category = queue_item.get("category", "")
        asset = assets.get(queue_item.get("keyword"), {})
        topic = stable_seo_topic(
            queue_item.get("keyword", ""),
            asset.get("title_topic") or queue_item.get("title") or queue_item.get("keyword"),
        )
        internal_links = asset.get("internal_links", [])
        templates = SEO_TEMPLATES.get(category, [])
        for idx, template in enumerate(templates, start=1):
            title = render_title(template["title_template"], topic)
            items.append(
                {
                    "source_keyword": queue_item.get("keyword"),
                    "source_title": queue_item.get("title"),
                    "category": category,
                    "title": title,
                    "slug": slugify(title),
                    "role": template["role"],
                    "post_type": template["post_type"],
                    "priority_score": round(float(queue_item.get("publish_priority_score", 0)) - (idx * 3) + (readiness_score / 20), 2),
                    "search_intent": template["search_intent"],
                    "monetization_goal": template["monetization_goal"],
                    "cta_focus": template["cta_focus"],
                    "primary_internal_link_target": queue_item.get("html_path", ""),
                    "secondary_internal_link_targets": internal_links[:3],
                    "base_revenue_objective": queue_item.get("revenue_objective", ""),
                    "labels": asset.get("labels", []),
                }
            )
    items.sort(key=lambda item: (-item["priority_score"], item["source_keyword"], item["title"]))
    for idx, item in enumerate(items, start=1):
        item["backlog_sequence"] = idx
    return items


def write_markdown(items: list[dict]) -> None:
    lines = []
    lines.append("# SEO / 수익화 후속 글 백로그")
    lines.append("")
    lines.append(f"- 후보 수: `{len(items)}`")
    lines.append("")
    for item in items:
        lines.append(f"## {item['backlog_sequence']}. {item['title']}")
        lines.append("")
        lines.append(f"- 출발 글: {item['source_keyword']} / {item['source_title']}")
        lines.append(f"- 카테고리: {item['category']}")
        lines.append(f"- 역할: {item['role']} / 타입: {item['post_type']}")
        lines.append(f"- 우선순위 점수: {item['priority_score']}")
        lines.append(f"- 검색 의도: {item['search_intent']}")
        lines.append(f"- 수익화 목표: {item['monetization_goal']}")
        lines.append(f"- CTA 초점: {item['cta_focus']}")
        lines.append(f"- 메인 연결 글: {item['primary_internal_link_target']}")
        lines.append(f"- 보조 내부링크: {', '.join(item['secondary_internal_link_targets'])}")
        if item.get("labels"):
            lines.append(f"- 추천 라벨: {', '.join(item['labels'][:6])}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    items = backlog_items()
    payload = {"items": items, "count": len(items)}
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    write_markdown(items)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
