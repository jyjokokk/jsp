"""Functions for handling STDIN and STDOUT operations."""

import json
import sys

from rich.console import Console

from jsp.mock_data import EXAMPLE_DATA


def read_json(file_path: str | None = None) -> dict:
    """Read JSON from a file path or stdin if no path is given."""
    if file_path:
        with open(file_path) as f:
            return json.load(f)

    if not sys.stdin.isatty():
        return json.load(sys.stdin)

    raise ValueError("No input provided. Pass a file path or pipe JSON via stdin.")


console = Console()


def print_json(data: dict, pretty: bool = True):
    if pretty:
        console.print_json(json.dumps(data, indent=4))
    else:
        print(json.dumps(data))


def print_example_data():
    print_json(EXAMPLE_DATA)
    print("\n\n=== NON PRETTY JSON OUTPUT ===\n\n")
    print_json(EXAMPLE_DATA, pretty=False)
