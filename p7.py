import numpy as np

def print_triangular_matrices(matrix):
    """
    Prints lower and upper triangular matrices.

    Args:
        matrix (numpy.ndarray): Input matrix.
    """
    # Get the dimensions of the matrix
    rows, cols = matrix.shape

    # Print original matrix
    print("Original Matrix:")
    print(matrix)

    # Create lower triangular matrix
    lower_triangular = np.tril(matrix)

    # Print lower triangular matrix
    print("\nLower Triangular Matrix:")
    print(lower_triangular)

    # Create upper triangular matrix
    upper_triangular = np.triu(matrix)

    # Print upper triangular matrix
    print("\nUpper Triangular Matrix:")
    print(upper_triangular)


def main():
    # Get matrix dimensions from user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Check if matrix is square
    if rows != cols:
        print("Note: The input matrix is not square.")

    # Get matrix elements from user
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i, j] = float(input(f"Enter element [{i+1}][{j+1}]: "))

    # Print triangular matrices
    print_triangular_matrices(matrix)


if __name__ == "__main__":
    main()
