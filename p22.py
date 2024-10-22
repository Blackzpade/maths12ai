import numpy as np

def calculate_vector_norm():
    vector = input("Enter the vector elements separated by space: ")
    vector = list(map(float, vector.split()))
    vector = np.array(vector)

    norm_type = input("Enter the type of norm (1 for L1, 2 for L2, 'inf' for infinity norm): ")

    if norm_type == '1':
        norm = np.linalg.norm(vector, 1)
        print("L1 Norm: ", norm)
    elif norm_type == '2':
        norm = np.linalg.norm(vector)
        print("L2 Norm: ", norm)
    elif norm_type == 'inf':
        norm = np.linalg.norm(vector, np.inf)
        print("Infinity Norm: ", norm)
    else:
        print("Invalid norm type. Please enter 1, 2, or 'inf'.")

calculate_vector_norm()
