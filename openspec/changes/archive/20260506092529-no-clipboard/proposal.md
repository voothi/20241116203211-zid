## Why

The current ZID generator always copies the generated ID to the clipboard. Some users need a way to generate a ZID and output it only to the terminal without affecting clipboard contents.

## What Changes

- Add a `--no-clipboard` launch option to `zid.py`.
- Preserve the existing default behavior of copying the generated ZID to the clipboard.
- Ensure the script still prints the ZID to standard output in both modes.

## Capabilities

### New Capabilities
- `no-clipboard-flag`: Add a CLI option that disables clipboard copying while still printing the generated ZID.

### Modified Capabilities
- 

## Impact

- `zid.py` command-line behavior will change by supporting an additional flag.
- Existing users who rely on clipboard copying will not be affected unless they opt into the new flag.
