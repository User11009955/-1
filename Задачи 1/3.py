class Balance:
    def __init__(self):
        self.balance = 0

    def add_right(self, amount):
        self.balance -= amount
    
    def add_left(self, amount):
        self.balance += amount

    def result(self):
        if self.balance < 0:
            return 'R'
        elif self.balance > 0:
            return 'L'
        return '='