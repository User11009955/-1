class Stat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        if len(self.numbers) == 0:
            return None
        return self.return_result()

class MinStat(Stat):
    
    def return_result(self):
        return min(self.numbers)


class MaxStat(Stat):
    def return_result(self):
        return max(self.numbers)


class AverageStat(Stat):
    def return_result(self):
        return sum(self.numbers) / len(self.numbers)

    
mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())