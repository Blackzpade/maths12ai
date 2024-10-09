import numpy as np

# Get the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create a matrix with user-input values
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = float(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(val)
    matrix.append(row)

# Convert the matrix to a NumPy array
matrix = np.array(matrix)

# Check if the matrix is square (i.e., has the same number of rows and columns)
if rows != cols:
    print("Error: Matrix must be square to find its inverse.")
else:
    # Calculate the inverse of the matrix using NumPy's `linalg.inv` function
    inverse_matrix = np.linalg.inv(matrix)

    # Print the inverse matrix
    print("Inverse Matrix:")
    print(inverse_matrix)
