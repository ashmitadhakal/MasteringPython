

class HistoryEntry:
    def __init__(self,id,operation_name,operand):
        self.id=id
        self.operation_name=operation_name
        self.operand=operand

    def __repr__(self):
        return f"{self.operation_name}: {self.operand}"

#update the rest of the application to use the HistoryEntry class instead of
#the dictionary which is being used to store each history entry

