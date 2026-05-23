# Phase0 Day4 — Bitmask Abstraction

## Objective

Upgrade from:

```text
single brute force solution
```

to:

```text
readable helper functions
reusable bitmask logic
clean main / solve separation
```

Core engineering goal:

```text
state encoding → helper abstraction → algorithm clarity
```

---

# File Structure

```text
Engineering_C++/phase0/day4_bitmask_abstraction/
├── bitmask_helper.cpp
├── apple_division_refactored.cpp
├── README.md
└── debug_trace.md
```

---

# Core Files

## bitmask_helper.cpp

Purpose:

```text
Visualize mask states
Test subset sums
Debug bitmask logic safely
```

---

## apple_division_refactored.cpp

Purpose:

```text
Use helper functions inside real CSES Apple Division
Separate:
main → input/output
solve → algorithm
helper → state tools
```

---

# Compile

## Helper

```bash
g++ -std=c++17 bitmask_helper.cpp -o bitmask_helper
```

## Apple Division

```bash
g++ -std=c++17 apple_division_refactored.cpp -o apple_division_refactored
```

---

# Run

## Helper

```bash
./bitmask_helper
```

---

## Apple Division Manual Input

```bash
./apple_division_refactored
```

Example:

```text
3
3 5 7
```

---

## Apple Division CLI Pipe Test

```bash
echo "3
3 5 7" | ./apple_division_refactored
```

Meaning:

```text
echo = simulated stdin
| = pipe
program = consumes reproducible input
```

---

# Expected Result

```text
1
```

Because:

```text
[7] vs [3+5]
7 vs 8
Difference = 1
```

---

# Engineering Principles

## Separation of Concerns

```text
maskToBinaryString() → explain state
subsetSumFromMask() → evaluate state
solveAppleDivision() → compare solutions
main() → input/output only
```

---

# Complexity

## Bitmask Enumeration

```text
States = 2^n
Each state checks n bits
Total = O(n * 2^n)
```

---

# Permanent Engineering Rules

```text
[ ] Sum / large constraints → long long
[ ] Bitmask bound → (1LL << n)
[ ] Vector loop bound → i < values.size()
[ ] main = orchestration
[ ] helper = reusable logic
[ ] solve = algorithm core
[ ] Check complexity before submit
```

---

# Day4 Upgrade

```text
Before:
Solve one problem.

After:
Build reusable state-processing components.
```

---

# One-Line Summary

```text
Good engineering is turning brute force into readable, testable system components.
```

---