# Topological Sorting in Autodiff

## What is topological sorting?

Topological sorting determines the correct order to process nodes in a computational graph.

In autodiff systems:
the backward pass must process nodes in reverse dependency order.

---

## Why Order Matters

Suppose:

a -> b -> c -> loss

During backpropagation:

loss gradients must be computed first.

Then:

c
b
a

If nodes are processed in the wrong order:
gradients become incorrect.

---

## Forward Pass

Operations execute:

inputs → output

Example:

a = 2
b = 3

c = a * b
d = c + 4

Order:

a, b → c → d

---

## Backward Pass

Gradients flow backward:

d → c → a, b

The graph must be traversed in reverse topological order.

---

## Dependency Rule

A node can only run backward after all nodes depending on it are processed.

This guarantees correct gradient accumulation.

---

## Example Graph

a ----*
       \
        c ----+
              \
               d
              /
4 -----------+

Forward order:

a, b → c → d

Backward order:

d → c → a, b

---

## Why Topological Sorting Matters

Without topological sorting:

- gradients may be incomplete
- graph traversal breaks
- autodiff becomes incorrect

Modern frameworks rely heavily on graph ordering.

---

## DFS Traversal

Micrograd builds topological order using:

Depth First Search (DFS)

The graph is recursively traversed before backward execution.

---

## Reverse Topological Order

Backward propagation executes:

reversed(topological_order)

This ensures gradients flow correctly.

---

## Goal

Build a correct execution order for backward propagation in the autodiff engine.