# src/uncoded/instruction_files.py

from pathlib import Path

MARKER_START = '<!-- uncoded:start -->'  # L12
MARKER_END = '<!-- uncoded:end -->'  # L13
DEFAULT_INSTRUCTION_FILES = [Path('CLAUDE.md'), Path('AGENTS.md')]  # L15
_SECTION_BODY = ...  # L17-72
SECTION = f'{MARKER_START}\n{_SECTION_BODY}\n{MARKER_END}\n'  # L74

def generate_section() -> str:  # L77-79
    """Return the full delimited uncoded section for an instruction file."""
    ...

def _replace_or_append(existing: str, section: str) -> str:  # L82-92
    """Replace the delimited section in existing text, or append it if absent."""
    ...

def sync_instruction_file(path: Path) -> None:  # L95-106
    """Write or update the uncoded navigation section in an instruction file."""
    ...
