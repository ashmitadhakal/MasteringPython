from calc_app_mod_OOP.console_input import (
    console_str_input, console_int_input, console_float_input
)
from calc_app_mod_OOP.console_output import (
    console_error_output, console_history_output,
    console_info_output, console_result_output
)
import logging
#from calc_app_mod_OOP.calc import add, sub, mul, div
from .history import History

history = History() 

def command_clear():
    history.clear_history_entries()
    console_result_output(history.calc_result())

def command_calc(command_name):
    operand = console_float_input("Please enter an operand: ")
    #if command_name == "divide" and operand == 0:

    history.append_history_entry(command_name, operand)
    console_result_output(history.calc_result())

def command_remove():
    last_entry_id = console_int_input("Enter the history entry id to remove: ")
    history.remove_history_entry(last_entry_id)

def command_history():
    console_history_output(history)

def command_invalid(command):
    logging.warning(f"Unknown command: '{command}'")
    console_error_output(f"Unknown command '{command}'")
    

def command_exit():
    console_info_output("Calculator exiting...")

def get_command():
    return console_str_input("Enter a command: ")

def command_loop():

    while True:
        command = get_command()

        if command == "exit":
            command_exit()
            break
        elif command == "clear":
            command_clear()
        elif command == "add":
            command_calc(command)
        elif command == "subtract":
            command_calc(command)
        elif command == "multiply":
            command_calc(command)
        elif command == "divide":
            command_calc(command)
        elif command == "remove":
            command_remove()
        elif command == "history":
            command_history()
        else:
            command_invalid(command)