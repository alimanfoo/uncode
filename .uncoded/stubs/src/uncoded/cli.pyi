# src/uncoded/cli.py

import argparse
import sys
from pathlib import Path
from uncoded.extract import walk_source
from uncoded.namespace_map import build_map, render_map
from uncoded.stubs import DEFAULT_STUBS_OUTPUT, build_stubs

def main(argv: list[str] | None):  # L14-53
    ...

def cmd_stubs(args: argparse.Namespace) -> int:  # L56-64
    ...

def cmd_map(args: argparse.Namespace) -> int:  # L67-82
    ...
