# Neurons in Neural Networks

## What is a neuron?

A neuron is a small computational unit that:

- receives inputs
- applies weights
- computes a weighted sum
- applies an activation function
- produces an output

Neurons are the building blocks of neural networks.

---

## Basic Neuron Equation

A neuron computes:

y = w1*x1 + w2*x2 + ... + b

Then applies an activation function.

---

## Weighted Sum

Each input has an associated weight.

Example:

x1 = input feature
w1 = importance of x1

Large weight:
strong influence

Small weight:
weak influence

---

## Bias Term

The bias shifts the neuron output.

It helps the neuron learn more flexible decision boundaries.

---

## Activation Function

After computing the weighted sum:

an activation function is applied.

Examples:

- tanh
- ReLU
- sigmoid

Activation functions introduce nonlinearity.

Without nonlinearity:
deep networks become useless.

---

## Computational Graph

A neuron internally creates a computational graph.

Example:

x1*w1 + x2*w2 + b

This graph supports automatic differentiation.

---

## Forward Pass

The neuron:

1. multiplies inputs by weights
2. sums results
3. applies activation
4. produces output

---

## Backward Pass

Backpropagation computes gradients for:

- weights
- inputs
- bias

The neuron learns using gradient descent.

---

## Why Neurons Matter

Large neural networks are built from:

- neurons
- layers
- repeated computation

Transformers and LLMs are extremely large compositions of neuron-like operations.

---

## Goal

Implement a tiny neuron using Value objects and autodiff.