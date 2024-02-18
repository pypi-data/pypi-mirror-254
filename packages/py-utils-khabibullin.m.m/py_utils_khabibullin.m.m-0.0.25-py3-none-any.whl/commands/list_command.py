import json
from prettytable import PrettyTable

from commands.const import DATA_FILE, ID, LABELS, COMMAND, COMMANDS


def list_commands(labels: [str] = None):
    table = PrettyTable(["id", "command"])

    print(DATA_FILE)

    labels_set = set(labels or [])
    print(f"Labels: {labels_set}")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        commands = data[COMMANDS]

        for cmd in commands:
            if labels_set and not __has_labels(labels_set, cmd):
                continue
            table.add_row([cmd[ID], cmd[COMMAND]])

    print(table)


def __has_labels(labels_set: set[str], command: dict[any, str]) -> bool:
    if LABELS not in command:
        return False
    
    return set(command[LABELS]).intersection(labels_set)
