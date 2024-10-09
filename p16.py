import numpy as np

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Get the number of columns from the user
cols = int(input("Enter the number of columns: "))

# Create an empty matrix
matrix = []

# Get the matrix values from the user
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("Enter value for row {} column {}: ".format(i+1, j+1)))
        row.append(val)
    matrix.append(row)

# Print the input matrix
print("The input matrix is:")
for row in matrix:
    print(row)

# Convert the matrix to a NumPy array
matrix = np.array(matrix)

# Calculate and print the determinant
determinant = np.linalg.det(matrix)
print("The determinant of the matrix is: ", int(determinant))
