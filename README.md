# ZID Generator

A simple and configurable Zettelkasten ID (ZID) generator for Python. Specifically designed for creating timestamp-based IDs for your notes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [AutoHotkey Integration](#autohotkey-integration)
  - [zid.ahk](#zidahk)
- [Configuration](#configuration)
- [Testing](#testing)
- [Kardenwort Ecosystem](#kardenwort-ecosystem)
- [License](#license)

---

## Features
- **Fast**: Generates a timestamp-based ID in milliseconds.
- **Configurable**: Customize your IDs via `config.ini` (format, prefix, suffix).
- **Clipboard-Ready**: Automatically copies the generated ID to your clipboard.
- **Tested**: Built-in test suite ensures reliability.

[Return to Top](#zid-generator)

## Installation

```bash
pip install pyperclip
```

[Return to Top](#zid-generator)

## Usage

Run the script directly:
```bash
python zid.py
```

The output will be printed to the console and copied to your clipboard.

[Return to Top](#zid-generator)

## AutoHotkey Integration

### zid.ahk

For a full collection of AHK scripts, see [voothi/20240411110510-autohotkey](https://github.com/voothi/20240411110510-autohotkey).


- **Description**: A simple utility to insert a timestamp in the format `YYYYMMDDHHMMSS`. Ideal for creating unique identifiers for notes or files.
- **Hotkey**: `Ctrl + Shift + /`

1.  Create a file named `zid.ahk`.
2.  Add the following script (update the python path):
    ```autohotkey
    ^+/:: ; Ctrl + Shift + /
    {
        RunWait, python "C:\Path\To\zid.py",, Hide
        Send, ^v
    }
    return
    ```
3.  Run the script. Now pressing `Ctrl + Shift + /` will generate and past a ZID.

[Return to Top](#zid-generator)

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

[Return to Top](#zid-generator)

## Testing

Run the tests using Python's built-in `unittest` module:

```bash
python -m unittest discover tests
```

[Return to Top](#zid-generator)

## Kardenwort Ecosystem

This project is part of the [Kardenwort](https://github.com/kardenwort) environment, designed to create a focused and efficient learning ecosystem.

[Return to Top](#zid-generator)

## License
MIT

[Return to Top](#zid-generator)

