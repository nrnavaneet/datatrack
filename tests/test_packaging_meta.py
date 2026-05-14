"""Guardrails for packaging metadata in the repository root."""

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]


def test_pyproject_version_follows_semver_patch_pattern():
    text = _REPO_ROOT.joinpath("pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"(\d+\.\d+\.\d+)"', text, re.MULTILINE)
    assert match, "pyproject.toml must declare version as MAJOR.MINOR.PATCH in quotes"


def test_changelog_mentions_top_version():
    text = _REPO_ROOT.joinpath("CHANGELOG.md").read_text(encoding="utf-8")
    pyproject = _REPO_ROOT.joinpath("pyproject.toml").read_text(encoding="utf-8")
    ver_match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.MULTILINE)
    assert ver_match
    version = ver_match.group(1)
    assert f"## [{version}]" in text, "CHANGELOG should have a section header for the current pyproject version"
