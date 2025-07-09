# Usage Guide for Datatrack

Datatrack is a CLI tool for tracking, linting, verifying, and exporting database schema changes.

## 1. Initialize a Datatrack Project

```bash
datatrack init
```

Creates a `.datatrack/` folder with configuration.

## 2. Connect to a Database

Save your DB connection for future use:

### MySQL

```bash
datatrack connect mysql+pymysql://root:mysecurepassword@localhost:3306/mydatabase
```

### PostgreSQL

```bash
datatrack connect postgresql+psycopg2://postgres:mysecurepassword@localhost:5432/mydatabase
```


## 3. Take a Schema Snapshot

```bash
datatrack snapshot
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

Optionally specify a custom source or output directory:

```bash
datatrack pipeline run --source sqlite:///.databases/example.db --export-dir output_dir
```

For advanced use cases and integration into CI/CD, visit:

**https://github.com/nrnavaneet/datatrack**
