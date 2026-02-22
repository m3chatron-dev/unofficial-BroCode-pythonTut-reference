# return = statement used to end a function
#          and send a result back to the caller

fName = input("Enter your first name: ")
lName = input("Enter your last name: ")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name(fName, lName)

print(f"You're name is {full_name}")