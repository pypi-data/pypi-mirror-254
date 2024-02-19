"""Triade - Convert JSON, YAML, TOML and XML on the command-line

usage:
    triade -h
    triade -v
    triade [-i] [-o OUTPUT_FILE] [-I INPUT_FORMAT] [-O OUTPUT_FORMAT] <FILE>

description:
    Triade allows you to convert data formatted as JSON, YAML, TOML and XML.
    By giving a file name on the command line, 'triade' will read it and
    convert the data to another format based on the chosen format or the output
    file name.

    If no input file name is given, and standard input is not a terminal, then
    data will be read from stdin. In that case, the '-I' option is necessary.

    If no output file is chosen, the data will be written to standard output.
    If no output format is chosen, the data will be converted to JSON, and the
    program will print a warning to standard error.

positional arguments:
    FILE
        The input file from which the data will be read before conversion. If
        the file name is '-', data will be read from standard input.

options:
    -h, --help
        Show this help message and exit.

    -v, --version
        Show version number.

    -o OUTPUT_FILE, --output-file OUTPUT_FILE
        Choose an output file to write the data. If the file is '-', the data
        will be written to standard output.

    -I INPUT_FORMAT, --input-format INPUT_FORMAT
        Specify the input format. This option is required if the data is read
        from standard input.

    -O OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
        Specify the output format. This options is required if the data is
        written to standard output.

    -i, --interactive
        Not implemented yet.
"""
import sys
from getopt import gnu_getopt, GetoptError
import io
import typing as t

from triade.lib import parse, write
from triade import __version__


FORMAT_LIST = ["json", "yaml", "toml", "xml"]
SHORT_OPTS = "io:I:O:hv"
LONG_OPTS = ["output-file=", "input-format=", "output-format=", "help",
             "version", "interactive"]

args_t = list[str]
opts_t = list[tuple[str, str]]


def parse_args() -> tuple[opts_t, args_t]:
    try:
        return gnu_getopt(sys.argv[1:], SHORT_OPTS, LONG_OPTS)
    except GetoptError as err:
        print("Error:", err.msg, file=sys.stderr)
        sys.exit(2)


def show_help():
    print(__doc__.strip())
    return 0


def print_version():
    if __version__ is None:
        return 3

    print(__version__)
    return 0


def get_input_file(args: args_t, opts: opts_t) -> tuple[t.TextIO, str]:
    """Read the command-line arguments and optional arguments and return the
    input file and data format. The file is returned as a file object from the
    'open' builtin function. It is up to the caller to close the file."""
    try:
        file_name = args[0]
        input_format = file_name.split(".")[-1]
    except IndexError:
        file_name = ""
        input_format = None

    for flag, optarg in opts:
        if flag in ["-I", "--input-format"]:
            input_format = optarg.lower()

    input_format = input_format.replace("yml", "yaml")

    if len(args) == 0 and sys.stdin.isatty():
        print("Error: no input file or stream detected.", file=sys.stderr)
        sys.exit(1)
    elif len(args) == 0 and input_format is None:
        print("Error: input data format cannot be inferred.", file=sys.stderr)
        print("Valid formats: %s" % (FORMAT_LIST), file=sys.stderr)
        sys.exit(1)
    elif input_format not in FORMAT_LIST:
        print("Error: format %s is not recognized." % (input_format),
              file=sys.stderr)
        print("Valid formats: %s" % (FORMAT_LIST), file=sys.stderr)
        sys.exit(1)

    if len(args) == 0:
        return sys.stdin, input_format
    elif input_format is None:
        input_format = file_name.split(".")[-1]
        if input_format not in FORMAT_LIST:
            print("Error: format %s is not recognized." % (input_format),
                  file=sys.stderr)
            sys.exit(1)

    return open(file_name, mode="r"), input_format


def get_output_file(opts: opts_t) -> tuple[t.TextIO, str]:
    """Read command-line optional arguments and return the output file and data
    format. The file is returned as a file object from the 'open' builting
    function. It is up to the caller to close the file."""
    output_format = None
    file_name = ""
    for flag, optarg in opts:
        if flag in ["-O", "--output-format"]:
            output_format = optarg.lower()
        elif flag in ["-o", "--output-file"]:
            file_name = optarg

    if output_format is None and len(file_name.split(".")) <= 1:
        output_format = get_default_output_format()
    elif output_format is None:
        output_format = file_name.split(".")[-1]

    if file_name in ["", "-"]:
        return sys.stdout, output_format

    return open(file_name, mode="w"), output_format


def get_default_output_format() -> str:
    print("Warning: the output file's format is not recognized.",
          "Defaulting to json as standard format.", file=sys.stderr)
    return "json"


def main():
    opts, args = parse_args()

    for flag, optarg in opts:
        if flag in ["-h", "--help"]:
            return show_help()
        elif flag in ["-v", "--version"]:
            return print_version()

    input_file = io.StringIO()
    output_file = io.StringIO()
    try:
        input_file, input_format = get_input_file(args, opts)
        output_file, output_format = get_output_file(opts)

        input_data = input_file.read()
        parsed_data = parse(input_data, input_format)
        output_data = write(parsed_data, output_format)

        output_file.write(output_data.strip())
        output_file.write("\n")

        return 0
    finally:
        if input_file is not sys.stdin:
            input_file.close()
        if output_file is not sys.stdout:
            output_file.close()
