"""Non-destructive checks for local Datatrack layout (no database writes).

`collect_rows` returns one row per filesystem check; `format_report` renders them for the CLI.
"""
from __future__ import annotations

from pathlib import Path

from datatrack.paths import CONFIG_DIR, DB_LINK_FILE, EXPORT_BASE


def collect_rows() -> list[tuple[str, str, bool]]:
    """Return (label, path or detail, ok)."""
    rows: list[tuple[str, str, bool]] = [
        (".datatrack directory", str(CONFIG_DIR), CONFIG_DIR.is_dir()),
        ("Saved connection file", str(DB_LINK_FILE), DB_LINK_FILE.is_file()),
        ("Export base", str(EXPORT_BASE), EXPORT_BASE.parent.is_dir()),
        (
            "schema_rules.yaml",
            str(Path("schema_rules.yaml").resolve()),
            Path("schema_rules.yaml").is_file(),
        ),
    ]
    return rows


def format_report() -> str:
    lines = ["Datatrack doctor — local layout", "=" * 44]
    for label, detail, ok in collect_rows():
        flag = "ok" if ok else "missing"
        lines.append(f"  [{flag:7}] {label}")
        lines.append(f"            {detail}")
    lines.append("")
    lines.append("This does not run SQL; use `datatrack test-connection` for that.")
    return "\n".join(lines)
