# Phase0 Day4 — Debug Trace

## Final Status

```text
PASS
```

---

# Bug 1 — Wrong Compile Target

## Problem

```text
undefined reference to WinMain
```

## Cause

```text
Wrong filename / wrong compile target
```

## Fix

```text
Compile actual .cpp containing int main()
```

## Lesson

```text
Build system correctness matters before algorithm correctness.
```

---

# Bug 2 — Off-by-One Vector Bounds

## Original Mistake

```cpp
for (int i = 0; i <= values.size(); i++)
```

---

# Why It Failed

```text
values[values.size()] is out-of-bounds
Undefined behavior
Garbage outputs
```

---

# Fix

```cpp
for (int i = 0; i < values.size(); i++)
```

---

# Lesson

```text
Vector upper bounds are exclusive.
Last valid index = size() - 1.
```

---

# Bug 3 — State Dimension Confusion

## Confusion

```text
Why 256 outputs instead of 8?
```

---

# Resolution

```text
3 values → 2^3 = 8 states
8 values → 2^8 = 256 states
```

---

# Correct Mental Model

```text
Number of bits = number of elements
State count = 2^n
```

---

# Verification

## Input

```cpp
{3,5,7,8,1,6,2,9}
```

## Final State

```text
11111111 -> 41
```

## Check

```text
3+5+7+8+1+6+2+9 = 41
```

---

# CLI Testing Upgrade

## Command

```bash
echo "3
3 5 7" | ./apple_division_refactored
```

## Meaning

```text
Simulated stdin
Reproducible testing
No manual typing
```

---

# Final Engineering Lessons

```text
[ ] Wrong file target can break linker
[ ] Off-by-one destroys memory safety
[ ] Dimension controls state explosion
[ ] Debugging is system reasoning
[ ] Reusable helpers improve clarity
```

---

# One-Line Summary

```text
My algorithm was mostly right; my real bugs were engineering precision, bounds safety, and system correctness.
```
