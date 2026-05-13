# Backward Functions in Autodiff

## What is a backward function?

A backward function defines how gradients flow backward through an operation.

Each operation stores its own local gradient rule.

During backpropagation:
these backward functions are executed in reverse order.

---

## Core Idea

Every operation knows:

"How should gradients propagate to my inputs?"

Example:

c = a + b

The backward function distributes gradients to:

- a
- b

---

## Example: Addition

Suppose:

c = a + b

Local derivatives:

dc/da = 1
dc/db = 1

Backward logic:

a.grad += out.grad
b.grad += out.grad

Both inputs receive the upstream gradient.

---

## Example: Multiplication

Suppose:

c = a * b

Local derivatives:

dc/da = b
dc/db = a

Backward logic:

a.grad += b.data * out.grad

b.grad += a.data * out.grad

The upstream gradient is scaled using local derivatives.

---

## Why Backward Functions Matter

Backward functions allow:

- modular autodiff
- automatic gradient propagation
- computational graph traversal
- neural network training

Each node becomes responsible for its own gradient computation.

---

## Local Gradient + Upstream Gradient

Core backpropagation idea:

new gradient = local derivative × upstream gradient

This is repeated across the entire graph.

---

## Computational Graph Flow

Forward pass:

inputs → operations → output

Backward pass:

output gradients → operations → input gradients

Gradients flow backward through stored backward functions.

---

## Why This Design Is Powerful

Each operation stores:

- forward computation
- graph structure
- local gradient logic

This creates a fully automatic differentiation system.

---

## Goal

Implement local backward functions for each operation in the Value class.