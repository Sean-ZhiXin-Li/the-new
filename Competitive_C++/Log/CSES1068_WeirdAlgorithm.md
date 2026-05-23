# CSES 1068_Weird Algorithm

Problem Type:
Simulation

logic:
Repeatedly apply:
if odd → 3n + 1
if even → n / 2

Complexity:
O(number of sequence steps)

Key Bug Risks:
- int overflow
- forgetting final 1
- formatting spaces
- infinite loop

Key Lesson:
Use `long long`for growth safety.