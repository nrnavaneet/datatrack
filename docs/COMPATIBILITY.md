# Compatibility

[← Documentation home](README.md)

## Python

The supported range is defined by `requires-python` in `pyproject.toml` (currently **3.7+**). GitHub Actions runs a recent CPython (see `docs/CI.md`); older interpreters depend on published wheels for dependencies.

## Databases and drivers

- **PostgreSQL** — `postgresql+psycopg2://…` via `psycopg2-binary`.
- **MySQL** — `mysql+pymysql://…` via `pymysql`.
- **SQLite** — `sqlite://…` through SQLAlchemy’s built-in backend.

URI formats follow SQLAlchemy URL rules; see [Usage](USAGE.md) for examples.

## Terminals and locales

Rich tables and Typer help assume a Unicode-capable terminal. If borders render incorrectly over SSH, set UTF-8 locales as described in [Environment](ENVIRONMENT.md).
