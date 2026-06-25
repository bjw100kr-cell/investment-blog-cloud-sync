#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/site_foundation.json"
OUTPUT_DIR = ROOT / "outputs/latest/site-foundation"
INDEX_MD = OUTPUT_DIR / "site-foundation-index.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n")


def build_about_page(config: dict) -> str:
    about = config["about"]
    lines = []
    lines.append(f"# {config['site_name']} 소개")
    lines.append("")
    lines.append(config["site_tagline"])
    lines.append("")
    lines.append("## 이 블로그는 무엇을 하나")
    lines.append("")
    lines.append(about["owner_role"])
    lines.append("")
    lines.append("## 운영 목적")
    lines.append("")
    lines.append(about["mission"])
    lines.append("")
    lines.append("## 이런 분들을 위해 씁니다")
    lines.append("")
    for item in about["audience"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 글을 쓸 때 지키는 원칙")
    lines.append("")
    for item in about["writing_principles"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 한 줄 약속")
    lines.append("")
    lines.append("복잡한 시장 뉴스를 더 쉽게, 더 차분하게, 더 오래 참고할 수 있게 정리합니다.")
    return "\n".join(lines)


def build_disclosure_page(config: dict) -> str:
    trust = config["trust_pages"]
    lines = []
    lines.append(f"# {trust['disclosure_title']}")
    lines.append("")
    for item in trust["disclosure_points"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 기본 면책")
    lines.append("")
    lines.append("이 블로그의 글은 정보 제공 및 학습용 정리이며, 특정 자산에 대한 투자 권유나 자문이 아닙니다.")
    return "\n".join(lines)


def build_fact_check_page(config: dict) -> str:
    trust = config["trust_pages"]
    lines = []
    lines.append(f"# {trust['fact_check_title']}")
    lines.append("")
    for item in trust["fact_check_points"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 발행 전 확인 체크")
    lines.append("")
    lines.append("- 날짜와 기준 시점")
    lines.append("- 핵심 수치와 가격")
    lines.append("- 공식 출처 링크")
    lines.append("- 과장 표현 여부")
    return "\n".join(lines)


def build_privacy_page(config: dict) -> str:
    trust = config["trust_pages"]
    lines = []
    lines.append(f"# {trust['privacy_title']}")
    lines.append("")
    for item in trust["privacy_points"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 기본 원칙")
    lines.append("")
    lines.append("- 필수적으로 필요한 최소 정보만 다룹니다.")
    lines.append("- 방문 통계는 운영 개선 목적으로만 사용합니다.")
    lines.append("- 외부 분석/광고 도구 연결 시 해당 사실을 본 페이지에서 갱신합니다.")
    return "\n".join(lines)


def build_editorial_page(config: dict) -> str:
    trust = config["trust_pages"]
    lines = []
    lines.append(f"# {trust['editorial_title']}")
    lines.append("")
    for item in trust["editorial_points"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 업데이트 원칙")
    lines.append("")
    lines.append("- 핵심 수치와 일정이 바뀌면 본문과 발행일 기준 메모를 함께 수정합니다.")
    lines.append("- 과장되거나 단정적인 표현은 수정 우선순위를 높게 둡니다.")
    return "\n".join(lines)


def build_contact_page(config: dict) -> str:
    trust = config["trust_pages"]
    contact = config.get("contact", {})
    lines = []
    lines.append(f"# {trust['contact_title']}")
    lines.append("")
    for item in trust["contact_points"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 운영 메모")
    lines.append("")
    lines.append(contact.get("channel_note", "연락 채널은 실제 운영 단계에서 연결합니다."))
    lines.append("")
    lines.append("## 응답 기준")
    lines.append("")
    lines.append(contact.get("response_note", "오류 제보와 운영 문의를 우선 확인합니다."))
    return "\n".join(lines)


def build_hub_page(hub: dict) -> str:
    lines = []
    lines.append(f"# {hub['title']}")
    lines.append("")
    lines.append(hub["description"])
    lines.append("")
    lines.append("## 이 카테고리에서 다루는 핵심 키워드")
    lines.append("")
    for keyword in hub["target_keywords"]:
        lines.append(f"- {keyword}")
    lines.append("")
    lines.append("## 먼저 쌓아둘 핵심 허브 글")
    lines.append("")
    for idea in hub["pillar_post_ideas"]:
        lines.append(f"- {idea}")
    lines.append("")
    lines.append("## 운영 메모")
    lines.append("")
    lines.append("속보형 글에서 유입된 독자가 이 허브 글로 이동할 수 있게 내부링크를 연결합니다.")
    return "\n".join(lines)


def build_home_structure(config: dict) -> str:
    lines = []
    lines.append("# 홈/메뉴 구조 제안")
    lines.append("")
    lines.append(f"- 사이트명: {config['site_name']}")
    lines.append(f"- 태그라인: {config['site_tagline']}")
    lines.append("")
    lines.append("## 상단 메뉴")
    lines.append("")
    lines.append("- 거시경제")
    lines.append("- 코인")
    lines.append("- 세계 흐름·섹터")
    lines.append("- About")
    lines.append("- 운영 원칙")
    lines.append("")
    lines.append("## 홈 화면 구성")
    lines.append("")
    lines.append("- 상단: 오늘의 핵심 글 1개")
    lines.append("- 중단: 최신 글 3~5개")
    lines.append("- 하단: 카테고리 허브 3개")
    lines.append("- 사이드/하단: 주간 회고, 인기 해설 글")
    lines.append("")
    lines.append("## 수익화 메모")
    lines.append("")
    for item in config["monetization_notes"]:
        lines.append(f"- {item}")
    return "\n".join(lines)


def main() -> int:
    config = load_json(CONFIG_PATH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    write(OUTPUT_DIR / "about.md", build_about_page(config))
    write(OUTPUT_DIR / "disclosure.md", build_disclosure_page(config))
    write(OUTPUT_DIR / "fact-check-policy.md", build_fact_check_page(config))
    write(OUTPUT_DIR / "privacy-policy.md", build_privacy_page(config))
    write(OUTPUT_DIR / "editorial-policy.md", build_editorial_page(config))
    write(OUTPUT_DIR / "contact.md", build_contact_page(config))
    write(OUTPUT_DIR / "home-structure.md", build_home_structure(config))

    hub_paths = []
    for hub in config["category_hubs"]:
        hub_path = OUTPUT_DIR / f"hub-{hub['slug']}.md"
        write(hub_path, build_hub_page(hub))
        hub_paths.append(hub_path.name)

    index_lines = []
    index_lines.append("# 사이트 기반 페이지 인덱스")
    index_lines.append("")
    index_lines.append("- about.md")
    index_lines.append("- disclosure.md")
    index_lines.append("- fact-check-policy.md")
    index_lines.append("- privacy-policy.md")
    index_lines.append("- editorial-policy.md")
    index_lines.append("- contact.md")
    index_lines.append("- home-structure.md")
    for name in hub_paths:
        index_lines.append(f"- {name}")
    write(INDEX_MD, "\n".join(index_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
