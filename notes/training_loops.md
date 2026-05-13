# Training Loops

## What is a training loop?

A training loop repeatedly trains a neural network by:

1. making predictions
2. computing loss
3. computing gradients
4. updating parameters

This process allows neural networks to learn from data.

---

## Core Training Pipeline

Input
→ Forward Pass
→ Prediction
→ Loss
→ Backward Pass
→ Parameter Updates

This cycle repeats many times.

---

## Forward Pass

The network computes predictions using current parameters.

Example:

prediction = model(x)

---

## Compute Loss

The loss function measures prediction error.

Example:

loss = (prediction - target)^2

The goal is to minimize this loss.

---

## Backward Pass

Backpropagation computes gradients.

Example:

loss.backward()

Gradients tell the network how parameters affect the loss.

---

## Parameter Updates

Parameters are updated using gradients.

Example:

weight = weight - learning_rate * gradient

This improves predictions over time.

---

## Epochs

One complete pass through the dataset is called an epoch.

Training often requires many epochs.

---

## Why Training Loops Matter

Training loops are the engine of deep learning.

They allow:

- pattern learning
- optimization
- neural network improvement

---

## Goal

Implement a complete neural network training loop from scratch.