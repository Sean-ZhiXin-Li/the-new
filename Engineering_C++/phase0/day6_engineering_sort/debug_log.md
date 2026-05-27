# Day6 Engineering C++ Debug Log

## Goal

Convert competitive sorting code into structured engineering C++.

---

## Core Structure

The program is organized into:

* struct Event
* compareEvents()
* readEvents()
* printEvents()
* solve()
* main()

### Engineering Meaning

main() is only the entry point.

solve() controls the main workflow.

Helper functions are reusable modules.

This structure is cleaner and easier to debug than placing all logic inside main().

---

## Comparator Logic

Primary rule:

* smaller time goes first

Secondary rule:

* if time is equal
* higher priority goes first

Comparator defines the system priority rule.

---

## stdout vs stderr

I separated:

* formal program output
* debug information

using:

* std::cout
* std::cerr

and Linux redirection:

```bash
>  stdout
2> stderr
```

This allows clean experiment outputs and isolated debugging logs.

---

## Linux Commands Used

```bash
g++ -std=c++17 -Wall -Wextra -O2 event_sorter.cpp -o /tmp/event_sorter
```

```bash
/tmp/event_sorter < /tmp/day6_engineering_input.txt
```

```bash
/tmp/event_sorter < /tmp/day6_engineering_input.txt > /tmp/day6_stdout.txt 2> /tmp/day6_stderr.txt
```

---

## Bug 1 — Heredoc Did Not Exit

### Problem

Terminal remained in:

```text
>
```

state.

### Cause

EOF marker was missing.

### Fix

Type:

```text
EOF
```

on a separate line.

### Lesson

The shell waits for the heredoc closing token before execution.

---

## Bug 2 — Comparator Direction Mistake

### Problem

Sorting order was opposite of the expected behavior.

### Cause

Comparator direction was reversed.

### Fix

Use:

```cpp
return left.priority > right.priority;
```

for higher priority first.

### Lesson

Comparator defines system behavior.

---

## Bug 3 — Forgot Recompilation

### Problem

Program behavior did not change after editing source code.

### Cause

The executable binary was not rebuilt.

### Fix

Re-run:

```bash
g++ -std=c++17 -Wall -Wextra -O2 ...
```

### Lesson

C++ requires recompilation after source changes.

---

## Bug 4 — printEvents Signature Mismatch

### Problem

Compiler produced:

```text
too many arguments in function call
```

### Cause

The function definition only accepted one parameter:

```cpp
printEvents(events)
```

but the call passed:

```cpp
printEvents(events, std::cerr)
```

### Fix

Upgrade function signature:

```cpp
void printEvents(const std::vector<Event>& events,
                 std::ostream& output)
```

### Lesson

Function calls must match the function interface exactly.

---

## Bug 5 — Unused Parameter Warning

### Problem

Compiler warning:

```text
unused parameter
```

### Cause

The parameter:

```cpp
std::ostream& output
```

was declared but not used.

The code still used:

```cpp
std::cout
```

inside the function.

### Fix

Replace:

```cpp
std::cout
```

with:

```cpp
output
```

### Lesson

Warnings should always be investigated carefully.

---

## Engineering Concepts Learned

* helper function structure
* comparator logic
* grouped data using struct
* stdout vs stderr separation
* Linux redirection
* compile warnings
* reusable interfaces
* engineering-style debugging

---

## Connection to Engineering Playground

This workflow is similar to:

* stdout.txt
* stderr.txt
* metrics.json
* reproducible pipelines

used in larger engineering systems and AI experiments.

---

## Future Engineering Risks

* stale binaries
* incorrect comparator logic
* invalid vector indexing
* debug information polluting stdout
* missing recompilation
* inconsistent interfaces
