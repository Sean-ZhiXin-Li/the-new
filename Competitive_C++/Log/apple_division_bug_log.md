# Phase0 Day4 — Apple Division Bug Log

## Final Status

```text
ACCEPTED
```

---

# Main Bugs Encountered

## Bug 1 — Integer Overflow

## Original Mistake:

```cpp
int totalSum
int groupSum
int bestDiff
```

---

# Why It Failed

Apple weights can become large enough that:

```text
totalSum exceeds int safe range
```

This caused hidden test WA.

---

# Fix

```cpp
long long totalSum
long long groupSum
long long otherSum
long long diff
long long bestDiff
```

---

# Lesson

```text
When sums / differences / large constraints exist:
Prefer long long.
```

---

# Bug 2 — Shift Type Safety

## Original:

```cpp
(1 << n)
```

---

# Risk

```text
Uses int shift
Potential overflow / unsafe habit
```

---

# Fix

```cpp
(1LL << n)
```

---

# Lesson

```text
Bitmask engineering habit:
Always use 1LL for safer subset bounds.
```

---

# Bug 3 — Conceptual Confusion

## Confusion:

```text
Why decimal loop but binary logic?
```

---

# Resolution

```text
mask increments normally in decimal
Binary is interpretation layer
```

---

# Correct Mental Model

```text
Decimal = counter
Binary = subset meaning
```

---

# Bug 4 — `&` Operator Misunderstanding

## Initial confusion:

```text
Thought & was normal comparison
```

---

# Correct:

```text
& = bitwise AND
Used to test whether bit i is selected
```

---

# Correct Translation

```cpp
mask & (1LL << i)
```

=

```text
Is bit i ON?
```

---

# Performance Check

## Worst Case:

```text
n = 20
2^20 ≈ 1,048,576
```

---

# Result:

```text
Brute force acceptable
```

---

# Final Engineering Upgrades

## Before Day4:

```text
Brute force vaguely understood
```

## After Day4:

```text
Subset enumeration
Bitmask state encoding
Overflow awareness
Type safety
Complexity awareness
```

---

# Permanent Rules Added

```text
[ ] Sum large numbers → long long
[ ] Bitmask upper bound → 1LL << n
[ ] mask = state
[ ] bit = decision
[ ] O(n * 2^n) before submit
```

---

# One-Line Summary

```text
My logic was correct; my bug was engineering precision (type safety), not algorithm design.
```
