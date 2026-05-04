#all programing languagaes have concept of function, except for assembly

#create a simple  function
def do_it():
    print("did it!")

print(type(do_it)) #functions are object in Python

#Function can be called multiple times
do_it()
do_it()
do_it()

def add(a,b):
    return a+b

print(add(1,2))
print(add(3,4))

def print_nums(nums):
    for num in nums:
        print(num)

print_nums([1,2,3,4])


message = "did it!"

#create a simple  function
def do_it2():
    #global message
    message = "cool"
    print(message)
do_it2()
print(message)