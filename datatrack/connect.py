from pathlib import Path

import yaml

CONFIG_DIR = ".datatrack"
DB_LINK_FILE = Path(CONFIG_DIR) / "db_link.yaml"


def save_connection(link: str):
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)
    with open(DB_LINK_FILE, "w") as f:
        yaml.dump({"link": link}, f)
    print(f"Connected to database: {link}")


def get_saved_connection():
    if DB_LINK_FILE.exists():
        with open(DB_LINK_FILE) as f:
            data = yaml.safe_load(f)
            return data.get("link")
    return None


def remove_connection():
    if DB_LINK_FILE.exists():
        DB_LINK_FILE.unlink()
        print("Disconnected from database and removed stored link.")
    else:
        print("No active connection found.")
