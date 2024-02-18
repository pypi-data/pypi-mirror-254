import json
import os
from prettytable import PrettyTable


def list_commands():
    table = PrettyTable(["id", "name"])

    data_folder = os.path.dirname(__file__)
    file_name = os.path.join(data_folder, "data.json")

    print(os.getcwd())
    print(file_name)

    with open(file_name, "r") as f:
        data = json.load(f)

