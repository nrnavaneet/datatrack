import shutil
import time
from pathlib import Path

import pytest
import yaml
from assertpy import assert_that
from sqlalchemy import create_engine, text

from datatrack.connect import (
    get_connected_db_name,
    get_saved_connection,
    remove_connection,
    save_connection,
)
from datatrack.exporter import load_latest_snapshots
from datatrack.tracker import snapshot

# Constants
DB_FILE = Path(".databases/test_tracker.db")
TEST_URI = f"sqlite:///{DB_FILE}"
EXPORT_DIR = Path(".databases/exports")
TRACK_DIR = Path(".datatrack")


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup schema + cleanup."""
    engine = create_engine(TEST_URI)
    with engine.begin() as conn:
        # Tables
        conn.execute(
            text(
                """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            );
        """
            )
        )
        conn.execute(
            text(
                """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                total REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """
            )
        )
        # Data
        conn.execute(
            text(
                "INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')"
            )
        )
        conn.execute(text("INSERT INTO orders (user_id, total) VALUES (1, 99.9)"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_user_email ON users(email);"))
        conn.execute(
            text(
                """
            CREATE VIEW IF NOT EXISTS user_order_summary AS
            SELECT u.id, u.name, COUNT(o.id) AS orders
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id;
        """
            )
        )

    yield

    for path in [DB_FILE, EXPORT_DIR, TRACK_DIR]:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()


def test_connection_saved_and_loaded():
    remove_connection()
    save_connection(TEST_URI)
    assert_that(get_saved_connection()).is_equal_to(TEST_URI)
    assert_that(get_connected_db_name()).is_equal_to("test_tracker")
    remove_connection()
    assert_that(get_saved_connection()).is_none()


def test_snapshot_file_created_and_valid():
    save_connection(TEST_URI)
    snap_path = snapshot(TEST_URI)
    assert_that(snap_path.exists()).is_true()
    assert_that(snap_path.suffix).is_equal_to(".yaml")
    with open(snap_path) as f:
        data = yaml.safe_load(f)
        assert_that(data).contains("tables")
        assert_that(data["tables"]).is_instance_of(list)


def test_snapshot_structure_and_content():
    snapshot(TEST_URI)
    snap = load_latest_snapshots(n=1)[0]
    tables = {t["name"]: t for t in snap["tables"]}

    assert_that(tables).contains("users", "orders")
    user_cols = [col["name"] for col in tables["users"]["columns"]]
    assert_that(set(["id", "email", "name"]).issubset(set(user_cols))).is_true()
    assert_that(tables["users"]["columns"][0]["type"]).is_instance_of(str)
    assert_that(tables["users"]).contains("primary_key")
    assert_that(tables["users"]["primary_key"]).is_instance_of(list)


def test_snapshot_export_folder_structure():
    db_name = get_connected_db_name()
    snap_dir = EXPORT_DIR / db_name / "snapshots"
    assert_that(snap_dir.exists()).is_true()
    assert_that(list(snap_dir.glob("snapshot_*.yaml"))).is_not_empty()


def test_snapshot_contains_indexes_and_views():
    snap = load_latest_snapshots(n=1)[0]
    users = next(t for t in snap["tables"] if t["name"] == "users")
    index_names = [idx["name"] for idx in users.get("indexes", [])]
    view_names = [v["name"] for v in snap.get("views", [])]

    assert_that(index_names).contains("idx_user_email")
    assert_that(view_names).contains("user_order_summary")


def test_snapshot_contains_triggers():
    engine = create_engine(TEST_URI)
    with engine.connect() as conn:
        conn.execute(
            text(
                """
            CREATE TRIGGER IF NOT EXISTS trg_users_insert
            AFTER INSERT ON users
            BEGIN
                UPDATE users SET name = 'Triggered' WHERE id = NEW.id;
            END;
        """
            )
        )

    time.sleep(1)
    snap_path = snapshot(TEST_URI)
    with open(snap_path) as f:
        data = yaml.safe_load(f)
        triggers = data.get("triggers", [])
        trigger_names = [trg.get("name") or trg.get("trigger_name") for trg in triggers]

    assert_that(any("trg_users_insert" in t for t in trigger_names)).is_true()


def test_sqlite_has_no_functions_or_procedures():
    snap_path = snapshot(TEST_URI)
    with open(snap_path) as f:
        data = yaml.safe_load(f)

    assert_that(data.get("functions", [])).is_equal_to([])
    assert_that(data.get("procedures", [])).is_equal_to([])


def test_sqlite_has_no_sequences():
    snap_path = snapshot(TEST_URI)
    with open(snap_path) as f:
        data = yaml.safe_load(f)

    assert_that(data.get("sequences", [])).is_equal_to([])


def test_snapshot_includes_table_data():
    snap_path = snapshot(TEST_URI, include_data=True, max_rows=5)
    with open(snap_path) as f:
        data = yaml.safe_load(f)

    assert_that(data).contains("data")
    assert_that(data["data"]).contains("users")
    assert_that(data["data"]["users"]).is_instance_of(list)
    assert_that(any("email" in row for row in data["data"]["users"])).is_true()


def test_snapshot_meta_and_hash():
    snap_path = snapshot(TEST_URI)
    with open(snap_path) as f:
        data = yaml.safe_load(f)

    meta = data.get("__meta__", {})
    assert_that(meta).contains("timestamp", "snapshot_id", "hash")
    assert_that(len(meta["hash"])).is_equal_to(64)
