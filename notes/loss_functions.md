# Loss Functions

## What is a loss function?

A loss function measures how wrong a neural network prediction is.

It converts prediction quality into a numerical value.

Small loss:
good prediction

Large loss:
bad prediction

---

## Why Loss Functions Matter

Neural networks learn by minimizing loss.

The optimizer repeatedly adjusts parameters to reduce the loss value.

The entire training process is driven by loss minimization.

---

## Prediction Pipeline

Input
→ Neural Network
→ Prediction
→ Loss Function
→ Error Signal

The loss becomes the starting point for backpropagation.

---

## Example

Suppose:

true value = 5
predicted value = 3

The loss function measures the difference between them.

---

## Mean Squared Error (MSE)

One of the most common loss functions:

MSE = (prediction - target)^2

Large errors are penalized strongly.

---

## Why Squaring Helps

Squaring:

- removes negative signs
- penalizes large mistakes more heavily
- creates smooth gradients

This helps optimization.

---

## Computational Graph

Loss functions become the final node in the computational graph.

Example:

prediction → subtraction → square → loss

Backpropagation starts from the loss node.

---

## Backpropagation

The loss gradient is computed first:

dL/dprediction

Then gradients flow backward through the network.

---

## Optimization Goal

Training tries to find parameters that minimize loss.

This is an optimization problem.

---

## Why Loss Functions Matter in AI

Different AI tasks use different losses.

Examples:

Regression:
- Mean Squared Error

Classification:
- Cross Entropy

Language Models:
- Token prediction loss

---

## Goal

Implement a simple loss function for neural network training.