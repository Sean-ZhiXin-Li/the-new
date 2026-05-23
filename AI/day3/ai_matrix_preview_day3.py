import numpy as np

def predict_branch(features_matrix, weights, bias):
    return features_matrix @ weights + bias

def squared_loss(prediction, target):
    error = prediction - target
    return error * error

features_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])

target = 10.0

weights = np.array([
    2.0,
    1.0,
])

bias = 1.0

prediction = predict_branch(features_matrix, weights, bias)

print("Feature: ")
print(features_matrix)

print("weight: ")
print(weights)

print("Bias: ")
print(bias)
print()
loss = squared_loss(prediction, target)

print("Prediction: ", prediction)
print("Loss:", loss)