import numpy as np

def create_matrix(rows, cols):
    matrix = np.ones((rows, cols), dtype=int)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = create_matrix(rows, cols)
print(matrix)
