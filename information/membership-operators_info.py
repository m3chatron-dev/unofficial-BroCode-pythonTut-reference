# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# LETTER EXAMPLE
    # email = "BroCode@gmail.com"

    # if "@" in email and "." in email:
        # print("Valid email")
    # else:
        # print("Invalid email")

# LIST EXAMPLE
    # students = {"Spongebob", "Patrick", "Sandy"}

    # student = input("Enter the name of a student: ").capitalize()

    # if student in students:
        # print(f"{student} is a student")
    # else:
        # print(f"{student} was not found")

    # ALSO WORKS:
    # if student not in students:
        # print(f"{student} was not found")
    # else:
        # print(f"{student} is a student")

# DICTIONARY EXAMPLE

    # grades = {"Sandy": "A",
              # "Squidward": "B",
              # "Spongebob": "C",
              # "Patrick": "D",}

    # student = input("Enter the name of a student: ").capitalize()

    # if student in grades:
        # print(f"{student}'s grade is {grades[student]}")
    # else:
         #print(f"{student} was not found")
