# Continuous integration

[← Documentation home](../README.md)

GitHub Actions runs on every push and pull request to `main` (see `.github/workflows/ci.yml`). **Concurrency** is configured so newer commits on the same branch cancel older in-flight workflow runs, keeping the queue short for fast feedback.

Steps in order:

1. **Checkout** the repository.
2. **Python 3.11** with pip cache keyed off `requirements.txt`.
3. **Editable install** (`pip install -e .`) plus `pytest`.
4. **`datatrack init`** as a smoke test (allowed to no-op if already initialised).
5. **pre-commit** on all files.
6. **`pytest -q tests/`** for the unit suite (includes a `python -m datatrack --help` smoke test). Discovery defaults live in `pyproject.toml` under `[tool.pytest.ini_options]`.

On GitHub you can also run **Actions → Datatrack CI → Run workflow** (`workflow_dispatch`). A **weekly schedule** (Mondays 12:00 UTC) re-runs the same job on `main` even without new commits.

To reproduce locally:

```bash
pip install -e .
pre-commit run --all-files
python3 -m pytest tests/ -q
```

Or, after an editable install, `make test` and `make lint` run the same pytest and pre-commit entrypoints as the Makefile shortcuts. `make clean` drops local `build/`, `dist/`, and egg-info artefacts from packaging experiments.

Contributors should mirror the [pull request template](https://github.com/nrnavaneet/datatrack/blob/main/.github/PULL_REQUEST_TEMPLATE.md) locally—especially the changelog/version boxes—before requesting review on release-related branches.
