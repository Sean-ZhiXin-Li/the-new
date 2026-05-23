# CSES 1083_Missing Number

Problem Type: 
Math / Excepted vs. Actual

Complexity: 
O(n)

Initial Bug: 
- Incorrect input (`n + 1` instead of `n - 1`)
- I first considered checking each number from `1` to `n` against the input, which could become `O(n^2)` if implemented with nested loops.
- I mistakenly tried to use `string<long long>`, but `string` is not a numeric numbers.
- I did not immediately recognize the formula `1 + 2 + 3 + ... + n = n * (n + 1) / 2`.

Key Lessons:
- Use mathematical structure before brute force.
- The input has exactly `n - 1` numbers after `n`.
- For this problem, only `actualSum` is needed; no array or string storage is required.
- `expectedSum - actualSum` gives the missing number.