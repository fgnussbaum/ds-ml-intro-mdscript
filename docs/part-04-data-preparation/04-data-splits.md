> **Navigation:** [<-- Scaling and Imputation](03-scaling-imputation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Preparation Checklist -->](05-prep-checklist.md)

---

# Data Splits

**Requires**: [Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md)

**Motivation**: Before fitting any model, you face a foundational structural decision: Which data will the model actually see during its "training"? The answer shapes every evaluation number you will report. The model will always perform better on data it saw during training. So what does **honest** evaluation look like?

> In this nugget, you'll learn why a held-out test set is the only unbiased measure of generalization, what data leakage is and how to guard against it, and what that means for how you order your preprocessing steps.

## Table of Contents

- [The Train/Test Split](#the-traintest-split)
- [The Train/Validation/Test Split](#the-trainvalidationtest-split)
- [Data Leakage](#data-leakage)
- [Summary](#summary)

## The Train/Test Split

A model will always fit its training data to some degree. However, the final goal for model training is different: being able to generalize to new data.

The only honest reponse is to withhold some data before training begins and use it solely for evaluation. This held-out set is called the **test set**. To obtain it, we need to split the data.

The most common split ratio is 80/20, though it depends on the amount of available data.

For a good split, both training and test sets represent the data distribution well. You can verify this by comparing distribution statistics. For example, for [🖝 Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md) a simple sanity check could be to verify that the target variable's mean (for regression) or class distribution (for classification) is roughly the same for both sets.

> Always fix random states (seeds) when splitting data. This is important for reproducibility.

---

## The Train/Validation/Test Split

During modeling, you'll typically also need to make decisions like selecting the best set of features or tuning some model [🖝 Hyperparameter Optimization](../part-05-supervised-learning/06-hyperparameters.md). You'll want to make these decisions by comparing options in terms of their error on some kind of held-out data. However, this held-out data cannot be the test set: 

> The test set should **always** be consulted exactly once: after all modeling decisions are final.

If you allow the test set to influence any modeling choice, the test set error can no longer serve as a clean estimate of how the model will perform on truly unseen data.

The solution is to carve out a third partition before any work begins:

- **Training set**: to fit model parameters,
- **Validation set**: to compare alternatives and guide decisions,
- **Test set**: reserved for final evaluation only.

Typical split ratios are 60/20/20 or 70/15/15 (train/val/test), though again the right ratio depends on dataset size.

The most common reason to need a validation set is **hyperparameter tuning**: settings that control model behavior but lie outside what the optimizer can determine during training. [🖝 Hyperparameter Optimization](../part-05-supervised-learning/06-hyperparameters.md) covers this in full. For now, the rule to keep in mind is this:

> If you consult a held-out set to make a decision, it is not your test set.

---

## Data Leakage

Splitting the data establishes a standalone test set from which _no information ever_ enters the training process. Failure to maintain this separation is called data leakage:

> **Data leakage** is the problem that happens when **any** information from the test set transfers to the training set, making model evaluation unfair on the test set.

### Preprocessing Leakage

The most common form is **preprocessing leakage**: a transformation uses a statistic computed across multiple rows, and test rows contributed to that statistic. Scaling as in [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md) is the canonical example. If you compute the mean and standard deviation on the full dataset, test observations would shift those numbers, and your training data ends up transformed using statistics it should never have seen.

Consequently, the diagnostic question for any preparation step is:

> Does transforming a row require a statistic computed **across** rows, such as a mean or a percentile?

If yes, that statistic must be computed on training rows only, then applied to all splits. If no, each row transforms using only its own values and the full dataset is safe to use before splitting.

A reference for which pre-processing steps go before and after the split comes next in [🖝 Data Preparation Checklist](../part-04-data-preparation/05-prep-checklist.md).

### Feature Leakage

**Feature leakage** occurs in [🖝 Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md) when during [🖝 Feature Engineering](../part-04-data-preparation/01-feature-engineering.md) a feature is derived from the target variable or is only measurable after the outcome is known. Example: predicting hospital readmission while including "total length of current stay", a figure unavailable until the stay ends.

### Time-ordered Leakage

**Time-ordered leakage** occurs when a time series is shuffled before splitting. This would let the model train on data from the future. Always split chronologically. *See also: [🖝 Preparing Non-Tabular Data](../part-zz-appendix/02-beyond-tabular-prep.md).*

> **Discussion:** You are building a model to predict whether a loan applicant will default within the next year. A colleague suggests including the applicant's current savings balance, arguing it is a strong predictor. What questions would you ask to determine whether this constitutes leakage?

The diagnostic question is the same across all leakage forms: would this information be available at the moment of prediction in production?

---

## Summary

- A held-out test set is the only honest measure of how a model performs on new data.
- When any modeling decision depends on held-out performance, a third validation split protects the test set's integrity as the sole final benchmark.
- Data leakage occurs when test-set information influences training decisions. The most common form in tabular work is a preprocessing step whose statistic was computed on the full dataset before splitting.
- Steps that compute statistics across rows must follow the split. Steps that transform each row independently can precede it. The complete ordering is in [🖝 Data Preparation Checklist](../part-04-data-preparation/05-prep-checklist.md).

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Scaling and Imputation](03-scaling-imputation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Preparation Checklist -->](05-prep-checklist.md)

Script v1.3 (2026-06-09) · FGN
