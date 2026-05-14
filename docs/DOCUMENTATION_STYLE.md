# Documentation style

[← Documentation home](README.md)

## Voice

- Prefer **direct** instructions (“Run …”, “See …”) over passive voice.
- Use `datatrack` in monospace for the command; **Datatrack** for the product name in prose.

## Links

- Cross-link new pages from `docs/README.md` and, when user-facing, from the root `README.md` or `USAGE.md`.
- Use relative links inside `docs/` (e.g. `[Usage](USAGE.md)`) so the tree works offline and on GitHub.

## Changelog

- Each user-facing release line should start with a verb (**Add**, **Fix**, **Document**, …).
- Keep `pyproject.toml` `version` and the `## [x.y.z]` header in `CHANGELOG.md` in lockstep (CI tests enforce this).

## Code blocks

- Prefer fenced blocks with a language tag (`bash`, `yaml`, `text`) when it helps copy-paste.
