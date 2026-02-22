# Python reading files (.csv)

import csv

file_path = "" # enter yours

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read that file")