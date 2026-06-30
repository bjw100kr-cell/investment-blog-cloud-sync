#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import requests
try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:  # pragma: no cover
    YouTubeTranscriptApi = None


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/investment_sources.json"
DEFAULT_OUTPUT_JSON = ROOT / "outputs/latest/source-snapshot.json"
DEFAULT_OUTPUT_MD = ROOT / "outputs/latest/source-snapshot.md"

USER_AGENT = "Mozilla/5.0 (Codex Investment Blog Research Bot)"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
HTML_TAG_RE = re.compile(r"<[^>]+>")
NAVER_DATALAB_URL = "https://openapi.naver.com/v1/datalab/search"
TRANSCRIPT_LANGUAGES = ["ko", "en"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect daily investment blog source candidates.")
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("--output-json", default=str(DEFAULT_OUTPUT_JSON))
    parser.add_argument("--output-md", default=str(DEFAULT_OUTPUT_MD))
    parser.add_argument("--limit-per-source", type=int, default=8)
    return parser.parse_args()


def load_config(path: Path) -> dict:
    return json.loads(path.read_text())


def fetch_text(url: str) -> str:
    response = requests.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    return response.text.lstrip("\ufeff").lstrip("ï»¿")


def clean_text(value: str) -> str:
    if not value:
        return ""
    value = HTML_TAG_RE.sub(" ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_sentences(text: str) -> list:
    chunks = re.split(r"(?<=[.!?])\s+|(?<=[다요죠])\s+|\n+", text)
    return [clean_text(chunk) for chunk in chunks if clean_text(chunk)]


def parse_rss_items(xml_text: str, limit: int) -> list:
    root = ET.fromstring(xml_text)
    items = []
    for item in root.findall("./channel/item")[:limit]:
        title = clean_text(item.findtext("title", ""))
        link = clean_text(item.findtext("link", ""))
        pub_date = clean_text(item.findtext("pubDate", ""))
        description = clean_text(item.findtext("description", ""))
        approx_traffic = ""
        for child in item:
            if child.tag.endswith("approx_traffic"):
                approx_traffic = clean_text(child.text or "")
                break
        items.append(
            {
                "title": title,
                "link": link,
                "published": pub_date,
                "description": description,
                "approx_traffic": approx_traffic,
            }
        )
    return items


def parse_youtube_items(xml_text: str, limit: int) -> list:
    root = ET.fromstring(xml_text)
    items = []
    for entry in root.findall("atom:entry", ATOM_NS)[:limit]:
        title = clean_text(entry.findtext("atom:title", "", ATOM_NS))
        link = ""
        link_elem = entry.find("atom:link[@rel='alternate']", ATOM_NS)
        if link_elem is not None:
            link = clean_text(link_elem.attrib.get("href", ""))
        published = clean_text(entry.findtext("atom:published", "", ATOM_NS))
        video_id = clean_text(entry.findtext("yt:videoId", "", ATOM_NS))
        items.append(
            {
                "title": title,
                "link": link,
                "published": published,
                "description": "",
                "approx_traffic": "",
                "video_id": video_id,
            }
        )
    return items


def parse_manual_items(html_text: str, source_url: str, limit: int) -> list:
    page_title_match = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    page_title = clean_text(page_title_match.group(1)) if page_title_match else "최신 업데이트"

    heading_pattern = r"<(?:h1|h2|h3)[^>]*>(.*?)</(?:h1|h2|h3)>"
    link_pattern = r"<a[^>]+href=[\"'](?P<link>[^\"']+)[\"'][^>]*>(?P<title>[^<]+)</a>"

    raw_titles = [clean_text(text) for text in re.findall(heading_pattern, html_text, re.IGNORECASE | re.DOTALL)]
    raw_titles += [clean_text(match[1]) for match in re.findall(link_pattern, html_text, re.IGNORECASE | re.DOTALL)]
    seen = set()
    items = []
    for raw_title in raw_titles:
        title = raw_title.strip()
        if len(title) < 8 or title in seen:
            continue
        seen.add(title)
        items.append(
            {
                "title": title,
                "link": source_url,
                "published": "",
                "description": "",
                "approx_traffic": "",
            }
        )
        if len(items) >= limit:
            break

    if not items:
        items.append(
            {
                "title": page_title,
                "link": source_url,
                "published": "",
                "description": "",
                "approx_traffic": "",
            }
        )

    return items


def parse_youtube_channel_items(html_text: str, limit: int) -> list:
    pattern = re.compile(
        r'"videoId":"(?P<video_id>[^"]+)".{0,5000}?"lockupMetadataViewModel":\{"title":\{"content":"(?P<title>[^"]+)"\},"metadata":\{"contentMetadataViewModel":\{"metadataRows":\[\{"metadataParts":\[\{"text":\{"content":"(?P<published>[^"]+)"',
        re.DOTALL,
    )
    items = []
    seen = set()
    for match in pattern.finditer(html_text):
        video_id = clean_text(match.group("video_id"))
        if not video_id or video_id in seen:
            continue
        seen.add(video_id)
        items.append(
            {
                "title": clean_text(match.group("title")),
                "link": f"https://www.youtube.com/watch?v={video_id}",
                "published": clean_text(match.group("published")),
                "description": "",
                "approx_traffic": "",
                "video_id": video_id,
            }
        )
        if len(items) >= limit:
            break
    return items


def build_transcript_digest(text: str, aliases: dict, max_points: int = 3) -> list:
    sentences = split_sentences(text)
    if not sentences:
        return []

    digest = []
    seen = set()
    for sentence in sentences:
        hits = find_keywords(sentence, aliases)
        if not hits:
            continue
        normalized = sentence[:220]
        if normalized in seen:
            continue
        digest.append(normalized)
        seen.add(normalized)
        if len(digest) >= max_points:
            return digest

    return [sentence[:220] for sentence in sentences[:max_points]]


def fetch_youtube_transcript(video_id: str, aliases: dict) -> dict:
    if not video_id:
        return {"available": False, "reason": "missing video_id"}
    if YouTubeTranscriptApi is None:
        return {"available": False, "reason": "youtube-transcript-api not installed"}

    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        try:
            transcript = transcript_list.find_transcript(TRANSCRIPT_LANGUAGES)
            mode = "preferred"
        except Exception:  # noqa: BLE001
            transcript = next(iter(transcript_list), None)
            mode = "fallback"

        if transcript is None:
            return {"available": False, "reason": "no transcript tracks available"}

        fetched = transcript.fetch()
        snippets = fetched.to_raw_data()
        combined_text = clean_text(" ".join(snippet.get("text", "") for snippet in snippets))

        return {
            "available": True,
            "language": getattr(fetched, "language", ""),
            "language_code": getattr(fetched, "language_code", ""),
            "is_generated": getattr(fetched, "is_generated", False),
            "mode": mode,
            "snippet_count": len(snippets),
            "excerpt": combined_text[:1000],
            "digest_points": build_transcript_digest(combined_text, aliases),
        }
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "reason": str(exc)}


def extract_traffic_score(value: str) -> int:
    if not value:
        return 0
    digits = re.sub(r"[^0-9]", "", value)
    if not digits:
        return 0
    base = int(digits)
    return min(max(base // 100, 1), 100)


def find_keywords(text: str, aliases: dict) -> list:
    haystack = text.lower()
    hits = []
    for canonical, variations in aliases.items():
        for variant in variations:
            if variant.lower() in haystack:
                hits.append(canonical)
                break
    return hits


def rank_keywords(all_items: list, aliases: dict) -> list:
    keyword_scores = Counter()
    keyword_sources = defaultdict(set)
    for item in all_items:
        title = item["title"]
        text = f"{title} {item.get('description', '')} {item.get('transcript_excerpt', '')}"
        hits = find_keywords(text, aliases)
        base_weight = item["source_weight"]
        traffic_bonus = extract_traffic_score(item.get("approx_traffic", ""))
        score = base_weight + traffic_bonus
        for keyword in hits:
            keyword_scores[keyword] += score
            keyword_sources[keyword].add(item["source_name"])

    ranked = []
    for keyword, score in keyword_scores.most_common():
        ranked.append(
            {
                "keyword": keyword,
                "score": score,
                "source_count": len(keyword_sources[keyword]),
                "sources": sorted(keyword_sources[keyword]),
            }
        )
    return ranked


def collect_sources(config: dict, limit_per_source: int) -> tuple[list, list]:
    items = []
    source_status = []

    for source in config["sources"]:
        status = {
            "id": source["id"],
            "name": source["name"],
            "type": source["type"],
            "enabled": source.get("enabled", True),
            "ok": False,
            "count": 0,
            "error": "",
        }

        if not source.get("enabled", True):
            status["error"] = source.get("notes", "disabled")
            source_status.append(status)
            continue

        try:
            xml_text = fetch_text(source["url"])
            if source["type"] == "rss":
                parsed_items = parse_rss_items(xml_text, limit_per_source)
            elif source["type"] == "youtube_rss":
                parsed_items = parse_youtube_items(xml_text, limit_per_source)
            elif source["type"] == "youtube_channel":
                parsed_items = parse_youtube_channel_items(xml_text, limit_per_source)
            elif source["type"] == "manual":
                parsed_items = parse_manual_items(xml_text, source["url"], limit_per_source)
            else:
                raise ValueError(f"Unsupported source type: {source['type']}")

            for item in parsed_items:
                if source["type"] in {"youtube_rss", "youtube_channel"}:
                    transcript_info = fetch_youtube_transcript(item.get("video_id", ""), config["keyword_aliases"])
                    item["transcript_available"] = transcript_info.get("available", False)
                    item["transcript_reason"] = transcript_info.get("reason", "")
                    item["transcript_language"] = transcript_info.get("language", "")
                    item["transcript_language_code"] = transcript_info.get("language_code", "")
                    item["transcript_is_generated"] = transcript_info.get("is_generated", False)
                    item["transcript_mode"] = transcript_info.get("mode", "")
                    item["transcript_excerpt"] = transcript_info.get("excerpt", "")
                    item["transcript_digest_points"] = transcript_info.get("digest_points", [])
                item["source_id"] = source["id"]
                item["source_name"] = source["name"]
                item["source_category"] = source["category"]
                item["source_type"] = source["type"]
                item["source_weight"] = source["weight"]
                items.append(item)

            status["ok"] = True
            status["count"] = len(parsed_items)
        except Exception as exc:  # noqa: BLE001
            status["error"] = str(exc)

        source_status.append(status)
        time.sleep(0.25)

    return items, source_status


def build_topic_candidates(items: list, aliases: dict) -> list:
    grouped = defaultdict(list)
    for item in items:
        hits = find_keywords(f"{item['title']} {item.get('description', '')} {item.get('transcript_excerpt', '')}", aliases)
        if not hits:
            continue
        for keyword in hits:
            grouped[keyword].append(item)

    candidates = []
    for keyword, keyword_items in grouped.items():
        score = sum(i["source_weight"] + extract_traffic_score(i.get("approx_traffic", "")) for i in keyword_items)
        candidates.append(
            {
                "keyword": keyword,
                "score": score,
                "headline_count": len(keyword_items),
                "sample_titles": [i["title"] for i in keyword_items[:3]],
            }
        )

    candidates.sort(key=lambda x: (-x["score"], -x["headline_count"], x["keyword"]))
    return candidates


def fetch_naver_datalab(candidates: list, aliases: dict) -> Optional[dict]:
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        return None

    keyword_groups = []
    for candidate in candidates[:5]:
        keyword = candidate["keyword"]
        keyword_groups.append(
            {
                "groupName": keyword,
                "keywords": aliases.get(keyword, [keyword]),
            }
        )

    if not keyword_groups:
        return None

    end_date = datetime.now(timezone.utc).date()
    start_date = end_date - timedelta(days=7)
    body = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "timeUnit": "date",
        "keywordGroups": keyword_groups,
    }
    response = requests.post(
        NAVER_DATALAB_URL,
        timeout=30,
        headers={
            "User-Agent": USER_AGENT,
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
            "Content-Type": "application/json",
        },
        json=body,
    )
    response.raise_for_status()
    data = response.json()

    ranked = []
    for result in data.get("results", []):
        ratios = [entry.get("ratio", 0) for entry in result.get("data", [])]
        latest = ratios[-1] if ratios else 0
        avg = sum(ratios) / len(ratios) if ratios else 0
        ranked.append(
            {
                "keyword": result.get("title", ""),
                "latest_ratio": latest,
                "avg_ratio": round(avg, 2),
            }
        )

    ranked.sort(key=lambda x: (-x["latest_ratio"], -x["avg_ratio"], x["keyword"]))
    return {
        "window": {
            "startDate": body["startDate"],
            "endDate": body["endDate"],
        },
        "ranked": ranked,
    }


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))


