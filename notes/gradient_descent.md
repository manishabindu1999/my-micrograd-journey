# Gradient Descent

## What is gradient descent?

Gradient descent is an optimization algorithm used to minimize loss.

It updates neural network parameters using gradients.

---

## Core Idea

If a parameter increases loss:
decrease it.

If a parameter decreases loss:
increase it.

---

## Update Rule

new_weight = old_weight - learning_rate * gradient

---

## Why It Works

Gradients point toward increasing loss.

Gradient descent moves in the opposite direction.

This reduces error over time.

---

## Learning Process

Repeated steps:

1. compute predictions
2. compute loss
3. compute gradients
4. update parameters

This gradually improves the model.

---

## Why Gradient Descent Matters

Gradient descent powers:

- neural network training
- transformers
- diffusion models
- language models

Without it:
deep learning would not work.

---

## Goal

Understand how optimization improves neural network performance.