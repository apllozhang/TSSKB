"""Small JSON-lines event logger shared by build and release flows."""

from __future__ import annotations

import json
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EventLogger:
    json_output: bool = True

    def emit(self, event: str, **fields: Any) -> None:
        payload = {"event": event, **fields}
        if self.json_output:
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True), file=sys.stdout)
        else:
            detail = " ".join(f"{key}={value}" for key, value in fields.items())
            print(f"[{event}] {detail}".rstrip(), file=sys.stdout)

    @contextmanager
    def timed(self, event: str, **fields: Any) -> Iterator[None]:
        started = time.perf_counter()
        self.emit(f"{event}.started", **fields)
        try:
            yield
        except Exception as exc:
            self.emit(
                f"{event}.failed",
                duration_ms=round((time.perf_counter() - started) * 1000, 2),
                error=type(exc).__name__,
                **fields,
            )
            raise
        self.emit(
            f"{event}.completed",
            duration_ms=round((time.perf_counter() - started) * 1000, 2),
            **fields,
        )

