# Phase0 Day5 — STL Container Selection Notes

## Core Idea

STL container = reusable state tool.

Day4:

* mask = state
* bit = decision

Day5:

* container = structured state storage

---

# Container Table

| Container | Stores What        | Order Rule         | Best For                   | Day5 Meaning                    |
| --------- | ------------------ | ------------------ | -------------------------- | ------------------------------- |
| vector    | sequence of values | insertion order    | list / array-like data     | store all input numbers         |
| pair      | two related values | first then second  | value + count / coordinate | return best value and count     |
| map       | key to value       | sorted by key      | frequency / dictionary     | value -> count                  |
| set       | unique values      | sorted by key      | remove duplicates          | unique sorted numbers           |
| queue     | FIFO process order | first in first out | BFS later                  | process states in arrival order |
| stack     | LIFO process order | last in first out  | DFS/backtracking later     | reverse / backtracking state    |

---

# Today’s Main Choice

For frequency counting, use:

```cpp
map<int, int> frequency;
```

Reason:

* key = number
* value = count
* map keeps keys sorted
* tie-breaking becomes easier when smaller value should win

---

# Why Not Vector?

Using vector to count frequency by scanning every time may become:

```text
O(n^2)
```

because each new value may need another full scan.

map gives:

```text
structured key-value counting
```

with:

```text
O(log n)
```

update cost.

---

# map Traversal

```cpp
for (const auto& entry : frequency)
```

means:

```text
iterate over every key-value pair in the map
```

where:

```cpp
entry.first
```

is the key.

```cpp
entry.second
```

is the value.

Example:

```text
2 -> 3
3 -> 3
5 -> 2
```

During traversal:

```cpp
entry.first = 2
entry.second = 3
```

---

# Tie-breaking Logic

We use:

```cpp
if (count > bestCount)
```

instead of:

```cpp
if (count >= bestCount)
```

because:

```text
map traverses keys in sorted order
```

So the smaller value appears first.

If counts are equal, we keep the earlier (smaller) key.

---

# Complexity

Input:

```text
n numbers
```

Each map insertion/update:

```text
O(log n)
```

Total:

```text
O(n log n)
```

Worst case:

```text
all numbers are unique
```

---

# Day5 Core Understanding

Today is not about memorizing STL syntax.

Today is about understanding:

```text
data structure = state organization system
```

Examples:

```text
vector = ordered state sequence
map = state -> metadata
set = unique state storage
queue = processing order
stack = backtracking order
```
