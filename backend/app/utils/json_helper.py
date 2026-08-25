import json


def safe_json_load(value, default=None):

    if not value:
        return default if default is not None else {}

    try:
        return json.loads(value)

    except json.JSONDecodeError:
        return default if default is not None else {}