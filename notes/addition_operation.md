# Addition Operation in Autodiff

## Goal

Implement addition between Value objects.

Example:

c = a + b

The system should:

- compute the new value
- create a graph connection
- store backward gradient logic

---

## Forward Pass

Suppose:

a = 2
b = 3

Then:

c = a + b = 5

The forward pass computes the numerical result.

---

## Computational Graph

Graph:

a ----+
       \
        c
       /
b ----+

The output node c stores:

- value = 5
- parents = {a, b}
- operation = "+"

---

## Local Gradients

For:

c = a + b

derivatives are:

dc/da = 1
dc/db = 1

Addition distributes gradients equally.

---

## Backward Pass

Suppose:

dL/dc = 4

Then:

dL/da = 4 * 1 = 4
dL/db = 4 * 1 = 4

Both inputs receive the same gradient.

---

## Why Addition Matters

Addition seems simple, but it teaches:

- graph construction
- local gradient rules
- gradient propagation
- autodiff mechanics

All complex neural networks are built from simple operations like this.

---

## Operator Overloading

Python allows custom behavior for operators.

Example:

__add__()

This lets:

a + b

create computational graph nodes automatically.

---

## Goal

Implement:

- Value.__add__()
- graph connections
- backward gradient logic