# Multiplication Operation in Autodiff

## Goal

Implement multiplication between Value objects.

Example:

c = a * b

The system should:

- compute the result
- create graph connections
- store backward gradient logic

---

## Forward Pass

Suppose:

a = 2
b = 3

Then:

c = a * b = 6

The forward pass computes the numerical output.

---

## Computational Graph

Graph:

a ----*
       \
        c
       /
b ----*

The output node c stores:

- value = 6
- parents = {a, b}
- operation = "*"

---

## Local Gradients

For:

c = a * b

derivatives are:

dc/da = b
dc/db = a

This is different from addition.

The gradient depends on the opposite input.

---

## Example

Suppose:

a = 2
b = 3

Then:

dc/da = 3
dc/db = 2

---

## Backward Pass

Suppose:

dL/dc = 4

Then:

dL/da = 4 * 3 = 12
dL/db = 4 * 2 = 8

Gradients are multiplied using the chain rule.

---

## Why Multiplication Matters

Multiplication teaches:

- parameter interactions
- gradient scaling
- chain rule mechanics
- nonlinear gradient flow

Modern neural networks rely heavily on multiplication operations.

---

## Backward Logic

During backward propagation:

a.grad += b.data * out.grad

b.grad += a.data * out.grad

The upstream gradient is distributed using local derivatives.

---

## Why This Is Important

This operation demonstrates how gradients propagate through computational graphs.

This is the heart of neural network training.

---

## Goal

Implement:

- Value.__mul__()
- graph tracking
- local backward rules
- gradient propagation