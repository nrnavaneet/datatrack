"""
Benchmark the datatrack snapshot logic on three SQLite databases of different sizes.
Creates sample databases, runs timed snapshots, and prints a summary table with percentage improvements over baseline.

Author: nrnavaneet
"""

import os
import sqlite3
import time
from datatrack.tracker import snapshot
from rich.console import Console
from rich.table import Table

os.makedirs(".databases", exist_ok=True)

def create_db(path, n_tables, n_rows=10):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    for i in range(n_tables):
        table = f"table_{i}"
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY, value TEXT)")
        cur.executemany(f"INSERT INTO {table} (value) VALUES (?)", [(f"row_{j}",) for j in range(n_rows)])
    conn.commit()
    conn.close()

create_db(".databases/small.db", 10)
create_db(".databases/medium.db", 100)
create_db(".databases/large.db", 250)

def run_benchmark(db_uri, label, console):
    console.rule(f"Benchmarking {label}")
    console.print(f"[bold cyan]Connecting:[/bold cyan] {db_uri}")
    from datatrack.connect import save_connection, remove_connection
    save_connection(db_uri)
    start = time.time()
    snapshot(source=db_uri, include_data=True, max_rows=10)
    elapsed = time.time() - start
    console.print(f"[green]{label} snapshot completed in {elapsed:.2f} seconds[/green]")
    remove_connection()
    return elapsed


console = Console()
results = []
results.append(("Small (10 tables)", run_benchmark("sqlite:///.databases/small.db", "Small (10 tables)", console)))
results.append(("Medium (100 tables)", run_benchmark("sqlite:///.databases/medium.db", "Medium (100 tables)", console)))
results.append(("Large (250 tables)", run_benchmark("sqlite:///.databases/large.db", "Large (250 tables)", console)))


baseline = {
    "Small (10 tables)": 0.10,
    "Medium (100 tables)": 0.75,
    "Large (250 tables)": 2.80
}


table = Table(title="Benchmark Results Summary", show_lines=True)
table.add_column("Database Size", justify="left", style="bold")
table.add_column("Snapshot Time (s)", justify="right")
table.add_column("Improvement over Baseline", justify="right")
for label, timing in results:
    base = baseline[label]
    percent = ((base - timing) / base) * 100
    table.add_row(label, f"{timing:.2f}", f"{percent:.1f}%")
console.print(table)
