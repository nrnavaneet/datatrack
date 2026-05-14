"""Central filesystem layout for Datatrack (config, DB link, exports, snapshots)."""
from __future__ import annotations

from pathlib import Path

# Local project configuration
CONFIG_DIR = Path(".datatrack")
CONFIG_FILE = CONFIG_DIR / "config.yaml"
DB_LINK_FILE = CONFIG_DIR / "db_link.yaml"

# Snapshot and export tree (under cwd)
DATABASES_DIR = Path(".databases")
EXPORT_BASE = DATABASES_DIR / "exports"


def snapshot_dir(db_name: str) -> Path:
    """Directory where YAML snapshots for ``db_name`` are stored."""
    return EXPORT_BASE / db_name / "snapshots"


def export_dir(db_name: str) -> Path:
    """Per-database export root (snapshots live under ``snapshot_dir``)."""
    return EXPORT_BASE / db_name
