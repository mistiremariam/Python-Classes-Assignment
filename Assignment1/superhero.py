# Assignment1/superhero.py

class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def attack(self):
        print(f"{self.name} uses {self.power}! 💥")

    def info(self):
        print(f"Superhero: {self.name}, Power: {self.power}, Universe: {self.universe}")
