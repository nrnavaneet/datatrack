# Datatrack - Lightweight Schema Change Tracker

Datatrack is a minimal open-source CLI tool to **track schema changes** across versions in your data systems. It's built for **Data Engineers** and **Platform Teams** who want **automated schema linting, verification, diffs, and export** across snapshots.


## Features

- Snapshot schemas from any SQL-compatible DB
- Lint schema naming issues
- Enforce verification rules
- Compare schema snapshots (diff)
- Export to JSON/YAML for auditing or CI
- Full pipeline in one command

##  Installation

Option 1: Install from PyPI (production use)
```bash
pip install datatrack-core
```
This is the easiest and recommended way to use datatracker as a CLI tool in your workflows.


Option 2: Install from GitHub (for development)
```bash
git clone https://github.com/nrnavaneet/datatrack.git
cd datatrack
pip install -r requirements.txt
pip install -e .
```
This method is ideal if you want to contribute or modify the tool.


##  How to Use

### 1. Initialize Tracking

```bash
datatrack init
```

Creates `.datatrack/`, `.databases/`, and optional initial files.


### 2. Connect to a Database

Save your DB connection for future use:

### MySQL

```bash
datatrack connect mysql+pymysql://root:<password>@localhost:3306/<database-name>
```

### PostgreSQL

```bash
datatrack connect postgresql+psycopg2://postgres:<password>@localhost:5432/<database-name>
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

For advanced use cases and integration into CI/CD, visit:

**https://github.com/nrnavaneet/datatrack**
