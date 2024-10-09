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

# Print the input matrix
print("Input Matrix:")
print(matrix)

# Check if the matrix is square (i.e., has the same number of rows and columns)
if rows != cols:
    print("Error: Matrix must be square to find its trace.")
else:
    # Calculate the trace of the matrix using NumPy's `trace` function
    trace = np.trace(matrix)

    # Print the trace
    print("Trace of the Matrix:")
    print(trace)
