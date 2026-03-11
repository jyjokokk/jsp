# jspprint

A CLI tool for viewing and manipulating JSON files. Pretty-prints JSON with syntax highlighting by default, supports filtering by keys, and allows in-memory modifications for easy piping — without altering the original file.

## Features

- **Pretty-print JSON** with syntax highlighting (default behavior)
- **Filter by key(s)** to extract and display specific parts of a JSON structure
- **In-memory modifications** — add, update, replace, or delete values in the output without touching the source file
- **Merge from file or stdin** — set a key's value to the contents of another JSON file, or pipe JSON in via stdin
- **Stdin as input** — read JSON from stdin instead of a file (`cat data.json | jspprint`)
- **Pipe-friendly** — output can be piped to other commands or redirected to files

## Planned

- CSV, XML, and YAML support

## Tech Stack

- **Python**
- **Rich** for colored/syntax-highlighted output
- **Typer** for argument parsing

## Installation

```sh
pip install jspprint
# or
pipx install jspprint
```

## Usage

```sh
# Pretty-print a JSON file with syntax highlighting
jspprint data.json

# Read JSON from stdin
cat data.json | jspprint

# Filter by key
jspprint data.json name

# Filter by nested key path
jspprint data.json users.0.email

# Modify a value in the output (file is not changed)
jspprint data.json --set name=updated

# Delete a key from the output
jspprint data.json --del obsoleteField

# Set a key's value from another JSON file
jspprint data.json --set config=@overrides.json

# Same thing via stdin pipe
cat overrides.json | jspprint data.json --set config=@-

# Output compact JSON (single line, no highlighting)
jspprint data.json --compact
jspprint data.json -c

# Pipe the result
jspprint data.json --set env=prod -c | kubectl apply -f -
```

## License

MIT
