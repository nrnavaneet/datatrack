<p align="center">
  <a href="https://pypi.org/project/dbtracker/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/dbtracker?color=0052FF&labelColor=090422" />
  </a>
  <a href="https://pypi.org/project/dbtracker/">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/dbtracker?color=0052FF&labelColor=090422" />
  </a>
  <a href="https://github.com/nrnavaneet/datatrack">
    <img src="https://img.shields.io/github/stars/nrnavaneet/datatrack?color=0052FF&labelColor=090422" />
  </a>
  <a href="https://github.com/nrnavaneet/datatrack/pulse">
    <img src="https://img.shields.io/github/commit-activity/m/nrnavaneet/datatrack?color=0052FF&labelColor=090422" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/INSTALLATION.md">Installation</a>
  ·
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/USAGE.md">Usage</a>
  ·
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/README.md">Docs index</a>
  ·
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/ENVIRONMENT.md">Environment</a>
  ·
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/contribute/CONTRIBUTING.md">Contributing</a>
  ·
  <a href="https://github.com/nrnavaneet/datatrack/tree/main/docs/contribute/CODE_OF_CONDUCT.md">Code of Conduct</a>
</p>

# Datatrack

**Datatrack** is a lightweight and open-source command-line tool designed to help data engineers and platform teams track database schema changes across versions. It ensures that schema updates are transparent and auditable, helping prevent silent failures in downstream pipelines.

## Key Features

- Capture schema snapshots from SQL-compatible databases (PostgreSQL, SQLite, MySQL, etc.)
- Lint schemas for naming issues and structural smells
- Verify schema compliance against custom rules
- Compare schema versions and generate diffs
- Export snapshots and diffs to JSON or YAML formats
- Run the full schema audit pipeline with a single command

## Why Use Datatrack

Managing schema changes in evolving environments is complex. Even a small change in column name, type, or structure can silently break dashboards or data pipelines. **Datatrack** helps prevent that by enabling:

- Git-like version control for database schemas
- Transparent collaboration and visibility within teams
- Faster issue detection with automatic diffs and rule checks

## Performance & Cost Savings

Datatrack’s parallel and batched snapshot engine delivers **significant performance improvements** for real-world databases.
Benchmarks were run in August 2025 on a MacBook Pro M2, Python 3.11, using SQLite and PostgreSQL.

| Database Size | Tables | Serial Time | Parallel Time | Speedup | Time Saved (per 1k runs) | Time Saved (per 50k runs) |
|--------------:|-------:|------------:|--------------:|--------:|-------------------------:|--------------------------:|
| **Small**     | 12     | 0.18 s      | 0.09 s        | **2×**  | 90 s                     | 75 min                    |
| **Medium**    | 75     | 0.95 s      | 0.32 s        | **3×**  | 630 s (10.5 min)         | 8.75 hrs                  |
| **Large**     | 250    | 2.80 s      | 0.80 s        | **3.5×**| 2,000 s (33 min)         | 27 hrs                    |

### Key Takeaways

- **Snapshot time reduced by 65–75%** for medium and large databases.
- **Scales linearly**: higher workloads → greater savings.
- **Faster developer feedback**: reduced CI/CD wait times, fewer timeouts.
- **Lower infrastructure costs**: less CPU time means direct savings on cloud compute.

### Datatrack Architecture

```text
+-------------------+
|      User/CLI     |
+-------------------+
          |
          v
+-------------------+
|   Typer CLI App   |  (datatrack/cli.py)
+-------------------+
          |
          v
+-------------------+
|   Command Router  |  (CLI commands: snapshot, diff, lint, verify, export, pipeline)
+-------------------+
          |
          v
+-------------------+
|   Tracker Logic   |  (datatrack/tracker.py)
|-------------------|
| - Introspection   |
| - Caching         |
| - Parallel Fetch  |
| - Batched Fetch   |
+-------------------+
          |
          v
+-------------------+
|   Path layout     |  (datatrack/paths.py — config, exports, snapshot dirs)
+-------------------+
          |
          v
+-------------------+
|   SQLAlchemy ORM  |  (DB connection, inspection)
+-------------------+
          |
          v
+-------------------+
|   Database Layer  |  (PostgreSQL, SQLite, MySQL, etc.)
+-------------------+
          |
          v
+-------------------+
|   Export/History  |  (JSON/YAML, snapshot history)
+-------------------+
          |
          v
+-------------------+
|   CI/CD & Audits  |  (Integration, reporting)
+-------------------+
```

### Pipeline Execution Flow (Mermaid Diagram)
```text
flowchart TD
    A[User/CLI] --> B[Typer CLI App]
    B --> C[Pipeline Command (pipeline run)]
    C --> D1[SQLAlchemy DB Connection]
    D1 --> D2[Database (PostgreSQL, MySQL, SQLite, etc.)]
    D2 --> D3[Snapshot: Save latest schema\n(via Tracker Logic: parallel/cached introspection)]
    D3 --> D4[Linting: Check naming, types, ambiguity]
    D4 --> D5[Verify: Apply schema rules (snake_case, reserved words)]
    D5 --> D6[Diff: Compare with previous snapshot]
    D6 --> D7[Export: Save snapshot & diff as JSON]
    D7 --> D8[Export/History/Reporting]
```

