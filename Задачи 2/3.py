class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

class AmericanDate(Date):
    def format(self):
        return f"{self.month:02d}.{self.day:02d}.{self.year}"

class EuropeanDate(Date):
    def format(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())