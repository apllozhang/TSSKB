from __future__ import annotations

from pathlib import Path

import pytest

from tsskb.cli import main
from tsskb.config import ProjectPaths


def test_cli_validates_repository(
    project_paths: ProjectPaths,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["--root", str(project_paths.root), "validate"]) == 0
    assert '"status": "valid"' in capsys.readouterr().out


def test_cli_deploy_and_rollback_dry_runs() -> None:
    root = Path(__file__).resolve().parents[2]
    assert main(["--root", str(root), "deploy", "--environment", "staging", "--dry-run"]) == 0
    assert main(["--root", str(root), "rollback", "--environment", "staging", "--dry-run"]) == 0


def test_cli_reports_missing_site() -> None:
    root = Path(__file__).resolve().parents[2]
    assert main(["--root", str(root), "metrics", "--site", "does-not-exist"]) == 2


def test_cli_serve_closes_cleanly_on_keyboard_interrupt(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname='test'\n", encoding="utf-8")
    (tmp_path / "dist" / "site").mkdir(parents=True)

    class FakeServer:
        closed = False

        def __init__(self, *_: object, **__: object) -> None:
            pass

        def serve_forever(self) -> None:
            raise KeyboardInterrupt

        def server_close(self) -> None:
            self.closed = True

    server = FakeServer()
    monkeypatch.setattr("tsskb.cli.http.server.ThreadingHTTPServer", lambda *_: server)

    assert main(["--root", str(tmp_path), "serve"]) == 0
    assert server.closed is True
    assert "Server stopped." in capsys.readouterr().out
