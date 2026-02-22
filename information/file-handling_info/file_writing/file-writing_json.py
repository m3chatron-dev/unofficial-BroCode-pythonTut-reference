# Python writing files (.json)

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook",
}

file_path = "" # enter yours

try:
    with open(file_path, "x") as file:
        json.dump(employee, file, indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("That file already exists!")