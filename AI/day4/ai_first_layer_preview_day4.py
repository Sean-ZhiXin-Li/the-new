import numpy as np

def first_layer(feature_matrix, weight_matrix, bias_vector):
    return feature_matrix @ weight_matrix + bias_vector

feature_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])

weight_matrix = np.array([
    [2.0, -1.0, 0.5],
    [1.0, 3.0, 2.0],
])

bias_vector = np.array([1.0, 0.0, -1.0])

outputs = first_layer(feature_matrix, weight_matrix, bias_vector)

print("feature matrix shape: ", feature_matrix.shape)
print("Weight matrix shape: ", weight_matrix.shape)
print("Output shape: ", outputs.shape)
print("Outputs: ", outputs)