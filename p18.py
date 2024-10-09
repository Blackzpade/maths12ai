import numpy as np

# Get the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create a matrix with zeros
matrix = np.zeros((rows, cols))

# Get the matrix values from the user
print("Enter the matrix values:")
for i in range(rows):
    for j in range(cols):
        matrix[i, j] = float(input(f"Enter value for row {i+1}, column {j+1}: "))

# Calculate the sparsity of the matrix
non_zero_elements = np.count_nonzero(matrix)
total_elements = rows * cols
sparsity = 1 - (non_zero_elements / total_elements)

# Print the sparsity
print(f"The sparsity of the matrix is: {sparsity:.4f}")
