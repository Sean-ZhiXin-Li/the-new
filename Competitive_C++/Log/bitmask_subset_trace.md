# bitmask_subset_trace.md

# Phase0 Day4 — Bitmask Subset Trace (Apple Division)

## Objective

Understand:

```text
for (mask = 0 → 2^n - 1)
```

means:

```text
Enumerate every possible subset selection state.
```

---

# Core Mental Model

```text
mask = one complete decision plan
bit i = whether apple[i] is selected
```

For each apple:

```text
0 = not selected
1 = selected
```

So:

```text
n apples → 2^n possible subsets
```

---

# Example Input

```text
apples = [3,5,7]
```

```text
index 0 → 3
index 1 → 5
index 2 → 7
```

---

# Why `(1LL << n)`?

```cpp
1LL << 3 = 8
```

Meaning:

```text
2^3 = 8 total subset states
```

So:

```text
mask = 0 → 7
```

---

# Full State Table

| Decimal mask | Binary mask | Selected Apples | groupSum |
| ------------ | ----------- | --------------- | -------: |
| 0            | 000         | []              |        0 |
| 1            | 001         | [3]             |        3 |
| 2            | 010         | [5]             |        5 |
| 3            | 011         | [3,5]           |        8 |
| 4            | 100         | [7]             |        7 |
| 5            | 101         | [3,7]           |       10 |
| 6            | 110         | [5,7]           |       12 |
| 7            | 111         | [3,5,7]         |       15 |

---

# Key Line Breakdown

## Outer Loop

```cpp
for (long long mask = 0; mask < (1LL << n); mask++)
```

Meaning:

```text
Try every possible subset plan.
```

---

## Inner Loop

```cpp
for (int i = 0; i < n; i++)
```

Meaning:

```text
Check each apple.
```

---

## Bit Check

```cpp
if (mask & (1LL << i))
```

Meaning:

```text
Does current subset plan select apple i?
```

---

# Example Trace — mask = 5

## Decimal:

```text
5
```

## Binary:

```text
101
```

---

## Check i = 0

```text
101
001
---
001 → selected
```

```text
Select apple[0] = 3
```

---

## Check i = 1

```text
101
010
---
000 → not selected
```

```text
Skip apple[1] = 5
```

---

## Check i = 2

```text
101
100
---
100 → selected
```

```text
Select apple[2] = 7
```

---

# Final Result

```text
groupSum = 3 + 7 = 10
otherSum = 15 - 10 = 5
diff = |10 - 5| = 5
```

---

# Important Distinction

## Program counts in decimal:

```text
0,1,2,3,4...
```

## We interpret each number in binary:

```text
5 → 101
```

---

# True Meaning of Bitmask

```text
Run normal numbers
Interpret bits as state
```

---

# Complexity

## Outer:

```text
2^n
```

## Inner:

```text
n
```

## Total:

```text
O(n * 2^n)
```

---

# Day4 Core Insight

```text
Bitmask = Use binary representation of an integer to encode subset decisions.
```

---

# Engineering Relevance

Future uses:

```text
Subset search
Feature flags
State encoding
DP state compression
Controller mode combinations
```

---

# Today’s Win

```text
mask = full plan
bit = local decision
bitmask = decision encoding system
```

---