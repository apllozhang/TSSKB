"""Markdown/frontmatter parsing with the portal's readability transforms."""

from __future__ import annotations

import re
from dataclasses import dataclass

import markdown
from markupsafe import Markup

_CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮"


@dataclass(frozen=True, slots=True)
class MarkdownDocument:
    metadata: dict[str, str]
    body: str


def parse_frontmatter(text: str) -> MarkdownDocument:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    metadata: dict[str, str] = {}
    if not match:
        return MarkdownDocument(metadata=metadata, body=text)
    for number, line in enumerate(match.group(1).splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter at line {number}: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return MarkdownDocument(metadata=metadata, body=text[match.end() :])


def _bulletize_dense_blocks(text: str) -> str:
    blocks: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        stripped = block.strip()
        if "\n|" in block or stripped.startswith("|"):
            blocks.append(block)
            continue
        if (
            len(stripped) > 200
            and stripped.count("。") >= 3
            and not stripped.startswith(("#", "|", "-", "*", "!", ">", "`"))
            and not re.match(r"^\d+\.\s", stripped)
        ):
            sentences = [item.strip() for item in stripped.replace("\n", "").split("。") if item.strip()]
            if len(sentences) >= 3:
                blocks.append("\n".join(f"- {item}。" for item in sentences))
                continue
        blocks.append(block)
    return "\n\n".join(blocks)


def preprocess_markdown(text: str) -> str:
    """Improve scanability while preserving tables, code and source quotations."""

    def bulletize_after_heading(match: re.Match[str]) -> str:
        heading, paragraph = match.group(1), match.group(2).strip()
        if paragraph.startswith(("- ", "* ", "1.", "|", "!", ">")):
            return match.group(0)
        sentences = [item.strip() for item in paragraph.split("。") if item.strip()]
        if len(sentences) < 2 or len(paragraph) < 100:
            return match.group(0)
        return heading + "\n" + "\n".join(f"- {item}。" for item in sentences) + "\n"

    text = re.sub(
        r"(^#{1,3}\s*[^\n]+\n+)([^\n#\-*|!>][^\n]*)",
        bulletize_after_heading,
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(r"^\*\*(\d+)\.\s*([^*\n]+)\*\*", r"\1. **\2**", text, flags=re.MULTILINE)
    text = _bulletize_dense_blocks(text)

    def lead_split(match: re.Match[str]) -> str:
        lead, rest = match.group(1).strip(), match.group(2).strip()
        visible = re.sub(r"<[^>]+>", "", lead)
        if not rest or lead.startswith("**") or len(visible) > 52:
            return match.group(0)
        return f"- **{lead}**：<br>{rest}"

    text = re.sub(r"^- ([^：*\n]{2,240})：(.+)$", lead_split, text, flags=re.MULTILINE)
    text = re.sub(
        r"<<<PAGE\s+([\d,\s\-]+)>>>",
        lambda match: f'<span class="source-page">原文p{match.group(1).strip()}</span> ',
        text,
    )

    cleaned: list[str] = []
    for line in text.splitlines():
        if "cangjie" in line.lower():
            line = re.sub(
                r"[*_`\s]*由\s*cangjie-skill\s*流水线[^*\n]*?蒸馏生成\. ?",
                "",
                line,
                flags=re.IGNORECASE,
            )
            line = re.sub(r"cangjie-skill\s*流水线|cangjie-skill", "内部整理流程", line, flags=re.IGNORECASE)
            if not line.strip().strip("*_ `"):
                continue
        cleaned.append(line)
    text = "\n".join(cleaned).replace("蒸馏流水线", "整理流程")

    def split_circled_paragraph(match: re.Match[str]) -> str:
        segment = match.group(0)
        has_markers = any(f"**{item}" in segment or segment.count(item) >= 2 for item in _CIRCLED)
        if segment.count("**") < 4 or not has_markers:
            return segment
        parts = [
            part.strip()
            for part in re.split(r"(?=\**\s*[②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮])", segment)
            if part.strip()
        ]
        return "\n\n".join(parts) if len(parts) > 1 else segment

    text = re.sub(r"^[^\n|>#*\-]{60,}$", split_circled_paragraph, text, flags=re.MULTILINE)

    def source_line(match: re.Match[str]) -> str:
        tokens = [item.strip() for item in re.split(r"[,，]\s*", match.group(2)) if item.strip()]
        return match.group(1) + " · ".join(tokens)

    return re.sub(r"^(来源条目[:：]\s*)(.+)$", source_line, text, flags=re.MULTILINE)


class MarkdownRenderer:
    def render(self, text: str) -> Markup:
        rendered = markdown.markdown(
            preprocess_markdown(text),
            extensions=["tables", "fenced_code", "toc"],
            # types-Markdown 桩尚未收录 html5（运行时 Markdown 3.3+ 支持）
            output_format="html5",  # type: ignore[arg-type]
        )
        rendered = rendered.replace("<table>", '<div class="table-scroll"><table>')
        rendered = rendered.replace("</table>", "</table></div>")
        return Markup(rendered)

