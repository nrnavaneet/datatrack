"""Tests for snapshot history timestamp formatting."""
from datatrack.history import format_timestamp_from_filename


def test_format_timestamp_from_standard_snapshot_name():
    assert format_timestamp_from_filename("snapshot_20250708_174233.yaml") == "2025-07-08 17:42:33"


def test_format_timestamp_invalid_name_returns_placeholder():
    assert format_timestamp_from_filename("not_a_snapshot.yaml") == "Invalid format"
    assert format_timestamp_from_filename("") == "Invalid format"
