# src/uncoded/namespace_map.py

from pathlib import Path
import yaml
from uncoded.extract import ModuleInfo

def build_map(modules: list[ModuleInfo]) -> dict:  # L24-57
    """Build a nested dict representing the namespace."""
    ...

def render_map(namespace: dict) -> str:  # L60-67
    """Render a namespace map dict as a YAML string."""
    ...
