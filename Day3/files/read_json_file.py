import json


class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
    
    def __repr__(self):
        return f"Person<{self.__dict__}>"

# person = Person("bob", "smith")
# print(person)

# person = Person("bob", "smith")
# print(person.__dict__)

# with open("person.json","r",encoding="utf-8") as person_file:
#      person_dict = json.load(person_file)
#      person = Person(person_dict["fn"], person_dict["ln"])
#      print(person)
#      #json.dump(person.__dict__, person_file)

#mini-lab - implement the load people function

def load_people(file_name):
    
    try:
        #write code here to load people
        with open(file_name,"r",encoding="utf-8") as people_file:
            people_list = json.load(people_file)
            people_objects = []
            for people in people_list:
                person = Person(people["fn"], people["ln"])
                people_objects.append(person)
            return people_objects
    except FileNotFoundError: 
        print(f"{file_name} is not found") 
        return[]
    


people = load_people("people.json") 
print(people)
# def load_people(file_name):
#     try:
#         with open(file_name, "r", encoding="utf-8") as people_file:
#             people_list = json.load(people_file)

#             people_objects = []
#             for people in people_list:
#                 person = Person(people["fn"], people["ln"])
#                 people_objects.append(person)

#             return people_objects

#     except FileNotFoundError:
#         print(f"{file_name} is not found")
#         return []

# people = load_people("people.json")
# print(people)
# with open("person.json","w",encoding="utf-8") as person_file:
#     json.dump(person.__dict__, person_file)

# people = [
#     Person("bob", "smith"),
#     Person("Alice", "smith"),
#     Person("Tim", "smith"),
#     Person("Niki", "smith"),
#     Person("Sam", "smith"),
# ]

# with open ("people.json","w",encoding="utf-8") as person_file:
#     people_dicts = []
#     for person in people:
#         people_dicts.append(person.__dict__)
    
#     json.dump(people_dicts, person_file)
