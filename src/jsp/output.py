import json
import rich


def print_json(data):
    print(json.dumps(data, indent=2))
