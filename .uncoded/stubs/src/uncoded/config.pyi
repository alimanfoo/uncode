# src/uncoded/config.py

import tomllib
from pathlib import Path
from uncoded.instruction_files import DEFAULT_INSTRUCTION_FILES

def find_pyproject_toml() -> Path | None:  # L9-19
    """Search for pyproject.toml starting from cwd, walking up."""
    ...

def read_source_roots() -> list[Path]:  # L22-40
    """Read source roots from [tool.uncoded] source-roots in pyproject.toml."""
    ...

def read_instruction_files() -> list[Path]:  # L43-62
    """Read instruction files from [tool.uncoded] instruction-files in pyproject.toml."""
    ...
