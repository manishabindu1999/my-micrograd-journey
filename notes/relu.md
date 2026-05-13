# ReLU Activation Function

## What is ReLU?

ReLU stands for:

Rectified Linear Unit

It is one of the most important activation functions in deep learning.

---

## Equation

f(x) = max(0, x)

---

## Behavior

If x > 0:
output = x

If x < 0:
output = 0

---

## Why ReLU Matters

ReLU helps deep networks train efficiently.

Advantages:

- simple
- fast
- computationally efficient

---

## Why ReLU Became Popular

Older activations suffered from vanishing gradients.

ReLU reduced this problem.

This enabled very deep neural networks.

---

## Goal

Implement ReLU activation inside the autodiff engine.