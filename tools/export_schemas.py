"""Export the Pydantic contracts as reviewable JSON Schema files."""

from __future__ import annotations

import json
from pathlib import Path

from tsskb.models import Catalog, EnvironmentConfig, LearningPaths, RecentUpdates, Redirects

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    output = ROOT / "schemas"
    output.mkdir(exist_ok=True)
    schemas = {
        "catalog.schema.json": Catalog.model_json_schema(),
        "learning-paths.schema.json": LearningPaths.model_json_schema(),
        "recent.schema.json": RecentUpdates.model_json_schema(),
        "redirects.schema.json": Redirects.model_json_schema(),
        "environment.schema.json": EnvironmentConfig.model_json_schema(),
    }
    for name, schema in schemas.items():
        (output / name).write_text(
            json.dumps(schema, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(f"exported {len(schemas)} schemas to {output}")


if __name__ == "__main__":
    main()
