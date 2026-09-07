class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"This Car is {self.name} and Model is {self.model}"

    def __eq__(self, other: Car):
        return self.name == other.name

    def __add__(self, other: Car):

        return self.model + other.model


Car1 = Car("Car1", 12)
Car2 = Car("Car2", 12)
Car3 = Car1 + Car2

print(Car3)
print(Car1)
print(f"{Car1}")