def write_markdown(path: Path, payload: dict) -> None:
    lines = []
    lines.append("# 투자 블로그 소스 스냅샷")
    lines.append("")
    lines.append(f"- 생성 시각: `{payload['generated_at']}`")
    lines.append(f"- 수집 성공 소스: `{payload['summary']['ok_sources']}`")
    lines.append(f"- 수집 아이템 수: `{payload['summary']['item_count']}`")
    lines.append("")
    lines.append("## 소스 상태")
    lines.append("")
    for status in payload["source_status"]:
        flag = "OK" if status["ok"] else "SKIP"
        detail = f"{status['count']} items" if status["ok"] else status["error"]
        lines.append(f"- `{flag}` {status['name']} ({status['type']}): {detail}")
    youtube_items = [item for item in payload["items"] if item.get("source_type") in {"youtube_rss", "youtube_channel"}]
    if youtube_items:
        lines.append("")
        lines.append("## 유튜브 transcript 포인트")
        lines.append("")
        for item in youtube_items[:6]:
            lines.append(f"- `{item['source_name']}` / {item['title']}")
            if item.get("transcript_available"):
                lines.append(
                    f"  - transcript: {item.get('transcript_language_code', '')}, generated={item.get('transcript_is_generated', False)}"
                )
                for point in item.get("transcript_digest_points", [])[:3]:
                    lines.append(f"  - {point}")
            else:
                lines.append(f"  - transcript unavailable: {item.get('transcript_reason', '')}")
    lines.append("")
    lines.append("## 상위 키워드")
    lines.append("")
    for item in payload["ranked_keywords"][:10]:
        lines.append(
            f"- `{item['keyword']}`: score {item['score']}, source_count {item['source_count']}, sources {', '.join(item['sources'])}"
        )
    if payload.get("naver_datalab"):
        lines.append("")
        lines.append("## 네이버 데이터랩 비교")
        lines.append("")
        for item in payload["naver_datalab"]["ranked"]:
            lines.append(
                f"- `{item['keyword']}`: latest_ratio {item['latest_ratio']}, avg_ratio {item['avg_ratio']}"
            )
    lines.append("")
    lines.append("## 오늘의 글감 후보")
    lines.append("")
    for candidate in payload["topic_candidates"][:10]:
        lines.append(f"- `{candidate['keyword']}`: score {candidate['score']}, headlines {candidate['headline_count']}")
        for title in candidate["sample_titles"]:
            lines.append(f"  - {title}")
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    args = parse_args()
    config = load_config(Path(args.config))
    items, source_status = collect_sources(config, args.limit_per_source)
    ranked_keywords = rank_keywords(items, config["keyword_aliases"])
    topic_candidates = build_topic_candidates(items, config["keyword_aliases"])
    naver_datalab = fetch_naver_datalab(topic_candidates, config["keyword_aliases"])

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "ok_sources": sum(1 for s in source_status if s["ok"]),
            "item_count": len(items),
        },
        "source_status": source_status,
        "ranked_keywords": ranked_keywords,
        "topic_candidates": topic_candidates,
        "naver_datalab": naver_datalab,
        "items": items,
    }

    write_json(Path(args.output_json), payload)
    write_markdown(Path(args.output_md), payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
