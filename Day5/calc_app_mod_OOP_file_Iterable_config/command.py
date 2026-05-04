from calc_app_mod_OOP_file_Iterable_config.console_input import (
    console_str_input, console_int_input, console_float_input
)
from calc_app_mod_OOP_file_Iterable_config.console_output import (
    console_error_output, console_history_output,
    console_info_output, console_result_output
)
import logging
import json
import re
#from calc_app_mod_OOP.calc import add, sub, mul, div
from .history import History

history = History() 

CALC_PATTERN = re.compile(r"^(?P<name>add|subtract|multiply|divide)\s+(?P<operand>-?\d+(?:\.\d+)?)$")
REMOVE_PATTERN = re.compile(r"^(?P<name>remove)\s+(?P<operand>\d+)$")
FILE_PATTERN = re.compile(r"^(?P<name>save|load)\s+(?P<operand>\S+)$")
BARE_PATTERN = re.compile(r"^(?P<name>history|clear|exit)$")

def command_clear():
    history.clear_history_entries()
    console_result_output(history.calc_result())

def command_calc(command_name, operand):
    if command_name == "divide" and operand == 0:
        raise ZeroDivisionError()

    history.append_history_entry(command_name, operand)
    console_result_output(history.calc_result())

def command_remove(history_entry_id):
    history.remove_history_entry(history_entry_id)

def command_history():
    console_history_output(history)

def command_save(file_name):
    if history.save_to_file(file_name):
        console_info_output(f"History saved to {file_name}")
    else:
        console_error_output(f"Failed to save history to {file_name}")

def command_load(file_name):
    if history.load_from_file(file_name):
        console_info_output(f"History loaded from {file_name}")
        console_result_output(history.calc_result())
    else:
        console_error_output(f"Failed to load history from {file_name}")

def command_invalid(command):
    logging.warning("Unknown command: %s", command)
    console_error_output(f"Unknown command '{command}'")

def command_exit():
    console_info_output("Calculator exiting...")

def get_command():
    return console_str_input("Enter a command: ")

def command_loop():

    while True:
        try:
            command = get_command()
            logging.info("Command: %s", command)

            calc_match = CALC_PATTERN.match(command)
            remove_match = REMOVE_PATTERN.match(command)
            file_match = FILE_PATTERN.match(command)
            bare_match = BARE_PATTERN.match(command)

            if calc_match:
                command_calc(calc_match["name"], float(calc_match["operand"]))
            elif remove_match:
                command_remove(int(remove_match["operand"]))
            elif file_match:
                name = file_match["name"]
                operand = file_match["operand"]
                if name == "save":
                    command_save(operand)
                else:
                    command_load(operand)
            elif bare_match:
                name = bare_match["name"]
                if name == "exit":
                    command_exit()
                    break
                elif name == "clear":
                    command_clear()
                else:
                    command_history()
            else:
                command_invalid(command)
        except ZeroDivisionError:
            console_error_output("Cannot divide by zero.")