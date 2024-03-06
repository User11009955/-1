class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        
    def __sub__(self, other):
        return (self.month - other.month) * 30 + self.day - other.day
        
# Ваш код

mar5 = Date(3, 3)
jan1 = Date(1, 5)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)