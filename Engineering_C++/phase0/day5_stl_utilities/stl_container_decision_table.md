# Phase0 Day5 — STL Container Decision Table

## Core Idea

```text
Different STL containers organize different kinds of state.
```

Today is not about memorizing syntax.

Today is about:

```text
Choosing the correct container for the correct state structure.
```

---

# STL Container Decision Table

| Container        | Main Purpose             | State Structure    | Ordered?              | Duplicate Allowed? | Typical Complexity     | Day5 Understanding    |
| ---------------- | ------------------------ | ------------------ | --------------------- | ------------------ | ---------------------- | --------------------- |
| `vector<int>`    | Store sequence data      | index -> value     | Yes (insertion order) | Yes                | append: O(1) amortized | Raw input state       |
| `map<int, int>`  | Store key-value metadata | key -> value       | Yes (sorted by key)   | key unique         | insert/find: O(log n)  | Frequency statistics  |
| `set<int>`       | Store unique states      | value existence    | Yes (sorted)          | No                 | insert/find: O(log n)  | Deduplication         |
| `queue<int>`     | FIFO processing          | first-in-first-out | Sequential            | Yes                | push/pop: O(1)         | BFS / task processing |
| `stack<int>`     | LIFO processing          | last-in-first-out  | Sequential            | Yes                | push/pop: O(1)         | DFS / backtracking    |
| `pair<int, int>` | Store two related values | first + second     | N/A                   | N/A                | O(1)                   | Final answer state    |

---

# 1. vector<int>

## Purpose

```text
Store ordered sequence data.
```

## Example

```cpp
std::vector<int> values;
```

Input:

```text
1 2 2 3 3
```

State:

```text
[1, 2, 2, 3, 3]
```

## Day5 Meaning

```text
Raw input state.
```

## Important Operations

```cpp
push_back()
size()
[]
```

---

# 2. map<int, int>

## Purpose

```text
Store structured metadata.
```

## Example

```cpp
std::map<int, int> frequency;
```

Meaning:

```text
number -> count
```

State:

```text
1 -> 1
2 -> 2
3 -> 2
```

## Day5 Meaning

```text
Structured frequency state.
```

## Important Operations

```cpp
frequency[value]++
entry.first
entry.second
```

## Important Insight

```text
map automatically creates missing keys.
```

Example:

```cpp
frequency[5]++;
```

If key 5 does not exist:

```text
5 -> 0
```

is automatically created first.

---

# 3. set<int>

## Purpose

```text
Store unique values.
```

## Example

```cpp
std::set<int> visited;
```

## Day5 Meaning

```text
Deduplicated state.
```

## Example

Input:

```text
1 2 2 3 3
```

set state:

```text
1 2 3
```

## Important Insight

```text
set removes duplicates automatically.
```

---

# 4. queue<int>

## Purpose

```text
First-in-first-out processing.
```

## Example

```cpp
std::queue<int> q;
```

## Day5 Meaning

```text
Processing order state.
```

## Future Use

```text
BFS
Task scheduling
Pipeline processing
```

## Important Operations

```cpp
push()
pop()
front()
```

---

# 5. stack<int>

## Purpose

```text
Last-in-first-out processing.
```

## Example

```cpp
std::stack<int> st;
```

## Day5 Meaning

```text
Backtracking state.
```

## Future Use

```text
DFS
Recursion simulation
Undo systems
```

## Important Operations

```cpp
push()
pop()
top()
```

---

# 6. pair<int, int>

## Purpose

```text
Store two related values.
```

## Example

```cpp
std::pair<int, int> result;
```

Meaning:

```text
(bestValue, bestCount)
```

Example:

```text
(2, 2)
```

## Day5 Meaning

```text
Final decision state.
```

## Important Operations

```cpp
result.first
result.second
```

---

# Day5 Core State Transformation

```text
stdin
→ vector<int>
→ map<int,int>
→ pair<int,int>
→ stdout
```

Meaning:

```text
raw sequence state
→ structured metadata state
→ final decision state
```

---

# Day5 Engineering Insight

Competitive programming beginners often think:

```text
"I need to memorize STL syntax."
```

But the deeper engineering idea is:

```text
Choose the correct container
for the correct state structure.
```

That is the beginning of:

```text
engineering system thinking
```

not just:

```text
writing random code inside main()
```
