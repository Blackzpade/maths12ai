import numpy as np

# Get matrix input from user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input("Enter row {} (space-separated): ".format(i+1)).split()))
    matrix.append(row)
matrix = np.array(matrix)

# Extract diagonal vector from matrix
diagonal_vector = np.diag(matrix)
print("Diagonal vector: ", diagonal_vector)

# Get vector input from user
vector_size = int(input("Enter the size of the vector: "))
vector = list(map(int, input("Enter the vector (space-separated): ").split()))
vector = np.array(vector)

# Create diagonal matrix from vector
diagonal_matrix = np.diag(vector)
print("Diagonal matrix: \n", diagonal_matrix)
