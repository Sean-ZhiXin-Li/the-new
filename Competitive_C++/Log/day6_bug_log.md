## Bug 1 — Heredoc Did Not Exit

### Problem

The terminal kept showing:

>

and did not run the program.

### Cause

EOF was not entered correctly.

The shell was still waiting for the heredoc ending marker.

### Fix

Type:

EOF

on a separate line.

### Lesson

Heredoc requires an exact ending marker.

Linux shell waits for the closing token before executing the command.

## Bug 2 — Comparator Direction Mistake

### Problem

The sorting order was different from the expected output.

### Cause

The comparator direction was reversed.

Using:

a.second < b.second

creates ascending order.

Using:

a.second > b.second

creates descending order.

### Fix

Use:

return a.second > b.second;

for higher priority first.

### Lesson

Comparator directly defines system priority rules.

## Bug 3 — Forgot Compilation After Code Change

### Problem

Program output did not change after modifying the source code.

### Cause

The executable binary was not recompiled.

### Fix

Run:

g++ -std=c++17 -Wall -Wextra -O2 ...

again after changing the source file.

### Lesson

C++ requires recompilation after source code changes.

## Bug 4 — Used | Instead of ||

### Problem

The compiler produced a warning related to:

|

inside an if condition.

### Cause

| is bitwise OR.

The correct operator for logical conditions is:

||

### Fix

Replace:

|

with:

||

### Lesson

Bitwise operators and logical operators are different.

Warnings should always be investigated carefully.

# Common Risks

- Forgetting to recompile
- Wrong comparator direction
- Missing include headers
- Invalid vector index
- Infinite loop
- Incorrect sorting assumptions