import yaml
import os
import json
from pathlib import Path
from datatrack.diff import diff_schemas

def load_latest_snapshots(n=2):
    snap_dir = Path(".datatrack/snapshots")
    snapshots = sorted(snap_dir.glob("*.yaml"), reverse=True)
    if len(snapshots) < n:
        raise ValueError(f"Not enough snapshots found to compare. Found {len(snapshots)}, need {n}.")
    return [yaml.safe_load(open(s)) for s in snapshots[:n]]

def export_snapshot(output_path, fmt):
    latest = load_latest_snapshots(n=1)[0]
    _write_to_file(latest, output_path, fmt)

def export_diff(output_path, fmt):
    snap_new, snap_old = load_latest_snapshots(n=2)
    diff = _generate_diff(snap_old, snap_new)
    _write_to_file(diff, output_path, fmt)

def _generate_diff(old, new):
    diff_result={
        "added_tables": [],
        "removed_tables": [],
        "changed_tables": {}
    }

    old_tables = {t["name"]: t for t in old['tables']}
    new_tables = {t["name"]: t for t in new['tables']}

    added= set(new_tables.keys()) - set(old_tables.keys())
    removed = set(old_tables.keys()) - set(new_tables.keys())
    common = set(new_tables.keys()) & set(old_tables.keys())

    for t in added:
        diff_result["added_tables"].append(t)
    for t in removed:
        diff_result["removed_tables"].append(t) 

    for t in common:
        old_cols = {c["name"]: c['type'] for c in old_tables[t]["columns"]}
        new_cols = {c["name"]: c['type'] for c in new_tables[t]["columns"]}

        added_cols = set(new_cols.keys()) - set(old_cols.keys())
        removed_cols = set(old_cols.keys()) - set(new_cols.keys())
        common_cols = {
            c: {"from": old_cols[c], "to": new_cols[c]}
            for c in set(old_cols) & set(new_cols)
            if old_cols[c] != new_cols[c]
        }

        return diff_result
    

def _write_to_file(data, path, fmt):
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True) 

    if fmt not in {"json", "yaml"}:
        raise ValueError(f"Unsupported format: {fmt}")

    with open(output_path, "w") as f:
        if fmt == "json":
            json.dump(data, f, indent=2)
        elif fmt == "yaml":
            yaml.dump(data, f)
