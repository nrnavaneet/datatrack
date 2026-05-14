# Benchmarks

`parallel_processing.py` builds three synthetic SQLite databases (small / medium / large table counts), then times `datatrack.tracker.snapshot` against each.

Run from the **repository root** after an editable install:

```bash
pip install -e .
python benchmark_tests/parallel_processing.py
```

The script writes under `.databases/` in the current working directory; it is meant for local investigation, not for CI (CI runs `pytest` only).
