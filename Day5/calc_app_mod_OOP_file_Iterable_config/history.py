import json
import csv
import logging
from calc_app_mod_OOP_file_Iterable_config.calc import add, sub, mul, div
from .history_entry import HistoryEntry
from pathlib import Path

class ListIterator:
    def __init__(self, items):
        self.__items = items
        self.__index = 0

    def __next__(self):
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            self.__index += 1
            return item
        raise StopIteration


class History:

    def __init__(self):
        self.__last_entry_id = 0
        self.__entries = []

    def __iter__(self):
        return ListIterator(self.__entries)        

    def append_history_entry(self, command, operand):

        self.__last_entry_id = self.__last_entry_id + 1
        history_entry = HistoryEntry(self.__last_entry_id, command, operand)
        self.__entries.append(history_entry)

    def remove_history_entry(self, history_entry_id):
        for history_entry in self.__entries:
            if history_entry.id == history_entry_id:
                self.__entries.remove(history_entry)
                break

    def clear_history_entries(self):
        self.__entries.clear()

    def save_to_file(self, file_name):
        ext = Path(file_name).suffix
        try:
            if ext == ".json":
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(
                        [entry.__dict__ for entry in self.__entries],
                        f,
                        indent=2)
                return True
            
            elif ext == ".csv":
                with open(file_name,"w",encoding="UTF-8") as csv_file:
                    writer = csv.DictWriter(csv_file,
                            fieldnames=["id", "op_name", "op_value"])
                    writer.writeheader()

                    for entry in self.__entries:
                        writer.writerow({
                            "id": entry.id,
                            "op_name": entry.op_name,
                            "op_value": entry.op_value
                        })

                return True
            else:
                print(f"Unsupported file extension: {ext}")
                return False
        except OSError:
                logging.error("Failed to save history to %s", file_name, exc_info=True)
                return False


    def load_from_file(self, file_name):
        ext = Path(file_name).suffix.lower()
        try:    
            #self.__entries.clear()
            if ext == ".json":
                with open(file_name, "r", encoding="utf-8") as f:
                    entries = json.load(f)
                    self.__entries.clear()
                    for entry in entries:
                        self.__entries.append(
                            HistoryEntry(
                                entry["id"],
                                entry["op_name"],
                                entry["op_value"]))
                self.__last_entry_id = max(
                    (entry.id for entry in self.__entries), default=0
                )
                return True
            elif ext == ".csv":
                with open(file_name, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    for entry in reader:
                        entry_id = entry.get("id") or entry.get("_HistoryEntry__id")
                        op_name = entry.get("op_name") or entry.get("_HistoryEntry__op_name")
                        op_value = entry.get("op_value") or entry.get("_HistoryEntry__op_value")
                        self.__entries.append(
                                    HistoryEntry(
                                        int(entry_id),
                                        op_name,
                                        float(op_value)
                                    )
                        )
                return True
            else:
                print(f"Unsupported file extension: {ext}")
                return False
        except (OSError, json.JSONDecodeError):
            logging.error("Failed to load history from %s", file_name, exc_info=True)
            return False

    def calc_result(self):
        result = 0
        for entry in self.__entries:
            if entry.op_name == "add":
                result = add(result, entry.op_value)
            elif entry.op_name == "subtract":
                result = sub(result, entry.op_value)
            elif entry.op_name == "multiply":
                result = mul(result, entry.op_value)
            elif entry.op_name == "divide":
                result = div(result, entry.op_value)
        return result