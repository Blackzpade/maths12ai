import numpy as np

def main():
    # Input the size of the matrix
    n = int(input("Enter the size of the square matrix (n x n): "))

    # Initialize the matrix
    matrix = []

    print("Enter the elements of the matrix row by row:")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    # Convert list to numpy array
    A = np.array(matrix)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Display the results
    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors:")
    print(eigenvectors)

if __name__ == "__main__":
    main()

