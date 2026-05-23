# Day 1 Engineering C++ — `print_vector`

## Objective

Phase 0 Day 1 Engineering C++ reboot:

Practice:

* `vector<int>` basic STL usage
* function decomposition (`printVector(...)`)
* compile / run workflow
* project structure discipline
* local build confidence

---

# File Structure

```text
Engineering_C++/
└── phase0/
    └── day1_cpp_reboot/
        ├── print_vector.cpp
        ├── README.md
        └── bug_log.md
```

---

# Source Code Purpose

## `print_vector.cpp`

Build a reusable function that prints all values inside a `vector<int>`.

Core engineering concepts:

* `#include <vector>`
* `const std::vector<int>&`
* range-based for loop
* `void` function
* modular structure

---

# Compile

```bash
g++ -std=c++17 Engineering_C++/phase0/day1_cpp_reboot/print_vector.cpp -o print_vector
```

---

# Run

## PowerShell / Windows:

```bash
./print_vector
```

## Expected Output:

```text
1 2 3 4 5
```

---

# Key Engineering Lessons

## 1. `void`

`void` means the function performs an action but does not return a value.

Example:

```cpp
void printVector(...)
```

---

## 2. `const &`

```cpp
const std::vector<int>& values
```

Meaning:

* `const`: do not modify input
* `&`: avoid copying the entire vector

This improves:

* safety
* readability
* efficiency

---

## 3. Build Workflow

```text
Source Code
→ Compile (`g++`)
→ Executable
→ Run
→ Verify Output
```

---

# Common Bugs

* Missing `#include <vector>`
* Missing `std::`
* Wrong file path
* Compile command typo
* Using `int` when `long long` is safer
* Writing everything inside `main` instead of functions

---

# Bug Log Reflection

## Day 1 Success:

* Correct project path
* Successful compile
* Successful execution
* Correct output
* First modular C++ function completed

---

# Stretch Goal

Upgrade:

```cpp
std::vector<int>
```

To:

```cpp
std::vector<long long>
```

Why:
Connect competitive overflow awareness with engineering structure.

---

# Today’s Win Condition

```text
I did not just write a simple print program.
I rebuilt:
Code structure + compile workflow + modular engineering discipline.
```

---

# Next Phase Preview

Phase 0 Day 2:

* `string`
* `max streak`
* sequence scan
* CSES Repetitions
