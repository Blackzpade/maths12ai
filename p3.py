import numpy as np

def hadamard_product(A, B):
    """
    Calculate the Hadamard product of two matrices A and B.

    Parameters:
    A (numpy.ndarray): The first matrix.
    B (numpy.ndarray): The second matrix.

    Returns:
    numpy.ndarray: The Hadamard product of A and B.
    """
    # Check if the input matrices have the same dimensions
    assert A.shape == B.shape, "Input matrices must have the same dimensions"

    # Calculate the Hadamard product using the * operator
    return A * B

# Get user input for matrices A and B
rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))

rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

# Check if the input matrices have the same dimensions
assert rows_A == rows_B and cols_A == cols_B, "Input matrices must have the same dimensions"

A = np.zeros((rows_A, cols_A))
B = np.zeros((rows_B, cols_B))

print("Enter elements for matrix A:")
for i in range(rows_A):
    A[i] = list(map(int, input().split()))

print("Enter elements for matrix B:")
for i in range(rows_B):
    B[i] = list(map(int, input().split()))

result = hadamard_product(A, B)
print("The Hadamard product of A and B is:")
print(result)
