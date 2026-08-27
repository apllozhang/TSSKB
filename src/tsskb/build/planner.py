"""Digest-based full and course-level incremental build planning."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from tsskb.config import ProjectPaths, stable_json
from tsskb.content.provenance import digest_files, sha256_bytes
from tsskb.models import Catalog, Course


@dataclass(frozen=True, slots=True)
class BuildPlan:
    mode: str
    input_digest: str
    global_digest: str
    course_digests: dict[str, str]
    changed_courses: frozenset[str]


class BuildPlanner:
    def __init__(self, paths: ProjectPaths, catalog: Catalog) -> None:
        self.paths = paths
        self.catalog = catalog

    def create(self, output: Path, *, incremental: bool) -> BuildPlan:
        global_files = self._global_files()
        global_digest = digest_files(global_files, self.paths.root)
        course_digests = {
            course.id: self._course_digest(course, global_digest) for course in self.catalog.courses
        }
        input_payload = {
            "global": global_digest,
            "courses": course_digests,
        }
        input_digest = sha256_bytes(stable_json(input_payload).encode("utf-8"))
        previous = self._previous_cache(output) if incremental else None
        all_courses = frozenset(course_digests)
        if not previous or previous.get("global_digest") != global_digest:
            changed = all_courses
        else:
            previous_value = previous.get("course_digests", {})
            previous_courses = previous_value if isinstance(previous_value, dict) else {}
            changed = frozenset(
                course_id
                for course_id, digest in course_digests.items()
                if previous_courses.get(course_id) != digest
            )
        return BuildPlan(
            mode="incremental" if incremental else "full",
            input_digest=input_digest,
            global_digest=global_digest,
            course_digests=course_digests,
            changed_courses=changed,
        )

    def _global_files(self) -> list[Path]:
        roots = (
            self.paths.content,
            self.paths.templates,
            self.paths.static,
            self.paths.schemas,
            self.paths.root / "src" / "tsskb",
        )
        files = [path for root in roots for path in root.rglob("*") if path.is_file()]
        files.extend(
            path
            for path in (self.paths.root / "pyproject.toml",)
            if path.is_file()
        )
        return files

    def _course_digest(self, course: Course, global_digest: str) -> str:
        book = self.paths.books / course.book
        files = [path for path in book.rglob("*") if path.is_file()]
        book_digest = digest_files(files, self.paths.root)
        payload = {
            "global": global_digest,
            "book": book_digest,
            "course": course.model_dump(mode="json"),
        }
        return sha256_bytes(stable_json(payload).encode("utf-8"))

    @staticmethod
    def _previous_cache(output: Path) -> dict[str, object] | None:
        path = output / "_meta" / "cache.json"
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            return value if isinstance(value, dict) else None
        except (FileNotFoundError, json.JSONDecodeError):
            return None
