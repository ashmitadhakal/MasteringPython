from classes import Person
#First instance
p1 = Person("Bob", "Smith", 2,"LA")
p2 = Person("Alicia", "Smith", 34, "SF")
p3 = Person("Ashmita","Dhakal",29, "Redlands")

print(p1.fn)
print(p1.ln)
print(p1.age)
p1.walk()
p1.run()
p1.greet()
print(p1.is_adult())
#second instance
print(p2.fn)
print(p2.ln)
print(p2.age)
p2.walk()
p2.run()
print(p2.is_adult())

print(p3.fn)
print(p3.ln)
print(p3.age)
p3.walk()
p3.run()
print(p3.is_adult())
