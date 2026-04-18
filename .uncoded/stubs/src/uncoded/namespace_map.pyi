# src/uncoded/namespace_map.py

from pathlib import Path
import yaml
from uncoded.extract import ModuleInfo

HEADER = ...  # L9-19

def build_map(modules: list[ModuleInfo]) -> dict:  # L37-73
    """Build a nested dict representing the namespace."""
    ...

def render_map(namespace: dict) -> str:  # L76-84
    """Render a namespace map dict as a YAML string with an explanatory header."""
    ...

class _CleanDumper(yaml.SafeDumper):  # L22-27
    """YAML dumper that indents list items and suppresses 'null' values."""

    def increase_indent(self, flow, indentless):  # L25-27
        """Force list items to be indented relative to their parent key."""
        ...
