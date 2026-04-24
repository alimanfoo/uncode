# tests/test_cli.py

import os
import sys
import textwrap
import pytest
from uncoded import cli
from uncoded.skill import SKILL_OUTPUTS

def _init_repo(tmp_path, source_roots):  # L19-35
    """Set up a minimal repo: pyproject.toml + source root + chdir."""
    ...

class TestSyncApplyMode:  # L38-91

    def test_writes_namespace_map_stubs_and_instruction_file(self, tmp_path):  # L39-48
        ...

    def test_idempotent_second_run(self, tmp_path):  # L50-70
        ...

    def test_error_when_no_pyproject_toml(self, tmp_path, capsys):  # L72-75
        ...

    def test_error_when_source_root_missing(self, tmp_path, capsys):  # L77-91
        ...

class TestSyncCheckMode:  # L94-151

    def test_returns_one_and_does_not_write_on_empty_repo(self, tmp_path):  # L95-102
        ...

    def test_returns_zero_when_index_is_up_to_date(self, tmp_path):  # L104-108
        ...

    def test_returns_one_when_source_changes_after_sync(self, tmp_path):  # L110-121
        ...

    def test_returns_one_when_source_file_deleted(self, tmp_path):  # L123-132
        ...

    def test_returns_one_when_instruction_file_drifts(self, tmp_path):  # L134-145
        ...

    def test_error_still_returns_one(self, tmp_path, capsys):  # L147-151
        ...

class TestMainDispatch:  # L154-199

    def test_sync_subcommand_runs_in_apply_mode(self, tmp_path, monkeypatch):  # L155-161
        ...

    def test_check_subcommand_runs_in_check_mode(self, tmp_path, monkeypatch):  # L163-170
        ...

    def test_check_subcommand_returns_zero_on_fresh_index(self, tmp_path, monkeypatch):  # L172-178
        ...

    def test_setup_serena_subcommand(self, tmp_path, monkeypatch):  # L180-184
        ...

    def test_no_subcommand_is_an_error(self, tmp_path, monkeypatch):  # L186-193
        ...

    def test_unknown_subcommand_is_an_error(self, tmp_path, monkeypatch):  # L195-199
        ...
