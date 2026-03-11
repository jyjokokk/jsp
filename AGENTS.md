# AGENTS.md

## Environment

This project uses **uv** as its package manager and task runner. All Python commands must be run through `uv run`:

```sh
uv run python -m pytest          # run tests
uv run jspprint <args>            # run the CLI
uv run python -m <module>        # run any Python module
```

To add dependencies, use `uv add <package>`. For dev dependencies, use `uv add --group dev <package>`.

## Testing

- Run `uv run python -m pytest` after any edit to files containing logic (source or test files).
- When adding new functions or features, write corresponding tests before considering the work complete.
- Test files mirror the source structure:
  - `src/jspprint/json_io.py` → `tests/test_json_io.py`
  - `src/jspprint/csv_io.py` → `tests/test_csv_io.py`
  - `src/jspprint/cli.py` → `tests/test_cli.py` (JSON CLI), `tests/test_csv_cli.py` (CSV CLI)
- CLI tests use `typer.testing.CliRunner`.
