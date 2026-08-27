"""Host-key-verified SSH/SFTP transport for immutable release directories."""

from __future__ import annotations

import os
import posixpath
import re
import shlex
from pathlib import Path
from typing import Protocol

from tsskb.content.provenance import sha256_file
from tsskb.models import DeployConfig

RELEASE_PATTERN = re.compile(r"^[a-f0-9]{16}$")


class ReleaseTransport(Protocol):
    def current_release(self) -> str | None: ...
    def list_releases(self) -> list[str]: ...
    def upload_release(self, site: Path, release_id: str) -> None: ...
    def verify_release(self, site: Path, release_id: str) -> None: ...
    def activate(self, release_id: str) -> None: ...
    def close(self) -> None: ...


class SftpDirectoryClient(Protocol):
    def stat(self, path: str) -> object: ...
    def mkdir(self, path: str) -> object: ...


class SshReleaseTransport:
    def __init__(self, config: DeployConfig) -> None:
        if not config.host or not config.user or not config.remote_root:
            raise ValueError("deploy host, user and remote_root are required")
        if not config.remote_root.startswith("/"):
            raise ValueError("remote_root must be an absolute POSIX path")
        if any(character in config.remote_root for character in "\n\r\0"):
            raise ValueError("remote_root contains forbidden characters")
        try:
            import paramiko
        except ImportError as exc:
            raise RuntimeError("Install the deployment extra: pip install -e .[deploy]") from exc

        self._paramiko = paramiko
        self.config = config
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        if config.known_hosts:
            self.client.load_host_keys(os.path.expandvars(config.known_hosts))
        self.client.set_missing_host_key_policy(paramiko.RejectPolicy())
        password = os.environ.get("TSSKB_DEPLOY_PASSWORD")
        key_filename = os.environ.get("TSSKB_DEPLOY_KEY")
        self.client.connect(
            hostname=config.host,
            port=config.port,
            username=config.user,
            password=password,
            key_filename=key_filename,
            look_for_keys=True,
            allow_agent=True,
            timeout=12,
        )

    def current_release(self) -> str | None:
        value = self._run(f"readlink {shlex.quote(self.config.remote_root + '/current')} || true").strip()
        return posixpath.basename(value) if value else None

    def list_releases(self) -> list[str]:
        root = shlex.quote(self.config.remote_root + "/releases")
        output = self._run(f"find {root} -mindepth 1 -maxdepth 1 -type d -printf '%f\\n' 2>/dev/null || true")
        return sorted(item for item in output.splitlines() if RELEASE_PATTERN.fullmatch(item))

    def upload_release(self, site: Path, release_id: str) -> None:
        self._validate_release(release_id)
        release_root = posixpath.join(self.config.remote_root or "", "releases", release_id)
        quoted = shlex.quote(release_root)
        exists = self._run(f"test -e {quoted} && echo exists || true").strip()
        if exists:
            raise FileExistsError(f"remote immutable release already exists: {release_id}")
        self._run(f"mkdir -p {quoted}")
        sftp = self.client.open_sftp()
        try:
            for local in sorted(path for path in site.rglob("*") if path.is_file()):
                relative = local.relative_to(site).as_posix()
                remote = posixpath.join(release_root, relative)
                self._mkdirs(sftp, posixpath.dirname(remote))
                sftp.put(str(local), remote)
        finally:
            sftp.close()

    def verify_release(self, site: Path, release_id: str) -> None:
        self._validate_release(release_id)
        relative = "_meta/release-manifest.json"
        local_hash = sha256_file(site / relative)
        remote = posixpath.join(self.config.remote_root or "", "releases", release_id, relative)
        output = self._run(f"sha256sum {shlex.quote(remote)}").split()[0]
        if output != local_hash:
            raise RuntimeError(f"release manifest checksum mismatch: {output} != {local_hash}")

    def activate(self, release_id: str) -> None:
        self._validate_release(release_id)
        root = shlex.quote(self.config.remote_root or "")
        target = shlex.quote(f"releases/{release_id}")
        self._run(
            f"cd {root} && ln -sfn {target} current.next && mv -Tf current.next current"
        )

    def close(self) -> None:
        self.client.close()

    def _run(self, command: str) -> str:
        _, stdout, stderr = self.client.exec_command(command, timeout=60)
        output = stdout.read().decode("utf-8", "replace")
        error = stderr.read().decode("utf-8", "replace")
        status = stdout.channel.recv_exit_status()
        if status:
            raise RuntimeError(f"remote command failed with status {status}: {error.strip()}")
        return output

    @staticmethod
    def _mkdirs(sftp: SftpDirectoryClient, path: str) -> None:
        current = ""
        for part in path.strip("/").split("/"):
            current += "/" + part
            try:
                sftp.stat(current)
            except OSError:
                sftp.mkdir(current)

    @staticmethod
    def _validate_release(release_id: str) -> None:
        if not RELEASE_PATTERN.fullmatch(release_id):
            raise ValueError(f"invalid release id: {release_id!r}")
