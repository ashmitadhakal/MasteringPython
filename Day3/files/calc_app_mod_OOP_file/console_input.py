def console_str_input(prompt):
    return input(prompt)

def console_float_input(prompt):
    return float(console_str_input(prompt))

def console_int_input(prompt):
    return int(console_str_input(prompt))

def console_result_output(result):
    print(f"Result: {result}")

def console_error_output(error_message):
    print(f"Error: {error_message}")

def console_info_output(info_message):
    print(f"Info: {info_message}")  

def command_invalid(command):
    console_error_output(f"Unknown command '{command}'")

def command_exit():
    console_info_output("Calculator exiting...")