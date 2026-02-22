
# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# NOTE: In the video, they start with the class in the same file, so I would start with what the video has first.
from car import Car

# car1 = an object
# Car() invokes the constructor
car1 = Car("Mustang", 2024, "red", False)

# other examples
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

# Gives memory address
# print(car1)

# Gives all the object's attributes (car1)
print("Car 1:\n" + car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

# Gives all the object's attributes (car1)
print("\nCar 2:\n" + car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

# Gives all the object's attributes (car3)
print("\nCar 3:\n" + car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

# NOTE: In the video, they use the same file and delete everything to add this, but I made an extra file for methods to be more organized
# Refer to the file "method_info.py" when looking for methods