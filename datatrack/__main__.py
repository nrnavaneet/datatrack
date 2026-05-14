"""Allow `python -m datatrack` as an alternative to the `datatrack` console script.

Useful in CI sandboxes where console scripts are not on ``PATH`` but the package is importable.
"""

from datatrack.cli import app

if __name__ == "__main__":
    app()
