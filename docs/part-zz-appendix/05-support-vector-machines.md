> **Navigation:** [<-- Statistical Significance](04-statistical-significance.md) | [Part Index](00-index.md) | [Main Index](../index.md)

---

# Support Vector Machines

**Requires**: [Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md)

**Motivation**: A decision tree and a logistic regression both classify by drawing a boundary between classes — but they make different choices about where to place it. Support Vector Machines ask a different question: of all the boundaries that separate the classes correctly, which one is farthest from both? That geometric intuition leads to a classifier with strong theoretical backing and surprising performance on high-dimensional data.

> In this optional nugget you will learn how SVMs find the maximum-margin decision boundary, how kernels extend this idea to data that is not linearly separable, and when SVMs are worth considering over simpler alternatives.

> **Context:** This nugget covers **classification**. SVMs can also be applied to regression (support vector regression), but the classification case is the canonical use and the focus here.

TBD: Rework

## Table of Contents

- [The Maximum-Margin Classifier: The Intuition](#the-maximum-margin-classifier-the-intuition)
- [Kernels: Handling Non-Linear Boundaries](#kernels-handling-non-linear-boundaries)
- [When to Consider SVMs](#when-to-consider-svms)
- [Summary](#summary)

## The Maximum-Margin Classifier: The Intuition

Imagine two classes of points that are linearly separable — you can draw a straight line between them. Many straight-line boundaries separate them correctly. Which one should you pick?

The SVM answer: pick the boundary that maximizes the **margin** — the distance from the boundary to the nearest training points on each side. Those nearest points are called **support vectors** because they define and "support" the boundary. All other training points do not affect where the boundary is placed.

[Figure: 2D scatter plot with two linearly separable classes. Three candidate decision boundaries shown. The SVM boundary in the middle, with the margin zone shaded and support vectors highlighted. The other two boundaries are shown closer to one class, with visibly smaller margins. Makes the geometric intuition immediate.]

Why maximum margin? Intuitively, a large-margin boundary generalizes better: a new point must be farther from the training data before it crosses the boundary. A boundary pressed close to one class is likely to misclassify new points from that class that land slightly differently from the training examples.

The constraint can be softened with a hyperparameter **C**: a larger C penalizes misclassifications more (tighter fit to training data, smaller margin). A smaller C allows some misclassifications in exchange for a wider margin. Tuning C is the primary hyperparameter task for linear SVMs.

---

## Kernels: Handling Non-Linear Boundaries

Many real datasets are not linearly separable. Mapping the data into a higher-dimensional feature space can sometimes separate the classes linearly there. The **kernel trick** computes the distances the SVM needs in that higher-dimensional space without explicitly constructing the expanded features — making it computationally feasible even when the expanded space has thousands or millions of dimensions.

The most common kernel is the **Radial Basis Function (RBF)** kernel, which measures similarity based on distance between points:

$$K(\mathbf{x}_i, \mathbf{x}_j) = \exp\!\left(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2\right)$$

The hyperparameter $\gamma$ controls the influence radius of each support vector. A small $\gamma$ makes each support vector's influence wide (smoother, more linear-looking boundary). A large $\gamma$ makes each support vector's influence narrow (complex locally fitted boundary, risk of overfitting).

[Figure: SVM with RBF kernel on a non-linearly separable dataset (two concentric circles). Contrasts a linear SVM that fails to separate with an RBF kernel SVM that finds a clean circular boundary. Side panels show the effect of too-small $\gamma$ (underfits) and too-large $\gamma$ (overfits).]

> **Tip:** With an RBF kernel, the two key hyperparameters are C (margin trade-off) and $\gamma$ (influence radius). Tune them together using cross-validation — they interact, and optimizing one while holding the other fixed can mislead you.

---

## When to Consider SVMs

| Situation | SVMs are a good fit |
|---|---|
| High-dimensional data (many more features than samples) | Yes — text classification, genomics |
| Clear margin of separation expected | Yes |
| Small to medium datasets | Yes |
| Large datasets (hundreds of thousands of rows) | No — training SVMs is slow at scale |
| Need for interpretable rules | No — SVMs are defined by support vectors, not readable rules |
| Tabular data with moderate dimensionality | Random forests are often simpler and comparable in accuracy |

SVMs were dominant in the early 2000s for tasks like text classification and bioinformatics. They remain competitive in low-to-medium-data settings with high-dimensional features. For most tabular data science tasks, gradient boosted trees or random forests have displaced them as the practical default.

> **Discussion:** You are classifying text documents into categories — technical reports vs. news articles — and have 10,000 documents with 50,000 TF-IDF features each. Would you reach for a random forest, an SVM, or another method first? What properties of the data inform your choice?

---

## Summary

- SVMs find the decision boundary that maximizes the margin between classes. Only the support vectors (nearest points to the boundary) determine the model.
- Hyperparameter C controls the margin-vs.-training-accuracy trade-off. The RBF kernel allows non-linear boundaries; $\gamma$ controls the influence radius of each support vector.
- SVMs work well in high-dimensional, small-to-medium-data settings. They are slow on large datasets and not interpretable as rule sets.
- For typical tabular data at scale, random forests are a simpler and often comparable alternative.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Statistical Significance](04-statistical-significance.md) | [Part Index](00-index.md) | [Main Index](../index.md)

Script v1.5 (2026-06-24) · FGN
