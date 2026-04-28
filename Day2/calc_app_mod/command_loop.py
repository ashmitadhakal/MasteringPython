from calc_app_mod.math import command_calc, add, sub, mul, div
from calc_app_mod.console import get_command, command_invalid, command_exit
from calc_app_mod.history import command_clear, command_remove, command_history

def command_loop():
    while True:
        command = get_command()
        if command == "exit":
            command_exit()
            break
        elif command == "clear":
            command_clear()
        elif command == "add":
            command_calc(add, command)
        elif command == "subtract":
            command_calc(sub, command)
        elif command == "multiply":
            command_calc(mul, command)
        elif command == "divide":
            command_calc(div, command)
        elif command == "remove":
            command_remove()
        elif command == "history":
            command_history()
        else:
            command_invalid(command)
