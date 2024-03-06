class SparseArray():
    def __init__(self):
        self.array = {}
        
    def __setitem__(self, index, value):
        if value != 0:
            self.array[index] = value
        elif index in self.array:
            del self.array[index]
    
    def __getitem__(self, index):
        if index in self.array:
            return self.array[index]
        else:
            return 0

# Ваш код

def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)