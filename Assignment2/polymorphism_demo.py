# Assignment2/polymorphism_demo.py

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        print("Running")


class Bird(Animal):
    def move(self):
        print("Flying")


class Fish(Animal):
    def move(self):
        print("Swimming")


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


if __name__ == "__main__":
    # List of animals
    animals = [Dog(), Bird(), Fish()]
    print("🐾 Animal Movements:")
    for animal in animals:
        animal.move()

    print("\n Vehicle Movements:")
    # List of vehicles
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()
