"""Compatibility entry point for the versioned deployment workflow.

The previous script deleted the live directory before upload. This wrapper keeps
the familiar filename but routes operators to the dry-run-first release command.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from tsskb.cli import main


if __name__ == "__main__":
    print("Legacy destructive deployment is disabled; using immutable release workflow.")
    raise SystemExit(main(["deploy", "--environment", "prod", *sys.argv[1:]]))
