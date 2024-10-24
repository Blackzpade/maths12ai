import numpy as np

def main():
    # Input the size of the matrix
    n = int(input("Enter the size of the square matrix (n x n): "))

    # Choose to input matrix elements or generate a random matrix
    choice = input("Would you like to (1) input matrix elements or (2) generate a random matrix? Enter 1 or 2: ")

    # Initialize the matrix
    matrix = []

    if choice == '1':
        print("Enter the elements of the matrix row by row:")
        for i in range(n):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            matrix.append(row)
    elif choice == '2':
        # Generate a random matrix
        matrix = np.random.rand(n, n)  # Generates a random n x n matrix
        print(f"Generated random matrix:\n{matrix}")
    else:
        print("Invalid choice. Please run the program again.")
        return

    # Convert list to numpy array
    A = np.array(matrix)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Display the results without decimal points for whole numbers
    print("\nEigenvalues:")
    for val in eigenvalues:
        if val.is_integer():
            print(f"{int(val)}", end=" ")
        else:
            print(val, end=" ")
    print()  # New line for better formatting

    print("\nEigenvectors:")
    for vec in eigenvectors.T:  # Transpose to iterate over columns
        formatted_vec = ' '.join(f"{int(x)}" if x.is_integer() else f"{x}" for x in vec)
        print(f"[{formatted_vec}]")

if __name__ == "__main__":
    main()
