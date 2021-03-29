def max_list(list):
    max_value = 0
    for value in list:
        if value > max_value:
            max_value = value
    return max_value
    

my_list = [-2, 1, 2, -10, 22]
print(max_list(my_list))
print(max(my_list))
