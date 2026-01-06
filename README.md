# ZID Generator

A simple and configurable Zettelkasten ID (ZID) generator for Python.

## Features
- **Fast**: Generates a timestamp-based ID in milliseconds.
- **Configurable**: Customize your IDs via `config.ini` (format, prefix, suffix).
- **Clipboard-Ready**: Automatically copies the generated ID to your clipboard.
- **Tested**: Built-in test suite ensures reliability.

## Installation

```bash
pip install pyperclip
```

## Usage

Run the script directly:
```bash
python zid.py
```

The output will be printed to the console and copied to your clipboard.

## Configuration

Create a `config.ini` in the project root to customize the output:

```ini
[Settings]
# Format for the timestamp (ZID)
format = %Y%m%d%H%M%S
# Optional prefix and suffix
prefix = 
suffix = 
```

## Testing

Run the tests using Python's built-in `unittest` module:

```bash
python -m unittest discover tests
```

## License
MIT
