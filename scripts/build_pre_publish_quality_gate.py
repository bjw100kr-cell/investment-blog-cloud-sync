#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_READY_REPORT_JSON = ROOT / "outputs/latest/publish-ready-report.json"
SEO_PUBLISH_READY_REPORT_JSON = ROOT / "outputs/latest/seo-publish-ready-report.json"
MONETIZATION_PLAYBOOK_JSON = ROOT / "config/monetization_playbook.json"
OUTPUT_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
OUTPUT_MD = ROOT / "outputs/latest/pre-publish-quality-gate.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def read_text(path_text: str) -> str:
    path = Path(path_text)
    if not path.exists():
        return ""
    return path.read_text()


def is_source_string_strong(html_text: str) -> bool:
    source_line = ""
    match = re.search(r"<strong>참고 소스</strong>:\s*([^<]+)</p>", html_text)
    if match:
        source_line = match.group(1).lower()
    strong_markers = [
        "reuters",
        "cnbc",
        "financial times",
        "marketwatch",
        "coindesk",
        "cointelegraph",
        "federal reserve",
        "fomc",
        "investing.com",
        "google trends",
        "ft.com",
        "financial times home",
        "official",
        "press",
    ]
    weak_markers = [
        "관련 해설 글과 핵심 키워드",
        "관련 해설 글",
    ]
    if any(marker in source_line for marker in weak_markers):
        return False
    return any(marker in source_line for marker in strong_markers)


def count_internal_links(html_text: str) -> int:
    return len(re.findall(r'href=\"[^\"]*?/p/[^"]+\"', html_text))


def has_selected_image(item: dict, slot: str) -> bool:
    for image in item.get("image_plan", []):
        if image.get("slot") != slot:
            continue
        if image.get("selected_url", "").strip():
            return True
        if image.get("search_query", "").strip():
            return True
    return False


def audit_item(item: dict, checklist: list[str]) -> dict:
    html_text = read_text(item.get("html_path", ""))
    checks = []

    def add_check(name: str, ok: bool, severity: str, detail: str) -> None:
        checks.append(
            {
                "name": name,
                "ok": ok,
                "severity": severity,
                "detail": detail,
            }
        )

    meta_description = item.get("meta_description", "")
    add_check(
        "meta_description_present",
        bool(meta_description.strip()),
        "high",
        "메타 설명이 비어 있으면 검색 클릭률에 직접 악영향을 줄 수 있습니다.",
    )
    add_check(
        "author_box_present",
        "post-author-box" in html_text and bool(item.get("author_name")),
        "high",
        "작성 정보와 운영 주체가 노출되어야 신뢰 신호가 유지됩니다.",
    )
    add_check(
        "publish_date_present",
        bool(item.get("recommended_publish_date")) and "발행 기준일:" in html_text,
        "high",
        "발행 기준일이 있어야 시의성과 업데이트 신호를 확인하기 쉽습니다.",
    )
    add_check(
        "disclaimer_present",
        bool(item.get("trust_footer_note")) and "post-disclosure" in html_text,
        "high",
        "면책/운영 원칙 문구가 있어야 투자 해설 블로그 신뢰도에 유리합니다.",
    )
    add_check(
        "fact_check_box_present",
        "post-fact-check" in html_text,
        "medium",
        "핵심 숫자와 날짜를 재확인하는 박스는 helpful content 신뢰도에 중요합니다.",
    )
    add_check(
        "source_strength",
        is_source_string_strong(html_text),
        "medium",
        "공식 자료나 신뢰 가능한 매체 소스가 직접 보이면 글 신뢰도가 높아집니다.",
    )
    add_check(
        "internal_links_minimum",
        count_internal_links(html_text) >= 2,
        "medium",
        "관련 허브/정책/소개 글 내부링크 최소 2개는 재방문과 체류시간에 유리합니다.",
    )
    add_check(
        "follow_up_posts_present",
        len(item.get("follow_up_posts", [])) >= 1,
        "medium",
        "후속 글 연결이 있어야 검색 유입이 사이트 내 순환으로 이어집니다.",
    )
    if item.get("category") in {"macro", "crypto", "global-sector"}:
        add_check(
            "hero_image_selected",
            has_selected_image(item, "hero"),
            "medium",
            "대표 이미지 1장은 체류시간과 썸네일 완성도에 유리하므로 발행 전 선택해 두는 편이 좋습니다.",
        )
    add_check(
        "image_license_review_ready",
        bool(item.get("image_plan")),
        "low",
        "라이선스가 확인된 이미지 후보와 alt 문구가 같이 준비되어야 운영 속도가 안정적입니다.",
    )
    add_check(
        "faq_schema_present",
        "FAQPage" in item.get("structured_data_types", []),
        "low",
        "FAQ 구조화 데이터는 검색 결과 확장 가능성을 높일 수 있습니다.",
    )
    add_check(
        "canonical_url_present",
        bool(item.get("canonical_url")),
        "low",
        "BLOG_BASE_URL이 있으면 canonical URL을 넣어 중복 해석을 줄일 수 있습니다.",
    )
    add_check(
        "newsletter_ready",
        bool(item.get("newsletter_enabled")),
        "low",
        "뉴스레터 구독 동선은 재방문과 수익화 확장에 도움이 됩니다.",
    )
    add_check(
        "ga4_ready",
        bool(item.get("ga4_enabled")),
        "low",
        "GA4가 있어야 실제 체류/유입 성과를 계량적으로 볼 수 있습니다.",
    )

    hard_fail = any(not check["ok"] and check["severity"] == "high" for check in checks)
    medium_fail = any(not check["ok"] and check["severity"] == "medium" for check in checks)
    status = "pass"
    if hard_fail:
        status = "needs_fix"
    elif medium_fail:
        status = "review_before_publish"

    return {
        "keyword": item.get("keyword", ""),
        "title": item.get("title", ""),
        "status": status,
        "checklist_reference": checklist,
        "checks": checks,
        "html_path": item.get("html_path", ""),
        "manifest_path": item.get("manifest_path", ""),
    }


