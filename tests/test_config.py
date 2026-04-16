import os
from pathlib import Path

import pytest

from uncoded.config import find_pyproject_toml, read_source_roots


class TestFindPyprojectToml:
    def test_finds_in_cwd(self, tmp_path):
        (tmp_path / "pyproject.toml").write_text("")
        os.chdir(tmp_path)
        assert find_pyproject_toml() == tmp_path / "pyproject.toml"

    def test_finds_in_parent(self, tmp_path):
        (tmp_path / "pyproject.toml").write_text("")
        subdir = tmp_path / "sub"
        subdir.mkdir()
        os.chdir(subdir)
        assert find_pyproject_toml() == tmp_path / "pyproject.toml"

    def test_returns_none_if_not_found(self, tmp_path):
        os.chdir(tmp_path)
        assert find_pyproject_toml() is None


class TestReadSourceRoots:
    def test_reads_source_roots(self, tmp_path):
        (tmp_path / "pyproject.toml").write_text(
            '[tool.uncoded]\nsource-roots = ["src", "tests"]\n'
        )
        os.chdir(tmp_path)
        roots = read_source_roots()
        assert roots == [Path("src"), Path("tests")]

    def test_raises_if_no_pyproject_toml(self, tmp_path):
        os.chdir(tmp_path)
        with pytest.raises(FileNotFoundError):
            read_source_roots()

    def test_raises_if_no_uncoded_section(self, tmp_path):
        (tmp_path / "pyproject.toml").write_text("[tool.ruff]\n")
        os.chdir(tmp_path)
        with pytest.raises(KeyError):
            read_source_roots()
