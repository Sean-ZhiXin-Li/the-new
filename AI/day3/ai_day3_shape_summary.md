# AI Day 3 — Shape Summary

## Objective

Upgrade from:

```text
single sample → single prediction
```

to:

```text
batch samples → prediction vector
```

Core goal:

```text
dot product → matrix multiplication
feature vector → feature matrix
```

---

# 1. Core Code Structure

```python
feature_matrix = np.array([
    [3.0, 2.0],
    [1.0, 4.0],
    [5.0, 1.0],
])

weights = np.array([
    2.0,
    1.0,
])

bias = 1.0

predictions = feature_matrix @ weights + bias
```

---

# 2. Shape Audit

## Feature Matrix

```text
Shape: (3, 2)
```

Meaning:

```text
3 rows = 3 samples
2 columns = 2 features per sample
```

Detailed:

```text
Sample 1 → [3,2]
Sample 2 → [1,4]
Sample 3 → [5,1]
```

---

## Weights

```text
Shape: (2,)
```

Meaning:

```text
2 feature weights
One weight per feature
```

Detailed:

```text
Weight for feature 1 = 2
Weight for feature 2 = 1
```

---

# 3. Matrix Multiplication Rule

```text
(3,2) @ (2,) → (3,)
```

Why valid:

```text
Inner dimensions match:
2 == 2
```

Meaning:

```text
Each row performs one dot product with weights.
```

So:

```text
3 samples → 3 predictions
```

---

# 4. Prediction Breakdown

## Sample 1

```text
[3,2] · [2,1] + 1
= 3×2 + 2×1 +1
= 9
```

---

## Sample 2

```text
[1,4] · [2,1] +1
= 1×2 +4×1 +1
= 7
```

---

## Sample 3

```text
[5,1] · [2,1] +1
= 5×2 +1×1 +1
= 12
```

---

## Final Prediction Vector

```text
[9, 7, 12]
```

Shape:

```text
(3,)
```

Meaning:

```text
One prediction per sample
```

---

# 5. Loss Structure

If:

```text
target = 10
```

Then:

```text
Loss = (prediction - target)^2
```

Results:

```text
(9-10)^2 = 1
(7-10)^2 = 9
(12-10)^2 = 4
```

Loss Vector:

```text
[1, 9, 4]
```

Shape:

```text
(3,)
```

---

# 6. Structural Upgrade

## Day 2

```text
One feature vector
→ one dot product
→ one prediction
→ one loss
```

---

## Day 3

```text
Feature matrix
→ many dot products simultaneously
→ prediction vector
→ loss vector
```

---

# 7. Core Mental Model

```text
Rows = samples
Columns = features
Weights = feature importance
Bias = global offset
```

So:

```text
feature_matrix @ weights
```

means:

```text
Apply the same model to every sample simultaneously.
```

---

# 8. Why This Matters for AI

Today:

```text
Linear batch prediction
```

Later:

```text
X @ W + b
```

This becomes:

## Neural Network Layer

```text
input_batch @ weight_matrix + bias_vector
```

---

# 9. Spacecraft / PPO Preview

Future observation example:

```text
[r_error, vr, vt, fuel, angle]
```

One spacecraft state:

```text
feature vector
```

Many spacecraft states:

```text
feature matrix
```

So today’s concept directly scales into:

```text
batch policy evaluation
```

---

# 10. Common Failure Modes

## Bug 1

```text
Wrong dimensions
Example:
(3,2) @ (3,)
→ invalid
```

---

## Bug 2

```text
Confusing rows and columns
```

---

## Bug 3

```text
Using float() on batch output
```

---

## Bug 4

```text
Variable mismatch:
features vs feature_matrix
```

---

# 11. Day 3 Final Summary

```text
Single sample:
prediction = dot(features, weights) + bias
```

```text
Batch:
predictions = feature_matrix @ weights + bias
```

Key upgrade:

```text
One prediction → many predictions
```

---

# 12. One-Sentence Memory Rule

```text
A feature matrix is many feature vectors stacked together.
```

Even shorter:

```text
Rows = samples, columns = features.
```

---

# 13. Today’s Win Condition

```text
I understand:
Matrix multiplication here is many dot products at once.
```

Not:

```text
I only know how to run NumPy code.
```

---

# Deliverable Status

```text
ai_matrix_preview_day3.py ✅
ai_day3_shape_summary.md ✅
AI Day 3 Complete ✅
```
