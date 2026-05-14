# Installation Guide for Datatrack

Index of all guides: [Documentation home](README.md).

Datatrack is a lightweight CLI tool for tracking schema changes in databases. You can install it in two ways depending on your use case. **Python 3.7 or newer** is required (see `requires-python` in `pyproject.toml`). Locale-related environment variables are described in [Environment](ENVIRONMENT.md) if Rich output looks broken over SSH.


## Option 1: Install from PyPI (Recommended for Users)

Use this if you just want to use `datatrack` as a command-line tool in your projects.

```bash
pip install datatrack-core
```
## Initialize a Datatrack Project

```bash
datatrack init
```
Creates a `.datatrack/` folder with configuration.


Once installed, you can start using the `datatrack` CLI directly.

Rotating the active database always starts with `datatrack disconnect` before a new `connect` (details in [Usage](USAGE.md#2b-clear-or-rotate-the-saved-uri)).

For a guided command order, see [`examples/workflow.md`](https://github.com/nrnavaneet/datatrack/blob/main/examples/workflow.md) in the repository.

## Option 2: Install from GitHub (For Development & Contribution)

Use this method if you intend to modify or contribute to the project.

```bash
git clone https://github.com/nrnavaneet/datatrack.git
cd datatrack
pip install -r requirements.txt
pip install -e .
```

`requirements.txt` stays aligned with `pyproject.toml` so GitHub Actions can cache wheels predictably.

See [Developing](DEVELOPING.md) for venv tips, pytest, and pre-commit.

The [`tests/test_paths.py`](https://github.com/nrnavaneet/datatrack/blob/main/tests/test_paths.py) module encodes the expected `.databases/exports/` layout if you are wiring integrations.

This sets up a local editable environment where you can test changes to the source code.

## Helpful Commands

Datatrack comes with built-in help and guidance for every command. Use this to quickly learn syntax and options:
```bash
datatrack --help
python3 -m datatrack --help
or
datatrack -h
```

For any issues, refer to [Troubleshooting](TROUBLESHOOTING.md), [Architecture](ARCHITECTURE.md), the [FAQ](FAQ.md), and the [CI](CI.md) overview, or open a ticket on [GitHub issues](https://github.com/nrnavaneet/datatrack/issues).
