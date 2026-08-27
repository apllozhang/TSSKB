from __future__ import annotations

import pytest

from tsskb.content.markdown import MarkdownRenderer, parse_frontmatter


def test_frontmatter_is_separated_from_body() -> None:
    document = parse_frontmatter("---\nname: example\ndescription: 'Example'\n---\n# Heading\n")
    assert document.metadata == {"name": "example", "description": "Example"}
    assert document.body == "# Heading\n"


def test_invalid_frontmatter_has_line_context() -> None:
    with pytest.raises(ValueError, match="line 2"):
        parse_frontmatter("---\ninvalid\n---\ntext")


def test_markdown_tables_get_responsive_wrapper() -> None:
    rendered = str(MarkdownRenderer().render("| A | B |\n|---|---|\n| 1 | 2 |"))
    assert '<div class="table-scroll"><table>' in rendered
    assert "</table></div>" in rendered


def test_page_markers_become_source_badges() -> None:
    rendered = str(MarkdownRenderer().render("<<<PAGE 12-13>>> evidence"))
    assert "source-page" in rendered
    assert "原文p12-13" in rendered

