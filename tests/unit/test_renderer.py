from __future__ import annotations

from pathlib import Path

from tsskb.build.renderer import PageRenderer


def test_jinja_autoescapes_configuration_values(tmp_path: Path) -> None:
    (tmp_path / "test.html").write_text("<p>{{ value }}</p>", encoding="utf-8")
    result = PageRenderer(tmp_path).render("test.html", value='<script>alert("x")</script>')
    assert "<script>" not in result
    assert "&lt;script&gt;" in result

