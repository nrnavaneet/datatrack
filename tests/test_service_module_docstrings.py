"""Meta checks for lightweight service modules."""

import datatrack.exporter as exporter
import datatrack.history as history
import datatrack.linter as linter
import datatrack.test_connection as test_connection


def test_service_modules_expose_docstrings():
    for mod in (exporter, history, linter, test_connection):
        assert mod.__doc__ and mod.__doc__.strip(), f"{mod.__name__} should define a module docstring"
