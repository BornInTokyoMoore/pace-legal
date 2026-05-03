from __future__ import annotations

import html
import re
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify as markdown_slugify


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "source"
TEMPLATE_PATH = ROOT / "template.html"

PAGES = [
    {
        "source": SOURCE_DIR / "PACE_HEALTH_PRIVACY_POLICY.md",
        "output": ROOT / "health-privacy.html",
        "nav": "health",
        "description": "Pace consumer health data policy required by Washington's My Health My Data Act.",
        "canonical_url": "https://usepace.fit/health-privacy",
        "strip_first_comment": True,
    },
    {
        "source": SOURCE_DIR / "PACE_PRIVACY_POLICY.md",
        "output": ROOT / "privacy.html",
        "nav": "privacy",
        "description": "How Pace handles your personal information.",
        "canonical_url": "https://usepace.fit/privacy",
        "strip_first_comment": False,
    },
    {
        "source": SOURCE_DIR / "PACE_TERMS_OF_SERVICE.md",
        "output": ROOT / "terms.html",
        "nav": "terms",
        "description": "The terms governing your use of the Pace app.",
        "canonical_url": "https://usepace.fit/terms",
        "strip_first_comment": False,
    },
]

TABLE_RE = re.compile(r"(<table>.*?</table>)", re.DOTALL)
COMMENT_RE = re.compile(r"\n?<!--.*?-->\n?", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
TAG_RE = re.compile(r"<[^>]+>")
NUMBERED_HEADING_RE = re.compile(r"^(\d+(?:\.\d+)*)\b")


def extract_title(source: str) -> str:
    match = H1_RE.search(source)
    if not match:
        raise ValueError("Source markdown does not contain an H1 title.")
    title = match.group(1)
    title = re.sub(r"[*_`]+", "", title)
    return html.unescape(title).strip()


def strip_internal_comment(source: str) -> str:
    return COMMENT_RE.sub("\n", source, count=1).strip() + "\n"


def slugify_heading(value: str, separator: str) -> str:
    text = html.unescape(TAG_RE.sub("", value)).strip()
    match = NUMBERED_HEADING_RE.match(text)
    if match:
        return "section-" + match.group(1).replace(".", separator)
    return markdown_slugify(value, separator)


def render_markdown(source: str) -> str:
    rendered = markdown.markdown(
        source,
        extensions=["extra", "toc", "sane_lists", "smarty"],
        extension_configs={
            "toc": {
                "slugify": slugify_heading,
            }
        },
        output_format="html5",
    )
    return TABLE_RE.sub(r'<div class="table-wrapper">\n\1\n</div>', rendered)


def apply_template(
    template: str,
    *,
    title: str,
    description: str,
    canonical_url: str,
    nav: str,
    content: str,
) -> str:
    replacements = {
        "{{title}}": html.escape(title, quote=True),
        "{{description}}": html.escape(description, quote=True),
        "{{canonical_url}}": html.escape(canonical_url, quote=True),
        "{{content}}": content,
        "{{home_active}}": ' class="active"' if nav == "home" else "",
        "{{privacy_active}}": ' class="active"' if nav == "privacy" else "",
        "{{health_active}}": ' class="active"' if nav == "health" else "",
        "{{terms_active}}": ' class="active"' if nav == "terms" else "",
    }
    page = template
    for placeholder, value in replacements.items():
        page = page.replace(placeholder, value)
    return page


def main() -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    generated = []

    for page in PAGES:
        source_path = page["source"]
        output_path = page["output"]
        source = source_path.read_text(encoding="utf-8")
        render_source = strip_internal_comment(source) if page["strip_first_comment"] else source
        title = extract_title(source)
        body = render_markdown(render_source)
        output = apply_template(
            template,
            title=title,
            description=page["description"],
            canonical_url=page["canonical_url"],
            nav=page["nav"],
            content=body,
        )
        output_path.write_text(output, encoding="utf-8")
        generated.append((source_path, output_path, source, output))

    print("Generated policy HTML:")
    for source_path, output_path, source, output in generated:
        size = output_path.stat().st_size
        print(
            f"- {source_path.relative_to(ROOT)} -> {output_path.name}: "
            f"{size:,} bytes, {len(source):,} source chars, {len(output):,} output chars"
        )


if __name__ == "__main__":
    main()
