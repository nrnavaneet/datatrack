# Changelog

All notable changes to this project are documented here. Versions follow the package version in `pyproject.toml`.

## [1.2.0] — 2026-05

- Introduce **`datatrack.paths`**: one module defines `.datatrack/`, `.databases/exports/`, and per-database snapshot directories; tracker, diff, history, linter, verifier, exporter, pipeline, connect, CLI, tests, and benchmarks now use it.

## [1.1.9] — 2026-05

- New docs: environment variables, CI overview, troubleshooting, and benchmark readme.
- Examples: minimal snapshot YAML for copying into fixtures.
- Tests for verifier snake_case rules and connection-derived database folder names.
- Safer rule loading in the verifier, clearer test-connection errors, and SQLAlchemy 2 friendly `SELECT 1`.
- CI uses pip cache and `pytest -q tests/`.

## [1.1.8] — 2025

- CLI pipeline summary tables use the **Datatrack** spelling consistently.
- **History** command tolerates corrupt snapshot YAML more safely than a bare `except`.
- **Connect** suggests running `test-connection` after a successful `connect`.
- Contributor docs mention running `pytest` from the repo root.
- **Diff** `load_snapshots` docstring clarifies ordering and error behavior.

## Earlier

Prior releases were published on PyPI as **datatrack-core**; see git history for full detail.
