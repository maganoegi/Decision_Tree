

class Question():

    __slots__ = [
        'column',
        'value'
    ]

    def __init__(self, col, val):
        """ saves the column from the dataset to compare and the value to compare against """
        assert col != 0
        self.column = col
        self.value = val

    def __str__(self):
        return f"Does the column {self.column} equal {self.value} ?"
    
    def compare(self, data_row):
        """ take the row in question, and compares the column in question """
        return data_row[self.column] == self.value
