def predict(x, weight, bias):
    return weight * x + bias

def squared_loss(prediction, target):
    error = prediction - target
    return error * error

x = 3.0
target = 10

weight = 4.0
bias = 1.0

prediction = predict(x, weight, bias)
loss = squared_loss(prediction, target)

print("Prediction: ", prediction)
print("Loss:", loss)