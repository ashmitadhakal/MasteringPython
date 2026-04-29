def console_result_output(result):
    print(f"Result: {result}")

def console_history_output(history):
    for history_entry in history.entries:
        print(history_entry)

def console_error_output(error_message):
    print(f"Error: {error_message}")

def console_info_output(info_message):
    print(f"Info: {info_message}")     