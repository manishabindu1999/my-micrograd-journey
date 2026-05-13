# Value Class

## What is the Value class?

The Value class is the core data structure in micrograd.

It represents:

- a numerical value
- its gradient
- the operation that created it
- connections in the computational graph

Every mathematical operation produces a new Value object.

---

## Why the Value Class Matters

The Value class allows the system to:

- build computational graphs
- track operations automatically
- store gradients
- perform backpropagation

This is the foundation of autodiff systems.

---

## Core Components

A Value object usually stores:

- data
- grad
- _prev
- _op
- _backward

---

## data

Stores the actual numerical value.

Example:

Value(2.0)

means:

data = 2.0

---

## grad

Stores the gradient.

Example:

dL/dx

Initially gradients are usually:

grad = 0

After backpropagation:
the gradient gets updated.

---

## _prev

Stores parent nodes in the computational graph.

Example:

c = a + b

Then:

c._prev = {a, b}

This creates graph connections.

---

## _op

Stores the operation that created the node.

Examples:

+
*
tanh
relu

Useful for debugging and visualization.

---

## _backward

Stores the local gradient function.

Each operation defines how gradients flow backward.

Example:

For:

c = a + b

local gradients are:

dc/da = 1
dc/db = 1

---

## Computational Graph Example

Suppose:

c = a * b

The graph stores:

- value of c
- operation "*"
- parents a and b
- backward rule for multiplication

---

## Why This Design Is Powerful

The Value class combines:

- data
- graph structure
- differentiation logic

into a single object.

Modern deep learning frameworks use much larger versions of this idea internally.

---

## Goal

Build a tiny autodiff engine by implementing the Value class from scratch.