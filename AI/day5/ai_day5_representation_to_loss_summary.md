# Phase0 Day5 — AI Representation → Prediction → Loss

# Core Goal

Today is NOT:

```text
training AI
```

Today IS:

```text
understanding the minimal AI pipeline
```

Core chain:

```text
representation
→ transformation
→ prediction
→ evaluation
```

This is the mathematical backbone of:

```text
neural networks
control systems
reinforcement learning
OrbitEnv policies
```

---

# 1. Full Code

```python
import numpy as np


def linear_layer(feature_matrix, weight_matrix, bias_vector):
    return feature_matrix @ weight_matrix + bias_vector



def mean_squared_error(predictions, targets):
    errors = predictions - targets
    return np.mean(errors ** 2)


feature_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])

weight_matrix = np.array([
    [2.0, -1.0],
    [1.0,  3.0],
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
```

---

# 2. Step-by-Step Computation

# Step 1 — Feature Matrix

```python
feature_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])
```

Shape:

```text
(3, 2)
```

Meaning:

```text
3 samples
2 features per sample
```

Table form:

| Sample | Feature 1 | Feature 2 |
| ------ | --------- | --------- |
| 1      | 3         | 2         |
| 2      | 1         | 4         |
| 3      | 5         | 1         |

Core meaning:

```text
feature_matrix = state representation
```

Examples in real systems:

```text
robot state
OrbitEnv observation
sensor data
AI feature vector
velocity vector
```

---

# Step 2 — Weight Matrix

```python
weight_matrix = np.array([
    [2.0, -1.0],
    [1.0,  3.0],
])
```

Shape:

```text
(2, 2)
```

Meaning:

```text
transformation rule
```

Important Day5 idea:

```text
matrix = transformation
```

The model applies a transformation to the input representation.

---

# Step 3 — Matrix Multiplication

```python
feature_matrix @ weight_matrix
```

Shape calculation:

```text
(3,2) @ (2,2)
→ (3,2)
```

Reason:

```text
left columns = right rows
2 = 2
```

Valid matrix multiplication.

---

# Step 4 — Manual Matrix Multiplication

# First Row

Input vector:

```text
[3,2]
```

Transformation:

```text
[[ 2, -1],
 [ 1,  3]]
```

First output dimension:

```text
3*2 + 2*1
= 6 + 2
= 8
```

Second output dimension:

```text
3*(-1) + 2*3
= -3 + 6
= 3
```

Result:

```text
[3,2]
→
[8,3]
```

---

# Second Row

Input:

```text
[1,4]
```

First output dimension:

```text
1*2 + 4*1
= 2 + 4
= 6
```

Second output dimension:

```text
1*(-1) + 4*3
= -1 + 12
= 11
```

Result:

```text
[1,4]
→
[6,11]
```

---

# Third Row

Input:

```text
[5,1]
```

First output dimension:

```text
5*2 + 1*1
= 10 + 1
= 11
```

Second output dimension:

```text
5*(-1) + 1*3
= -5 + 3
= -2
```

Result:

```text
[5,1]
→
[11,-2]
```

---

# Step 5 — Matrix Multiplication Result

```text
feature_matrix @ weight_matrix
=
[
 [ 8,  3],
 [ 6, 11],
 [11, -2]
]
```

This is:

```text
transformed representation
```

---

# Step 6 — Bias Vector

```python
bias_vector = np.array([1.0, -1.0])
```

Shape:

```text
(2,)
```

The code:

```python
feature_matrix @ weight_matrix + bias_vector
```

uses broadcasting.

Meaning:

```text
add [1,-1] to every row
```

---

# Step 7 — Add Bias

First row:

```text
[8,3] + [1,-1]
=
[9,2]
```

Second row:

```text
[6,11] + [1,-1]
=
[7,10]
```

Third row:

```text
[11,-2] + [1,-1]
=
[12,-3]
```

Final predictions:

```text
predictions =
[
 [ 9,  2],
 [ 7, 10],
 [12, -3]
]
```

---

# Step 8 — Target Matrix

```python
target_matrix = np.array([
    [9.0, 1.0],
    [7.0, 10.0],
    [12.0, -2.0],
])
```

Meaning:

```text
ground truth
correct answers
```

Important distinction:

```text
prediction != target
```

Predictions are:

```text
model guesses
```

Targets are:

```text
correct answers
```

---

# Step 9 — Prediction Error

```python
errors = predictions - targets
```

Computation:

```text
[
 [ 9-9,   2-1 ],
 [ 7-7, 10-10],
 [12-12, -3-(-2)]
]
```

Result:

```text
errors =
[
 [0,  1],
 [0,  0],
 [0, -1]
]
```

Meaning:

```text
prediction error
```

---

# Step 10 — Square Error

```python
errors ** 2
```

Result:

```text
[
 [0,1],
 [0,0],
 [0,1]
]
```

Why square?

Because:

```text
positive and negative errors should not cancel out
```

Example:

```text
-2 and +2
```

Both become:

```text
4
```

---

# Step 11 — Mean Squared Error

Total sum:

```text
0 + 1 + 0 + 0 + 0 + 1
= 2
```

Total number of elements:

```text
6
```

Loss:

```text
2 / 6
=
0.3333333333333333
```

Final result:

```text
Loss = 0.3333333333333333
```

---

# 12. Most Important Day5 AI Insight

Today is NOT:

```text
training AI
```

Today IS:

```text
understanding the AI computation chain
```

The chain is:

```text
feature representation
→ matrix transformation
→ predictions
→ error
→ loss evaluation
```

This is the mathematical backbone of:

```text
neural networks
control systems
reinforcement learning
OrbitEnv policies
```

---

# 13. Reflection Questions

## Q1

```text
Do I still think matrices are only tables of numbers?
```

Correct understanding:

```text
Matrices are transformation rules.
```

---

## Q2

```text
Do I understand what Wx+b means?
```

Correct understanding:

```text
representation transformation + offset
```

---

## Q3

```text
Do I understand what loss is?
```

Correct understanding:

```text
Loss is a scalar evaluation of prediction quality.
```

---

## Q4

```text
Do I confuse prediction with target?
```

Correct understanding:

```text
prediction = model output
target = ground truth
```

---

# 14. Final Summary

The most important sentence today is:

```text
AI models transform representations and evaluate prediction quality.
```

Or more structurally:

```text
representation
→ transformation
→ prediction
→ evaluation
```

This is the foundation for:

```text
gradient
optimizer
backpropagation
PyTorch
PPO
```

which come later.
