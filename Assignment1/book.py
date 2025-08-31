# Assignment1/book.py

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author} 📖")

    def info(self):
        print(f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}")
