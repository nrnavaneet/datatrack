# Python modules

[← Documentation home](README.md)

Datatrack is primarily a **CLI**, but several packages are safe to import from automation or extensions.

| Module | Role |
|--------|------|
| `datatrack.cli` | Typer application (`app`) and command registration. |
| `datatrack.paths` | Canonical `.datatrack/`, `.databases/exports/`, snapshot and export directory helpers (`__all__` lists stable public names). Tests cover both path strings and `__all__` membership. |
| `datatrack.tracker` | Snapshot creation via SQLAlchemy introspection (writes YAML under `paths.snapshot_dir`). |
| `datatrack.diff` | Compare two snapshot YAML files for the active database (loads latest pair from disk). |
| `datatrack.linter` | Heuristic lint over the latest snapshot YAML (reads `schema_rules.yaml`; module docstring summarises inputs). |
| `datatrack.verifier` | Rule-driven verification (see module docstring at top of `verifier.py`). |
| `datatrack.exporter` | JSON/YAML export of snapshots or diffs (writes next to export paths). |
| `datatrack.history` | List snapshot files and parse timestamps from filenames. |
| `datatrack.pipeline` | Orchestrated command sequence (`pipeline run`); see [Pipeline](PIPELINE.md). |
| `datatrack.doctor` | Offline layout checks (`collect_rows`, `format_report`). |
| `datatrack.connect` | Persist and parse saved database URIs (see module docstring in `connect.py`). |
| `datatrack.test_connection` | Smoke-test the saved URI with a trivial SQL query. |

Importing `datatrack.cli` has side effects (Typer setup). Prefer **`paths`**, **`doctor`**, or **`tracker`** entrypoints for libraries that only need filesystem or snapshot logic.

## Benchmark harness (not a package)

The `benchmark_tests/` directory holds **manual** timing scripts (`parallel_processing.py`) documented in [`benchmark_tests/README.md`](../benchmark_tests/README.md). They are not importable library modules; run them from the repo root when validating performance claims in [Performance](PERFORMANCE.md).
