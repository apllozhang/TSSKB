from __future__ import annotations

import json

import pytest

from tsskb.observability import EventLogger


def test_json_event_logger_emits_machine_readable_events(capsys: pytest.CaptureFixture[str]) -> None:
    logger = EventLogger(json_output=True)
    with logger.timed("example", build_id="abc"):
        pass
    rows = [json.loads(line) for line in capsys.readouterr().out.splitlines()]
    assert [row["event"] for row in rows] == ["example.started", "example.completed"]
    assert rows[-1]["duration_ms"] >= 0


def test_timed_event_reports_failure(capsys: pytest.CaptureFixture[str]) -> None:
    logger = EventLogger(json_output=True)
    with pytest.raises(RuntimeError):
        with logger.timed("example"):
            raise RuntimeError("boom")
    rows = [json.loads(line) for line in capsys.readouterr().out.splitlines()]
    assert rows[-1]["event"] == "example.failed"
    assert rows[-1]["error"] == "RuntimeError"

