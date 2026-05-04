#take input from user and print
name = input("Enter your name: ")
print("hello, "+name + "!")

age_input = input("Enter your age: ")
age = int(age_input)
print(type(age), age)

#Operations in different datatypes
#Operator overloading i.e. Operator works differently when data type is different such as:

age_input = age_input + 1 
age_input = age_input + str(1)
age = age+1
print(age_input)
print(age)