### Real-World Impact

For a team running 50,000 large snapshots/month, Datatrack saves ~27 hours of CPU time.
At typical cloud compute rates, this translates into **hundreds of dollars per year** in savings.
The bigger win, however, is **developer productivity and reliability**: faster pipelines, earlier error detection,
and less risk of schema-related outages.

## Documentation

Please refer to the following docs for detailed guidance:

- [Documentation home (all guides)](https://github.com/nrnavaneet/datatrack/tree/main/docs/README.md)
- [Python modules (import surface)](https://github.com/nrnavaneet/datatrack/blob/main/docs/MODULES.md)
- [Testing (pytest layout)](https://github.com/nrnavaneet/datatrack/blob/main/docs/TESTING.md) (includes packaging metadata consistency tests)
- [CI overview](https://github.com/nrnavaneet/datatrack/blob/main/docs/CI.md)
- [Architecture (modules & data flow)](https://github.com/nrnavaneet/datatrack/tree/main/docs/ARCHITECTURE.md) (path layout tests live in `tests/test_paths.py`)
- [Performance (benchmarks & parallelism)](https://github.com/nrnavaneet/datatrack/blob/main/docs/PERFORMANCE.md)
- [Benchmark harness (local timings)](https://github.com/nrnavaneet/datatrack/tree/main/benchmark_tests)
- [Developing locally](https://github.com/nrnavaneet/datatrack/blob/main/docs/DEVELOPING.md) (`datatrack`, `python -m datatrack`, or module mode in containers)
- [Compatibility (Python & databases)](https://github.com/nrnavaneet/datatrack/blob/main/docs/COMPATIBILITY.md)
- [Installation Guide](https://github.com/nrnavaneet/datatrack/tree/main/docs/INSTALLATION.md) (editable installs use `requirements.txt` + `pyproject.toml` together)
- [Usage Instructions](https://github.com/nrnavaneet/datatrack/tree/main/docs/USAGE.md) (includes a dedicated **disconnect** section for rotating URIs)
- [FAQ (common design questions)](https://github.com/nrnavaneet/datatrack/blob/main/docs/FAQ.md)
- [Examples (workflow, minimal snapshot, troubleshooting links)](https://github.com/nrnavaneet/datatrack/tree/main/examples)
- [Glossary](https://github.com/nrnavaneet/datatrack/blob/main/docs/GLOSSARY.md)
- [Environment variables](https://github.com/nrnavaneet/datatrack/tree/main/docs/ENVIRONMENT.md) (includes locale notes for Rich output)
- [Contributing Guide](https://github.com/nrnavaneet/datatrack/blob/main/docs/contribute/CONTRIBUTING.md) (also summarised briefly on PyPI via `pypiREADME.md`)
- [Code of Conduct](https://github.com/nrnavaneet/datatrack/tree/main/docs/contribute/CODE_OF_CONDUCT.md)
- [Support (bug report checklist)](https://github.com/nrnavaneet/datatrack/blob/main/docs/SUPPORT.md)
- [Roadmap (informal priorities)](https://github.com/nrnavaneet/datatrack/blob/main/docs/ROADMAP.md)
- [Credits](https://github.com/nrnavaneet/datatrack/blob/main/docs/CREDITS.md)
- [Security](https://github.com/nrnavaneet/datatrack/blob/main/SECURITY.md) (includes guidance on shell history and leaked connection strings)
- [Releasing (maintainers)](https://github.com/nrnavaneet/datatrack/blob/main/docs/RELEASING.md) (`MANIFEST.in` shapes the sdist)

Issue and PR templates live under [`.github/`](https://github.com/nrnavaneet/datatrack/tree/main/.github), including [`CODEOWNERS`](https://github.com/nrnavaneet/datatrack/blob/main/.github/CODEOWNERS) for default review routing when enabled in repository settings. The pull request template records **risk notes** and reminds authors to bump `CHANGELOG.md` / `pyproject.toml` together when shipping user-visible changes. After cloning, `make test` and `make lint` mirror the CI pytest and pre-commit steps. An [`.editorconfig`](https://github.com/nrnavaneet/datatrack/blob/main/.editorconfig) file keeps basic formatting defaults aligned across editors. The root [`.gitignore`](https://github.com/nrnavaneet/datatrack/blob/main/.gitignore) excludes `.databases/`, `.venv/`, and common build artefacts so they never enter commits by mistake. **Dependabot** opens weekly dependency update PRs for Actions and pip. GitHub Actions also runs a **weekly schedule** on `main` to catch drift when no PRs are open, and **concurrency** settings cancel outdated workflow runs when you push new commits to the same branch.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/nrnavaneet/datatrack/blob/main/LICENSE) file for details.

Community participation follows the [Code of Conduct](https://github.com/nrnavaneet/datatrack/blob/main/docs/contribute/CODE_OF_CONDUCT.md); reports are handled privately via the contact listed there.

## Maintainer

Developed and maintained by [N R Navaneet](https://github.com/nrnavaneet).
