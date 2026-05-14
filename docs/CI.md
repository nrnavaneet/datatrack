# Continuous integration

[← Documentation home](../README.md)

GitHub Actions runs on every push and pull request to `main` (see `.github/workflows/ci.yml`). **Concurrency** is configured so newer commits on the same branch cancel older in-flight workflow runs, keeping the queue short for fast feedback. The workflow declares **`permissions: contents: read`** so the default `GITHUB_TOKEN` stays read-only for repository contents.

Steps in order:

1. **Checkout** the repository.
2. **Python 3.11** with pip cache keyed off `requirements.txt` (kept in sync with `pyproject.toml` for reproducible CI).
3. **Editable install** (`pip install -e .`) plus `pytest`.
4. **`datatrack init`** as a smoke test (allowed to no-op if already initialised).
5. **pre-commit** on all files (includes `check-merge-conflict` for stray `<<<<<<<` markers).
6. **`pytest -q tests/`** for the unit suite (includes packaging metadata checks, `paths.__all__` export tests, service module docstring checks, `python -m datatrack --help`, and path layout tests). Discovery defaults live in `pyproject.toml` under `[tool.pytest.ini_options]`.

On GitHub you can also run **Actions → Datatrack CI → Run workflow** (`workflow_dispatch`). A **weekly schedule** (Mondays 12:00 UTC) re-runs the same job on `main` even without new commits. The `test` job has a **30 minute** wall-clock timeout so hung steps fail fast instead of consuming runner quota indefinitely.

To reproduce locally:

```bash
pip install -e .
pre-commit run --all-files
python3 -m pytest tests/ -q
```

Or, after an editable install, `make test` and `make lint` run the same pytest and pre-commit entrypoints as the Makefile shortcuts. `make clean` drops local `build/`, `dist/`, and egg-info artefacts from packaging experiments. `make list-docs` lists `docs/*.md` filenames to sanity-check the index.

Contributors should mirror the [pull request template](https://github.com/nrnavaneet/datatrack/blob/main/.github/PULL_REQUEST_TEMPLATE.md) locally—especially the changelog/version boxes—before requesting review on release-related branches. Keep generated artefacts (`.databases/`, `htmlcov/`, `dist/`) out of commits; they are listed in `.gitignore`. See [Testing](TESTING.md) for what CI’s pytest job is meant to cover.

## When CI fails

1. **Pre-commit** — run `pre-commit run --all-files` locally; failures are usually formatting or YAML issues.
2. **pytest** — run `PYTHONPATH=. python3 -m pytest tests/ -q`; packaging meta tests require `CHANGELOG.md` to include a section for the current `pyproject.toml` version.
3. **Smoke `datatrack init`** — safe to ignore if your branch only touches docs; investigate if CLI imports regressed.

If failures only appear on Ubuntu CI but not macOS, check path case sensitivity and line endings (see `.editorconfig`).
