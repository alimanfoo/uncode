"""CLI entry point for uncoded."""

import argparse
import sys
from pathlib import Path

from uncoded.extract import walk_source
from uncoded.namespace_map import build_map, render_map
from uncoded.stubs import DEFAULT_STUBS_OUTPUT, build_stubs

DEFAULT_OUTPUT = Path(".uncoded/namespace.yaml")


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        description="Generate code navigation indexes for AI agents.",
    )
    subparsers = parser.add_subparsers(dest="command")

    map_parser = subparsers.add_parser("map", help="Generate namespace map")
    map_parser.add_argument(
        "source_root", type=Path, help="Path to source root (e.g. src/)"
    )
    map_parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output file path (default: {DEFAULT_OUTPUT})",
    )

    stubs_parser = subparsers.add_parser("stubs", help="Generate stub files")
    stubs_parser.add_argument(
        "source_root", type=Path, help="Path to source root (e.g. src/)"
    )
    stubs_parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_STUBS_OUTPUT,
        help=f"Output directory (default: {DEFAULT_STUBS_OUTPUT})",
    )

    args = parser.parse_args(argv)

    if args.command == "map":
        return cmd_map(args)

    if args.command == "stubs":
        return cmd_stubs(args)

    parser.print_help()
    return 1


def cmd_stubs(args: argparse.Namespace) -> int:
    source_root = args.source_root.resolve()

    if not source_root.is_dir():
        print(f"Error: {source_root} is not a directory", file=sys.stderr)
        return 1

    build_stubs(source_root, output_dir=args.output)
    return 0


def cmd_map(args: argparse.Namespace) -> int:
    source_root = args.source_root.resolve()

    if not source_root.is_dir():
        print(f"Error: {source_root} is not a directory", file=sys.stderr)
        return 1

    modules = walk_source(source_root)
    namespace = build_map(modules)
    output = render_map(namespace)

    output_path: Path = args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output)
    print(f"Wrote {output_path}")
    return 0
