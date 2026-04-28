'''
Exercise 4 - Organize the Calculator into Functions
Refactor calculator code into functions (at least three functions). 
Define the functions at the top and in the same file. Remember, 
we can define functions to eliminate repetitive code and to organize responsibilities.

You are free to update your code to use additional syntaxes and other Python features not covered yet, except for classes.
'''
result = 0
hist = []
id = 1
def user_command_input():
    return(input("Enter a command: "))
def user_operand_input():
    return(float(input("Please enter an operand: ")))
def write_history(command, operand):
    global id
    hist.append({"id":id,"command":command, "operand":operand})
    id+=1
while True:
    command = user_command_input()
    if command == "clear":
        result = 0
        hist.clear()
        print("Result:",result)
    elif command == "exit":
        break
    elif command == "add":
        operand = user_operand_input()
        result = result + operand
        print("Result:",result)
        write_history(command, operand)
    elif command == "subtract":
        operand = user_operand_input()
        result = result-operand
        print("Result:",result)
        write_history(command, operand)
    elif command == "multiply":
        operand = user_operand_input()
        result = result*operand
        print("Result:",result)
        write_history(command, operand)
    elif command == "divide":
        operand = user_operand_input()
        if operand == 0:
            print("cannot divide by 0")
        else:
            result = result/operand
            print("Result:",result)
            write_history(command, operand)
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
