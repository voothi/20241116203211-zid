## Context

The current `zid.py` generator creates a timestamp-based ZID and always copies the result to the clipboard using `pyperclip.copy()`. This behavior is convenient for many workflows, but some users need to generate a ZID without modifying clipboard contents.

## Goals / Non-Goals

**Goals:**
- Add a CLI option that disables clipboard copying while preserving current output behavior.
- Keep the default behavior unchanged: generate ZID, print it, and copy it to clipboard.
- Minimize changes in `zid.py` and avoid adding new runtime dependencies.

**Non-Goals:**
- Changing the ZID format, prefix/suffix config behavior, or output formatting.
- Removing clipboard copy entirely as the default.
- Adding a GUI or alternate input mechanism.

## Decisions

- Use Python's standard `argparse` library to add a `--no-clipboard` flag.
- Keep `pyperclip` as the clipboard implementation and only call `pyperclip.copy()` when clipboard copy is enabled.
- Print the generated ZID unconditionally to standard output so both modes remain consistent.

## Risks / Trade-offs

- [Risk] `pyperclip` clipboard behavior may vary across platforms.
  → Mitigation: Maintain existing clipboard path as the default and only skip the copy operation when explicitly requested.
- [Risk] Users may accidentally pass the wrong flag name.
  → Mitigation: Use an explicit `--no-clipboard` flag name and rely on argparse help text.
