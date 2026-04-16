"""Read uncoded configuration from pyproject.toml."""

import tomllib
from pathlib import Path


def find_pyproject_toml() -> Path | None:
    """Search for pyproject.toml starting from cwd, walking up."""
    current = Path.cwd()
    while True:
        candidate = current / "pyproject.toml"
        if candidate.exists():
            return candidate
        parent = current.parent
        if parent == current:
            return None
        current = parent


def read_source_roots() -> list[Path]:
    """Read source roots from [tool.uncoded] source-roots in pyproject.toml."""
    toml_path = find_pyproject_toml()
    if toml_path is None:
        raise FileNotFoundError(
            "No pyproject.toml found. Add [tool.uncoded] source-roots to configure."
        )

    with toml_path.open("rb") as f:
        data = tomllib.load(f)

    try:
        roots = data["tool"]["uncoded"]["source-roots"]
    except KeyError:
        raise KeyError(
            "No [tool.uncoded] source-roots found in pyproject.toml."
        ) from None

    return [Path(r) for r in roots]
