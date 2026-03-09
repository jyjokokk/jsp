from typing import Optional

import typer

from jsp.io import print_json, read_json

app = typer.Typer()


@app.command()
def main(
    file: Optional[str] = typer.Argument(None, help="Path to a JSON file. Reads from stdin if omitted."),
) -> None:
    """A CLI tool for viewing and manipulating JSON files."""
    try:
        data = read_json(file)
    except ValueError as e:
        raise typer.BadParameter(str(e)) from e

    print_json(data)


if __name__ == "__main__":
    app()
