from __future__ import annotations

import importlib


def test_main_module_can_be_imported_without_running_cli() -> None:
    module = importlib.import_module("tsskb.__main__")

    assert callable(module.main)
