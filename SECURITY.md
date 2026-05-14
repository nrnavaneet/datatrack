# Security

If you believe you have found a security vulnerability in **Datatrack**, please **do not** open a public GitHub issue with exploit details.

Instead, contact the maintainer privately (see the email on the [PyPI package page](https://pypi.org/project/datatrack-core/) or the GitHub profile linked from the repository README). Include:

- A short description of the impact
- Steps to reproduce (minimal)
- Affected versions or commit SHAs if known

This project is a **developer CLI** for schema inspection; it is not a networked service. Most risk comes from **running untrusted connection strings** or **parsing untrusted YAML** on the same machine as production credentials—treat both like any other local tooling.

Shell history, terminal scrollback, and CI logs can capture `datatrack connect` arguments; prefer environment-provided secrets or masked URIs in automation.

Dependency updates for GitHub Actions and `pip` manifests are automated via **Dependabot** (see `.github/dependabot.yml`); review those PRs like any other change.

Sensitive PRs should still use private disclosure per the top of this file even if [CODEOWNERS](.github/CODEOWNERS) routes reviews automatically.

The **CI workflow** requests read-only `contents` permission for the default token, reducing blast radius if a third-party Action were compromised.

Scheduled CI on `main` helps catch upstream breakage when dependencies move between PRs; treat failing scheduled runs with the same urgency as `push` failures.

Coordinated disclosure for security releases should follow both this document and [Releasing](RELEASING.md) so PyPI metadata and changelog entries stay aligned.

For a short note on what Datatrack keeps local versus what PyPI/GitHub may see, read [Privacy](docs/PRIVACY.md) in this repository.
