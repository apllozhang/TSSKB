from __future__ import annotations

import json
from pathlib import Path

import pytest

from tsskb.deploy.health import HealthResult
from tsskb.deploy.release import ReleaseService
from tsskb.models import EnvironmentConfig


class FakeTransport:
    def __init__(self) -> None:
        self.current = "1111111111111111"
        self.releases = [self.current, "2222222222222222"]
        self.actions: list[tuple[str, str | None]] = []

    def current_release(self) -> str | None:
        return self.current

    def list_releases(self) -> list[str]:
        return self.releases

    def upload_release(self, site: Path, release_id: str) -> None:
        self.actions.append(("upload", release_id))

    def verify_release(self, site: Path, release_id: str) -> None:
        self.actions.append(("verify", release_id))

    def activate(self, release_id: str) -> None:
        self.current = release_id
        self.actions.append(("activate", release_id))

    def close(self) -> None:
        self.actions.append(("close", None))


def _environment() -> EnvironmentConfig:
    return EnvironmentConfig.model_validate(
        {
            "schema_version": 1,
            "name": "staging",
            "search_budget": {
                "total_raw_bytes": 100_000,
                "total_gzip_bytes": 50_000,
                "max_shard_raw_bytes": 50_000,
                "max_shard_gzip_bytes": 20_000,
            },
            "deploy": {
                "enabled": True,
                "host": "example.internal",
                "user": "release",
                "remote_root": "/srv/tsskb",
                "public_url": "https://example.internal/",
            },
        }
    )


def _site(tmp_path: Path) -> Path:
    site = tmp_path / "site" / "_meta"
    site.mkdir(parents=True)
    (site / "release-manifest.json").write_text(
        json.dumps({"release_id": "2222222222222222"}), encoding="utf-8"
    )
    return site.parent


def test_deploy_activates_only_after_upload_and_verification(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    transport = FakeTransport()
    monkeypatch.setattr(
        "tsskb.deploy.release.check_release",
        lambda _, **__: (HealthResult("https://example.internal/", 200, 10),),
    )
    result = ReleaseService(transport_factory=lambda _: transport).deploy(
        _site(tmp_path), _environment(), dry_run=False
    )
    assert result.status == "deployed"
    assert transport.actions[:3] == [
        ("upload", "2222222222222222"),
        ("verify", "2222222222222222"),
        ("activate", "2222222222222222"),
    ]


def test_failed_health_check_restores_previous_release(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    transport = FakeTransport()
    monkeypatch.setattr(
        "tsskb.deploy.release.check_release",
        lambda _, **__: (_ for _ in ()).throw(RuntimeError("down")),
    )
    with pytest.raises(RuntimeError, match="down"):
        ReleaseService(transport_factory=lambda _: transport).deploy(
            _site(tmp_path), _environment(), dry_run=False
        )
    assert ("activate", "1111111111111111") in transport.actions


def test_rollback_selects_previous_release(monkeypatch: pytest.MonkeyPatch) -> None:
    transport = FakeTransport()
    transport.current = "2222222222222222"
    monkeypatch.setattr("tsskb.deploy.release.check_release", lambda _, **__: ())
    result = ReleaseService(transport_factory=lambda _: transport).rollback(
        _environment(), target=None, dry_run=False
    )
    assert result.release_id == "1111111111111111"
    assert transport.current == "1111111111111111"


def test_failed_rollback_health_check_restores_current_release(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    transport = FakeTransport()
    transport.current = "2222222222222222"
    monkeypatch.setattr(
        "tsskb.deploy.release.check_release",
        lambda _, **__: (_ for _ in ()).throw(RuntimeError("down")),
    )

    with pytest.raises(RuntimeError, match="down"):
        ReleaseService(transport_factory=lambda _: transport).rollback(
            _environment(), target=None, dry_run=False
        )

    assert transport.actions[-3:] == [
        ("activate", "1111111111111111"),
        ("activate", "2222222222222222"),
        ("close", None),
    ]
    assert transport.current == "2222222222222222"
