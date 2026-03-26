import sys

my_array = [1, 2, 3] # dynamic array


# Reading from the array (it is instant or O(1) time)
print(my_array[0])
print(id(my_array[0]))
print(sys.getsizeof(my_array[0]))
print(type(my_array[0]))
print(dir(my_array[0]))
