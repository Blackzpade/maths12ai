import numpy as np

def create_matrix_of_zeros(input_matrix):
    """
    Returns a matrix of 0 with the same shape and type as the input matrix.

    Parameters:
    input_matrix (numpy array): The input matrix.

    Returns:
    numpy array: A matrix of 0 with the same shape and type as the input matrix.
    """
    return np.zeros_like(input_matrix)

# Get the input matrix from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

input_matrix = np.zeros((rows, cols))

print("Enter the elements of the matrix:")
for i in range(rows):
    for j in range(cols):
        input_matrix[i, j] = float(input(f"Element [{i+1}, {j+1}]: "))

# Create the result matrix
result_matrix = create_matrix_of_zeros(input_matrix)

# Print the input and result matrices
print("Input Matrix:")
print(input_matrix)
print("\nResult Matrix:")
print(result_matrix)
