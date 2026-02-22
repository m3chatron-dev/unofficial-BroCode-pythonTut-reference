# NOTE: In the video, they use the same file and delete everything to add this, but I made an extra file for methods to be more organized
from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

# the drive function
car1.drive()
car2.drive()
car3.drive()

# the stop function
print()
car1.stop()
car2.stop()
car3.stop()

# the describe function
print()
car1.describe()
car2.describe()
car3.describe()