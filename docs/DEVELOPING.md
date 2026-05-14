# Developing Datatrack

[← Documentation home](README.md)

Use this guide when you clone the repository to add features or fix bugs. End users who only install from PyPI can skip it.

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pre-commit install
```

The `datatrack` console script is the usual entrypoint; in a checkout you can also run `python3 -m datatrack --help` after an editable install.

Run the full test suite before opening a PR:

```bash
python3 -m pytest tests/ -q
```

Pytest reads `[tool.pytest.ini_options]` in `pyproject.toml` so only `tests/` is collected by default.

From the repository root you can also run **`make test`** or **`make lint`** (see the root `Makefile`).

The repository ships an [`.editorconfig`](../.editorconfig) so most editors pick consistent indentation and newlines.

## Layout

- `datatrack/` — package source (`cli.py`, services, `paths.py`).
- `tests/` — pytest modules; command behaviour is covered under `tests/commands/`. Shared hooks belong in `tests/conftest.py`.
- `docs/` — user and contributor documentation; keep cross-links in `docs/README.md` current when you add pages.

## Pre-commit

Hooks run Black, Ruff, isort, and basic file checks. Run them on all files after large edits:

```bash
pre-commit run --all-files
```

## Version and changelog

Release versions live in `pyproject.toml`. User-facing changes should have a short entry under the matching version in `CHANGELOG.md` in the same PR when behaviour or docs change materially.

## See also

- [Architecture](ARCHITECTURE.md) — how modules fit together.
- [Contributing](contribute/CONTRIBUTING.md) — branch naming and review expectations.
- [Benchmark harness](../benchmark_tests/README.md) — optional local timings that complement [Performance](PERFORMANCE.md).
