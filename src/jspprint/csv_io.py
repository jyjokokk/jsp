"""Functions for reading and displaying CSV data."""

import csv

from rich.console import Console
from rich.table import Table

console = Console()


def read_csv(file_path: str, delimiter: str = ",") -> list[list[str]]:
    """Read CSV from a file path."""
    try:
        with open(file_path, newline="") as f:
            return list(csv.reader(f, delimiter=delimiter))
    except csv.Error as e:
        raise ValueError(f"Invalid CSV from {file_path}: {e}") from e


def print_csv(rows: list[list[str]], header: bool = True) -> None:
    """Print CSV data as a rich table with columns."""
    if not rows:
        return

    table = Table(show_header=header)

    if header:
        for col in rows[0]:
            table.add_column(col)
        data_rows = rows[1:]
    else:
        for i in range(len(rows[0])):
            table.add_column(f"Col {i + 1}")
        data_rows = rows

    for row in data_rows:
        table.add_row(*row)

    console.print(table)
