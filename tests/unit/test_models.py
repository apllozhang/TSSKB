from __future__ import annotations

import pytest
from pydantic import ValidationError

from tsskb.models import Catalog


def _catalog() -> dict[str, object]:
    return {
        "schema_version": 1,
        "site": {
            "name": "Test Portal",
            "short_name": "Portal",
            "description": "A sufficiently descriptive portal",
            "rights_notice": "Internal training content only",
        },
        "navigation": [{"label": "Home", "href": "index.html"}],
        "categories": [
            {
                "id": "postsales",
                "label": "Postsales",
                "description": "Delivery content",
                "accent": "#6B489D",
            }
        ],
        "courses": [
            {
                "id": "postsales/example",
                "category": "postsales",
                "book": "example-book",
                "title": "Example Course",
                "subtitle": "Edition 01 · 10 pages",
                "catalog_description": "Example delivery course",
                "version": "Edition 01",
                "pages": 10,
                "roles": ["support-engineer"],
                "difficulty": "intermediate",
                "tags": ["postsales"],
                "route": ["Start here"],
                "groups": [{"name": "Basics", "skills": ["first-skill"]}],
                "source": {"book": "example-book", "last_verified": "2026-08-27"},
            }
        ],
    }


def test_catalog_accepts_valid_contract() -> None:
    catalog = Catalog.model_validate(_catalog())
    assert catalog.courses[0].skill_slugs == ("first-skill",)


def test_catalog_rejects_unknown_category() -> None:
    payload = _catalog()
    payload["courses"][0]["category"] = "presales"  # type: ignore[index]
    with pytest.raises(ValidationError, match="course id must start"):
        Catalog.model_validate(payload)


def test_course_rejects_duplicate_skill() -> None:
    payload = _catalog()
    payload["courses"][0]["groups"].append(  # type: ignore[index]
        {"name": "Again", "skills": ["first-skill"]}
    )
    with pytest.raises(ValidationError, match="duplicate skills"):
        Catalog.model_validate(payload)

