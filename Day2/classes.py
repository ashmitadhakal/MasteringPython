class Person:
    #constructor
    def __init__(self, fn, ln, age, city):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.city = city

    def walk(self):
        print(f"{self.fn} is walking")
    def run(self):
        print(f"{self.fn} is running")
    def greet(self):
        print(f"Hi, I am {self.fn} and I'm {self.age} years old. I am from {self.city}")
    def is_adult(self):
        return self.age>18
    
