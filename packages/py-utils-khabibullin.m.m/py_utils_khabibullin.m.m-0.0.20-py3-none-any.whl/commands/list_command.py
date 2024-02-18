import json
import os
from prettytable import PrettyTable

from commands.const import LABELS


def list_commands(labels: [str] = None):
    table = PrettyTable(["id", "command"])

    data_folder = os.path.dirname(__file__)
    file_name = os.path.join(data_folder, "data.json")

    print(os.getcwd())
    print(file_name)

    labels_set = set(labels or [])
    print(f"Labels: {labels_set}")

    with open(file_name, "r") as f:
        data = json.load(f)
        commands = data["commands"]

        for cmd in commands:
            if labels_set and not __has_labels(labels_set, cmd):
                continue
            table.add_row([cmd["id"], cmd["command"]])

    print(table)


def __has_labels(labels_set: set[str], command: dict[any, str]) -> bool:
    if LABELS not in command:
        return False
    
    return set(command[LABELS]).intersection(labels_set)
