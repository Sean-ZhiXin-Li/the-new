# Phase0 Day6 — Composition of Transformations

## Core Objective

Day5 idea:

Matrix = transformation rule

Day6 idea:

Matrix multiplication = composition of transformations

The goal today is not matrix multiplication mechanics.

The goal today is:

understanding why

ABv = A(Bv)

represents sequential transformations.

---

# Main Intuition

A matrix represents a transformation.

Applying one matrix means:

vector
→ transformation
→ new vector

Applying two matrices means:

vector
→ transformation B
→ transformation A
→ final vector

This can be written as:

A(Bv)

---

# Example

## Vector

v = [2,3]

---

## Transformation B

B = [[1,1],
     [0,1]]

Interpretation:

x_new = x + y

y_new = y

This is a shear transformation.

Apply B:

(2,3)

↓

(5,3)

---

## Transformation A

A = [[2,0],
     [0,3]]

Interpretation:

x scaled by 2

y scaled by 3

Apply A:

(5,3)

↓

(10,9)

Therefore:

A(Bv)

=

(10,9)

---

# Composition

Instead of writing:

A(Bv)

we define:

AB

as the combined transformation.

Meaning:

ABv = A(Bv)

The matrix AB represents:

first apply B

then apply A

---

# Important Insight

Matrix multiplication is not primarily about multiplying numbers.

Matrix multiplication represents:

composition of transformations.

A complex transformation can be built from simpler transformations.

---

# Relationship Between Concepts

## Vector

A vector is:

state / representation

Examples:

- position
- velocity
- feature vector
- OrbitEnv observation

---

## Matrix

A matrix is:

a transformation rule

---

## Matrix Multiplication

Matrix multiplication is:

composition of transformation rules

---

# Connection to AI

Neural networks apply multiple transformations:

input

↓

layer1

↓

layer2

↓

layer3

This can be viewed as:

A(B(Cx))

Multiple matrix transformations form a processing pipeline.

---

# Connection to OrbitEnv

observation

↓

feature transformation

↓

policy transformation

↓

action

This is also a sequence of transformations.

The same abstraction appears in:

- AI
- control systems
- OrbitEnv
- linear algebra

---

# Reflection Questions

## Q1

Can I explain why:

ABv = A(Bv)

without using formulas?

Correct understanding:

AB represents a combined transformation.

---

## Q2

What does matrix multiplication mean?

Correct understanding:

composition of transformations.

---

## Q3

What is the difference between:

Matrix

and

Matrix Multiplication?

Correct understanding:

Matrix = transformation rule

Matrix multiplication = composition of transformation rules

---

# Boundary

Today is only:

composition intuition

Not included today:

- determinant
- inverse
- eigenvalues
- eigenvectors
- proofs

---

## Why Order Matters

ABv means:

first B
then A

BAv means:

first A
then B

In general:

AB ≠ BA

Transformation order matters.

---

# Day6 Final Summary

The most important sentence today is:

A matrix is a transformation.

Matrix multiplication combines multiple transformations into a single transformation.

ABv = A(Bv)

represents sequential transformations.