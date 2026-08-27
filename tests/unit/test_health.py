from __future__ import annotations

import json

import pytest

from tsskb.deploy.health import check_release


class FakeResponse:
    def __init__(self, body: bytes, status: int = 200) -> None:
        self.body = body
        self.status = status

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_: object) -> None:
        return None

    def read(self, _: int) -> bytes:
        return self.body


def test_release_health_checks_required_endpoints(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_open(request: object, timeout: float) -> FakeResponse:
        del timeout
        url = request.full_url  # type: ignore[attr-defined]
        if url.endswith("_meta/release-manifest.json"):
            return FakeResponse(json.dumps({"release_id": "a" * 16}).encode())
        if url.endswith("search/manifest.json"):
            return FakeResponse(json.dumps({"entry_count": 10}).encode())
        return FakeResponse(b"ok")

    monkeypatch.setattr("tsskb.deploy.health.urlopen", fake_open)
    results = check_release("https://portal.internal/", expected_release_id="a" * 16)
    assert len(results) == 5
    assert all(result.status == 200 for result in results)


def test_release_health_rejects_empty_search(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_open(request: object, timeout: float) -> FakeResponse:
        del timeout
        url = request.full_url  # type: ignore[attr-defined]
        if url.endswith("_meta/release-manifest.json"):
            body = json.dumps({"release_id": "a" * 16}).encode()
        elif url.endswith("search/manifest.json"):
            body = json.dumps({"entry_count": 0}).encode()
        else:
            body = b"ok"
        return FakeResponse(body)

    monkeypatch.setattr("tsskb.deploy.health.urlopen", fake_open)
    with pytest.raises(RuntimeError, match="search manifest is empty"):
        check_release("https://portal.internal/")


def test_release_health_rejects_stale_release(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_open(request: object, timeout: float) -> FakeResponse:
        del timeout
        url = request.full_url  # type: ignore[attr-defined]
        if url.endswith("_meta/release-manifest.json"):
            return FakeResponse(json.dumps({"release_id": "a" * 16}).encode())
        if url.endswith("search/manifest.json"):
            return FakeResponse(json.dumps({"entry_count": 10}).encode())
        return FakeResponse(b"ok")

    monkeypatch.setattr("tsskb.deploy.health.urlopen", fake_open)
    with pytest.raises(RuntimeError, match="release id mismatch"):
        check_release("https://portal.internal/", expected_release_id="b" * 16)
