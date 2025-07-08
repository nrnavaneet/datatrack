# Installation Guide for Datatrack

Datatrack is a lightweight CLI tool for tracking schema changes in databases. You can install it in two ways depending on your use case.


## Option 1: Install from PyPI (Recommended for Users)

Use this if you just want to use `datatrack` as a command-line tool in your projects.

```bash
pip install dbtracker
```

Once installed, you can start using the `datatrack` CLI directly.

## Option 2: Install from GitHub (For Development & Contribution)

Use this method if you intend to modify or contribute to the project.

```bash
git clone https://github.com/nrnavaneet/datatrack.git
cd datatrack
pip install -r requirements.txt
pip install -e .
```

This sets up a local editable environment where you can test changes to the source code.

For any issues, refer to [https://github.com/nrnavaneet/datatrack/issues](https://github.com/nrnavaneet/datatrack/issues).
