import numpy as np

grades_py_list = [100, 89, 44, 78, 45, 24, 18]
grades_np_array = np.array(grades_py_list, dtype=np.int32)

print(grades_py_list)
print(grades_np_array)

print(np.max(grades_np_array))
print(np.min(grades_np_array))