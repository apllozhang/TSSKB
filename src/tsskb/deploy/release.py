"""Safe release promotion and rollback orchestration."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from tsskb.deploy.health import HealthResult, check_release
from tsskb.deploy.transport import ReleaseTransport, SshReleaseTransport
from tsskb.models import DeployConfig, EnvironmentConfig
from tsskb.observability import EventLogger


@dataclass(frozen=True, slots=True)
class ReleaseResult:
    status: str
    release_id: str | None
    previous_release: str | None
    steps: tuple[str, ...]
    health: tuple[HealthResult, ...] = ()


class ReleaseService:
    def __init__(
        self,
        logger: EventLogger | None = None,
        transport_factory: Callable[[DeployConfig], ReleaseTransport] | None = None,
    ) -> None:
        self.logger = logger or EventLogger()
        self.transport_factory = transport_factory or SshReleaseTransport

    def deploy(self, site: Path, environment: EnvironmentConfig, *, dry_run: bool) -> ReleaseResult:
        release_manifest = json.loads(
            (site / "_meta" / "release-manifest.json").read_text(encoding="utf-8")
        )
        release_id = str(release_manifest["release_id"])
        steps = (
            f"upload immutable release releases/{release_id}",
            "verify release-manifest checksum",
            "atomically switch current symlink",
            "check homepage, search, representative course and brand asset",
            "restore previous symlink automatically on health-check failure",
        )
        if dry_run:
            self.logger.emit("deploy.dry_run", environment=environment.name, release_id=release_id)
            return ReleaseResult("dry-run", release_id, None, steps)
        if not environment.deploy.enabled:
            raise PermissionError(f"deployment is disabled in {environment.name}.json")
        if not environment.deploy.public_url:
            raise ValueError("deploy.public_url is required for health checks")

        transport = self.transport_factory(environment.deploy)
        previous: str | None = None
        try:
            previous = transport.current_release()
            self.logger.emit("deploy.upload.started", environment=environment.name, release_id=release_id)
            transport.upload_release(site, release_id)
            transport.verify_release(site, release_id)
            transport.activate(release_id)
            try:
                health = check_release(
                    str(environment.deploy.public_url),
                    expected_release_id=release_id,
                )
            except Exception:
                if previous:
                    transport.activate(previous)
                    self.logger.emit(
                        "deploy.auto_rollback",
                        environment=environment.name,
                        failed_release=release_id,
                        restored_release=previous,
                    )
                raise
            self.logger.emit("deploy.completed", environment=environment.name, release_id=release_id)
            return ReleaseResult("deployed", release_id, previous, steps, health)
        finally:
            transport.close()

    def rollback(
        self,
        environment: EnvironmentConfig,
        *,
        target: str | None,
        dry_run: bool,
    ) -> ReleaseResult:
        steps = (
            "read current immutable release",
            "select requested or previous release",
            "atomically switch current symlink",
            "run the standard health-check suite",
        )
        if dry_run:
            self.logger.emit("rollback.dry_run", environment=environment.name, target=target)
            return ReleaseResult("dry-run", target, None, steps)
        if not environment.deploy.enabled:
            raise PermissionError(f"deployment is disabled in {environment.name}.json")
        if not environment.deploy.public_url:
            raise ValueError("deploy.public_url is required for health checks")

        transport = self.transport_factory(environment.deploy)
        try:
            current = transport.current_release()
            releases = transport.list_releases()
            candidate = target or next((item for item in reversed(releases) if item != current), None)
            if not candidate:
                raise RuntimeError("no previous release is available")
            transport.activate(candidate)
            try:
                health = check_release(
                    str(environment.deploy.public_url),
                    expected_release_id=candidate,
                )
            except Exception:
                if current:
                    transport.activate(current)
                    self.logger.emit(
                        "rollback.compensated",
                        environment=environment.name,
                        failed_release=candidate,
                        restored_release=current,
                    )
                raise
            self.logger.emit(
                "rollback.completed",
                environment=environment.name,
                release_id=candidate,
                previous_release=current,
            )
            return ReleaseResult("rolled-back", candidate, current, steps, health)
        finally:
            transport.close()
