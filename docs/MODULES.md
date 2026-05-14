# Python modules

[← Documentation home](README.md)

Datatrack is primarily a **CLI**, but several packages are safe to import from automation or extensions.

| Module | Role |
|--------|------|
| `datatrack.cli` | Typer application (`app`) and command registration. |
| `datatrack.paths` | Canonical `.datatrack/`, `.databases/exports/`, snapshot and export directory helpers (`__all__` lists stable public names). |
| `datatrack.tracker` | Snapshot creation via SQLAlchemy introspection. |
| `datatrack.diff` | Compare two snapshot YAML files. |
| `datatrack.linter` / `datatrack.verifier` | Lint and verify latest snapshot against rules. |
| `datatrack.exporter` | JSON/YAML export of snapshots or diffs. |
| `datatrack.history` | List snapshot files for a database. |
| `datatrack.pipeline` | Orchestrated command sequence. |
| `datatrack.doctor` | Offline layout checks (`collect_rows`, `format_report`). |
| `datatrack.connect` / `datatrack.test_connection` | Connection URI handling and smoke queries. |

Importing `datatrack.cli` has side effects (Typer setup). Prefer **`paths`**, **`doctor`**, or **`tracker`** entrypoints for libraries that only need filesystem or snapshot logic.
