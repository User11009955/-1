class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]

values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))