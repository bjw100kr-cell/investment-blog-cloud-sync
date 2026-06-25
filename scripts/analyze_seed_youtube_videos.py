#!/usr/bin/env python3
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests
from youtube_transcript_api import YouTubeTranscriptApi


ROOT = Path(__file__).resolve().parents[1]
CONFIG_JSON = ROOT / "config/seed_youtube_videos.json"
OUTPUT_JSON = ROOT / "outputs/latest/seed-video-analysis.json"
OUTPUT_MD = ROOT / "outputs/latest/seed-video-analysis.md"
USER_AGENT = "Mozilla/5.0 (Codex Seed Video Analyzer)"
LANGUAGES = ["ko", "en"]
MIN_DESCRIPTION_SENTENCE_TEXT = 40

WORKFLOW_TOPICS = {
    "ai_writing": ["블로그", "글", "클로드", "챗지피티", "제미나", "스크립트", "프롬프트"],
    "automation": ["자동", "시스템", "워크플로우", "업로드", "세팅", "연결"],
    "platform_ops": ["블로그스팟", "업로드", "api", "토큰", "계정", "배포"],
    "monetization": ["수익", "애드센스", "광고", "트래픽", "클릭"],
}

TONE_MARKERS = {
    "question_hook": ["계신가요?", "아닌데", "왜", "어떻게"],
    "tool_naming": ["클로드", "챗지피티", "제미나", "블로그스팟", "api", "업로드"],
    "conversation": ["안녕하세요", "해볼게요", "보시면", "그러면", "쉽게"],
    "result_first": ["만들 건", "시스템입니다", "끝난다", "바로"],
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        return parsed.path.strip("/")
    query_video_id = parse_qs(parsed.query).get("v", [""])[0]
    if query_video_id:
        return query_video_id
    parts = [part for part in parsed.path.split("/") if part]
    return parts[-1] if parts else ""


def clean_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "")
    return value.strip()


def split_sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[.!?])\s+|(?<=[다요죠])\s+|\n+", text)
    return [clean_text(chunk) for chunk in chunks if clean_text(chunk)]


def fetch_video_page(video_id: str) -> str:
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    return response.text


def fetch_title_and_description(video_id: str) -> tuple[str, str]:
    html = fetch_video_page(video_id)
    og_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    if og_match:
        title = clean_text(og_match.group(1))
    else:
        title_match = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
        title = clean_text(title_match.group(1).replace("- YouTube", "")) if title_match else video_id

    og_description = re.search(r'<meta property="og:description" content="([^"]+)"', html)
    twitter_description = re.search(r'<meta name="twitter:description" content="([^"]+)"', html)
    description_match = og_description or twitter_description
    description = clean_text(description_match.group(1)) if description_match else ""
    return title, description
    if title_match:
        return clean_text(title_match.group(1).replace("- YouTube", ""))
    return video_id


def fetch_transcript(video_id: str) -> dict:
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=LANGUAGES)
    raw = transcript.to_raw_data()
    text = clean_text(" ".join(item.get("text", "") for item in raw))
    return {
        "language": getattr(transcript, "language", ""),
        "language_code": getattr(transcript, "language_code", ""),
        "is_generated": getattr(transcript, "is_generated", False),
        "text": text,
        "snippets": raw,
    }


def pick_sentences(text: str, terms: list[str], limit: int = 4) -> list[str]:
    sentences = split_sentences(text)
    hits = []
    seen = set()
    for sentence in sentences:
        if not any(term.lower() in sentence.lower() for term in terms):
            continue
        normalized = sentence[:220]
        if normalized in seen:
            continue
        seen.add(normalized)
        hits.append(normalized)
        if len(hits) >= limit:
            return hits
    return hits or [sentence[:220] for sentence in sentences[:limit]]


def score_topic_hits(text: str, mapping: dict[str, list[str]]) -> dict:
    lowered = text.lower()
    scores = {}
    for topic, terms in mapping.items():
        scores[topic] = sum(lowered.count(term.lower()) for term in terms)
    return scores


def infer_tone_takeaways(text: str) -> list[str]:
    scores = score_topic_hits(text, TONE_MARKERS)
    takeaways = []
    if scores["question_hook"] > 0:
        takeaways.append("도입부에서 질문이나 반문으로 바로 훅을 건다.")
    if scores["tool_naming"] > 0:
        takeaways.append("도구 이름을 숨기지 않고 바로 꺼내 실전형 느낌을 만든다.")
    if scores["conversation"] > 0:
        takeaways.append("설명체보다 말하듯 이어가는 회화형 리듬이 강하다.")
    if scores["result_first"] > 0:
        takeaways.append("무엇을 만들지 먼저 선언하고 뒤에서 과정을 푼다.")
    if not takeaways:
        takeaways.append("짧은 문장과 직접 화법 중심의 실전형 설명 톤을 유지한다.")
    return takeaways


