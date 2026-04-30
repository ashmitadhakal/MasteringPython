from calc_app_mod_OOP_file_Iterable.console_input import (
    console_str_input, console_int_input, console_float_input
)
from calc_app_mod_OOP_file_Iterable.console_output import (
    console_error_output, console_history_output,
    console_info_output, console_result_output
)
import logging
import json
#from calc_app_mod_OOP.calc import add, sub, mul, div
from .history import History

history = History() 

COMMAND_LOG_FILE = "commands.log"

def log_command(command):
    try:
        with open(COMMAND_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(command + "\n")
    except OSError:
        logging.error("Failed to write to command log %s", COMMAND_LOG_FILE, exc_info=True)

def get_command():
    return  console_str_input("Enter a command: ")

def command_clear():
    history.clear_history_entries()
    console_result_output(history.calc_result())

def command_calc(command_name):
    operand = console_float_input("Please enter an operand: ")

    if command_name == "divide" and operand == 0:
        raise ZeroDivisionError()

    history.append_history_entry(command_name, operand)
    console_result_output(history.calc_result())


def command_remove():
    last_entry_id = console_int_input("Enter the history entry id to remove: ")
    history.remove_history_entry(last_entry_id)

def command_history():
    console_history_output(history)
    
def command_save():
    file_name = console_str_input("Enter a file name to save history: ")
    if history.save_to_file(file_name):
        console_info_output(f"History saved to {file_name}")
    else:
        console_error_output(f"Failed to save history to {file_name}")

def command_load():
    file_name = console_str_input("Enter a file name to load history: ")
    if history.load_from_file(file_name):
        console_info_output(f"History loaded from {file_name}")
        console_result_output(history.calc_result())
    else:
        console_error_output(f"Failed to load history from {file_name}")

def command_invalid(command):
    logging.warning(f"Unknown command: '{command}'")
    console_error_output(f"Unknown command '{command}'")
    
def command_exit():
    console_info_output("Calculator exiting...")


def command_loop():

    while True:
        try:
            command = get_command()
            log_command(command)

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
            elif command == "save":
                command_save()
            elif command == "load":
                command_load()
            else:
                command_invalid(command)
        except ZeroDivisionError:
            console_error_output("Cannot divide by zero.")
