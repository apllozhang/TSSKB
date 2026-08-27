"""Build-output validation for internal links, anchors, assets and template leaks."""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True, slots=True)
class ValidationReport:
    page_count: int
    reference_count: int
    issues: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.issues


class _ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.references.append((attribute, values[attribute] or ""))


def _resolve(current: PurePosixPath, reference: str) -> tuple[PurePosixPath, str] | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("mailto:", "data:", "javascript:")):
        return None
    raw_path = unquote(parsed.path)
    if not raw_path:
        target = current
    elif raw_path.startswith("/"):
        target = PurePosixPath(raw_path.lstrip("/"))
    else:
        target = current.parent / raw_path
    parts: list[str] = []
    for part in target.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    normalized = PurePosixPath(*parts)
    if raw_path.endswith("/"):
        normalized /= "index.html"
    return normalized, unquote(parsed.fragment)


def validate_site(site: Path, *, strict: bool = True) -> ValidationReport:
    pages = sorted(site.rglob("*.html"))
    parsers: dict[PurePosixPath, _ReferenceParser] = {}
    issues: list[str] = []
    for page in pages:
        relative = PurePosixPath(page.relative_to(site).as_posix())
        text = page.read_text(encoding="utf-8")
        if "{{" in text or "{%" in text:
            issues.append(f"{relative}: unresolved template expression")
        parser = _ReferenceParser()
        parser.feed(text)
        parsers[relative] = parser

    reference_count = 0
    for current, parser in parsers.items():
        for attribute, reference in parser.references:
            reference_count += 1
            resolved = _resolve(current, reference)
            if resolved is None:
                continue
            target, fragment = resolved
            target_disk = site / Path(target.as_posix())
            if not target_disk.exists():
                issues.append(f"{current}: {attribute} target is missing: {reference}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = parsers.get(target)
                if target_parser is not None and fragment not in target_parser.ids:
                    issues.append(f"{current}: anchor is missing: {reference}")

    report = ValidationReport(
        page_count=len(pages),
        reference_count=reference_count,
        issues=tuple(sorted(set(issues))),
    )
    if strict and report.issues:
        preview = "\n- ".join(report.issues[:50])
        suffix = f"\n... and {len(report.issues) - 50} more" if len(report.issues) > 50 else ""
        raise ValueError(f"Site validation failed:\n- {preview}{suffix}")
    return report

