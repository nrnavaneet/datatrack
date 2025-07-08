# Usage Guide for Datatrack

After installing Datatrack, you can use it to track schema changes in your SQL databases.


## 1. Initialize a Datatrack Project

```bash
datatrack init
```

This creates a `.datatrack/` folder with configuration files.

## 2. Take a Schema Snapshot

```bash
datatrack snapshot --source sqlite:///.databases/example.db
```

This saves the current database schema to a snapshot.

## 3. Lint the Schema

```bash
datatrack lint
```

Detects issues in schema naming or structure.

## 4. Verify Schema Rules

```bash
datatrack verify
```

Checks schema against rules defined in `schema_rules.yaml`.

## 5. View Schema Differences

```bash
datatrack diff
```

Shows differences between the latest two schema snapshots.


## 6. Export Snapshots or Diffs

```bash
datatrack export --type snapshot --format json --output output/snapshot.json
datatrack export --type diff --format yaml --output output/diff.yaml
```

## 7. View Snapshot History

```bash
datatrack history
```

Lists all schema snapshots stored so far.


## 8. Run the Full Pipeline

```bash
datatrack pipeline run --source sqlite:///.databases/example.db
```

This runs `lint`, `snapshot`, `verify`, `diff`, and `export` in one step.

You can specify the export directory:

```bash
datatrack pipeline run --source sqlite:///.databases/example.db --export-dir my_output_dir
```

For advanced usage and integration into CI/CD, refer to the full documentation.
