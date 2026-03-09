from typing import Optional

import typer

from jsp.io import print_json, read_json

app = typer.Typer()


@app.command()
def main(
    file: Optional[str] = typer.Argument(
        None, help="Path to a JSON file. Reads from stdin if omitted."
    ),
    compact: bool = typer.Option(
        False, "--compact", "-c", help="Output compact JSON without formatting."
    ),
) -> None:
    """A CLI tool for viewing and manipulating JSON files."""
    try:
        data = read_json(file)
    except ValueError as e:
        raise typer.BadParameter(str(e)) from e

    print_json(data, pretty=not compact)


if __name__ == "__main__":
    app()
