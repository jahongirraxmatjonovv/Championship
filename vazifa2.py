def tuple_to_list(tup):
    return list(tup)

def tuple_to_set(tup):
    return set(tup)

def tuple_to_dict(tup):
    return dict(enumerate(tup))

my_tuple = (1, 2, 3)
my_list = tuple_to_list(my_tuple)
my_set = tuple_to_set(my_tuple)
my_dict = tuple_to_dict(my_tuple)

print("Tuple:", my_tuple)
print("List:", my_list)
print("Set:", my_set)
print("Dictionary:", my_dict)
