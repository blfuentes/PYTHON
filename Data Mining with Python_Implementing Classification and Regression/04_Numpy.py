import numpy as np

print(np.__version__)

int_array = np.array([2,3,4])
float_array = np.array([1.2,3.5,5.1])
int_array
float_array

print(int_array.dtype)
print(float_array.dtype)

print(np.zeros([2,4]))
print(np.ones([3,3]))

print(np.arange(1,10,2))

even_numbers = np.array([2,4,6,8,10])
odd_numbers = np.array([1,3,5,7,9])
print(even_numbers+odd_numbers)
print(even_numbers-odd_numbers)
print(even_numbers*odd_numbers)

matrix_1 = np.array([[1,1],[2,3]])
matrix_2 = np.array([[2,0],[1,6]])
print(matrix_1)
print(matrix_2)
matrix_multiplication = matrix_1.dot(matrix_2)
print(matrix_multiplication)

print(even_numbers.sum())
print(even_numbers.mean())