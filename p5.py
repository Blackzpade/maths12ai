import numpy as np

def matrix_multiplication():
    # Get the dimensions of the matrices from the user
    rows_A = int(input("Enter the number of rows for matrix A: "))
    cols_A = int(input("Enter the number of columns for matrix A: "))
    rows_B = int(input("Enter the number of rows for matrix B: "))
    cols_B = int(input("Enter the number of columns for matrix B: "))

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        print("Error: Matrices cannot be multiplied")
        return

    # Get the elements of the matrices from the user
    A = np.zeros((rows_A, cols_A))
    B = np.zeros((rows_B, cols_B))

    print("Enter elements of matrix A:")
    for i in range(rows_A):
        for j in range(cols_A):
            A[i, j] = float(input(f"Enter element ({i+1}, {j+1}): "))

    print("Enter elements of matrix B:")
    for i in range(rows_B):
        for j in range(cols_B):
            B[i, j] = float(input(f"Enter element ({i+1}, {j+1}): "))

    # Perform matrix multiplication
    C = np.dot(A, B)

    # Print the result
    print("Result of matrix multiplication:")
    print(C)

matrix_multiplication()
