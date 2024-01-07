import math
import types

class Sudoku(object):
    s_data = []

    def __init__(self, data):
        self.s_data = data
        return

    def check_correct(self):
        n_rows = len(self.s_data)
        if n_rows == 0:
            return False
        n_cols = len(self.s_data[0])
        if n_rows != n_cols:
            return False
        if math.sqrt(n_cols) % int(math.sqrt(n_cols)) > 0:
            return False
        for row in self.s_data:
            for n in row:
                if not n:
                    return False
                if type(n) != int or type(n) == bool:
                    return False
                if n < 1 or n > n_cols:
                    return False
        return True

    def is_valid(self):
        #check matrix dimensions
        if not self.check_correct():
            return False
        # check rows unique
        for row in self.s_data:
            for n in row:
                if row.count(n) > 1:
                    return False
        # check columns unique
        for n_col in range(len(self.s_data[0])):
            col = []
            for n_row in range(len(self.s_data)):
                col.append(self.s_data[n_col][n_row])
            for n in col:
                if col.count(n) > 1:
                    return False
        # print(self.s_data[0])
        # check blocks unique
        block_size = int(math.sqrt(len(self.s_data)))
        for n_col in range(0, len(self.s_data[0]), block_size):
            for n_row in range(0, len(self.s_data), block_size):
                block = []
                for l in range(block_size):
                    for n in self.s_data[n_row + l][n_col:n_col + block_size:]:
                        block.append(n)
                for n in block:
                    if block.count(n) > 1:
                        return False

        return True