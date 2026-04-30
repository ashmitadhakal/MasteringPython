import json


class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

person = Person("bob", "smith")
print(person.__dict__)

with open("person.json","w",encoding="utf-8") as person_file:
    json.dump(person.__dict__, person_file)

people = [
    Person("bob", "smith"),
    Person("Alice", "smith"),
    Person("Tim", "smith"),
    Person("Niki", "smith"),
    Person("Sam", "smith"),
]

with open ("people.json","w",encoding="utf-8") as person_file:
    people_dicts = []
    for person in people:
        people_dicts.append(person.__dict__)
    
    json.dump(people_dicts, person_file)