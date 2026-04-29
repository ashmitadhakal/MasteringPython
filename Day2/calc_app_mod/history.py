from calc_app_mod.calc import add, sub, mul, div

last_entry_id = 0

def append_history_entry(history, command, operand):
    global last_entry_id
    last_entry_id = last_entry_id + 1
    history_entry = {
        "id": last_entry_id,
        "op_name": command,
        "op_value": operand,
    }
    history.append(history_entry)

def remove_history_entry(history, history_entry_id):
    for history_entry in history:
        if history_entry["id"] == history_entry_id:
            history.remove(history_entry)
            break

def clear_history_entries(history):
    history.clear()

def calc_result(history):
    result = 0
    for entry in history:
        if entry["op_name"] == "add":
            result = add(result, entry["op_value"])
        elif entry["op_name"] == "subtract":
            result = sub(result, entry["op_value"])
        elif entry["op_name"] == "multiply":
            result = mul(result, entry["op_value"])
        elif entry["op_name"] == "divide":
            result = div(result, entry["op_value"])
    return result