import json
import logging
from calc_app_mod_OOP_file_Iterable.calc import add, sub, mul, div
from .history_entry import HistoryEntry
 
last_entry_id = 0

class History:
    def __init__(self):
        self._entries = []
        self.last_entry_id = 0

    def __iter__(self):
        return iter(self._entries) 
    
    def __repr__(self):
        return f"history<{self.__dict__}>"
    
    def append_history_entry(self, command, operand):
        self.last_entry_id += 1
        history_entry = HistoryEntry(self.last_entry_id, command, operand)
        self._entries.append(history_entry)

    def remove_history_entry(self, history_entry_id):
        for entry in self._entries:
            if entry.id == history_entry_id:
                self._entries.remove(entry)
                break

    def clear_history_entries(self):
        self._entries.clear()

    def save_to_file(self, file_name):
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(
                    [entry.__dict__ for entry in self._entries],
                    f,
                    indent=2)
            return True
        except OSError:
            logging.error("Failed to save history to %s", file_name, exc_info=True)
            return False

    def load_from_file(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                entries = json.load(f)
                self._entries.clear()
                for entry in entries:
                    self._entries.append(
                        HistoryEntry(entry["id"], entry["operation_name"], entry["operand"])
                    )

            self.last_entry_id = max(
                (entry.id for entry in self._entries), default=0
            )

            return True
        except (OSError, json.JSONDecodeError):
            logging.error("Failed to load history from %s", file_name, exc_info=True)
            return False
    
    def calc_result(self):
        result = 0
        for entry in self._entries:
            if entry.operation_name == "add":
                result = add(result, entry.operand)
            elif entry.operation_name == "subtract":
                result = sub(result, entry.operand)
            elif entry.operation_name == "multiply":
                result = mul(result, entry.operand)
            elif entry.operation_name == "divide":
                result = div(result, entry.operand)
        return result
    
class ListIterator:
    def __init__(self, entries):
        self.__entries=entries
        self.__index=0

    def __next__(self):
        if self.__index < len(self.__entries):
            entries=self.__entries[self.__index]
            self.__index+=1
            return entries
        raise StopIteration