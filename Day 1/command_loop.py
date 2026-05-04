#single equals is assignment
'''
This is if loop
command = input("Enter a command: ")

#double equals is cpmparision
if command == "exit":
    #no curly brace code blocks
    #identing makes code block
    print("exiting")
else:
    print("do something else")
'''
'''
#infinite loop
while True:
    #single equals is assignment
    command = input("Enter a command: ")

    #double equals comparision
    if command == "exit":
        break
    else:
        print(command)
'''
#elif command use
while True:
    #single equals is assignment
    command = input("Enter a command: ")

    #double equals comparision
    if command == "exit":
        break #exit the loop
    elif command == "version":
        print("0.0.1")
        continue #start back at the top of the loop
    else:
        print(command)


