"""One-time, deterministic extraction of literal portal data from build_site.py.

The migration deliberately evaluates only constants, containers and ``dict(...)``
calls. It never imports the legacy generator because importing that module writes
to ``site/`` as a side effect.
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "tools" / "legacy" / "build_site_v1.py"
EXTRACTED_ON = "2026-08-27"

CATEGORY_IDS = {
    "售前 · Presales": "presales",
    "售后 · Postsales": "postsales",
    "OV2500 配置手册 · Manuals": "manuals",
    "AOS 软件手册 · Software Guides": "aos",
    "硬件手册 · Hardware Guides": "hardware",
    "产品彩页 · Product Datasheets": "brochures",
    "解决方案 · Solutions": "solutions",
    "无线网络 · WLAN": "wlan",
    "有线网络 · LAN Switching": "lan",
    "云网管 · Cloud base Management": "cloud",
    "安全 · Security": "security",
    "认证与学习路径 · Certification": "certification",
}

CATEGORY_DESCRIPTIONS = {
    "presales": "方案、选型、竞争与商务能力",
    "postsales": "实施、交付、运维与故障排查",
    "manuals": "OmniVista 平台部署与配置参考",
    "aos": "AOS 软件功能、命令与版本参考",
    "hardware": "OmniSwitch 硬件安装与规格参考",
    "brochures": "产品组合和官方数据表速查",
    "solutions": "行业与技术方案设计指南",
    "wlan": "Stellar WLAN 专题资料",
    "lan": "园区有线网络专题资料",
    "cloud": "云网管和体验分析专题资料",
    "security": "网络准入与基础设施安全",
    "certification": "课程目录、认证体系与学习路径",
}

ROLE_BY_CATEGORY = {
    "presales": ["presales-engineer"],
    "postsales": ["support-engineer", "delivery-engineer"],
    "certification": ["learner", "training-manager"],
}


def evaluate(node: ast.AST) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.List):
        return [evaluate(item) for item in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(evaluate(item) for item in node.elts)
    if isinstance(node, ast.Dict):
        return {
            evaluate(key): evaluate(value)
            for key, value in zip(node.keys, node.values, strict=True)
        }
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "dict":
        if node.args:
            raise ValueError("positional dict arguments are not allowed")
        return {item.arg: evaluate(item.value) for item in node.keywords}
    raise ValueError(f"Unsupported legacy expression: {ast.dump(node, include_attributes=False)}")


def constant(module: ast.Module, name: str) -> Any:
    for statement in module.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in statement.targets
        ):
            return evaluate(statement.value)
    raise KeyError(name)


def version_and_pages(subtitle: str) -> tuple[str | None, int | None]:
    version_match = re.match(
        r"^(Edition\s+\S+|Issue\s+\S+|Rev\s+\S+|AWOS\s+[\d.]+|\d+\.\d+R\d+)",
        subtitle,
    )
    pages_match = re.search(r"(\d[\d,]*)\s*页", subtitle)
    version = version_match.group(1) if version_match else None
    pages = int(pages_match.group(1).replace(",", "")) if pages_match else None
    return version, pages


def dump(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    module = ast.parse(LEGACY.read_text(encoding="utf-8"), filename=str(LEGACY))
    courses = constant(module, "NEW_COURSES")
    catalog_groups = constant(module, "CATALOG")
    navigation = constant(module, "NAV_ITEMS")
    banners = constant(module, "CAT_BANNER")
    learning_paths = constant(module, "LEARNING_PATHS")
    recent = constant(module, "RECENT")

    catalog_descriptions: dict[str, str] = {}
    planned: dict[str, list[dict[str, str]]] = {}
    accents: dict[str, str] = {}
    for label, accent, items in catalog_groups:
        category_id = CATEGORY_IDS[label]
        accents[category_id] = accent
        planned[category_id] = []
        for title, description, href in items:
            if href:
                catalog_descriptions[href.removesuffix("/index.html")] = description
            else:
                planned[category_id].append({"title": title, "description": description})

    category_order = [CATEGORY_IDS[label] for label, _, _ in catalog_groups]
    categories = [
        {
            "id": category_id,
            "label": next(label for label, _, _ in catalog_groups if CATEGORY_IDS[label] == category_id),
            "description": CATEGORY_DESCRIPTIONS[category_id],
            "accent": accents[category_id],
            "banner": banners.get(category_id),
            "planned_items": planned[category_id],
        }
        for category_id in category_order
    ]

    course_rows: list[dict[str, object]] = []
    for course in courses:
        category = course["id"].split("/", 1)[0]
        version, pages = version_and_pages(course["subtitle"])
        course_rows.append(
            {
                "id": course["id"],
                "category": category,
                "book": course["book"],
                "title": course["title"],
                "subtitle": course["subtitle"],
                "catalog_description": catalog_descriptions.get(course["id"], course["subtitle"]),
                "status": "published",
                "version": version,
                "pages": pages,
                "roles": ROLE_BY_CATEGORY.get(category, ["network-engineer"]),
                "difficulty": "advanced" if category in {"aos", "solutions"} else "intermediate",
                "tags": [category, "ale-networking"],
                "route": course["route"],
                "groups": [
                    {"name": group_name, "skills": skills}
                    for group_name, skills in course["groups"]
                ],
                "source": {
                    "book": course["book"],
                    "rights_scope": "internal-training",
                    "last_verified": EXTRACTED_ON,
                },
            }
        )

    dump(
        ROOT / "content" / "catalog.json",
        {
            "schema_version": 1,
            "site": {
                "name": "ALE Networking 技术培训",
                "short_name": "ALE 培训门户",
                "description": "面向售前、售后与网络工程师的 ALE 内部技术知识平台",
                "locale": "zh-CN",
                "rights_notice": "仅供内部学习使用 · 教材版权归 ALE Training Services 所有",
            },
            "navigation": [
                {
                    "label": label,
                    "href": href,
                    "category": href.split("/", 1)[0] if "/" in href else None,
                }
                for label, href in navigation
            ],
            "categories": categories,
            "courses": course_rows,
        },
    )

    path_ids = ("presales-engineer", "postsales-engineer", "wlan-specialist")
    dump(
        ROOT / "content" / "learning_paths.json",
        {
            "schema_version": 1,
            "paths": [
                {
                    "id": path_id,
                    "title": title,
                    "description": description,
                    "banner": banner,
                    "steps": [
                        {"title": step_title, "description": step_description, "href": href}
                        for step_title, step_description, href in steps
                    ],
                }
                for path_id, (title, description, banner, steps) in zip(
                    path_ids, learning_paths, strict=True
                )
            ],
        },
    )
    dump(
        ROOT / "content" / "recent.json",
        {
            "schema_version": 1,
            "items": [
                {"date": date, "title": title, "href": href, "note": note}
                for date, title, href, note in recent
            ],
        },
    )
    print(f"migrated {len(course_rows)} courses and {len(categories)} categories")


if __name__ == "__main__":
    main()
