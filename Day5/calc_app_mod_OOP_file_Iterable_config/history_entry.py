

class HistoryEntry:
    def __init__(self, id, op_name, op_value):
        self.id = id
        self.op_name = op_name
        self.op_value = op_value

    def __repr__(self):
        return f"{self.op_name}: {self.op_value}"

#update the rest of the application to use the HistoryEntry class instead of
#the dictionary which is being used to store each history entry

