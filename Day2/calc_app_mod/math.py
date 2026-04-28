from calc_app_mod.console import console_result_output, console_int_input, console_float_input
from calc_app_mod.history import append_history_entry

result = 0.0

def add(result, operand):
    return result + operand


def sub(result, operand):
    return result - operand


def mul(result, operand):
    return result * operand

def div(result, operand):
    return result / operand

def command_calc(calc_fn, command_name):
    global result
    operand = console_float_input("Please enter an operand: ")
    result = calc_fn(result, operand)
    console_result_output(result)
    append_history_entry(command_name, operand)