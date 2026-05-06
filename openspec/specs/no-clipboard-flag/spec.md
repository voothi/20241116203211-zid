# no-clipboard-flag Specification

## Purpose
TBD - created by archiving change 20260506092529-no-clipboard. Update Purpose after archive.
## Requirements
### Requirement: Disable clipboard copying with CLI flag
The system SHALL support a `--no-clipboard` option on `zid.py` that generates the ZID and prints it to standard output without copying it to the clipboard.

#### Scenario: Generate ZID without copying
- **WHEN** the user runs `python zid.py --no-clipboard`
- **THEN** the generated ZID is printed to standard output
- **AND** the clipboard is not modified by the script

#### Scenario: Preserve default clipboard behavior
- **WHEN** the user runs `python zid.py`
- **THEN** the generated ZID is printed to standard output
- **AND** the generated ZID is copied to the clipboard

