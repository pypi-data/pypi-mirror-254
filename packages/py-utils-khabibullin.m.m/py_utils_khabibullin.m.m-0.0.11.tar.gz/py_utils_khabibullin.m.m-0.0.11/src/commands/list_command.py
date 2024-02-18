import json
from prettytable import PrettyTable


def list_commands():
    table = PrettyTable(["id", "name"])

    with open("data.json", "r") as f:
        data = json.load(f)

