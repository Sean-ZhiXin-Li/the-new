import numpy as np


def check_rank(vector_matrix, case_name):
    rank = np.linalg.matrix_rank(vector_matrix)

    print("=" * 50)
    print(case_name)
    print("Matrix:")
    print(vector_matrix)
    print("Matrix shape:", vector_matrix.shape)
    print("Rank:", rank)
    print()


# Case A:
# v1 = (1, 0), v2 = (0, 1)
# These two vectors span R2.
case_a = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
])

# Case B:
# v1 = (1, 2), v2 = (2, 4)
# v2 = 2 * v1, so they only span one line.
case_b = np.array([
    [1.0, 2.0],
    [2.0, 4.0],
])

# Case C:
# v1 = (1, 0), v2 = (0, 1), v3 = (1, 1)
# v3 = v1 + v2, so v3 is redundant.
case_c = np.array([
    [1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0],
])

check_rank(case_a, "Case A: Standard basis in R2")
print("Meaning: rank 2 means these vectors span R2.")
print()

check_rank(case_b, "Case B: Redundant direction")
print("Meaning: rank 1 means these vectors only span a line, not R2.")
print()

check_rank(case_c, "Case C: Span R2 with one redundant vector")
print("Meaning: rank 2 with 3 vectors means one vector is redundant.")
print()

print("=" * 50)
print("Day4 Summary")
print("Span asks: can these vectors reach the full space?")
print("Basis asks: can we remove redundant vectors and still reach the same space?")
print("Rank means: number of independent directions.")