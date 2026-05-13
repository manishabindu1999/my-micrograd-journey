# Computational Graphs

## What is a computational graph?

A computational graph represents mathematical operations as nodes and edges.

Example:

y = (a * b) + c

This becomes:

a ----*
       \
        + ---- y
       /
b ----*

c --------/

## Why computational graphs matter

Computational graphs allow:

- automatic differentiation
- backpropagation
- neural network training

Modern frameworks like PyTorch and TensorFlow use computational graphs internally.

## Important concepts to study

- gradients
- chain rule
- backward pass
- autodiff
- graph traversal

## Goal

Understand how backpropagation works from first principles.