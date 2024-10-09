import numpy as np

def get_matrix_from_user():
    """
    Get matrix from user input
    """
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i+1} values (separated by space): ")
        row = list(map(float, row.split()))
        matrix.append(row)

    return np.array(matrix)

def find_rank(matrix):
    """
    Find the rank of a matrix using numpy
    """
    return np.linalg.matrix_rank(matrix)

# Get matrix from user
matrix = get_matrix_from_user()

# Find and print the rank of the matrix
rank = find_rank(matrix)
print(f"The rank of the matrix is: {rank}")
