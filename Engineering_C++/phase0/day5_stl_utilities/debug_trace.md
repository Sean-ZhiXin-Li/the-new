# Day5 Debug Trace

## Bug 1

Forgot to declare:

std::map<int, int> frequency;

Reason:
Confused map existence with key existence.

---

## Bug 2

Forgot semicolon after:

return frequency;

---

## Bug 3

Tried:

std::cout << result;

Reason:
pair cannot be directly printed.

Fix:
Use:
result.first
result.second