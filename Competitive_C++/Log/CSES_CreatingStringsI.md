CSES 1622 — Creating Strings I

Problem Type:
DFS / Backtracking / Permutation / Duplicate Control

Complexity:
Time: O(k * n), where k is the number of unique permutations.
Worst case: O(n! * n), because k can be n! when all characters are distinct.
Space: O(k * n) for storing all result strings, plus O(n) recursion depth and used[].

Initial Bugs:
- I did not understand why search() calls itself.
- I did not understand when path.pop_back() and used[i] = false are executed.
- I first printed each complete string directly, but CSES requires printing the total number first.
- I generated duplicate strings for input like abb.
- I got a compiler warning from comparing int i with s.size().

Key Lessons:
- search() means entering the next recursion layer.
- push_back means choosing one character for the current position.
- pop_back means undoing the choice after recursion returns.
- used[i] prevents using the same character index twice.
- sort(s.begin(), s.end()) is required before duplicate skipping.
- Duplicate rule: if the current character equals the previous one and the previous one is not used, skip the current character.
- The duplicate rule prevents choosing the later duplicate before the earlier duplicate at the same recursion level.
- Store answers in vector<string> results first, then print results.size() before printing all strings.
- Use static_cast<int>(s.size()) or store int n = s.size() to avoid signed / unsigned comparison warnings.