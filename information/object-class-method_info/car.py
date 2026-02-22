
# __ dunder method (double underscore)
class Car:
    # constructor (used to make objects), self = the class we're creating right now/the class "Car"
    # the parameters after "self" are attributes of the "Car" (the class)
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")