"""Strongly typed domain contracts for portal content and release settings."""

from __future__ import annotations

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

SLUG_PATTERN = r"^[a-z0-9]+(?:[a-z0-9-]*/?)*[a-z0-9]$|^[a-z0-9]$"


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SiteInfo(StrictModel):
    name: str = Field(min_length=2, max_length=100)
    short_name: str = Field(min_length=2, max_length=60)
    description: str = Field(min_length=5, max_length=300)
    locale: str = "zh-CN"
    rights_notice: str = Field(min_length=5, max_length=300)


class NavigationItem(StrictModel):
    label: str = Field(min_length=1, max_length=40)
    href: str = Field(pattern=r"^[a-z0-9][a-z0-9_./-]*\.html$")
    category: str | None = None


class SourceInfo(StrictModel):
    book: str = Field(pattern=SLUG_PATTERN)
    rights_scope: Literal["internal-training"] = "internal-training"
    last_verified: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")


class CourseGroup(StrictModel):
    name: str = Field(min_length=1, max_length=80)
    skills: tuple[str, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_skills(self) -> "CourseGroup":
        if len(self.skills) != len(set(self.skills)):
            raise ValueError(f"duplicate skill in group {self.name!r}")
        for slug in self.skills:
            if not re.fullmatch(SLUG_PATTERN, slug):
                raise ValueError(f"invalid skill slug {slug!r}")
        return self


class Course(StrictModel):
    id: str = Field(pattern=SLUG_PATTERN)
    category: str = Field(pattern=SLUG_PATTERN)
    book: str = Field(pattern=SLUG_PATTERN)
    title: str = Field(min_length=3, max_length=180)
    subtitle: str = Field(min_length=3, max_length=300)
    catalog_description: str = Field(min_length=3, max_length=300)
    status: Literal["draft", "review", "published", "archived"] = "published"
    version: str | None = Field(default=None, max_length=80)
    pages: int | None = Field(default=None, ge=1, le=100_000)
    roles: tuple[str, ...] = Field(min_length=1)
    difficulty: Literal["foundation", "intermediate", "advanced"]
    tags: tuple[str, ...] = Field(min_length=1)
    route: tuple[str, ...] = Field(min_length=1)
    groups: tuple[CourseGroup, ...] = Field(min_length=1)
    source: SourceInfo

    @model_validator(mode="after")
    def validate_course(self) -> "Course":
        if self.id.split("/", 1)[0] != self.category:
            raise ValueError("course id must start with its category")
        skills = self.skill_slugs
        if len(skills) != len(set(skills)):
            raise ValueError(f"course {self.id!r} contains duplicate skills")
        return self

    @property
    def skill_slugs(self) -> tuple[str, ...]:
        return tuple(skill for group in self.groups for skill in group.skills)


class PlannedItem(StrictModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=2, max_length=300)


class Category(StrictModel):
    id: str = Field(pattern=SLUG_PATTERN)
    label: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=180)
    accent: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$")
    banner: str | None = Field(default=None, pattern=r"^[a-z0-9][a-z0-9_.-]+$")
    planned_items: tuple[PlannedItem, ...] = ()


class Catalog(StrictModel):
    schema_version: Literal[1]
    site: SiteInfo
    navigation: tuple[NavigationItem, ...] = Field(min_length=1)
    categories: tuple[Category, ...] = Field(min_length=1)
    courses: tuple[Course, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_references(self) -> "Catalog":
        category_ids = [category.id for category in self.categories]
        if len(category_ids) != len(set(category_ids)):
            raise ValueError("category ids must be unique")
        course_ids = [course.id for course in self.courses]
        if len(course_ids) != len(set(course_ids)):
            raise ValueError("course ids must be unique")
        unknown = sorted({course.category for course in self.courses} - set(category_ids))
        if unknown:
            raise ValueError(f"courses reference unknown categories: {unknown}")
        return self


class LearningStep(StrictModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=2, max_length=300)
    href: str = Field(pattern=r"^[a-z0-9][a-z0-9_./-]*\.html$")


class LearningPath(StrictModel):
    id: str = Field(pattern=SLUG_PATTERN)
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=300)
    banner: str = Field(pattern=r"^[a-z0-9][a-z0-9_.-]+$")
    steps: tuple[LearningStep, ...] = Field(min_length=1)


class LearningPaths(StrictModel):
    schema_version: Literal[1]
    paths: tuple[LearningPath, ...] = Field(min_length=1)


class RecentItem(StrictModel):
    date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    title: str = Field(min_length=2, max_length=150)
    href: str | None = Field(default=None, pattern=r"^[a-z0-9][a-z0-9_./-]*\.html$")
    note: str = Field(min_length=2, max_length=300)


class RecentUpdates(StrictModel):
    schema_version: Literal[1]
    items: tuple[RecentItem, ...]


class Redirect(StrictModel):
    from_path: str = Field(pattern=r"^[a-z0-9][a-z0-9_./-]*\.html$")
    to_path: str = Field(pattern=r"^[a-z0-9][a-z0-9_./-]*\.html$")
    reason: str = Field(min_length=5, max_length=240)


class Redirects(StrictModel):
    schema_version: Literal[1]
    redirects: tuple[Redirect, ...]

    @model_validator(mode="after")
    def unique_sources(self) -> "Redirects":
        sources = [redirect.from_path for redirect in self.redirects]
        if len(sources) != len(set(sources)):
            raise ValueError("redirect sources must be unique")
        if any(redirect.from_path == redirect.to_path for redirect in self.redirects):
            raise ValueError("redirect source and target must differ")
        return self


class SearchBudget(StrictModel):
    total_raw_bytes: int = Field(ge=100_000)
    total_gzip_bytes: int = Field(ge=50_000)
    max_shard_raw_bytes: int = Field(ge=50_000)
    max_shard_gzip_bytes: int = Field(ge=20_000)


class DeployConfig(StrictModel):
    enabled: bool = False
    host: str | None = None
    port: int = Field(default=22, ge=1, le=65_535)
    user: str | None = None
    remote_root: str | None = None
    public_url: HttpUrl | None = None
    known_hosts: str | None = None
    keep_releases: int = Field(default=5, ge=2, le=50)


class EnvironmentConfig(StrictModel):
    schema_version: Literal[1]
    name: Literal["dev", "staging", "prod"]
    strict: bool = True
    base_url: str = "/"
    search_budget: SearchBudget
    deploy: DeployConfig
