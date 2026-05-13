# The backward() Engine

## What is backward()?

The backward() function performs backpropagation across the computational graph.

Its job is to:

- traverse the graph
- execute backward functions
- propagate gradients
- compute derivatives for all nodes

This is the core execution engine of autodiff systems.

---

## High-Level Process

The backward engine performs:

1. build topological order
2. initialize output gradient
3. traverse graph backward
4. execute local backward functions
5. accumulate gradients

---

## Step 1 — Build Topological Order

The graph is traversed using DFS.

This creates a dependency-safe execution order.

Forward order:

inputs → output

Backward order:

output → inputs

---

## Step 2 — Initialize Final Gradient

For the final output node:

dL/dL = 1

Example:

loss.grad = 1

This starts gradient propagation.

---

## Step 3 — Reverse Traversal

Nodes are processed in reverse topological order.

This guarantees:

dependent gradients are computed first.

---

## Step 4 — Execute Backward Functions

Each node runs its stored backward function.

Example:

a.grad += local_derivative * upstream_gradient

Gradients flow backward through the graph.

---

## Step 5 — Gradient Accumulation

Gradients are accumulated using:

+=

because multiple paths may contribute to the same node.

---

## Why Gradient Accumulation Matters

Suppose:

a affects loss through multiple paths.

Then:

all gradient contributions must be summed.

This is required for correct backpropagation.

---

## Computational Graph Example

Suppose:

a = 2
b = 3

c = a * b
d = c + 4

Backward order:

d → c → a, b

Each node executes its backward rule.

---

## Why backward() Is Powerful

The backward engine transforms:

- local derivatives
- graph structure
- chain rule

into a complete automatic differentiation system.

---

## Goal

Implement a complete backward propagation engine from scratch.