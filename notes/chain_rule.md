# Chain Rule

## What is the chain rule?

The chain rule is a calculus rule used to compute derivatives through multiple operations.

It is the mathematical foundation of backpropagation.

---

## Core Equation

If:

y = f(x)

and:

L = g(y)

then:

dL/dx = dL/dy * dy/dx

This allows gradients to flow backward through a computational graph.

---

## Intuition

The chain rule answers:

"How does changing x affect the final loss L?"

Even if many intermediate operations exist.

---

## Example

Suppose:

y = 2x

L = y^2

Then:

dL/dy = 2y

dy/dx = 2

So:

dL/dx = 2y * 2 = 4y

---

## Why Chain Rule Matters

Neural networks contain millions or billions of parameters.

The chain rule allows gradients to be computed efficiently across all operations.

Without the chain rule:

- deep learning would not work
- transformers could not train
- modern AI would not exist

---

## Things To Study Next

- local gradients
- global gradients
- partial derivatives
- computational graphs
- autodiff systems