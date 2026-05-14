# Architecture

This document complements the diagram in the root [README](../README.md). It names **modules**, **data flow**, and **extension points**.

## Layers

1. **CLI (`datatrack/cli.py`)** — Typer entrypoints; parses options, calls services, exits with codes.
2. **Services** — `tracker` (snapshots), `diff`, `linter`, `verifier`, `exporter`, `history`, `pipeline`, `doctor`, `test_connection`.
3. **Paths (`datatrack/paths.py`)** — Single definition of `.datatrack/`, `.databases/exports/`, and per-database snapshot directories. All services import from here.
4. **Persistence** — YAML snapshots on disk; `schema_rules.yaml` for lint/verify; `.datatrack/db_link.yaml` for the saved URI.

## Snapshot lifecycle

1. User runs `datatrack connect <uri>`.
2. `snapshot` uses SQLAlchemy introspection (`tracker.py`) and writes YAML under `paths.snapshot_dir(db_name)`.
3. `lint` / `verify` read the latest YAML file in that directory (same ordering convention: sort by filename, take newest).
4. `diff` loads the two newest files and prints a textual report.
5. `export` serialises snapshot or structured diff to JSON/YAML next to the database export folder.

## Pipeline

`pipeline run` orchestrates the above in sequence and records pass/fail in a Rich table (`pipeline.py`). It does not introduce a separate storage format.

## Adding behaviour

- **New CLI command**: register in `cli.py`, implement in a new module or extend an existing one, document in `docs/USAGE.md`, add tests under `tests/`.
- **New rule**: extend `schema_rules.yaml` and the parsing logic in `linter.py` / `verifier.py` together so lint and verify stay aligned.

## Testing strategy

Unit tests patch `get_connected_db_name` or filesystem paths (`tests/commands/test_diff.py`) so CI does not require PostgreSQL or MySQL. Integration tests against real engines are left to contributors’ machines.

## See also

- [Developing](DEVELOPING.md) — local environment and common commands.
- [FAQ](FAQ.md) — single-URI storage, snapshot paths, lint vs verify.
