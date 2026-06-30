#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
OUTPUT_JSON = ROOT / "outputs/latest/monetization-roadmap.json"
OUTPUT_MD = ROOT / "outputs/latest/monetization-roadmap.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_phase(phase: str, gate: str, focus: str, tasks: list[str], success_signal: str) -> dict:
    return {
        "phase": phase,
        "gate": gate,
        "focus": focus,
        "tasks": tasks,
        "success_signal": success_signal,
    }


def build_report() -> dict:
    monetization = load_json(MONETIZATION_JSON)
    dashboard = load_json(GO_LIVE_JSON)
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)

    first_title = ((revenue_focus.get("today_path") or [{}])[0]).get("title", "오늘의 메인 글")
    second_title = ((revenue_focus.get("today_path") or [{}, {}, {}])[2]).get("title", "다음 슬롯 글")

    phases = [
        build_phase(
            "phase_1_validate_blogger",
            "GitHub repo 연결 전후 첫 Blogger draft 검증",
            "게시 파이프라인이 실제로 하루 1건씩 안전하게 돌아가는지 확인",
            [
                f"`{first_title}` 단건 승인 후 Blogger draft 업로드",
                "`platform-publish-plan`과 `first-cloud-run-verification` 결과 확인",
                "Blogger draft 화면에서 제목, 본문, 링크, 라벨 수동 검수",
            ],
            "Blogger draft 1건이 승인 범위대로 생성되고 추가 오작동 업로드가 없어야 함",
        ),
        build_phase(
            "phase_2_repeatable_content_loop",
            "첫 draft 검증 성공 후 3~7일 운영",
            "검색 유입용 메인 글과 후속 SEO 글이 반복 루프로 굴러가는지 확인",
            [
                f"`{first_title}` -> SEO 후속 글 -> `{second_title}` 흐름 반복",
                "daily-revenue-focus 기준으로 매일 1순위 글과 후속 글 연결",
                "승인 keyword 운영이 과도하게 번거롭지 않은지 체크",
            ],
            "3일 이상 연속으로 메인 글과 후속 글 경로가 유지되고 승인/업로드 루틴이 안정적이어야 함",
        ),
        build_phase(
            "phase_3_measurement_stack",
            "반복 발행 루프 확인 후",
            "어떤 글이 실제 체류시간과 재방문을 만드는지 측정",
            [
                "`GA4_MEASUREMENT_ID` 연결",
                "상위 3개 글의 체류시간, 진입, 내부링크 클릭 흐름 추적",
                "daily-revenue-focus와 실제 성과가 얼마나 맞는지 비교",
            ],
            "상위 글별 진입/체류/재방문 데이터를 확인할 수 있어야 함",
        ),
        build_phase(
            "phase_4_retention_stack",
            "측정 데이터 확인 후",
            "유입을 재방문으로 바꾸는 장치 추가",
            [
                "`NEWSLETTER_SUBSCRIBE_URL` 또는 텔레그램/구독 채널 연결",
                "메인 글과 SEO 글 하단 CTA에 재방문 유도 문구 삽입",
                "다음 주제 예고형 내부링크와 구독 유도 문구 점검",
            ],
            "구독/재방문 경로가 글 하단 CTA와 연결되고 운영자가 누적 전환을 추적할 수 있어야 함",
        ),
        build_phase(
            "phase_5_adsense_stack",
            "체류와 재방문 흐름 확인 후",
            "광고 수익화를 붙여도 UX가 망가지지 않는 상태 만들기",
            [
                "`ADSENSE_PUBLISHER_ID`, `ADSENSE_SITE_VERIFICATION` 연결",
                "광고 위치가 글 흐름과 CTA를 방해하지 않는지 검수",
                "광고 노출형 글과 신뢰형 글 비율 조정",
            ],
            "광고가 붙어도 읽기 흐름이 무너지지 않고 광고 노출/체류 간 균형이 유지되어야 함",
        ),
        build_phase(
            "phase_6_expand_wordpress",
            "Blogger 운영과 수익화 루프가 안정화된 뒤",
            "두 번째 채널로 WordPress 확장",
            [
                "`WORDPRESS_SITE_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_APPLICATION_PASSWORD` 연결",
                "Blogger 승인 경로를 WordPress draft 채널에도 동일 적용",
                "중복 게시 정책과 canonical/내부링크 정책 결정",
            ],
            "WordPress가 Blogger를 흔들지 않는 보조 채널로 동작하고 중복/운영 리스크가 통제되어야 함",
        ),
    ]

    return {
        "generated_at": monetization.get("generated_at", ""),
        "monetization_score": monetization.get("readiness_score", 0),
        "first_live_run_ready": dashboard.get("ready_for_first_live_run", False),
        "phases": phases,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Monetization Roadmap")
    lines.append("")
    lines.append("발행 자동화 이후 수익화 스택을 어떤 순서로 붙일지 정리한 운영 로드맵입니다.")
    lines.append("")
    lines.append(f"- monetization_score: `{report.get('monetization_score', 0)}`")
    lines.append(f"- first_live_run_ready: `{report.get('first_live_run_ready', False)}`")
    lines.append("")
    for phase in report.get("phases", []):
        lines.append(f"## {phase.get('phase', '')}")
        lines.append("")
        lines.append(f"- gate: {phase.get('gate', '')}")
        lines.append(f"- focus: {phase.get('focus', '')}")
        for task in phase.get("tasks", []):
            lines.append(f"- task: {task}")
        lines.append(f"- success_signal: {phase.get('success_signal', '')}")
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
