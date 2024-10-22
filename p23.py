import numpy as np

def calculate_dot_product():
    # Get the dimensions of the vectors from the user
    dimensions = int(input("Enter the number of dimensions for the vectors: "))

    # Get the components of the first vector from the user
    print("Enter the components of the first vector:")
    u = []
    for i in range(dimensions):
        component = float(input(f"Component {i+1}: "))
        u.append(component)

    # Get the components of the second vector from the user
    print("Enter the components of the second vector:")
    v = []
    for i in range(dimensions):
        component = float(input(f"Component {i+1}: "))
        v.append(component)

    # Convert the lists to NumPy arrays
    u = np.array(u)
    v = np.array(v)

    # Calculate the dot product
    dot_product = np.dot(u, v)

    # Print the result
    print(f"The dot product of the two vectors is: {dot_product}")

    # Check if the vectors are orthogonal
    if dot_product == 0:
        print("The vectors are orthogonal.")
    else:
        print("The vectors are not orthogonal.")

calculate_dot_product()
