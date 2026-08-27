from __future__ import annotations

import json

from tsskb.config import ProjectPaths
from tsskb.content.loader import ContentRepository
from tsskb.models import Catalog, EnvironmentConfig, LearningPaths, RecentUpdates, Redirects


def test_repository_content_and_cross_references_are_valid(project_paths: ProjectPaths) -> None:
    bundle = ContentRepository(project_paths).load(check_files=True)
    assert len(bundle.catalog.courses) == 65
    assert sum(len(course.skill_slugs) for course in bundle.catalog.courses) == 369
    assert len(bundle.redirects.redirects) == 8


def test_checked_in_json_schemas_match_models(project_paths: ProjectPaths) -> None:
    expected = {
        "catalog.schema.json": Catalog.model_json_schema(),
        "learning-paths.schema.json": LearningPaths.model_json_schema(),
        "recent.schema.json": RecentUpdates.model_json_schema(),
        "redirects.schema.json": Redirects.model_json_schema(),
        "environment.schema.json": EnvironmentConfig.model_json_schema(),
    }
    for name, schema in expected.items():
        checked_in = json.loads((project_paths.schemas / name).read_text(encoding="utf-8"))
        assert checked_in == schema, f"run python tools/export_schemas.py: {name}"

