> **Navigation:** [<-- Data Preparation Checklist](05-prep-checklist.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part V: Supervised Learning -->](../part-05-supervised-learning/00-index.md)

---

# Data Preparation Best Practices

**Motivation**: With [🖝 Data Preparation Checklist](../part-04-data-preparation/05-prep-checklist.md) you got a guideline what to do and in what order. But just trying to encode data-science knowledge as "ordered steps" is not enough. It is also important to understand principles and avoid mistakes that can silently corrupt a project. What are recurring pitfalls that undermine data preparation, and how do you guard against them?

> This nugget covers cross-cutting principles that apply at every phase of data preparation: keeping raw data read-only, preventing data leakage, fixing random seeds, using pipelines to enforce preprocessing correctness, and documenting structural decisions. Violating any one of them can silently invalidate any project outcomes.

## Table of Contents

- [Keep raw data read-only and traceable](#keep-raw-data-read-only-and-traceable)
- [Prevent data leakage](#prevent-data-leakage)
- [Fix random seeds](#fix-random-seeds)
- [Use pipelines to enforce correctness](#use-pipelines-to-enforce-correctness)
- [Document structural decisions](#document-structural-decisions)
- [Summary](#summary)

## Keep raw data read-only and traceable

Your original input files should never be modified in place. Store raw data separately from processed data, and write all transformations as reproducible code that reads from raw and writes to a derived location. If something goes wrong upstream, you can always re-run the pipeline from scratch. If you have overwritten the raw data, you cannot. For projects where multiple derived datasets exist (different cleaning versions, different feature sets), use clearly named folders or a lightweight versioning tool so that a model artifact can always be traced back to the exact data it was trained on.

---

## Prevent data leakage

Data leakage occurs when information that would be unavailable at prediction time influences the training process, producing evaluation numbers that are artificially optimistic and collapse at deployment. [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md) covers the main forms: **preprocessing leakage** (statistics such as means or percentiles computed on the full dataset before splitting), **feature leakage** (features encoding information only available after the outcome is known), and **time-ordered leakage** (shuffling a time series before splitting, letting the model train on the future). The diagnostic question is always the same: would this information be available at the moment of prediction in production? If not, exclude it.

*See also: [🖝 Underfitting and Overfitting](../part-05-supervised-learning/04-under-overfitting.md) for why inflated evaluation numbers are dangerous, and [🖝 Generalization](../part-06-reflection/01-generalization.md) for evaluation strategies that keep the test set honest.*

---

## Fix random seeds

Any operation that involves randomness (data splits, shuffling steps inside cross-validation, and stochastic optimization) must be seeded with a fixed value. This gives random number generators a deterministic trajectory. The specific number does not matter. Without a fixed seed, results change on every run, making it impossible to reproduce either a result or a bug.

---

## Use pipelines to enforce correctness

When statistic-estimating steps are applied manually, the correct sequence (fit on training only, then apply to all splits) depends entirely on the programmer following a convention. **Pipelines**, as in `sklearn.pipeline`, enforce that separation structurally: the pipeline object remembers what it learned from training and applies only those learned parameters when transforming new data. This eliminates an entire category of subtle bugs. It also makes the trained artifact portable: a pipeline that bundles preprocessing and model can be applied to new data without reconstructing the transformation logic separately.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression()),
])

pipe.fit(X_train, y_train)   # scaler sees X_train only
pipe.predict(X_test)          # scaler uses train parameters — no leakage
```

---

## Document structural decisions

When you drop rows, recode a variable, choose a particular imputation strategy, or decide to bin a continuous attribute, write down why in a comment or a notebook cell. The choices that seem obvious today will be opaque in six months, and they will be opaque immediately to a colleague picking up the project. A one-sentence justification is enough: "Rows with `age > 100` dropped as likely data entry errors (n=3)".

---

## Summary

- Keep raw data read-only and write all transformations as reproducible code that reads from raw and writes to a derived location.
- Fix random seeds for every operation that involves randomness. Use pipelines to enforce fit/transform separation structurally rather than relying on programmer convention.
- Guard against data leakage in all its forms: preprocessing statistics computed before splitting, features derived from post-outcome information, and shuffled time series. The diagnostic question is always: would this be available at prediction time?
- Document every structural decision. A one-sentence justification is enough to make choices recoverable months later.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Data Preparation Checklist](05-prep-checklist.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part V: Supervised Learning -->](../part-05-supervised-learning/00-index.md)

Script v1.5 (2026-06-24) · FGN
