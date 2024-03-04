class OddEvenSeparator:
    def __init__(self):
        self.odd_lst = []
        self.even_lst = []
    
    def add_number(self, number):
        if number % 2 == 0:
            self.even_lst.append(number)
        else:
            self.odd_lst.append(number)
    def even(self):
        return self.even_lst

    def odd(self):
        return self.odd_lst