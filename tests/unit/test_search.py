from __future__ import annotations

import json
from pathlib import Path

from tsskb.build.search import build_search_index
from tsskb.models import SearchBudget


def test_search_builds_category_shards(tmp_path: Path) -> None:
    for category, title, term in (
        ("aos", "AOS Routing", "BGP route map"),
        ("wlan", "Stellar WLAN", "radio roaming"),
    ):
        page = tmp_path / category / "course.html"
        page.parent.mkdir(parents=True)
        page.write_text(
            f"<html><head><title>{title}</title></head><body><main><h2 id='part'>{term}</h2><p>details</p></main></body></html>",
            encoding="utf-8",
        )
    budget = SearchBudget(
        total_raw_bytes=100_000,
        total_gzip_bytes=50_000,
        max_shard_raw_bytes=50_000,
        max_shard_gzip_bytes=20_000,
    )
    metrics = build_search_index(tmp_path, budget, enforce_budget=True)
    manifest = json.loads((tmp_path / "search" / "manifest.json").read_text(encoding="utf-8"))
    assert metrics.entry_count == 2
    assert {item["category"] for item in manifest["shards"]} == {"aos", "wlan"}
    assert json.loads((tmp_path / "search" / "shards" / "aos.json").read_text(encoding="utf-8"))[0]["a"] == "part"

