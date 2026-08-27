"""Compatibility entry point for the modular TSSKB 2.x build pipeline."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from tsskb.cli import main

if __name__ == "__main__":
    print("TSSKB 2.x: building governed output in dist/site (legacy site/ is preserved).")
    raise SystemExit(main(["build", "--output", "dist/site", "--full", "--strict", *sys.argv[1:]]))
