# Gradients

## What is a gradient?

A gradient measures how much a variable affects the final loss.

In deep learning, gradients tell neural networks how to update parameters.

---

## Important Equation

dL/dw

Meaning:

"How much does changing weight w change loss L?"

---

## Intuition

If a gradient is:

Positive:
- increasing the weight increases loss

Negative:
- increasing the weight decreases loss

Small:
- parameter has little effect

Large:
- parameter strongly affects loss

---

## Why Gradients Matter

Neural networks learn by adjusting weights using gradients.

The optimization process repeatedly:

1. computes gradients
2. updates parameters
3. reduces loss

This process is called gradient descent.

---

## Gradient Descent Update Rule

new_weight = old_weight - learning_rate * gradient

---

## Example

Suppose:

gradient = 0.5
learning_rate = 0.1

Then:

new_weight = old_weight - 0.05

The parameter moves slightly in the direction that reduces loss.

---

## Why Gradients Are Powerful

Gradients allow:

- neural network training
- transformer optimization
- image generation models
- language model learning

Without gradients:
modern AI systems cannot learn.

---

## Things To Study Next

- gradient descent
- exploding gradients
- vanishing gradients
- optimization
- SGD
- Adam optimizer