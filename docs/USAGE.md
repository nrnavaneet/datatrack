# Usage Guide

Datatrack is a high-performance CLI tool for tracking database schema changes with intelligent optimization features.

## Quick Reference

```bash
datatrack --help                    # Get help
datatrack init                      # Initialize project
datatrack connect <connection-url>  # Connect to database
datatrack snapshot                  # Take schema snapshot
datatrack diff <snap1> <snap2>      # Compare snapshots
datatrack lint                      # Check schema quality
```

## Initialize Project

```bash
datatrack init
```

Creates a `.datatrack/` folder with configuration files.

## Database Connections

Connect to your database:

### PostgreSQL
```bash
datatrack connect postgresql://user:pass@localhost:5432/dbname
```

### MySQL
```bash
datatrack connect mysql+pymysql://user:pass@localhost:3306/dbname
```

### SQLite
```bash
datatrack connect sqlite:///path/to/database.db
## Schema Snapshots

### Basic Snapshot
```bash
datatrack snapshot
```

### Performance Options

Datatrack automatically optimizes based on schema size:

```bash
# Manual parallel processing
datatrack snapshot --parallel

# Custom worker count
datatrack snapshot --max-workers 8

# Batch processing for large schemas
datatrack snapshot --batch-size 100

# Combined optimization
datatrack snapshot --parallel --max-workers 4 --batch-size 50
```

### Performance Comparison

| Schema Size   | Processing Method    | Performance Gain |
|---------------|----------------------|------------------|
| 1-49 tables   | Standard | Baseline  |                  |
| 50-199 tables | Parallel (4 workers) | 65-70% faster    |
| 200+ tables   | Parallel + Batched   | 70-75% faster    |
## Schema Comparison

Compare schema snapshots:

```bash
# Compare latest two snapshots
datatrack diff

# Compare specific snapshots
datatrack diff snapshot1 snapshot2

# Export diff in different formats
datatrack diff --format json
datatrack diff --format markdown > changes.md
```

## Schema Linting

Check schema quality:

```bash
# Basic linting
datatrack lint

# Strict mode with all checks
datatrack lint --strict

# Export lint report
datatrack lint --export-report lint-report.json
```

## Schema Verification

Validate against custom rules:

```bash
datatrack verify
```

Rules are defined in `schema_rules.yaml`.

## Export and History

Export snapshots:

```bash
# Export latest snapshot
datatrack export

# Export as JSON
datatrack export --format json

# Export specific snapshot
datatrack export snapshot_20240730_120000
```

View snapshot history:

```bash
datatrack history
```

## Complete Pipeline

Run the full workflow:

```bash
datatrack pipeline run
```

This executes: snapshot → lint → verify → diff → export.

Runs `lint`, `snapshot`, `verify`, `diff`, and `export` together.


For advanced use cases and integration into CI/CD, visit:

**https://github.com/nrnavaneet/datatrack**
