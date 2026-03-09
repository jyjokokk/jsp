import typer


app = typer.Typer()


@app.command()
def main() -> None:
    """A CLI tool for viewing and manipulating JSON files."""
    print("Hello from jsp!")


if __name__ == "__main__":
    app()
