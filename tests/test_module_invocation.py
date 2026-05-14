"""Smoke test for invoking the package as a module."""

import subprocess
import sys


def test_python_m_datatrack_help():
    proc = subprocess.run(
        [sys.executable, "-m", "datatrack", "--help"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0
    out = (proc.stdout or "") + (proc.stderr or "")
    assert len(out.strip()) > 0
