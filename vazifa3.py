my_list = [1, 2, 3, 4, 5]

my_tuple = (6, 7, 8, 9, 10)

my_set = {11, 12, 13, 14, 15}

my_dict = {'a': 16, 'b': 17, 'c': 18, 'd': 19, 'e': 20}

my_string = "Hello, World!"

my_range = range(5)

class MyIterator:
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

my_iterable = MyIterator([21, 22, 23, 24, 25])

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
print("String:", my_string)
print("Range:", list(my_range))
print("Custom Iterator:", list(my_iterable))
