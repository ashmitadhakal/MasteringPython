from calc_app_mod.console import console_result_output, console_int_input
history = []
last_entry_id = 0

def console_history_output():
    for history_entry in history:
        print(history_entry)
def command_history():
    console_history_output()
def append_history_entry(command, operand):
    global last_entry_id
    last_entry_id = last_entry_id + 1
    history_entry = {
        "id": last_entry_id,
        "Command": command,
        "Operand": operand,
    }
    history.append(history_entry)


def command_clear():
    global result
    result = 0.0
    history.clear()
    console_result_output(result)

def command_remove():
    history_entry_id = console_int_input("Enter the history entry id to remove: ")
    for history_entry in history:
        if history_entry["id"] == history_entry_id:
            history.remove(history_entry)
            break