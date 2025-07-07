import os
import yaml
import typer
from pathlib import Path
from  datatrack import tracker
from datatrack import diff as diff_module
from datatrack import verifier

app = typer.Typer(help="📊 Datatrack: Schema tracking CLI")

CONFIG_DIR = ".datatrack"
CONFIG_FILE = "config.yaml"


@app.command()
def init():
    """
    Initialize Datatrack in the current directory.
    """
    config_path = Path(CONFIG_DIR)
    if config_path.exists():
        typer.echo("✅ Datatrack is already initialized.")
        raise typer.Exit()

    # Create .datatrack directory
    config_path.mkdir(parents=True, exist_ok=True)

    # Default config contents
    default_config = {
        "project_name": "my-datatrack-project",
        "created_by": os.getenv("USER") or "unknown",
        "version": "0.1",
        "sources": []
    }

    with open(config_path / CONFIG_FILE, "w") as f:
        yaml.dump(default_config, f)

    typer.echo("🎉 Datatrack initialized in .datatrack/")

@app.command()
def snapshot():
    """
    Capture the current schema atate and save a snapshot.
    """
    typer.echo("📸 Capturing schema snapshot...")

    schema= tracker.get_mock_schema()
    file_path = tracker.save_schema_snapshot(schema)

    typer.echo(f"Snapshot saved to {file_path}")


@app.command()
def diff():
    """
    Compare latest two snapshots and show schema differences.
    """
    try:
        old, new = diff_module.load_snapshots()
        diff_module.diff_schemas(old, new)
    except Exception as e:
        typer.secho(f"{str(e)}", fg=typer.colors.RED)

from datatrack import verifier

@app.command()
def verify():
    """
    Check schema against configured rules (e.g. snake_case, reserved words).
    """
    typer.echo("\n🔍 Verifying schema...\n")

    try:
        schema = verifier.load_latest_snapshot()
        rules = verifier.load_rules() 
        violations = verifier.verify_schema(schema, rules) 

        if not violations:
            typer.secho("All schema rules passed!", fg=typer.colors.GREEN)
        else:
            for v in violations:
                typer.secho(v, fg=typer.colors.RED)
            raise typer.Exit(code=1)

    except Exception as e:
        typer.secho(f"Error during verification: {str(e)}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()