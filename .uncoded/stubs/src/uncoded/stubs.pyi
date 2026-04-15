# src/uncoded/stubs.py

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from uncoded.extract import is_public, iter_source_files

def extract_stub(source: str, rel_path: str) -> StubModule:  # L144-161
    """Parse Python source and extract the public API surface."""
    ...

def render_stub(module: StubModule) -> str:  # L185-218
    """Render a StubModule as a .pyi file string."""
    ...

def build_stubs(source_root: Path, base: Path | None, output_dir: Path) -> None:  # L224-242
    """Generate stub files for all public modules under source_root."""
    ...

class StubParam:  # L12-16
    """A function parameter with name and optional type annotation."""

    name: str
    annotation: str | None

class StubFunction:  # L20-29
    """A public function or method with signature and line range."""

    name: str
    params: list[StubParam]
    return_annotation: str | None
    docstring_excerpt: str | None
    start_line: int
    end_line: int
    is_async: bool

class StubClass:  # L33-42
    """A public class with its members and line range."""

    name: str
    bases: list[str]
    docstring_excerpt: str | None
    start_line: int
    end_line: int
    attributes: list[StubParam]
    methods: list[StubFunction]

class StubModule:  # L46-52
    """Public API surface of a single Python module."""

    rel_path: str
    imports: list[str]
    classes: list[StubClass]
    functions: list[StubFunction]
