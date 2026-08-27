from __future__ import annotations

import json
import shutil
from pathlib import Path

from tsskb.build.pipeline import BuildResult, SiteBuilder
from tsskb.config import ProjectPaths
from tsskb.observability import EventLogger


def test_unchanged_incremental_build_matches_full_output(
    tmp_path: Path,
    built_site: tuple[Path, BuildResult],
    project_paths: ProjectPaths,
) -> None:
    full_site, _ = built_site
    incremental_site = tmp_path / "site"
    shutil.copytree(full_site, incremental_site)
    before = json.loads((incremental_site / "_meta" / "manifest.json").read_text(encoding="utf-8"))

    result = SiteBuilder(project_paths, EventLogger(json_output=False)).build(
        output=incremental_site,
        environment="dev",
        incremental=True,
        strict=True,
    )
    after = json.loads((incremental_site / "_meta" / "manifest.json").read_text(encoding="utf-8"))

    assert result.changed_courses == 0
    assert after["input_digest"] == before["input_digest"]
    assert after["output_digest"] == before["output_digest"]
    assert after["provenance"] == before["provenance"]

