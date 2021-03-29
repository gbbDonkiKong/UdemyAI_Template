my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

my_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list2)

# List Comprehension
my_list2 = [i for i in range(10)]

# Multi-dim List
my_matrix = [[1, 2], 
             [3, 4]]

my_matrix2 = [[i + j for j in range(3)] for i in range(3)]
print(my_matrix2)