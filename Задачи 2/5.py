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


# Пример использования

tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

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