> **Navigation:** [<-- Preparing Non-Tabular Data](02-beyond-tabular-prep.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Regression: Interpretation and Assumptions -->](04-regression-depth.md)

---

# Logistic Regression

**Requires**: [Linear Regression](../part-05-supervised-learning/02-linear-regression.md)

**Motivation**: You know how to predict a number using linear regression. Now the target is binary: yes or no, positive or negative. The obvious shortcut is to apply linear regression anyway and round the output. This turns out to be a bad idea — and understanding why reveals something deep about how machine learning models are trained and how they connect to neural networks.

> In this optional nugget you will learn why a smooth probability output is more useful than a hard threshold, how the sigmoid function converts any real number into a probability, and how logistic regression is a direct conceptual building block for the neural networks you will encounter in Part VIII.

> **Context:** This nugget covers **classification** — specifically, binary classification with probabilistic outputs. It also serves as a conceptual bridge from linear models to neural networks.

## Table of Contents

- [Sigmoid as a Differentiable Threshold](#sigmoid-as-a-differentiable-threshold)
- [Cross-Entropy Loss](#cross-entropy-loss)
- [Bridge from Linear Models to Neural Networks](#bridge-from-linear-models-to-neural-networks)
- [Summary](#summary)

## Sigmoid as a Differentiable Threshold

Apply a linear model to a classification problem and you get a continuous output ranging from $-\infty$ to $+\infty$. To make a binary decision, you would apply a step function: if $h_w(\mathbf{x}) > 0.5$, predict class 1; otherwise predict class 0.

The problem: the gradient of a step function is zero almost everywhere. Gradient descent needs a gradient to move. Where the gradient is zero, the weights do not update.

The fix is to replace the step function with a smooth approximation, the **sigmoid function** (also called the logistic function):

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

where $z = w_0 + w_1 x_1 + \cdots + w_n x_n$ is the linear combination of features and weights. The sigmoid maps any real number to the open interval $(0, 1)$, and its output can be interpreted directly as a class probability.

[Figure: Side-by-side comparison of the step function (non-differentiable, gradient = 0 everywhere except the discontinuity) and the sigmoid function (smooth, differentiable, gradient largest near $z = 0$). Makes the motivation for replacing one with the other concrete.]

$\sigma(z)$ is close to 1 for large positive $z$ (the model is confident about class 1) and close to 0 for large negative $z$ (the model is confident about class 0). At $z = 0$ the output is exactly 0.5: maximum uncertainty.

---

## Cross-Entropy Loss

With a probabilistic output you need a loss function that measures how wrong a probability estimate is — not how wrong a number is. Mean squared error, which makes sense for regression, is poorly suited to probabilities.

The appropriate choice is **cross-entropy loss** (also called log loss):

$$L = -\bigl[y \log(\hat{p}) + (1 - y) \log(1 - \hat{p})\bigr]$$

where $y \in \{0, 1\}$ is the true label and $\hat{p} = \sigma(z)$ is the model's predicted probability.

When $y = 1$: the loss is $-\log(\hat{p})$. A predicted probability of 0.99 gives near-zero loss. A predicted probability of 0.01 gives a large loss — the model was confidently wrong.

When $y = 0$: the loss is $-\log(1 - \hat{p})$. The same logic applies in reverse.

Cross-entropy is differentiable with respect to the weights, so gradient descent can minimize it. The gradient turns out to have a clean form that makes the weight updates efficient to compute.

---

## Bridge from Linear Models to Neural Networks

Look at what logistic regression does: compute a linear combination of inputs, apply a non-linear function (sigmoid), output a probability. This is exactly the computation of a single artificial neuron.

**Logistic regression is a neural network with no hidden layers** — just an input layer connected directly to a single output neuron with a sigmoid activation.

To build a neural network with one hidden layer, you stack logistic regression units: the outputs of one layer become the inputs of the next. The same gradient descent optimization applies, extended across layers by the chain rule (backpropagation).

[Figure: Progression from logistic regression (input layer connected to a single sigmoid output) to a shallow neural network (input layer, one hidden layer of sigmoid units, output layer). Arrows indicate the shared optimization framework.]

This means everything you have learned about logistic regression scales directly: the sigmoid activation (or a variant), the cross-entropy loss, gradient descent with a learning rate, and the risk of overfitting. The machinery is the same. The scale is different.

*See also: [🖝 Part VIII: When Simple Fails — Deep Learning](../part-08-deep-learning/00-index.md) for the full treatment.*

---

## Summary

- The sigmoid function converts a linear model's unbounded output into a probability. It is differentiable everywhere, which makes gradient descent applicable.
- Cross-entropy loss is the appropriate loss function for classification with probabilistic outputs. It penalizes confident wrong predictions heavily.
- Logistic regression is a single neuron with a sigmoid activation. Stacking such units produces a neural network. The same optimization framework scales to arbitrary depth.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Preparing Non-Tabular Data](02-beyond-tabular-prep.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Regression: Interpretation and Assumptions -->](04-regression-depth.md)

Script v1.4 (2026-06-10) · FGN
