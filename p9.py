import numpy as np

# Get the size of the matrix from the user
n = int(input("Enter the size of the identity matrix: "))

# Create the identity matrix using NumPy
identity_matrix = np.eye(n)

# Print the identity matrix
print("The identity matrix of size {}x{} is:".format(n, n))
print(identity_matrix)
