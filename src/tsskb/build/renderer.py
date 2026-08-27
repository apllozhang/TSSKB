"""Jinja2 rendering boundary with mandatory auto-escaping."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape


class PageRenderer:
    def __init__(self, templates: Path) -> None:
        self.environment = Environment(
            loader=FileSystemLoader(templates),
            autoescape=select_autoescape(default_for_string=True, default=True),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.environment.filters["course_code"] = self._course_code

    @staticmethod
    def _course_code(title: str) -> str:
        return title.split(" · ", 1)[0]

    def render(self, template: str, **context: Any) -> str:
        return self.environment.get_template(template).render(**context)

