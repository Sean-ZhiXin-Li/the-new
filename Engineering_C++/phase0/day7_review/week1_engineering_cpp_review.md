# Week 1 Engineering C++ Review

## 1. Clean Code Habits

Week 1 was not only about solving small C++ problems.

The real goal was to build engineering habits:

```text
clear structure
small helper functions
safe types
clean compile workflow
reproducible testing
debug notes
repo hygiene
```

The biggest change is that I am starting to separate code into:

```text
main() -> input / orchestration
solve() -> algorithm workflow
helper functions -> reusable logic
```

This is better than writing everything inside `main()`.

---

## 2. Helper Functions Used

### Day 1 — printVector

I wrote a reusable function:

```cpp
void printVector(const std::vector<int>& values)
```

Key engineering ideas:

```text
const = do not modify input
& = avoid copying
void = action without return value
```

This was my first modular C++ function in this phase.

---

### Day 2 — DFS Skeleton

I practiced the basic DFS structure:

```text
base case
choose
recurse
undo
```

The important pattern was:

```cpp
path.push_back(...);
dfs(...);
path.pop_back();
```

This trained state recovery.

---

### Day 3 — Branching DFS Template

I upgraded from one path to multiple branches:

```text
for loop
used[]
choose
recurse
undo
```

Core idea:

```text
DFS is controlled state-space traversal.
```

Every branch must restore state before the next branch begins.

---

### Day 4 — Bitmask Helper Functions

I used helper functions to make bitmask logic cleaner:

```text
maskToBinaryString()
subsetSumFromMask()
solveAppleDivision()
```

This changed the code from a single brute-force block into readable components.

Core idea:

```text
state encoding -> helper abstraction -> algorithm clarity
```

---

### Day 5 — STL Utilities

I practiced STL data flow:

```text
stdin
-> vector<int>
-> map<int, int>
-> pair<int, int>
-> stdout
```

Key idea:

```text
Different containers organize different kinds of state.
```

I used:

```cpp
std::map<int, int> frequency;
```

to represent:

```text
number -> count
```

---

### Day 6 — Event Sorter

I organized the program into:

```text
struct Event
compareEvents()
readEvents()
printEvents()
solve()
main()
```

This was the most engineering-style C++ program of Week 1.

Main lesson:

```text
main() is only the entry point.
solve() controls the workflow.
helper functions make the system readable and testable.
```

---

## 3. Compiler Flags

By Day 6, I used:

```bash
g++ -std=c++17 -Wall -Wextra -O2 event_sorter.cpp -o /tmp/event_sorter
```

Important flags:

```text
-std=c++17 = use modern C++17
-Wall = enable common warnings
-Wextra = enable extra warnings
-O2 = optimize generated binary
```

Warnings are not noise.

Warnings are debugging signals.

---

## 4. Debugging Lessons

### Wrong Compile Target

I encountered:

```text
undefined reference to WinMain
```

Cause:

```text
Wrong file target / wrong compile command.
```

Lesson:

```text
Build system correctness matters before algorithm correctness.
```

---

### Off-by-One Vector Bounds

Bug pattern:

```cpp
for (int i = 0; i <= values.size(); i++)
```

Correct:

```cpp
for (int i = 0; i < values.size(); i++)
```

Lesson:

```text
Vector upper bounds are exclusive.
Last valid index = size() - 1.
```

---

### Missing State Recovery

DFS requires:

```cpp
path.pop_back();
used[i] = false;
```

Without undo logic:

```text
state becomes polluted
future branches become incorrect
```

Lesson:

```text
Backtracking is not complete without state restoration.
```

---

### Map Key / Value Confusion

For:

```cpp
std::map<int, int> frequency;
```

The meaning is:

```text
entry.first = key
entry.second = value
```

Example:

```text
2 -> 3
```

means:

```text
entry.first = 2
entry.second = 3
```

---

### Pair Cannot Be Printed Directly

Wrong idea:

```cpp
std::cout << result;
```

Correct:

```cpp
std::cout << result.first << " " << result.second << "\n";
```

Lesson:

```text
Structured data often needs explicit output formatting.
```

---

### Comparator Direction Mistake

Comparator answers:

```text
Should left go before right?
```

For higher priority first:

```cpp
return left.priority > right.priority;
```

Lesson:

```text
Comparator defines system priority rules.
```

---

### Forgot Recompilation

Problem:

```text
Source code changed but output did not change.
```

Cause:

```text
Executable binary was stale.
```

Fix:

```text
Recompile after every source code change.
```

Lesson:

```text
C++ has a source -> compile -> binary -> run workflow.
```

---

### stdout vs stderr

I learned to separate:

```text
std::cout = formal program output
std::cerr = debug information
```

With Linux redirection:

```bash
/tmp/event_sorter < /tmp/input.txt > /tmp/stdout.txt 2> /tmp/stderr.txt
```

Lesson:

```text
Clean output and debug output should not be mixed.
```

---

## 5. Repository Hygiene

I checked for local build artifacts:

```bash
find . -name "*.exe"
find . -name "*.out"
find . -type d -name "cmake-build-debug"
```

I found several local `.exe` files and one `cmake-build-debug` directory.

They were not tracked by Git, because `git status` only showed the Week 1 markdown file as untracked.

Current `.gitignore` already blocks:

```text
*.exe
*.out
cmake-build-debug/
```

Recommended additions:

```gitignore
*.o
build/
```

Repo hygiene rule:

```text
Source files and notes should be committed.
Compiled binaries and build directories should not be committed.
```

---

## 6. Binaries / Build Artifacts Risk

Compiled files such as:

```text
.exe
.out
.o
cmake-build-debug/
build/
```

should not enter Git history.

Reasons:

```text
They are generated files.
They depend on the local machine.
They make the repo noisy.
They can become stale.
They hide the real source code changes.
```

Better habit:

```text
Compile into /tmp or build/
Keep source code in repo.
Keep generated files out of repo.
```

Example:

```bash
g++ -std=c++17 -Wall -Wextra -O2 event_sorter.cpp -o /tmp/event_sorter
```

This keeps the repo clean.

---

## 7. Week 1 Engineering C++ Summary

Week 1 taught me that C++ engineering is not only syntax.

It is a workflow:

```text
write source code
compile with warnings
run with controlled input
separate stdout / stderr
debug systematically
clean artifacts
document lessons
commit only meaningful files
```

The most important engineering upgrade was:

```text
I am starting to write C++ as small systems, not isolated contest snippets.
```

---

## 8. What I Can Explain Now

I can explain:

```text
vector<int>
const reference
void function
DFS skeleton
choose -> recurse -> undo
used[] state tracking
bitmask helper abstraction
map frequency counting
pair result state
struct Event
custom comparator
stdout vs stderr
compile/run workflow
repo hygiene
```

---

## 9. What Still Feels Weak

I still need more practice with:

```text
multi-file C++ projects
header files
larger debugging sessions
CMake basics
stronger STL fluency
Graph class design
BFS implementation
clean reusable templates
```

---

## 10. Final Reflection

Before Week 1, C++ felt like isolated syntax and small contest solutions.

After Week 1, I can see a larger engineering pattern:

```text
data structure -> state representation
helper function -> reusable logic
compiler warning -> debugging signal
stdout/stderr -> experiment separation
.gitignore -> repo discipline
```

The main result of Week 1 is not that I solved difficult problems.

The main result is:

```text
I started building engineering discipline around C++.
```
