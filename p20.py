import numpy as np

def get_matrix_from_user():
    """
    Get matrix dimensions and elements from user input.
    """
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element [{i+1}][{j+1}]: ")))
        matrix.append(row)

    return np.array(matrix)

def to_echelon_form(matrix):
    """
    Transform the matrix to its echelon form using Gaussian elimination.
    """
    num_rows, num_cols = matrix.shape
    current_row = 0

    for j in range(num_cols):
        if current_row >= num_rows:
            break

        pivot_row = current_row
        while pivot_row < num_rows and matrix[pivot_row, j] == 0:
            pivot_row += 1

        if pivot_row == num_rows:
            continue

        # Swap current row with pivot row
        matrix[[current_row, pivot_row]] = matrix[[pivot_row, current_row]]

        # Make pivot element equal to 1
        pivot = matrix[current_row, j]
        matrix[current_row] = matrix[current_row] / pivot

        # Eliminate pivot variable from other rows
        for i in range(num_rows):
            if i != current_row:
                factor = matrix[i, j]
                matrix[i] = matrix[i] - factor * matrix[current_row]

        current_row += 1

    return matrix

def calculate_rank(matrix):
    """
    Calculate the rank of the matrix by counting the number of non-zero rows.
    """
    rank = 0
    for row in matrix:
        if any(element != 0 for element in row):
            rank += 1
    return rank

def main():
    matrix = get_matrix_from_user()
    print("Original Matrix:")
    print(np.array2string(matrix, formatter={'float_kind': lambda x: "%.0f" % x}))

    echelon_form = to_echelon_form(matrix.copy())
    print("\nEchelon Form:")
    print(np.array2string(echelon_form, formatter={'float_kind': lambda x: "%.0f" % x}))

    rank = calculate_rank(echelon_form)
    print(f"\nRank: {rank}")

if __name__ == "__main__":
    main()
