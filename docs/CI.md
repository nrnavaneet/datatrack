# Continuous integration

[← Documentation home](../README.md)

GitHub Actions runs on every push and pull request to `main` (see `.github/workflows/ci.yml`).

Steps in order:

1. **Checkout** the repository.
2. **Python 3.11** with pip cache keyed off `requirements.txt`.
3. **Editable install** (`pip install -e .`) plus `pytest`.
4. **`datatrack init`** as a smoke test (allowed to no-op if already initialised).
5. **pre-commit** on all files.
6. **`pytest -q tests/`** for the unit suite.

On GitHub you can also run **Actions → Datatrack CI → Run workflow** (`workflow_dispatch`).

To reproduce locally:

```bash
pip install -e .
pre-commit run --all-files
python3 -m pytest tests/ -q
```
