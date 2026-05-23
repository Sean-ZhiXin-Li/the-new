# Engineering C++ — Phase 0 Day 2

## DFS Reboot Skeleton

---

# Objective

Build the smallest possible DFS skeleton to understand:

```text
state
recursion depth
base case
push_back / pop_back
state recovery
```

This is **not** a full permutation generator.

This file exists to train:

```text
DFS structure → choose → recurse → undo
```

---

# File

```text
dfs_skeleton.cpp
```

---

# Compile

```bash
g++ -std=c++17 dfs_skeleton.cpp -o dfs_skeleton
```

---

# Run

```bash
./dfs_skeleton
```

---

# Expected Output

```text
ABC
```

---

# Code

```cpp
#include <iostream>
#include <string>

void dfs(int depth, int maxDepth, std::string& path) {
    if (depth == maxDepth) {
        std::cout << path << '\n';
        return;
    }

    path.push_back('A' + depth);
    dfs(depth + 1, maxDepth, path);
    path.pop_back();
}

int main() {
    std::string path;

    dfs(0, 3, path);

    return 0;
}
```

---

# Core Logic Breakdown

## Parameters

### `depth`

```text
Current recursion layer.
```

### `maxDepth`

```text
Maximum recursion depth.
```

### `path`

```text
Current chosen state / partial path.
```

---

# DFS Structure

## Step 1 — Choose

```cpp
path.push_back('A' + depth);
```

Meaning:

```text
Add one choice into current path.
```

---

## Step 2 — Recurse

```cpp
dfs(depth + 1, maxDepth, path);
```

Meaning:

```text
Enter next decision layer.
```

---

## Step 3 — Undo

```cpp
path.pop_back();
```

Meaning:

```text
Recover state after recursion returns.
```

---

# Base Case

```cpp
if (depth == maxDepth)
```

Meaning:

```text
Stop recursion when target depth is reached.
```

---

# Execution Trace

```text
""
↓ push A
"A"
↓ push B
"AB"
↓ push C
"ABC"
↓ print
ABC
↓ pop C
"AB"
↓ pop B
"A"
↓ pop A
""
```

---

# Key Engineering Lessons

## 1. Reference Matters

```cpp
std::string& path
```

```text
Reference avoids unnecessary copying.
```

---

## 2. State Recovery Matters

```text
Without pop_back(), path becomes corrupted.
```

---

## 3. Base Case Prevents Infinite Recursion

```text
Every recursive DFS needs a stopping rule.
```

---

# Complexity

```text
Current version:
O(maxDepth)
```

Because:

```text
Only one branch per level.
```

Future full branching:

```text
O(branches^depth)
```

---

# Common Bugs

```text
1. Missing base case
2. Forgetting pop_back()
3. Passing path by value instead of reference
4. Wrong depth increment
5. State pollution
```

---

# Relation to CSES 1622

Current:

```text
Single path DFS skeleton
```

Next:

```text
for-loop branching
used[]
duplicate skipping
full permutation generation
```

---

# Lab / Engineering Relevance

This same structure later applies to:

```text
Search trees
Path planning
Controller branching
Decision systems
Trajectory exploration
```

---

# Win Condition

If you understand:

```text
push → recurse → pop
```

You understand the foundation of DFS / Backtracking.

---

# Day 2 Deliverable Standard

```text
✔ Can compile independently
✔ Can explain depth
✔ Can explain base case
✔ Can explain state recovery
✔ Can trace execution manually
```

---

# Next Upgrade (Day 3)

```text
Single path → multi-branch DFS
Add:
for loop
used[]
true permutation generation
```
