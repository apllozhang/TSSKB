from __future__ import annotations

import json
from pathlib import Path

from tsskb.build.pipeline import BuildResult


def test_full_build_contains_baseline_routes_and_platform_assets(
    built_site: tuple[Path, BuildResult],
) -> None:
    site, result = built_site
    assert result.page_count >= 659
    assert result.validation.valid
    expected = (
        "index.html",
        "paths.html",
        "postsales/os-lan-access/index.html",
        "postsales/os-lan-access/skills/aos-config-management.html",
        "brochures/omniswitch/skills/bp-sw-access-selection.html",
        "assets/ale-logo-color.png",
        "assets/css/tokens.css",
        "assets/js/search-worker.js",
        "search/manifest.json",
        "_meta/manifest.json",
        "_meta/release-manifest.json",
    )
    assert all((site / path).is_file() for path in expected)


def test_search_manifest_is_sharded_and_within_budget(
    built_site: tuple[Path, BuildResult],
) -> None:
    site, result = built_site
    manifest = json.loads((site / "search" / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["shards"]) > 10
    assert result.search.max_shard_raw_bytes < 700_000
    assert result.search.gzip_bytes < 1_500_000

