# Datatrack documentation

Start here and jump to the guide you need.

| Document | What you will find |
|----------|--------------------|
| [CODEOWNERS](https://github.com/nrnavaneet/datatrack/blob/main/.github/CODEOWNERS) | Default review routing on GitHub |
| [Pull request template](https://github.com/nrnavaneet/datatrack/blob/main/.github/PULL_REQUEST_TEMPLATE.md) | Reviewer checklist for risk notes, tests, and changelog alignment |
| [Issue & PR templates](https://github.com/nrnavaneet/datatrack/tree/main/.github) | Bug reports, feature requests, pull request checklist |
| [Security](../SECURITY.md) | How to report vulnerabilities responsibly |
| [Benchmark harness](../benchmark_tests/README.md) | Manual SQLite timing script (not executed in CI) |
| [Examples index](../examples/README.md) | Minimal snapshot fixture, workflow, and links to troubleshooting or performance follow-ups |
| [Glossary](GLOSSARY.md) | Short definitions of snapshot, lint, verify, pipeline, doctor |
| [FAQ](FAQ.md) | Common questions about storage layout, lint vs verify, and testing |
| [Performance](PERFORMANCE.md) | Benchmarks, parallelism, when to expect wins |
| [Developing](DEVELOPING.md) | Local venv, editable install, pytest, pre-commit |
| [Dependabot config](https://github.com/nrnavaneet/datatrack/blob/main/.github/dependabot.yml) | Weekly PRs for Actions and pip dependencies |
| [EditorConfig](../.editorconfig) | Shared indentation and newline defaults for editors |
| [Makefile](../Makefile) | `make test` / `make lint` / `make clean` shortcuts from the repo root |
| [Support](SUPPORT.md) | Where to ask questions and what to include in bug reports |
| [Testing](TESTING.md) | Where tests live, goals, and how to run pytest |
| [Python modules](MODULES.md) | Which packages are intended for import vs CLI-only |
| [Architecture](ARCHITECTURE.md) | Modules, snapshot lifecycle, pipeline, extension points |
| [Doctor](USAGE.md#0-doctor-sanity-check-layout) | `datatrack doctor` — quick layout checks without SQL |
| [Installation](INSTALLATION.md) | PyPI vs editable install, Python version, first commands |
| [Usage](USAGE.md) | Every CLI command with examples |
| [Environment](ENVIRONMENT.md) | Env vars and path layout notes |
| [Troubleshooting](TROUBLESHOOTING.md) | Common failures and fixes |
| [Releasing](RELEASING.md) | Maintainer checklist for PyPI versions, tags, and Twine uploads |
| [CI](CI.md) | What GitHub Actions runs, including weekly scheduled builds |
| [Code of Conduct](contribute/CODE_OF_CONDUCT.md) | Community expectations and enforcement contact |
| [Contributing](contribute/CONTRIBUTING.md) | Branch workflow, tests, pre-commit |

The main [README](../README.md) stays the marketing and architecture overview; these files are the **operational** reference. The PyPI readme mirrors a subset of this index for package-page readers.
