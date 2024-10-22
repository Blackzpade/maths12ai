import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine similarity between two vectors.

    Parameters:
    v1 (list or numpy array): The first vector.
    v2 (list or numpy array): The second vector.

    Returns:
    float: The cosine similarity between the two vectors.
    """
    # Convert the input vectors to numpy arrays
    v1 = np.array(v1)
    v2 = np.array(v2)

    # Calculate the dot product of the two vectors
    dot_product = np.dot(v1, v2)

    # Calculate the magnitudes of the two vectors
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    # Calculate the cosine similarity
    cosine_similarity = dot_product / (magnitude_v1 * magnitude_v2)

    return cosine_similarity

def get_vector_input(prompt):
    """
    Get vector input from the user.

    Parameters:
    prompt (str): The prompt to display to the user.

    Returns:
    list: A list of floats representing the vector.
    """
    user_input = input(prompt)
    # Convert the input string to a list of floats
    vector = list(map(float, user_input.split()))
    return vector

# Main program
if __name__ == "__main__":
    print("Enter the first vector (space-separated values):")
    v1 = get_vector_input("Vector 1: ")

    print("Enter the second vector (space-separated values):")
    v2 = get_vector_input("Vector 2: ")

    similarity = cosine_similarity(v1, v2)
    print("Cosine similarity:", similarity)
