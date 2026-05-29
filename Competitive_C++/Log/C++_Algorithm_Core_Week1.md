# C++ Algorithm Core Week 1

## 1. Recursion

### What It Does

Recursion solves a problem by calling the same function on a smaller subproblem.

A recursive function usually contains:

* Base case
* Recursive case

The base case stops the recursion.

### When To Use It

Use recursion when:

* A problem naturally breaks into smaller versions of itself
* Tree traversal
* DFS
* Backtracking
* Divide and conquer

### Common Bug

* Missing base case
* Infinite recursion
* Not understanding when recursion returns
* Forgetting that each recursive call creates a new stack frame

### Week 1 Example

Creating Strings I

```text
search()
→ choose character
→ search()
→ undo choice
→ return
```

### Key Insight

```text
Recursion is not repetition.
Recursion is problem decomposition.
```

---

## 2. DFS / Backtracking

### What It Does

DFS explores one path completely before trying another path.

Backtracking means:

```text
Choose
Explore
Undo
Try next choice
```

### When To Use It

Use DFS / Backtracking for:

* Permutations
* Combinations
* Search trees
* State exploration
* Constraint problems

### Common Bug

* Forgetting to undo state
* Missing visited tracking
* Duplicate results
* Incorrect recursion termination

### Week 1 Example

Creating Strings I

```cpp
path.push_back(...)
used[i] = true

search()

path.pop_back()
used[i] = false
```

### Key Insight

```text
Backtracking = explore a branch, then restore the state.
```

---

## 3. Permutation

### What It Does

Permutation generates every possible ordering.

Example:

```text
abc

abc
acb
bac
bca
cab
cba
```

### When To Use It

Use permutations when:

* Order matters
* Need all arrangements
* State search problems

### Common Bug

* Duplicate permutations
* Incorrect used[] handling
* Printing before completion
* Not restoring state

### Week 1 Example

Creating Strings I

Input:

```text
abb
```

Output:

```text
abb
bab
bba
```

### Duplicate Rule

```cpp
if (i > 0 &&
    s[i] == s[i - 1] &&
    !used[i - 1])
{
    continue;
}
```

### Key Insight

```text
Same-level duplicate choices must be skipped.
```

---

## 4. Subset / Bitmask

### What It Does

Bitmask uses binary digits to represent decisions.

```text
0 = not selected
1 = selected
```

Example:

```text
101
```

means:

```text
take item 0
skip item 1
take item 2
```

### When To Use It

Use bitmask for:

* Subset enumeration
* State encoding
* Feature flags
* Small search spaces

### Common Bug

* Integer overflow
* Misunderstanding binary interpretation
* Wrong bit operations

### Week 1 Example

Apple Division

```cpp
for (long long mask = 0;
     mask < (1LL << n);
     mask++)
```

### Key Lessons

```text
mask = full plan
bit = local decision
```

```cpp
mask & (1LL << i)
```

means:

```text
Is bit i selected?
```

### Complexity

```text
O(n * 2^n)
```

### Key Insight

```text
Bitmask is a decision encoding system.
```

---

## 5. STL Containers

### What It Does

STL containers organize data.

Different containers represent different state structures.

### When To Use Them

#### vector

```text
Ordered sequence
```

Use for:

* Arrays
* Lists
* Input storage

#### pair

```text
Two related values
```

Use for:

* Coordinate pairs
* Score + ID
* Value + Count

#### map

```text
Key -> Value
```

Use for:

* Frequency counting
* Dictionaries
* Metadata lookup

#### set

```text
Unique values
```

Use for:

* Duplicate removal
* Ordered unique storage

#### queue

```text
FIFO
```

Use for:

* BFS
* Processing order

#### stack

```text
LIFO
```

Use for:

* DFS
* Backtracking

### Common Bug

* Confusing key and value
* Using the wrong container
* Forgetting ordering rules

### Week 1 Example

```cpp
map<int, int> frequency;
```

```text
number -> count
```

### Key Insight

```text
Container = structured state storage.
```

---

## 6. Sorting + Comparator

### What It Does

Sorting organizes data according to a rule.

### When To Use It

Use sorting for:

* Ranking
* Selection
* Searching
* Scheduling
* Priority systems

### Common Bug

* Wrong comparator direction
* Wrong tie-breaking rule
* Assuming default ordering

### Week 1 Example

Default sort:

```cpp
sort(v.begin(), v.end());
```

Comparator:

```cpp
return a.second > b.second;
```

### Comparator Meaning

```text
Should a go before b?
```

### Key Insight

```text
Comparator defines system priority rules.
```

---

## 7. Complexity Summary

| Tool                    | Typical Complexity | Why It Matters                            |
| ----------------------- | ------------------ | ----------------------------------------- |
| loop scan               | O(n)               | Basic traversal                           |
| sort                    | O(n log n)         | Organize data before searching or ranking |
| nested loop             | O(n²)              | Often too slow for large inputs           |
| set/map operation       | O(log n)           | Ordered lookup and updates                |
| unordered_map operation | Average O(1)       | Fast frequency counting                   |
| DFS traversal           | O(V + E)           | Graph exploration                         |
| Bitmask subset search   | O(n × 2ⁿ)          | Complete subset enumeration               |
| Permutation search      | O(n! × n)          | Generate all orderings                    |

### Week 1 Biggest Complexity Lesson

```text
Always estimate complexity before coding.
```

---

## 8. Bug Log Summary

### Weird Algorithm

* Risk of int overflow
* Forgetting final 1
* Infinite loop risk

Rule:

```text
Use long long when values can grow.
```

### Missing Number

* Misread input size
* Considered O(n²) solution first
* Did not immediately recognize mathematical structure

Rule:

```text
Look for math before brute force.
```

### Creating Strings I

* Did not understand recursion flow
* Duplicate permutations
* Signed/unsigned warnings

Rule:

```text
Understand recursion state transitions.
```

### Apple Division

* Integer overflow
* Unsafe shift operations
* Bitwise confusion

Rule:

```text
Use 1LL << n
Use long long for sums
```

### STL Frequency Problem

* map key/value confusion
* Tie-breaking mistakes

Rule:

```text
Choose containers based on state structure.
```

### Day 6 Comparator Practice

* Wrong comparator direction
* Forgot recompilation
* Used | instead of ||

Rule:

```text
Warnings are debugging signals.
```

---

## 9. What I Can Explain Now

I can explain:

* Time complexity basics
* O(n), O(n log n), O(n²)
* Recursion
* DFS
* Backtracking
* Permutations
* Duplicate skipping
* Bitmask subset enumeration
* vector
* pair
* map
* set
* queue
* stack
* sort
* Comparator design
* Frequency counting
* Basic debugging workflow

---

## 10. What Still Feels Weak

Topics that need more practice:

### Competitive Programming

* Prefix Sum
* Two Pointers
* Binary Search
* BFS
* Graphs
* Dynamic Programming

### Engineering C++

* Modular project structure
* Multi-file projects
* Header files
* Debugging larger codebases
* STL mastery

### Complexity

* Recognizing optimal solutions quickly
* Estimating complexity under contest pressure

---

# Week 1 Final Reflection

Week 1 was not about solving difficult problems.

It was about building core mental models:

```text
Recursion = problem decomposition

DFS = path exploration

Backtracking = choose → explore → undo

Bitmask = state encoding

Container = state organization

Sorting = ranking and selection

Comparator = priority rule

Complexity = feasibility check
```

The most important upgrade from Week 1 is:

```text
I no longer see algorithms as isolated tricks.

I see them as ways to represent, organize, explore, and evaluate state.
```
