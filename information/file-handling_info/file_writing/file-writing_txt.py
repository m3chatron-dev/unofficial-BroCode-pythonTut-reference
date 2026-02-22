# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "" # enter yours

# "w": writes a new file, no duplicates but won't give error. if it were an existing file then it would overwrite it
"""
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")
"""
# "x": writes a new file, will give error if duplicate unless you use except statement
"""
try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")
"""
# "a": same functionality as 'w', but appends if it's an existing file
"""
try:
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")
"""

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")