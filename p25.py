import numpy as np

def add(v1, v2):
    return v1 + v2

def scalar_multiply(scalar, v):
    return scalar * v

def check_axioms(vectors, zero_vector):
    vectors = [np.array(v) for v in vectors]
    zero_vector = np.array(zero_vector)

    # 1. Closure under Addition
    for v1 in vectors:
        for v2 in vectors:
            if not any(np.array_equal(add(v1, v2), v) for v in vectors):
                return False, "Closure under Addition failed."

    # 2. Closure under Scalar Multiplication
    for v in vectors:
        for scalar in range(-10, 11):  # Example scalars from -10 to 10
            if not any(np.array_equal(scalar_multiply(scalar, v), sv) for sv in vectors):
                return False, "Closure under Scalar Multiplication failed."

    # 3. Associativity of Addition
    for v1 in vectors:
        for v2 in vectors:
            for v3 in vectors:
                if not np.array_equal(add(v1, add(v2, v3)), add(add(v1, v2), v3)):
                    return False, "Associativity of Addition failed."

    # 4. Commutativity of Addition
    for v1 in vectors:
        for v2 in vectors:
            if not np.array_equal(add(v1, v2), add(v2, v1)):
                return False, "Commutativity of Addition failed."

    # 5. Identity Element of Addition
    for v in vectors:
        if not np.array_equal(add(v, zero_vector), v):
            return False, "Identity Element of Addition failed."

    # 6. Inverse Elements of Addition
    for v in vectors:
        if not any(np.array_equal(add(v, -v), zero_vector) for v in vectors):
            return False, "Inverse Elements of Addition failed."

    # 7. Distributive Property
    for v1 in vectors:
        for v2 in vectors:
            for scalar in range(-10, 11):
                if not np.array_equal(scalar_multiply(scalar, add(v1, v2)), add(scalar_multiply(scalar, v1), scalar_multiply(scalar, v2))):
                    return False, "Distributive Property failed."

    # 8. Compatibility of Scalar Multiplication
    for scalar1 in range(-10, 11):
        for scalar2 in range(-10, 11):
            for v in vectors:
                if not np.array_equal(scalar_multiply(scalar1, scalar_multiply(scalar2, v)), scalar_multiply(scalar1 * scalar2, v)):
                    return False, "Compatibility of Scalar Multiplication failed."

    # 9. Identity Element of Scalar Multiplication
    for v in vectors:
        if not np.array_equal(scalar_multiply(1, v), v):
            return False, "Identity Element of Scalar Multiplication failed."

    return True, "The set satisfies all vector space axioms."

def get_vectors_from_user():
    vectors = []
    print("Enter the vectors (comma-separated) or type 'done' to finish:")
    while True:
        user_input = input("Vector: ")
        if user_input.lower() == 'done':
            break
        try:
            vector = tuple(map(int, user_input.split(',')))
            vectors.append(vector)
        except ValueError:
            print("Invalid input. Please enter a comma-separated list of integers.")

    zero_vector_input = input("Enter the zero vector (comma-separated): ")
    zero_vector = tuple(map(int, zero_vector_input.split(',')))

    return vectors, zero_vector

def main():
    while True:
        print("\nOptions:")
        print("1. Check vector space axioms")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            user_vectors, zero_vector = get_vectors_from_user()
            is_vector_space, message = check_axioms(user_vectors, zero_vector)
            print(message)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

# Main execution
if __name__ == "__main__":
    main()
