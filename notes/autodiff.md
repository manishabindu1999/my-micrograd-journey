# Automatic Differentiation (Autodiff)

## What is autodiff?

Automatic differentiation is a technique for automatically computing gradients through computational graphs.

Instead of manually calculating derivatives for every operation, the system computes them automatically.

---

## Why Autodiff Matters

Modern neural networks contain millions or billions of parameters.

Manually computing gradients would be impossible.

Autodiff allows frameworks like PyTorch to:

- build computational graphs
- track operations
- compute gradients automatically
- train neural networks efficiently

---

## Core Idea

During the forward pass:

operations are recorded into a computational graph.

During the backward pass:

gradients flow backward through the graph using the chain rule.

---

## Forward Pass

Example:

a = 2
b = 3

c = a * b

d = c + 4

The system records:

- multiplication
- addition
- dependencies between variables

---

## Backward Pass

Autodiff computes:

dL/da
dL/db
dL/dc

using local gradient rules and the chain rule.

---

## Computational Graph

Example graph:

a ----*
       \
        + ---- d
       /
b ----*

4 --------/

Each node stores:

- value
- operation
- parents
- gradient

---

## Why Autodiff Is Powerful

Autodiff powers:

- neural network training
- transformers
- diffusion models
- reinforcement learning
- scientific machine learning

Without autodiff:
modern deep learning frameworks would not exist.

---

## Important Concepts

- forward pass
- backward pass
- computational graph
- chain rule
- local gradients
- graph traversal

---

## Goal

Build a tiny autodiff engine from scratch like micrograd.