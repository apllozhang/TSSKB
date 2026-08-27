from __future__ import annotations

from pathlib import Path

import pytest

from tsskb.build.validator import validate_site


def test_validator_accepts_root_links_and_anchors(tmp_path: Path) -> None:
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "app.js").write_text("", encoding="utf-8")
    (tmp_path / "index.html").write_text(
        '<main id="top"><a href="/course.html#part">Course</a><script src="/assets/app.js"></script></main>',
        encoding="utf-8",
    )
    (tmp_path / "course.html").write_text('<main><h2 id="part">Part</h2></main>', encoding="utf-8")
    report = validate_site(tmp_path, strict=True)
    assert report.valid
    assert report.page_count == 2


def test_validator_reports_missing_target(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text('<a href="/missing.html">broken</a>', encoding="utf-8")
    with pytest.raises(ValueError, match="target is missing"):
        validate_site(tmp_path, strict=True)

