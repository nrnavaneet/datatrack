# Environment variables

[← Documentation home](README.md)

Datatrack reads a few standard environment variables when you run the CLI.

| Variable | Used by | Notes |
|----------|---------|--------|
| `USER` | `datatrack init` | Fills `created_by` in `.datatrack/config.yaml` when set; otherwise the literal `unknown` is stored. |
| `HOME` | shell / OS | Only relevant if you put SQLite databases or config under your home directory in connection URIs. |
| `LANG` / `LC_ALL` | Typer / Rich output | Optional; only affects localised help text and table rendering in some terminals. |

There are **no** secret `DATATRACK_*` variables today: the database URI is stored in `.datatrack/db_link.yaml` after you run `datatrack connect`.

Relative paths for exports and snapshots are defined in **`datatrack.paths`** (`.databases/exports/`, etc.); override nothing unless you fork the package.

For CI, prefer a disposable SQLite file and a URI such as `sqlite:////tmp/datatrack_ci.db` so jobs do not depend on network databases.

Snapshot duration is dominated by database latency and schema size; see [Performance](PERFORMANCE.md) for benchmark-oriented guidance (not additional environment variables).
