# Layers in Neural Networks

## What is a layer?

A layer is a collection of neurons operating together.

Each neuron receives inputs and produces an output.

The outputs from one layer become inputs to the next layer.

---

## Why Layers Matter

Single neurons are limited.

By combining many neurons into layers:
neural networks can learn complex patterns.

Layers allow:

- hierarchical feature learning
- abstraction
- deep representations

---

## Layer Structure

Example:

Input Layer:
[x1, x2, x3]

Hidden Layer:
[h1, h2, h3, h4]

Output Layer:
[y]

Each neuron has:

- weights
- bias
- activation function

---

## Forward Pass Through a Layer

A layer performs:

1. weighted sums
2. activation functions
3. output generation

Each neuron computes independently.

---

## Computational Graph

Each neuron creates its own computational graph.

A layer combines many computational graphs together.

This creates larger differentiable systems.

---

## Hidden Layers

Layers between input and output are called hidden layers.

Deep learning models often contain:

- many hidden layers
- millions of neurons
- billions of parameters

---

## Layer Outputs

Suppose a layer has:

4 neurons

Then its output becomes:

[h1, h2, h3, h4]

This vector is passed to the next layer.

---

## Why Deep Networks Work

Different layers learn different abstractions.

Example in image models:

Early layers:
- edges
- textures

Middle layers:
- shapes
- parts

Deep layers:
- objects
- semantic concepts

---

## Backpropagation Through Layers

Gradients flow backward through:

- activations
- neurons
- weights
- inputs

The chain rule propagates gradients layer by layer.

---

## Goal

Implement a Layer class containing multiple neurons.