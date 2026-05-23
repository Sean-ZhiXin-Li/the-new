import numpy as np

def predict(features, weights, bias):
    return float(np.dot(features, weights) + bias)

def squared_loss(prediction, target):
    error = prediction - target
    return error * error

features = np.array([3.0, 2.0])
target = 10.0

weights = np.array([2.0, 1.0])
bias = 1.0

prediction = predict(features, weights, bias)
loss = squared_loss(prediction, target)

print("Prediction: ", prediction)
print("Loss:", loss)