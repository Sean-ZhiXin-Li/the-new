# Phase0 Day6 — AI Selection, Ranking, and Tensor Introduction

## Core Objective

Today is NOT:

```text
training AI
```

Today IS:

```text
understanding how AI selects actions
```

Core chain:

```text
score
→ ranking
→ selection
→ action
```

This is the foundation for:

```text
policy networks
reinforcement learning
PPO
controller decision systems
```

---

# 1. Previous Knowledge Chain

## Day1

```text
function approximation

y = f(x; θ)
```

---

## Day2

```text
features
→ weights
→ prediction
→ loss
```

---

## Day3

```text
feature matrix
→ batch prediction
```

---

## Day4

```text
matrix transformation
→ new representation
```

---

## Day5

```text
representation
→ transformation
→ prediction
→ evaluation
```

---

## Day6

```text
evaluation score
→ ranking
→ selection
```

---

# 2. First Tensor

Code:

```python
scores = torch.tensor([0.2, 0.8, 0.5])
```

Meaning:

```text
Action 0 → 0.2
Action 1 → 0.8
Action 2 → 0.5
```

Tensor interpretation:

```text
tensor = AI computation container
```

Current tensor shape:

```text
(3,)
```

Meaning:

```text
3 scores
```

---

# 3. What Is argmax?

Code:

```python
torch.argmax(scores)
```

Question:

```text
Which position contains the largest value?
```

Table:

| Index | Score |
|---------|---------|
| 0 | 0.2 |
| 1 | 0.8 |
| 2 | 0.5 |

Largest value:

```text
0.8
```

Position:

```text
1
```

Result:

```python
tensor(1)
```

Meaning:

```text
Select Action 1
```

---

# 4. Understanding argmax

Important distinction:

```text
max
=
largest value
```

Example:

```text
max(scores)
=
0.8
```

---

```text
argmax
=
location of largest value
```

Example:

```text
argmax(scores)
=
1
```

Memory rule:

```text
max = how large?

argmax = where?
```

---

# 5. First Action Selection

Code:

```python
best_action = torch.argmax(scores)
```

Meaning:

```text
Compare all candidate actions

Find highest score

Select corresponding action
```

Pipeline:

```text
scores
→ comparison
→ ranking
→ selection
```

---

# 6. Tensor vs List

Initial bug:

```python
scores = [0.2, 0.8, 0.5]
```

Error:

```text
argmax() must receive a Tensor
```

Reason:

```text
Python list
≠
PyTorch tensor
```

Correct:

```python
scores = torch.tensor([0.2, 0.8, 0.5])
```

Lesson:

```text
AI systems operate on tensors.
```

---

# 7. Day6 Bug Log

## Bug 1 — Tensor Required

### Problem

```text
TypeError:
argmax() must be Tensor, not list
```

### Cause

Input was:

```python
[0.2, 0.8, 0.5]
```

which is a Python list.

### Fix

Convert to:

```python
torch.tensor([0.2, 0.8, 0.5])
```

### Lesson

PyTorch functions expect tensor inputs.

---

# 8. MIT 6.S191 Connection

Today only browsed:

```text
Deep Learning Intro
```

Main realization:

```text
Input
→ Model
→ Prediction
→ Loss
→ Training
```

This matches:

```text
Day1–Day5 AI chain
```

Current stage:

```text
Before training
```

Not yet learning:

```text
Gradient Descent
Backpropagation
Optimizers
PPO
```

---

# 9. Spacecraft Connection

Future policy:

```text
Observation
→ Action Scores
→ argmax
→ Selected Action
```

Example:

```text
coast      0.2
radial_in  0.8
radial_out 0.5
```

Selection:

```text
radial_in
```

because:

```text
0.8 is highest
```

---

# 10. Core Mental Model

Today is not:

```text
training
```

Today is:

```text
scoring candidates
→ comparing candidates
→ selecting an action
```

---

# Day6 Final Summary

The most important sentence today is:

```text
AI decision-making can be viewed as scoring candidates, ranking them, and selecting the best action.
```

Or structurally:

```text
tensor
→ scores
→ ranking
→ argmax
→ selected action
```

This is the foundation for:

```text
policy networks
reinforcement learning
PPO
controller action selection
```

## Important Limitation

argmax is a deterministic selection rule.

Real AI systems may also use:

- probabilities
- exploration
- stochastic sampling

PPO will later introduce action distributions
instead of pure argmax selection.

