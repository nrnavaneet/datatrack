# Example workflow

[← Examples index](README.md)

This is a **reference order** for new projects; adapt flags and engines to your environment.

1. **`datatrack init`** — create `.datatrack/` metadata.
2. **`datatrack connect <uri>`** — persist a database URI (one active connection at a time).
3. **`datatrack disconnect`** — clear the saved URI before rotating to another database (see [Usage §2b](../docs/USAGE.md#2b-clear-or-rotate-the-saved-uri)).
4. **`datatrack doctor`** — optional offline check that expected paths exist.
5. **`datatrack snapshot`** — write YAML under `.databases/exports/<db>/snapshots/`.
6. **`datatrack lint`** then **`datatrack verify`** — catch naming and policy issues.
7. **`datatrack diff`** — compare the two newest snapshots after schema changes.
8. **`datatrack export`** — emit JSON or YAML for auditing or downstream tools.
9. **`datatrack pipeline run`** — run the guarded sequence in CI when you want a single entrypoint.

If a step fails unexpectedly, jump to [Troubleshooting](../docs/TROUBLESHOOTING.md) with the exact command output (redacted). For a narrative breakdown of each stage, read [Pipeline](../docs/PIPELINE.md).

See `sample_snapshot_minimal.yaml` for the smallest snapshot shape used in tests and docs.

That fixture mirrors real tracker YAML closely enough for diff experiments; empty lists stand in for optional introspection sections the CLI would normally populate.
