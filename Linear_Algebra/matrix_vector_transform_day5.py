import numpy as np

transform_matrix = np.array([
    [2.0, 0.0],
    [0.0, 3.0],
])

vector = np.array([1.0, 2.0])

transformed_vector = transform_matrix @ vector

print("Matrix: ", transform_matrix)

print("\nOriginal vector: ", vector)

print("\nTransformed vector: ", transformed_vector)