"""
Automated Schema Validation and Analysis Pipeline

This module orchestrates a comprehensive database schema validation workflow,
automating the entire process from snapshot creation to final analysis and reporting.
It provides a streamlined, production-ready pipeline for database schema management.

Pipeline Workflow:
1. Schema Snapshot: Capture current database state with full metadata
2. Quality Linting: Analyze design patterns, naming conventions, and best practices
3. Rule Verification: Enforce organizational schema standards and constraints
4. Change Analysis: Compare current state with previous snapshots for differences
5. Export Generation: Create comprehensive reports and data exports

Key Features:
- Fully automated end-to-end schema validation
- Configurable pipeline stages with selective execution
- Comprehensive error handling and recovery
- Detailed logging and progress tracking
- Export artifacts for CI/CD integration
- Interactive and batch execution modes

Output Artifacts:
- Schema snapshots (YAML format)
- Linting reports (JSON format)
- Verification results (detailed analysis)
- Diff reports (change analysis)
- Export files for external tool integration

Integration Points:
- CI/CD pipeline compatibility
- Custom rule configuration support
- External tool API integration
- Automated reporting and notifications

Author: Navaneet
"""

import typer

from datatrack.connect import get_connected_db_name, get_saved_connection
from datatrack.diff import diff_schemas, load_snapshots
from datatrack.exporter import export_diff, export_snapshot
from datatrack.linter import lint_schema
from datatrack.linter import load_latest_snapshot as load_lint_snapshot
from datatrack.tracker import snapshot
from datatrack.verifier import load_latest_snapshot as load_ver_snapshot
from datatrack.verifier import load_rules, verify_schema

app = typer.Typer()

# Step result summary
step_summary = {}

# Export directory (hardcoded in current architecture)
EXPORT_PATH = ".databases/exports/"


def prompt_to_continue(step_name: str) -> bool:
    return typer.confirm(
        f"[{step_name}] failed. Do you want to continue?", default=False
    )


def print_summary(summary: dict):
    """Display formatted pipeline execution summary."""
    print("\n┏" + "━" * 46 + "┓")
    print("┃{:^46}┃".format("DataTrack: Schema Workflow"))
    print("┣" + "━" * 46 + "┫")
    for step, result in summary.items():
        print(f"┃ {step:<20} ── {result:<21}┃")
    print("┗" + "━" * 46 + "┛")


def print_artifact_paths():
    """Display locations of generated artifacts and output files."""
    print("\nSaved artifacts:")
    print(f"- Snapshot directory : {EXPORT_PATH}{get_connected_db_name()}/snapshots/")
    print(
        f"- Diff output        : {EXPORT_PATH}{get_connected_db_name()}/latest_diff.json"
    )
    print(f"- Exported files     : {EXPORT_PATH} (e.g., snapshot.json, diff.json)")


@app.command("run")
def run_pipeline(
    verbose: bool = typer.Option(True, help="Enable detailed output"),
    strict: bool = typer.Option(False, help="Fail pipeline on lint warnings"),
):
    # 1. Snapshot
    print("\n[1] Snapshotting schema...")
    source = get_saved_connection()
    if not source:
        step_summary["1. Snapshot"] = "✖ No DB connection"
        print_summary(step_summary)
        raise typer.Exit(code=1)

    try:
        snapshot(source)
        step_summary["1. Snapshot"] = "✔ Success"
    except Exception as e:
        step_summary["1. Snapshot"] = "✖ Error"
        print(f"Snapshot failed: {e}")
        print_summary(step_summary)
        raise typer.Exit(code=1) from e

    # 2. Linting
    print("\n[2] Linting schema...")
    try:
        schema = load_lint_snapshot()
        lint_warnings = lint_schema(schema)
        if lint_warnings:
            for w in lint_warnings:
                print(f"  - {w}")
            if strict:
                step_summary["2. Linting"] = f"✖ {len(lint_warnings)} Warnings"
                print_summary(step_summary)
                raise typer.Exit(code=1)
            else:
                step_summary["2. Linting"] = f"⚠ {len(lint_warnings)} Warnings"
                if not prompt_to_continue("Linting"):
                    print_summary(step_summary)
                    raise typer.Exit(code=1)
        else:
            step_summary["2. Linting"] = "✔ Clean"
    except Exception as e:
        step_summary["2. Linting"] = "✖ Error"
        print(f"Linting failed: {e}")
        print_summary(step_summary)
        if not prompt_to_continue("Linting"):
            raise typer.Exit(code=1) from e

    # 3. Verification
    print("\n[3] Verifying schema...")
    try:
        schema = load_ver_snapshot()
        rules = load_rules()
        violations = verify_schema(schema, rules)
        if violations:
            for v in violations:
                print(f"  - {v}")
            step_summary["3. Verify"] = f"✖ {len(violations)} Violations"
            if not prompt_to_continue("Verification"):
                print_summary(step_summary)
                raise typer.Exit(code=1)
        else:
            step_summary["3. Verify"] = "✔ OK"
    except Exception as e:
        step_summary["3. Verify"] = "✖ Error"
        print(f"Verification failed: {e}")
        print_summary(step_summary)
        if not prompt_to_continue("Verification"):
            raise typer.Exit(code=1) from e

    # 4. Diff
    print("\n[4] Computing diff...")
    try:
        old, new = load_snapshots()
        diff_schemas(old, new)
        step_summary["4. Diff"] = "✔ Applied"
    except Exception as e:
        step_summary["4. Diff"] = "✖ Skipped"
        print(f"Diff error: {e}")
        if not prompt_to_continue("Diff"):
            print_summary(step_summary)
            raise typer.Exit(code=1) from e

    # 5. Export
    print("\n[5] Exporting...")
    try:
        export_snapshot(fmt="json")
        export_diff(fmt="json")
        step_summary["5. Export"] = "✔ Saved"
    except Exception as e:
        step_summary["5. Export"] = "✖ Failed"
        print(f"Export error: {e}")
        print_summary(step_summary)
        raise typer.Exit(code=1) from e

    # Final UI + Paths
    print_summary(step_summary)
    print_artifact_paths()
