"""Ensure ``datatrack.paths`` public API matches ``__all__``."""

import datatrack.paths as paths


def test_paths_all_exports_existing_names():
    for name in paths.__all__:
        assert hasattr(paths, name), f"missing export: {name}"


def test_paths_all_includes_core_paths():
    assert "CONFIG_DIR" in paths.__all__
    assert "snapshot_dir" in paths.__all__
    assert "export_dir" in paths.__all__
