# Usage Guide for Datatrack

[← Documentation home](README.md)

Datatrack is a CLI tool for tracking, linting, verifying, and exporting database schema changes.

Terms like **snapshot**, **lint**, and **verify** are defined in the [Glossary](GLOSSARY.md). For programmatic use, see [Python modules](MODULES.md). The table below complements `datatrack --help`; full narrative for each step follows in numbered sections.

## Helpful Commands

Datatrack comes with built-in help and guidance for every command. Use this to quickly learn syntax and options:

```bash
datatrack --help
# or, equivalent when running from a checkout with an editable install:
python3 -m datatrack --help
or
datatrack -h
```

## Command quick reference

| Command | One-line purpose |
|---------|------------------|
| `doctor` | Offline checks for `.datatrack/`, `db_link.yaml`, export paths, and `schema_rules.yaml`. |
| `init` | Create the local `.datatrack/` metadata folder. |
| `connect` / `disconnect` | Save or clear the active database URI. |
| `snapshot` | Write YAML schema snapshots under `.databases/exports/…`. |
| `lint` / `verify` | Heuristics and `schema_rules.yaml` checks on the latest snapshot. |
| `diff` | Compare the two newest snapshots. |
| `export` | Emit JSON or YAML artefacts. |
| `history` | List snapshot files for the connected database. |
| `pipeline run` | Run lint, snapshot, verify, diff, and export in sequence. |

## 0. Doctor (sanity check layout)

```bash
datatrack doctor
```

Prints whether `.datatrack/`, the saved DB link file, export paths, and `schema_rules.yaml` exist. Does **not** open a database connection.

Each line is labelled `ok` or `missing` so you can paste the output into bug reports without sharing secrets.

## 1. Initialize a Datatrack Project

```bash
datatrack init
```

Creates a `.datatrack/` folder with configuration.

## 2. Connect to a Database

Save your DB connection for future use:

### MySQL

```bash
datatrack connect mysql+pymysql://root:<password>@localhost:3306/<database-name>
```

### PostgreSQL

```bash
datatrack connect postgresql+psycopg2://postgres:<password>@localhost:5432/<database-name>
```


### SQLite

```bash
datatrack connect sqlite:///.databases/<database-name>
```

## 2b. Clear or rotate the saved URI

Datatrack stores **one** connection string at a time. To point it at a different database, remove the saved link first, then connect again:

```bash
datatrack disconnect
datatrack connect <new-uri>
```

## 3. Take a Schema Snapshot

```bash
datatrack snapshot
```

Include sample row data in the snapshot:
```bash
datatrack snapshot --include-data
```

Limit the number of rows per table captured (only works with --include-data):
```bash
datatrack snapshot --include-data --max-rows 100
```

Saves the current schema to `.databases/exports/<db_name>/snapshots/`.

## 4. Lint the Schema

```bash
datatrack lint
```

Detects issues in naming and structure.

## 5. Verify Schema Rules

```bash
datatrack verify
```

Validates schema against `schema_rules.yaml`.

## 6. View Schema Differences

```bash
datatrack diff
```

Shows table and column changes between the latest two snapshots.

## 7. Export Snapshots or Diffs

Export latest snapshot as YAML (default)
```bash
datatrack export
```

Explicitly export snapshot as YAML
```bash
datatrack export --type snapshot --format yaml
```
Export latest diff as JSON
```bash
datatrack export --type diff --format json
```

Output is saved in `.databases/exports/<db_name>/`.

## 8. View Snapshot History

```bash
datatrack history
```

Displays all snapshot timestamps and table counts.

## 9. Run the Full Pipeline

```bash
datatrack pipeline run
```

Runs `lint`, `snapshot`, `verify`, `diff`, and `export` together.

See the dedicated [Pipeline](PIPELINE.md) guide for stage-by-stage behaviour and failure triage tips.

A narrative walkthrough from `init` to `pipeline run` lives under [`examples/workflow.md`](https://github.com/nrnavaneet/datatrack/blob/main/examples/workflow.md).

## 10. When something goes wrong

See [Troubleshooting](TROUBLESHOOTING.md) for disconnect issues, missing snapshots, and driver errors.

Answers to common design questions (single URI file, where snapshots live, lint vs verify) live in the [FAQ](FAQ.md).

For advanced use cases and integration into CI/CD, visit:

**https://github.com/nrnavaneet/datatrack**

Deeper module layout: [Architecture](ARCHITECTURE.md). Path constants are covered by [`tests/test_paths.py`](https://github.com/nrnavaneet/datatrack/blob/main/tests/test_paths.py). Documentation conventions: [Documentation style](DOCUMENTATION_STYLE.md).
