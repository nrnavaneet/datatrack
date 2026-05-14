"""Tests for connection helper that derives export folder names from URIs."""
from pathlib import Path

import pytest
import yaml

from datatrack import connect as connect_mod


def test_get_connected_db_name_sqlite_file(tmp_path, monkeypatch):
    cfg = tmp_path / "db_link.yaml"
    monkeypatch.setattr(connect_mod, "DB_LINK_FILE", cfg)
    cfg.parent.mkdir(parents=True, exist_ok=True)
    with open(cfg, "w") as f:
        yaml.dump({"link": "sqlite:////tmp/sample_ci.db"}, f)
    assert connect_mod.get_connected_db_name() == "sample_ci"


def test_get_connected_db_name_postgres_path(tmp_path, monkeypatch):
    cfg = tmp_path / "db_link.yaml"
    monkeypatch.setattr(connect_mod, "DB_LINK_FILE", cfg)
    cfg.parent.mkdir(parents=True, exist_ok=True)
    with open(cfg, "w") as f:
        yaml.dump({"link": "postgresql://user:pw@localhost:5432/analytics"}, f)
    assert connect_mod.get_connected_db_name() == "analytics"
