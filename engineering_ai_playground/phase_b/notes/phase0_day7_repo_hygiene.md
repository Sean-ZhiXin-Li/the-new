# Phase0 Day7 — Repo Hygiene

## Objective

Verify that the repository is clean, reproducible, and safe to commit.

Today is not about building new functionality.

Today is about:

```text
repo hygiene
artifact inspection
Git discipline
Linux inspection workflow
```

---

# What I Found

## Build Artifacts

Search commands:

```bash
find . -name "*.exe"
find . -name "*.out"
find . -type d -name "cmake-build-debug"
```

Results:

```text
No .exe files found.
No .out files found.
No cmake-build-debug directory found.
```

Interpretation:

```text
No compiled C++ binaries or build directories are currently present inside the repository.
```

---

## Python Cache

Search command:

```bash
find . -name "__pycache__"
```

Result:

```text
engineering_ai_playground/phase_b/src/__pycache__
```

Interpretation:

```text
A local Python cache directory existed.
```

Action:

```text
Removed local cache directory.
```

---

## Git Status

Command:

```bash
git status --short
```

Observed files:

```text
Day7 notes
Math deliverables
AI deliverables
Competitive C++ summary
Engineering C++ review
```

Interpretation:

```text
Only source files, notes, and deliverables are pending.

No generated binaries are being tracked.
```

---

# What Should Not Be Committed

Compiled artifacts:

```text
*.exe
*.out
*.o
```

Build directories:

```text
build/
cmake-build-debug/
```

Python cache:

```text
__pycache__/
.pytest_cache/
```

IDE-specific files:

```text
.vscode/
.idea/
```

Generated outputs:

```text
temporary logs
machine-specific artifacts
```

Rule:

```text
Git should track source code and documentation,
not generated products.
```

---

# Current .gitignore Status

Existing protection:

```text
*.exe
*.out
*.o

__pycache__/
*.pyc

build/
cmake-build-debug/
```

Additional entries added:

```text
.pytest_cache/
.vscode/
```

Interpretation:

```text
The repository now covers the most common local artifact risks.
```

---

# Why Build Artifacts Are Dangerous

Build artifacts are generated files.

Problems:

```text
Machine dependent
Can become stale
Increase repository noise
Hide meaningful source changes
Complicate code reviews
```

Example:

```text
Source code changes should be reviewed.

Compiled binaries should be regenerated.
```

Important engineering principle:

```text
Source files are the source of truth.

Generated files are disposable.
```

---

# Commands Used

```bash
pwd

git status --short

find . -name "*.exe"
find . -name "*.out"
find . -name "__pycache__"
find . -name ".pytest_cache"
find . -type d -name "cmake-build-debug"

cat .gitignore
```

---

# Engineering Connection

Week 1 progression:

```text
Day1
System map

Day2
Controlled input

Day3
Consistency check

Day4
Git recovery

Day5
Linux trace

Day6
Repository search

Day7
Repository hygiene
```

Engineering workflow progression:

```text
understand
→ control
→ verify
→ recover
→ inspect
→ search
→ maintain
```

---

# Next Cleanup Action

Before every future commit:

```bash
git status
```

Verify:

```text
No binaries
No cache directories
No build folders
Only meaningful source changes
```

Recommended C++ workflow:

```bash
g++ -std=c++17 -Wall -Wextra -O2 file.cpp -o /tmp/program
```

instead of storing binaries inside the repository.

---

# Key Lesson

```text
A clean repository is part of engineering quality.

Good engineers do not only write code.

They also maintain reproducibility, traceability, and repository health.
```

---

# Day7 Win Condition

```text
✔ No tracked build artifacts

✔ .gitignore reviewed

✔ Cache directories identified

✔ Repository status inspected

✔ Deliverables separated from generated files

✔ Repository ready for clean commits
```

---

## Reproducibility Connection

A clean repository improves reproducibility.

Benefits:

- easier debugging
- cleaner Git history
- simpler code review
- more reliable experiment tracking

Repository hygiene supports scientific reproducibility.

---

# One-Sentence Summary

```text
Today I learned that repository maintenance is an engineering responsibility, and that version control should track source-of-truth artifacts rather than generated products.
```
