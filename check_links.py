"""Compatibility entry point for the unified output validator."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from tsskb.cli import main


if __name__ == "__main__":
    site = sys.argv[1] if len(sys.argv) > 1 else "dist/site"
    raise SystemExit(main(["validate", "--site", site, "--strict"]))
