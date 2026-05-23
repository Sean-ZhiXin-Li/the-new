import numpy as np

def linear_layer(feature_matrix, weight_matrix, bias_vector):
    return feature_matrix @ weight_matrix + bias_vector

def mean_squared_error(predictions, target):
    error = predictions - target
    return np.mean(error ** 2)

feature_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])

weight_matrix = np.array([
    [2.0, -1.0],
    [1.0, 3.0],
])

bias_vector = np.array([1.0, -1.0])

target_matrix = np.array([
    [9.0, 1.0],
    [7.0, 10.0],
    [12.0, -2.0],
])

predictions = linear_layer(feature_matrix, weight_matrix, bias_vector)
loss = mean_squared_error(predictions, target_matrix)

print("Feature matrix shape:", feature_matrix.shape)
print("Weight matrix shape:", weight_matrix.shape)
print("Prediction shape:", predictions.shape)
print("Target shape:", target_matrix.shape)
print("Predictions:")
print(predictions)
print("Loss:", loss)

