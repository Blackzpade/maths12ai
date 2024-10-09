import numpy as np

def get_matrix(prompt):
    rows = int(input(prompt + " number of rows: "))
    cols = int(input(prompt + " number of columns: "))
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        row = input(prompt + " row {} (space-separated values): ".format(i+1)).split()
        matrix[i] = [float(x) for x in row]
    return matrix

def main():
    print("Matrix Addition and Subtraction")
    matrix1 = get_matrix("Matrix 1")
    matrix2 = get_matrix("Matrix 2")

    if matrix1.shape != matrix2.shape:
        print("Error: Matrices must have the same dimensions for addition and subtraction.")
        return

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    add_result = np.add(matrix1, matrix2)
    subtract_result = np.subtract(matrix1, matrix2)

    print("Matrix 1 + Matrix 2:")
    print(add_result)
    print("Matrix 1 - Matrix 2:")
    print(subtract_result)

if __name__ == "__main__":
    main()
