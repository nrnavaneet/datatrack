# Documentation style

[← Documentation home](README.md)

## Voice

- Prefer **direct** instructions (“Run …”, “See …”) over passive voice.
- Use `datatrack` in monospace for the command; **Datatrack** for the product name in prose.

## Links

- Cross-link new pages from `docs/README.md` and, when user-facing, from the root `README.md` or `USAGE.md`.
- Use relative links inside `docs/` (e.g. `[Usage](USAGE.md)`) so the tree works offline and on GitHub.
- Keep **SECURITY** and **Privacy** pages short and actionable; point deep technical detail at the modules or CLI sections it belongs with.

## Changelog

- Each user-facing release line should start with a verb (**Add**, **Fix**, **Document**, …).
- Keep `pyproject.toml` `version` and the `## [x.y.z]` header in `CHANGELOG.md` in lockstep (CI tests enforce this).

The repository `LICENSE` file includes an **SPDX-License-Identifier** line; do not drop it when editing copyright years.

## Code blocks

- Prefer fenced blocks with a language tag (`bash`, `yaml`, `text`) when it helps copy-paste.

Python modules that are part of the supported import surface should start with a short **module docstring** summarising side effects (see `datatrack.connect`, `datatrack.diff`, `datatrack.tracker`, `datatrack.exporter`, `datatrack.history`, `datatrack.linter`, and `datatrack.test_connection`).
