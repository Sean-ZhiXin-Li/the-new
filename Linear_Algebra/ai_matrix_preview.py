import numpy as np

basis_matrix = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
])

target = np.array([3.0, 4.0])

coefficients = np.linalg.solve(basis_matrix, target)

print("Coefficients: ", coefficients)
print("Reconstructed: ", basis_matrix @ coefficients)

