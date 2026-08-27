"""Project paths and environment configuration."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from tsskb.models import EnvironmentConfig


@dataclass(frozen=True, slots=True)
class ProjectPaths:
    root: Path
    content: Path
    books: Path
    templates: Path
    static: Path
    schemas: Path
    dist: Path

    @classmethod
    def discover(cls, root: Path | None = None) -> ProjectPaths:
        project_root = (root or Path.cwd()).resolve()
        if not (project_root / "pyproject.toml").is_file():
            raise FileNotFoundError(f"Not a TSSKB project root: {project_root}")
        return cls(
            root=project_root,
            content=project_root / "content",
            books=project_root / "books",
            templates=project_root / "templates",
            static=project_root / "static",
            schemas=project_root / "schemas",
            dist=project_root / "dist",
        )

    def environment(self, name: str) -> EnvironmentConfig:
        path = self.content / "environments" / f"{name}.json"
        if not path.is_file():
            raise FileNotFoundError(f"Unknown environment {name!r}: {path}")
        return EnvironmentConfig.model_validate_json(path.read_text(encoding="utf-8"))


def stable_json(value: object) -> str:
    """Return a deterministic JSON representation used by build digests."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

