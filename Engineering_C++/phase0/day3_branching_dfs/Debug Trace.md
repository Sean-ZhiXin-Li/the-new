# Branching DFS Debug Trace — Day 3

## Objective

Understand and verify the reusable DFS engineering skeleton:

```text
for loop → choose → recurse → undo
```

This is not just permutation generation.
This trace proves that the recursion tree, state transitions, and restoration logic are structurally correct.

---

# Compile Command

```bash
g++ -std=c++17 -Wall -Wextra Engineering_C++/phase0/day3_branching_dfs/branching_dfs_template.cpp -o branching_dfs_template
```

---

# Run Command

```bash
./branching_dfs_template
```

---

# Partial Debug Output (Annotated)

```text
choose: A
 choose: B
  choose: C
   leaf: ABC
 undo: C
undo: B
 choose: C
  choose: B
   leaf: ACB
 undo: B
undo: C
undo: A
```

---

# Structural Interpretation

## Root Level

```text
choose: A
```

Meaning:

```text
Depth 0
Path = ""
Choose A as first branch
```

---

## Second Level

```text
 choose: B
```

Meaning:

```text
Depth 1
Path = "A"
Choose B as second branch
Current path = "AB"
```

---

## Third Level

```text
  choose: C
```

Meaning:

```text
Depth 2
Path = "AB"
Choose C
Current path = "ABC"
```

---

## Leaf Node

```text
   leaf: ABC
```

Meaning:

```text
Depth 3
Path size == choices size
A complete permutation is formed
Output ABC
```

---

## Undo Phase

```text
 undo: C
```

Meaning:

```text
Backtrack from C
Remove C from path
Restore used[C] = false
Return to path = "AB"
```

---

# Core Engineering Pattern

## Choose

```cpp
used[i] = 1;
path.push_back(choices[i]);
```

Meaning:

```text
Commit one choice
Update state
```

---

## Recurse

```cpp
dfs(..., depth + 1);
```

Meaning:

```text
Solve the smaller subproblem
Move one layer deeper
```

---

## Undo

```cpp
path.pop_back();
used[i] = 0;
```

Meaning:

```text
Restore previous state
Allow future branches
```

---

# Full Tree Mental Model

```text
""
├── A
│   ├── B
│   │   └── C → ABC
│   └── C
│       └── B → ACB
├── B
│   ├── A
│   │   └── C → BAC
│   └── C
│       └── A → BCA
└── C
    ├── A
    │   └── B → CAB
    └── B
        └── A → CBA
```

---

# Bug Audit

## Verified Correct

```text
[PASS] path is passed by reference
[PASS] choices is const reference
[PASS] used state is restored
[PASS] push_back / pop_back symmetry works
[PASS] for-loop explores all indices
[PASS] base case triggers only at full path
```

---

# Common Failure Modes (Not Present Here)

## Bug 1

```text
Forgot path.pop_back()
→ path corruption
```

## Bug 2

```text
Forgot used[i] = 0
→ future branches blocked
```

## Bug 3

```text
Base case missing return
→ invalid deeper recursion
```

---

# Key Insight

```text
DFS is not random recursion.
It is controlled state-space traversal.
```

More precisely:

```text
for loop = enumerate possibilities
used = legality filter
choose = commit state
recurse = explore branch
undo = restore state
```

---

# Day 3 Win Condition

```text
I can now read, debug, and explain branching DFS as an engineering template.
```

Not just:

```text
“I can solve one permutation problem.”
```

But:

```text
“I understand reusable recursive search structure.”
```

---

# One-Sentence Memory Rule

```text
Every DFS branch must fully restore state before the next branch begins.
```

Or shorter:

```text
Choose → Recurse → Undo.
```
