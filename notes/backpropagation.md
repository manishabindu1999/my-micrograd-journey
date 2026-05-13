# Backpropagation

## What is backpropagation?

Backpropagation is the algorithm used to compute gradients in neural networks.

It tells us:

"How much did each parameter affect the final error?"

The goal is to minimize loss.

---

## Core Idea

If changing a weight increases loss:

- decrease the weight

If changing a weight decreases loss:

- increase the weight

This is optimization using gradients.

---

## Important Equation

The most important quantity in deep learning is:

dL/dw

Meaning:

"How much does changing weight w affect loss L?"

---

## Chain Rule

Backpropagation uses the chain rule from calculus.

Example:

L -> y -> x

Then:

dL/dx = dL/dy * dy/dx

Gradients flow backward through the computational graph.

---

## Why Backpropagation Matters

Without backpropagation:

- neural networks cannot learn
- transformers cannot train
- ChatGPT cannot exist

Backpropagation is the core engine of modern AI.

---

## Things To Study Next

- derivatives
- chain rule
- local gradients
- global gradients
- computational graphs
- autodiff