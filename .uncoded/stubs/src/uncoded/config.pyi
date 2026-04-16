# src/uncoded/config.py

import tomllib
from pathlib import Path

def find_pyproject_toml() -> Path | None:  # L7-17
    """Search for pyproject.toml starting from cwd, walking up."""
    ...

def read_source_roots() -> list[Path]:  # L20-38
    """Read source roots from [tool.uncoded] source-roots in pyproject.toml."""
    ...
