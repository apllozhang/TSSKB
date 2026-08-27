"""Generate category shards and a light title index for client-side search."""

from __future__ import annotations

import gzip
import html
import json
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

from tsskb.config import stable_json
from tsskb.content.provenance import sha256_bytes
from tsskb.models import SearchBudget


@dataclass(frozen=True, slots=True)
class SearchMetrics:
    entry_count: int
    shard_count: int
    raw_bytes: int
    gzip_bytes: int
    max_shard_raw_bytes: int
    max_shard_gzip_bytes: int


class _PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.main_parts: list[str] = []
        self.sections: list[dict[str, str]] = []
        self._in_title = False
        self._in_main = False
        self._skip_depth = 0
        self._heading_level: str | None = None
        self._heading_id = ""
        self._heading_parts: list[str] = []
        self._section_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "main":
            self._in_main = True
        if self._in_main and tag in {"nav", "script", "style", "footer"}:
            self._skip_depth += 1
        if self._in_main and not self._skip_depth and tag in {"h2", "h3"}:
            self._finish_section()
            self._heading_level = tag
            self._heading_id = attributes.get("id") or ""
            self._heading_parts = []
            self._section_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if self._in_main and tag in {"nav", "script", "style", "footer"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "main":
            self._finish_section()
            self._in_main = False
        if self._heading_level == tag:
            self._heading_level = None

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if not value:
            return
        if self._in_title:
            self.title_parts.append(value)
        if not self._in_main or self._skip_depth:
            return
        self.main_parts.append(value)
        if self._heading_level:
            self._heading_parts.append(value)
        elif self._heading_parts:
            self._section_parts.append(value)

    def close(self) -> None:
        super().close()
        self._finish_section()

    def _finish_section(self) -> None:
        if not self._heading_parts:
            return
        self.sections.append(
            {
                "a": self._heading_id,
                "s": " ".join(self._heading_parts),
                "x": " ".join(self._section_parts)[:400],
            }
        )
        self._heading_parts = []
        self._section_parts = []
        self._heading_id = ""


def _page_entries(path: Path, root: Path) -> list[dict[str, str]]:
    relative = path.relative_to(root).as_posix()
    parser = _PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    title = html.unescape(" ".join(parser.title_parts)).strip() or relative
    category = relative.split("/", 1)[0] if "/" in relative else "core"
    if parser.sections:
        return [
            {"u": relative, "a": row["a"], "s": row["s"], "t": title, "x": row["x"], "c": category}
            for row in parser.sections
        ]
    body = " ".join(parser.main_parts)[:400]
    return [{"u": relative, "a": "", "s": title.split(" — ", 1)[0], "t": title, "x": body, "c": category}]


def build_search_index(site: Path, budget: SearchBudget, *, enforce_budget: bool) -> SearchMetrics:
    entries: list[dict[str, str]] = []
    for page in sorted(site.rglob("*.html")):
        if page.name == "index.html" and page.parent == site:
            continue
        entries.extend(_page_entries(page, site))

    by_category: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        by_category.setdefault(entry["c"], []).append(entry)

    search_root = site / "search"
    shard_root = search_root / "shards"
    shard_root.mkdir(parents=True, exist_ok=True)
    shards: list[dict[str, object]] = []
    total_raw = 0
    total_gzip = 0
    max_raw = 0
    max_gzip = 0
    target_shard_bytes = min(450_000, budget.max_shard_raw_bytes - 10_000)
    for category, rows in sorted(by_category.items()):
        chunks: list[list[dict[str, str]]] = []
        current: list[dict[str, str]] = []
        current_size = 2
        for row in rows:
            row_size = len(stable_json(row).encode("utf-8")) + 1
            if current and current_size + row_size > target_shard_bytes:
                chunks.append(current)
                current = []
                current_size = 2
            current.append(row)
            current_size += row_size
        if current:
            chunks.append(current)
        for index, chunk in enumerate(chunks, start=1):
            shard_id = category if len(chunks) == 1 else f"{category}-{index:02d}"
            payload = stable_json(chunk).encode("utf-8")
            compressed = gzip.compress(payload, compresslevel=9, mtime=0)
            relative = f"search/shards/{shard_id}.json"
            (site / relative).write_bytes(payload)
            raw_size = len(payload)
            gzip_size = len(compressed)
            total_raw += raw_size
            total_gzip += gzip_size
            max_raw = max(max_raw, raw_size)
            max_gzip = max(max_gzip, gzip_size)
            shards.append(
                {
                    "id": shard_id,
                    "category": category,
                    "url": relative,
                    "entries": len(chunk),
                    "bytes": raw_size,
                    "gzip_bytes": gzip_size,
                    "sha256": sha256_bytes(payload),
                }
            )

    # Candidate routing only needs category/title/section. URLs and anchors stay in
    # the body shards, which keeps the eagerly loaded index materially smaller.
    title_rows = [{key: row[key] for key in ("s", "t", "c")} for row in entries]
    titles_payload = stable_json(title_rows).encode("utf-8")
    (search_root / "titles.json").write_bytes(titles_payload)
    titles_gzip_bytes = len(gzip.compress(titles_payload, compresslevel=9, mtime=0))
    total_raw += len(titles_payload)
    total_gzip += titles_gzip_bytes
    max_raw = max(max_raw, len(titles_payload))
    max_gzip = max(max_gzip, titles_gzip_bytes)
    manifest = {
        "schema_version": 1,
        "entry_count": len(entries),
        "title_index_bytes": len(titles_payload),
        "title_index_gzip_bytes": titles_gzip_bytes,
        "shards": shards,
    }
    (search_root / "manifest.json").write_text(stable_json(manifest), encoding="utf-8")

    metrics = SearchMetrics(
        entry_count=len(entries),
        shard_count=len(shards),
        raw_bytes=total_raw,
        gzip_bytes=total_gzip,
        max_shard_raw_bytes=max_raw,
        max_shard_gzip_bytes=max_gzip,
    )
    if enforce_budget:
        violations = []
        if total_raw > budget.total_raw_bytes:
            violations.append(f"raw search bytes {total_raw} > {budget.total_raw_bytes}")
        if total_gzip > budget.total_gzip_bytes:
            violations.append(f"gzip search bytes {total_gzip} > {budget.total_gzip_bytes}")
        if max_raw > budget.max_shard_raw_bytes:
            violations.append(f"largest raw shard {max_raw} > {budget.max_shard_raw_bytes}")
        if max_gzip > budget.max_shard_gzip_bytes:
            violations.append(f"largest gzip shard {max_gzip} > {budget.max_shard_gzip_bytes}")
        if violations:
            raise ValueError("Search capacity budget exceeded: " + "; ".join(violations))
    return metrics
