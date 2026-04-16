# tests/test_config.py

import os
from pathlib import Path
import pytest
from uncoded.config import find_pyproject_toml, read_source_roots

class TestFindPyprojectToml:  # L9-24

    def test_finds_in_cwd(self, tmp_path):  # L10-13
        ...

    def test_finds_in_parent(self, tmp_path):  # L15-20
        ...

    def test_returns_none_if_not_found(self, tmp_path):  # L22-24
        ...

class TestReadSourceRoots:  # L27-45

    def test_reads_source_roots(self, tmp_path):  # L28-34
        ...

    def test_raises_if_no_pyproject_toml(self, tmp_path):  # L36-39
        ...

    def test_raises_if_no_uncoded_section(self, tmp_path):  # L41-45
        ...
