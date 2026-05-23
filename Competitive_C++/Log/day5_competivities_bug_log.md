# Phase0 Day5 — Competitive C++ Bug Log

## Task

Input `n` integers and output the most frequent value.

If there is a tie, output the smaller value.

---

## Core Data Structure

```cpp
std::map<int, int> frequency;
```

Meaning:

```text
number -> count
```

This is the main Day5 idea:

```text
STL container = reusable state tool
```

---

## Bug / Risk 1 — map key/value confusion

### Mistake

I may confuse:

```cpp
entry.first
entry.second
```

### Correct Understanding

```cpp
entry.first
```

means:

```text
key = number
```

```cpp
entry.second
```

means:

```text
value = count
```

Example:

```text
2 -> 3
```

Then:

```cpp
entry.first = 2
entry.second = 3
```

---

## Bug / Risk 2 — frequency[value]++ meaning

### Mistake

I may think `frequency[value]` must already exist before using it.

### Correct Understanding

For `std::map<int, int>`:

```cpp
frequency[value]++;
```

means:

```text
If value does not exist, map creates it with default count 0.
Then ++ increases it by 1.
```

Example:

```text
first 3: frequency[3] becomes 1
second 3: frequency[3] becomes 2
third 3: frequency[3] becomes 3
```

---

## Bug / Risk 3 — tie-breaking mistake

### Mistake

Writing:

```cpp
if (count >= bestCount)
```

### Why It Is Wrong

If two numbers have the same count, `>=` will replace the earlier answer.

But the problem says:

```text
If counts are tied, output the smaller value.
```

### Correct Code

```cpp
if (count > bestCount)
```

### Why It Works

`std::map` traverses keys in sorted order.

So smaller numbers appear first.

If the count is tied, we do not update the answer.

---

## Bug / Risk 4 — wrong initial bestCount

### Code

```cpp
int bestCount = -1;
```

### Meaning

`-1` means:

```text
No valid answer has been selected yet.
```

Because all real counts are at least `1`, the first map entry will always update the answer.

This is an invalid initial state pattern.

---

## Bug / Risk 5 — using vector inefficiently

### Mistake

Using a `vector` and scanning repeatedly to count frequency.

### Problem

That may become:

```text
O(n^2)
```

because each value may need another full scan.

### Better Choice

Use:

```cpp
std::map<int, int>
```

because it stores:

```text
value -> count
```

in a structured way.

---

## Complexity

Let `n` be the number of input values.

Each map update costs:

```text
O(log k)
```

where `k` is the number of unique values.

Total complexity:

```text
O(n log k)
```

Worst case:

```text
O(n log n)
```

because all values may be unique.

---

## Test Cases

### Test 1

Input:

```text
8
3 5 3 2 5 3 2 2
```

Output:

```text
2 3
```

Reason:

```text
2 and 3 both appear 3 times.
The smaller value is 2.
```

---

### Test 2

Input:

```text
5
1 1 2 2 3
```

Output:

```text
1 2
```

Reason:

```text
1 and 2 both appear 2 times.
The smaller value is 1.
```

---

### Test 3

Input:

```text
4
-1 -1 -2 -2
```

Output:

```text
-2 2
```

Reason:

```text
-2 and -1 both appear 2 times.
The smaller value is -2.
```

---

## Day5 Reflection

Today I learned that `map<int, int>` is not just syntax.

It is a structured state tool:

```text
key -> value
state -> metadata
number -> frequency
```

The main Competitive C++ idea today is:

```text
Choose the right container to organize state.
```
