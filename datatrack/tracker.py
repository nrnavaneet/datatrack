import yaml
from pathlib import Path
from datetime import datetime

SNAPSHORT_DIR = Path(".datatrack/snapshots")

def get_mock_schema():
    """
    Simulate a table schema from a data warehouse.
    In real implementation, this would query the actual DB.
    """
    return {
        "dataset": "analytics",
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "name", "type": "STRING"},
                    {"name": "created_at", "type": "TIMESTAMP"}
                ]
            },
            {
                "name": "events",
                "columns": [
                    {"name": "event_id", "type": "STRING"},
                    {"name": "user_id", "type": "INTEGER"},
                    {"name": "timestamp", "type": "TIMESTAMP"}
                ]
            }
        ]
    }

def save_schema_snapshot(schema:dict):
    """
    Save the given scehma dict into a timestamped YAML file.
    """
    SNAPSHORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_file = SNAPSHORT_DIR / f"snapshot_{timestamp}.yaml"

    with open(snapshot_file, "w") as f:
        yaml.dump(schema,f)
    
    return snapshot_file
