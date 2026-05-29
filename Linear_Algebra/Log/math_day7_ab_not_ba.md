# Math Day7 — AB Is Not Usually BA

## Objective

Understand why:

```text
AB ≠ BA
```

and why matrix multiplication represents transformation composition.

This is one of the most important ideas in linear algebra because future topics such as:

```text
Control systems
Robotics
Computer graphics
Optimization
Neural networks
Spacecraft dynamics
```

all rely on applying transformations in the correct order.

---

# Core Idea

Matrix multiplication represents:

```text
Transformation composition
```

For matrices:

```text
A
B
```

and vector:

```text
v
```

we have:

```text
ABv = A(Bv)
```

Meaning:

```text
First apply B
Then apply A
```

The rightmost transformation happens first.

---

# Example Setup

Vector:

```text
v = [1, 2]
```

Transformation A:

```text
A = [[2, 0],
     [0, 1]]
```

Meaning:

```text
Scale x by 2
Keep y unchanged
```

So:

```text
A([x, y]) = [2x, y]
```

---

Transformation B:

```text
B = [[1, 1],
     [0, 1]]
```

Meaning:

```text
New x = x + y
Keep y unchanged
```

So:

```text
B([x, y]) = [x + y, y]
```

This transformation is called a shear.

---

# Compute A(Bv)

## Step 1

Apply B first:

```text
v = [1, 2]

Bv = [1 + 2, 2]
    = [3, 2]
```

---

## Step 2

Apply A:

```text
A(Bv)
= A([3, 2])

= [2 × 3, 2]

= [6, 2]
```

Result:

```text
A(Bv) = [6, 2]
```

---

# Compute B(Av)

## Step 1

Apply A first:

```text
Av = [2 × 1, 2]

   = [2, 2]
```

---

## Step 2

Apply B:

```text
B(Av)

= [2 + 2, 2]

= [4, 2]
```

Result:

```text
B(Av) = [4, 2]
```

---

# Compare Results

We obtained:

```text
A(Bv) = [6, 2]

B(Av) = [4, 2]
```

These are different.

Therefore:

```text
A(Bv) ≠ B(Av)
```

which means:

```text
ABv ≠ BAv
```

for this vector.

Therefore:

```text
AB ≠ BA
```

in general.

---

# Why Does This Happen?

Because:

```text
Transformation order matters.
```

Consider:

```text
Shear then Scale
```

versus:

```text
Scale then Shear
```

These are physically different actions.

Just like:

```text
Turn a spacecraft
then accelerate
```

is different from:

```text
Accelerate
then turn the spacecraft
```

The order changes the final state.

---

# Matrix View

Compute:

```text
AB
```

First:

```text
A = [[2, 0],
     [0, 1]]

B = [[1, 1],
     [0, 1]]
```

Then:

```text
AB = [[2, 2],
      [0, 1]]
```

---

Compute:

```text
BA
```

Result:

```text
BA = [[2, 1],
      [0, 1]]
```

Clearly:

```text
AB ≠ BA
```

because:

```text
[[2, 2],
 [0, 1]]

≠

[[2, 1],
 [0, 1]]
```

---

# Connection to Math51

Key idea:

```text
Matrix multiplication
=
Composition of linear transformations
```

A matrix is not just a table of numbers.

A matrix represents an action.

Matrix multiplication combines actions.

Because actions occur in sequence:

```text
Order matters.
```

Therefore:

```text
AB is usually different from BA.
```

---

# Spacecraft / Control Connection

Future examples:

```text
Rotate velocity vector
then scale thrust
```

versus:

```text
Scale thrust
then rotate velocity vector
```

These operations generally produce different results.

This is why transformation order becomes important in:

```text
Guidance
Navigation
Control
Robotics
Orbit dynamics
```

---

# Key Takeaways

## Rule 1

```text
ABv = A(Bv)
```

Meaning:

```text
Apply B first
Apply A second
```

---

## Rule 2

```text
Transformation order matters.
```

---

## Rule 3

```text
AB ≠ BA
```

in general.

---

# One-Sentence Memory Rule

```text
Matrix multiplication is order-sensitive because transformations are order-sensitive.
```
