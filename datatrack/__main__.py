"""Allow `python -m datatrack` as an alternative to the `datatrack` console script."""

from datatrack.cli import app

if __name__ == "__main__":
    app()
