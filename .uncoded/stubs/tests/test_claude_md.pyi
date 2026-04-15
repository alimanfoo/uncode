# tests/test_claude_md.py

from pathlib import Path
from uncoded.claude_md import MARKER_END, MARKER_START, check_claude_md, generate_section, sync_claude_md

class TestGenerateSection:  # L12-23

    def test_contains_markers(self):  # L13-16
        ...

    def test_markers_in_order(self):  # L18-20
        ...

    def test_ends_with_newline(self):  # L22-23
        ...

class TestSyncClaudeMd:  # L26-64

    def test_creates_file_if_missing(self, tmp_path):  # L27-31
        ...

    def test_appends_to_existing_file(self, tmp_path):  # L33-39
        ...

    def test_replaces_existing_section(self, tmp_path):  # L41-49
        ...

    def test_preserves_content_after_section(self, tmp_path):  # L51-57
        ...

    def test_idempotent(self, tmp_path):  # L59-64
        ...

class TestCheckClaudeMd:  # L67-84

    def test_returns_false_if_missing(self, tmp_path):  # L68-69
        ...

    def test_returns_false_if_section_absent(self, tmp_path):  # L71-74
        ...

    def test_returns_true_after_sync(self, tmp_path):  # L76-79
        ...

    def test_returns_false_if_section_outdated(self, tmp_path):  # L81-84
        ...
