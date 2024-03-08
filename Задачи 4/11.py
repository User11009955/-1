class Summator:
    def __init__(self) -> None:
        pass

    def sum(self, N):
        result = 0
        for n in range(1, N + 1):
            result += self.transform(n)
        return result

class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

q = SquareSummator()
print(q.sum(3))