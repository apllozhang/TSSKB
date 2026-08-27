from __future__ import annotations

from pathlib import Path

import pytest

from tsskb.build.pipeline import BuildResult, SiteBuilder
from tsskb.config import ProjectPaths
from tsskb.observability import EventLogger


@pytest.fixture(scope="session")
def project_paths() -> ProjectPaths:
    return ProjectPaths.discover(Path(__file__).resolve().parents[1])


@pytest.fixture(scope="session")
def built_site(
    tmp_path_factory: pytest.TempPathFactory,
    project_paths: ProjectPaths,
) -> tuple[Path, BuildResult]:
    output = tmp_path_factory.mktemp("tsskb-build") / "site"
    result = SiteBuilder(project_paths, EventLogger(json_output=False)).build(
        output=output,
        environment="dev",
        incremental=False,
        strict=True,
    )
    return output, result

