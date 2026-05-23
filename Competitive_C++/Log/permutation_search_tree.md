# Permutation Search Tree for `abb`

## 1. Problem Setup

We want to generate all unique permutations of the string:

```text
abb
```

After sorting, the string is still:

```text
index: 0 1 2
char : a b b
```

So we have:

```text
s[0] = 'a'
s[1] = 'b'
s[2] = 'b'
```

The two `b` characters are equal in value, but they have different indices.

The goal is to generate:

```text
abb
bab
bba
```

without generating duplicate permutations.

---

## 2. Core Duplicate-Skip Rule

The standard duplicate-skip rule is:

```cpp
if (i > 0 && s[i] == s[i - 1] && !used[i - 1]) {
    continue;
}
```

Meaning:

```text
If the current character is the same as the previous character,
and the previous same character has not been used yet,
then skip the current character.
```

For `abb`, this rule mainly controls whether `b(2)` can be chosen before `b(1)`.

---

## 3. Main Intuition

The key idea is:

```text
At the same recursion level, among unused equal characters, only the earliest unused copy is allowed to start a branch.
The earlier duplicate character must be chosen before the later duplicate character.
```

So:

```text
b(1) may branch before b(2).
b(2) may not branch before b(1) at the same level.
```

This avoids duplicate branches in the search tree.

---

## 4. Full Search Tree

```text
s = "abb"  (sorted)

Root:
path = ""
used = [F, F, F]

""
├── a(0) -> "a"
│   used = [T, F, F]
│
│   ├── b(1) -> "ab"
│   │   used = [T, T, F]
│   │
│   │   └── b(2) -> "abb" ✅
│   │       used = [T, T, T]
│   │
│   └── b(2) -> SKIP
│       reason:
│       s[2] == s[1] == 'b'
│       used[1] == false
│       choosing b(2) before b(1) would create a duplicate branch
│
├── b(1) -> "b"
│   used = [F, T, F]
│
│   ├── a(0) -> "ba"
│   │   used = [T, T, F]
│   │
│   │   └── b(2) -> "bab" ✅
│   │       used = [T, T, T]
│   │
│   └── b(2) -> "bb"
│       used = [F, T, T]
│
│       └── a(0) -> "bba" ✅
│           used = [T, T, T]
│
└── b(2) -> SKIP
    reason:
    s[2] == s[1] == 'b'
    used[1] == false
    choosing b(2) before b(1) at the root level would create a duplicate branch
```

---

## 5. Why Root `b(2)` Is Skipped

At the root level:

```text
path = ""
used = [F, F, F]
choices: a(0), b(1), b(2)
```

When the loop reaches `b(2)`, the condition becomes:

```text
i = 2
s[2] == s[1]
used[1] == false
```

So the skip rule is triggered.

This means:

```text
Do not choose the second b before the first b at the same recursion level.
```

If we allowed this branch:

```text
"" -> b(2)
```

it would generate the same string-level results as:

```text
"" -> b(1)
```

The indices are different, but the characters are identical, so the final permutations would be duplicates.

---

## 6. Why `"a" -> b(2)` Is Skipped

After choosing `a(0)`, we have:

```text
path = "a"
used = [T, F, F]
remaining choices: b(1), b(2)
```

At this recursion level, `b(1)` and `b(2)` are still duplicate choices.

When the loop reaches `b(2)`, the condition is again:

```text
i = 2
s[2] == s[1]
used[1] == false
```

So `b(2)` is skipped.

The branch:

```text
"a" -> b(2)
```

would duplicate the branch:

```text
"a" -> b(1)
```

Therefore only `b(1)` is allowed to branch first at this level.

---

## 7. Why `"b" -> b(2)` Is Not Skipped

After choosing `b(1)`, we have:

```text
path = "b"
used = [F, T, F]
remaining choices: a(0), b(2)
```

Now when the loop reaches `b(2)`, the condition checks:

```text
i = 2
s[2] == s[1]
used[1] == true
```

Because `used[1] == true`, the skip rule does not trigger.

This means:

```text
The earlier b has already been used.
Now it is legal to use the later b.
```

So this branch is valid:

```text
"b" -> b(2) -> "bb"
```

This eventually produces:

```text
bba
```

---

## 8. Which Branches Are Skipped?

There are two skipped branches in this search tree.

### Skipped Branch 1

```text
"" -> b(2)
```

Reason:

```text
At the root level, b(1) and b(2) are duplicate choices.
Only b(1) is allowed to branch first.
```

### Skipped Branch 2

```text
"a" -> b(2)
```

Reason:

```text
At the "a" level, b(1) and b(2) are still duplicate choices.
Only b(1) is allowed to branch first.
```

---

## 9. What Would Happen Without the Skip Rule?

Without the skip rule, the algorithm distinguishes b(1) and b(2) by index.
So it creates different index-level paths, but those paths collapse into the same string-level permutation.

It would generate duplicate paths such as:

```text
choose b(1), then b(2)
choose b(2), then b(1)
```

Both produce the same visible string:

```text
bb
```

For the full permutation problem, this would create repeated outputs.

The skip rule prevents these repeated branches before they are fully expanded.

---

## 10. Final Unique Permutations

The final valid leaves are:

```text
abb
bab
bba
```

So the unique permutations of `abb` are:

```text
["abb", "bab", "bba"]
```

---

## 11. Short Summary

The duplicate-skip rule:

```cpp
if (i > 0 && s[i] == s[i - 1] && !used[i - 1]) {
    continue;
}
```

means:

```text
If the current character is a duplicate of the previous character,
and the previous duplicate has not been used in the current path,
then the current character must be skipped.
```

For `abb`, this prevents `b(2)` from being chosen before `b(1)` at the same recursion level.

The key mental model is:

```text
Same-level duplicate choices are skipped.
Deeper-level repeated characters are allowed only after the earlier duplicate has already been used.
```

---

## 12. One-Sentence Memory Rule

```text
For duplicate characters, the later duplicate can only be used after the earlier duplicate has already been used.
```

Or even shorter:

```text
Same level: skip duplicates.
Next level: allow duplicates after the earlier copy is used.
```
