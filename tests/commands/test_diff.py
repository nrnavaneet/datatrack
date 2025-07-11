import shutil
from pathlib import Path

import pytest
import yaml

from datatrack.diff import diff_schemas, load_snapshots

EXPORT_BASE = Path(".databases/exports")
DB_NAME = "test_db"
SNAPSHOT_DIR = EXPORT_BASE / DB_NAME / "snapshots"


@pytest.fixture(autouse=True)
def setup_snapshots(monkeypatch):
    monkeypatch.setattr("datatrack.diff.get_connected_db_name", lambda: DB_NAME)
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    yield
    shutil.rmtree(EXPORT_BASE)


def write_snapshot(data: dict, filename: str):
    with open(SNAPSHOT_DIR / filename, "w") as f:
        yaml.dump(data, f)


def test_load_snapshots_success():
    old_schema = {
        "tables": [
            {"name": "users", "columns": [{"name": "id", "type": "INTEGER"}]},
            {"name": "orders", "columns": [{"name": "id", "type": "INTEGER"}]},
        ]
    }
    new_schema = {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "email", "type": "TEXT"},
                ],
            },
            {"name": "products", "columns": [{"name": "id", "type": "INTEGER"}]},
        ]
    }

    write_snapshot(old_schema, "snapshot_20240701_120000.yaml")
    write_snapshot(new_schema, "snapshot_20240702_120000.yaml")

    older, newer = load_snapshots()
    assert "orders" in {t["name"] for t in older["tables"]}
    assert "products" in {t["name"] for t in newer["tables"]}


def test_diff_schemas_outputs_changes(capsys):
    old = {
        "tables": [
            {"name": "users", "columns": [{"name": "id", "type": "INTEGER"}]},
            {"name": "orders", "columns": [{"name": "id", "type": "INTEGER"}]},
        ],
        "views": [{"name": "v1"}],
        "functions": [{"name": "func1"}],
        "data": {"users": [{"id": 1}]},
    }
    new = {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "email", "type": "TEXT"},
                ],
            },
            {"name": "products", "columns": [{"name": "id", "type": "INTEGER"}]},
        ],
        "triggers": [{"name": "trg1"}],
        "data": {"users": [{"id": 1}, {"id": 2}]},
    }

    write_snapshot(old, "snapshot_old.yaml")
    write_snapshot(new, "snapshot_new.yaml")

    diff_schemas(old, new)
    out = capsys.readouterr().out

    assert "+ Added table: products" in out
    assert "- Removed table: orders" in out
    assert "  + users.email (TEXT)" in out
    assert "- Removed view: v1" in out
    assert "+ Added trigger: trg1" in out
    assert "+ {'id': 2}" in out


def test_no_changes(capsys):
    snap = {
        "tables": [{"name": "users", "columns": [{"name": "id", "type": "INTEGER"}]}],
        "data": {"users": [{"id": 1}]},
    }
    write_snapshot(snap, "s1.yaml")
    write_snapshot(snap, "s2.yaml")

    older, newer = load_snapshots()
    diff_schemas(older, newer)
    out = capsys.readouterr().out

    assert "No tables added or removed." in out
    assert "No views added or removed." in out
    assert "No triggers added or removed." in out
    assert "No functions added or removed." in out
    assert "No procedures added or removed." in out
    assert "No sequences added or removed." in out
    assert "No data changes in `users`." in out
    assert "Diff complete." in out


def test_corrupt_snapshot_raises():
    write_snapshot({"tables": []}, "snap1.yaml")
    (SNAPSHOT_DIR / "snap2.yaml").write_text("not: valid: yaml: }")

    with pytest.raises(yaml.YAMLError):
        load_snapshots()


def test_missing_columns_key():
    s1 = {"tables": [{"name": "users", "columns": [{"name": "id", "type": "INTEGER"}]}]}
    s2 = {"tables": [{"name": "users"}]}  # columns key missing
    write_snapshot(s1, "s_a.yaml")
    write_snapshot(s2, "s_b.yaml")

    with pytest.raises(KeyError):
        older, newer = load_snapshots()
        diff_schemas(older, newer)


def test_added_and_removed_columns(capsys):
    old = {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INT"},
                    {"name": "age", "type": "INT"},
                ],
            }
        ]
    }
    new = {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INT"},
                    {"name": "email", "type": "TEXT"},
                ],
            }
        ]
    }
    write_snapshot(old, "snap_old.yaml")
    write_snapshot(new, "snap_new.yaml")

    diff_schemas(old, new)
    out = capsys.readouterr().out
    assert "- users.age (INT)" in out
    assert "+ users.email (TEXT)" in out


def test_non_yaml_file_ignored():
    write_snapshot({"tables": [{"name": "t1", "columns": []}]}, "snapshot_1.yaml")
    write_snapshot({"tables": [{"name": "t2", "columns": []}]}, "snapshot_2.yaml")
    (SNAPSHOT_DIR / "README.txt").write_text("this is not a yaml")

    older, newer = load_snapshots()
    assert isinstance(older, dict)
    assert isinstance(newer, dict)
