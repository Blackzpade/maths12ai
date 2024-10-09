import numpy as np

def get_matrix_from_user(rows, cols):
    """Get matrix elements from user input."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Enter element [{i+1}][{j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        matrix.append(row)
    return np.array(matrix)

def scalar_matrix_multiplication(scalar, matrix):
    """Perform scalar matrix multiplication using NumPy."""
    result = scalar * matrix
    return result

def print_matrix(matrix):
    """Print the matrix in a readable format."""
    print(matrix)

def main():
    # Get matrix dimensions from user
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Matrix dimensions must be positive integers.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Get scalar value from user
    while True:
        try:
            scalar = float(input("Enter scalar value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get matrix elements from user
    matrix = get_matrix_from_user(rows, cols)

    # Perform scalar matrix multiplication
    result = scalar_matrix_multiplication(scalar, matrix)

    # Print the result
    print("Result of scalar matrix multiplication:")
    print_matrix(result)

if __name__ == "__main__":
    main()
