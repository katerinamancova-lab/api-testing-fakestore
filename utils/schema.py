import json
from pathlib import Path

from jsonschema import validate


def validate_schema(instance: dict, schema_path: str) -> None:
    schema_file = Path(schema_path)
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    validate(instance=instance, schema=schema)
