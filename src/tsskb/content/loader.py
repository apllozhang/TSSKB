"""Load versioned content configuration and validate repository references."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TypeVar

from pydantic import BaseModel, ValidationError

from tsskb.config import ProjectPaths
from tsskb.models import Catalog, LearningPaths, RecentUpdates, Redirects

ModelT = TypeVar("ModelT", bound=BaseModel)


class ContentValidationError(ValueError):
    """Aggregated content errors suitable for CI and author feedback."""

    def __init__(self, issues: list[str]) -> None:
        self.issues = issues
        super().__init__("Content validation failed:\n- " + "\n- ".join(issues))


@dataclass(frozen=True, slots=True)
class ContentBundle:
    catalog: Catalog
    learning_paths: LearningPaths
    recent: RecentUpdates
    redirects: Redirects


class ContentRepository:
    def __init__(self, paths: ProjectPaths) -> None:
        self.paths = paths

    def load(self, *, check_files: bool = True) -> ContentBundle:
        issues: list[str] = []
        catalog = self._model("catalog.json", Catalog, issues)
        learning = self._model("learning_paths.json", LearningPaths, issues)
        recent = self._model("recent.json", RecentUpdates, issues)
        redirects = self._model("redirects.json", Redirects, issues)
        if issues or catalog is None or learning is None or recent is None or redirects is None:
            raise ContentValidationError(issues)
        bundle = ContentBundle(
            catalog=catalog,
            learning_paths=learning,
            recent=recent,
            redirects=redirects,
        )
        issues.extend(self._cross_reference_issues(bundle))
        if check_files:
            issues.extend(self._file_issues(bundle))
        if issues:
            raise ContentValidationError(issues)
        return bundle

    def _model(
        self,
        name: str,
        model: type[ModelT],
        issues: list[str],
    ) -> ModelT | None:
        path = self.paths.content / name
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            return model.model_validate(raw)
        except FileNotFoundError:
            issues.append(f"{path}: file is missing")
        except json.JSONDecodeError as exc:
            issues.append(f"{path}:{exc.lineno}:{exc.colno}: invalid JSON: {exc.msg}")
        except ValidationError as exc:
            for error in exc.errors(include_url=False):
                location = ".".join(str(part) for part in error["loc"])
                issues.append(f"{path}:{location}: {error['msg']}")
        return None

    def _cross_reference_issues(self, bundle: ContentBundle) -> list[str]:
        issues: list[str] = []
        published = {f"{course.id}/index.html" for course in bundle.catalog.courses}
        category_pages = {f"{category.id}/index.html" for category in bundle.catalog.categories}
        valid_targets = published | category_pages
        for path in bundle.learning_paths.paths:
            for step in path.steps:
                if step.href not in valid_targets:
                    issues.append(f"learning_paths.{path.id}: unknown target {step.href!r}")
        generated = {"index.html", "paths.html"} | category_pages
        for course in bundle.catalog.courses:
            generated.update(
                {
                    f"{course.id}/index.html",
                    f"{course.id}/digest.html",
                    f"{course.id}/overview.html",
                    f"{course.id}/glossary.html",
                }
            )
            generated.update(f"{course.id}/skills/{skill}.html" for skill in course.skill_slugs)
            if (self.paths.books / course.book / "GALLERY.md").is_file():
                generated.add(f"{course.id}/gallery.html")
        for redirect in bundle.redirects.redirects:
            if redirect.from_path in generated:
                issues.append(f"redirects: source shadows a generated page: {redirect.from_path!r}")
            if redirect.to_path not in generated:
                issues.append(f"redirects: target is not generated: {redirect.to_path!r}")
        return issues

    def _file_issues(self, bundle: ContentBundle) -> list[str]:
        issues: list[str] = []
        required = ("DIGEST.md", "BOOK_OVERVIEW.md", "GLOSSARY.md")
        for course in bundle.catalog.courses:
            book = self.paths.books / course.book
            if not book.is_dir():
                issues.append(f"course {course.id}: book directory is missing: {book}")
                continue
            for name in required:
                if not (book / name).is_file():
                    issues.append(f"course {course.id}: required source is missing: {book / name}")
            for skill in course.skill_slugs:
                source = book / skill / "SKILL.md"
                if not source.is_file():
                    issues.append(f"course {course.id}: skill source is missing: {source}")
        return issues
