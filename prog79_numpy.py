# The NumPy (Numeric Python) package helps
# us manipulate large arrays and matrices of
# numeric data.
import numpy as np

a = np.array([1, 2, 3])
print(a)

a = np.array([1, 2, 3, 4, 5], int)
print(a[1])          #2

# we can define the type of array passed
b = np.array([1, 2, 3, 4, 5], dtype=float)
print(b)           #2.0

array_1 = np.array([[1,2,3],[0,0,0]])
array_2 = np.array([[0,1,1],[7,8,9]])

print(np.concatenate((array_1, array_2), axis=1))
print(np.concatenate((array_1, array_2), axis=0))

print(np.eye(8, 7, 2))
