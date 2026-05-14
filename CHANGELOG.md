# Changelog

All notable changes to this project are documented here. Versions follow the package version in `pyproject.toml`.

## [1.2.10] — 2026-05

- Add **EditorConfig** defaults for Python, YAML, and the Makefile.

## [1.2.9] — 2026-05

- New **Performance** doc with benchmark tables and reproduction pointers; PyPI readme links to it for full methodology.

## [1.2.8] — 2026-05

- Support **`python -m datatrack`** via `datatrack/__main__.py`, with a smoke test and usage doc updates.

## [1.2.7] — 2026-05

- Root **Makefile** with `install-editable`, `test`, and `lint` targets; documented in CI and contributor docs.

## [1.2.6] — 2026-05

- New **Developing** guide for contributors (venv, editable install, tests, pre-commit).

## [1.2.5] — 2026-05

- GitHub **issue** and **pull request** templates for clearer reports and reviews.

## [1.2.4] — 2026-05

- Add **SECURITY.md**, refresh LICENSE copyright range, and link security reporting from README, PyPI readme, and contributing guide.

## [1.2.3] — 2026-05

- Unit tests for `datatrack.paths` helpers; CI can be triggered manually via `workflow_dispatch`.

## [1.2.2] — 2026-05

- New **Architecture** guide describing modules, snapshot lifecycle, and extension points.

## [1.2.1] — 2026-05

- New **`datatrack doctor`** command and module for offline layout checks.
- Documentation index at `docs/README.md` with cross-links from each guide.

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
