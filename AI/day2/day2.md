# Phase 0 Day 2 — AI Bug Log

## Module

```text
Vectorized Prediction Model
prediction = dot(features, weights) + bias
```

---

# Core Objective

Build first-principles understanding of:

```text
features
weights
bias
dot product
prediction
loss
```

This is not “training” yet.

This phase is:

```text
understand forward pass
```

---

# Initial Bugs

## Bug 1 — Wrong NumPy Array Syntax

### Wrong:

```python
weights = np.array[(2.0, 1.0)]
```

### Correct:

```python
weights = np.array([2.0, 1.0])
```

### Why:

```text
np.array() is a function call.
It requires parentheses containing a list.
```

### Lesson:

```text
Use [] for vector contents.
Use () for function call.
```

---

# Bug 2 — Did Not Understand np.dot()

## Confusion:

```text
What does dot actually do?
```

## Reality:

```text
dot = corresponding multiply + sum
```

## Example:

```text
[3,2] · [2,1]
= 3×2 + 2×1
= 6 + 2
= 8
```

### Lesson:

```text
dot product = weighted sum of features
```

---

# Bug 3 — Did Not Understand Bias

## Confusion:

```text
Why + bias?
```

## Reality:

```text
bias shifts prediction globally
```

## Example:

```text
Without bias:
8

With bias = 1:
9
```

### Lesson:

```text
bias = baseline adjustment
```

---

# Bug 4 — Did Not Understand Prediction Flow

## Full Flow:

```text
features
→ dot(weights)
→ + bias
→ prediction
```

## Actual Values:

```text
features = [3,2]
weights = [2,1]
bias = 1

prediction:
(3×2 + 2×1) + 1
= 9
```

### Lesson:

```text
Prediction = model output
```

---

# Bug 5 — Did Not Understand Loss

## Confusion:

```text
Why compare with target?
```

## Reality:

```text
Loss measures prediction quality
```

## Formula:

```text
error = prediction - target
loss = error²
```

## Example:

```text
target = 10
prediction = 9

error = -1
loss = 1
```

### Lesson:

```text
Lower loss = better prediction
```

---

# Bug 6 — Why Square the Error?

## Reason:

```text
1. Prevent negative and positive errors from canceling
2. Penalize larger mistakes more strongly
```

## Example:

```text
error = -3
loss = 9
```

### Lesson:

```text
Squared loss amplifies mistakes
```

---

# Engineering Lessons

## 1. features

```text
Input state / signal
```

---

## 2. weights

```text
Importance of each feature
```

---

## 3. bias

```text
Global offset
```

---

## 4. prediction

```text
Model guess
```

---

## 5. loss

```text
How wrong the guess is
```

---

# Mathematical Upgrade

## Day 1:

```text
y = wx + b
```

## Day 2:

```text
y = dot(features, weights) + b
```

---

# Spacecraft / Control Connection

Future state:

```text
[x, y, vx, vy, vr]
```

Possible controller scoring:

```text
score = dot(state, weights) + bias
```

### Meaning:

```text
State evaluation
Danger scoring
Control priority
Decision systems
```

---

# Common Bugs to Watch Next

```text
1. Shape mismatch
2. Wrong vector length
3. Missing float conversion
4. Wrong target value
5. Poor weight choice
```

---

# Day 2 Win Condition

```text
✔ Can explain np.array syntax
✔ Can explain dot product
✔ Can explain weights
✔ Can explain bias
✔ Can explain prediction
✔ Can explain squared loss
✔ Can manually compute full example
```

---

# One-Sentence Summary

```text
This model combines multiple weighted inputs into one prediction, then uses squared loss to mea
```
