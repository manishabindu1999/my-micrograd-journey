# Multilayer Perceptron (MLP)

## What is an MLP?

An MLP (Multilayer Perceptron) is a neural network made of multiple layers of neurons.

It consists of:

- input layer
- hidden layers
- output layer

Each layer transforms the data into higher-level representations.

---

## Basic Structure

Example:

Input → Hidden Layer → Hidden Layer → Output

This creates a deep computational graph.

---

## Why MLPs Matter

MLPs are one of the foundational neural network architectures.

They introduced key ideas used in modern deep learning:

- layered computation
- nonlinear transformations
- gradient-based learning
- hierarchical representations

---

## Forward Pass

During the forward pass:

1. inputs pass through neurons
2. weighted sums are computed
3. activation functions are applied
4. outputs flow to the next layer

Eventually the network produces a prediction.

---

## Example Architecture

Suppose:

Input size = 3

Hidden layers:
[4, 4]

Output size:
1

Architecture:

3 → 4 → 4 → 1

---

## Computational Graph

An MLP creates a massive computational graph composed of:

- additions
- multiplications
- activations
- neuron outputs

Autodiff computes gradients across the entire graph automatically.

---

## Backpropagation in MLPs

The backward pass computes gradients for:

- weights
- biases
- neuron outputs
- activations

Gradients flow backward layer by layer.

---

## Learning Process

Training loop:

1. forward pass
2. compute loss
3. backward pass
4. update parameters

This process repeats many times.

---

## Why Deep Networks Work

Different layers learn different abstractions.

Early layers:
simple patterns

Deep layers:
complex representations

This hierarchical learning is the core strength of deep learning.

---

## Goal

Implement a complete MLP using:

- Value objects
- neurons
- layers
- autodiff