# Update this code to make it work...

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# implement the iterator class here
class PeopleIterator:
    def __init__(self, person):
        self.__person=person
        self.__index=0

    def __next__(self):
        if self.__index < len(self.__person):
            person=self.__person[self.__index]
            self.__index+=1
            return person
        raise StopIteration

class People:

    def __init__(self):
        self.__persons = []

    def __iter__(self):
        return PeopleIterator(self.__persons)

    def add(self, person):
        self.__persons.append(person)

people = People()
people.add(Person("Alice", 40))
people.add(Person("Bob", 23))
people.add(Person("Joe", 50))
people.add(Person("Katherine", 30))
people.add(Person("Philip", 33))


for person in people:
    print(f"{person.name}: {person.age}")