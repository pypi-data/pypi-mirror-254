import sys
import json
from typing import Any

import yaml
import toml

from triade.xml_lib import TriadeDocument


def read_xml(input_data: str) -> dict:
    with TriadeDocument.fromxml(input_data) as document:
        return document.data


def write_toml(input_data: Any) -> str:
    if not isinstance(input_data, dict):
        print("Error: input data for TOML writer should be a dictionary",
              file=sys.stderr)
        sys.exit(1)

    return toml.dumps(input_data)


def write_xml(input_data: dict[str, Any]) -> str:
    with TriadeDocument(input_data) as doc:
        return doc.toprettyxml(indent="  ")


parsers = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "toml": toml.loads,
    "xml": read_xml,
}

writers = {
    "json": lambda data: json.dumps(data, ensure_ascii=False),
    "yaml": lambda data: yaml.dump(data, Dumper=yaml.SafeDumper,
                                   allow_unicode=True),
    "toml": write_toml,
    "xml": write_xml,
}


def parse(input_data: str, data_format: str) -> Any:
    if data_format not in parsers:
        raise ValueError("input format not recognized")

    output_data = parsers[data_format](input_data)

    if data_format != "json":
        output_data = json.loads(json.dumps(output_data))

    return output_data


def write(input_data: Any, data_format: str) -> str:
    if data_format not in writers:
        raise ValueError("output format not recognized")

    return writers[data_format](input_data).strip()
