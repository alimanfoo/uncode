# src/uncoded/cli.py

import argparse
import sys
from pathlib import Path
from uncoded.claude_md import check_claude_md, sync_claude_md
from uncoded.extract import walk_source
from uncoded.namespace_map import build_map, render_map
from uncoded.stubs import DEFAULT_STUBS_OUTPUT, build_stubs, generate_stubs

def main(argv: list[str] | None):  # L15-39
    ...

def _resolve_source_roots(args: argparse.Namespace) -> list[Path] | None:  # L42-50
    ...

def cmd_sync(args: argparse.Namespace) -> int:  # L53-67
    ...

def cmd_check(args: argparse.Namespace) -> int:  # L70-104
    ...
