"""Tests for `datatrack.paths` layout helpers (export base, per-db folders)."""

from datatrack.paths import DATABASES_DIR, EXPORT_BASE, export_dir, snapshot_dir


def test_export_base_under_dot_databases():
    assert EXPORT_BASE.parts[:2] == (".databases", "exports")


def test_snapshot_dir_nests_under_export():
    p = snapshot_dir("analytics")
    assert p == EXPORT_BASE / "analytics" / "snapshots"


def test_export_dir_is_database_root():
    assert export_dir("analytics") == EXPORT_BASE / "analytics"


def test_databases_dir_constant():
    assert str(DATABASES_DIR) == ".databases"
