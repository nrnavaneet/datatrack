# Rules directory

Today, **lint** and **verify** read the shared **`schema_rules.yaml`** file at the **repository root** (next to `pyproject.toml`). The Python entry points are `datatrack.linter.load_lint_rules()` and `datatrack.verifier.load_rules()`.

This package subdirectory is **reserved** for future work such as pluggable rule modules or packaged presets. Nothing here is imported yet; changing only files under `datatrack/rules/` will not affect the CLI until those hooks are wired up.

When adding a new rule class later, keep YAML keys in sync with the tables documented in the main **Usage** guide so existing projects do not break.
