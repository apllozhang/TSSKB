"""Single operational entry point for build, validation, metrics and releases."""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import sys
from dataclasses import asdict
from pathlib import Path

from tsskb.build.metrics import collect_metrics, enforce_metrics
from tsskb.build.pipeline import SiteBuilder
from tsskb.build.validator import validate_site
from tsskb.config import ProjectPaths
from tsskb.content.loader import ContentRepository
from tsskb.deploy.release import ReleaseService
from tsskb.observability import EventLogger


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tsskb", description="TSSKB content platform")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="project root")
    parser.add_argument("--human", action="store_true", help="human-readable events")
    commands = parser.add_subparsers(dest="command", required=True)

    validate = commands.add_parser("validate", help="validate content and optionally a built site")
    validate.add_argument("--site", type=Path)
    validate.add_argument("--strict", action=argparse.BooleanOptionalAction, default=True)

    build = commands.add_parser("build", help="build the complete static portal")
    build.add_argument("--output", type=Path, default=Path("dist/site"))
    build.add_argument("--environment", choices=("dev", "staging", "prod"), default="dev")
    mode = build.add_mutually_exclusive_group()
    mode.add_argument("--full", action="store_true")
    mode.add_argument("--incremental", action="store_true")
    build.add_argument("--strict", action=argparse.BooleanOptionalAction, default=None)

    metrics = commands.add_parser("metrics", help="report output and search capacity")
    metrics.add_argument("--site", type=Path, default=Path("dist/site"))
    metrics.add_argument("--environment", choices=("dev", "staging", "prod"), default="dev")
    metrics.add_argument("--enforce-budget", action="store_true")

    serve = commands.add_parser("serve", help="serve a built site for local review")
    serve.add_argument("--site", type=Path, default=Path("dist/site"))
    serve.add_argument("--bind", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)

    deploy = commands.add_parser("deploy", help="promote an immutable release")
    deploy.add_argument("--site", type=Path, default=Path("dist/site"))
    deploy.add_argument("--environment", choices=("staging", "prod"), required=True)
    deploy.add_argument("--dry-run", action="store_true")

    rollback = commands.add_parser("rollback", help="atomically restore an earlier release")
    rollback.add_argument("--environment", choices=("staging", "prod"), required=True)
    rollback.add_argument("--target")
    rollback.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        paths = ProjectPaths.discover(args.root)
        logger = EventLogger(json_output=not args.human)
        if args.command == "validate":
            bundle = ContentRepository(paths).load(check_files=True)
            payload: dict[str, object] = {
                "status": "valid",
                "courses": len(bundle.catalog.courses),
                "skills": sum(len(course.skill_slugs) for course in bundle.catalog.courses),
                "redirects": len(bundle.redirects.redirects),
            }
            if args.site:
                report = validate_site(_resolve(paths, args.site), strict=args.strict)
                payload.update({"pages": report.page_count, "references": report.reference_count})
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0
        if args.command == "build":
            SiteBuilder(paths, logger).build(
                output=_resolve(paths, args.output),
                environment=args.environment,
                incremental=args.incremental and not args.full,
                strict=args.strict,
            )
            return 0
        if args.command == "metrics":
            values = collect_metrics(_resolve(paths, args.site))
            if args.enforce_budget:
                enforce_metrics(values, paths.environment(args.environment).search_budget)
            print(json.dumps(values, ensure_ascii=False, indent=2))
            return 0
        if args.command == "serve":
            site = _resolve(paths, args.site)
            if not site.is_dir():
                raise FileNotFoundError(f"build the site first: {site}")
            handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(site))
            server = http.server.ThreadingHTTPServer((args.bind, args.port), handler)
            print(f"Serving {site} at http://{args.bind}:{args.port}/")
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("Server stopped.")
            finally:
                server.server_close()
            return 0
        if args.command == "deploy":
            result = ReleaseService(logger).deploy(
                _resolve(paths, args.site), paths.environment(args.environment), dry_run=args.dry_run
            )
            print(json.dumps(asdict(result), ensure_ascii=False, default=str, indent=2))
            return 0
        if args.command == "rollback":
            result = ReleaseService(logger).rollback(
                paths.environment(args.environment), target=args.target, dry_run=args.dry_run
            )
            print(json.dumps(asdict(result), ensure_ascii=False, default=str, indent=2))
            return 0
    except (FileNotFoundError, PermissionError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 1


def _resolve(paths: ProjectPaths, value: Path) -> Path:
    return value.resolve() if value.is_absolute() else (paths.root / value).resolve()
