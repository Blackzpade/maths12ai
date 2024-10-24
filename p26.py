import numpy as np

def check_vector_space(vectors, scalar):
    # Convert list of vectors to numpy array for easier manipulation
    vectors = np.array(vectors)

    # Check closure under addition
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            sum_vector = vectors[i] + vectors[j]
            if not any(np.array_equal(sum_vector, vec) for vec in vectors):
                print(f"Closure under addition failed for {vectors[i]} + {vectors[j]} = {sum_vector}")
                return False

    # Check closure under scalar multiplication
    for vector in vectors:
        scaled_vector = scalar * vector
        if not any(np.array_equal(scaled_vector, vec) for vec in vectors):
            print(f"Closure under scalar multiplication failed for {scalar} * {vector} = {scaled_vector}")
            return False

    print("The set of vectors satisfies closure under addition and scalar multiplication.")
    return True

# User input
num_vectors = int(input("Enter the number of vectors: "))
vectors = []
for _ in range(num_vectors):
    vector = list(map(float, input("Enter vector components separated by space: ").split()))
    vectors.append(vector)

scalar = float(input("Enter a scalar value: "))

# Check vector space properties
check_vector_space(vectors, scalar)
