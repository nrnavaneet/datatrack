# Frequently asked questions

[← Documentation home](README.md)

## Why does Datatrack only store one database URI?

The CLI targets a single **active** project context: `.datatrack/db_link.yaml` holds one connection string so commands like `snapshot` and `pipeline run` do not need extra flags every time. Switch databases with `datatrack disconnect` followed by `datatrack connect <new-uri>` (see [Usage §2b](USAGE.md#2b-clear-or-rotate-the-saved-uri)).

## Where do snapshots live on disk?

Under `.databases/exports/<database_name>/snapshots/`, with filenames timestamped when the snapshot was taken. The exact helper is `datatrack.paths.snapshot_dir(db_name)` if you integrate programmatically.

## Do I need PostgreSQL or MySQL running for the unit tests in this repository?

No. CI and the default `tests/` suite patch filesystem and database discovery so they stay offline. Use your own database when exercising `connect` and `snapshot` manually.

## What is the difference between `lint` and `verify`?

**Lint** applies lightweight naming and structural heuristics to the latest snapshot YAML. **Verify** enforces declarative rules from `schema_rules.yaml` (reserved words, casing, and similar policies). Run both in CI; `pipeline run` executes them in a sensible order alongside snapshotting and diffing.

## Which environment variables matter for the CLI?

Locale and identity-related variables (`USER`, `HOME`, `LANG`, `LC_ALL`) are summarised in [Environment](ENVIRONMENT.md).

## Can I run Datatrack without installing the `datatrack` script on `PATH`?

Yes, after an editable install you can use `python3 -m datatrack --help` (see [Usage](USAGE.md)).

## Where do maintainers document PyPI releases?

See [Releasing](RELEASING.md) for versioning, tags, and Twine uploads.

## How do I report a code of conduct concern?

Use the contact listed in [Code of Conduct](contribute/CODE_OF_CONDUCT.md); avoid posting sensitive personal details in public GitHub threads.
