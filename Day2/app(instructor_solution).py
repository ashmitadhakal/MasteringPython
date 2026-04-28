last_entry_id = 0
result = 0.0
history = []

def console_str_input(prompt):
    return input(prompt)

def console_float_input(prompt):
    return float(console_str_input(prompt))

def console_int_input(prompt):
    return int(console_str_input(prompt))

def console_result_output(result):
    print(f"Result: {result}")

def console_history_output():
    for history_entry in history:
        print(history_entry)

def console_error_output(error_message):
    print(f"Error: {error_message}")

def console_info_output(info_message):
    print(f"Info: {info_message}")     

def append_history_entry(command, operand):
    global last_entry_id
    last_entry_id = last_entry_id + 1
    history_entry = {
        "id": last_entry_id,
        "op_name": command,
        "op_value": operand,
    }
    history.append(history_entry)


def command_clear():
    global result
    result = 0.0
    history.clear()
    console_result_output(result)


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

def command_remove():
    history_entry_id = console_int_input("Enter the history entry id to remove: ")
    for history_entry in history:
        if history_entry["id"] == history_entry_id:
            history.remove(history_entry)
            break

def command_history():
    console_history_output()

def command_invalid(command):
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


def main():

    print("Calculator Tool")
    print("Available commands: add, subtract, multiply, divide, clear, exit")

    command_loop()

main()