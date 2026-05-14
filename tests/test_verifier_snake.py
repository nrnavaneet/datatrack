"""Unit tests for verifier naming helpers."""
import pytest

from datatrack.verifier import is_snake_case


@pytest.mark.parametrize(
    "name,expected",
    [
        ("users", True),
        ("user_orders", True),
        ("t1_extra", True),
        ("UserOrders", False),
        ("user-orders", False),
        ("", False),
    ],
)
def test_is_snake_case_matches_verifier_rules(name, expected):
    assert is_snake_case(name) is expected
