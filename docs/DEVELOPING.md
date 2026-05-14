# Developing Datatrack

[← Documentation home](README.md)

Use this guide when you clone the repository to add features or fix bugs. End users who only install from PyPI can skip it.

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
```

Run the full test suite before opening a PR:

```bash
python3 -m pytest tests/ -q
```

Or use `make test` from the repository root if you prefer a short alias.

## Layout

- `datatrack/` — package source (`cli.py`, services, `paths.py`).
- `tests/` — pytest modules; command behaviour is covered under `tests/commands/`.
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
