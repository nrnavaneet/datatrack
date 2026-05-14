# Privacy

[← Documentation home](README.md)

Datatrack is a **local command-line tool**. It does not ship telemetry, crash reporting, or background network calls as part of normal CLI use.

## What stays on your machine

- **Connection strings** you pass to `datatrack connect` or store under `.datatrack/` remain on disk unless you copy them elsewhere.
- **Snapshot YAML**, exports, and diff outputs are ordinary files you control; treat them like any other schema documentation that may describe internal systems.

## Third-party services you may use alongside Datatrack

- **PyPI** hosts the published wheel and sdist; installing from PyPI is subject to [PyPI’s policies](https://pypi.org/policies/privacy-policy/) and your network path to them.
- **GitHub** hosts the source repository, issues, and Actions logs; see [GitHub’s privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement) if you interact there.

This document is informational, not legal advice. For vulnerability reporting, follow [SECURITY.md](../SECURITY.md).
