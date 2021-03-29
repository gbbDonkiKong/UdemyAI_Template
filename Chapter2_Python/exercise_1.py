import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1
freundebuch = {"Peter": 21, "Jan": 24, "Dieter": 44, "Dennis": 27, "Daniel": 33}

def get_friends_by_age(freundebuch, age):
    freunde = []
    for item in freundebuch.items():
        if item[1] > age:
            freunde.append(item[0])

    return freunde


print(get_friends_by_age(freundebuch, 22))

# Aufgabe 2
M = [[1, 2], [3, 4]]

def transpose(M):
    M_t = [[0, 0], [0, 0]]
    for i in range(len(M)):
        for j in range(len(M[i])):
            M_t[j][i] = M[i][j]

    return M_t


print(transpose(M))

# Aufgabe 3
def e_function(a, b):
    return np.array([np.exp(a), np.exp(b)], dtype=np.int32)
    

a, b = 1, 5
exp_vals = e_function(a, b)
print(exp_vals)

...