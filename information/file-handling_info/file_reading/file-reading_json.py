# Python reading files (.json)

import json

file_path = "" # enter yours

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
        print(content["age"])
        print(content["job"])
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read that file")