'''
Exercise 3 - Add Remove Command to the History
Add a new command to the calculator named "remove". When the user runs the "remove" command, 
ask the user for a history entry id. Then remove the history entry from the history list. 
Do not update the result.
We did not cover the remove command. Look this up in the Python documentation.

When the "clear" command is executed, clear the history.
'''
result = 0
hist = []
id= 1
while True:
    command = input("Enter a command: ")
    if command == "clear":
        result = 0
        hist.clear()
        print("Result:",result)
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
    elif command == "remove":
        remove_item = int(input("Enter history ID you want to delete: "))
        for item in hist:
            if item["id"] == remove_item:
                hist.remove(item)
                break
    else:
        print("command unknown, please give new command")
    