# Testing

[← Documentation home](README.md)

## Goals

- **Fast by default** — `tests/` runs without PostgreSQL, MySQL, or network databases.
- **Deterministic** — filesystem and DB name helpers are patched so snapshots do not touch real `.databases/` trees during unit runs.
- **Smoke critical entrypoints** — `python -m datatrack --help` is exercised so module mode keeps working in minimal environments.

Doc-only PRs should still follow [Documentation style](DOCUMENTATION_STYLE.md) for cross-links and changelog bullets.

End-user command summaries live in [Usage](USAGE.md#command-quick-reference) alongside the long-form walkthrough.

## Commands

```bash
python3 -m pytest tests/ -q
# or
make test
```

## Where tests live

| Path | Focus |
|------|--------|
| `tests/commands/` | CLI-adjacent behaviour (e.g. diff with patched paths). |
| `tests/test_paths.py` | Directory layout contracts. |
| `tests/test_doctor.py` | Offline doctor formatting. |
| `tests/test_paths_exports.py` | `paths.__all__` matches real attributes. |
| `tests/test_packaging_meta.py` | `pyproject.toml` / `CHANGELOG.md` consistency checks. |
| `tests/test_module_invocation.py` | `python -m datatrack` smoke. |
| `tests/conftest.py` | Reserved for shared fixtures. |

## Integration and benchmarks

Real-engine tests and timing harnesses are **manual** — see [Benchmark harness](../benchmark_tests/README.md) and run databases on your machine when needed.

When diagnosing **CI-only** failures, start with [CI](CI.md#when-ci-fails) before assuming a database regression.
