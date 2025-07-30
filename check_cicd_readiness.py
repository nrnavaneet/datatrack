#!/usr/bin/env python3
"""
DataTrack CI/CD Readiness Check
Validates that the project is ready for GitHub CI/CD automation
"""

import os
import subprocess
import sys
from pathlib import Path

import yaml


def check_file_exists(filepath, description):
    """Check if a required file exists."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} missing: {filepath}")
        return False


def check_yaml_valid(filepath):
    """Check if YAML file is valid."""
    try:
        with open(filepath) as f:
            yaml.safe_load(f)
        print(f"✅ Valid YAML: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Invalid YAML: {filepath} - {e}")
        return False


def check_python_import(module_name):
    """Check if Python module can be imported."""
    try:
        __import__(module_name)
        print(f"✅ Python import: {module_name}")
        return True
    except ImportError as e:
        print(f"❌ Python import failed: {module_name} - {e}")
        return False


def check_command_available(command):
    """Check if command is available in PATH."""
    try:
        # Try both python3 and python
        if command == "python":
            for cmd in ["python3", "python"]:
                try:
                    subprocess.run([cmd, "--version"], capture_output=True, check=True)
                    print(f"✅ Command available: {cmd}")
                    return True
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            print("❌ Command not available: python/python3")
            return False
        elif command == "pip":
            # Try pip3, pip, and python -m pip
            for cmd in [
                ["pip3", "--version"],
                ["pip", "--version"],
                ["python3", "-m", "pip", "--version"],
            ]:
                try:
                    subprocess.run(cmd, capture_output=True, check=True)
                    print(f"✅ Command available: {' '.join(cmd[:2])}")
                    return True
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            print("❌ Command not available: pip")
            return False
        else:
            subprocess.run([command, "--version"], capture_output=True, check=True)
            print(f"✅ Command available: {command}")
            return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"❌ Command not available: {command}")
        return False


def run_tests():
    """Run the test suite."""
    try:
        # Try python3 first, then python
        for python_cmd in ["python3", "python"]:
            try:
                result = subprocess.run(
                    [python_cmd, "-m", "pytest", "tests/", "-v", "--tb=short"],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    passed = result.stdout.count(" PASSED")
                    skipped = result.stdout.count(" SKIPPED")
                    print(f"✅ Tests: {passed} passed, {skipped} skipped")
                    return True
                else:
                    print(f"❌ Tests failed: {result.stderr}")
                    return False
            except FileNotFoundError:
                continue
        print("❌ No python executable found")
        return False
    except Exception as e:
        print(f"❌ Test execution error: {e}")
        return False


def check_package_build():
    """Test package building."""
    try:
        # Clean previous builds
        subprocess.run(["rm", "-rf", "dist/", "build/"], capture_output=True)

        # Try python3 first, then python
        for python_cmd in ["python3", "python"]:
            try:
                result = subprocess.run(
                    [python_cmd, "-m", "build"], capture_output=True, text=True
                )
                if result.returncode == 0:
                    # Check if files exist
                    dist_files = list(Path("dist").glob("*"))
                    if len(dist_files) >= 2:  # wheel and sdist
                        print(f"✅ Package build: {len(dist_files)} artifacts created")
                        return True
                    else:
                        print(
                            f"❌ Package build: insufficient artifacts ({len(dist_files)})"
                        )
                        return False
                else:
                    print(f"❌ Package build failed: {result.stderr}")
                    return False
            except FileNotFoundError:
                continue
        print("❌ No python executable found for building")
        return False
    except Exception as e:
        print(f"❌ Package build error: {e}")
        return False


def main():
    """Run all checks."""
    print("🔍 DataTrack CI/CD Readiness Check")
    print("=" * 50)

    checks = []

    # File existence checks
    checks.append(check_file_exists(".github/workflows/ci-cd.yml", "CI/CD Workflow"))
    checks.append(check_file_exists(".github/workflows/pr-checks.yml", "PR Workflow"))
    checks.append(check_file_exists("pyproject.toml", "PyProject Config"))
    checks.append(check_file_exists("tests/", "Tests Directory"))
    checks.append(check_file_exists("datatrack/", "Package Directory"))

    # YAML validation
    if os.path.exists(".github/workflows/ci-cd.yml"):
        checks.append(check_yaml_valid(".github/workflows/ci-cd.yml"))
    if os.path.exists(".github/workflows/pr-checks.yml"):
        checks.append(check_yaml_valid(".github/workflows/pr-checks.yml"))

    # Python dependencies
    checks.append(check_python_import("datatrack"))
    checks.append(check_python_import("pytest"))
    checks.append(check_python_import("yaml"))

    # Required commands
    checks.append(check_command_available("python"))
    checks.append(check_command_available("pip"))

    # Test suite
    checks.append(run_tests())

    # Package building
    checks.append(check_package_build())

    # Summary
    print("\n" + "=" * 50)
    passed_checks = sum(checks)
    total_checks = len(checks)

    if passed_checks == total_checks:
        print(f"🎉 ALL CHECKS PASSED ({passed_checks}/{total_checks})")
        print("\n✅ Your project is ready for GitHub CI/CD!")
        print("\nNext steps:")
        print("1. Set up PyPI API tokens in GitHub secrets")
        print("2. Push to main branch to trigger CI/CD")
        print("3. Create a version tag (e.g., v1.1.3) for release")
        return 0
    else:
        print(f"❌ SOME CHECKS FAILED ({passed_checks}/{total_checks})")
        print("\n🔧 Please fix the failing checks before proceeding.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
