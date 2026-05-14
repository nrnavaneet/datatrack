# Support

[← Documentation home](README.md)

## Before you open an issue

1. Skim the [FAQ](FAQ.md) and [Troubleshooting](TROUBLESHOOTING.md) pages — many `connect`, `snapshot`, and path questions are answered there.
2. Run `datatrack doctor` for offline layout checks.
3. Confirm your Python version meets `requires-python` in `pyproject.toml`.

## Where to ask

- **Bugs and feature requests** — [GitHub Issues](https://github.com/nrnavaneet/datatrack/issues) using the templates.
- **Security-sensitive reports** — follow [SECURITY.md](../SECURITY.md); do not file public issues with live credentials.

## What to include

- Datatrack version (`pip show datatrack-core` or commit SHA for git installs).
- OS and Python version.
- Redacted connection URI shape (omit passwords).
- Minimal CLI output showing the failure.

Maintainers monitor issues asynchronously; Dependabot and scheduled CI noise is normal on busy weeks.
