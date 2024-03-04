class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        del self.table[row]
        self.rows -= 1

    def delete_col(self, col):
        for row in range(self.rows):
            del self.table[row][col]
        self.cols -= 1

    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1

    def add_col(self, col):
        for row in range(self.rows):
            self.table[row].insert(col, 0)
        self.cols += 1

        
tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()