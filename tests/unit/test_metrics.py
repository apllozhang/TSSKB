from __future__ import annotations

from pathlib import Path

import pytest

from tsskb.build.metrics import collect_metrics, enforce_metrics
from tsskb.build.pipeline import BuildResult
from tsskb.models import SearchBudget


def test_metrics_reports_built_site(built_site: tuple[Path, BuildResult]) -> None:
    site, result = built_site
    metrics = collect_metrics(site)
    assert metrics["page_count"] == result.page_count
    assert metrics["search_shard_count"] == result.search.shard_count


def test_metrics_budget_failure_is_actionable() -> None:
    metrics: dict[str, object] = {
        "search_raw_bytes": 100_001,
        "search_gzip_bytes": 50_000,
        "max_search_asset_raw_bytes": 50_000,
        "max_search_asset_gzip_bytes": 20_000,
    }
    budget = SearchBudget(
        total_raw_bytes=100_000,
        total_gzip_bytes=50_000,
        max_shard_raw_bytes=50_000,
        max_shard_gzip_bytes=20_000,
    )
    with pytest.raises(ValueError, match="search_raw_bytes"):
        enforce_metrics(metrics, budget)

