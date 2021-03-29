list_a = [10, 20, 30]
list_b = ["Jan", "Peter", "Max"]

for value_a, value_b in zip(list_a, list_b):
    print(value_a, value_b)


for i in range(len(list_a)):
    print(i, ": ", list_a[i])