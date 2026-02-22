# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

# instance variables = Defined in the constructor
# ex. self.model = model (refer to object-class-method_info folder/directory for more detail)

# NOTE: the class must always be capitalized, such as "Student" shown in the next line
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self is usually when talking about an object; however if it's just the class, we'll use the class ("Student" in this situation)
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

"""
# student1 description
print(student1.name)
print(student1.age)

# student2 description
print()
print(student2.name)
print(student2.age)
"""

# class_year and num_students
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# Theoretically, you could use this
    # print(student1.class_year)
# or
    # print(student2.class_year)
# However it's inefficient when you could use the class itself since it's a variable shared with both objects