def analyze_video(entry: dict) -> dict:
    video_id = extract_video_id(entry["url"])
    title, description = fetch_title_and_description(video_id)
    fallback_takeaways = []
    if "blog" in entry["label"].lower() or "writing" in entry["label"].lower():
        fallback_takeaways.append("AI로 블로그 글 생산성을 높이는 흐름을 시스템에 흡수할 가치가 높다.")
    if "upload" in entry["label"].lower() or "blogger" in entry["label"].lower():
        fallback_takeaways.append("Blogger 업로드 자동화와 계정 연결 단계를 운영 체크리스트로 분리하는 편이 맞다.")
    if not fallback_takeaways:
        fallback_takeaways.append("실전 적용 순서와 운영 단계 분리를 우선하는 영상이다.")

    try:
        transcript = fetch_transcript(video_id)
        workflow_scores = score_topic_hits(transcript["text"], WORKFLOW_TOPICS)

        workflow_takeaways = []
        if workflow_scores["ai_writing"] > 0:
            workflow_takeaways.append("AI 초안 작성 흐름과 프롬프트 설계를 운영 시스템에 반영할 가치가 높다.")
        if workflow_scores["automation"] > 0:
            workflow_takeaways.append("글 생성보다 자동화 연결과 반복 실행 구조를 함께 강조하는 편이다.")
        if workflow_scores["platform_ops"] > 0:
            workflow_takeaways.append("블로그스팟, 업로드, 계정 연결 같은 운영 단계를 별도 체크리스트로 분리하는 게 맞다.")
        if workflow_scores["monetization"] > 0:
            workflow_takeaways.append("트래픽과 수익 연결을 단순 조회수보다 시스템 관점에서 다룬다.")
        if not workflow_takeaways:
            workflow_takeaways = fallback_takeaways

        relevant_terms = []
        for terms in WORKFLOW_TOPICS.values():
            relevant_terms.extend(terms)

        return {
            "label": entry["label"],
            "url": entry["url"],
            "video_id": video_id,
            "title": title,
            "status": "ok",
            "language_code": transcript["language_code"],
            "is_generated": transcript["is_generated"],
            "workflow_scores": workflow_scores,
            "key_sentences": pick_sentences(transcript["text"], relevant_terms, limit=5),
            "workflow_takeaways": workflow_takeaways,
            "tone_takeaways": infer_tone_takeaways(transcript["text"]),
            "transcript_error": "",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "label": entry["label"],
            "url": entry["url"],
            "video_id": video_id,
            "title": title,
            "status": "transcript_unavailable",
            "language_code": "",
            "is_generated": False,
            "workflow_scores": {},
            "key_sentences": pick_sentences(description, description.split()[:5], limit=2) if len(description) >= MIN_DESCRIPTION_SENTENCE_TEXT else [],
            "workflow_takeaways": fallback_takeaways,
            "tone_takeaways": [
                "실전형 툴 소개 영상은 결과를 먼저 말하고, 단계는 뒤에서 풀어주는 구조를 유지하는 편이 좋다."
            ],
            "transcript_error": str(exc),
        }


def write_markdown(items: list[dict]) -> None:
    lines = []
    lines.append("# Seed Video Analysis")
    lines.append("")
    lines.append("시스템이 참고할 유튜브 시드 영상 분석입니다.")
    lines.append("")
    for item in items:
        lines.append(f"## {item['title']}")
        lines.append("")
        lines.append(f"- label: {item['label']}")
        lines.append(f"- url: {item['url']}")
        lines.append(f"- status: {item['status']}")
        if item.get("transcript_error"):
            lines.append(f"- transcript_error: {item['transcript_error']}")
        else:
            lines.append(f"- transcript: {item['language_code']} / generated={item['is_generated']}")
        lines.append("- workflow takeaways:")
        for takeaway in item["workflow_takeaways"]:
            lines.append(f"  - {takeaway}")
        lines.append("- tone takeaways:")
        for takeaway in item["tone_takeaways"]:
            lines.append(f"  - {takeaway}")
        lines.append("- key sentences:")
        for sentence in item["key_sentences"]:
            lines.append(f"  - {sentence}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    config = load_json(CONFIG_JSON)
    items = [analyze_video(entry) for entry in config.get("videos", [])]
    OUTPUT_JSON.write_text(json.dumps({"items": items}, ensure_ascii=False, indent=2))
    write_markdown(items)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
