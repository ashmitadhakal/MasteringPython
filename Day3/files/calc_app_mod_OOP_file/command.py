from calc_app_mod_OOP_file.console_input import (
    console_str_input, console_int_input, console_float_input
)
from calc_app_mod_OOP_file.console_output import (
    console_error_output, console_history_output,
    console_info_output, console_result_output
)
import logging
import json
#from calc_app_mod_OOP.calc import add, sub, mul, div
from .history import History

history = History() 

def log_command(command):
    with open("commands.log","a", encoding="utf-8") as f:
        f.write(command + "\n")
def get_command():
    return  console_str_input("Enter a command: ")

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


def command_loop():

    while True:
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
            with open("my_calc.json","w") as f:
                json.dump(history.entries,f)
            print("history saved")
        elif command == "load":
            file_name = console_str_input("Enter the file name:")
            try:

                with open(file_name,"r") as f:
                    loaded_entries = json.load(f)
                    history.entries.clear()
                    history.entries.extend(loaded_entries)
            except FileNotFoundError:
                console_error_output("Cannot find the file")
        else:
            command_invalid(command)