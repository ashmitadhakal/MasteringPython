#simple calculator as a lab exercise for the training
'''
Exercise 1 - Create a Calculator
Create a new folder named calc_app in the demos folder. Create new file named app.py folder.
Build a command line program which prompts the user for a command.
Six Commands:
"add" : operation to perform => +
"subtract" : operation to perform => -
"multiply" : operation to perform => *
"divide" : operation to perform => /
"clear" - reset current result to 0 - does not have an operand
"exit" - that exits program
Prompt the user for the command and the operand.

Enter a command: add
Please enter an operand: 10
Display the result after each command. For example, if I did an "add" operation:

Result: <previous result + 10>
If the user types an unknown command, display an error for unknown command, and ask for the next command.
'''
#My solution (considering knowledge of loop, int/float datatypes, basic operations)
result = 0
while True:
    command = input("Enter a command: ")
    if command == "clear":
        result = 0
        print("Result:",result)
    elif command == "exit":
        break
    elif command == "add":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result + operand
        print("Result:",result)
    elif command == "subtract":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result-operand
        print("Result:",result)
    elif command == "multiply":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        result = result*operand
        print("Result:",result)
    elif command == "divide":
        operand = input("Please enter an operand: ")
        operand = float(operand)
        if operand == 0:
            print("cannot divide by 0")
        else:
            operand = float(operand)
            result = result/operand
            print("Result:",result)
    else:
        print("command unknown, please give new command")