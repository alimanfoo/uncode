from pathlib import Path

from uncoded.claude_md import (
    MARKER_END,
    MARKER_START,
    check_claude_md,
    generate_section,
    sync_claude_md,
)


class TestGenerateSection:
    def test_contains_markers(self):
        section = generate_section()
        assert MARKER_START in section
        assert MARKER_END in section

    def test_markers_in_order(self):
        section = generate_section()
        assert section.index(MARKER_START) < section.index(MARKER_END)

    def test_ends_with_newline(self):
        assert generate_section().endswith("\n")


class TestSyncClaudeMd:
    def test_creates_file_if_missing(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        sync_claude_md(path)
        assert path.exists()
        assert generate_section() in path.read_text()

    def test_appends_to_existing_file(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        path.write_text("# My Project\n\nSome content.\n")
        sync_claude_md(path)
        content = path.read_text()
        assert "# My Project" in content
        assert generate_section() in content

    def test_replaces_existing_section(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        old_section = f"{MARKER_START}\nold content\n{MARKER_END}\n"
        path.write_text(f"# My Project\n\n{old_section}")
        sync_claude_md(path)
        content = path.read_text()
        assert "old content" not in content
        assert generate_section() in content
        assert "# My Project" in content

    def test_preserves_content_after_section(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        old_section = f"{MARKER_START}\nold\n{MARKER_END}\n"
        path.write_text(f"{old_section}\n## Other section\n")
        sync_claude_md(path)
        content = path.read_text()
        assert "## Other section" in content

    def test_idempotent(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        sync_claude_md(path)
        first = path.read_text()
        sync_claude_md(path)
        assert path.read_text() == first


class TestCheckClaudeMd:
    def test_returns_false_if_missing(self, tmp_path):
        assert check_claude_md(tmp_path / "CLAUDE.md") is False

    def test_returns_false_if_section_absent(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        path.write_text("# My Project\n")
        assert check_claude_md(path) is False

    def test_returns_true_after_sync(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        sync_claude_md(path)
        assert check_claude_md(path) is True

    def test_returns_false_if_section_outdated(self, tmp_path):
        path = tmp_path / "CLAUDE.md"
        path.write_text(f"{MARKER_START}\nstale content\n{MARKER_END}\n")
        assert check_claude_md(path) is False
