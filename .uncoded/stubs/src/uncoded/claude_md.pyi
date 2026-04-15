# src/uncoded/claude_md.py

from pathlib import Path

def generate_section() -> str:  # L46-48
    """Return the full delimited uncoded section for insertion into CLAUDE.md."""
    ...

def _replace_or_append(existing: str, section: str) -> str:  # L51-60
    ...

def sync_claude_md(path: Path) -> None:  # L63-74
    """Write or update the uncoded navigation section in CLAUDE.md."""
    ...

def check_claude_md(path: Path) -> bool:  # L77-81
    """Return True if CLAUDE.md contains the current uncoded navigation section."""
    ...
