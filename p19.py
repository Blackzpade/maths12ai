
import numpy as np

# Get the range of random integers from the user
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Create two 3x3 arrays of random integers within the specified range
array1 = np.random.randint(min_value, max_value + 1, (3, 3))
array2 = np.random.randint(min_value, max_value + 1, (3, 3))

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)

# Perform matrix addition
addition_result = array1 + array2
print("Matrix Addition Result:")
print(addition_result)

# Perform matrix multiplication
multiplication_result = np.dot(array1, array2)
print("Matrix Multiplication Result:")
print(multiplication_result)

# Transpose of the product matrix
transpose_result = multiplication_result.T
print("Transpose of the Product Matrix:")
print(transpose_result)
