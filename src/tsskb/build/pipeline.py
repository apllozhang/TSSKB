"""End-to-end content validation, rendering, indexing and artifact verification."""

from __future__ import annotations

import json
import os
import re
import shutil
import time
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from markupsafe import Markup

from tsskb.build.manifest import write_manifests
from tsskb.build.planner import BuildPlan, BuildPlanner
from tsskb.build.renderer import PageRenderer
from tsskb.build.search import SearchMetrics, build_search_index
from tsskb.build.validator import ValidationReport, validate_site
from tsskb.config import ProjectPaths, stable_json
from tsskb.content.loader import ContentBundle, ContentRepository
from tsskb.content.markdown import MarkdownDocument, MarkdownRenderer, parse_frontmatter
from tsskb.models import Category, Course
from tsskb.observability import EventLogger


@dataclass(frozen=True, slots=True)
class BuildResult:
    output: Path
    build_id: str
    mode: str
    changed_courses: int
    page_count: int
    total_bytes: int
    duration_ms: float
    search: SearchMetrics
    validation: ValidationReport


class SiteBuilder:
    def __init__(self, paths: ProjectPaths, logger: EventLogger | None = None) -> None:
        self.paths = paths
        self.logger = logger or EventLogger()
        self.pages = PageRenderer(paths.templates)
        self.markdown = MarkdownRenderer()
        self.provenance: dict[str, list[str]] = {}

    def build(
        self,
        *,
        output: Path,
        environment: str = "dev",
        incremental: bool = False,
        strict: bool | None = None,
    ) -> BuildResult:
        started = time.perf_counter()
        self.provenance = {}
        bundle = ContentRepository(self.paths).load(check_files=True)
        env = self.paths.environment(environment)
        strict_mode = env.strict if strict is None else strict
        plan = BuildPlanner(self.paths, bundle.catalog).create(output, incremental=incremental)
        self.logger.emit(
            "build.plan",
            mode=plan.mode,
            courses=len(bundle.catalog.courses),
            changed_courses=len(plan.changed_courses),
            input_digest=plan.input_digest,
        )

        if incremental and output.is_dir():
            work = output
            self.provenance.update(self._previous_provenance(output))
        else:
            work = output.parent / f".{output.name}.build-{os.getpid()}"
            if work.exists():
                shutil.rmtree(work)
            work.mkdir(parents=True)

        self._copy_static(work)
        self._render_portal(work, bundle)
        categories = {category.id: category for category in bundle.catalog.categories}
        selected = [
            course for course in bundle.catalog.courses if course.id in plan.changed_courses
        ]
        for course in selected:
            self._render_course(work, bundle, categories[course.category], course)
        self._render_redirects(work, bundle)

        search = build_search_index(work, env.search_budget, enforce_budget=strict_mode)
        manifest = write_manifests(
            work,
            project_root=self.paths.root,
            input_digest=plan.input_digest,
            course_digests=plan.course_digests,
            provenance=self.provenance,
            search=search,
        )
        self._write_cache(work, plan)
        validation = validate_site(work, strict=strict_mode)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        total_bytes = sum(path.stat().st_size for path in work.rglob("*") if path.is_file())
        metrics = {
            "schema_version": 1,
            "generated_at": datetime.now(UTC).isoformat(),
            "build_id": manifest["build_id"],
            "mode": plan.mode,
            "duration_ms": duration_ms,
            "page_count": validation.page_count,
            "reference_count": validation.reference_count,
            "total_bytes": total_bytes,
            "changed_courses": len(plan.changed_courses),
            "search": asdict(search),
        }
        (work / "_meta" / "build-metrics.json").write_text(
            json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        if work != output:
            self._publish_local(work, output, str(manifest["build_id"]))
        result = BuildResult(
            output=output,
            build_id=str(manifest["build_id"]),
            mode=plan.mode,
            changed_courses=len(plan.changed_courses),
            page_count=validation.page_count,
            total_bytes=total_bytes,
            duration_ms=duration_ms,
            search=search,
            validation=validation,
        )
        self.logger.emit(
            "build.completed",
            build_id=result.build_id,
            mode=result.mode,
            duration_ms=result.duration_ms,
            page_count=result.page_count,
            total_bytes=result.total_bytes,
            search_bytes=result.search.raw_bytes,
        )
        return result

    def _base_context(self, bundle: ContentBundle, *, active_nav: str, page_kind: str) -> dict[str, object]:
        return {
            "site": bundle.catalog.site,
            "navigation": bundle.catalog.navigation,
            "active_nav": active_nav,
            "page_kind": page_kind,
        }

    def _render_portal(self, output: Path, bundle: ContentBundle) -> None:
        courses_by_category = {
            category.id: [course for course in bundle.catalog.courses if course.category == category.id]
            for category in bundle.catalog.categories
        }
        common = self._base_context(bundle, active_nav="home", page_kind="home")
        self._write(
            output,
            "index.html",
            self.pages.render(
                "home.html",
                **common,
                categories=bundle.catalog.categories,
                courses_by_category=courses_by_category,
                recent=bundle.recent,
                metrics={
                    "course_count": len(bundle.catalog.courses),
                    "skill_count": sum(len(course.skill_slugs) for course in bundle.catalog.courses),
                },
            ),
            ["content/catalog.json", "content/recent.json"],
        )
        self._write(
            output,
            "paths.html",
            self.pages.render(
                "paths.html",
                **self._base_context(bundle, active_nav="paths", page_kind="paths"),
                learning_paths=bundle.learning_paths,
            ),
            ["content/learning_paths.json"],
        )
        for category in bundle.catalog.categories:
            courses = courses_by_category[category.id]
            self._write(
                output,
                f"{category.id}/index.html",
                self.pages.render(
                    "category.html",
                    **self._base_context(bundle, active_nav=category.id, page_kind="category"),
                    category=category,
                    courses=courses,
                ),
                ["content/catalog.json"],
            )

    def _render_course(
        self,
        output: Path,
        bundle: ContentBundle,
        category: Category,
        course: Course,
    ) -> None:
        book = self.paths.books / course.book
        documents: dict[str, MarkdownDocument] = {}
        skill_titles: dict[str, str] = {}
        skill_descriptions: dict[str, str] = {}
        for slug in course.skill_slugs:
            source = book / slug / "SKILL.md"
            document = parse_frontmatter(source.read_text(encoding="utf-8"))
            documents[slug] = document
            skill_titles[slug] = self._heading(document.body, slug)
            skill_descriptions[slug] = document.metadata.get("description", "")

        has_gallery = (book / "GALLERY.md").is_file()
        course_context = {
            **self._base_context(bundle, active_nav=course.category, page_kind="course"),
            "category": category,
            "course": course,
            "has_gallery": has_gallery,
            "skill_titles": skill_titles,
            "skill_descriptions": skill_descriptions,
        }
        self._write(
            output,
            f"{course.id}/index.html",
            self.pages.render("course_landing.html", **course_context, current="landing"),
            ["content/catalog.json", f"books/{course.book}"],
        )

        reference_pages = (
            ("DIGEST.md", "精华长文 DIGEST", "digest", "digest.html"),
            ("BOOK_OVERVIEW.md", "教书理解 BOOK_OVERVIEW", "overview", "overview.html"),
            ("GLOSSARY.md", "术语词典", "glossary", "glossary.html"),
        )
        for source_name, title, current, target in reference_pages:
            source = book / source_name
            body = self._link_skills(self.markdown.render(source.read_text(encoding="utf-8")), course)
            self._write(
                output,
                f"{course.id}/{target}",
                self.pages.render(
                    "content.html",
                    **course_context,
                    current=current,
                    title=title,
                    body_html=body,
                    skill_slug=None,
                    source_chapter=None,
                    previous_href=None,
                    previous_label=None,
                    next_href=None,
                    next_label=None,
                ),
                [f"books/{course.book}/{source_name}"],
            )

        skills = course.skill_slugs
        for index, slug in enumerate(skills):
            document = documents[slug]
            previous_href = (
                f"/{course.id}/skills/{skills[index - 1]}.html" if index else f"/{course.id}/index.html"
            )
            previous_label = skill_titles[skills[index - 1]] if index else "返回课程首页"
            next_href = (
                f"/{course.id}/skills/{skills[index + 1]}.html"
                if index < len(skills) - 1
                else f"/{course.id}/digest.html"
            )
            next_label = skill_titles[skills[index + 1]] if index < len(skills) - 1 else "查看课程精华"
            body = self._link_skills(self.markdown.render(document.body), course)
            self._write(
                output,
                f"{course.id}/skills/{slug}.html",
                self.pages.render(
                    "content.html",
                    **course_context,
                    current=slug,
                    title=skill_titles[slug],
                    body_html=body,
                    skill_slug=slug,
                    source_chapter=document.metadata.get("source_chapter"),
                    previous_href=previous_href,
                    previous_label=previous_label,
                    next_href=next_href,
                    next_label=next_label,
                ),
                [f"books/{course.book}/{slug}/SKILL.md"],
            )

        image_source = book / "images"
        if image_source.is_dir():
            shutil.copytree(
                image_source,
                output / course.id / "skills" / "images",
                dirs_exist_ok=True,
            )
        if has_gallery:
            source = book / "GALLERY.md"
            gallery = str(self.markdown.render(source.read_text(encoding="utf-8")))
            gallery = gallery.replace('src="images/', f'src="/{course.id}/skills/images/')
            gallery = self._gallery_figures(gallery)
            self._write(
                output,
                f"{course.id}/gallery.html",
                self.pages.render(
                    "gallery.html",
                    **course_context,
                    current="gallery",
                    body_html=Markup(gallery),
                ),
                [f"books/{course.book}/GALLERY.md", f"books/{course.book}/images"],
            )

    def _render_redirects(self, output: Path, bundle: ContentBundle) -> None:
        for redirect in bundle.redirects.redirects:
            self._write(
                output,
                redirect.from_path,
                self.pages.render("redirect.html", site=bundle.catalog.site, redirect=redirect),
                ["content/redirects.json"],
            )

    @staticmethod
    def _heading(body: str, fallback: str) -> str:
        match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        if not match:
            return fallback
        return re.sub(r"[*_`]", "", match.group(1)).strip()

    @staticmethod
    def _link_skills(body: Markup, course: Course) -> Markup:
        value = str(body)
        for slug in course.skill_slugs:
            value = value.replace(
                f">{slug}<", f'><a href="/{course.id}/skills/{slug}.html">{slug}</a><'
            )
        return Markup(value)

    @staticmethod
    def _gallery_figures(value: str) -> str:
        def figure(match: re.Match[str]) -> str:
            attrs = match.group(1)
            alt_match = re.search(r'alt="([^"]*)"', attrs)
            caption = alt_match.group(1) if alt_match else ""
            return f"<figure><img {attrs} loading=\"lazy\"><figcaption>{caption}</figcaption></figure>"

        value = re.sub(r"<p><img\s+([^>]+)></p>", figure, value)
        return re.sub(r"(?<!<figure>)<img\s+([^>]+)>", figure, value)

    def _copy_static(self, output: Path) -> None:
        asset_root = output / "assets"
        asset_root.mkdir(parents=True, exist_ok=True)
        for source in self.paths.static.iterdir():
            if source.name == "assets" and source.is_dir():
                shutil.copytree(source, asset_root, dirs_exist_ok=True)
            elif source.is_dir():
                shutil.copytree(source, asset_root / source.name, dirs_exist_ok=True)
            elif source.is_file():
                shutil.copy2(source, asset_root / source.name)

    def _write(self, output: Path, relative: str, value: str, inputs: list[str]) -> None:
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value, encoding="utf-8", newline="\n")
        self.provenance[relative] = inputs

    @staticmethod
    def _write_cache(output: Path, plan: BuildPlan) -> None:
        cache = {
            "schema_version": 1,
            "global_digest": plan.global_digest,
            "course_digests": plan.course_digests,
        }
        (output / "_meta" / "cache.json").write_text(stable_json(cache), encoding="utf-8")

    @staticmethod
    def _previous_provenance(output: Path) -> dict[str, list[str]]:
        try:
            manifest = json.loads((output / "_meta" / "manifest.json").read_text(encoding="utf-8"))
            value = manifest.get("provenance", {})
            return {
                str(path): [str(source) for source in sources]
                for path, sources in value.items()
                if isinstance(sources, list)
            }
        except (FileNotFoundError, json.JSONDecodeError, AttributeError):
            return {}

    @staticmethod
    def _publish_local(work: Path, output: Path, build_id: str) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists():
            backup_root = output.parent / "backups"
            backup_root.mkdir(exist_ok=True)
            stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
            output.rename(backup_root / f"{output.name}-{build_id}-{stamp}")
        work.rename(output)
