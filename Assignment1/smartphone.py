# Assignment1/smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")
