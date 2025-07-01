# Custom iterator class

class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# List of integers
numbers = [10, 20, 30, 40, 50]

# Creating and using the iterator
my_iterator = ListIterator(numbers)

for number in my_iterator:
    print(number)
