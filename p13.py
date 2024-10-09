import numpy as np

# Get the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty matrix
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Get the matrix elements from the user
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Enter element [{i+1}, {j+1}]: "))

# Print the accepted matrix
print("Accepted matrix:")
for row in matrix:
    print([int(x) if x.is_integer() else x for x in row])

# Convert the matrix to a NumPy array
matrix = np.array(matrix)

# Find the transpose of the matrix
transpose = matrix.T

# Print the transpose
print("Transpose of the matrix:")
for row in transpose:
    print([int(x) if x.is_integer() else x for x in row])
