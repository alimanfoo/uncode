# tests/test_claude_md.py

from uncoded.claude_md import MARKER_END, MARKER_START, generate_section, sync_claude_md

class TestGenerateSection:  # L9-20

    def test_contains_markers(self):  # L10-13
        ...

    def test_markers_in_order(self):  # L15-17
        ...

    def test_ends_with_newline(self):  # L19-20
        ...

class TestSyncClaudeMd:  # L23-61

    def test_creates_file_if_missing(self, tmp_path):  # L24-28
        ...

    def test_appends_to_existing_file(self, tmp_path):  # L30-36
        ...

    def test_replaces_existing_section(self, tmp_path):  # L38-46
        ...

    def test_preserves_content_after_section(self, tmp_path):  # L48-54
        ...

    def test_idempotent(self, tmp_path):  # L56-61
        ...
