from __future__ import annotations

import io
from pathlib import Path

import pytest

from tsskb.content.provenance import sha256_file
from tsskb.deploy.transport import SshReleaseTransport
from tsskb.models import DeployConfig


class Channel:
    def __init__(self, status: int = 0) -> None:
        self.status = status

    def recv_exit_status(self) -> int:
        return self.status


class Stream(io.BytesIO):
    def __init__(self, value: bytes, status: int = 0) -> None:
        super().__init__(value)
        self.channel = Channel(status)


class FakeSftp:
    def __init__(self) -> None:
        self.directories: set[str] = set()
        self.uploads: list[tuple[str, str]] = []
        self.closed = False

    def stat(self, path: str) -> None:
        if path not in self.directories:
            raise OSError(path)

    def mkdir(self, path: str) -> None:
        self.directories.add(path)

    def put(self, local: str, remote: str) -> None:
        self.uploads.append((local, remote))

    def close(self) -> None:
        self.closed = True


class FakeClient:
    def __init__(self, outputs: list[str] | None = None) -> None:
        self.outputs = list(outputs or [])
        self.commands: list[str] = []
        self.sftp = FakeSftp()
        self.closed = False

    def exec_command(self, command: str, timeout: int) -> tuple[None, Stream, Stream]:
        del timeout
        self.commands.append(command)
        output = self.outputs.pop(0) if self.outputs else ""
        return None, Stream(output.encode()), Stream(b"")

    def open_sftp(self) -> FakeSftp:
        return self.sftp

    def close(self) -> None:
        self.closed = True


def _transport(client: FakeClient) -> SshReleaseTransport:
    transport = object.__new__(SshReleaseTransport)
    transport.config = DeployConfig(
        host="host",
        user="user",
        remote_root="/srv/tsskb",
    )
    transport.client = client
    return transport


def test_transport_rejects_relative_remote_root() -> None:
    with pytest.raises(ValueError, match="absolute POSIX"):
        SshReleaseTransport(DeployConfig(host="host", user="user", remote_root="relative"))


def test_transport_reads_and_activates_release() -> None:
    client = FakeClient(["releases/1111111111111111\n", "1111111111111111\n2222222222222222\n", ""])
    transport = _transport(client)
    assert transport.current_release() == "1111111111111111"
    assert transport.list_releases() == ["1111111111111111", "2222222222222222"]
    transport.activate("2222222222222222")
    assert "current.next" in client.commands[-1]


def test_transport_uploads_and_verifies_manifest(tmp_path: Path) -> None:
    site = tmp_path / "site"
    manifest = site / "_meta" / "release-manifest.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text("{}", encoding="utf-8")
    release = "2222222222222222"
    client = FakeClient(["", "", f"{sha256_file(manifest)}  file\n"])
    transport = _transport(client)
    transport.upload_release(site, release)
    transport.verify_release(site, release)
    assert client.sftp.uploads[0][1].endswith("/_meta/release-manifest.json")
    transport.close()
    assert client.closed


def test_transport_rejects_untrusted_release_id() -> None:
    transport = _transport(FakeClient())
    with pytest.raises(ValueError, match="invalid release id"):
        transport.activate("../../current")

