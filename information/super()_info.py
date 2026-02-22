# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a circle with an area of {self.width ** 2}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a circle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "blue", is_filled = False, width = 6)
triangle = Triangle(color = "yellow", is_filled = True, width = 7, height = 8)

# circle
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe() # describe method in child overrides the describe method in parent so we use super() to use both

# square
print()
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
square.describe()

# triangle
print()
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()