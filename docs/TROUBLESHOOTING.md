# Troubleshooting

[← Documentation home](README.md)

## `datatrack connect` says a database is already connected

Only one saved URI is stored under `.datatrack/db_link.yaml`. Run:

```bash
datatrack disconnect
```

then connect again with the new URI.

## Quick layout check without connecting

```bash
datatrack doctor
```

Shows whether expected paths and `schema_rules.yaml` exist; it does not run SQL.

## `datatrack snapshot` or `lint` says no snapshots

You need at least one successful `datatrack snapshot` after `connect`. Snapshots live under:

`.databases/exports/<db_name>/snapshots/`

That path is built in code as `datatrack.paths.snapshot_dir(db_name)`; integrations should import it rather than duplicating string paths.

If snapshots feel slow on large schemas, read [Performance](PERFORMANCE.md) for parallelism expectations before changing infrastructure.

If the directory name looks wrong, check that your connection URI points at the intended database name (especially for PostgreSQL path segments).

## Import or driver errors when connecting

Install the matching driver in the same environment as Datatrack (`psycopg2-binary` for PostgreSQL, `pymysql` for MySQL). The PyPI package lists these as dependencies, but a minimal `pip install` without extras can still miss drivers in some setups.

## `pytest` fails on a clean clone

Run from the repository root with the package installed editable:

```bash
pip install -e .
python3 -m pytest tests/ -q
```

Some commands still expect a configured `.datatrack/` tree; unit tests under `tests/` patch paths so they do not need a live database.
