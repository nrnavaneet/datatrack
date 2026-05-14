# Pipeline command

[← Documentation home](README.md)

`datatrack pipeline run` executes the main quality steps in one invocation. Exact ordering and flags live in `datatrack/pipeline.py` and [Usage](USAGE.md#9-run-the-full-pipeline).

## Typical sequence

1. **Lint** — naming and structural heuristics on the latest snapshot YAML.
2. **Snapshot** — refresh schema metadata from the connected database.
3. **Verify** — apply `schema_rules.yaml` policies.
4. **Diff** — compare the two newest snapshots.
5. **Export** — write JSON or YAML artefacts for auditing or downstream tools.

## When to use it

- **Local** — quick “full sweep” before pushing schema-sensitive changes.
- **CI** — single entrypoint when you already ran `connect` in the job (or rely on tests that patch paths).

## When not to use it

- **Dry layout checks** — use `datatrack doctor` instead; the pipeline expects a configured project and (for snapshot steps) a working database URI.

Failures surface as a Rich table with per-step status; copy that table (redacted) into bug reports as described in [Support](SUPPORT.md).
