# Glossary

[← Documentation home](README.md)

| Term | Meaning in Datatrack |
|------|---------------------|
| **Snapshot** | A point-in-time serialisation of schema metadata (tables, columns, constraints) written as YAML under `.databases/exports/<db>/snapshots/`. |
| **Diff** | A textual comparison between the two newest snapshot files for a database, produced by `datatrack diff`. |
| **Lint** | Fast heuristics over the latest snapshot YAML for naming and structural smells (`datatrack lint`). |
| **Verify** | Rule-driven checks declared in `schema_rules.yaml` (`datatrack verify`). |
| **Pipeline** | `datatrack pipeline run` orchestrates snapshot, lint, verify, diff, and export in one invocation. |
| **Doctor** | `datatrack doctor` checks local folders and config files exist without opening a SQL connection. |
| **Export base** | The `.databases/exports/` directory tree where per-database artefacts are stored; see `datatrack.paths`. |

For narrative context, see [Architecture](ARCHITECTURE.md) and the [FAQ](FAQ.md). Operational environment variables are listed in [Environment](ENVIRONMENT.md).

Rule definitions ship in the repository-root `schema_rules.yaml`; treat unexpected key renames as breaking changes for `verify`.

Worked examples without a live database live under [`examples/`](../examples/README.md).
