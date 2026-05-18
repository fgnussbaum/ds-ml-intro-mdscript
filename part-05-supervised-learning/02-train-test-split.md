> **Navigation:** [<-- Supervised Learning](01-supervised-learning.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Linear Regression -->](03-linear-regression.md)

---

# Train/Test Split

**Requires**: [Supervised Learning](01-supervised-learning.md)

**Motivation**: 
Before fitting any model, you face a foundational structural decision: Which data will the model actually see during its "training"? The answer shapes every evaluation number you will report. The model will always perform better on data it saw during training. So what does **honest** evaluation look like?

> In this nugget, you'll learn why a carefully prepared held-out test set is the only unbiased measure of generalization. You'll learn what data leakage is and how to guard against it, and what that means for how you order your preprocessing steps.

## Table of Contents

- [Why You Need a Train/Test Split](#why-you-need-a-traintest-split)
- [Performing the Split](#performing-the-split)
- [Data Leakage](#data-leakage)
- [What Goes Before and After the Split](#what-goes-before-and-after-the-split)
- [Summary](#summary)

## Why You Need a Train/Test Split

A model will always fit its training data to some degree. However, the final goal for model training is different: being able to generalize to new data.

> A model that only memorizes the training data perfectly is useless in practice. It will fail when it sees new observations.

The only honest reponse to the matter is to withhold some data before training begins and use it solely for evaluation. This held-out set is called the **test set**. To obtain it, we need to split the data.

---

## Performing the Split

The most common split ratio is 80/20 (80% training, 20% test), though it really depends on the amount of available data. `sklearn` offers a convenient function for splitting data:

```Python
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)
```

Here, as introduced before in [🖝 Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md),
- `X` is the feature matrix, that is, your input columns, and
- `y` is the target variable, the one you intend to predict.

Also notice the `random_state` parameter above. Without setting it, you'd get a different split everytime you run the function. You set it to fix a particular "random" split.

> **Best Practice**: Even when you randomize something, use fixed random states (random seeds) to ensure full reproducibility of experimental results.

For a good split, both train and test data sets represent the underlying data distributions well. As a simple sanity check, verify that the target variable's mean (for regression) or class distribution (for classification) is roughly the same for both train and test data sets.

TODO: move to discussion of class imbalance
For example for classification, you may want the class distribution in the test data set the same. To enforce this, a safe option is a **stratified split**, which intuitively preserves the target `y` distribution by shuffling _within_ each class separately, then sampling proportionally from each "pile". This ensures that every subset mirrors the original class ratios.

```Python
train_X, test_X, train_y, test_y = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
```

---

## Data Leakage

Splitting the data aims at having a standalone test set from which _no information ever_ enters the training process. Failure in this regard is called data leakage:

> **Data leakage** is the problem that happens when **any** information from the test set transfers to the training set, making model evaluation unfair on the test set.

Data leakage can be as subtle as computing scaling parameters on the full dataset before splitting. In examples like that, the test set's distribution silently shapes the transformations applied to training data: This **can distort evaluation results**.

We discuss different types of data leakage in detail in [🖝 Overfitting and Generalization](../part-06-reflection/01-overfitting-and-generalization.md).
Here, let's check out how to prevent data leakage for tabular data specifically.

---

## What Goes Before and After the Split

For tabular data, a special type data leakage is pre-processing leakage. It happens when a transformation on training data uses a statistic **computed from multiple rows**, and test rows contribute to it.
Therefore, to decide whether any preparation step belongs before or after the split, ask:

> Does transforming a row require a statistic computed **across** rows, such as a mean or a median?

- **If yes**, that statistic must be computed on training rows only, then applied to both sets. Computing it on the full dataset lets test observations silently shape how training data is transformed.
- **If no**, each row transforms using _only its own values_, and the full dataset is safe to use before splitting.

Let's quickly sort everything we covered so far in before/after the split:

What goes **before** the split (each row transforms on its own values only):
- Constructing features like ratios, date decomposition, domain-derived columns: [🖝 Feature Engineering](../part-04-data-preparation/01-feature-engineering.md)
- Structural cleaning, type fixes, and categorical encoding (one-hot, ordinal, label): [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md)

What goes **after** the split (because a statistic gathered across rows is required):
- **Scaling**: mean and standard deviation are computed across all training rows
- **Imputation**: the fill value (e.g., median) is computed across all training rows
- **Outlier capping**: percentile thresholds are computed across all training rows

These three were covered in [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md).

---

## Summary

- A held-out test set is the only honest measure of how a model performs on new data. Establish it before any data-dependent preparation step.
- Data leakage occurs when test-set information influences training decisions. The most common form in tabular work is preprocessing steps whose statistics were computed on the full dataset before splitting.
- Steps that transform each row using only its own values (feature construction, structural cleaning, encoding) can safely precede the split. Steps that compute statistics across rows (scaling, imputation, outlier capping) must follow it.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Supervised Learning](01-supervised-learning.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Linear Regression -->](03-linear-regression.md)

Script v1.1 (2026-05-18) · FGN