def build_report() -> dict:
    publish_ready = load_json(PUBLISH_READY_REPORT_JSON)
    seo_publish_ready = load_json(SEO_PUBLISH_READY_REPORT_JSON)
    playbook = load_json(MONETIZATION_PLAYBOOK_JSON)
    checklist = playbook.get("readiness_checklist", [])

    audited_items = []
    for source_name, report in [
        ("main", publish_ready),
        ("seo", seo_publish_ready),
    ]:
        for item in report.get("items", []):
            audited = audit_item(item, checklist)
            audited["source_group"] = source_name
            audited_items.append(audited)

    summary = {
        "item_count": len(audited_items),
        "pass_count": sum(1 for item in audited_items if item["status"] == "pass"),
        "review_before_publish_count": sum(1 for item in audited_items if item["status"] == "review_before_publish"),
        "needs_fix_count": sum(1 for item in audited_items if item["status"] == "needs_fix"),
    }
    return {
        "summary": summary,
        "items": audited_items,
        "readiness_checklist": checklist,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Pre-Publish Quality Gate")
    lines.append("")
    lines.append("발행 전에 신뢰, 내부링크, 구조화 데이터, 재방문 장치가 빠졌는지 자동 점검하는 품질 게이트입니다.")
    lines.append("")
    summary = report.get("summary", {})
    lines.append(f"- item_count: `{summary.get('item_count', 0)}`")
    lines.append(f"- pass_count: `{summary.get('pass_count', 0)}`")
    lines.append(f"- review_before_publish_count: `{summary.get('review_before_publish_count', 0)}`")
    lines.append(f"- needs_fix_count: `{summary.get('needs_fix_count', 0)}`")
    lines.append("")
    lines.append("## Readiness Checklist Reference")
    lines.append("")
    for item in report.get("readiness_checklist", []):
        lines.append(f"- {item}")
    lines.append("")
    for entry in report.get("items", []):
        lines.append(f"## {entry.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{entry.get('keyword', '')}`")
        lines.append(f"- source_group: `{entry.get('source_group', '')}`")
        lines.append(f"- status: `{entry.get('status', '')}`")
        lines.append(f"- html_path: `{entry.get('html_path', '')}`")
        for check in entry.get("checks", []):
            marker = "ok" if check.get("ok") else "fail"
            lines.append(
                f"- {marker} / `{check.get('severity', '')}` / `{check.get('name', '')}`: {check.get('detail', '')}"
            )
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
