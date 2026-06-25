#!/usr/bin/env python3
import json
import os
from html import escape
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
FOUNDATION_DIR = ROOT / "outputs/latest/site-foundation"
CONFIG_JSON = ROOT / "config/blog_rendering.json"
OUTPUT_DIR = ROOT / "outputs/latest/site-pages"
OUTPUT_JSON = ROOT / "outputs/latest/site-pages-report.json"
OUTPUT_MD = ROOT / "outputs/latest/site-pages-report.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def markdown_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["extra", "nl2br", "tables"])


def resolve_page_url(base_url: str, slug: str) -> str:
    path = f"/p/{slug}.html"
    if not base_url:
        return path
    return f"{base_url.rstrip('/')}{path}"


def read_foundation_pages() -> list[Path]:
    return sorted(
        path
        for path in FOUNDATION_DIR.glob("*.md")
        if path.name != "site-foundation-index.md"
    )


def build_nav(config: dict, base_url: str) -> str:
    link_map = config.get("internal_link_url_map", {})
    nav_targets = [
        ("거시 허브", link_map.get("site-foundation/hub-macro.md", "/p/hub-macro.html")),
        ("코인 허브", link_map.get("site-foundation/hub-crypto.md", "/p/hub-crypto.html")),
        ("섹터 허브", link_map.get("site-foundation/hub-global-sector.md", "/p/hub-global-sector.html")),
        ("About", link_map.get("site-foundation/about.md", "/p/about.html")),
        ("Disclosure", link_map.get("site-foundation/disclosure.md", "/p/disclosure.html")),
        ("Privacy", link_map.get("site-foundation/privacy-policy.md", "/p/privacy-policy.html")),
        ("Editorial", link_map.get("site-foundation/editorial-policy.md", "/p/editorial-policy.html")),
        ("Contact", link_map.get("site-foundation/contact.md", "/p/contact.html")),
    ]
    items = []
    for label, url in nav_targets:
        resolved = url if url.startswith("http") or not base_url else f"{base_url.rstrip('/')}{url}"
        items.append(f"<li><a href=\"{escape(resolved)}\">{escape(label)}</a></li>")
    return f"<nav class='site-foundation-nav'><ul>{''.join(items)}</ul></nav>"


def build_html_document(config: dict, title: str, body_html: str, nav_html: str, canonical_url: str) -> str:
    canonical_meta = f"<p class='site-page-canonical'><a href=\"{escape(canonical_url)}\">{escape(canonical_url)}</a></p>" if canonical_url else ""
    return (
        "<article class='site-foundation-page'>"
        f"<header class='site-page-header'><h1>{escape(title)}</h1>"
        f"<p>{escape(config.get('site_name', ''))} · {escape(config.get('author_role', ''))}</p>"
        f"{canonical_meta}</header>"
        f"{nav_html}"
        f"<section class='site-page-body'>{body_html}</section>"
        "</article>"
    )


def extract_title(markdown_text: str, fallback: str) -> tuple[str, str]:
    lines = markdown_text.splitlines()
    title = fallback
    body_lines = lines
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            body_lines = lines[idx + 1 :]
        else:
            title = stripped[:120]
            body_lines = lines[idx + 1 :]
        break
    return title, "\n".join(body_lines).strip()


def main() -> int:
    config = load_json(CONFIG_JSON)
    base_url = os.getenv("BLOG_BASE_URL", config.get("default_base_url", "")).strip()
    nav_html = build_nav(config, base_url)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    items = []
    for page_path in read_foundation_pages():
        markdown_text = page_path.read_text()
        slug = page_path.stem
        title, body_md = extract_title(markdown_text, slug.replace("-", " "))
        body_html = markdown_to_html(body_md)
        canonical_url = resolve_page_url(base_url, slug)
        html = build_html_document(config, title, body_html, nav_html, canonical_url)
        html_path = OUTPUT_DIR / f"{slug}.html"
        html_path.write_text(html)
        items.append(
            {
                "slug": slug,
                "title": title,
                "source_markdown": str(page_path),
                "html_path": str(html_path),
                "canonical_url": canonical_url,
            }
        )

    report = {"base_url": base_url, "items": items}
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = ["# Site Foundation Pages", ""]
    for item in items:
        lines.append(f"- `{item['slug']}`: {item['title']}")
        lines.append(f"  - html: {item['html_path']}")
        lines.append(f"  - canonical: {item['canonical_url']}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
