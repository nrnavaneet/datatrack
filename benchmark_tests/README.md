# Benchmarks

[← Documentation home](../docs/README.md)

`parallel_processing.py` builds three synthetic SQLite databases (small / medium / large table counts), then times `datatrack.tracker.snapshot` against each.

## What gets created

- SQLite files under `.databases/` (see `datatrack.paths.DATABASES_DIR`) named `small.db`, `medium.db`, and `large.db`.
- Console output with Rich tables summarising serial vs parallel timings.

## When to use this

- Local tuning before proposing performance-related code changes.
- Generating numbers that match the tables in [Performance](../docs/PERFORMANCE.md).

## When **not** to use this

- **CI** — the main workflow only runs `pytest`; benchmarks are intentionally manual to avoid flaky timing assertions on shared runners.

Run from the **repository root** after an editable install:

```bash
pip install -e .
python benchmark_tests/parallel_processing.py
```

The script writes under `.databases/` in the current working directory; it is meant for local investigation, not for CI (CI runs `pytest` only).

The **large** profile creates a multi-hundred-megabyte SQLite file; ensure you have **several gigabytes** of free disk before running the full suite, or delete prior `.databases/*.db` files between runs.

If numbers diverge from the published tables, capture your hardware, Python version, and whether the database files were on SSD vs network storage in your notes.
