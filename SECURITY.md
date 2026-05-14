# Security

If you believe you have found a security vulnerability in **Datatrack**, please **do not** open a public GitHub issue with exploit details.

Instead, contact the maintainer privately (see the email on the [PyPI package page](https://pypi.org/project/datatrack-core/) or the GitHub profile linked from the repository README). Include:

- A short description of the impact
- Steps to reproduce (minimal)
- Affected versions or commit SHAs if known

This project is a **developer CLI** for schema inspection; it is not a networked service. Most risk comes from **running untrusted connection strings** or **parsing untrusted YAML** on the same machine as production credentials—treat both like any other local tooling.

Dependency updates for GitHub Actions and `pip` manifests are automated via **Dependabot** (see `.github/dependabot.yml`); review those PRs like any other change.
