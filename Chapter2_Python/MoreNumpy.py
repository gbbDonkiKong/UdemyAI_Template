import numpy as np

my_array = np.array([1, 2, 3], dtype=np.float32)
print(my_array)

my_zero_array = np.zeros(shape=(10), dtype=np.int32)
print(my_zero_array)
my_ones_array = np.ones(shape=(10), dtype=np.int32)
print(my_ones_array)

my_ones_matrix = np.ones(shape=(3, 3), dtype=np.int32)
print(my_ones_matrix)

my_random_array = np.random.randint(low=0, high=11, size=10)
print(my_random_array)