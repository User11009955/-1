class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        result = 0
        for n in range(1, N + 1):
            result += self.transform(n)
        return result


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

q = SquareSummator()
print(q.sum(3))