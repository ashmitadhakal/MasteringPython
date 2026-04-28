'''
Exercise 2 - Capture Calculation History
Using the data types and structures we have learned thus far(List and Disctionary),
 capture a history of the calculator commands: add, subtract, multiple, and divide.

For each history entry, store a unique integer id (do not use external modules,
just write some code to generate an id - do the best you can with this), the name of the command, and the operand value typed in. Do not track the result on the history.

Add a new command to the calculator named "history". When the user runs the "history" 
command display a history of the commands.'''

result = 0
hist = []
id= 1
while True:
    command = input("Enter a command: ")
    if command == "clear":
        result = 0
        print("Result:",result)
        hist.append({"id":id,"command":command, "operand":"No operand"})
        id=id+1
    elif command == "exit":
        break
    elif command == "add":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result + operand
        print("Result:",result)
        hist.append({"id":id,"command":command, "operand":operand})
        id=id+1
    elif command == "subtract":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result-operand
        print("Result:",result)
        hist.append({"id":id,"command":command, "operand":operand})
        id=id+1
    elif command == "multiply":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result*operand
        print("Result:",result)
        hist.append({"id":id,"command":command, "operand":operand})
        id=id+1
    elif command == "divide":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        if operand == 0:
            print("cannot divide by 0")
        else:
            operand = float(operand)
            result = result/operand
            print("Result:",result)
        hist.append({"id":id,"command":command, "operand":operand})
        id=id+1
    elif command == "history":
        if not hist:
            print("No calculation history so far")
        else:
            print("The complete detail of the calculation history: ")
            for item in hist:
               print(f"ID: {item['id']}, Command:{item['command']}, Operand:{item['operand']}")
        hist.append({"id":id,"command":command, "operand":"No operand"})
        id=id+1
    else:
        print("command unknown, please give new command")
        hist.append({"id ":id,"command ":command, "operand ":"No operand"})
        id=id+1
    