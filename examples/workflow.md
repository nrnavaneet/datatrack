# Example workflow

[← Examples index](README.md)

This is a **reference order** for new projects; adapt flags and engines to your environment.

1. **`datatrack init`** — create `.datatrack/` metadata.
2. **`datatrack connect <uri>`** — persist a database URI (one active connection at a time).
3. **`datatrack doctor`** — optional offline check that expected paths exist.
4. **`datatrack snapshot`** — write YAML under `.databases/exports/<db>/snapshots/`.
5. **`datatrack lint`** then **`datatrack verify`** — catch naming and policy issues.
6. **`datatrack diff`** — compare the two newest snapshots after schema changes.
7. **`datatrack export`** — emit JSON or YAML for auditing or downstream tools.
8. **`datatrack pipeline run`** — run the guarded sequence in CI when you want a single entrypoint.

See `sample_snapshot_minimal.yaml` for the smallest snapshot shape used in tests and docs.

That fixture mirrors real tracker YAML closely enough for diff experiments; empty lists stand in for optional introspection sections the CLI would normally populate.
