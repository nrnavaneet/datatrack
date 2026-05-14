# Changelog

All notable changes to this project are documented here. Versions follow the package version in `pyproject.toml`.

## [1.2.51] — 2026-05

- Document optional **`TZ`** interactions with timestamps and link them from compatibility, performance, and troubleshooting guides.

## [1.2.50] — 2026-05

- Add a **Pipeline** guide describing `pipeline run` stages and when to use `doctor` instead.

## [1.2.49] — 2026-05

- Expand the **PyPI readme** contributing blurb with roadmap and deeper doc pointers for package-page readers.

## [1.2.48] — 2026-05

- Restrict the **CI workflow** token to `contents: read` and document the permission model in CI and security notes.

## [1.2.47] — 2026-05

- Document **what to do when CI fails** in the CI guide and cross-link it from troubleshooting, testing, and contributor docs.

## [1.2.46] — 2026-05

- Add **`make list-docs`** to print top-level markdown files under `docs/` for documentation index maintenance.

## [1.2.45] — 2026-05

- Add tests that **`paths.__all__`** only lists real module attributes so the public API cannot drift silently.

## [1.2.44] — 2026-05

- Add **Documentation style** guidance for voice, links, and changelog bullets across the doc set.

## [1.2.43] — 2026-05

- Add **Credits** for maintainer attribution and upstream library acknowledgement.

## [1.2.42] — 2026-05

- Publish an informal **Roadmap** and link it from support and contributor-facing docs.

## [1.2.41] — 2026-05

- Add a **Compatibility** guide for Python, database drivers, and terminal or locale considerations.

## [1.2.40] — 2026-05

- Add **MANIFEST.in** so source distributions include LICENSE, SECURITY, and markdown documentation trees.

## [1.2.39] — 2026-05

- Declare **`__all__`** on `datatrack.paths` and add tests that keep `pyproject.toml` and `CHANGELOG.md` versions aligned.

## [1.2.38] — 2026-05

- Add a **Support** page with issue etiquette, redaction expectations, and links to FAQ and troubleshooting.

## [1.2.37] — 2026-05

- Add **CODEOWNERS** for default GitHub review routing and document it in contributor and security notes.

## [1.2.36] — 2026-05

- Add a **Testing** guide describing pytest layout, offline defaults, and manual integration expectations.

## [1.2.35] — 2026-05

- Add **Python modules** reference for safe imports (`paths`, `doctor`, `tracker`, etc.) vs CLI-heavy entrypoints.

## [1.2.34] — 2026-05

- Cross-link **examples** with troubleshooting and performance docs so local experiments have an obvious escalation path.

## [1.2.33] — 2026-05

- Expand **security** guidance around shell history, CI logs, and redacted support questions across SECURITY, FAQ, and troubleshooting docs.

## [1.2.32] — 2026-05

- Clarify **`python -m datatrack`** usage for PATH-less environments and tighten the help smoke test.

## [1.2.31] — 2026-05

- Document why **`requirements.txt`** mirrors `pyproject.toml` for contributor installs and CI caching.

## [1.2.30] — 2026-05

- Clarify **`schema_rules.yaml`** header comments and cross-link verify behaviour from the FAQ, glossary, and troubleshooting guides.

## [1.2.29] — 2026-05

- Document how **`tests/test_paths.py`** guards export and snapshot directory layout alongside architecture notes.

## [1.2.28] — 2026-05

- Broaden **`.gitignore`** coverage for build trees, pytest caches, and coverage reports so accidental commits stay rare.

## [1.2.27] — 2026-05

- Add a **Contributing** section to the PyPI readme with links back to the full GitHub documentation set.

## [1.2.26] — 2026-05

- Add a **`make clean`** target for local build and pytest cache directories, documented for contributors.

## [1.2.25] — 2026-05

- Promote **`disconnect` + `connect`** guidance to its own usage section with anchors from installation and FAQ.

## [1.2.24] — 2026-05

- Configure GitHub Actions **concurrency** so newer pushes cancel superseded workflow runs on the same branch.

## [1.2.23] — 2026-05

- Expand the **pull request template** with risk notes and explicit changelog/version checklist items.

## [1.2.22] — 2026-05

- Align the **minimal snapshot example** with tracker-shaped YAML (`indexes` per table) and cross-link it from architecture notes.

## [1.2.21] — 2026-05

- Strengthen **doctor** coverage and clarify how `ok` / `missing` lines should be read in support material.

## [1.2.20] — 2026-05

- Document optional **`LANG` / `LC_ALL`** interactions with Rich output and link environment notes from installation and glossary pages.

## [1.2.19] — 2026-05

- Clarify **Code of Conduct** reporting expectations and link them from contributing docs and the FAQ.

## [1.2.18] — 2026-05

- Add a **Releasing** guide for maintainers covering version bumps, tags, and PyPI uploads.

## [1.2.17] — 2026-05

- Expand **benchmark** documentation: what artefacts are created, when to run locally, and why CI skips timing scripts.

## [1.2.16] — 2026-05

- Add an **examples workflow** document that orders `init` through `pipeline run` for onboarding.

## [1.2.15] — 2026-05

- Run **CI on a weekly cron** against `main` in addition to pushes and manual dispatch.

## [1.2.14] — 2026-05

- Add a **Glossary** defining snapshot, lint, verify, pipeline, and related terms used across the docs.

## [1.2.13] — 2026-05

- Add an **FAQ** for recurring questions about on-disk layout, lint vs verify, and offline tests.

## [1.2.12] — 2026-05

- Declare **pytest** defaults in `pyproject.toml` and add `tests/conftest.py` for future shared fixtures.

## [1.2.11] — 2026-05

- Enable **Dependabot** for GitHub Actions and pip with a weekly schedule, and document reviewer expectations.

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
