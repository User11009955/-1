class Queue:
    def __init__(self, *args):
        self.items = list(args)
    
    def append(self, *values):
        self.items.extend(values)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    def next(self):
        return Queue(*self.items[1:])

    def copy(self):
        return Queue(*self.items)
    
    def extend(self, other):
        self.items.extend(other.items)
    
    def __next__(self):
        return self.next()
    
    def __add__(self, other):
        new_queue = Queue(*self.items)
        new_queue.extend(other)
        return new_queue

    def __iadd__(self, other):
        self.extend(other)
        return self

    
    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.items == other.items
        return False
    
    def __rshift__(self, N):
        if N >= len(self.items):
            return []
        return Queue(*self.items[N:])
    
    def __str__(self):
        if self.items == []:
            return '[]'
        return ' -> '.join(str(i) for i in self.items)
    
q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)