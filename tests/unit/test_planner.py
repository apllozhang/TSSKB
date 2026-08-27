from __future__ import annotations

from tsskb.build.planner import BuildPlanner
from tsskb.config import ProjectPaths
from tsskb.content.loader import ContentRepository


def test_global_build_digest_includes_builder_source(project_paths: ProjectPaths) -> None:
    catalog = ContentRepository(project_paths).load(check_files=False).catalog

    global_files = BuildPlanner(project_paths, catalog)._global_files()

    assert project_paths.root / "src" / "tsskb" / "build" / "planner.py" in global_files
