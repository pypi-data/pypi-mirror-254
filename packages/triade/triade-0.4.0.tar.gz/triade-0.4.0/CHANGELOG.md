## 0.4.0 - 2024-02-05

### Added

- Added support for XML input. It is now possible to convert XML into TOML,
YAML and JSON.
- Improved help messages with new updates. The -v option, which wasn't
documented, was also added to the help message.

### Fixed

- Prevent the standard input and standard output streams from being closed
after the program's execution. It doesn't change the functionality of the CLI
script, but allows for the main function to be used in automated tests.

## 0.3.0 - 2024-01-30

### Added

- Added support for XML output.
- Integrate library with Python's "xml.dom" builtin library. This allows the
creation of elements with multiple text nodes alongside other child elements
with a simple API.
- Convert str, int and float nodes into text nodes.

### Changed

- Replaced argparse with getopt. While it provides a more straightforward way
to parse command-line arguments, it shouldn't make a difference for the end
user.

## 0.2.1 - 2023-05-20

### Fixed

- Fixed special unicode characters on JSON output

## 0.2.0 - 2023-04-28

### Added

- Added custom error message when TOML writer tries to convert invalid data.
The input data should be a dictionary.

## 0.1.1 - 2023-04-22

### Fixed

- Fixed lib import. The previous version didn't import the parse and write
functions correctly.
- Warn the user when writing to output file in an unrecognized format.

## 0.1.0 - 2023-04-22

### Added

- Released version 0.1. The cli application freely converts from and to JSON,
YAML and TOML.
