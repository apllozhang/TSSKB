"""Read build artifacts and enforce published capacity budgets."""

from __future__ import annotations

import gzip
import json
from pathlib import Path

from tsskb.models import SearchBudget


def collect_metrics(site: Path) -> dict[str, object]:
    if not site.is_dir():
        raise FileNotFoundError(f"site output is missing: {site}")
    files = [path for path in site.rglob("*") if path.is_file()]
    search_manifest_path = site / "search" / "manifest.json"
    search_manifest = json.loads(search_manifest_path.read_text(encoding="utf-8"))
    titles = (site / "search" / "titles.json").read_bytes()
    shard_raw = sum(int(shard["bytes"]) for shard in search_manifest["shards"])
    shard_gzip = sum(int(shard["gzip_bytes"]) for shard in search_manifest["shards"])
    return {
        "page_count": sum(path.suffix == ".html" for path in files),
        "file_count": len(files),
        "total_bytes": sum(path.stat().st_size for path in files),
        "search_entry_count": int(search_manifest["entry_count"]),
        "search_shard_count": len(search_manifest["shards"]),
        "search_raw_bytes": shard_raw + len(titles),
        "search_gzip_bytes": shard_gzip + len(gzip.compress(titles, compresslevel=9, mtime=0)),
        "max_search_asset_raw_bytes": max(
            [len(titles), *(int(shard["bytes"]) for shard in search_manifest["shards"])]
        ),
        "max_search_asset_gzip_bytes": max(
            [
                len(gzip.compress(titles, compresslevel=9, mtime=0)),
                *(int(shard["gzip_bytes"]) for shard in search_manifest["shards"]),
            ]
        ),
    }


def enforce_metrics(metrics: dict[str, object], budget: SearchBudget) -> None:
    checks = (
        ("search_raw_bytes", budget.total_raw_bytes),
        ("search_gzip_bytes", budget.total_gzip_bytes),
        ("max_search_asset_raw_bytes", budget.max_shard_raw_bytes),
        ("max_search_asset_gzip_bytes", budget.max_shard_gzip_bytes),
    )
    violations = [
        f"{name}={metrics[name]} exceeds {limit}"
        for name, limit in checks
        if int(metrics[name]) > limit
    ]
    if violations:
        raise ValueError("Capacity budget exceeded: " + "; ".join(violations))

