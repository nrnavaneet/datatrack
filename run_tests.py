#!/usr/bin/env python3
"""
Test runner script for datatrack.
"""
import subprocess
import sys
from pathlib import Path


def run_tests():
    """Run all tests and report results."""
    print("🧪 Running Datatrack Test Suite")
    print("=" * 50)

    # Get project root
    project_root = Path(__file__).parent

    # Run all tests
    print("\n📦 Running All Tests...")
    test_result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"], cwd=project_root
    )

    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    print(f"All Tests: {'✅ PASSED' if test_result.returncode == 0 else '❌ FAILED'}")

    overall_success = test_result.returncode == 0
    print(
        f"Overall: {'✅ ALL TESTS PASSED' if overall_success else '❌ SOME TESTS FAILED'}"
    )

    return 0 if overall_success else 1


if __name__ == "__main__":
    sys.exit(run_tests())
