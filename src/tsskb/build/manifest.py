"""Deterministic output manifest and release metadata."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from tsskb.build.search import SearchMetrics
from tsskb.config import stable_json
from tsskb.content.provenance import sha256_bytes, sha256_file


def source_revision(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def write_manifests(
    site: Path,
    *,
    project_root: Path,
    input_digest: str,
    course_digests: dict[str, str],
    provenance: dict[str, list[str]],
    search: SearchMetrics,
) -> dict[str, object]:
    metadata_root = site / "_meta"
    metadata_root.mkdir(parents=True, exist_ok=True)
    files: dict[str, dict[str, object]] = {}
    for path in sorted(item for item in site.rglob("*") if item.is_file() and "_meta" not in item.parts):
        relative = path.relative_to(site).as_posix()
        files[relative] = {"bytes": path.stat().st_size, "sha256": sha256_file(path)}
    output_digest = sha256_bytes(stable_json(files).encode("utf-8"))
    build_id = input_digest[:16]
    manifest: dict[str, object] = {
        "schema_version": 1,
        "build_id": build_id,
        "source_revision": source_revision(project_root),
        "input_digest": input_digest,
        "output_digest": output_digest,
        "files": files,
        "provenance": dict(sorted(provenance.items())),
        "search": {
            "entries": search.entry_count,
            "shards": search.shard_count,
            "raw_bytes": search.raw_bytes,
            "gzip_bytes": search.gzip_bytes,
            "max_shard_raw_bytes": search.max_shard_raw_bytes,
            "max_shard_gzip_bytes": search.max_shard_gzip_bytes,
        },
    }
    manifest_payload = stable_json(manifest)
    (metadata_root / "manifest.json").write_text(manifest_payload, encoding="utf-8")
    release = {
        "schema_version": 1,
        "release_id": build_id,
        "input_digest": input_digest,
        "output_digest": output_digest,
        "manifest_sha256": sha256_bytes(manifest_payload.encode("utf-8")),
    }
    (metadata_root / "release-manifest.json").write_text(stable_json(release), encoding="utf-8")
    cache = {
        "schema_version": 1,
        "global_digest": input_digest if not course_digests else None,
        "course_digests": course_digests,
    }
    # ``global_digest`` is overwritten by the pipeline with the planner's exact value.
    (metadata_root / "cache.json").write_text(stable_json(cache), encoding="utf-8")
    return manifest
