# Activation Functions

## What is an activation function?

An activation function transforms the output of a neuron.

It introduces nonlinearity into neural networks.

Without activation functions:
deep neural networks would behave like simple linear models.

---

## Basic Neuron

A neuron first computes:

y = w1*x1 + w2*x2 + b

Then applies:

activation(y)

---

## Why Nonlinearity Matters

Without nonlinearity:

multiple neural network layers collapse into a single linear transformation.

This means:

deep networks become useless.

Activation functions allow networks to learn:

- complex patterns
- nonlinear relationships
- hierarchical representations

---

## Common Activation Functions

### ReLU

f(x) = max(0, x)

Most widely used activation in modern deep learning.

Advantages:

- simple
- fast
- helps deep networks train efficiently

---

## tanh

Outputs values between:

-1 and 1

Useful in small neural networks and micrograd examples.

---

## Sigmoid

Outputs values between:

0 and 1

Historically important but less common in deep deep networks.

---

## Computational Graph

Activation functions become nodes in the computational graph.

Example:

x → tanh(x)

The activation stores:

- forward output
- local derivative
- backward logic

---

## Backpropagation Through Activations

Gradients flow through activation functions using the chain rule.

Example:

dL/dx = dL/dy * dy/dx

where:

y = activation(x)

---

## Why Activation Functions Matter

Activation functions enable:

- deep learning
- image recognition
- language models
- transformers
- nonlinear reasoning

Without them:
modern AI systems would not exist.

---

## Goal

Implement activation functions inside the autodiff engine.