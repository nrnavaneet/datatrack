# Troubleshooting

[← Documentation home](README.md)

Before opening a new GitHub issue, read [Support](SUPPORT.md) for what maintainers need in a report.

If formatting hooks fail only on your machine, confirm your editor respects the repository [`.editorconfig`](https://github.com/nrnavaneet/datatrack/blob/main/.editorconfig) and that `pre-commit run --all-files` is clean. Setting a UTF-8 locale (`LANG=en_US.UTF-8` or similar) avoids odd Rich borders in some SSH sessions.

If `git status` shows thousands of files under `.databases/` or `.venv/`, ensure you are not staging ignored paths; the root [`.gitignore`](https://github.com/nrnavaneet/datatrack/blob/main/.gitignore) lists the canonical exclusions.

## `datatrack connect` says a database is already connected

Only one saved URI is stored under `.datatrack/db_link.yaml`. Run:

```bash
datatrack disconnect
```

then connect again with the new URI.

When pasting CLI output for support, scrub passwords and tokens—shell history and CI logs are not secret stores.

## Quick layout check without connecting

```bash
datatrack doctor
```

Shows whether expected paths and `schema_rules.yaml` exist; it does not run SQL.

The report labels each check as `ok` or `missing`; if everything is `missing`, you may be running the command outside a project directory that was initialised with `datatrack init`.

If `schema_rules.yaml` is missing but you expect it, confirm you are in the repository root (or copied the file into your project) because verify reads that exact filename relative to the working directory.

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

If packaging experiments leave `build/` or `dist/` folders behind, run `make clean` from the repository root before opening a PR.

Some commands still expect a configured `.datatrack/` tree; unit tests under `tests/` patch paths so they do not need a live database.

Unfamiliar with Datatrack vocabulary? Skim the [Glossary](GLOSSARY.md).
