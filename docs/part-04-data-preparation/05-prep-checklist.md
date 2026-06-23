> **Navigation:** [<-- Data Splits](04-data-splits.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Preparation Best Practices -->](06-prep-principles.md)

---

# Data Preparation Checklist

**Motivation**: The previous nuggets covered specific preparation steps: structural cleaning, encoding, imputation, and scaling. The data preparation phase of [🖝 CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md) sits between data understanding and modeling, but when you face a real dataset, the order in which you apply those steps matters. Which operations are safe to run on the full dataset, and which must wait until after the data split?

> This checklist walks you through five preparation phases in the correct sequence: protecting your setup, structural cleaning, feature engineering, splitting the data, and statistic-estimating transformations. Steps in the last phase estimate statistics from data and must be fitted on training data only. The following companion nugget covers cross-cutting principles that apply at every phase: [🖝 Data Preparation Best Practices](../part-04-data-preparation/06-prep-principles.md).

## Table of Contents

- [Phase 1: Before touching data](#phase-1-before-touching-data)
- [Phase 2: Initial inspection and structural cleaning](#phase-2-initial-inspection-and-structural-cleaning)
- [Phase 3: Feature engineering](#phase-3-feature-engineering)
- [Phase 4: Splitting the data](#phase-4-splitting-the-data)
- [Phase 5: Statistic-estimating steps](#phase-5-statistic-estimating-steps)
- [Summary](#summary)

## Phase 1: Before touching data

- **Protect your raw data.** Place input files in a read-only location. All transformations should read from raw and write to a derived location.
- **Fix all random seeds.** Set `random_state` to a fixed integer for every operation that uses randomness. Do this before executing any code that splits or shuffles data.

---

## Phase 2: Initial inspection and structural cleaning

*Scope: full dataset, no statistics required.*

These operations do not use statistics from data for transformation, so they can safely be applied to the full dataset.

- **Consult the data dictionary/documentation.** Documenting a dataset is a responsibility of those who create it. For those working with data, reading the documentation is best practice. It should inform about column types, how data was recorded and encoded, and potential use of sentinel values.
- **Remove or reconcile duplicate records.** For survey data, exact duplicates can usually be dropped. Near-duplicates require judgment: do they represent different events or the same event recorded twice? Whether this step applies depends on the domain of the data.
- **Resolve wrong data types.** Coerce columns to their correct representation (`int`, `float`, `str`). Correct or remove erroneous data that prevents coercion.
- **Recode sentinel values to missing.** Replace values that encode missingness or special responses (e.g., `99` → `NaN`) before treating a column as numeric.
- **Correct or remove implausible entries.** An `age` of 200 or a score outside the declared scale range is a data-entry error. Recover the true value if possible; otherwise remove the row. Document removals.

*See also: [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md) and [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md).*

---

## Phase 3: Feature engineering

Feature construction is driven by what EDA revealed and by what you want to predict. The constructions below can be applied to the full dataset. Any construction that estimates statistics, such as group means, must be deferred to Phase 5. What you should do depends on the data. Typically you do things like:

- **Recode and binarize where EDA motivates it.** Skewed distributions, meaningful thresholds, and scale-direction inconsistencies are all triggers.
- **Build composite indexes for multi-item constructs.** If several columns measure the same underlying concept, average them into a single index. Verify that all source columns point in the same direction and use the same unit before averaging.
- **Group high-cardinality categorical columns before encoding.** Consider collapsing infrequent categories into an "other" bucket to avoid noise.
- **Engineer derived attributes when domain knowledge or EDA calls for it.** Ratios, products, and differences can produce features more informative than either source column alone. Single-column transformations, such as switching to a log scale, can also help. Before using any derived feature, ask: *would this value be known before the outcome is observed?* If not, drop it. This is target leakage: see [🖝 Data Preparation Best Practices](../part-04-data-preparation/06-prep-principles.md) for a deeper treatment.
- **Encode categorical attributes by attribute type.** Binary nominal attributes get a single 0/1 column. Multi-value nominal attributes get one-hot encoding: use $k - 1$ columns to avoid perfect collinearity. Ordinal attributes with a natural rank get ordered integers. Avoid ordinal encoding for nominal attributes: it implies an ordering that does not exist. See [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md).
- **Respect measurement scales.** Arithmetic on nominal attributes is meaningless. Averaging ordinal codes treats intervals as equal. Check the measurement scale of source columns before any derived operation. See [🖝 Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md).

*See also: [🖝 Feature Engineering](../part-04-data-preparation/01-feature-engineering.md).*

---

## Phase 4: Splitting the data

- **Split before any statistic-estimating step.** The data split must happen before any operation that computes statistics from data: means, medians, min/max, frequencies. Your test set must not influence any preprocessing decision. See [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md).

For [🖝 Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md), `sklearn` offers a convenient splitting function:

```python
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)
```

Apply twice if a validation set is also needed. Fixing `random_state` ensures reproducibility.

---

## Phase 5: Statistic-estimating steps

*Rationale: fit on training data only, apply to all splits.*

Apply the following three steps in sequence. Each step's output is the next step's input.

- **If necessary: Cap outliers if the model is sensitive to them.** Compute cap thresholds (e.g., 1st and 99th percentile) on the training set and apply to all splits. Capping must come before scaling: a single extreme value can otherwise compress all other values into a narrow band. Skip this step for tree-based models, which are not sensitive to extreme values. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md).
- **If necessary: Impute missing values, or delete incomplete rows.** Choose between listwise deletion (remove any row with a missing value) and imputation (substitute an estimate from the training set). Match the strategy to the missingness mechanism: choose mean or median for data missing completely at random (MCAR), and model-based imputation for data missing at random (MAR). Consider adding a binary indicator column that flags which rows were imputed. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md) and [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md).
- **Scale numeric features.** Distance-based models (k-NN), models like [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md), and neural networks are sensitive to feature scale; tree-based models are not. Z-score standardization is the safe default. Min-max scaling is appropriate only when bounded output is needed and outliers have already been handled. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md).

---

## Summary

- Preparation steps fall into two categories: those that require no statistics (structural cleaning, encoding, most feature construction) and those that estimate statistics from data (outlier capping, imputation, scaling). The first group can be applied to the full dataset. The second must be fitted on the training set only, then applied identically to all splits.
- The ordering within statistic-estimating steps matters: cap outliers first, then impute, then scale. Each step's output is the next step's input.
- Encode by attribute type: a single 0/1 column for binary nominal, one-hot ($k - 1$ columns) for multi-category nominal, ordered integers for ordinal. Group high-cardinality columns before encoding.
- Scale only when the model requires it. Tree-based models are not sensitive to feature scale; distance-based and regularized models are.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Data Splits](04-data-splits.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Preparation Best Practices -->](06-prep-principles.md)

Script v1.4.1 (2026-06-23) · FGN
