"""HTTP health checks executed after an atomic release switch."""

from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.parse import urljoin
from urllib.request import Request, urlopen


@dataclass(frozen=True, slots=True)
class HealthResult:
    url: str
    status: int
    bytes_read: int


def check_release(
    base_url: str,
    *,
    expected_release_id: str | None = None,
    timeout: float = 8.0,
) -> tuple[HealthResult, ...]:
    paths = (
        "",
        "_meta/release-manifest.json",
        "search/manifest.json",
        "postsales/os-lan-access/index.html",
        "assets/ale-logo-color.png",
    )
    results: list[HealthResult] = []
    for path in paths:
        url = urljoin(base_url.rstrip("/") + "/", path)
        request = Request(url, headers={"User-Agent": "tsskb-release-check/2.0"})
        # The URL comes from reviewed environment configuration, not request data.
        with urlopen(request, timeout=timeout) as response:
            body = response.read(128 * 1024)
            status = int(response.status)
        if status != 200:
            raise RuntimeError(f"health check returned HTTP {status}: {url}")
        if path == "_meta/release-manifest.json":
            payload = json.loads(body.decode("utf-8"))
            observed_release_id = str(payload.get("release_id", ""))
            if not observed_release_id:
                raise RuntimeError(f"release manifest has no release_id: {url}")
            if expected_release_id and observed_release_id != expected_release_id:
                raise RuntimeError(
                    "release id mismatch: "
                    f"expected {expected_release_id}, observed {observed_release_id}: {url}"
                )
        elif path == "search/manifest.json":
            payload = json.loads(body.decode("utf-8"))
            if int(payload.get("entry_count", 0)) < 1:
                raise RuntimeError(f"search manifest is empty: {url}")
        results.append(HealthResult(url=url, status=status, bytes_read=len(body)))
    return tuple(results)
